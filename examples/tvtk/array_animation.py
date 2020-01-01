#!/usr/bin/env python
"""A simple example showing an animation.  The example illustrates a
few things.

 1. You can pass a numpy array of scalars and use it directly with
    tvtk.

 2. The tvtk arrays are views of numpy arrays.  Thus changing the
    array in-place will also change the underlying VTK data.

 3. When changing the numpy data you must call `modified` on a
    relevant tvtk object.

The example is a little contrived since there are better ways of
achieving the same effect but the present form nicely illustrates item
2 mentioned above.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.

from tvtk.api import tvtk
from tvtk.common import configure_input
import numpy as np
import time

# First create a structured points data set.
sp = tvtk.StructuredPoints(origin=(-10., -10., 0.0),
                           dimensions=(80, 80, 1),
                           spacing=(0.25, 0.25, 0.0))

# Create some nice data at these points.
x = np.arange(-10., 10., 0.25)
y = x
r = np.sqrt(x[:,None]**2+y**2)
# We need the transpose so the data is as per VTK's expected format
# where X coords vary fastest, Y next and then Z.
try:
    import scipy.special
    z = np.reshape(np.transpose(5.0*scipy.special.j0(r)), (-1,) )
except ImportError:
    z = np.reshape(np.transpose(5.0*np.sin(r)/r), (-1,) )

# Now set the scalar data for the StructuredPoints object.  The
# scalars of the structured points object will be a view into our
# Numeric array.  Thus, if we change `z` in-place, the changes will
# automatically affect the VTK arrays.
sp.point_data.scalars = z

# Convert this to a PolyData object.
geom_filter = tvtk.ImageDataGeometryFilter()
configure_input(geom_filter, sp)

# Now warp this using the scalar value to generate a carpet plot.
warp = tvtk.WarpScalar()
configure_input(warp, geom_filter)

# Smooth the resulting data so it looks good.
normals = tvtk.PolyDataNormals()
configure_input(normals, warp)

# The rest of the VTK pipeline.
m = tvtk.PolyDataMapper(scalar_range=(min(z), max(z)))
configure_input(m, normals)

a = tvtk.Actor(mapper=m)

ren = tvtk.Renderer(background=(0.5, 0.5, 0.5))
ren.add_actor(a)

# Get a nice view.
cam = ren.active_camera
cam.azimuth(-60)
cam.roll(90)

# Create a RenderWindow, add the renderer and set its size.
rw = tvtk.RenderWindow(size=(600, 600))
rw.add_renderer(ren)

# Create the RenderWindowInteractor
rwi = tvtk.RenderWindowInteractor(render_window=rw)

rwi.initialize()
ren.reset_camera()
rwi.render()

# The following is a crude approach but illustrates the point.
scale = old_scale = 1.0
for i in np.arange(np.pi*0.5, 2.5*np.pi, 0.2):
    if abs(i) < 1.0e-10:
        continue
    scale = np.sin(i)
    # We change 'z' in-place
    z *= scale/old_scale
    # Reset the scalar range.
    m.scalar_range = min(z), max(z)
    # Now explicitly notify `sp` that its data has changed.  If this
    # is not done, VTK has no way of knowing the data changed in order
    # to flush the pipeline.
    sp.modified()
    # Re-render the scene to actually flush the VTK pipeline.
    rwi.render()
    old_scale = scale
    time.sleep(0.1) # Just in case your hardware is really fast.

# Start the VTK event loop.
rwi.start()
