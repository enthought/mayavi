from numpy import mgrid, sin, sqrt
from enthought.mayavi import mlab

# This option sets offscreen rendering.
mlab.options.offscreen = True

# Create some data
X, Y = mgrid[-1:1:100j, -1:1:100j]
R = 10*sqrt(X**2 + Y**2)
Z = sin(R)/R

# Plot it.
s = mlab.surf(X, Y, Z, colormap='gist_earth')
mlab.savefig('offscreen_mlab.png')
mlab.show()
