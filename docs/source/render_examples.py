"""
Render the examples to images and adds them to the documentation.
"""

# Standard library imports
import glob
import inspect
import os
import re
from io import StringIO
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import token, tokenize
import textwrap
import itertools

import numpy as np

# Enthought imports
from mayavi import mlab

# A global counter, for subsitutions.
global_counter = itertools.count()

EXAMPLE_DIR = '../../examples/mayavi'

# Examples whose figure differs from run to run, so that re-rendering would flip
# the published image back and forth for no gain.  The first two draw
# overlapping translucent actors, which VTK composites slightly differently from
# one run to the next: tvtk_in_mayavi about one run in five, and magnetic_field
# -- which culls front faces to fake transparency -- in three of the last four
# CI runs, a third of the image at a time.  wx_mayavi_embed_in_notebook is the
# odd one out: it is a screenshot of a wx window, and the notebook it draws
# lands differently often enough to have come back changed in two of the four
# CI runs after it was added, on the committed bytes both times, on main and on
# a branch that had not touched it.  See the note in CLAUDE.md for what was
# tried on the first two.
FLAKY_EXAMPLES = frozenset({'tvtk_in_mayavi', 'magnetic_field',
                            'wx_mayavi_embed_in_notebook'})

# Examples that cannot be rendered unattended, and why.
SKIP_EXAMPLES = {
    # Its two scenes are windows of their own rather than panels of the dialog
    # the example opens, and the first of them -- the one anything looking for
    # a scene finds first -- is the empty one it creates "just for kicks", so
    # shooting it would put a blank figure in the gallery.
    'standalone': 'builds its own Engine and puts each scene in its own window',
    'user_mayavi': 'is loaded by the mayavi2 application, not run on its own',
    'zzz_reader': 'registers a reader; there is nothing to show',
}

# No example takes anything like this long; it is here so that one which will
# never finish fails the build instead of hanging it.
EXAMPLE_TIMEOUT = 60

# ...except lucy, which on a cold cache downloads 307 MB and unpacks 523 MB from
# it before it can render.  Once the data is there it is as quick as the rest.
EXAMPLE_TIMEOUTS = {'lucy': 300}

# Examples that were meant to produce a figure and did not.  A failure only
# prints and moves on, so that one broken example does not cost the gallery
# every later figure -- which also means it leaves the committed image in place
# and looks, in the diff, exactly like an example that rendered unchanged.
# render_docs.py turns a non-empty list into a failed build at the very end.
RENDER_FAILURES = []


def keep_windows_in_background():
    """ Stops the windows we open from stealing focus and swallowing keystrokes.

        Rendering has to paint on screen, but nothing says it has to happen in
        front of whatever the user is doing: WA_ShowWithoutActivating keeps the
        window from taking focus, and WindowStaysOnBottomHint keeps it behind
        the other windows.  The attribute has to be set before the window is
        shown, hence patching setVisible rather than fixing up windows
        afterwards.

        The hint, though, goes on the QWindow *after* the show, not on the
        QWidget before it.  QWidget.setWindowFlag recreates the window's native
        window, and on X11 destroying a window destroys its children -- which
        takes out the X window a scene widget was created with.  Qt goes on
        handing out the dead id (winId() returns it, and neither create() nor
        another destroy()/create() replaces it), so the next paint has VTK ask
        the server about a window that is gone; XGetWindowAttributes fails,
        VTK's CreateAWindow carries on with a null XVisualInfo, and the
        glXCreateContext failsafe at the end of it dereferences the null.  That
        is what used to take qt_embedding -- the one example that shows a
        window it has already built a scene into -- down under Xvfb and on real
        X11 alike.  Setting the hint on the QWindow leaves the native windows
        alone and keeps the same behaviour.
    """
    from pyface.qt import QtCore, QtGui

    def enum(holder, name):
        # PyQt6 scopes these, PySide6 offers them both ways
        return getattr(QtCore.Qt, name, None) or getattr(holder, name)

    # traitsui's dialogs and pyface's windows raise themselves too
    QtGui.QWidget.raise_ = lambda self: None
    QtGui.QWidget.activateWindow = lambda self: None

    no_activate = enum(QtCore.Qt.WidgetAttribute, 'WA_ShowWithoutActivating')
    at_the_back = enum(QtCore.Qt.WindowType, 'WindowStaysOnBottomHint')
    real_set_visible = QtGui.QWidget.setVisible

    def set_visible(self, visible):
        # testAttribute keeps this to once per window, so that re-showing one
        # does not push the hint down a second time
        first_show = (visible and self.isWindow()
                      and not self.testAttribute(no_activate))
        if first_show:
            self.setAttribute(no_activate, True)
        real_set_visible(self, visible)
        if first_show:
            handle = self.windowHandle()
            if handle is not None:
                handle.setFlag(at_the_back, True)

    QtGui.QWidget.setVisible = set_visible


