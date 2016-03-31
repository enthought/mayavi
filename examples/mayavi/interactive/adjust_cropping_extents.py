"""
A custom dialog to adjust the parameters of a GeometryFilter to crop
data points.

This example shows how to use a GeometryFilter to crop data points, but
also how to build a custom dialog to easily set interactively parameters
of a filter, or any other Mayavi object.

The GeometryFilter crops all data within a bounding box specified by
'extents'. In this example, we want to be able to tweak these extents
interactively. For this, we build a Traits object that has 'x_min',
'x_max', 'y_min', ... attributes. Traits enables us to represent this
object as a dialog box. We use a callback called when these attributes
are modified to propagate them to the filter. For more information
on creating GUIs with Traits:

    http://docs.enthought.com/traitsui

    http://docs.enthought.com/traits

    https://support.enthought.com/hc/en-us/articles/204469620-Introductory-materials-for-Traits-and-Traits-UI

"""
# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2010, Enthought, Inc.
# License: BSD Style.


################################################################################
# Create a set of points, with given density
import numpy as np
x, y, z, s = np.random.random((4, 500))

################################################################################
# A dialog to edit a range interactively and propagate it to the filter
from traits.api import HasTraits, Range, Float, Instance, \
    on_trait_change
from traitsui.api import View

class ExtentDialog(HasTraits):
    """ A dialog to graphical adjust the extents of a filter.
    """

    # Data extents
    data_x_min = Float
    data_x_max = Float
    data_y_min = Float
    data_y_max = Float
    data_z_min = Float
    data_z_max = Float

    x_min = Range('data_x_min', 'data_x_max', 'data_x_min')
    x_max = Range('data_x_min', 'data_x_max', 'data_x_max')
    y_min = Range('data_y_min', 'data_y_max', 'data_y_min')
    y_max = Range('data_y_min', 'data_y_max', 'data_y_max')
    z_min = Range('data_z_min', 'data_z_max', 'data_z_min')
    z_max = Range('data_z_min', 'data_z_max', 'data_z_max')

    filter = Instance(HasTraits, allow_none=False)

    @on_trait_change('x_min,x_max,y_min,y_max,z_min,z_max')
    def update_extent(self):
        if (self.filter is not None
                    and self.x_min < self.x_max
                    and self.y_min < self.y_max
                    and self.z_min < self.z_max
                            ):
            self.filter.extent = (self.x_min, self.x_max,
                                  self.y_min, self.y_max,
                                  self.z_min, self.z_max)

    view = View('x_min', 'x_max', 'y_min', 'y_max', 'z_min', 'z_max',
                title='Edit extent', resizable=True)


################################################################################
# Now build the visualization using mlab
from mayavi import mlab
fig = mlab.figure(1, bgcolor=(1, 1, 1))

# Create unconnected points
pts = mlab.pipeline.scalar_scatter(x, y, z, s)
mlab.outline(pts)

# Use a geometry_filter to filter with a bounding box
geometry_filter = mlab.pipeline.user_defined(pts,
                                   filter='GeometryFilter')
geometry_filter.filter.extent_clipping = True
# Connect our dialog to the filter
extent_dialog = ExtentDialog(
            data_x_min=0, data_x_max=1,
            data_y_min=0, data_y_max=1,
            data_z_min=0, data_z_max=1,
            filter=geometry_filter.filter)
# We need to use 'edit_traits' and not 'configure_traits()' as we do
# not want to start the GUI event loop (the call to mlab.show())
# at the end of the script will do it.
extent_dialog.edit_traits()

# The geometry_filter leaves hanging points, we need to add a
# CleanPolyData filter to get rid of these.
clip = mlab.pipeline.user_defined(geometry_filter,
                                    filter='CleanPolyData')

# Finally, visualize the remaining points with spheres using a glyph
# module
spheres = mlab.pipeline.glyph(clip, scale_factor=.1)

mlab.show()
