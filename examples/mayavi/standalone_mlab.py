#!/usr/bin/env python
"""A simple example of how you can use MayaVi and mlab without
using Envisage or the MayaVi envisage application.
"""
# Author: Gael Varoquaux <gael.varoquaux@normalesup.org> 
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from enthought.mayavi import mlab
from numpy import mgrid, sin, sqrt

# Create some data
X, Y = mgrid[-1:1:100j, -1:1:100j]
R = 10*sqrt(X**2 + Y**2)
Z = sin(R)/R

# Plot it.
mlab.figure(fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
mlab.surf(X, Y, Z, colormap='gist_earth')

# Display the MayaVi tree view UI.
ui = mlab.show_pipeline()

mlab.show()
