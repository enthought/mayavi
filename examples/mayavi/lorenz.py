"""
A simple example displaying the trajectories for the Lorenz system of
equations using mlab along with the z-nullcline.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2009, Enthought, Inc.
# License: BSD Style.

import numpy
from enthought.mayavi import mlab

def lorenz(x, y, z, s=10.,r=28., b=8./3.):
    """The Lorenz system."""
    u = s*(y-x)
    v = r*x -y - x*z
    w = x*y - b*z
    return u, v, w

# Sample the space in an interesting region.
x, y, z = numpy.mgrid[-50:50:100j,-50:50:100j,-10:60:70j]
u, v, w = lorenz(x, y, z)
fig = mlab.figure(size=(600, 600))
# Plot the flow of trajectories with suitable parameters.
f = mlab.flow(x, y, z, u, v, w)
f.stream_tracer.integration_direction = 'both'
f.stream_tracer.maximum_propagation = 200
# An outline.
o = mlab.outline()
# Extract the z-velocity from the vectors and plot the 0 level set
# hence producing the z-nullcline.
src = f.mlab_source.m_data
e = mlab.pipeline.extract_vector_components(src)
e.component = 'z-component'
zc = mlab.pipeline.iso_surface(e, opacity=0.5)
zc.contour.auto_contours = False
zc.contour.contours = [0.0]
# A nice view of the plot.
mlab.view(120, 60, 200)
mlab.show()

