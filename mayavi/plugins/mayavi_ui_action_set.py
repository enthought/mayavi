"""Mayavi action set for menus and actions etc.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from envisage.ui.action.api import Action, ActionSet, Group, Menu
from mayavi.core.registry import registry

########################################
# Groups

file_group = Group(
    id='MayaviFileGroup',
    path='MenuBar/File',
    before='ExitGroup'
)

visualize_group = Group(
    id='VisualizeGroup',
    path='MenuBar/VisualizeMenu',
)

modules_group = Group(
    id='ModulesGroup',
    path='MenuBar/VisualizeMenu/ModulesMenu',
)

filters_group = Group(
    id='FiltersGroup',
    path='MenuBar/VisualizeMenu/FiltersMenu',
)
########################################
# Menus

open_menu = Menu(
    id     = "LoadDataMenu",
    name   = "&Load data",
    path = 'MenuBar/File',
    group='MayaviFileGroup'
)

visualize_menu = Menu(
    id     = "VisualizeMenu",
    name   = "Visuali&ze",
    path = "MenuBar",
    before = "View"
)

modules_menu = Menu(
    id     = "ModulesMenu",
    name   = "&Modules",
    path="MenuBar/VisualizeMenu",
)

filters_menu = Menu(
    id     = "FiltersMenu",
    name   = "&Filters",
    path="MenuBar/VisualizeMenu",
    after="ModulesMenu",
)

########################################
# File menu items.

ID = 'mayavi'

####################
# Source actions.

open_file = Action(
    id            = "OpenFile",
    class_name    = ID + ".action.sources.OpenFile",
    name          = "&Open file ...",
    path        =  "MenuBar/File/LoadDataMenu"
)

# Automatic source generation for non-open file related sources.
SOURCE_ACTIONS = [open_file]

for src in registry.sources:
    if len(src.extensions) == 0:
        action = Action(id=src.id,
                        class_name=ID + ".action.sources." + src.id,
                        name= src.menu_name,
                        path="MenuBar/File/LoadDataMenu"
                        )
        SOURCE_ACTIONS.append(action)

####################
# Save/load actions.

save_viz = Action(
    id            = "SaveVisualization",
    class_name    = ID + ".action.save_load.SaveVisualization",
    name          = "&Save Visualization",
    group = "MayaviFileGroup",
    path="MenuBar/File",
)

load_viz = Action(
    id            = "LoadVisualization",
    class_name    = ID + ".action.save_load.LoadVisualization",
    name          = "&Load Visualization",
    group = "MayaviFileGroup",
    path="MenuBar/File",
)

run_script = Action(
    id            = "RunScript",
    class_name    = ID + ".action.save_load.RunScript",
    name          = "&Run Python Script",
    group = "MayaviFileGroup",
    path="MenuBar/File",
)

########################################
# Visualize menu items.

add_mm = Action(
    id            = "AddModuleManager",
    class_name    = ID + ".action.modules.AddModuleManager",
    name          = "&Add ModuleManager",
    path="MenuBar/VisualizeMenu",
    after="FiltersMenu"
)

########################################
# Modules.

MODULE_ACTIONS = []
for module in registry.modules:
    action = Action(id=module.id,
                    class_name=ID + ".action.modules." + module.id,
                    name= module.menu_name,
                    group = "ModulesGroup",
                    path="MenuBar/VisualizeMenu/ModulesMenu"
                    )
    MODULE_ACTIONS.append(action)

########################################
# Filter items.
########################################
FILTER_ACTIONS = []
for filter in registry.filters:
    action = Action(id=filter.id,
                    class_name=ID + ".action.filters." + filter.id,
                    name= filter.menu_name,
                    group = "FiltersGroup",
                    path="MenuBar/VisualizeMenu/FiltersMenu"
                    )
    FILTER_ACTIONS.append(action)

########################################
# Help menu items.

help_index = Action(
    id            = "HelpIndex",
    class_name    = ID + ".action.help.HelpIndex",
    name          = "&User Guide",
    path="MenuBar/Help"
)


tvtk_class_browser = Action(
    id            = "TVTKClassBrowser",
    class_name    = ID + ".action.help.TVTKClassBrowser",
    name          = "&VTK Class Browser",
    path          = "MenuBar/Help",
)


################################################################################
# `MayaviUIActionSet` class.
################################################################################
class MayaviUIActionSet(ActionSet):
    """ The default action set for the mayavi UI plugin. """

    groups  = [file_group,
               visualize_group,
               modules_group,
               filters_group,
               ]
    menus = [open_menu,
             visualize_menu,
             modules_menu,
             filters_menu
             ]
    actions = SOURCE_ACTIONS + \
              [save_viz, # Save load actions.
               load_viz,
               run_script,
               # Add module manager.
               add_mm,
              ] + \
              MODULE_ACTIONS + \
              FILTER_ACTIONS + \
              [help_index,
               tvtk_class_browser,
              ]
