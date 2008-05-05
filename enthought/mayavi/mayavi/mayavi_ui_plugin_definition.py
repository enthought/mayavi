"""The MayaVi plugin definition.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2007, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import sys
from os.path import join, exists

# Enthought library imports.
from enthought.util.home_directory import get_home_directory
from enthought.envisage.api import PluginDefinition
from enthought.envisage.core.core_plugin_definition import \
     ApplicationObject
from enthought.envisage.workbench.action.action_plugin_definition import \
     Action, Group, Location, Menu, WorkbenchActionSet
from enthought.envisage.workbench.workbench_plugin_definition import \
     View, Perspective, Workbench, Branding

# Local imports
from enthought.mayavi.services import IMAYAVI_ENGINE, IMAYAVI_ENGINE_VIEW

# The plugin's globally unique identifier should really be
# enthought.mayavi_ui.  However this will break the module names that
# we use to define the actions.  We therefore fix the ID in the plugin
# definition.  This ID is used as the prefix for all identifiers
# defined in this module.
ID = "enthought.mayavi"

######################################################################
# Utility functions.
def get_customizations():
    """Obtains any customizations in the form of plugin `extensions`
    and `requires` that are imported from a `mayavi_custom_ui.py`
    provided by the user for customization.  This file must be placed
    inside the `~/.mayavi2` directory.  The variables `extensions`,
    and `requires` must be a list of extensions and strings
    respectively as expected by the `PluginDefinition` class.

    Note that `~/.mayavi2` is placed in `sys.path` so make sure that
    you choose your module names carefully (so as not to override any
    common module names).  The `mayavi_custom_ui.py` can be any legal
    Python code.

    This function returns two lists containing the `extensions` and
    `requires`.
    """
    home = get_home_directory()
    m2dir = join(home, '.mayavi2')
    if exists(m2dir):
        # Add ~/.mayavi2 to sys.path.
        sys.path.append(m2dir)
        # Now try and import the user defined plugin extension.
        try:
            from mayavi_custom_ui import extensions, requires
        except ImportError:
            pass
        else:
            return extensions, requires
    
    return [], []


######################################################################
# Branding.

branding =  Branding(
    # Additional text displayed.
    about_additions = ['Author: Prabhu Ramachandran'],
    # The about box image.
    about_image = 'm2_about.jpg',
    # The application icon.
    application_icon = 'm2.ico',
    # The application name.
    application_name = 'MayaVi2'
)


######################################################################
# Actions.

groups = [Group(id = "VisualizeMenuGroup",
                location = Location(path="MenuBar",
                                    before='ToolsMenuGroup')
                ),
          ]

########################################
# Menus

open_menu = Menu(
    id     = "LoadDataMenu",
    name   = "&Load data",
    location   = Location(path="MenuBar/FileMenu/additions",
                          after="NewMenu"),
)

visualize_menu = Menu(
    id     = "VisualizeMenu",
    name   = "Visuali&ze",
    location   = Location(path="MenuBar/VisualizeMenuGroup",
                          ),
)

modules_menu = Menu(
    id     = "ModulesMenu",
    name   = "&Modules",
    location  = Location(path="MenuBar/VisualizeMenu/additions"),
)

filters_menu = Menu(
    id     = "FiltersMenu",
    name   = "&Filters",
    location   = Location(path="MenuBar/VisualizeMenu/additions",
                          after="ModulesMenu"),
)

########################################
# File menu items.

open_3ds = Action(
    id            = "Open3DSFile",
    class_name    = ID + ".action.sources.Open3DSFile",
    name          = "&3D Studio file",
    #image         = "images/new_scene.png",
    tooltip       = "Import a 3D Studio file",
    description   = "Import a 3D Studio file",
    locations     = [Location(path="MenuBar/FileMenu/LoadDataMenu/additions"),]
)

open_image = Action(
    id            = "OpenImageFile",
    class_name    = ID + ".action.sources.OpenImageFile",
    name          = "&Image file (PNG/JPG/BMP/PNM/TIFF)",
    #image         = "images/new_scene.png",
    tooltip       = "Import a PNG/JPG/BMP/PNM/TIFF image",
    description   = "Import a PNG/JPG/BMP/PNM/TIFF image",
    locations     = [Location(path="MenuBar/FileMenu/LoadDataMenu/additions"),]
)

open_plot3d = Action(
    id            = "OpenPLOT3DFile",
    class_name    = ID + ".action.sources.OpenPLOT3DFile",
    name          = "&PLOT3D file",
    #image         = "images/new_scene.png",
    tooltip       = "Open a PLOT3D data file",
    description   = "Open a PLOT3D data file",
    locations     = [Location(path="MenuBar/FileMenu/LoadDataMenu/additions"),]
)

open_vrml = Action(
    id            = "OpenVRMLFile",
    class_name    = ID + ".action.sources.OpenVRMLFile",
    name          = "V&RML2 file",
    #image         = "images/new_scene.png",
    tooltip       = "Import a VRML2 data file",
    description   = "Import a VRML2 data file",
    locations     = [Location(path="MenuBar/FileMenu/LoadDataMenu/additions"),]
)

open_vtk = Action(
    id            = "OpenVTKFile",
    class_name    = ID + ".action.sources.OpenVTKFile",
    name          = "&VTK file",
    #image         = "images/new_scene.png",
    tooltip       = "Open a VTK data file",
    description   = "Open a VTK data file",
    locations     = [Location(path="MenuBar/FileMenu/LoadDataMenu/additions"),]
)

open_vtk_xml = Action(
    id            = "OpenVTKXMLFile",
    class_name    = ID + ".action.sources.OpenVTKXMLFile",
    name          = "VTK &XML file",
    #image         = "images/new_scene.png",
    tooltip       = "Open a VTK XML data file",
    description   = "Open a VTK XML data file",
    locations     = [Location(path="MenuBar/FileMenu/LoadDataMenu/additions"),]
)

parametric_surface = Action(
    id            = "ParametricSurfaceSource",
    class_name    = ID + ".action.sources.ParametricSurfaceSource",
    name          = "&Create Parametric surface source",
    tooltip       = "Create a parametric surface source",
    description   = "Create a parametric surface source",
    locations     = [Location(path="MenuBar/FileMenu/LoadDataMenu/additions"),]
)

point_load = Action(
    id            = "PointLoadSource",
    class_name    = ID + ".action.sources.PointLoadSource",
    name          = "Create Point &load source",
    tooltip       = "Simulates a point load on a cube of data (for tensors)",
    description   = "Simulates a point load on a cube of data (for tensors)",
    locations     = [Location(path="MenuBar/FileMenu/LoadDataMenu/additions"),]
)

save_viz = Action(
    id            = "SaveVisualization",
    class_name    = ID + ".action.save_load.SaveVisualization",
    name          = "&Save Visualization",
    #image         = "images/new_scene.png",
    tooltip       = "Save current visualization",
    description   = "Save current visualization to a MayaVi2 file",
    locations     = [Location(path="MenuBar/FileMenu/additions",
                              after="LoadVisualization"),]
)

load_viz = Action(
    id            = "LoadVisualization",
    class_name    = ID + ".action.save_load.LoadVisualization",
    name          = "&Load Visualization",
    #image         = "images/new_scene.png",
    tooltip       = "Load saved visualization",
    description   = "Load saved visualization from a MayaVi2 file",
    locations     = [Location(path="MenuBar/FileMenu/additions",
                              after="SaveScene"),]
)

add_mm = Action(
    id            = "AddModuleManager",
    class_name    = ID + ".action.modules.AddModuleManager",
    name          = "&Add ModuleManager",
    tooltip       = "Add a ModuleManager to the current source/filter",
    description   = "Add a ModuleManager to the current source/filter",
    locations = [Location(path="MenuBar/VisualizeMenu/additions",
                          after="FiltersMenu"),]
)

########################################
# Visualize/Module menu items.

axes_module = Action(
    id            = "AxesModule",
    class_name    = ID + ".action.modules.AxesModule",
    name          = "&Axes",
    #image         = "images/new_scene.png",
    tooltip       = "Draw axes on the outline of input data",
    description   = "Draw cubical axes on the outline for given input",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

contour_grid_plane_module = Action(
    id            = "ContourGridPlaneModule",
    class_name    = ID + ".action.modules.ContourGridPlaneModule",
    name          = "&ContourGridPlane",
    #image         = "images/new_scene.png",
    tooltip       = "Shows a contour grid plane for the given input",
    description   = "Shows a contour grid plane for the given input",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

custom_grid_plane_module = Action(
    id            = "CustomGridPlaneModule",
    class_name    = ID + ".action.modules.CustomGridPlaneModule",
    name          = "CustomGridPlane",
    #image         = "images/new_scene.png",
    tooltip       = "Creates a highly customizable grid plane for given input",
    description   = "Creates a highly customizable grid plane for given input",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

glyph_module = Action(
    id            = "GlyphModule",
    class_name    = ID + ".action.modules.GlyphModule",
    name          = "Gl&yph",
    #image         = "images/new_scene.png",
    tooltip       = "Creates colored and scaled glyphs at at input points",
    description   = "Creates colored and scaled glyphs at at input points",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

grid_plane_module = Action(
    id            = "GridPlaneModule",
    class_name    = ID + ".action.modules.GridPlaneModule",
    name          = "&GridPlane",
    #image         = "images/new_scene.png",
    tooltip       = "Shows a grid plane for the given input",
    description   = "Shows a grid plane for the given input",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

hyper_streamline_module = Action(
    id            = "HyperStreamlineModule",
    class_name    = ID + ".action.modules.HyperStreamlineModule",
    name          = "&HyperStreamline",
    tooltip       = "Shows hyper streamlines for tensor data",
    description   = "Shows hyper streamlines for tensor data",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

image_actor_module = Action(
    id            = "ImageActorModule",
    class_name    = ID + ".action.modules.ImageActorModule",
    name          = "&ImageActor",
    #image         = "images/new_scene.png",
    tooltip       = "Shows an image actor for image data",
    description   = "Shows an image actor for image data",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

image_plane_widget_module = Action(
    id            = "ImagePlaneWidgetModule",
    class_name    = ID + ".action.modules.ImagePlaneWidgetModule",
    name          = "I&magePlaneWidget",
    #image         = "images/new_scene.png",
    tooltip       = "Shows an image plane widget for image data",
    description   = "Shows an image plane widget for image data",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

isosurface_module = Action(
    id            = "IsoSurfaceModule",
    class_name    = ID + ".action.modules.IsoSurfaceModule",
    name          = "&IsoSurface",
    #image         = "images/new_scene.png",
    tooltip       = "Creates an iso-surface for the given input",
    description   = "Creates an iso-surface for the given input",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

orientation_axes_module = Action(
    id            = "OrientationAxesModule",
    class_name    = ID + ".action.modules.OrientationAxesModule",
    name          = "Orientation A&xes",
    #image         = "images/new_scene.png",
    tooltip       = "Show an axes indicating the current orientation",
    description   = "Show an axes indicating the current orientation",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

outline_module = Action(
    id            = "OutlineModule",
    class_name    = ID + ".action.modules.OutlineModule",
    name          = "&Outline",
    #image         = "images/new_scene.png",
    tooltip       = "Draw an outline for given input",
    description   = "Draw an outline for given input",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

scalar_cut_plane_module = Action(
    id            = "ScalarCutPlaneModule",
    class_name    = ID + ".action.modules.ScalarCutPlaneModule",
    name          = "Scalar Cut &Plane",
    #image         = "images/new_scene.png",
    tooltip       = "Slice through the data with optional contours",
    description   = "Slice through the data with optional contours",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

slice_ug_module = Action(
    id            = "SliceUnstructuredGridModule",
    class_name    = ID + ".action.modules.SliceUnstructuredGridModule",
    name          = "Slice &Unstructured Grid",
    #image         = "images/new_scene.png",
    tooltip       = "Slice an unstructured grid to show cells",
    description   = "Slice an unstructured grid to show cells",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

sgrid_outline_module = Action(
    id            = "StructuredGridOutlineModule",
    class_name    = ID + ".action.modules.StructuredGridOutlineModule",
    name          = "StructuredGridOutline",
    #image         = "images/new_scene.png",
    tooltip       = "Draw a grid-conforming outline for structured grids",
    description   = "Draw a grid-conforming outline for structured grids",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

streamline_module = Action(
    id            = "StreamlineModule",
    class_name    = ID + ".action.modules.StreamlineModule",
    name          = "Stream&line",
    #image         = "images/new_scene.png",
    tooltip       = "Generate streamlines for the vectors",
    description   = "Generate streamlines for the vectors",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

surface_module = Action(
    id            = "SurfaceModule",
    class_name    = ID + ".action.modules.SurfaceModule",
    name          = "&Surface",
    #image         = "images/new_scene.png",
    tooltip       = "Creates a surface for the given input",
    description   = "Creates a surface for the given input",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

tensor_glyph_module = Action(
    id            = "TensorGlyphModule",
    class_name    = ID + ".action.modules.TensorGlyphModule",
    name          = "Te&nsorGlyph",
    tooltip       = "Displays glyphs scaled and oriented as per tensor data",
    description   = "Displays glyphs scaled and oriented as per tensor data",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

text_module = Action(
    id            = "TextModule",
    class_name    = ID + ".action.modules.TextModule",
    name          = "&Text",
    #image         = "images/new_scene.png",
    tooltip       = "Displays text on screen",
    description   = "Displays user specified text on screen",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

vector_cut_plane_module = Action(
    id            = "VectorCutPlaneModule",
    class_name    = ID + ".action.modules.VectorCutPlaneModule",
    name          = "&VectorCutPlane",
    #image         = "images/new_scene.png",
    tooltip       = "Display vectors along a cut plane",
    description   = "Display vectors along a cut plane",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

vectors_module = Action(
    id            = "VectorsModule",
    class_name    = ID + ".action.modules.VectorsModule",
    name          = "Vecto&rs",
    #image         = "images/new_scene.png",
    tooltip       = "Display input vectors using arrows or other glyphs",
    description   = "Display input vectors using arrows or other glyphs",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

volume_module = Action(
    id            = "VolumeModule",
    class_name    = ID + ".action.modules.VolumeModule",
    name          = "Volum&e",
    #image         = "images/new_scene.png",
    tooltip       = "Use volume rendering to view the scalar field",
    description   = "Use volume rendering to view the scalar field",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

warp_vector_cut_plane_module = Action(
    id            = "WarpVectorCutPlaneModule",
    class_name    = ID + ".action.modules.WarpVectorCutPlaneModule",
    name          = "&WarpVectorCutPlane",
    #image         = "images/new_scene.png",
    tooltip       = "Warp cut plane along scaled input vectors",
    description   = "Warp cut plane along scaled input vectors",
    locations = [Location(path="MenuBar/VisualizeMenu/ModulesMenu/additions"),]
)

cell_to_point_data_filter = Action(
    id            = "CellToPointDataFilter",
    class_name    = ID + ".action.filters.CellToPointDataFilter",
    name          = "&CellToPointData",
    #image         = "images/new_scene.png",
    tooltip       = "Convert cell data to point data for the active data",
    description   = "Convert cell data to point data for the active data",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

decimatepro_filter = Action(
    id            = "DecimateProFilter",
    class_name    = ID + ".action.filters.DecimateProFilter",
    name          = "&DecimatePro",
    #image         = "images/new_scene.png",
    tooltip       = "Simpilies a mesh using the DecimatePro filter",
    description   = "Simpilies a mesh using the DecimatePro filter",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

delaunay2d_filter = Action(
    id            = "Delaunay2DFilter",
    class_name    = ID + ".action.filters.Delaunay2DFilter",
    name          = "&Delaunay2D",
    #image         = "images/new_scene.png",
    tooltip       = "Perform a 2D Delaunay triangulation for the given data",
    description   = "Perform a 2D Delaunay triangulation for the given data",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

delaunay3d_filter = Action(
    id            = "Delaunay3DFilter",
    class_name    = ID + ".action.filters.Delaunay3DFilter",
    name          = "Delaunay&3D",
    #image         = "images/new_scene.png",
    tooltip       = "Perform a 3D Delaunay triangulation for the given data",
    description   = "Perform a 3D Delaunay triangulation for the given data",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
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
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

extract_edges_filter = Action(
    id            = "ExtractEdgesFilter",
    class_name    = ID + ".action.filters.ExtractEdgesFilter",
    name          = "Extract Edges",
    #image         = "images/new_scene.png",
    tooltip       = "Turns edges into lines.",
    description   = "Turns edges into lines.",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

extract_grid_filter = Action(
    id            = "ExtractGridFilter",
    class_name    = ID + ".action.filters.ExtractGridFilter",
    name          = "Extract &Grid",
    #image         = "images/new_scene.png",
    tooltip       = "Extract/subsample part of any structured grid",
    description   = "Extract/subsample part of any structured grid",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

extract_tensor_components_filter = Action(
    id            = "ExtractTensorComponentsFilter",
    class_name    = ID + ".action.filters.ExtractTensorComponentsFilter",
    name          = "Extract &Tensor Components",
    tooltip       = "Extract tensor components from tensor data",
    description   = "Extract tensor components from tensor data",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

extract_unstructured_grid_filter = Action(
    id            = "ExtractUnstructuredGridFilter",
    class_name    = ID + ".action.filters.ExtractUnstructuredGridFilter",
    name          = "Extract &Unstructured Grid",
    #image         = "images/new_scene.png",
    tooltip       = "Extract part of an unstructured grid",
    description   = "Extract part of an unstructured grid",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

extract_vector_norm_filter = Action(
    id            = "ExtractVectorNormFilter",
    class_name    = ID + ".action.filters.ExtractVectorNormFilter",
    name          = "Extract &Vector Norm",
    #image         = "images/new_scene.png",
    tooltip       = "Compute the vector norm for the current vector data",
    description   = "Compute the vector norm for the current vector data",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
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
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

greedy_terrain_decimation_filter = Action(
    id            = "GreedyTerrainDecimationFilter",
    class_name    = ID + ".action.filters.GreedyTerrainDecimationFilter",
    name          = "Greedy Terrain Decimation",
    #image         = "images/new_scene.png",
    tooltip       = "Simplifies image data and performs a triangulation",
    description   = "Simplifies image data and performs a triangulation",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

mask_points_filter = Action(
    id            = "MaskPointsFilter",
    class_name    = ID + ".action.filters.MaskPointsFilter",
    name          = "&Mask Points",
    #image         = "images/new_scene.png",
    tooltip       = "Mask the input points in the data",
    description   = "Mask the input points in the data",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

point_to_cell_data_filter = Action(
    id            = "PointToCellDataFilter",
    class_name    = ID + ".action.filters.PointToCellDataFilter",
    name          = "&PointToCellData",
    #image         = "images/new_scene.png",
    tooltip       = "Convert point data to cell data for the active data",
    description   = "Convert point data to cell data for the active data",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

poly_data_normals_filter = Action(
    id            = "PolyDataNormalsFilter",
    class_name    = ID + ".action.filters.PolyDataNormalsFilter",
    name          = "Compute &Normals",
    #image         = "images/new_scene.png",
    tooltip       = "Compute normals and smooth the appearance",
    description   = "Compute normals and smooth the appearance",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

quadric_decimation_filter = Action(
    id            = "QuadricDecimationFilter",
    class_name    = ID + ".action.filters.QuadricDecimationFilter",
    name          = "Quadric Decimation",
    #image         = "images/new_scene.png",
    tooltip       = "Simplifies a triangular mesh",
    description   = "Simplifies a triangular mesh",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

transform_data_filter = Action(
    id            = "TransformDataFilter",
    class_name    = ID + ".action.filters.TransformDataFilter",
    name          = "T&ransform Data",
    #image         = "images/new_scene.png",
    tooltip       = "Transform (rotate/translate/scale) non ImageData datasets",
    description   = "Transform (rotate/translate/scale) non ImageData datasets",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

threshold_filter = Action(
    id            = "ThresholdFilter",
    class_name    = ID + ".action.filters.ThresholdFilter",
    name          = "&Threshold",
    #image         = "images/new_scene.png",
    tooltip       = "Threshold input data based on scalar values",
    description   = "Threshold input data based on scalar values",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

triangle_filter = Action(
    id            = "TriangleFilter",
    class_name    = ID + ".action.filters.TriangleFilter",
    name          = "TriangleFilter",
    #image         = "images/new_scene.png",
    tooltip       = "Convert input polygons and triangle strips to triangles",
    description   = "Convert input polygons and triangle strips to triangles",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)
tube_filter = Action(
    id            = "TubeFilter",
    class_name    = ID + ".action.filters.TubeFilter",
    name          = "Tu&be",
    #image         = "images/new_scene.png",
    tooltip       = "Turns lines into tubes",
    description   = "Turns lines into tubes",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

warp_scalar_filter = Action(
    id            = "WarpScalarFilter",
    class_name    = ID + ".action.filters.WarpScalarFilter",
    name          = "Warp S&calar",
    #image         = "images/new_scene.png",
    tooltip       = "Move points of data along normals by the scalar data",
    description   = "Move points of data along normals by the scalar data",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
)

warp_vector_filter = Action(
    id            = "WarpVectorFilter",
    class_name    = ID + ".action.filters.WarpVectorFilter",
    name          = "Warp &Vector",
    #image         = "images/new_scene.png",
    tooltip       = "Move points of data along the vector data at point",
    description   = "Move points of data along the vector data at point",
    locations = [Location(path="MenuBar/VisualizeMenu/FiltersMenu/additions"),]
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
    locations = [Location(path="MenuBar/HelpMenu/additions"),]
)

########################################
# List of all actions.

action_set = WorkbenchActionSet(
    id = ID + '.action_set',
    name = 'Mayavi2ActionSet',
    groups = groups,
    menus = [open_menu,
             visualize_menu,
             modules_menu,
             filters_menu
             ],

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
               gaussian_splatter_filter,
               greedy_terrain_decimation_filter,
               mask_points_filter,
               point_to_cell_data_filter,
               poly_data_normals_filter,
               quadric_decimation_filter,
               transform_data_filter,
               threshold_filter,
               triangle_filter,
               tube_filter,
               warp_scalar_filter,
               warp_vector_filter,
               help_index,
               ]
)

######################################################################
# Views.

engine_view_object = ApplicationObject(class_name=ID +'.view.engine_view.EngineView',
                                       uol='service://' + IMAYAVI_ENGINE_VIEW)

views = [View(name="MayaVi",
              id=ID + ".view.engine_view.EngineView",
              uol='service://' + IMAYAVI_ENGINE_VIEW,
              position="left",
              ),
         View(id=ID + '.current_selection',
              uol='service://' + IMAYAVI_ENGINE,
              name="MayaVi object editor",
              traits_ui_view = 'current_selection_view',
              position='bottom'
              )
         ]

# Perspectives.
perspectives = [
    Perspective(
        id = ID + ".default_perspective",
        name = 'Mayavi',

        contents = [
            Perspective.Item(
                id = ID + '.view.engine_view.EngineView',
                position = 'left'
            ),

            Perspective.Item(
                id = ID + '.current_selection',
                position = 'bottom',
                relative_to = ID + '.view.engine_view.EngineView'
            ),

            Perspective.Item(
                id = 'enthought.logger.plugin.view.logger_view.LoggerView',
                position = 'bottom'
            ),

            Perspective.Item(
                id = 'enthought.plugins.python_shell.view.PythonShellView',
                position = 'with',
                relative_to = 'enthought.logger.plugin.view.logger_view.LoggerView'
            ),

        ]
    )
]

workbench = Workbench(views=views, perspectives=perspectives,
                      default_perspective=ID + '.default_perspective')

requires = ["enthought.envisage.workbench",
            "enthought.plugins.python_shell",
            "enthought.tvtk.plugins.scene",
             ]
extensions = [engine_view_object, action_set, workbench, branding]


######################################################################
# Handle user customizations.
custom_ext, custom_req = get_customizations()
extensions.extend(custom_ext)
requires.extend(custom_req)


######################################################################
# The MayaVi UI plugin definition.
PluginDefinition(
    # This plugins unique identifier.
    id = ID + '_ui',

    # General info.
    name = "The MayaVi UI Plugin",
    version = "2.0",
    provider_name = "Prabhu Ramachandran",
    provider_url = "www.enthought.com",
    enabled = True,
    autostart = True,

    # Id's of plugin that this one requires.
    requires = requires + ['enthought.mayavi'],
    
    # The extension points that we provide.
    extension_points = [],

    # The contributions that this plugin makes to extension points offered by
    # either itself or other plugins.
    extensions = extensions
)
