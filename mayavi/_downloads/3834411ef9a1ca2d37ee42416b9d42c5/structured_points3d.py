"""An example of how to generate a 3D structured points dataset
using numpy arrays.  Also shown is a way to visualize this data with
the mayavi2 application.

The script can be run like so::

  $ mayavi2 -x structured_points3d.py

Alternatively, it can be run as::

  $ python structured_points3d.py

"""
# Author: Prabhu Ramachandran <prabhu at aero dot iitb dot ac dot in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD style.

from tvtk.api import tvtk
from tvtk.array_handler import get_vtk_array_type
from tvtk.common import is_old_pipeline
from numpy import array, ogrid, sin, ravel
from mayavi.scripts import mayavi2

# Make the data.
dims = array((128, 128, 128))
vol = array((-5., 5, -5, 5, -5, 5))
origin = vol[::2]
spacing = (vol[1::2] - origin)/(dims -1)
xmin, xmax, ymin, ymax, zmin, zmax = vol
x, y, z = ogrid[xmin:xmax:dims[0]*1j,
                ymin:ymax:dims[1]*1j,
                zmin:zmax:dims[2]*1j]
x, y, z = [t.astype('f') for t in (x, y, z)]
scalars = sin(x*y*z)/(x*y*z)

# Make the tvtk dataset.
spoints = tvtk.StructuredPoints(origin=origin, spacing=spacing,
                                dimensions=dims)
# The copy makes the data contiguous and the transpose makes it
# suitable for display via tvtk.  Note that it is not necessary to
# make the data contiguous since in that case the array is copied
# internally.
s = scalars.transpose().copy()
spoints.point_data.scalars = ravel(s)
spoints.point_data.scalars.name = 'scalars'

# This is needed in slightly older versions of VTK (like the 5.0.2
# release) to prevent a segfault.  VTK does not detect the correct
# data type.
if is_old_pipeline():
    spoints.scalar_type = get_vtk_array_type(s.dtype)

# Uncomment the next two lines to save the dataset to a VTK XML file.
#w = tvtk.XMLImageDataWriter(input=spoints, file_name='spoints3d.vti')
#w.write()

# Now view the data.
@mayavi2.standalone
def view():
    from mayavi.sources.vtk_data_source import VTKDataSource
    from mayavi.modules.outline import Outline
    from mayavi.modules.image_plane_widget import ImagePlaneWidget

    mayavi.new_scene()
    src = VTKDataSource(data = spoints)
    mayavi.add_source(src)
    mayavi.add_module(Outline())
    mayavi.add_module(ImagePlaneWidget())

if __name__ == '__main__':
    view()
