""" Example showing how to pick data on a surface, going all the way back
to the index in the numpy arrays.

In this example, two views of the same data are shown. One with the data
on a sphere, the other with the data flat.

We use the 'on_mouse_pick' method of the scene to register a callback on
clicking on the sphere. The callback is called with a picker object as
and an argument. We use the point_id of the point that has been picked,
and go back to the 2D index on the data matrix to find its position.
"""

################################################################################
# Create some data
import numpy as np
pi  = np.pi
cos = np.cos
sin = np.sin

phi, theta = np.mgrid[0:pi:180j,0:2*pi:180j]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 1; m5 = 2; m6 = 2; m7 = 4;
s = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
x = sin(phi)*cos(theta)
y = cos(phi)
z = sin(phi)*sin(theta)

################################################################################
# Plot the data
from mayavi import mlab

# A first plot in 3D
fig = mlab.figure(1)
mlab.clf()
mesh = mlab.mesh(x, y, z, scalars=s)
cursor3d = mlab.points3d(0., 0., 0., mode='axes',
                                color=(0, 0, 0),
                                scale_factor=0.5)
mlab.title('Click on the ball')

# A second plot, flat
fig2d = mlab.figure(2)
mlab.clf()
im = mlab.imshow(s)
cursor = mlab.points3d(0, 0, 0, mode='2dthick_cross',
                                color=(0, 0, 0),
                                scale_factor=10)
mlab.view(90, 0)

################################################################################
# Some logic to select 'mesh' and the data index when picking.

def picker_callback(picker_obj):
    picked = picker_obj.actors
    if mesh.actor.actor._vtk_obj in [o._vtk_obj for o in picked]:
        # m.mlab_source.points is the points array underlying the vtk
        # dataset. GetPointId return the index in this array.
        x_, y_ = np.lib.index_tricks.unravel_index(picker_obj.point_id,
                                                                s.shape)
        print("Data indices: %i, %i" % (x_, y_))
        n_x, n_y = s.shape
        cursor.mlab_source.reset(x=x_ - n_x/2.,
                               y=y_ - n_y/2.)
        cursor3d.mlab_source.reset(x=x[x_, y_],
                                 y=y[x_, y_],
                                 z=z[x_, y_])

fig.on_mouse_pick(picker_callback)

mlab.show()
