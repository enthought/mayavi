"""The plugin definition for the TVTK scene.  This plugin can be used
when one wants to display TVTK actors on screen.  This version does
not add any menus/actions/toolbar items to the UI itself.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Plugin definition imports.
from enthought.envisage.api import PluginDefinition
from enthought.envisage.core.core_plugin_definition import Preferences

from enthought.envisage.workbench.preference.preference_plugin_definition \
     import PreferencePages, Page

######################################################################
# Extensions.
######################################################################

########################################
# Preferences.

preferences = Preferences(
    defaults={'stereo': False,
              'magnification': 1,
              'background_color': (0.1, 0.2, 0.4),
              'foreground_color': (1.0, 1.0, 1.0)
              }
    )

scene_preference_page = Page(
    id         = "ScenePreferencePage",
    class_name = "enthought.tvtk.plugins.scene.scene_preference_page.ScenePreferencePage",
    name       = "TVTK Scene",
    category   = "",
)

preference_pages = PreferencePages(
    pages = [scene_preference_page]
)
extensions = [preferences, preference_pages]

requires = ["enthought.envisage.workbench",
            ]


######################################################################
# The plugin definition.
######################################################################
PluginDefinition(
    # Plugin's globally unique identifier.
    id = "enthought.tvtk.plugins.scene",
    # Class that implements the plugin.
    class_name = "enthought.tvtk.plugins.scene.scene_plugin.ScenePlugin",
    
    # General information about the plugin.
    name            = "TVTK Scene Plugin",
    version         = "1.0.0",
    provider_name   = "Enthought Inc.",
    provider_url    = "www.enthought.com",
    enabled         = True,
    autostart       = True,

    # The Id's of the plugins that this plugin requires.
    requires = requires,
    # The extension points offered by this plugin.
    extension_points = [],
    # The contributions that this plugin makes to extension points
    # offered by either itself or other plugins.
    extensions = extensions
    )
