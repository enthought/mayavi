"""Various preference helpers for the mayavi preferences.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports
from enthought.traits.api import Bool, Enum, Tuple, Range
from enthought.traits.ui.api import View, Group, Item, RGBColorEditor
from enthought.preferences.api import PreferencesHelper

################################################################################
# `RootPreferencesHelper` class
################################################################################
class RootPreferencesHelper(PreferencesHelper):

    # The preferences path for which we use.
    preferences_path = 'enthought.mayavi'

    ######################################################################
    # Our preferences.

    # Specifies if the nodes on the tree may be deleted without a
    # confirmation or not.  If True the user will be prompted before
    # the object is deleted.  If it is False then the user will not be
    # prompted.
    confirm_delete = Bool(desc='if the user is prompted before'
                          ' a node on the MayaVi tree is deleted')

    # Specifies if the splash screen is shown when mayavi starts.
    show_splash_screen = Bool(desc='if the splash screen is shown at'
                              ' startup')

    # Specifies if the adder nodes are shown on the mayavi tree view.
    show_helper_nodes = Bool(desc='if the helper (adder) nodes are shown'
                             ' on the tree view')

    ######################################################################
    # Traits UI view.

    traits_view = View(Group(
                             Item(name='confirm_delete'),
                             Item(name='show_splash_screen'),
                             Item(name='show_helper_nodes'),
                             ),
                       resizable=True
                      )


################################################################################
# `MlabPreferencesHelper` class
################################################################################
class MlabPreferencesHelper(PreferencesHelper):

    # The preferences path for which we use.
    preferences_path = 'enthought.mayavi.mlab'

    ######################################################################
    # Our preferences.

    # The mlab backend to use.  
    backend = Enum('auto', 'envisage', 'simple', 
                   desc='the mlab backend to use')

    # The background color of the renderer.
    background_color = Tuple(Range(0., 1.), Range(0., 1.), Range(0., 1.),
                             editor=RGBColorEditor,
                             desc='the background color of the scene')

    # The foreground color of the renderer.
    foreground_color = Tuple(Range(0., 1.), Range(0., 1.), Range(0., 1.),
                             editor=RGBColorEditor,
                             desc='the foreground color of the scene')

    ######################################################################
    # Traits UI view.

    traits_view = View(Group(
                             Item(name='backend'),
                             Item(name='background_color'),
                             Item(name='foreground_color'),
                             ),
                       resizable=True
                      )

