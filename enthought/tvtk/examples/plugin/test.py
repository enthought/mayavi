#!/usr/bin/env python
"""
This is a simple test plugin to demonstrate how one can use the
tvtk.plugin.scene and tvtk.plugin.browser plugins.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import sys

# Enthought library imports.
from enthought.envisage.api import Application

# FIXME: This forces wxPython to be imported first.  This eliminates
# some very wierd problems with VTK and wxPython that produce Pango
# errors under Linux.
from enthought.pyface.api import GUI, ImageResource, SplashScreen

# Local imports.
from plugin_definitions import PLUGIN_DEFINITIONS


def main():
    """The main application is created and launched here."""
    
     # Create a GUI and put up the splash screen (if required).
    gui = GUI()

    # Create an Envisage application.
    application = Application(argv=sys.argv,
                              id='enthought.tvtk.examples.plugin.test',
                              gui=gui,
                              plugin_definitions=PLUGIN_DEFINITIONS,
                              requires_gui=False)
    # Start the application.
    application.start()

    # Start the GUI event loop (this call does not return until the GUI is
    # closed).
    gui.start_event_loop()
    
    # Stop the application.
    application.stop()


if __name__ == '__main__':
    main()
    
