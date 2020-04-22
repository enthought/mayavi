

.. _example_probe_filter:

Probe filter example
--------------------------------------------


Using the probe filter to visualize a scalar field along an arbitrary
surface.

This example shows how a data set can be 'projected' (or interpolated) on
another given source using the probe filter. It is also an example of a
complex VTK pipeline and shows how to inspect it with the
PipelineBrowser.

In this example, a function is sampled on a regular grid and can be
visualized using an ImagePlaneWidget. The function we are interested is
independent of the distance to the origin and a function only of the
angle. This is why it may be interesting to visualize its value sampled
on a sphere center at the origin, but we have the data sampled throughout
the volume on a regular grid.

We create a sphere with the BuiltinSurface source and use the VTK
ProbeFilter to sample the data on this surface. The ProbeFilter takes one
input, which is the data structure to project the data on, and a
'source', which is where the data values come from.

We need to use the UserDefined filter to insert this VTK filter in the
Mayavi pipeline (see :ref:`using_userdefined_filter` as well as
:ref:`example_image_cursor_filter` and :ref:`example_tvtk_segmentation`).
Specifying its input is done automatical when it is inserted on the
pipeline, be its source needs to be specified explicitly. As it is a VTK
filter, the source is the VTK dataset output by the Mayavi object: we can
find it in `.outputs[0]`.

Note that this filter violates slightly the simple pipeline model that
Mayavi tries to expose to the users: it has two entries. As a result,
the Mayavi pipeline is not longer really a tree. However, if you open up
the Mayavi :ref:`pipeline view <mlab-changing-objects-interactively>`,
you can see that the ProbeFilter has only one parent in the view. To
inspect the actually VTK pipeline underlying this visualization, we
use the TVTK PipelineBrowser at the end of the example. You can see that
the VTK pipeline is much more complex that the pipeline represented
in Mayavi: actors, data mappers, and other elements of the VTK pipeline
are collapsed in the Mayavi filters and modules.

Note that, as we know the expression of the function, it would be simpler
and more efficient to directly sample it on the sphere.


**Python source code:** :download:`probe_filter.py`

.. literalinclude:: probe_filter.py
    :lines: 44-


    