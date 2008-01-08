"""Plugin definitions for the MayaVi plugin.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Standard library imports.
from os.path import abspath, dirname, join

# Enthought library imports.
import enthought.envisage as envisage
import enthought.logger as logger
import enthought.plugins.debug as debug
import enthought.plugins.python_shell as python_shell
import enthought.plugins.text_editor as text_editor
import enthought.plugins.refresh_code as refresh_code

enthought_logger_path = abspath(dirname(logger.__file__))
enthought_debug_path = abspath(dirname(debug.__file__))
envisage_path = abspath(dirname(envisage.__file__))
python_shell_path = abspath(dirname(python_shell.__file__))
text_editor_path = abspath(dirname(text_editor.__file__))
refresh_code_path = abspath(dirname(refresh_code.__file__))

# tvtk path.
import enthought.tvtk as tvtk
tvtk_path = abspath(dirname(tvtk.__file__))


# MayaVi path.
import enthought.mayavi as mayavi
mayavi_path = abspath(dirname(mayavi.__file__))

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
    join(text_editor_path,
         'text_editor_plugin_definition.py'),
    join(refresh_code_path,
         'refresh_code_plugin_definition.py'),
    join(enthought_logger_path,
         'plugin/logger_plugin_definition.py'),
    join(enthought_debug_path,
         'fbi_plugin_definition.py'),

    join(tvtk_path, 'plugins/scene/scene_plugin_definition.py'),
    join(tvtk_path, 'plugins/scene/scene_ui_plugin_definition.py'),

    # Application plugins.
    join(mayavi_path, 'mayavi_plugin_definition.py'),
    join(mayavi_path, 'mayavi_ui_plugin_definition.py'),
   ]

NONGUI_PLUGIN_DEFINITIONS = [
    # Envisage plugins.
    join(envisage_path, 'core/core_plugin_definition.py'),
    join(envisage_path, 'resource/resource_plugin_definition.py'),
    join(envisage_path, 'action/action_plugin_definition.py'),
    join(envisage_path, 'workbench/workbench_plugin_definition.py'),

    join(tvtk_path, 'plugins/scene/scene_plugin_definition.py'),
    #join(enthought_path,
    #     'plugins/refresh_code/refresh_code_plugin_definition.py'),

    # Application plugins.
    join(mayavi_path, 'mayavi_plugin_definition.py'),
   ]


# The plugin definitions that we want to import from but don't want as part of
# the application.
INCLUDE = []
