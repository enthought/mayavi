

.. _example_julia_set_decimation:

Julia set decimation example
--------------------------------------------------------------------


The Julia set, but with a decimated mesh: unnecessary triangles due to the
initial grid and not matching the geometry of the Julia set
are removed.

We first build the mesh, applying a warp_scalar filter to a
array2d_source, to warp the Julia set along the z direction.

Then when have to convert the rectangles in the mesh to triangles, in
order to apply the decimate_pro filter. This filter does the decimation,
and we can represent the result using surface modules.

The triangle-generation filter generates warnings: some polygons
are degenerate, as the grid has subdivided flat parts of the Julia
set.

We have shown in white the decimated mesh, and in black the non-decimated
one. The view is zoom to the center of the Julia set. If you turn of the
wireframes and zoom out, you can appreciate the quality of the
decimation.

In the specific case of decimating a surface warped from 2D data, it is
more efficient to use the greedy-terrain-decimator, see the
:ref:`example_canyon_decimation`.


.. image:: ../generated_images/example_julia_set_decimation.jpg
    :align: center



**Python source code:** :download:`julia_set_decimation.py`

.. literalinclude:: julia_set_decimation.py
    :lines: 26-


    