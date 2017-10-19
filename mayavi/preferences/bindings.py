"""
Code to setup the preferences for common objects.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2015, Enthought Inc.
# License: BSD Style.

from .preference_manager import preference_manager


def get_scene_preferences():
    """Return a dictionary of the scene's default preferences."""
    pref = preference_manager.preferences
    res = {}
    res['stereo'] = eval(pref.get('tvtk.scene.stereo'))
    res['magnification'] = \
            eval(pref.get('tvtk.scene.magnification'))
    res['foreground'] = eval(pref.get('tvtk.scene.foreground_color'))
    res['background'] = eval(pref.get('tvtk.scene.background_color'))
    return res

def set_scene_preferences(scene, prefs_dict=None):
    """Setup the preferences for a scene given a scene and an optional
    dictionary with the preferences.
    """
    if prefs_dict is None:
        prefs_dict = get_scene_preferences()
    # Set the preferences.
    scene.trait_set(**prefs_dict)
    # If this isn't done the background isn't set.
    scene.renderer.background = scene.background
