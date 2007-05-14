#!/usr/bin/env python
"""The TVTK pipeline browser plugin definition.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Plugin definition imports.
from enthought.envisage.api import PluginDefinition
from enthought.envisage.workbench.workbench_plugin_definition import \
     View, Workbench  


# The plugin's globally unique identifier (also used as the prefix for all
# identifiers defined in this module).
ID = "enthought.tvtk.plugins.browser"

########################################
# Views.

browser_view = View(
    id         = ID + ".browser_view.BrowserView",
    class_name = ID + ".browser_view.BrowserView",
    name       = "TVTK pipeline browser",
    image      = "images/browser_view.png",
    position   = "left"
)

workbench = Workbench(views=[browser_view])
requires = ["enthought.envisage.workbench",
            "enthought.tvtk.plugins.scene"]
extensions = [workbench,]    


######################################################################
# The plugin definition.
######################################################################
class TVTKPipelineBrowserPluginDefinition(PluginDefinition):
    # Plugin's globally unique identifier.
    id = ID
    # Class that implements the plugin.
    class_name = ID + ".browser_plugin.BrowserPlugin"

    # General information about the plugin.
    name            = "TVTK Pipeline Browser"
    version         = "1.0.0"
    provider_name   = "Enthought Inc."
    provider_url    = "www.enthought.com"
    enabled         = True
    autostart       = True

    # The Id's of the plugins that this plugin requires.
    requires = requires
    # The extension points offered by this plugin.
    extension_points = []
    # The contributions that this plugin makes to extension points
    # offered by either itself or other plugins.
    extensions = extensions
