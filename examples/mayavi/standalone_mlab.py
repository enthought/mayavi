#!/usr/bin/env python
"""A simple example of how you can use MayaVi and mlab without
using Envisage or the MayaVi envisage application.

"""
# Author: Gael Varoquaux <gael.varoquaux@normalesup.org> 
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Mlab imports
from enthought.mayavi import mlab

from numpy import mgrid, sin, sqrt

# Display the MayaVi tree view UI.
ui = mlab.show_pipeline()

# Create some data
X, Y = mgrid[-1:1:100j, -1:1:100j]
R = 10*sqrt(X**2 + Y**2)
Z = sin(R)/R

# Plot it.
mlab.surf(X, Y, Z, colormap='gist_earth')

mlab.show()

