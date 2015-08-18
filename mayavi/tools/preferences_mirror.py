# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Enthought library imports.
from traits.api import HasTraits, List, Str, Instance
from apptools.preferences.api import PreferencesHelper


###############################################################################
# `PreferencesMirror` class.
###############################################################################
class PreferencesMirror(HasTraits):
    """
    This class mirrors preferences from a PreferencesHelper such that
    users can use them and change them but nothing is saved to disk till
    the user asks for an explicit save.
    """

    # The preferences we mirror.
    preferences = Instance(PreferencesHelper)

    # Private trait to store names of traits.
    _trait_names = List(Str)

    ######################################################################
    # Public interface.
    ######################################################################
    def save(self):
        """Updates the actual preferences and thereby persists them to
        disk.
        """
        for name in self._trait_names:
            setattr(self.preferences, name, getattr(self, name))

    ######################################################################
    # Private interface.
    ######################################################################
    def _preferences_changed(self):
        """Setup traits of our own based on those of the mayavi
        preferences.
        """
        trait_names = []
        opts = self.preferences
        for key, value in opts.traits().items():
            if key not in ['trait_added', 'trait_modified',
                           'preferences', 'preferences_path']:
                self.add_trait(key, value)
                setattr(self, key, getattr(opts, key))
                trait_names.append(key)
                opts.on_trait_change(self._update, key)
        self._trait_names = trait_names

    def _update(self, obj, name, old, new):
        setattr(self, name, new)
