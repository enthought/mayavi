"""
Code to setup the preferences for common objects.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Prabhu Ramachandran
# License: BSD Style.

from preference_manager import preference_manager


def set_scene_preferences(scene):
    """Setup the preferences for a scene given a scene and an optional
    preferences.
    """
    pref = preference_manager.preferences
    scene.stereo = eval(pref.get('enthought.tvtk.scene.stereo'))
    scene.magnification = \
            eval(pref.get('enthought.tvtk.scene.magnification'))

    fg = eval(pref.get('enthought.tvtk.scene.foreground_color'))
    bg = eval(pref.get('enthought.tvtk.scene.background_color'))
    scene.foreground = fg
    scene.background = bg
    # If this isn't done the background isn't set.
    scene.renderer.background = scene.background

