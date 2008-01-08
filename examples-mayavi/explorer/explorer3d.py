#!/usr/bin/env python
""" The entry point for an Envisage application. """

# Standard library imports.
import sys

# Enthought library imports.
from enthought.envisage.api import Application
from enthought.envisage.api import join
from enthought.envisage import _set_using_workbench
from enthought.pyface.api import ImageResource, SplashScreen, GUI

# imports used for finding plugins
import enthought.envisage
import enthought.logger
import enthought.plugins.python_shell
import enthought.tvtk
import enthought.mayavi


_set_using_workbench(True)


######################################################################
# The plugin definitions required by the application.
PLUGIN_DEFINITIONS = [
    # Envisage plugins.
    join(enthought.envisage, 'core/core_plugin_definition.py'),
    join(enthought.envisage, 'resource/resource_plugin_definition.py'),
    join(enthought.envisage, 'action/action_plugin_definition.py'),
    join(enthought.envisage, 'workbench/workbench_plugin_definition.py'),
    join(enthought.envisage, 'workbench/action/action_plugin_definition.py'),
    join(enthought.envisage, 'workbench/preference/preference_plugin_definition.py'),
    join(enthought.logger,   'plugin/logger_plugin_definition.py'),
    join(enthought.plugins.python_shell,  'python_shell_plugin_definition.py'),

    join(enthought.tvtk,     'plugins/scene/scene_plugin_definition.py'),
    join(enthought.tvtk,     'plugins/scene/scene_ui_plugin_definition.py'),

    join(enthought.mayavi,   'mayavi_plugin_definition.py'),
    join(enthought.mayavi,   'mayavi_ui_plugin_definition.py'),

    # Application plugins.
    join('explorer_plugin_definition.py'),
]

######################################################################
def main():
    gui = GUI()

    # Create an Envisage application.
    application = Application(
        argv               = sys.argv,
        id                 = "explorer3d.Explorer3D",
        gui                = gui,
        plugin_definitions = PLUGIN_DEFINITIONS,
        requires_gui       = False
    )

    # Start it!
    application.start()
    gui.start_event_loop()
    application.stop()

# Application entry point.
if __name__ == '__main__':
    main()

