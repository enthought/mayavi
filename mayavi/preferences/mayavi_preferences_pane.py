"""Preferences for Mayavi
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from apptools.preferences.api import PreferencesHelper
from traits.api import (Bool, Enum, Tuple, Range, List,
        Str, Instance, HasTraits)
from traitsui.api import View, Group, Item, RGBColorEditor
from envisage.ui.tasks.api import PreferencesPane

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
        from mayavi.preferences.preferences_helpers import RootPreferencesHelper
        return RootPreferencesHelper()




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
        from mayavi.preferences.preferences_helpers import MlabPreferencesHelper
        return MlabPreferencesHelper()
