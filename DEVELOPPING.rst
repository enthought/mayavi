
Building documentation
=========================

In the top-level directory, run::

    python setup.py build_docs

Uploading docs on the web page
=================================

The docs live on their own gh-pages git branch. So to update, starting
from the root of the project here is what you do::

   # Recompile docs
   cd docs/
   make html
   # Copy to other branch
   cd ..
   git checkout gh-pages
   cp -r docs/build/tvtk/html/* tvtk/
   cp -r docs/build/mayavi/html/* mayavi/
   git add tvtk mayavi
   # Commit and push new docs
   git commit -a -m "Updated docs"
   git push
   # Return to master branch
   git checkout master


