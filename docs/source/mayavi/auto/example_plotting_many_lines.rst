

.. _example_plotting_many_lines:

Plotting many lines example
--------------------------------------------------------------------


This examples shows how many lines can be grouped together in a single
object, for convenience and efficiency.

We want to plot a large number of lines. We could use mlab.plot3d for
this, but it will create an object for each line, this will be
inefficient. This example shows how to create one object comprised of
many lines.

The underlying idea is the same as that used to plot graphs (see for
instance :ref:`example_flight_graph`): create a set of points, and
specify explicitly the connectivity between them. First we create the
set of unconnected point (the underlying data structure is a
:ref:`poly_data`) using `mlab.pipeline.scalar_scatter`. To add the
connections, we need to keep track of which point is connected to which.
As we only have lines, this is fairly easy: in a line, each point is
connected to the following one.



.. image:: ../generated_images/example_plotting_many_lines.jpg
    :align: center



**Python source code:** :download:`plotting_many_lines.py`

.. literalinclude:: plotting_many_lines.py
    :lines: 20-


    