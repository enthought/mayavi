Creating data for Mayavi
========================


This section of the user guide will be improved later.  For now, the
following two presentations best describe how one can create data
objects or data files for Mayavi and TVTK.

 * Presentation on TVTK and Mayavi2 for course at IIT Bombay

   https://svn.enthought.com/enthought/attachment/wiki/Mayavi/tvtk_mayavi2.pdf

   This presentation provides information on graphics in general, 3D
   data representation, creating VTK data files, creating datasets
   from numpy in Python, and also about mayavi.

 * Presentation on making TVTK datasets using numpy arrays made for SciPy07.

   https://svn.enthought.com/enthought/attachment/wiki/Mayavi/tvtk_datasets.pdf

   This presentation focuses on creating TVTK datasets using numpy
   arrays.


There are several examples in the mayavi sources that highlight the
creation of the most important datasets from numpy arrays.  These may
be found in the ``examples`` directory.  Specifically they are:

   * ``polydata.py``:  Demonstrates how to create Polydata datasets
     from numpy arrays and visualize them in mayavi.

   * ``structured_points2d.py``: Demonstrates how to create a 2D
     structured points (or image data) dataset from numpy arrays and
     visualize them in mayavi.  This is basically a square of
     equispaced points.

   * ``structured_points3d.py``: Demonstrates how to create a 3D
     structured points (or image data) dataset from numpy arrays and
     visualize them in mayavi.  This is a cube of points that are
     regularly spaced.

   * ``structured_grid.py``: Demonstrates the creation and
     visualization of a 3D structured grid.

   * ``unstructured_grid.py``: Demonstrates the creation and
     visualization of an unstructured grid.

These scripts may be run like so::

  $ mayavi2 -x structured_grid.py

or better yet, all in one go like so::

  $ mayavi2 -x polydata.py -x structured_points2d.py \
  > -x structured_points3d.py -x structured_grid.py -x unstructured_grid.py
 

.. Creating datasets from numpy arrays
   -----------------------------------
   
   Add content here from the presentations.

.. VTK Data files
   --------------

   Add content here from the presentations.

..
   Local Variables:
   mode: rst
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:

