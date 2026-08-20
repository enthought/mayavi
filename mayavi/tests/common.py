"""
Common code for mayavi tests.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) Enthought, Inc.
# License: BSD Style.
import os.path

from traits.api import HasTraits, Any, Event, Callable


def fail_instead_of_dialogs(set_attr=setattr):
    """Keep mayavi's error reporting from blocking (or hiding) a run.

    A failure inside a pipeline update -- including a warning raised as an
    error -- is swallowed by a bare ``except:`` and shown in a modal pyface
    box, so on a headed toolkit the run stops until someone clicks OK and the
    caller then carries on regardless.  Re-raise instead, and route the
    genuinely user-facing messages to the log only.

    Anything that reports through pyface directly rather than through
    `mayavi.core.common` would still get a box, so take the class those all
    end up in as well: every convenience function builds a `MessageDialog` and
    opens it, and an exception out of `open` says what the box would have said.

    `set_attr` is the hook the test fixture uses to get its changes undone
    again; the integration scripts and the docs renderer, which are whole
    processes of their own, take the default and keep them.

    This lives here rather than in conftest.py so that it can be imported
    without pytest -- the docs job installs no such thing.
    """
    from mayavi.core import common
    set_attr(common, 'reraise_exceptions', True)
    if common.pyface is not None:
        for name in ('error', 'warning', 'information'):
            set_attr(common.pyface, name,
                     lambda parent, msg, *args, _name=name, **kwargs:
                         common.logger.info('pyface.%s: %s', _name, msg))
        from pyface.message_dialog import MessageDialog

        def open_instead(self):
            raise RuntimeError(
                ' '.join(part for part in
                         (self.title, self.message, self.informative,
                          self.detail) if part))

        set_attr(MessageDialog, 'open', open_instead)


def fixpath(filename):
    """Given a relative file path it sets the path relative to this
    directory.  This allows us to run the tests from other directories
    as well.
    """
    return os.path.join(os.path.dirname(__file__), filename)


def get_example_data(fname):
    """Given a relative path to data inside the examples directory,
    obtains the full path to the file.
    """
    p = os.path.join('data', fname)
    return os.path.abspath(fixpath(p))


# (action, message prefix, category) for running an example.  One inventory for
# both places examples run: `run_example_headless` below applies it in Python,
# and `scripts/render_docs.py` both applies it and carries it into the gallery
# render's per-example children through `PYTHONWARNINGS`.  A filter whose
# message begins with whitespace cannot go here -- `warnings._setoption` strips
# the message `PYTHONWARNINGS` gives it, so it could never match in those
# children; those live in `render_examples.UNSETTABLE_WARNING_FILTERS`.
EXAMPLE_WARNING_FILTERS = (
    ('error', '', Warning),
    # unsatisfiable until pyface.workbench moves to apptools
    ('ignore', 'Workbench will be moved from pyface', PendingDeprecationWarning),
    # an example calling plt.show() is right; it is the renderer that has no
    # interactive matplotlib backend
    ('ignore', 'FigureCanvasAgg is non-interactive', UserWarning),
    # tvtk_segmentation.py wants vtkImageThreshold, whose replacement
    # vtkImageBinaryThreshold does not exist before VTK 9.7 -- see
    # tvtk/WORKAROUNDS.md
    ('ignore', 'Call to deprecated class vtkImageThreshold', DeprecationWarning),
)


def example_warning_filters():
    """`EXAMPLE_WARNING_FILTERS`, plus the ones this VTK needs."""
    filters = list(EXAMPLE_WARNING_FILTERS)
    # VTK's own numpy_support.vtk_to_numpy assigns to .shape, which NumPy 2.5
    # deprecated; fixed in 9.7, so keep it fatal there.  mayavi/tests/conftest.py
    # carries the same gate for the suites -- see tvtk/WORKAROUNDS.md
    from tvtk.common import vtk_major_version, vtk_minor_version
    if (vtk_major_version, vtk_minor_version) < (9, 7):
        filters.append(('ignore',
                        'Setting the shape on a NumPy array has been deprecated',
                        DeprecationWarning))
    return filters


# Examples that are meant for the mayavi2 application to import rather than to
# be executed, and say so by exiting non-zero under `__main__`.  Their module
# body is the part that does the work, so they get a name that skips the guard.
RUN_AS_MODULE = ('user_mayavi', 'zzz_reader')


def run_example_headless(filename):
    """Run one example script to completion, with nothing left blocking.

    An example ends by handing itself to an event loop -- ``mlab.show()``,
    ``GUI.start_event_loop()``, ``configure_traits()``, VTK's own
    ``vtkRenderWindowInteractor::Start`` -- which never returns.  Stub those
    out and the whole script still runs, which is all this is checking: that
    the example works against the installed VTK and ETS.

    The gallery renderer in ``docs/source/render_examples.py`` does the same
    for the examples it shoots a figure of, but with the capture machinery
    wrapped around it; ``examples/test_examples.py`` calls this for the rest.
    """
    import re
    import runpy
    import sys
    import warnings

    from traits.api import push_exception_handler

    # an example is expected to run warning-clean, as it is in the gallery
    # render.  This is the only thing making them fatal here: pytest's
    # filterwarnings applies to the process it runs in, not to this child.
    for action, message, category in example_warning_filters():
        warnings.filterwarnings(action, re.escape(message), category)
    # as in the renderer: an exception in a notification handler is otherwise
    # printed and swallowed, and the example "passes" with half its work undone
    push_exception_handler(reraise_exceptions=True)
    fail_instead_of_dialogs()
    # an example that also draws with matplotlib would block in pyplot.show()
    os.environ.setdefault('MPLBACKEND', 'Agg')

    from pyface.api import GUI
    from mayavi import mlab
    from tvtk.api import tvtk
    from tvtk.tools import visual

    GUI.start_event_loop = lambda self: None
    tvtk.RenderWindowInteractor.start = lambda self: None
    visual.show = lambda: None
    # mlab.show doubles as a decorator, and returning None from it would leave
    # the example calling None() rather than its own function
    mlab.show = lambda func=None, stop=False: func
    HasTraits.configure_traits = \
        lambda self, *args, **kwargs: self.edit_traits(kind='live')
    try:
        from pyface.qt import QtGui
    except Exception:
        pass        # a toolkit-less run has no loop to stop either
    else:
        for name in ('exec', 'exec_'):
            if hasattr(QtGui.QApplication, name):
                setattr(QtGui.QApplication, name, lambda *a, **kw: 0)

    filename = os.path.abspath(filename)
    # examples/mayavi/explorer names its own modules as envisage services, and
    # resolving one is an import: give the example the sys.path[0] that running
    # it as a script would have given it
    sys.path.insert(0, os.path.dirname(filename))
    name = os.path.splitext(os.path.basename(filename))[0]
    runpy.run_path(filename,
                   run_name=name if name in RUN_AS_MODULE else '__main__')
