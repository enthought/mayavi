"""
Metadata for all modules.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Prabhu Ramachandran Enthought, Inc.
# License: BSD Style.

# Local imports.
from enthought.mayavi.core.metadata import ModuleMetadata

BASE = 'enthought.mayavi.modules'


################################################################################
# Metadata.
axes_module = ModuleMetadata(
    id            = "AxesModule",
    menu_name          = "&Axes",
    class_name = BASE + '.axes.Axes',
    desc   = "Draw cubical axes on the outline for given input",
    tooltip       = "Draw axes on the outline of input data",
    help       = "Draw axes on the outline of input data",
)

contour_grid_plane_module = ModuleMetadata(
    id            = "ContourGridPlaneModule",
    menu_name          = "&ContourGridPlane",
    class_name = BASE + '.contour_grid_plane.ContourGridPlane',
    desc   = "Shows a contour grid plane for the given input",
    tooltip       = "Shows a contour grid plane for the given input",
    help       = "Shows a contour grid plane for the given input",
)

custom_grid_plane_module = ModuleMetadata(
    id            = "CustomGridPlaneModule",
    menu_name          = "CustomGridPlane",
    class_name = BASE + '.custom_grid_plane.CustomGridPlane',
    desc   = "Creates a highly customizable grid plane for given input",
    tooltip       = "Creates a highly customizable grid plane for given input",
    help       = "Creates a highly customizable grid plane for given input",
)

glyph_module = ModuleMetadata(
    id            = "GlyphModule",
    menu_name          = "Gl&yph",
    class_name = BASE + '.glyph.Glyph',
    desc   = "Creates colored and scaled glyphs at at input points",
    tooltip       = "Creates colored and scaled glyphs at at input points",
    help       = "Creates colored and scaled glyphs at at input points",
)

grid_plane_module = ModuleMetadata(
    id            = "GridPlaneModule",
    menu_name          = "&GridPlane",
    class_name = BASE + '.grid_plane.GridPlane',
    desc   = "Shows a grid plane for the given input",
    tooltip       = "Shows a grid plane for the given input",
    help       = "Shows a grid plane for the given input",
)

hyper_streamline_module = ModuleMetadata(
    id            = "HyperStreamlineModule",
    menu_name          = "&HyperStreamline",
    class_name = BASE + '.hyper_streamline.HyperStreamline',
    desc   = "Shows hyper streamlines for tensor data",
    tooltip       = "Shows hyper streamlines for tensor data",
    help       = "Shows hyper streamlines for tensor data",
)

image_actor_module = ModuleMetadata(
    id            = "ImageActorModule",
    menu_name          = "&ImageActor",
    class_name = BASE + '.image_actor.ImageActor',
    desc   = "Shows an image actor for image data",
    tooltip       = "Shows an image actor for image data",
    help       = "Shows an image actor for image data",
)

image_plane_widget_module = ModuleMetadata(
    id            = "ImagePlaneWidgetModule",
    menu_name          = "I&magePlaneWidget",
    class_name = BASE + '.image_plane_widget.ImagePlaneWidget',
    desc   = "Shows an image plane widget for image data",
    tooltip       = "Shows an image plane widget for image data",
    help       = "Shows an image plane widget for image data",
)

isosurface_module = ModuleMetadata(
    id            = "IsoSurfaceModule",
    menu_name          = "&IsoSurface",
    class_name = BASE + '.iso_surface.IsoSurface',
    desc   = "Creates an iso-surface for the given input",
    tooltip       = "Creates an iso-surface for the given input",
    help       = "Creates an iso-surface for the given input",
)

labels_module = ModuleMetadata(
    id            = "LabelsModule",
    menu_name          = "&Labels",
    class_name = BASE + '.labels.Labels',
    desc   = "Display labels for active dataset or active module",
    tooltip       = "Display labels for active dataset or active module",
    help       = "Display labels for active dataset or active module",
)

orientation_axes_module = ModuleMetadata(
    id            = "OrientationAxesModule",
    menu_name          = "Orientation A&xes",
    class_name = BASE + '.orientation_axes.OrientationAxes',
    desc   = "Show an axes indicating the current orientation",
    tooltip       = "Show an axes indicating the current orientation",
    help       = "Show an axes indicating the current orientation",
)

outline_module = ModuleMetadata(
    id            = "OutlineModule",
    menu_name          = "&Outline",
    class_name = BASE + '.outline.Outline',
    desc   = "Draw an outline for given input",
    tooltip       = "Draw an outline for given input",
    help       = "Draw an outline for given input",
)

scalar_cut_plane_module = ModuleMetadata(
    id            = "ScalarCutPlaneModule",
    menu_name          = "Scalar Cut &Plane",
    class_name = BASE + '.scalar_cut_plane.ScalarCutPlane',
    desc   = "Slice through the data with optional contours",
    tooltip       = "Slice through the data with optional contours",
    help       = "Slice through the data with optional contours",
)

slice_ug_module = ModuleMetadata(
    id            = "SliceUnstructuredGridModule",
    menu_name          = "Slice &Unstructured Grid",
    class_name = BASE + '.slice_unstructured_grid.SliceUnstructuredGrid',
    desc   = "Slice an unstructured grid to show cells",
    tooltip       = "Slice an unstructured grid to show cells",
    help       = "Slice an unstructured grid to show cells",
)

sgrid_outline_module = ModuleMetadata(
    id            = "StructuredGridOutlineModule",
    menu_name          = "StructuredGridOutline",
    class_name = BASE + '.streamline.Streamline',
    desc   = "Generate streamlines for the vectors",
    tooltip       = "Generate streamlines for the vectors",
    help       = "Generate streamlines for the vectors",
)

streamline_module = ModuleMetadata(
    id            = "StreamlineModule",
    menu_name          = "Stream&line",
    class_name = BASE + '.structured_grid_outline.StructuredGridOutline',
    desc   = "Draw a grid-conforming outline for structured grids",
    tooltip       = "Draw a grid-conforming outline for structured grids",
    help       = "Draw a grid-conforming outline for structured grids",
)

surface_module = ModuleMetadata(
    id            = "SurfaceModule",
    menu_name          = "&Surface",
    class_name = BASE + '.surface.Surface',
    desc   = "Creates a surface for the given input",
    tooltip       = "Creates a surface for the given input",
    help       = "Creates a surface for the given input",
)

tensor_glyph_module = ModuleMetadata(
    id            = "TensorGlyphModule",
    menu_name          = "Te&nsorGlyph",
    class_name = BASE + '.tensor_glyph.TensorGlyph',
    desc   = "Displays glyphs scaled and oriented as per tensor data",
    tooltip       = "Displays glyphs scaled and oriented as per tensor data",
    help       = "Displays glyphs scaled and oriented as per tensor data",
)

text_module = ModuleMetadata(
    id            = "TextModule",
    menu_name          = "&Text",
    class_name = BASE + '.text.Text',
    desc   = "Displays user specified text on screen",
    tooltip       = "Displays text on screen",
    help       = "Displays text on screen",
)

vector_cut_plane_module = ModuleMetadata(
    id            = "VectorCutPlaneModule",
    menu_name          = "&VectorCutPlane",
    class_name = BASE + '.vector_cut_plane.VectorCutPlane',
    desc   = "Display vectors along a cut plane",
    tooltip       = "Display vectors along a cut plane",
    help       = "Display vectors along a cut plane",
)

vectors_module = ModuleMetadata(
    id            = "VectorsModule",
    menu_name          = "Vecto&rs",
    class_name = BASE + '.vectors.Vectors',
    desc   = "Display input vectors using arrows or other glyphs",
    tooltip       = "Display input vectors using arrows or other glyphs",
    help       = "Display input vectors using arrows or other glyphs",
)

volume_module = ModuleMetadata(
    id            = "VolumeModule",
    menu_name          = "Volum&e",
    class_name = BASE + '.volume.Volume',
    desc   = "Use volume rendering to view the scalar field",
    tooltip       = "Use volume rendering to view the scalar field",
    help       = "Use volume rendering to view the scalar field",
)

warp_vector_cut_plane_module = ModuleMetadata(
    id            = "WarpVectorCutPlaneModule",
    menu_name          = "&WarpVectorCutPlane",
    class_name = BASE + '.warp_vector_cut_plane.WarpVectorCutPlane',
    desc   = "Warp cut plane along scaled input vectors",
    tooltip       = "Warp cut plane along scaled input vectors",
    help       = "Warp cut plane along scaled input vectors",
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
           vector_cut_plane_module,
           vectors_module,
           volume_module,
           warp_vector_cut_plane_module,
          ]

