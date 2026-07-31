"""
Render the examples to images and adds them to the documentation.
"""

# Standard library imports
import glob
import inspect
import os
import shutil
import subprocess
import sys
import tempfile
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
# the published image back and forth for no gain.  tvtk_in_mayavi draws
# overlapping translucent actors, and VTK composites those slightly differently
# about one run in five; see the note in CLAUDE.md for what was tried.
FLAKY_EXAMPLES = frozenset({'tvtk_in_mayavi'})

# Examples that cannot be rendered unattended, and why.
SKIP_EXAMPLES = {
    'wx_embedding': 'needs wxPython, which the docs do not install',
    'wx_mayavi_embed_in_notebook':
        'needs wxPython, which the docs do not install',
    'compute_in_thread': 'drives a worker thread, so the figure never settles',
    'poll_file': 'waits for a file to be edited',
    'standalone': 'starts the Envisage application and its event loop',
    'user_mayavi': 'is loaded by the mayavi2 application, not run on its own',
    'zzz_reader': 'registers a reader; there is nothing to show',
}

# No example takes anything like this long; it is here so that one which will
# never finish fails the build instead of hanging it.
EXAMPLE_TIMEOUT = 60


def keep_windows_in_background():
    """ Stops the windows we open from stealing focus and swallowing keystrokes.

        Rendering has to paint on screen, but nothing says it has to happen in
        front of whatever the user is doing: WA_ShowWithoutActivating keeps the
        window from taking focus, and WindowStaysOnBottomHint keeps it behind
        the other windows.  Both have to be set before the window is shown,
        hence patching setVisible rather than fixing up windows afterwards.
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
        # testAttribute keeps this to once per window: setWindowFlag on a
        # window that is already up hides and re-shows it, which would recurse
        if visible and self.isWindow() and not self.testAttribute(no_activate):
            self.setAttribute(no_activate, True)
            self.setWindowFlag(at_the_back, True)
        real_set_visible(self, visible)

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


def is_dialog_example(filename):
    """ Whether the example puts its scene in a TraitsUI dialog.
    """
    code_only = _code_without_comments(filename)
    return 'configure_traits(' in code_only or 'edit_traits(' in code_only


def _code_without_comments(filename):
    tokens = tokenize.generate_tokens(open(filename).readline)
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
        kwargs['kind'] = 'live'   # non-modal, so the example returns to us
        ui = real_edit(self, *args, **kwargs)
        created.append(ui)
        return ui

    def settle():
        settle_layout(created[-1].control if created else None)
        app = QtGui.QApplication.instance()
        for _ in range(5):
            app.processEvents()

    mlab.show = lambda func=None: None
    HasTraits.edit_traits = edit_traits
    HasTraits.configure_traits = lambda self, *a, **k: edit_traits(self)
    np.random.seed(0)
    try:
        exec(compile(open(filename).read(), filename, 'exec'),
             {'__name__': '__main__'})
        if not created:
            raise RuntimeError('%s opened no dialog' % filename)
        ui = created[-1]
        dialog = ui.control
        dialog.show()
        # the scene is only built once the window is really on screen, and
        # several examples plot from a scene.activated handler
        QtTest.QTest.qWaitForWindowExposed(dialog.windowHandle() or dialog, 5000)
        settle()

        obj = ui.context.get('object')
        if obj is not None:      # a few examples only plot when clicked
            for name in obj.trait_names():
                if isinstance(obj.trait(name).trait_type, Button):
                    setattr(obj, name, True)
            settle()

        scenes = _scene_widgets(dialog)
        if not scenes:
            raise RuntimeError('%s has no scene to capture' % filename)
        shot = dialog.grab()
        painter = QtGui.QPainter(shot)
        try:
            for widget in scenes:
                with tempfile.NamedTemporaryFile(suffix='.png') as rendered:
                    to_image = tvtk.WindowToImageFilter(
                        input=widget._RenderWindow, read_front_buffer=False)
                    writer = tvtk.PNGWriter(file_name=rendered.name)
                    writer.set_input_data(to_image.output)
                    to_image.update()
                    writer.write()
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


def capture_one(filename, image_file):
    """ Renders one example, the way that suits it.  Runs in the child.
    """
    keep_windows_in_background()
    if is_dialog_example(filename):
        capture_dialog(filename, image_file)
    else:
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
    subprocess.run([sys.executable, '-P', '-c', code],
                   check=True, timeout=EXAMPLE_TIMEOUT,
                   capture_output=True, text=True)


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
    if not (is_dialog_example(filename) or is_mlab_example(filename)):
        print("Skipping %s: it neither shows a figure nor opens a dialog"
              % filename)
        return
    print("Generating images for %s" % filename, flush=True)
    try:
        capture_in_subprocess(filename, image_file)
    except Exception as exc:
        # one broken example should not cost the gallery every later figure
        print("Could not render %s: %s: %s"
              % (filename, type(exc).__name__, exc))


def is_mlab_example(filename):
    tokens = tokenize.generate_tokens(open(filename).readline)
    code_only = ''.join([tok_content
                            for tok_type, tok_content, _, _, _  in tokens
                            if not token.tok_name[tok_type] in ('COMMENT',
                                                                'STRING')])
    return ('mlab.show()' in code_only)


def run_mlab_file(filename, image_file):
    ## XXX: Monkey-patch mlab.show, so that we keep control of the
    ## the mainloop
    old_show = mlab.show
    def my_show(func=None):
        pass
    mlab.show = my_show
    mlab.clf()
    np.random.seed(0)  # so an example plotting random data renders the same way
    e = mlab.get_engine()
    e.close_scene(mlab.gcf())
    exec(
        compile(open(filename).read(), filename, 'exec'),
        {'__name__': '__main__'}
    )
    # Give the widget the size the example asked for before capturing it.
    # Until the layout is applied the render window can still be at VTK's
    # 300x300 default, which is what happens on CI, where nothing else has
    # realised a window first.
    control = getattr(mlab.gcf().scene, '_vtk_control', None)
    if control is not None:
        settle_layout(control)
    mlab.savefig(image_file)
    size = mlab.gcf().scene.get_size()
    for scene in e.scenes:
        e.close_scene(scene)
    mlab.show = old_show


def extract_docstring(filename):
    # Extract a module-level docstring, if any
    lines = open(filename).readlines()
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
            self.render_example_page(open(os.path.join(self.out_dir,
                                            'example_%s.rst') %
                                     short_file_name, 'w'), index, file_details)
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
            self.render_example_page(open(os.path.join(self.out_dir,
                                        'example_%s.rst') %
                                     short_file_name, 'w'), index, file_details)
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
    example_gallery_file = open(os.path.join(out_dir, 'examples.rst'), 'w')

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
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))

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
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))
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
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))
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
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))
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
    example_files.sort(key=lambda name: len(open(name, 'r').readlines()))
    example_lister = ExampleLister(title="Misc examples",
                                   out_dir=out_dir)
    example_lister.render_all(example_gallery_file, example_files)



if __name__ == '__main__':
    render_examples()
