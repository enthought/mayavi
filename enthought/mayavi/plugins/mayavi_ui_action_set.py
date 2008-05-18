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
    tooltip       = "Import a 3D Studio file",
    description   = "Import a 3D Studio file",
    path        =  "MenuBar/File/LoadDataMenu"
)

open_image = Action(
    id            = "OpenImageFile",
    class_name    = ID + ".action.sources.OpenImageFile",
    name          = "&Image file (PNG/JPG/BMP/PNM/TIFF)",
    tooltip       = "Import a PNG/JPG/BMP/PNM/TIFF image",
    description   = "Import a PNG/JPG/BMP/PNM/TIFF image",
    path="MenuBar/File/LoadDataMenu",
)

open_plot3d = Action(
    id            = "OpenPLOT3DFile",
    class_name    = ID + ".action.sources.OpenPLOT3DFile",
    name          = "&PLOT3D file",
    tooltip       = "Open a PLOT3D data file",
    description   = "Open a PLOT3D data file",
    path="MenuBar/File/LoadDataMenu",
)

open_vrml = Action(
    id            = "OpenVRMLFile",
    class_name    = ID + ".action.sources.OpenVRMLFile",
    name          = "V&RML2 file",
    tooltip       = "Import a VRML2 data file",
    description   = "Import a VRML2 data file",
    path="MenuBar/File/LoadDataMenu",
)

open_vtk = Action(
    id            = "OpenVTKFile",
    class_name    = ID + ".action.sources.OpenVTKFile",
    name          = "&VTK file",
    tooltip       = "Open a VTK data file",
    description   = "Open a VTK data file",
    path="MenuBar/File/LoadDataMenu",
)

open_vtk_xml = Action(
    id            = "OpenVTKXMLFile",
    class_name    = ID + ".action.sources.OpenVTKXMLFile",
    name          = "VTK &XML file",
    tooltip       = "Open a VTK XML data file",
    description   = "Open a VTK XML data file",
    path="MenuBar/File/LoadDataMenu",
)

parametric_surface = Action(
    id            = "ParametricSurfaceSource",
    class_name    = ID + ".action.sources.ParametricSurfaceSource",
    name          = "&Create Parametric surface source",
    tooltip       = "Create a parametric surface source",
    description   = "Create a parametric surface source",
    path="MenuBar/File/LoadDataMenu",
)

point_load = Action(
    id            = "PointLoadSource",
    class_name    = ID + ".action.sources.PointLoadSource",
    name          = "Create Point &load source",
    tooltip       = "Simulates a point load on a cube of data (for tensors)",
    description   = "Simulates a point load on a cube of data (for tensors)",
    path="MenuBar/File/LoadDataMenu",
)

save_viz = Action(
    id            = "SaveVisualization",
    class_name    = ID + ".action.save_load.SaveVisualization",
    name          = "&Save Visualization",
    tooltip       = "Save current visualization",
    description   = "Save current visualization to a MayaVi2 file",
    group = "MayaviFileGroup",
    path="MenuBar/File",
)

load_viz = Action(
    id            = "LoadVisualization",
    class_name    = ID + ".action.save_load.LoadVisualization",
    name          = "&Load Visualization",
    tooltip       = "Load saved visualization",
    description   = "Load saved visualization from a MayaVi2 file",
    group = "MayaviFileGroup",
    path="MenuBar/File",
)

run_script = Action(
    id            = "RunScript",
    class_name    = ID + ".action.save_load.RunScript",
    name          = "&Run Python Script",
    tooltip       = "Execute a Python script (typically a Mayavi script)",
    description   = "Execute a Python script (typically a Mayavi script)",
    group = "MayaviFileGroup",
    path="MenuBar/File",
)
########################################
# Visualize menu items.
add_mm = Action(
    id            = "AddModuleManager",
    class_name    = ID + ".action.modules.AddModuleManager",
    name          = "&Add ModuleManager",
    tooltip       = "Add a ModuleManager to the current source/filter",
    description   = "Add a ModuleManager to the current source/filter",
    path="MenuBar/VisualizeMenu",
    after="FiltersMenu"
)

