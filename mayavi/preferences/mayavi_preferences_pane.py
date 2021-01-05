"""Preferences for Mayavi
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from apptools.preferences.api import PreferencesHelper
from traits.api import (Bool, Enum, Tuple, Range, List,
        Str, Instance, HasTraits)
from traitsui.api import View, Group, InstanceEditor, Item, RGBColorEditor
from envisage.ui.tasks.api import PreferencesPane
        
from mayavi.preferences.api import preference_manager

################################################################################
# `MayaviRootPreferencesPage` class
################################################################################
class MayaviRootPreferencesPane(PreferencesPane):
    """ Preferences pane for Mayavi. """

    #### 'Controller' interface ###############################################

    #: The preferences helper for which this pane is a view.
    model = Instance(PreferencesHelper)

    #### 'PreferencesPane' interface ##########################################

    #: An identifier for the pane (unique within a category).
    id = Str("MayaviRoot")

    #: The ID of the category in which to place the pane.
    category = Str("Mayavi")

    #: The pane appears after the pane with this ID.
    before = Str

    #: The pane appears after the pane with this ID.
    after = Str

    def _model_default(self):
        return preference_manager.root

    traits_view = View(
                    Group(
                        Group(
                            Item(name='confirm_delete'),
                            Item(name='show_splash_screen'),
                            Item(name='show_helper_nodes'),
                            Item(name='open_help_in_light_browser'),
                            Item(name='use_ipython'),
                            label='General settings',
                            show_border=True,
                            ),
                        Group(
                            Group(
                                Item('_contrib_finder',
                                     style='custom',
                                     show_label=False,
                                     resizable=True,
                                     ),
                                ),
                            label='Contribution settings',
                            show_border=True,
                            ),
                        ),
                    resizable=True
                    )


################################################################################
# `MayaviMlabPreferencesPage` class
################################################################################
class MayaviMlabPreferencesPane(PreferencesPane):
    """ Preferences pane for Mayavi. """


    #### 'Controller' interface ###############################################

    #: The preferences helper for which this pane is a view.
    model = Instance(PreferencesHelper)

    #### 'PreferencesPane' interface ##########################################

    #: An identifier for the pane (unique within a category).
    id = Str("Mlab")

    #: The ID of the category in which to place the pane.
    category = Str("Mayavi")

    #: The pane appears after the pane with this ID.
    before = Str

    #: The pane appears after the pane with this ID.
    after = Str("MayaviRoot")

    def _model_default(self):
        return preference_manager.mlab

    traits_view = View(Group(
                             Item('backend'),
                             Item('background_color'),
                             Item('foreground_color'),
                             Item('offscreen')
                             ),
                       resizable=True
                      )