def should_render(short_file_name, image_file):
    """ Whether to (re-)render an example, honouring MAYAVI_RENDER_FLAKY.
    """
    if short_file_name not in FLAKY_EXAMPLES:
        return True
    if not os.path.exists(image_file):
        return True  # nothing committed to fall back on
    return os.environ.get('MAYAVI_RENDER_FLAKY', '').lower() \
        not in ('', '0', 'false', 'no')


def is_wx_example(filename):
    """ Whether the example is written against wx rather than Qt.

        Read from the source rather than kept in a list, so that a wx example
        added later is picked up on its own.  It cannot go through
        _code_without_comments, which joins tokens with nothing between them.
    """
    return re.search(r'^\s*(?:import|from)\s+wx\b', Path(filename).read_text(),
                     re.MULTILINE) is not None


def is_dialog_example(filename):
    """ Whether the example puts its scene in a TraitsUI dialog.
    """
    code_only = _code_without_comments(filename)
    return 'configure_traits(' in code_only or 'edit_traits(' in code_only


def is_app_example(filename):
    """ Whether the example runs itself inside the Mayavi2 application.

        ``@mayavi2.standalone`` starts Envisage and its event loop, so such an
        example has to be shot the way a dialog is -- with the Qt loop stubbed
        out -- rather than through ``run_mlab_file``, which would block in
        ``Mayavi.main()`` until the render timed out.  Its figure is the
        workbench window, not an mlab one.
    """
    return 'mayavi2.standalone' in _code_without_comments(filename)


def _code_without_comments(filename):
    tokens = tokenize.generate_tokens(StringIO(Path(filename).read_text()).readline)
    return ''.join([tok_content
                    for tok_type, tok_content, _, _, _ in tokens
                    if not token.tok_name[tok_type] in ('COMMENT', 'STRING')])


def settle_layout(widget):
    """ Makes Qt apply the geometry now, instead of when it gets round to
        delivering the LayoutRequest events it has posted.

        Every layout between the widget and its window has to be activated,
        not just the window's; mne/viz/backends/_qt.py does the same.
    """
    seen = set()
    while widget is not None and widget not in seen:
        layout = widget.layout()
        if layout is not None:
            layout.activate()
        seen.add(widget)
        widget = widget.parentWidget()


def _scene_widgets(widget, found=None):
    """ Every VTK render widget below ``widget``.

        Matched on the attribute rather than the class name, which differs
        between the QVTKRenderWindowInteractor subclasses.
    """
    from pyface.qt import QtGui

    found = [] if found is None else found
    if hasattr(widget, '_RenderWindow'):
        found.append(widget)
    for child in widget.children():
        if isinstance(child, QtGui.QWidget):
            _scene_widgets(child, found)
    return found


def _window_holding_a_scene():
    """ The visible top-level window that holds a scene, if there is one.

        For an example that runs inside the Mayavi2 application this is the
        workbench window: it opens no dialog we could have caught, so the only
        way to find its figure is to look at what ended up on screen.
    """
    from pyface.qt import QtGui

    for widget in QtGui.QApplication.topLevelWidgets():
        if widget.isVisible() and _scene_widgets(widget):
            return widget
    return None


class NoSceneInDialog(RuntimeError):
    """ Raised for an example whose dialog holds only controls, the scene
        being in an mlab figure of its own.
    """