########################################
# Modules.
axes_module = Action(
    id            = "AxesModule",
    class_name    = ID + ".action.modules.AxesModule",
    name          = "&Axes",
    tooltip       = "Draw axes on the outline of input data",
    description   = "Draw cubical axes on the outline for given input",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

contour_grid_plane_module = Action(
    id            = "ContourGridPlaneModule",
    class_name    = ID + ".action.modules.ContourGridPlaneModule",
    name          = "&ContourGridPlane",
    tooltip       = "Shows a contour grid plane for the given input",
    description   = "Shows a contour grid plane for the given input",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

custom_grid_plane_module = Action(
    id            = "CustomGridPlaneModule",
    class_name    = ID + ".action.modules.CustomGridPlaneModule",
    name          = "CustomGridPlane",
    tooltip       = "Creates a highly customizable grid plane for given input",
    description   = "Creates a highly customizable grid plane for given input",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

glyph_module = Action(
    id            = "GlyphModule",
    class_name    = ID + ".action.modules.GlyphModule",
    name          = "Gl&yph",
    tooltip       = "Creates colored and scaled glyphs at at input points",
    description   = "Creates colored and scaled glyphs at at input points",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

grid_plane_module = Action(
    id            = "GridPlaneModule",
    class_name    = ID + ".action.modules.GridPlaneModule",
    name          = "&GridPlane",
    tooltip       = "Shows a grid plane for the given input",
    description   = "Shows a grid plane for the given input",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

hyper_streamline_module = Action(
    id            = "HyperStreamlineModule",
    class_name    = ID + ".action.modules.HyperStreamlineModule",
    name          = "&HyperStreamline",
    tooltip       = "Shows hyper streamlines for tensor data",
    description   = "Shows hyper streamlines for tensor data",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

image_actor_module = Action(
    id            = "ImageActorModule",
    class_name    = ID + ".action.modules.ImageActorModule",
    name          = "&ImageActor",
    tooltip       = "Shows an image actor for image data",
    description   = "Shows an image actor for image data",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

image_plane_widget_module = Action(
    id            = "ImagePlaneWidgetModule",
    class_name    = ID + ".action.modules.ImagePlaneWidgetModule",
    name          = "I&magePlaneWidget",
    #image         = "images/new_scene.png",
    tooltip       = "Shows an image plane widget for image data",
    description   = "Shows an image plane widget for image data",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

isosurface_module = Action(
    id            = "IsoSurfaceModule",
    class_name    = ID + ".action.modules.IsoSurfaceModule",
    name          = "&IsoSurface",
    #image         = "images/new_scene.png",
    tooltip       = "Creates an iso-surface for the given input",
    description   = "Creates an iso-surface for the given input",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

orientation_axes_module = Action(
    id            = "OrientationAxesModule",
    class_name    = ID + ".action.modules.OrientationAxesModule",
    name          = "Orientation A&xes",
    #image         = "images/new_scene.png",
    tooltip       = "Show an axes indicating the current orientation",
    description   = "Show an axes indicating the current orientation",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

outline_module = Action(
    id            = "OutlineModule",
    class_name    = ID + ".action.modules.OutlineModule",
    name          = "&Outline",
    #image         = "images/new_scene.png",
    tooltip       = "Draw an outline for given input",
    description   = "Draw an outline for given input",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

scalar_cut_plane_module = Action(
    id            = "ScalarCutPlaneModule",
    class_name    = ID + ".action.modules.ScalarCutPlaneModule",
    name          = "Scalar Cut &Plane",
    #image         = "images/new_scene.png",
    tooltip       = "Slice through the data with optional contours",
    description   = "Slice through the data with optional contours",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

slice_ug_module = Action(
    id            = "SliceUnstructuredGridModule",
    class_name    = ID + ".action.modules.SliceUnstructuredGridModule",
    name          = "Slice &Unstructured Grid",
    #image         = "images/new_scene.png",
    tooltip       = "Slice an unstructured grid to show cells",
    description   = "Slice an unstructured grid to show cells",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

sgrid_outline_module = Action(
    id            = "StructuredGridOutlineModule",
    class_name    = ID + ".action.modules.StructuredGridOutlineModule",
    name          = "StructuredGridOutline",
    #image         = "images/new_scene.png",
    tooltip       = "Draw a grid-conforming outline for structured grids",
    description   = "Draw a grid-conforming outline for structured grids",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

streamline_module = Action(
    id            = "StreamlineModule",
    class_name    = ID + ".action.modules.StreamlineModule",
    name          = "Stream&line",
    #image         = "images/new_scene.png",
    tooltip       = "Generate streamlines for the vectors",
    description   = "Generate streamlines for the vectors",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

surface_module = Action(
    id            = "SurfaceModule",
    class_name    = ID + ".action.modules.SurfaceModule",
    name          = "&Surface",
    #image         = "images/new_scene.png",
    tooltip       = "Creates a surface for the given input",
    description   = "Creates a surface for the given input",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

tensor_glyph_module = Action(
    id            = "TensorGlyphModule",
    class_name    = ID + ".action.modules.TensorGlyphModule",
    name          = "Te&nsorGlyph",
    tooltip       = "Displays glyphs scaled and oriented as per tensor data",
    description   = "Displays glyphs scaled and oriented as per tensor data",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

text_module = Action(
    id            = "TextModule",
    class_name    = ID + ".action.modules.TextModule",
    name          = "&Text",
    #image         = "images/new_scene.png",
    tooltip       = "Displays text on screen",
    description   = "Displays user specified text on screen",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

vector_cut_plane_module = Action(
    id            = "VectorCutPlaneModule",
    class_name    = ID + ".action.modules.VectorCutPlaneModule",
    name          = "&VectorCutPlane",
    #image         = "images/new_scene.png",
    tooltip       = "Display vectors along a cut plane",
    description   = "Display vectors along a cut plane",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

vectors_module = Action(
    id            = "VectorsModule",
    class_name    = ID + ".action.modules.VectorsModule",
    name          = "Vecto&rs",
    #image         = "images/new_scene.png",
    tooltip       = "Display input vectors using arrows or other glyphs",
    description   = "Display input vectors using arrows or other glyphs",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

volume_module = Action(
    id            = "VolumeModule",
    class_name    = ID + ".action.modules.VolumeModule",
    name          = "Volum&e",
    #image         = "images/new_scene.png",
    tooltip       = "Use volume rendering to view the scalar field",
    description   = "Use volume rendering to view the scalar field",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)

warp_vector_cut_plane_module = Action(
    id            = "WarpVectorCutPlaneModule",
    class_name    = ID + ".action.modules.WarpVectorCutPlaneModule",
    name          = "&WarpVectorCutPlane",
    #image         = "images/new_scene.png",
    tooltip       = "Warp cut plane along scaled input vectors",
    description   = "Warp cut plane along scaled input vectors",
    group = "ModulesGroup",
    path="MenuBar/VisualizeMenu/ModulesMenu"
)


########################################
# Filter items.
########################################

cell_to_point_data_filter = Action(
    id            = "CellToPointDataFilter",
    class_name    = ID + ".action.filters.CellToPointDataFilter",
    name          = "&CellToPointData",
    #image         = "images/new_scene.png",
    tooltip       = "Convert cell data to point data for the active data",
    description   = "Convert cell data to point data for the active data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

decimatepro_filter = Action(
    id            = "DecimateProFilter",
    class_name    = ID + ".action.filters.DecimateProFilter",
    name          = "&DecimatePro",
    #image         = "images/new_scene.png",
    tooltip       = "Simpilies a mesh using the DecimatePro filter",
    description   = "Simpilies a mesh using the DecimatePro filter",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

delaunay2d_filter = Action(
    id            = "Delaunay2DFilter",
    class_name    = ID + ".action.filters.Delaunay2DFilter",
    name          = "&Delaunay2D",
    #image         = "images/new_scene.png",
    tooltip       = "Perform a 2D Delaunay triangulation for the given data",
    description   = "Perform a 2D Delaunay triangulation for the given data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

delaunay3d_filter = Action(
    id            = "Delaunay3DFilter",
    class_name    = ID + ".action.filters.Delaunay3DFilter",
    name          = "Delaunay&3D",
    #image         = "images/new_scene.png",
    tooltip       = "Perform a 3D Delaunay triangulation for the given data",
    description   = "Perform a 3D Delaunay triangulation for the given data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

elevation_filter = Action(
    id            = "ElevationFilter",
    class_name    = ID + ".action.filters.ElevationFilter",
    name          = "Elevation Filter",
    #image         = "images/new_scene.png",
    tooltip       = "Creates scalar data from the elevation along a" \
                        "direction",
    description   = "Creates scalar data from the elevation along a" \
                        "direction",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_edges_filter = Action(
    id            = "ExtractEdgesFilter",
    class_name    = ID + ".action.filters.ExtractEdgesFilter",
    name          = "Extract Edges",
    #image         = "images/new_scene.png",
    tooltip       = "Turns edges into lines.",
    description   = "Turns edges into lines.",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_grid_filter = Action(
    id            = "ExtractGridFilter",
    class_name    = ID + ".action.filters.ExtractGridFilter",
    name          = "Extract &Grid",
    #image         = "images/new_scene.png",
    tooltip       = "Extract/subsample part of any structured grid",
    description   = "Extract/subsample part of any structured grid",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_tensor_components_filter = Action(
    id            = "ExtractTensorComponentsFilter",
    class_name    = ID + ".action.filters.ExtractTensorComponentsFilter",
    name          = "Extract &Tensor Components",
    tooltip       = "Extract tensor components from tensor data",
    description   = "Extract tensor components from tensor data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_unstructured_grid_filter = Action(
    id            = "ExtractUnstructuredGridFilter",
    class_name    = ID + ".action.filters.ExtractUnstructuredGridFilter",
    name          = "Extract &Unstructured Grid",
    #image         = "images/new_scene.png",
    tooltip       = "Extract part of an unstructured grid",
    description   = "Extract part of an unstructured grid",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_vector_norm_filter = Action(
    id            = "ExtractVectorNormFilter",
    class_name    = ID + ".action.filters.ExtractVectorNormFilter",
    name          = "Extract Vector &Norm",
    #image         = "images/new_scene.png",
    tooltip       = "Compute the vector norm for the current vector data",
    description   = "Compute the vector norm for the current vector data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

extract_vector_components_filter = Action(
    id            = "ExtractVectorComponentsFilter",
    class_name    = ID + ".action.filters.ExtractVectorComponentsFilter",
    name          = "Extract &Vector Components",
    tooltip       = "Extract vector components from vector data",
    description   = "Extract vector components from vector data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)


gaussian_splatter_filter = Action(
    id            = "GaussianSplatterFilter",
    class_name    = ID + ".action.filters.GaussianSplatterFilter",
    name          = "Gaussian Splatter",
    #image         = "images/new_scene.png",
    tooltip       = "Builds a structured set of points from a cloud of "\
                        "points, the local density defining the scalar",
    description   = "Builds a structured set of points from a cloud of "\
                        "points, the local density defining the scalar",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

greedy_terrain_decimation_filter = Action(
    id            = "GreedyTerrainDecimationFilter",
    class_name    = ID + ".action.filters.GreedyTerrainDecimationFilter",
    name          = "Greedy Terrain Decimation",
    #image         = "images/new_scene.png",
    tooltip       = "Simplifies image data and performs a triangulation",
    description   = "Simplifies image data and performs a triangulation",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

mask_points_filter = Action(
    id            = "MaskPointsFilter",
    class_name    = ID + ".action.filters.MaskPointsFilter",
    name          = "&Mask Points",
    #image         = "images/new_scene.png",
    tooltip       = "Mask the input points in the data",
    description   = "Mask the input points in the data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

point_to_cell_data_filter = Action(
    id            = "PointToCellDataFilter",
    class_name    = ID + ".action.filters.PointToCellDataFilter",
    name          = "&PointToCellData",
    #image         = "images/new_scene.png",
    tooltip       = "Convert point data to cell data for the active data",
    description   = "Convert point data to cell data for the active data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

poly_data_normals_filter = Action(
    id            = "PolyDataNormalsFilter",
    class_name    = ID + ".action.filters.PolyDataNormalsFilter",
    name          = "Compute &Normals",
    #image         = "images/new_scene.png",
    tooltip       = "Compute normals and smooth the appearance",
    description   = "Compute normals and smooth the appearance",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

quadric_decimation_filter = Action(
    id            = "QuadricDecimationFilter",
    class_name    = ID + ".action.filters.QuadricDecimationFilter",
    name          = "Quadric Decimation",
    #image         = "images/new_scene.png",
    tooltip       = "Simplifies a triangular mesh",
    description   = "Simplifies a triangular mesh",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

select_output_filter = Action(
    id            = "SelectOutputFilter",
    class_name    = ID + ".action.filters.SelectOutputFilter",
    name          = "&Select Output",
    #image         = "images/new_scene.png",
    tooltip       = "Choose the output of the source that should be used",
    description   = "Choose the output of the source that should be used",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

transform_data_filter = Action(
    id            = "TransformDataFilter",
    class_name    = ID + ".action.filters.TransformDataFilter",
    name          = "T&ransform Data",
    #image         = "images/new_scene.png",
    tooltip       = "Transform (rotate/translate/scale) non ImageData datasets",
    description   = "Transform (rotate/translate/scale) non ImageData datasets",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

threshold_filter = Action(
    id            = "ThresholdFilter",
    class_name    = ID + ".action.filters.ThresholdFilter",
    name          = "&Threshold",
    #image         = "images/new_scene.png",
    tooltip       = "Threshold input data based on scalar values",
    description   = "Threshold input data based on scalar values",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

triangle_filter = Action(
    id            = "TriangleFilter",
    class_name    = ID + ".action.filters.TriangleFilter",
    name          = "TriangleFilter",
    #image         = "images/new_scene.png",
    tooltip       = "Convert input polygons and triangle strips to triangles",
    description   = "Convert input polygons and triangle strips to triangles",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)
tube_filter = Action(
    id            = "TubeFilter",
    class_name    = ID + ".action.filters.TubeFilter",
    name          = "Tu&be",
    #image         = "images/new_scene.png",
    tooltip       = "Turns lines into tubes",
    description   = "Turns lines into tubes",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

warp_scalar_filter = Action(
    id            = "WarpScalarFilter",
    class_name    = ID + ".action.filters.WarpScalarFilter",
    name          = "Warp S&calar",
    #image         = "images/new_scene.png",
    tooltip       = "Move points of data along normals by the scalar data",
    description   = "Move points of data along normals by the scalar data",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

warp_vector_filter = Action(
    id            = "WarpVectorFilter",
    class_name    = ID + ".action.filters.WarpVectorFilter",
    name          = "Warp &Vector",
    #image         = "images/new_scene.png",
    tooltip       = "Move points of data along the vector data at point",
    description   = "Move points of data along the vector data at point",
    group = "FiltersGroup",
    path="MenuBar/VisualizeMenu/FiltersMenu"
)

########################################
# Help menu items.

help_index = Action(
    id            = "HelpIndex",
    class_name    = ID + ".action.help.HelpIndex",
    name          = "&User Guide",
    #image         = "images/new_scene.png",
    tooltip       = "The Mayavi2 user guide",
    description   = "The Mayavi2 user guide",
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
               cell_to_point_data_filter,
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
               mask_points_filter,
               point_to_cell_data_filter,
               poly_data_normals_filter,
               quadric_decimation_filter,
               select_output_filter,
               transform_data_filter,
               threshold_filter,
               triangle_filter,
               tube_filter,
               warp_scalar_filter,
               warp_vector_filter,
               # Help.
               help_index,
              ]
