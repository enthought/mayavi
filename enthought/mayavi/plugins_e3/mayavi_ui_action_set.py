"""Mayavi action set for menus and actions etc.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc. 
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.ui.action.api import Action, ActionSet, Group, Menu

# This package
PKG = '.'.join(__name__.split('.')[:-1])

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

open_3ds = Action(
    id            = "Open3DSFile",
    class_name    = "enthought.mayavi.action.sources.Open3DSFile",
    name          = "&3D Studio file",
    #image         = "images/new_scene.png",
    tooltip       = "Import a 3D Studio file",
    description   = "Import a 3D Studio file",
    path        =  "MenuBar/File/LoadDataMenu"
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
    actions = [open_3ds, # File menu
              ]