def capture_dialog(filename, image_file):
    """ Shoots a TraitsUI example: the dialog, with its scenes painted in.

        QWidget.grab() draws the Qt widgets but not the native surface the VTK
        scene renders onto -- on macOS that leaves a black rectangle -- so each
        scene is rendered separately and pasted over its own place in the shot.
    """
    from pyface.qt import QtCore, QtGui, QtTest
    from traits.api import Button, HasTraits
    from tvtk.api import tvtk

    created = []
    real_edit, real_configure = HasTraits.edit_traits, HasTraits.configure_traits
    old_show = mlab.show

    def edit_traits(self, *args, **kwargs):
        # non-modal, so the example returns to us -- but an example that asks
        # to be embedded ('subpanel') means it, and prising the panel out into
        # a window of its own would shoot the panel instead of the window
        kwargs.setdefault('kind', 'live')
        ui = real_edit(self, *args, **kwargs)
        created.append(ui)
        return ui

    def settle():
        settle_layout(created[-1].control if created else None)
        app = QtGui.QApplication.instance()
        for _ in range(5):
            app.processEvents()

    # a few examples run the Qt loop themselves rather than through mlab.show
    real_execs = {name: getattr(QtGui.QApplication, name)
                  for name in ('exec', 'exec_')
                  if hasattr(QtGui.QApplication, name)}
    for name in real_execs:
        setattr(QtGui.QApplication, name, lambda *a, **k: 0)

    mlab.show = lambda func=None: None
    HasTraits.edit_traits = edit_traits
    HasTraits.configure_traits = lambda self, *a, **k: edit_traits(self)
    np.random.seed(0)
    try:
        exec(compile(Path(filename).read_text(), filename, 'exec'),
             {'__name__': '__main__', '__file__': os.path.abspath(filename)})
        ui = created[-1] if created else None
        if ui is not None:
            # for an embedded panel this is the window the example built round it
            dialog = ui.control.window()
        else:
            # an example driving the Mayavi2 application opens no dialog of its
            # own: its figure is whichever window Envisage put the scene in
            dialog = _window_holding_a_scene()
            if dialog is None:
                raise RuntimeError('%s opened no dialog' % filename)
        dialog.show()
        # the scene is only built once the window is really on screen, and
        # several examples plot from a scene.activated handler
        QtTest.QTest.qWaitForWindowExposed(dialog.windowHandle() or dialog, 5000)
        settle()

        obj = ui.context.get('object') if ui is not None else None
        if obj is not None:      # a few examples only plot when clicked
            for name in obj.trait_names():
                if isinstance(obj.trait(name).trait_type, Button):
                    setattr(obj, name, True)
            settle()

        scenes = _scene_widgets(dialog)
        if not scenes:
            raise NoSceneInDialog(filename)
        shot = dialog.grab()
        painter = QtGui.QPainter(shot)
        try:
            for widget in scenes:
                with tempfile.NamedTemporaryFile(suffix='.png') as rendered:
                    rw = widget._RenderWindow
                    to_image = tvtk.WindowToImageFilter(
                        input=rw, read_front_buffer=True)
                    writer = tvtk.PNGWriter(file_name=rendered.name)
                    writer.set_input_data(to_image.output)
                    # as in TVTKScene: the front buffer is the one VTK resolves
                    # the multisamples into properly, and holding the swap off
                    # refreshes it without presenting the frame
                    swap_buffers = rw.GetSwapBuffers()
                    rw.SwapBuffersOff()
                    try:
                        rw.Render()
                        to_image.update()
                        writer.write()
                    finally:
                        rw.SetSwapBuffers(swap_buffers)
                    painter.drawImage(
                        QtCore.QRect(widget.mapTo(dialog, QtCore.QPoint(0, 0)),
                                     widget.size()),
                        QtGui.QImage(rendered.name))
        finally:
            painter.end()
        shot.save(image_file)
    finally:
        for ui in created:
            ui.dispose()
        HasTraits.edit_traits = real_edit
        HasTraits.configure_traits = real_configure
        mlab.show = old_show
        for name, real in real_execs.items():
            setattr(QtGui.QApplication, name, real)


def _wx_scene_controls(window, found=None):
    """ Every VTK render widget below ``window``, wx side.

        VTK's wx interactor is what tvtk builds its scene on, and GetRenderWindow
        is the part of it worth matching on.
    """
    found = [] if found is None else found
    if hasattr(window, 'GetRenderWindow'):
        found.append(window)
    for child in window.GetChildren():
        _wx_scene_controls(child, found)
    return found


def _wx_scenes_on_screen(frame, filename, timeout=EXAMPLE_TIMEOUT / 4):
    """ Waits for the frame's scenes to be on screen, and returns them.

        The Qt path waits with QTest.qWaitForWindowExposed; wx has nothing
        equivalent, so wait on the thing that is actually wanted -- a scene the
        window server has put up -- rather than on a fixed number of turns
        round the event loop.  Update() then paints what is pending now, rather
        than whenever wx would next have got to it.

        A notebook's hidden tab is left out: it sits at the same place as the
        visible one, with an unrealised render window that would otherwise be
        scaled over the top of it.
    """
    import wx

    app = wx.GetApp()
    deadline = time.monotonic() + timeout
    while True:
        app.Yield()                 # processes everything currently pending
        scenes = [scene for scene in _wx_scene_controls(frame)
                  if scene.IsShownOnScreen()]
        if scenes and frame.IsShownOnScreen():
            frame.Layout()
            # IsShownOnScreen means the widget and its parents are shown, not
            # that the server has mapped and exposed the window -- there is no
            # wx qWaitForWindowExposed.  Update() paints the pending regions
            # synchronously, so the blit that follows has something to copy.
            frame.Update()
            return scenes
        if time.monotonic() >= deadline:
            raise NoSceneInDialog(filename)


