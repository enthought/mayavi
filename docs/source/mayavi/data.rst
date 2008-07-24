.. _creating-data-for-mayavi:

Creating data for Mayavi
========================

Describing data in three dimension in the general case is a complex
problem. Mayavi helps you focus on your visualization work and not worry
too much about the underlying data structures, for instance using mlab
(see :ref:`simple-scripting-with-mlab`). However, if you want to create
data for a more efficient visualization, it helps to understand the VTK
data structures that Mayavi uses.

VTK data structures
--------------------

The 5 VTK structures used are the following (ordered by the cost of
visualizing them).:

================== ============= =========================== ============================================================
VTK name            Connectivity  Suitable for                Required information
================== ============= =========================== ============================================================
ImageData           Implicit      Volumes and surfaces        3D data array and spacing along each axis
RectilinearGrid     Implicit      Volumes and surfaces        3D data array and 1D array of spacing for each axis
StructuredGrid      Implicit      Volumes and surfaces        3D data array and 3D position arrays for each axis
PolyData            Explicit      Points, lines and surfaces  x, y, z, positions of vertices and arrays of surface Cells
UnstructuredGrid    Explicit      Volumes and surfaces        x, y, z positions of vertices and arrays of volume Cells
================== ============= =========================== ============================================================

**Implicit connectivity**: connectivity or positioning is implicit. In
this case the data is considered as arranged on a lattice-like structure,
with equal number of layers in each direction, x increasing first along
the array, then y and finally z.

**Cell data and point data**: Each VTK dataset is defined by vertices and
cells, explicitly or implicitly. The data, scalar or vector, can be
positioned either on the vertices, in which case it is called point data,
or associated with a cell, in which case it is called cell data.


**Description of the datasets**:

:ImageData:
  This dataset is made of data points positioned on an orthogonal grid,
  with constant spacing along each axis. The position of the data points
  are inferred from their position on the data array (implicit
  positioning), an origin and a spacing between 2 slices along each axis.
  In 2D, this can be understood as a raster image. 

  .. image:: image_data.png

:RectilinearGrid:
  This dataset is made of data points positioned on an orthogonal grid, 
  with arbitrary spacing along the various axis. The position of the data
  points are inferred from their position on the data array, an
  origin and the list of spacings of each axis.

  .. image:: rectilinear_grid.png

:StructuredGrid:
  This dataset is made of data points positioned on arbitrary grid: each
  point is connected to its nearest neighbors on the data array. The
  position of the data points are fully described by 1 coordinate
  arrays, specifying x, y and z for each point.

  .. image:: structured_grid.png

:PolyData:
  This dataset is made of arbitrarily positioned data points that can
  be connected to form lines, or grouped in polygons to from surfaces
  (the polygons are broken up in triangles). Unlike the other datasets, 
  this one cannot be used to describe volumetric data.

  .. image:: poly_data.png

:UnstructuredGrid:
  This dataset is the most general dataset of all. It is made of data 
  points positioned arbitrarily. The connectivity between data points 
  can be arbitrary (any number of neighbors). It is described by
  specifying connectivity, defining volumetric cells made of adjacent 
  data points.

  .. image:: unstructured_grid.png

External references
--------------------

This section of the user guide will be improved later.  For now, the
following two presentations best describe how one can create data
objects or data files for Mayavi and TVTK.

 * Presentation on TVTK and Mayavi2 for course at IIT Bombay

   https://svn.enthought.com/enthought/attachment/wiki/MayaVi/tvtk_mayavi2.pdf

   This presentation provides information on graphics in general, 3D
   data representation, creating VTK data files, creating datasets
   from numpy in Python, and also about mayavi.

 * Presentation on making TVTK datasets using numpy arrays made for SciPy07.

   https://svn.enthought.com/enthought/attachment/wiki/MayaVi/tvtk_datasets.pdf

   This presentation focuses on creating TVTK datasets using numpy
   arrays.


Datasets creation examples
---------------------------

There are several examples in the mayavi sources that highlight the
creation of the most important datasets from numpy arrays.  These may
be found in the ``examples`` directory.  Specifically they are:

   * ``datasets.py`` : Generate a simple example for each type of VTK dataset.

   * ``polydata.py``:  Demonstrates how to create Polydata datasets
     from numpy arrays and visualize them in mayavi.

   * ``structured_points2d.py``: Demonstrates how to create a 2D
     structured points (an ImageData) dataset from numpy arrays and
     visualize them in mayavi.  This is basically a square of
     equispaced points.

   * ``structured_points3d.py``: Demonstrates how to create a 3D
     structured points (an ImageData) dataset from numpy arrays and
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

