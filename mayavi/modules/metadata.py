"""
Metadata for all modules.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Prabhu Ramachandran Enthought, Inc.
# License: BSD Style.

# Local imports.
from mayavi.core.metadata import ModuleMetadata
from mayavi.core.pipeline_info import PipelineInfo

BASE = 'mayavi.modules'


################################################################################
# Metadata.

axes_module = ModuleMetadata(
    id            = "AxesModule",
    menu_name          = "&Axes",
    class_name = BASE + '.axes.Axes',
    desc   = "Draw cubical axes on the outline for given input",
    tooltip       = "Draw axes on the outline of input data",
    help       = "Draw axes on the outline of input data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

contour_grid_plane_module = ModuleMetadata(
    id            = "ContourGridPlaneModule",
    menu_name          = "&ContourGridPlane",
    class_name = BASE + '.contour_grid_plane.ContourGridPlane',
    desc   = "Shows a contour grid plane for the given input",
    tooltip       = "Shows a contour grid plane for the given input",
    help       = "Shows a contour grid plane for the given input",
    input_info = PipelineInfo(datasets=['image_data',
                                        'structured_grid',
                                        'rectilinear_grid'],
                              attribute_types=['any'],
                              attributes=['any'])
)

custom_grid_plane_module = ModuleMetadata(
    id            = "CustomGridPlaneModule",
    menu_name          = "CustomGridPlane",
    class_name = BASE + '.custom_grid_plane.CustomGridPlane',
    desc   = "Creates a highly customizable grid plane for given input",
    tooltip       = "Creates a highly customizable grid plane for given input",
    help       = "Creates a highly customizable grid plane for given input",
    input_info = PipelineInfo(datasets=['image_data',
                                        'structured_grid',
                                        'rectilinear_grid'],
                              attribute_types=['any'],
                              attributes=['any'])
)

glyph_module = ModuleMetadata(
    id            = "GlyphModule",
    menu_name          = "Gl&yph",
    class_name = BASE + '.glyph.Glyph',
    desc   = "Creates colored and scaled glyphs at at input points",
    tooltip       = "Creates colored and scaled glyphs at at input points",
    help       = "Creates colored and scaled glyphs at at input points",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

grid_plane_module = ModuleMetadata(
    id            = "GridPlaneModule",
    menu_name          = "&GridPlane",
    class_name = BASE + '.grid_plane.GridPlane',
    desc   = "Shows a grid plane for the given input",
    tooltip       = "Shows a grid plane for the given input",
    help       = "Shows a grid plane for the given input",
    input_info = PipelineInfo(datasets=['image_data',
                                        'structured_grid',
                                        'rectilinear_grid'],
                              attribute_types=['any'],
                              attributes=['any'])
)

hyper_streamline_module = ModuleMetadata(
    id            = "HyperStreamlineModule",
    menu_name          = "&HyperStreamline",
    class_name = BASE + '.hyper_streamline.HyperStreamline',
    desc   = "Shows hyper streamlines for tensor data",
    tooltip       = "Shows hyper streamlines for tensor data",
    help       = "Shows hyper streamlines for tensor data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['tensors'])
)

image_actor_module = ModuleMetadata(
    id            = "ImageActorModule",
    menu_name          = "&ImageActor",
    class_name = BASE + '.image_actor.ImageActor',
    desc   = "Shows an image actor for image data",
    tooltip       = "Shows an image actor for image data",
    help       = "Shows an image actor for image data",
    input_info = PipelineInfo(datasets=['image_data'],
                              attribute_types=['any'],
                              attributes=['any'])
)

image_plane_widget_module = ModuleMetadata(
    id            = "ImagePlaneWidgetModule",
    menu_name          = "I&magePlaneWidget",
    class_name = BASE + '.image_plane_widget.ImagePlaneWidget',
    desc   = "Shows an image plane widget for image data",
    tooltip       = "Shows an image plane widget for image data",
    help       = "Shows an image plane widget for image data",
    input_info = PipelineInfo(datasets=['image_data'],
                              attribute_types=['any'],
                              attributes=['scalars'])
)

isosurface_module = ModuleMetadata(
    id            = "IsoSurfaceModule",
    menu_name          = "&IsoSurface",
    class_name = BASE + '.iso_surface.IsoSurface',
    desc   = "Creates an iso-surface for the given input",
    tooltip       = "Creates an iso-surface for the given input",
    help       = "Creates an iso-surface for the given input",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['scalars'])
)

labels_module = ModuleMetadata(
    id            = "LabelsModule",
    menu_name          = "&Labels",
    class_name = BASE + '.labels.Labels',
    desc   = "Display labels for active dataset or active module",
    tooltip       = "Display labels for active dataset or active module",
    help       = "Display labels for active dataset or active module",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

orientation_axes_module = ModuleMetadata(
    id            = "OrientationAxesModule",
    menu_name          = "Orientation A&xes",
    class_name = BASE + '.orientation_axes.OrientationAxes',
    desc   = "Show an axes indicating the current orientation",
    tooltip       = "Show an axes indicating the current orientation",
    help       = "Show an axes indicating the current orientation",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

outline_module = ModuleMetadata(
    id            = "OutlineModule",
    menu_name          = "&Outline",
    class_name = BASE + '.outline.Outline',
    desc   = "Draw an outline for given input",
    tooltip       = "Draw an outline for given input",
    help       = "Draw an outline for given input",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

scalar_cut_plane_module = ModuleMetadata(
    id            = "ScalarCutPlaneModule",
    menu_name          = "Scalar Cut &Plane",
    class_name = BASE + '.scalar_cut_plane.ScalarCutPlane',
    desc   = "Slice through the data with optional contours",
    tooltip       = "Slice through the data with optional contours",
    help       = "Slice through the data with optional contours",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['scalars'])
)

slice_ug_module = ModuleMetadata(
    id            = "SliceUnstructuredGridModule",
    menu_name          = "Slice &Unstructured Grid",
    class_name = BASE + '.slice_unstructured_grid.SliceUnstructuredGrid',
    desc   = "Slice an unstructured grid to show cells",
    tooltip       = "Slice an unstructured grid to show cells",
    help       = "Slice an unstructured grid to show cells",
    input_info = PipelineInfo(datasets=['unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['any'])
)

sgrid_outline_module = ModuleMetadata(
    id            = "StructuredGridOutlineModule",
    menu_name          = "StructuredGridOutline",
    class_name = BASE + '.structured_grid_outline.StructuredGridOutline',
    desc   = "Draw a grid-conforming outline for structured grids",
    tooltip       = "Draw a grid-conforming outline for structured grids",
    help       = "Draw a grid-conforming outline for structured grids",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

streamline_module = ModuleMetadata(
    id            = "StreamlineModule",
    menu_name          = "Stream&line",
    class_name = BASE + '.streamline.Streamline',
    desc   = "Generate streamlines for the vectors",
    tooltip       = "Generate streamlines for the vectors",
    help       = "Generate streamlines for the vectors",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])
)

surface_module = ModuleMetadata(
    id            = "SurfaceModule",
    menu_name          = "&Surface",
    class_name = BASE + '.surface.Surface',
    desc   = "Creates a surface for the given input",
    tooltip       = "Creates a surface for the given input",
    help       = "Creates a surface for the given input",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

tensor_glyph_module = ModuleMetadata(
    id            = "TensorGlyphModule",
    menu_name          = "Te&nsorGlyph",
    class_name = BASE + '.tensor_glyph.TensorGlyph',
    desc   = "Displays glyphs scaled and oriented as per tensor data",
    tooltip       = "Displays glyphs scaled and oriented as per tensor data",
    help       = "Displays glyphs scaled and oriented as per tensor data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['tensors'])
)

text_module = ModuleMetadata(
    id            = "TextModule",
    menu_name          = "&Text",
    class_name = BASE + '.text.Text',
    desc   = "Displays user specified text on screen",
    tooltip       = "Displays text on screen",
    help       = "Displays text on screen",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

text3d_module = ModuleMetadata(
    id            = "Text3DModule",
    menu_name          = "&Text3D",
    class_name = BASE + '.text3d.Text3D',
    desc   = "Displays user-specified text at a 3D location in the scene",
    tooltip    = "Displays user-specified text at a 3D location in the scene",
    help       = "Displays user-specified text at a 3D location in the scene",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

vector_cut_plane_module = ModuleMetadata(
    id            = "VectorCutPlaneModule",
    menu_name          = "&VectorCutPlane",
    class_name = BASE + '.vector_cut_plane.VectorCutPlane',
    desc   = "Display vectors along a cut plane",
    tooltip       = "Display vectors along a cut plane",
    help       = "Display vectors along a cut plane",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])
)

vectors_module = ModuleMetadata(
    id            = "VectorsModule",
    menu_name          = "Vecto&rs",
    class_name = BASE + '.vectors.Vectors',
    desc   = "Display input vectors using arrows or other glyphs",
    tooltip       = "Display input vectors using arrows or other glyphs",
    help       = "Display input vectors using arrows or other glyphs",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])
)

volume_module = ModuleMetadata(
    id            = "VolumeModule",
    menu_name          = "Volum&e",
    class_name = BASE + '.volume.Volume',
    desc   = "Use volume rendering to view the scalar field",
    tooltip       = "Use volume rendering to view the scalar field",
    help       = "Use volume rendering to view the scalar field",
    input_info = PipelineInfo(datasets=['image_data',
                                        'unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['scalars'])
)

warp_vector_cut_plane_module = ModuleMetadata(
    id            = "WarpVectorCutPlaneModule",
    menu_name          = "&WarpVectorCutPlane",
    class_name = BASE + '.warp_vector_cut_plane.WarpVectorCutPlane',
    desc   = "Warp cut plane along scaled input vectors",
    tooltip       = "Warp cut plane along scaled input vectors",
    help       = "Warp cut plane along scaled input vectors",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])
)


# Now collect all the modules for the mayavi registry.
modules = [axes_module,
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
           text3d_module,
           vector_cut_plane_module,
           vectors_module,
           volume_module,
           warp_vector_cut_plane_module,
          ]