def capture_wx_dialog(filename, image_file):
    """ Shoots a wx example: the frame, with its scenes painted in.

        The Qt counterpart with the toolkit swapped out -- MainLoop for exec_,
        WindowDC onto a MemoryDC for QWidget.grab, DrawBitmap for
        QPainter.drawImage -- and for the same reason: the blit copies the wx
        widgets but not the native surface VTK draws on.
    """
    import wx
    from tvtk.api import tvtk

    frames = []
    real_frame_init = wx.Frame.__init__
    real_main_loop = wx.App.MainLoop
    old_show = mlab.show

    def frame_init(self, *args, **kwargs):
        real_frame_init(self, *args, **kwargs)
        frames.append(self)

    wx.Frame.__init__ = frame_init
    wx.App.MainLoop = lambda self: None   # these examples run the loop
    mlab.show = lambda func=None: None
    np.random.seed(0)
    try:
        exec(compile(Path(filename).read_text(), filename, 'exec'),
             {'__name__': '__main__', '__file__': os.path.abspath(filename)})
        if not frames:
            raise RuntimeError('%s opened no frame' % filename)
        frame = frames[-1]
        frame.Show()
        scenes = _wx_scenes_on_screen(frame, filename)

        width, height = frame.GetSize()
        shot = wx.Bitmap(width, height)
        canvas = wx.MemoryDC(shot)
        canvas.Blit(0, 0, width, height, wx.WindowDC(frame), 0, 0)
        try:
            for control in scenes:
                render_window = control.GetRenderWindow()
                position = frame.ScreenToClient(control.GetScreenPosition())
                size = control.GetSize()
                with tempfile.NamedTemporaryFile(suffix='.png') as rendered:
                    to_image = tvtk.WindowToImageFilter(
                        input=render_window, read_front_buffer=True)
                    writer = tvtk.PNGWriter(file_name=rendered.name)
                    writer.set_input_data(to_image.output)
                    # as in TVTKScene: the front buffer is the one VTK resolves
                    # the multisamples into properly, and holding the swap off
                    # refreshes it without presenting the frame
                    swap_buffers = render_window.GetSwapBuffers()
                    render_window.SwapBuffersOff()
                    try:
                        render_window.Render()
                        to_image.update()
                        writer.write()
                    finally:
                        render_window.SetSwapBuffers(swap_buffers)
                    image = wx.Image(rendered.name)
                    if (image.GetWidth(), image.GetHeight()) != tuple(size):
                        # the render window is in pixels, the widget in points
                        image = image.Scale(size[0], size[1],
                                            wx.IMAGE_QUALITY_HIGH)
                    canvas.DrawBitmap(wx.Bitmap(image), position[0],
                                      position[1])
        finally:
            canvas.SelectObject(wx.NullBitmap)
        kind = (wx.BITMAP_TYPE_JPEG
                if image_file.lower().endswith(('.jpg', '.jpeg'))
                else wx.BITMAP_TYPE_PNG)
        shot.SaveFile(image_file, kind)
    finally:
        wx.Frame.__init__ = real_frame_init
        wx.App.MainLoop = real_main_loop
        mlab.show = old_show


def capture_one(filename, image_file):
    """ Renders one example, the way that suits it.  Runs in the child.
    """
    if is_wx_example(filename):
        # keep_windows_in_background is Qt-only, and pyface.qt need not even
        # import in a toolkit=wx child
        return capture_wx_dialog(filename, image_file)
    keep_windows_in_background()
    # an example that also draws with matplotlib would block in pyplot.show();
    # the environment only affects this child, not what users get
    os.environ.setdefault('MPLBACKEND', 'Agg')
    if is_dialog_example(filename) or is_app_example(filename):
        try:
            return capture_dialog(filename, image_file)
        except NoSceneInDialog:
            pass    # its dialog only holds controls; shoot the figure instead
    run_mlab_file(filename, image_file=image_file)


