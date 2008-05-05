"""Listens for any changes to the preferences and does the needful.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import HasTraits, Instance

# Local imports.
from enthought.mayavi.core.base import Base


##############################################################################
# `PreferenceManager` class.
##############################################################################
class PreferenceManager(HasTraits):

    # The MayaVi engine.  The preferences trait is set when this trait
    # is set.
    engine = Instance('enthought.mayavi.engine.Engine')

    # The application preferences.
    preferences = Instance('enthought.envisage.core.preferences.Preferences')


    ######################################################################
    # Non-public interface (various event handlers).
    ######################################################################
    def _handle_preference_changed(self, key, old, new):
        """This method handles any changes to the preferences.
        """
        if key == 'confirm_delete':
            Base.confirm_delete = new
            
    def _preferences_changed(self, old, new):
        for key in new.defaults:
            self._handle_preference_changed(key, None, new.get(key))

    def _preference_changed_changed_for_preferences(self, value):
        self._handle_preference_changed(value.key, value.old, value.new)

    def _engine_changed(self, value):
        # Sets our preferences trait given the engine object.
        app = value.application
        m2_plugin = [x for x in app.plugin_activator.plugins
                     if x.id == 'enthought.mayavi'][0]
        self.preferences = m2_plugin.preferences
        
