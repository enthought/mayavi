"""
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
pipeline, be its source needs to be specified explicitely. As it is a VTK
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
"""
import numpy as np

from mayavi import mlab
from tvtk.api import tvtk
from tvtk.common import configure_source_data, configure_input

# The angular par of the spherical harmonic (3, 2)
x, y, z = np.mgrid[-0.5:0.5:100j, -0.5:0.5:100j, -0.5:0.5:100j]
Phi = np.angle((x + y * 1j) ** 2 * z)

field = mlab.pipeline.scalar_field(x, y, z, Phi)
ipw = mlab.pipeline.image_plane_widget(field)
mlab.outline(field)

surface = mlab.pipeline.builtin_surface()
surface.source = "sphere"
surface.data_source.radius = 0.4
surface.data_source.phi_resolution = 200
surface.data_source.theta_resolution = 200
probe_filter = tvtk.ProbeFilter()
configure_input(probe_filter, surface.data_source)
configure_source_data(probe_filter, field.outputs[0])
probe = mlab.pipeline.user_defined(surface, filter=probe_filter)

surf = mlab.pipeline.surface(probe)

fig = mlab.gcf()

################################################################################
# Finally, to inspect the VTK Pipeline (and not the Mayavi one, we
# use the TVTK pipeline browser)
# Note that for Mayavi version < 3.4.1, there is a bug in the
# PipelineBrowser preventing a good display of this pipeline.
from tvtk.pipeline.browser import PipelineBrowser

browser = PipelineBrowser(fig.scene)
browser.show()

mlab.show()
