#!/usr/bin/env python
"""A simple example of how you can use MayaVi without using Envisage
or the MayaVi envisage application and do off screen rendering.  On
Linux/Mac you should see a small black window popup and disappear.  On
Win32 you will not see any windows popping up at all.  In the end you
should have an offscreen.png image in the same directory with the
rendered visualization.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from os.path import join, abspath

# The core Engine.
from enthought.mayavi.engine import Engine

# Usual MayaVi imports
from enthought.mayavi.scripts.util import get_data_dir
from enthought.mayavi.sources.api import VTKXMLFileReader
from enthought.mayavi.modules.api import Outline, ScalarCutPlane, Streamline

# The TVTK window.
from enthought.pyface.tvtk.tvtk_scene import TVTKWindow


def off_screen_viewer():
    """A factory that creates an offscreen viewer."""
    win = TVTKWindow(off_screen_rendering=True)
    # Need to set some non-zero size for the off screen window.  If
    # not we get VTK errors on Linux.
    win.scene.set_size((100,100))
    return win


def main():
    # Create the MayaVi engine and start it.  Set the scene_factory to
    # use an off screen viewer defined above.
    e = Engine(scene_factory=off_screen_viewer)
    # The `start` method does nothing much but is useful if someone is
    # listening to the engine's `started` event.
    e.start()

    # Create a new scene.
    win = e.new_scene()

    # Now setup a normal MayaVi pipeline.
    src = VTKXMLFileReader()
    src.initialize(join(get_data_dir(abspath(__file__)),
                        'fire_ug.vtu'))
    e.add_source(src)
    e.add_module(Outline())
    e.add_module(ScalarCutPlane())
    e.add_module(Streamline())
    win.scene.isometric_view()
    # Change the size argument to anything you want.
    win.scene.save('offscreen.png', size=(800,800))
    
                   
if __name__ == '__main__':
    main()
