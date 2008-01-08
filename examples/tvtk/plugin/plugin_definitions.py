"""
This is a simple test plugin to demonstrate how one can use the
tvtk.plugin.scene and tvtk.plugin.browser plugins.

Plugin definitions for the Test plugin.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Standard library imports.
from os import getcwd
from os.path import abspath, dirname, join

# Enthought library imports.
import enthought
from enthought import envisage
from enthought import tvtk
import enthought.plugins.python_shell as python_shell

enthought_path = abspath(dirname(enthought.__file__))
envisage_path = abspath(dirname(envisage.__file__))
python_shell_path = abspath(dirname(python_shell.__file__))

# tvtk path.
tvtk_path = abspath(dirname(tvtk.__file__))

# My path.
test_path = abspath(getcwd())

PLUGIN_DEFINITIONS = [
    # Envisage plugins.
    join(envisage_path, 'core/core_plugin_definition.py'),
    join(envisage_path, 'resource/resource_plugin_definition.py'),
    join(envisage_path, 'action/action_plugin_definition.py'),
    join(envisage_path, 'workbench/workbench_plugin_definition.py'),
    join(envisage_path, 'workbench/action/action_plugin_definition.py'),
    join(envisage_path, 'workbench/preference/preference_plugin_definition.py'),
    # Enthought plugins.
    join(python_shell_path,
         'python_shell_plugin_definition.py'),

    join(tvtk_path, 'plugins/scene/scene_plugin_definition.py'),
    join(tvtk_path, 'plugins/scene/scene_ui_plugin_definition.py'),
    join(tvtk_path, 'plugins/browser/browser_plugin_definition.py'),
    # Application plugins.
    join(test_path, 'test_plugin_definition.py'),
   ]
