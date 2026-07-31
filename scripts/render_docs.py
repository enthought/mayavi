"""Regenerate the docs' generated content (used by the Docs CI workflow).

Renders the gallery images and the example pages, then the mlab reference, in
that order: the generators only emit an ``.. image::`` for a figure that already
exists on disk, so running them the other way round silently drops the
illustrations.
"""

import faulthandler
import os
import runpy
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / 'docs' / 'source'


def main():
    # rendering drives VTK through a Qt event loop, where a crash arrives as a
    # bare signal number and nothing says where -- which is how qt_embedding's
    # SIGSEGV stayed opaque for as long as it did.  The variable carries this
    # into the per-example children.
    faulthandler.enable()
    os.environ['PYTHONFAULTHANDLER'] = '1'

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
