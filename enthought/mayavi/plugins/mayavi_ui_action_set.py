"""Mayavi action set for menus and actions etc.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc. 
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.ui.action.api import Action, ActionSet, Group, Menu
from enthought.mayavi.core.registry import registry

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

ID = 'enthought.mayavi'

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
axes_module = Action(
    id            = "AxesModule",
    class_name    = ID + ".action.modules.AxesModule",
    name          = "&Axes",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

contour_grid_plane_module = Action(
    id            = "ContourGridPlaneModule",
    class_name    = ID + ".action.modules.ContourGridPlaneModule",
    name          = "&ContourGridPlane",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

custom_grid_plane_module = Action(
    id            = "CustomGridPlaneModule",
    class_name    = ID + ".action.modules.CustomGridPlaneModule",
    name          = "CustomGridPlane",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

glyph_module = Action(
    id            = "GlyphModule",
    class_name    = ID + ".action.modules.GlyphModule",
    name          = "Gl&yph",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

grid_plane_module = Action(
    id            = "GridPlaneModule",
    class_name    = ID + ".action.modules.GridPlaneModule",
    name          = "&GridPlane",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

hyper_streamline_module = Action(
    id            = "HyperStreamlineModule",
    class_name    = ID + ".action.modules.HyperStreamlineModule",
    name          = "&HyperStreamline",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

image_actor_module = Action(
    id            = "ImageActorModule",
    class_name    = ID + ".action.modules.ImageActorModule",
    name          = "&ImageActor",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

image_plane_widget_module = Action(
    id            = "ImagePlaneWidgetModule",
    class_name    = ID + ".action.modules.ImagePlaneWidgetModule",
    name          = "I&magePlaneWidget",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

isosurface_module = Action(
    id            = "IsoSurfaceModule",
    class_name    = ID + ".action.modules.IsoSurfaceModule",
    name          = "&IsoSurface",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

labels_module = Action(
    id            = "LabelsModule",
    class_name    = ID + ".action.modules.LabelsModule",
    name          = "&Labels",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

orientation_axes_module = Action(
    id            = "OrientationAxesModule",
    class_name    = ID + ".action.modules.OrientationAxesModule",
    name          = "Orientation A&xes",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

outline_module = Action(
    id            = "OutlineModule",
    class_name    = ID + ".action.modules.OutlineModule",
    name          = "&Outline",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

scalar_cut_plane_module = Action(
    id            = "ScalarCutPlaneModule",
    class_name    = ID + ".action.modules.ScalarCutPlaneModule",
    name          = "Scalar Cut &Plane",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

slice_ug_module = Action(
    id            = "SliceUnstructuredGridModule",
    class_name    = ID + ".action.modules.SliceUnstructuredGridModule",
    name          = "Slice &Unstructured Grid",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

sgrid_outline_module = Action(
    id            = "StructuredGridOutlineModule",
    class_name    = ID + ".action.modules.StructuredGridOutlineModule",
    name          = "StructuredGridOutline",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

streamline_module = Action(
    id            = "StreamlineModule",
    class_name    = ID + ".action.modules.StreamlineModule",
    name          = "Stream&line",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

surface_module = Action(
    id            = "SurfaceModule",
    class_name    = ID + ".action.modules.SurfaceModule",
    name          = "&Surface",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

tensor_glyph_module = Action(
    id            = "TensorGlyphModule",
    class_name    = ID + ".action.modules.TensorGlyphModule",
    name          = "Te&nsorGlyph",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

text_module = Action(
    id            = "TextModule",
    class_name    = ID + ".action.modules.TextModule",
    name          = "&Text",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

vector_cut_plane_module = Action(
    id            = "VectorCutPlaneModule",
    class_name    = ID + ".action.modules.VectorCutPlaneModule",
    name          = "&VectorCutPlane",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

vectors_module = Action(
    id            = "VectorsModule",
    class_name    = ID + ".action.modules.VectorsModule",
    name          = "Vecto&rs",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

volume_module = Action(
    id            = "VolumeModule",
    class_name    = ID + ".action.modules.VolumeModule",
    name          = "Volum&e",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

warp_vector_cut_plane_module = Action(
    id            = "WarpVectorCutPlaneModule",
    class_name    = ID + ".action.modules.WarpVectorCutPlaneModule",
    name          = "&WarpVectorCutPlane",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)


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
               # Modules.
               axes_module,
               contour_grid_plane_module,
               custom_grid_plane_module,
               glyph_module,
               grid_plane_module,
               hyper_streamline_module,
               image_actor_module,
               image_plane_widget_module,
               isosurface_module,
               labels_module,
               orientation_axes_module,
               outline_module,
               scalar_cut_plane_module,
               slice_ug_module,
               sgrid_outline_module,
               streamline_module,
               surface_module,
               tensor_glyph_module,
               text_module,
               vector_cut_plane_module,
               vectors_module,
               volume_module,
               warp_vector_cut_plane_module,
               ] + \
               FILTER_ACTIONS + \
              [help_index,
              ]
