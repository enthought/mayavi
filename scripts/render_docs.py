"""Regenerate the docs' generated content (used by the Docs CI workflow).

Renders the gallery images and the example pages, then the mlab reference, in
that order: the generators only emit an ``.. image::`` for a figure that already
exists on disk, so running them the other way round silently drops the
illustrations.
"""

import os
import runpy
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / 'docs' / 'source'


def main():
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


if __name__ == '__main__':
    sys.exit(main())
