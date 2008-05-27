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

ID = 'enthought.mayavi'

open_3ds = Action(
    id            = "Open3DSFile",
    class_name    = "enthought.mayavi.action.sources.Open3DSFile",
    name          = "&3D Studio file",
    path        =  "MenuBar/File/LoadDataMenu"
)

open_image = Action(
    id            = "OpenImageFile",
    class_name    = ID + ".action.sources.OpenImageFile",
    name          = "&Image file (PNG/JPG/BMP/PNM/TIFF)",
    path="MenuBar/File/LoadDataMenu",
)

open_plot3d = Action(
    id            = "OpenPLOT3DFile",
    class_name    = ID + ".action.sources.OpenPLOT3DFile",
    name          = "&PLOT3D file",
    path="MenuBar/File/LoadDataMenu",
)

open_vrml = Action(
    id            = "OpenVRMLFile",
    class_name    = ID + ".action.sources.OpenVRMLFile",
    name          = "V&RML2 file",
    path="MenuBar/File/LoadDataMenu",
)

open_vtk = Action(
    id            = "OpenVTKFile",
    class_name    = ID + ".action.sources.OpenVTKFile",
    name          = "&VTK file",
    path="MenuBar/File/LoadDataMenu",
)

open_vtk_xml = Action(
    id            = "OpenVTKXMLFile",
    class_name    = ID + ".action.sources.OpenVTKXMLFile",
    name          = "VTK &XML file",
    path="MenuBar/File/LoadDataMenu",
)

parametric_surface = Action(
    id            = "ParametricSurfaceSource",
    class_name    = ID + ".action.sources.ParametricSurfaceSource",
    name          = "&Create Parametric surface source",
    path="MenuBar/File/LoadDataMenu",
)

point_load = Action(
    id            = "PointLoadSource",
    class_name    = ID + ".action.sources.PointLoadSource",
    name          = "Create Point &load source",
    path="MenuBar/File/LoadDataMenu",
)

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

