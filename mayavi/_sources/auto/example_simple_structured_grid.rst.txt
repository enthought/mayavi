

.. _example_simple_structured_grid:

Simple structured grid example
--------------------------------------------------------------------


An example creating a structured grid data set from numpy arrays using TVTK
and visualizing it using mlab.

In this example, we create a structured-grid data set: we describe
data, both scalar and vector, lying on a structured-grid, ie a grid where
each vertex has 6 neighbors. For this we directly create a
StructuredGrid tvtk object, rather than using the mlab.pipeline source
functions, as it gives us more control.

To visualize the resulting dataset, we apply several modules, using the
mlab.pipeline interface (see :ref:`controlling-the-pipeline-with-mlab-scripts`)


.. image:: ../generated_images/example_simple_structured_grid.jpg
    :align: center



**Python source code:** :download:`simple_structured_grid.py`

.. literalinclude:: simple_structured_grid.py
    :lines: 14-


    