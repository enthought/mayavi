Building documentation
=========================

Install the documentation requirements and an editable Mayavi, then build
from the top-level directory::

    pip install --group docs -ve ".[app]"
    make -C docs site

The site is written to ``docs/build/site``.  To regenerate the example gallery
images and the mlab reference first, run ``python scripts/render_docs.py``.

Publishing the docs
===================

There is nothing to do by hand: every push to ``main`` builds the docs and
deploys them to https://docs.enthought.com/mayavi/ (see
``.github/workflows/docs.yml``).
