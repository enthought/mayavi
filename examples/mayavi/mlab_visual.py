#!/usr/bin/env python

"""A very simple example to show how you can use TVTK's visual module
with mlab."""

from enthought.mayavi import mlab
from enthought.tvtk.tools import visual as V
# Create a figure
f = mlab.figure(size=(500,500))
# Tell visual to use this as the viewer.
V.set_viewer(f)

# A silly visualization.
mlab.test_plot3d()

# Even sillier animation.
b1 = V.box()
b2 = V.box(x=4., color=V.color.red)
b3 = V.box(x=-4, color=V.color.red)
b1.v = 5.0

@mlab.show
@mlab.animate(delay=250)
def anim():
    """Animate the b1 box."""
    while 1:
        b1.x = b1.x + b1.v*0.1
        if b1.x > 2.5 or b1.x < -2.5:
            b1.v = -b1.v
        yield

# Run the animation.
anim()
