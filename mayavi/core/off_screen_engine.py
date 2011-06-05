"""
An off-screen mayavi engine.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from traits.api import Callable, Str
from tvtk.pyface.tvtk_scene import TVTKWindow
from mayavi.core.engine import Engine
from mayavi.preferences.api import set_scene_preferences


def off_screen_viewer_factory(size=(400, 350)):
    """A factory that creates an offscreen viewer."""
    win = TVTKWindow(off_screen_rendering=True)
    # Set all preferences.
    set_scene_preferences(win.scene)
    # Set the size.
    win.scene.set_size(size)
    return win

################################################################################
# `OffScreenEngine` class.
################################################################################
class OffScreenEngine(Engine):
    # Overriding the scene factory trait of Engine.
    scene_factory = Callable(off_screen_viewer_factory)

    # Our name.
    name = Str('Mayavi offscreen Engine')
