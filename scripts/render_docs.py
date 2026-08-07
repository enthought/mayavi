"""Regenerate the docs' generated content (used by the Docs CI workflow).

Renders the gallery images and the example pages, then the mlab reference, in
that order: the generators only emit an ``.. image::`` for a figure that already
exists on disk, so running them the other way round silently drops the
illustrations.
"""

import faulthandler
import os
import re
import runpy
import sys
import warnings
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / 'docs' / 'source'

# (action, message prefix, category) -- the examples and the generators run as
# plain scripts, so this is the only thing making their warnings fatal; the
# Makefiles' -W covers Sphinx's own diagnostics, not Python's.
# Filters whose message begins with whitespace cannot go here -- PYTHONWARNINGS
# carries this list into the children and warnings._setoption strips it.  Those
# live in render_examples.UNSETTABLE_WARNING_FILTERS.
WARNING_FILTERS = (
    ('error', '', Warning),
    # third-party, reached through envisage's plugin manager and sphinxcontrib
    ('ignore', 'pkg_resources is deprecated as an API', UserWarning),
    ('ignore', 'Deprecated call to `pkg_resources.declare_namespace',
     DeprecationWarning),
    # unsatisfiable until pyface.workbench moves to apptools
    ('ignore', 'Workbench will be moved from pyface', PendingDeprecationWarning),
    # an example calling plt.show() is right; it is this renderer that has no
    # interactive matplotlib backend
    ('ignore', 'FigureCanvasAgg is non-interactive', UserWarning),
)


def apply_warning_filters():
    """Make warnings fatal, here and in the per-example child processes.

    `capture_in_subprocess` discards a child's output unless it exits
    non-zero, so a warning there is only ever seen by being raised.
    """
    filters = list(WARNING_FILTERS)
    # VTK's own numpy_support.vtk_to_numpy assigns to .shape, which NumPy 2.5
    # deprecated; fixed in 9.7, so keep it fatal there.  mayavi/tests/conftest.py
    # carries the same gate for the suites -- see tvtk/WORKAROUNDS.md
    from tvtk.common import vtk_major_version, vtk_minor_version
    if (vtk_major_version, vtk_minor_version) < (9, 7):
        filters.append(('ignore',
                        'Setting the shape on a NumPy array has been deprecated',
                        DeprecationWarning))
    for action, message, category in filters:
        warnings.filterwarnings(action, re.escape(message), category)
    # PYTHONWARNINGS matches the message as a literal prefix, not a regex
    os.environ['PYTHONWARNINGS'] = ','.join(
        ':'.join((action, message, category.__name__))
        for action, message, category in filters)


def main():
    # rendering drives VTK through a Qt event loop, where a crash arrives as a
    # bare signal number and nothing says where -- which is how qt_embedding's
    # SIGSEGV stayed opaque for as long as it did.  The variable carries this
    # into the per-example children.
    faulthandler.enable()
    os.environ['PYTHONFAULTHANDLER'] = '1'
    apply_warning_filters()

    # render_images.py imports its sibling render_examples, so docs/source has
    # to go on sys.path -- but docs/source/mayavi and docs/source/tvtk then
    # shadow the installed packages, as namespace packages win over an editable
    # install's finder no matter where on the path they turn up.  Binding the
    # real ones first settles it; neither import builds the QApplication, so
    # render_images.py can still set QT_SCALE_FACTOR when it runs.
    import mayavi  # noqa: F401
    import tvtk.api  # noqa: F401
    sys.path.insert(0, str(SOURCE))

    # both generators resolve their inputs relative to the working directory
    os.chdir(SOURCE)
    runpy.run_path(str(SOURCE / 'render_images.py'), run_name='__main__')

    os.chdir(REPO)
    runpy.run_path(str(REPO / 'mlab_reference.py'), run_name='__main__')

    # An example that fails to render keeps its committed image, so the run
    # looks clean and the figure quietly goes stale -- which is how lucy ended
    # up shipping an image CI had never produced.  The report is written rather
    # than raised so that the site and its images are still built and uploaded:
    # a red run is exactly when you want to look at them.
    import render_examples
    failures = render_examples.RENDER_FAILURES
    (REPO / 'render_failures.txt').write_text(
        ''.join(line + '\n' for line in failures))
    if failures:
        print('\n%d example(s) were meant to render and did not:'
              % len(failures), file=sys.stderr)
        for line in failures:
            print('  ' + line, file=sys.stderr)


if __name__ == '__main__':
    sys.exit(main())
