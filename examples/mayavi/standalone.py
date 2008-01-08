#!/usr/bin/env python
"""A simple example of how you can use MayaVi without
using Envisage or the MayaVi envisage application.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from os.path import join, dirname

from enthought.pyface.api import GUI
# The core Engine.
from enthought.mayavi.engine import Engine
from enthought.mayavi.view.engine_view import EngineView
# Usual MayaVi imports
from enthought.mayavi.sources.api import VTKXMLFileReader
from enthought.mayavi.modules.api import Outline, ScalarCutPlane, Streamline


def main():
    # Create the MayaVi engine and start it.
    e = Engine()
    # start does nothing much but useful if someone is listening to
    # your engine.
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
    src.initialize(join('data', 'fire_ug.vtu'))
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

