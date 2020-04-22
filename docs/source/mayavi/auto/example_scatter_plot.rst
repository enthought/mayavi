

.. _example_scatter_plot:

Scatter plot example
--------------------------------------------


An example of plotting scatter points with Mayavi's core API.

This script creates a bunch of random points with random scalar data
and then shows these as a "scatter" plot of points.  The script
illustrates how to

 1. create a dataset easily using tvtk and numpy,

 2. use a created dataset in Mayavi and visualize it.

This example achieve the same functionnality as mlab's points3d
function ( :func:`mayavi.mlab.points3d`), but explicitly
creating the objects and adding them to the pipeline engine via the Mayavi
core API. Compared to using mlab, this method has the advantage of giving
more control on which objects are created, and there life cycle.

Run this script like so::

  $ mayavi2 -x scatter_plot.py

Alternatively it can be run as::

  $ python scatter_plot.py


**Python source code:** :download:`scatter_plot.py`

.. literalinclude:: scatter_plot.py
    :lines: 26-


    