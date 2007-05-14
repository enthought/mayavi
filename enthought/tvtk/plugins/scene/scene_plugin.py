"""A TVTK render window scene plugin.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from enthought.envisage.api import Plugin
from enthought.traits.api import List, Instance, Property

# Local imports
from enthought.tvtk.plugins.scene.scene_editor import SceneEditor
from enthought.tvtk.plugins.scene.services import ITVTKSCENE


######################################################################
# `ScenePlugin` class.
######################################################################
class ScenePlugin(Plugin):

    # A list of views created by the plugin.
    editors = List(SceneEditor)

    # The currently active editor.
    current_editor = Property(Instance(SceneEditor))

    ########################################
    # Private traits.
    # The current editor -- this is usually set by the activated
    # editor.
    _current_editor = Instance(SceneEditor)
    ########################################

    ######################################################################
    # `Plugin` interface.
    ######################################################################
    def start(self, application):
        """Starts the plugin."""

        # Setup a callback to handle changes to preferences.
        prefs = self.preferences
        prefs.on_trait_change(self._preference_changed_handler,
                              'preference_changed')

        # Register our service.
        self.register_service(ITVTKSCENE, self)

    def stop(self, application):
        """Stop the plugin."""
        self.save_preferences()

    ######################################################################
    # Protected `ScenePlugin` interface.
    ######################################################################
    def _preference_changed_handler(self, value):
        """This is called when the preferences are changed."""
        for editor in self.editors:
            editor.preferences_changed(value)

    def _get_current_editor(self):
        le = len(self.editors)
        if le == 0:
            return None
        elif le == 1:
            return self.editors[0]
        else:
            return self._current_editor

    def _set_current_editor(self, editor):
        self._current_editor = editor