def capture_in_subprocess(filename, image_file):
    """ Renders one example in a child process, so that it can be killed.

        An example that reaches a Qt event loop never hands control back to the
        interpreter, so a signal-based timeout in this process would never be
        delivered -- only killing the process actually works.  Isolation also
        keeps one example's leftover scene state out of the next one's figure.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    code = ('import mayavi, tvtk.api, sys\n'          # bind before the doc
            'sys.path.insert(0, %r)\n'                # sources can shadow them
            'from render_examples import capture_one\n'
            'capture_one(%r, %r)\n' % (here, filename, image_file))
    short_name = os.path.splitext(os.path.basename(filename))[0]
    # the toolkit is per process, which is exactly what the isolation buys us:
    # a wx example gets a wx child and the rest of the gallery stays on Qt
    env = dict(os.environ)
    if is_wx_example(filename):
        env['ETS_TOOLKIT'] = 'wx'
    subprocess.run([sys.executable, '-P', '-c', code], check=True,
                   timeout=EXAMPLE_TIMEOUTS.get(short_name, EXAMPLE_TIMEOUT),
                   capture_output=True, text=True, env=env)


def capture_example(filename, short_file_name, image_file):
    """ Renders one example's figure, picking the way that suits it.

        Anything that cannot be rendered is left with whatever image is
        committed, so the gallery keeps its thumbnail either way.
    """
    if short_file_name in SKIP_EXAMPLES:
        print("Skipping %s: %s" % (filename, SKIP_EXAMPLES[short_file_name]))
        return
    if not should_render(short_file_name, image_file):
        print("Keeping the committed image for %s; it does not render "
              "reproducibly (set MAYAVI_RENDER_FLAKY=1 to redo it)" % filename)
        return
    if not (is_dialog_example(filename) or is_mlab_example(filename)
            or is_app_example(filename)):
        print("Skipping %s: it neither shows a figure nor opens a dialog"
              % filename)
        return
    print("Generating images for %s" % filename, flush=True)
    try:
        capture_in_subprocess(filename, image_file)
        if not os.path.exists(image_file):
            raise RuntimeError('rendered without leaving an image behind')
    except Exception as exc:
        # one broken example should not cost the gallery every later figure
        RENDER_FAILURES.append('%s: %s: %s'
                               % (filename, type(exc).__name__, exc))
        print("Could not render %s: %s: %s"
              % (filename, type(exc).__name__, exc))
        # the child's traceback is the only thing that says why, and it is not
        # part of str(CalledProcessError) -- without it a CI-only failure is
        # undiagnosable from the log
        for stream in (getattr(exc, 'stderr', None), getattr(exc, 'stdout', None)):
            if stream:
                text = stream if isinstance(stream, str) else stream.decode(
                    errors='replace')
                # faulthandler's dump ends with a list of every loaded
                # extension module, thousands of characters of it, which a
                # tail would show instead of the stack that matters
                lines = [line for line in text.strip().splitlines()
                         if not line.startswith('Extension modules:')]
                # both ends: a chained exception puts the cause that actually
                # explains the failure at the top, a crash dump puts the stack
                # at the bottom, and a tail alone loses the first of those
                if len(lines) > 70:
                    lines = (lines[:30] + ['    ... %d lines omitted ...'
                                           % (len(lines) - 70)] + lines[-40:])
                print(textwrap.indent('\n'.join(lines), '    '), flush=True)


def is_mlab_example(filename):
    tokens = tokenize.generate_tokens(StringIO(Path(filename).read_text()).readline)
    code_only = ''.join([tok_content
                            for tok_type, tok_content, _, _, _  in tokens
                            if not token.tok_name[tok_type] in ('COMMENT',
                                                                'STRING')])
    return ('mlab.show()' in code_only)


def realize_scene_window(scene):
    """ Puts a scene's window on screen at the size the example asked for.

        The render window only picks the size up from a resize event, so until
        the window is really on screen it stays at VTK's 300x300 default -- and
        a figure that was never shown at all reports 0x0, which is what
        mlab.screenshot cannot reshape.
    """
    control = getattr(scene, '_vtk_control', None)
    if control is None:
        return
    from pyface.qt import QtTest
    window = control.window()
    window.show()
    QtTest.QTest.qWaitForWindowExposed(window.windowHandle() or window, 5000)
    settle_layout(control)


def run_mlab_file(filename, image_file):
    ## XXX: Monkey-patch mlab.show, so that we keep control of the
    ## the mainloop
    old_show = mlab.show
    old_screenshot = mlab.screenshot

    def my_show(func=None):
        pass

    def my_screenshot(figure=None, *args, **kwargs):
        # an example that screenshots itself does so before anything has put
        # the figure on screen, where VTK still reports it as 0x0
        realize_scene_window((figure if figure is not None else mlab.gcf()).scene)
        return old_screenshot(figure, *args, **kwargs)

    mlab.show = my_show
    mlab.screenshot = my_screenshot
    mlab.clf()
    np.random.seed(0)  # so an example plotting random data renders the same way
    e = mlab.get_engine()
    e.close_scene(mlab.gcf())
    exec(
        compile(Path(filename).read_text(), filename, 'exec'),
        {'__name__': '__main__', '__file__': os.path.abspath(filename)}
    )
    realize_scene_window(mlab.gcf().scene)
    mlab.savefig(image_file)
    size = mlab.gcf().scene.get_size()
    for scene in e.scenes:
        e.close_scene(scene)
    mlab.show = old_show
    mlab.screenshot = old_screenshot


def extract_docstring(filename):
    # Extract a module-level docstring, if any
    lines = Path(filename).read_text().splitlines(keepends=True)
    start_row = 0
    if lines[0].startswith('#!'):
        lines.pop(0)
        start_row = 1

    docstring = ''
    first_par = ''
    li = lines.__iter__()
    li_next = li.__next__ if hasattr(li, '__next__') else li.next
    tokens = tokenize.generate_tokens(li_next)
    for tok_type, tok_content, _, (erow, _), _ in tokens:
        tok_type = token.tok_name[tok_type]
        if tok_type in ('NEWLINE', 'COMMENT', 'NL', 'INDENT', 'DEDENT'):
            continue
        elif tok_type == 'STRING':
            # cleandoc, not the raw string: a `""" Foo` opener would otherwise
            # indent the first line only, which rst reads as a block quote
            docstring = inspect.cleandoc(eval(tok_content))
            # If the docstring is formatted with several paragraphs, extract
            # the first one:
            paragraphs = '\n'.join(line.rstrip()
                                for line in docstring.split('\n')).split('\n\n')
            if len(paragraphs) > 0:
                first_par = paragraphs[0]
        break
    return docstring, first_par, erow+1+start_row


################################################################################
# class `ExampleLister`
################################################################################
class ExampleLister(object):
    """ Builds a rst-formatted list of examples from a list of files.
    """
    # Header template, for the example gallery.
    header_tpl = """
%(title)s
--------------------------------------------------

%(intro)s

.. toctree::
   :hidden:

%(toctree)s

.. A comment to split paragraphs

"""

    # Template used to create the example rst file
    example_rst_file_tpl = """

.. _example_%(short_file_name)s:

%(title)s example
--------------------------------------------

%(docstring)s

**Python source code:** :download:`%(short_file_name)s.py`

.. literalinclude:: %(short_file_name)s.py
    :lines: %(end_row)s-


    """

    # The title of the corresponding section in the example gallery.
    title = ''

    # The introductory text of the subsection
    intro =''

    def __init__(self, **kwargs):
        # Cheap unique hash for substitutions
        self._unique_hash = next(global_counter)
        for name, value in kwargs.items():
            setattr(self, name, value)


    def render_all(self, stream, file_list):
        """ Render the example list to the given
            stream (file-like object).
        """
        self._stream = stream
        files_details = self.render_header(file_list)
        for index, file_details in enumerate(files_details):
            filename, short_file_name, short_desc, title, docstring, \
                                                    end_row = file_details
            page = Path(self.out_dir, 'example_%s.rst' % short_file_name)
            with page.open('w') as stream:
                self.render_example_page(stream, index, file_details)
            self.gallery_entry(index, file_details)

        del self._stream


    def render_header(self, filenames):
        files_details = list()
        toctree = list()

        for filename in filenames:
            docstring, short_desc, end_row = extract_docstring(filename)
            short_file_name = os.path.basename(filename)[:-3]
            title = short_file_name.replace('_', ' ')
            title = title[0].upper() + title[1:]
            shutil.copy(filename,
                        os.path.join(self.out_dir, os.path.basename(filename)))


            toctree.append("""   example_%s.rst""" % short_file_name)
            files_details.append((filename, short_file_name, short_desc,
                                        title, docstring, end_row))

        toctree = '\n'.join(toctree)

        title = self.title
        intro = self.intro
        self._stream.write(self.header_tpl % locals())
        return files_details


    def render_example_page(self, stream, index, file_details):
        """ Render an individual example page.
        """
        filename, short_file_name, short_desc, title, docstring, end_row \
                                                                = file_details
        stream.write(self.example_rst_file_tpl % locals())


    def gallery_entry(self, index, file_details):
        """ Write the entry in the main example gallery file
            corresponding to the given file details.
        """
        filename, short_file_name, short_desc, title, docstring, \
                                end_row = file_details
        self._stream.write(
                "\n* :ref:`example_%(short_file_name)s`\n" % locals()
            )
        short_desc = short_desc.lstrip().rstrip()
        for line in short_desc.split('\n'):
            self._stream.write(4*" " + line.lstrip() + "\n")


################################################################################
# class `ImagesExampleLister`
################################################################################
class ImagesExampleLister(ExampleLister):
    """ ExampleLister that looks for thumbnails.
    """

    # Relative directory to images
    images_dir = 'mayavi/images/'

    def render_all(self, stream, file_list):
        self._stream = stream
        files_details = self.render_header(file_list)
        unique_hash = self._unique_hash
        for index, (filename, short_file_name, _, _, _, _) in \
                                        enumerate(files_details):
            image_file = os.path.join(self.images_dir,
                        'example_%(short_file_name)s.jpg' % locals())
            if os.path.exists(image_file):
                short_image_file = os.path.join(*(
                                    image_file.split(os.sep)[1:]))
                self._stream.write("""
.. |%(unique_hash)02i%(index)02i| image:: ../%(short_image_file)s
    :width: 150

            """ % locals())
            else:
                self._stream.write("""
.. |%(unique_hash)02i%(index)02i| raw:: html

    <br/>

            """ % locals())

        self._stream.write(2*('\n' + 7*"=" + " " + 45*"="))

        for index, file_details in enumerate(files_details):
            filename, short_file_name, short_desc, title, docstring, end_row = \
                                                                file_details
            page = Path(self.out_dir, 'example_%s.rst' % short_file_name)
            with page.open('w') as stream:
                self.render_example_page(stream, index, file_details)
            self.gallery_entry(index, file_details)

        self._stream.write("\n"+7*"=" + " " + 45*"=" + '\n')

        del self._stream


    def render_example_page(self, stream, index, file_details):
        """ Hijack this method to, optionally, render images.
        """
        # Jump one step up, and do not call ImagesExampleLister
        filename, short_file_name, short_desc, title, docstring, end_row = \
                                                                file_details
        image_file = os.path.join(self.images_dir,
                        'example_%(short_file_name)s.jpg' % locals())
        if os.path.exists(image_file):
            docstring += """

.. image:: ../%s
    :align: center

""" % os.path.join(*(image_file.split(os.sep)[1:]))

        file_details = \
            filename, short_file_name, short_desc, title, docstring, end_row

        stream.write(self.example_rst_file_tpl % locals())



    def gallery_entry(self, index, file_details):
        filename, short_file_name, short_desc, title, docstring, end_row = \
                                                                file_details
        # never break a word or a hyphenated one: a description mentioning
        # :ref:`data-structures-used-by-mayavi` would otherwise be split across
        # lines mid-label, leaving a reference that resolves to nothing
        short_desc = textwrap.wrap(short_desc, width=40,
                                   break_long_words=False,
                                   break_on_hyphens=False)
        unique_hash = self._unique_hash
        self._stream.write(
                ("\n|%(unique_hash)02i%(index)02i|" % locals()).ljust(9) +
                ":ref:`example_%(short_file_name)s`\n" % locals()
            )
        for line in short_desc:
            self._stream.write(9*" " + line.lstrip() + "\n")

################################################################################
# class `MlabExampleLister`
################################################################################
class RenderedExampleLister(ImagesExampleLister):
    """ ExampleLister that renders each example's figure rather than only
        looking for one already on disk.
    """

    render_images = False

    images_dir = 'mayavi/generated_images'

    def render_example_page(self, stream, index, file_details):
        """ Hijack this method to, optionally, render images.
        """
        filename, short_file_name, short_desc, title, docstring, end_row = \
                                                            file_details
        if self.render_images:
            image_file = os.path.join(self.images_dir, 'example_%s.jpg' \
                                    % short_file_name)
            capture_example(filename, short_file_name, image_file)
        ImagesExampleLister.render_example_page(self, stream,
                                                index, file_details)


################################################################################
# class `MlabExampleLister`
################################################################################
class MlabExampleLister(RenderedExampleLister):

    header_tpl = """
Mlab functions gallery
----------------------

These are the examples of the mlab plotting functions. They are
copied out here for convenience. Please refer to the corresponding
section of the user guide for more information (
:ref:`mlab_plotting_functions`).

.. currentmodule:: mayavi.mlab

+------------------+-------------------------+----------------------+
| :func:`plot3d`   | :func:`points3d`        | :func:`imshow`       |
|                  |                         |                      |
| |plot3d.jpg|     | |points3d.jpg|          | |imshow.jpg|         |
+------------------+-------------------------+----------------------+
| :func:`surf`     | :func:`contour_surf`    | :func:`mesh`         |
|                  |                         |                      |
| |surf.jpg|       | |contour_surf.jpg|      | |mesh.jpg|           |
+------------------+-------------------------+----------------------+
| :func:`barchart` | :func:`triangular_mesh` | :func:`contour3d`    |
|                  |                         |                      |
| |barchart.jpg|   | |triangular_mesh.jpg|   | |contour3d.jpg|      |
+------------------+-------------------------+----------------------+
| :func:`quiver3d` | :func:`flow`            | :func:`volume_slice` |
|                  |                         |                      |
| |quiver3d.jpg|   |  |flow.jpg|             | |volume_slice.jpg|   |
+------------------+-------------------------+----------------------+

.. |plot3d.jpg| image:: ../generated_images/mayavi_mlab_plot3d.jpg
     :width: 150

.. |points3d.jpg| image:: ../generated_images/mayavi_mlab_points3d.jpg
     :width: 150

.. |imshow.jpg| image:: ../generated_images/mayavi_mlab_imshow.jpg
     :width: 150

.. |contour_surf.jpg| image:: ../generated_images/mayavi_mlab_contour_surf.jpg
     :width: 150

.. |triangular_mesh.jpg| image:: ../generated_images/mayavi_mlab_triangular_mesh.jpg
     :width: 150

.. |surf.jpg| image:: ../generated_images/mayavi_mlab_surf.jpg
     :width: 150

.. |mesh.jpg| image:: ../generated_images/mayavi_mlab_mesh.jpg
     :width: 150

.. |barchart.jpg| image:: ../generated_images/mayavi_mlab_barchart.jpg
     :width: 150

.. |contour3d.jpg| image:: ../generated_images/mayavi_mlab_contour3d.jpg
     :width: 150

.. |quiver3d.jpg| image:: ../generated_images/mayavi_mlab_quiver3d.jpg
     :width: 150

.. |flow.jpg| image:: ../generated_images/mayavi_mlab_flow.jpg
     :width: 150

.. |volume_slice.jpg| image:: ../generated_images/mayavi_mlab_volume_slice.jpg
     :width: 150


Advanced mlab examples
-----------------------

.. toctree::
   :hidden:

%(toctree)s

"""

    example_rst_file_tpl = """

.. _example_%(short_file_name)s:

%(title)s example
--------------------------------------------------------------------

%(docstring)s

**Python source code:** :download:`%(short_file_name)s.py`

.. literalinclude:: %(short_file_name)s.py
    :lines: %(end_row)s-


    """




################################################################################
# Main entry point
def render_examples(render_images=False, out_dir='mayavi/auto'):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    example_gallery_file = StringIO()

    example_gallery_file.write("""

.. _example_gallery:

Example gallery
=================

""")

    ##########################################################################
    # Mlab examples
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        'mlab', '*.py'))
                    if is_mlab_example(filename)]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: (len(Path(name).read_text().splitlines()), name))

    mlab_example_lister = MlabExampleLister(render_images=render_images,
                                        out_dir=out_dir,
                                        images_dir='mayavi/generated_images')
    if render_images:
        pass
        # XXX: Add logics to deal with rerendering examples cleverly

    mlab_example_lister.render_all(example_gallery_file, example_files)

    ##########################################################################
    # Interactive application examples
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        'interactive', '*.py'))]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: (len(Path(name).read_text().splitlines()), name))
    example_lister = RenderedExampleLister(
            render_images=render_images,
            images_dir='mayavi/generated_images',
            title="Interactive examples",
            out_dir=out_dir,
            intro="""

Examples showing how to use the interactive features of Mayavi, either
via the mayavi2 application, or via specially-crafted dialogs and
applications.
    """)
    example_lister.render_all(example_gallery_file, example_files)

    ##########################################################################
    # Advanced visualization examples
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        'advanced_visualization', '*.py'))]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: (len(Path(name).read_text().splitlines()), name))
    example_lister = RenderedExampleLister(
            render_images=render_images,
            images_dir='mayavi/generated_images',
            title="Advanced visualization examples",
            out_dir=out_dir,
            intro="""
Data visualization using the core Mayavi API, object-oriented, and with
more fine control than mlab.

    """)
    example_lister.render_all(example_gallery_file, example_files)

    ##########################################################################
    # Data interaction examples
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        'data_interaction', '*.py'))]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: (len(Path(name).read_text().splitlines()), name))
    example_lister = RenderedExampleLister(
            render_images=render_images,
            images_dir='mayavi/generated_images',
            title="Data interaction examples",
            out_dir=out_dir,
            intro="""
Examples showing how you can query and interact with the data.

    """)
    example_lister.render_all(example_gallery_file, example_files)

    ##########################################################################
    # The remaining files
    example_files = [ filename
                    for filename in glob.glob(os.path.join(EXAMPLE_DIR,
                        '*.py'))]
    # Sort by file length (gives a measure of the complexity of the
    # example)
    example_files.sort(key=lambda name: (len(Path(name).read_text().splitlines()), name))
    example_lister = ExampleLister(title="Misc examples",
                                   out_dir=out_dir)
    example_lister.render_all(example_gallery_file, example_files)


    Path(out_dir, 'examples.rst').write_text(example_gallery_file.getvalue())


if __name__ == '__main__':
    render_examples()