cell_derivatives_filter = Action(
    id            = "CellDerivativesFilter",
    class_name    = ID + ".action.filters.CellDerivativesFilter",
    name          = "&CellDerivatives",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

cell_to_point_data_filter = Action(
    id            = "CellToPointDataFilter",
    class_name    = ID + ".action.filters.CellToPointDataFilter",
    name          = "&CellToPointData",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

contour_filter = Action(
    id            = "ContourFilter",
    class_name    = ID + ".action.filters.ContourFilter",
    name          = "&Contour",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)


cut_plane_filter = Action(
    id            = "CutPlaneFilter",
    class_name    = ID + ".action.filters.CutPlaneFilter",
    name          = "&CutPlane",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

decimatepro_filter = Action(
    id            = "DecimateProFilter",
    class_name    = ID + ".action.filters.DecimateProFilter",
    name          = "&DecimatePro",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

delaunay2d_filter = Action(
    id            = "Delaunay2DFilter",
    class_name    = ID + ".action.filters.Delaunay2DFilter",
    name          = "&Delaunay2D",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

delaunay3d_filter = Action(
    id            = "Delaunay3DFilter",
    class_name    = ID + ".action.filters.Delaunay3DFilter",
    name          = "Delaunay&3D",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

elevation_filter = Action(
    id            = "ElevationFilter",
    class_name    = ID + ".action.filters.ElevationFilter",
    name          = "Elevation Filter",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_edges_filter = Action(
    id            = "ExtractEdgesFilter",
    class_name    = ID + ".action.filters.ExtractEdgesFilter",
    name          = "Extract Edges",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_grid_filter = Action(
    id            = "ExtractGridFilter",
    class_name    = ID + ".action.filters.ExtractGridFilter",
    name          = "Extract &Grid",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_tensor_components_filter = Action(
    id            = "ExtractTensorComponentsFilter",
    class_name    = ID + ".action.filters.ExtractTensorComponentsFilter",
    name          = "Extract &Tensor Components",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_unstructured_grid_filter = Action(
    id            = "ExtractUnstructuredGridFilter",
    class_name    = ID + ".action.filters.ExtractUnstructuredGridFilter",
    name          = "Extract &Unstructured Grid",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_vector_norm_filter = Action(
    id            = "ExtractVectorNormFilter",
    class_name    = ID + ".action.filters.ExtractVectorNormFilter",
    name          = "Extract Vector &Norm",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_vector_components_filter = Action(
    id            = "ExtractVectorComponentsFilter",
    class_name    = ID + ".action.filters.ExtractVectorComponentsFilter",
    name          = "Extract &Vector Components",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)


gaussian_splatter_filter = Action(
    id            = "GaussianSplatterFilter",
    class_name    = ID + ".action.filters.GaussianSplatterFilter",
    name          = "Gaussian Splatter",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

greedy_terrain_decimation_filter = Action(
    id            = "GreedyTerrainDecimationFilter",
    class_name    = ID + ".action.filters.GreedyTerrainDecimationFilter",
    name          = "Greedy Terrain Decimation",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

image_data_probe_filter = Action(
    id            = "ImageDataProbeFilter",
    class_name    = ID + ".action.filters.ImageDataProbeFilter",
    name          = "&Probe data onto image data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

mask_points_filter = Action(
    id            = "MaskPointsFilter",
    class_name    = ID + ".action.filters.MaskPointsFilter",
    name          = "&Mask Points",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

point_to_cell_data_filter = Action(
    id            = "PointToCellDataFilter",
    class_name    = ID + ".action.filters.PointToCellDataFilter",
    name          = "&PointToCellData",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

poly_data_normals_filter = Action(
    id            = "PolyDataNormalsFilter",
    class_name    = ID + ".action.filters.PolyDataNormalsFilter",
    name          = "Compute &Normals",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

quadric_decimation_filter = Action(
    id            = "QuadricDecimationFilter",
    class_name    = ID + ".action.filters.QuadricDecimationFilter",
    name          = "Quadric Decimation",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

select_output_filter = Action(
    id            = "SelectOutputFilter",
    class_name    = ID + ".action.filters.SelectOutputFilter",
    name          = "&Select Output",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

set_active_attribute_filter = Action(
    id            = "SetActiveAttributeFilter",
    class_name    = ID + ".action.filters.SetActiveAttributeFilter",
    name          = "&SetActiveAttribute",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

transform_data_filter = Action(
    id            = "TransformDataFilter",
    class_name    = ID + ".action.filters.TransformDataFilter",
    name          = "T&ransform Data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

threshold_filter = Action(
    id            = "ThresholdFilter",
    class_name    = ID + ".action.filters.ThresholdFilter",
    name          = "&Threshold",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

triangle_filter = Action(
    id            = "TriangleFilter",
    class_name    = ID + ".action.filters.TriangleFilter",
    name          = "TriangleFilter",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

tube_filter = Action(
    id            = "TubeFilter",
    class_name    = ID + ".action.filters.TubeFilter",
    name          = "Tu&be",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

user_defined_filter = Action(
    id            = "UserDefinedFilter",
    class_name    = ID + ".action.filters.UserDefinedFilter",
    name          = "&UserDefined",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

vorticity_filter = Action(
    id            = "VorticityFilter",
    class_name    = ID + ".action.filters.VorticityFilter",
    name          = "&Vorticity",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

warp_scalar_filter = Action(
    id            = "WarpScalarFilter",
    class_name    = ID + ".action.filters.WarpScalarFilter",
    name          = "Warp S&calar",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

warp_vector_filter = Action(
    id            = "WarpVectorFilter",
    class_name    = ID + ".action.filters.WarpVectorFilter",
    name          = "Warp &Vector",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

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
    actions = [open_3ds, # File menu
               open_image, 
               open_plot3d,
               open_vrml,
               open_vtk,  
               open_vtk_xml,
               parametric_surface,
               point_load,
               save_viz,
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
               # Filters.
               cell_derivatives_filter,
               cell_to_point_data_filter,
               contour_filter,
               cut_plane_filter,
               decimatepro_filter,
               delaunay2d_filter,
               delaunay3d_filter,
               elevation_filter,
               extract_edges_filter,
               extract_grid_filter,
               extract_tensor_components_filter,
               extract_unstructured_grid_filter,
               extract_vector_norm_filter,
               extract_vector_components_filter,
               gaussian_splatter_filter,
               greedy_terrain_decimation_filter,
               image_data_probe_filter,
               mask_points_filter,
               point_to_cell_data_filter,
               poly_data_normals_filter,
               quadric_decimation_filter,
               select_output_filter,
               set_active_attribute_filter,
               transform_data_filter,
               threshold_filter,
               triangle_filter,
               tube_filter,
               user_defined_filter,
               vorticity_filter,
               warp_scalar_filter,
               warp_vector_filter,
               # Help.
               help_index,
              ]
