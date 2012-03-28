#!/usr/bin/env python
"""A simple example of how you can use Mayavi without
using Envisage or the Mayavi Envisage application.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from os.path import join, abspath

from pyface.api import GUI
# The core Engine.
from mayavi.core.api import Engine
from mayavi.core.ui.engine_view import EngineView
# Usual MayaVi imports
from mayavi.scripts.util import get_data_dir
from mayavi.sources.api import VTKXMLFileReader
from mayavi.modules.api import Outline, ScalarCutPlane, Streamline


def main():
    # Create the MayaVi engine and start it.
    e = Engine()
    # Starting the engine registers the engine with the registry and
    # notifies others that the engine is ready.
    e.start()

    # Do this if you need to see the MayaVi tree view UI.
    ev = EngineView(engine=e)
    ui = ev.edit_traits()

    # Create a new scene.
    scene = e.new_scene()
    # Now create a new scene just for kicks.
    scene1 = e.new_scene()

    # Now setup a normal MayaVi pipeline.
    src = VTKXMLFileReader()
    src.initialize(join(get_data_dir(abspath(__file__)),
                        'fire_ug.vtu'))
    e.add_source(src)
    e.add_module(Outline())
    e.add_module(ScalarCutPlane())
    e.add_module(Streamline())
    return e, ui

if __name__ == '__main__':
    # When main returns the ui to go out of scope and be gc'd causing the view
    # to disappear with qt4.
    e, ui = main()
    # Create a GUI instance and start the event loop.  We do this here so that
    # main can be run from IPython -wthread if needed.
    gui = GUI()
    gui.start_event_loop()

