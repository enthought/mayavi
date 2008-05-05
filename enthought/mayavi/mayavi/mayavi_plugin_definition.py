"""The MayaVi plugin definition.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.api import PluginDefinition
from enthought.envisage.core.core_plugin_definition import \
     ApplicationObject, Runnable, Preferences
from enthought.envisage.workbench.preference.preference_plugin_definition \
     import PreferencePages, Page

# Local imports
from enthought.mayavi.services import IMAYAVI_ENGINE, IMAYAVI


requires = ["enthought.envisage.workbench",
            "enthought.tvtk.plugins.scene",
            ]

# The plugin's globally unique identifier (also used as the prefix for all
# identifiers defined in this module).
ID = "enthought.mayavi"

########################################
# Preferences.

preferences = Preferences(
    defaults={'confirm_delete': True,
              }
    )

mayavi_preference_page = Page(
    id         = "enthought.mayavi.MayaviPreferencePage",
    class_name = "enthought.mayavi.preference_page.MayaviPreferencePage",
    name       = "MayaVi",
    category   = "",
)

preference_pages = PreferencePages(
    pages = [mayavi_preference_page]
)

########################################
# The application objects that publish the services.

engine_app_obj = ApplicationObject(
    class_name='enthought.mayavi.envisage_engine.EnvisageEngine',
    uol='service://' + IMAYAVI_ENGINE
    )

script_app_obj = ApplicationObject(
    class_name='enthought.mayavi.script.Script',
    uol='service://' + IMAYAVI
    )

# The runnable starts the mayavi engine and binds the Script object to
# the Python shell (if possible).
runnable = Runnable(class_name='enthought.mayavi.runnable.MayaviRunnable')


######################################################################
PluginDefinition(
    # This plugins unique identifier.
    id = ID,

    # General info.
    name = "The MayaVi Plugin",
    version = "2.0",
    provider_name = "Prabhu Ramachandran",
    provider_url = "www.enthought.com",
    enabled = True,
    autostart = True,

    # Id's of plugin that this one requires.
    requires = requires,
    
    # The extension points that we provide.
    extension_points = [],

    # The contributions that this plugin makes to extension points offered by
    # either itself or other plugins.
    extensions = [engine_app_obj, script_app_obj, runnable,
                  preferences, preference_pages]
)
