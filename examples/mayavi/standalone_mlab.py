#!/usr/bin/env python
"""A simple example of how you can use MayaVi and mlab without
using Envisage or the MayaVi envisage application.

"""
# Author: Gael Varoquaux <gael.varoquaux@normalesup.org> 
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from enthought.pyface.api import GUI
# Mlab imports
from enthought.mayavi import mlab

from numpy import mgrid, sin, sqrt

def main():
    # Display the MayaVi tree view UI.
    ui = mlab.show_engine()

    # Create some data
    X, Y = mgrid[-1:1:100j, -1:1:100j]
    R = 10*sqrt(X**2 + Y**2)
    Z = sin(R)/R

    # Plot it.
    mlab.surf(X, Y, Z, colormap='gist_earth')
    return ui


if __name__ == '__main__':
    # When main returns the ui goes out of scope and destructs causing the 
    # engine view to disappear with qt4. 
    ui = main()
    # Create a GUI instance and start the event loop.  We do this here
    # so that main can be run from IPython -wthread if needed.
    #gui = GUI()
    #gui.start_event_loop()
