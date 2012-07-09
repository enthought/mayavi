"""An example of how to generate a 2D structured points dataset
using numpy arrays.  Also shown is a way to visualize this data with
the mayavi2 application.

The script can be run like so::

  $ mayavi2 -x structured_points2d.py

Alternatively, it can be run as::

  $ python structured_points2d.py

"""
# Author: Prabhu Ramachandran <prabhu at aero dot iitb dot ac dot in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD style.

from numpy import arange, sqrt, sin
from tvtk.api import tvtk
from mayavi.scripts import mayavi2

# Generate the scalar values.
x = (arange(0.1, 50.0)-25)/2.0
y = (arange(0.1, 50.0)-25)/2.0
r = sqrt(x[:,None]**2+y**2)
z = 5.0*sin(r)/r  #

# Make the tvtk dataset.
# tvtk.ImageData is identical and could also be used here.
spoints = tvtk.StructuredPoints(origin=(-12.5,-12.5,0),
                                spacing=(0.5,0.5,1),
                                dimensions=(50,50,1))
# Transpose the array data due to VTK's implicit ordering. VTK assumes
# an implicit ordering of the points: X co-ordinate increases first, Y
# next and Z last.  We flatten it so the number of components is 1.
spoints.point_data.scalars = z.T.flatten()
spoints.point_data.scalars.name = 'scalar'

# Uncomment the next two lines to save the dataset to a VTK XML file.
#w = tvtk.XMLImageDataWriter(input=spoints, file_name='spoints2d.vti')
#w.write()

# Now view the data.
@mayavi2.standalone
def view():
    from mayavi.sources.vtk_data_source import VTKDataSource
    from mayavi.filters.warp_scalar import WarpScalar
    from mayavi.filters.poly_data_normals import PolyDataNormals
    from mayavi.modules.surface import Surface

    mayavi.new_scene()
    src = VTKDataSource(data = spoints)
    mayavi.add_source(src)
    mayavi.add_filter(WarpScalar())
    mayavi.add_filter(PolyDataNormals())
    s = Surface()
    mayavi.add_module(s)

if __name__ == '__main__':
    view()
