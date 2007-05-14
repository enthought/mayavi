"""This is a simple test plugin to demonstrate how one can use the
tvtk.plugin.scene and tvtk.plugin.browser plugins.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.api import PluginDefinition
from enthought.envisage.core.core_plugin_definition import ApplicationObject

# This binds the scene plugin to the python shell.
app_obj = ApplicationObject(
    class_name = 'test_application_object.TestApplicationObject'
)

requires = ["enthought.envisage.workbench",
            "enthought.tvtk.plugins.scene",
            "enthought.plugins.python_shell",
            ]
    

PluginDefinition(
    # This plugins unique identifier.
    id = "enthought.tvtk.example.plugin.test",

    # General info.
    name = "A Test Plugin for TVTK",
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
    extensions = [app_obj]
)
