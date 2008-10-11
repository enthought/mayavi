"""
Code to setup the preferences for common objects.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Prabhu Ramachandran
# License: BSD Style.

from enthought.preferences.api import bind_preference

from preference_manager import preference_manager


def bind_scene_preferences(scene):
    """Setup the preferences for a scene given a scene and an optional
    preferences.
    """
    pref = preference_manager.preferences
    bind_preference(scene, 'stereo', 'enthought.tvtk.scene.stereo', pref)
    bind_preference(scene, 'magnification', 
                    'enthought.tvtk.scene.magnification', pref)
    bind_preference(scene, 'foreground',
                    'enthought.tvtk.scene.foreground_color', pref)
    bind_preference(scene, 'background',
                    'enthought.tvtk.scene.background_color', pref)
    # If this isn't done the background isn't set.
    scene.renderer.background = scene.background

