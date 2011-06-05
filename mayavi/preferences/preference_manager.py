"""A preference manager for all mayavi related preferences.

The idea behind this module is that it lets the mayavi
library/application use the same preferences by managing them no matter
if mayavi is used as an application (via envisage3) or as a library.

The preferences helpers are divided into different categories for
different kinds of preferences.  Currently the following are available.

  - root: for global mayavi preferences of the form
    'mayavi.preference'.

For more details on the general preferences support in enthought, please
read the documentation for apptools.preferences (part of the AppTools
package).

"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports
from os.path import join
import pkg_resources

# Enthought library imports.
from traits.etsconfig.api import ETSConfig
from traits.api import HasTraits, Instance
from traitsui.api import View, Group, Item
from apptools.preferences.api import (ScopedPreferences, IPreferences,
        PreferencesHelper)

# Local imports.
from mayavi.preferences.preferences_helpers import (
        RootPreferencesHelper, MlabPreferencesHelper )

# The application ID where the preferences are stored.
ID = 'mayavi_e3'


################################################################################
# `PreferenceManager` class
################################################################################
class PreferenceManager(HasTraits):

    # The root preferences helper for preferences of the form
    # 'mayavi.preference'.
    root = Instance(PreferencesHelper)

    # The mlab preferences helper for preferences of the form
    # 'mayavi.mlab.preference'.
    mlab = Instance(PreferencesHelper)

    # The preferences.
    preferences = Instance(IPreferences)

    ######################################################################
    # Traits UI view.

    traits_view = View(Group(
                           Group(Item(name='root', style='custom'),
                                 show_labels=False, label='Root',
                                 show_border=True
                                ),
                           Group(Item(name='mlab', style='custom'),
                                 show_labels=False, label='Mlab',
                                 show_border=True,
                                ),
                           ),
                       buttons=['OK', 'Cancel'],
                       resizable=True
                      )

    ######################################################################
    # `HasTraits` interface.
    ######################################################################
    def __init__(self, **traits):
        super(PreferenceManager, self).__init__(**traits)

        if 'preferences' not in traits:
            self._load_preferences()

    def _preferences_default(self):
        """Trait initializer."""
        return ScopedPreferences()

    def _root_default(self):
        """Trait initializer."""
        return RootPreferencesHelper(preferences=self.preferences)

    def _mlab_default(self):
        """Trait initializer."""
        return MlabPreferencesHelper(preferences=self.preferences)

    ######################################################################
    # Private interface.
    ######################################################################
    def _load_preferences(self):
        """Load the default preferences."""
        # Save current application_home.
        app_home = ETSConfig.get_application_home()
        # Set it to where the mayavi preferences are temporarily.
        path = join(ETSConfig.get_application_data(), ID)
        ETSConfig.application_home = path
        try:
            for pkg in ('mayavi.preferences',
                        'tvtk.plugins.scene'):
                pref = 'preferences.ini'
                pref_file = pkg_resources.resource_stream(pkg, pref)

                preferences = self.preferences
                default = preferences.node('default/')
                default.load(pref_file)
                pref_file.close()
        finally:
            # Set back the application home.
            ETSConfig.application_home = app_home

    def _preferences_changed(self, preferences):
        """Setup the helpers if the preferences trait changes."""
        for helper in (self.root, ):
            helper.preferences = preferences


##########################################################
# A Global preference manager that all other modules can use.

preference_manager = PreferenceManager()

