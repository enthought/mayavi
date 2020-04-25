"""
Code to setup the preferences for common objects.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008-2020, Enthought Inc.
# License: BSD Style.

import ast
from .preference_manager import preference_manager


def get_scene_preferences():
    """Return a dictionary of the scene's default preferences."""
    pref = preference_manager.preferences
    res = {}
    res['stereo'] = ast.literal_eval(pref.get('tvtk.scene.stereo'))
    res['magnification'] = \
            ast.literal_eval(pref.get('tvtk.scene.magnification'))
    res['foreground'] = ast.literal_eval(pref.get('tvtk.scene.foreground_color'))
    res['background'] = ast.literal_eval(pref.get('tvtk.scene.background_color'))
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
