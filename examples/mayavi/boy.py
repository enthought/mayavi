#!/usr/bin/env mayavi2 
"""
Script to generate the Mayavi2 logo: a boy surface.
"""

############################################################################
# The following *optional* two lines allow a user to call this script
# as either `python script.py` or `mayavi2 script.py`.  These two
# lines must be placed before any other mayavi imports.
from enthought.mayavi.scripts import mayavi2
mayavi2.standalone(globals())

from numpy import sin, cos, mgrid, pi, sqrt 
from enthought.mayavi import mlab as M

u, v = mgrid[-0.035:pi:0.01, -0.035:pi:0.01]
X = 2/3.* (cos(u)* cos(2*v) 
        + sqrt(2)* sin(u)* cos(v))* cos(u) / (sqrt(2) - sin(2*u)* sin(3*v))
Y = 2/3.* (cos(u)* sin(2*v) - sqrt(2)* sin(u)* sin(v))* cos(u) / (sqrt(2)
        - sin(2*u)* sin(3*v))
Z = sqrt(2)* cos(u)* cos(u) / (sqrt(2) - sin(2*u)* sin(3*v))
S = sin(u)

# The view looks nicer if we revert X 
Z = -Z

M.clf()
M.mesh(X, Y, Z, scalars=S, colormap='YlGnBu', )

# Nice view from the front
M.view(.0, -5.0, 6.)
