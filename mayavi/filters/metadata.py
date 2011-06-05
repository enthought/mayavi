"""
Metadata for all filters.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008, Prabhu Ramachandran Enthought, Inc.
# License: BSD Style.

# Local imports.
from mayavi.core.metadata import FilterMetadata
from mayavi.core.pipeline_info import PipelineInfo

BASE = 'mayavi.filters'

################################################################################
# Factory functions.
################################################################################
def make_user_defined_filter():
    from mayavi.filters.user_defined import UserDefined
    f = UserDefined()
    f.setup_filter()
    return f


################################################################################
# Metadata.

cell_derivatives_filter = FilterMetadata(
    id            = "CellDerivativesFilter",
    menu_name          = "&CellDerivatives",
    class_name = BASE + '.cell_derivatives.CellDerivatives',
    tooltip = "Calculate derivatives of input point/vector data and output these as cell data",
    desc = "Calculate derivatives of input point/vector data and output these as cell data",
    help = "Calculate derivatives of input point/vector data and output these as cell data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

cell_to_point_data_filter = FilterMetadata(
    id            = "CellToPointDataFilter",
    menu_name          = "&CellToPointData",
    class_name = BASE + '.cell_to_point_data.CellToPointData',
    tooltip = "Convert cell data to point data for the active data",
    desc = "Convert cell data to point data for the active data",
    help = "Convert cell data to point data for the active data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['cell'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

clip_filter = FilterMetadata(
    id            = "DataSetClipperFilter",
    menu_name          = "&DataSet Clipper",
    class_name = BASE + '.data_set_clipper.DataSetClipper',
    tooltip = "Clip the input dataset",
    desc = "Clip the input dataset",
    help = "Clip the input dataset",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])
)


contour_filter = FilterMetadata(
    id            = "ContourFilter",
    menu_name          = "&Contour",
    class_name = BASE + '.contour.Contour',
    tooltip = "Compute contours of the input dataset",
    desc = "Compute contours of the input dataset",
    help = "Compute contours of the input dataset",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['point'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)


cut_plane_filter = FilterMetadata(
    id            = "CutPlaneFilter",
    menu_name          = "&CutPlane",
    class_name = BASE + '.cut_plane.CutPlane',
    tooltip = "Slice the input dataset with a cut plane",
    desc = "Slice the input dataset with a cut plane",
    help = "Slice the input dataset with a cut plane",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

decimatepro_filter = FilterMetadata(
    id            = "DecimateProFilter",
    menu_name          = "&DecimatePro",
    class_name = BASE + '.decimatepro.DecimatePro',
    tooltip = "Simpilies a mesh using the DecimatePro filter",
    desc = "Simpilies a mesh using the DecimatePro filter",
    help = "Simpilies a mesh using the DecimatePro filter",
    input_info = PipelineInfo(datasets=['poly_data'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

delaunay2d_filter = FilterMetadata(
    id            = "Delaunay2DFilter",
    menu_name          = "&Delaunay2D",
    class_name = BASE + '.delaunay2d.Delaunay2D',
    tooltip = "Perform a 2D Delaunay triangulation for the given data",
    desc = "Perform a 2D Delaunay triangulation for the given data",
    help = "Perform a 2D Delaunay triangulation for the given data",
    input_info = PipelineInfo(datasets=['structured_grid', 'poly_data',
                                        'unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

delaunay3d_filter = FilterMetadata(
    id            = "Delaunay3DFilter",
    menu_name          = "Delaunay&3D",
    class_name = BASE + '.delaunay3d.Delaunay3D',
    tooltip = "Perform a 3D Delaunay triangulation for the given data",
    desc = "Perform a 3D Delaunay triangulation for the given data",
    help = "Perform a 3D Delaunay triangulation for the given data",
    input_info = PipelineInfo(datasets=['structured_grid', 'poly_data',
                                        'unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])
)

elevation_filter = FilterMetadata(
    id            = "ElevationFilter",
    menu_name          = "Elevation Filter",
    class_name = BASE + '.elevation_filter.ElevationFilter',
    tooltip = "Creates scalar data from the elevation along a direction",
    desc = "Creates scalar data from the elevation along a direction",
    help = "Creates scalar data from the elevation along a direction",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

extract_edges_filter = FilterMetadata(
    id            = "ExtractEdgesFilter",
    menu_name          = "Extract Edges",
    class_name = BASE + '.extract_edges.ExtractEdges',
    tooltip = "Turns edges into lines.",
    desc = "Turns edges into lines.",
    help = "Turns edges into lines.",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

extract_grid_filter = FilterMetadata(
    id            = "ExtractGridFilter",
    menu_name          = "Extract &Grid",
    class_name = BASE + '.extract_grid.ExtractGrid',
    tooltip = "Extract/subsample part of any structured grid",
    desc = "Extract/subsample part of any structured grid",
    help = "Extract/subsample part of any structured grid",
    input_info = PipelineInfo(datasets=['image_data',
                                        'rectilinear_grid',
                                        'structured_grid'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['image_data',
                                         'rectilinear_grid',
                                         'structured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])
)

extract_tensor_components_filter = FilterMetadata(
    id            = "ExtractTensorComponentsFilter",
    menu_name          = "Extract &Tensor Components",
    class_name = BASE + '.extract_tensor_components.ExtractTensorComponents',
    tooltip = "Extract tensor components from tensor data",
    desc = "Extract tensor components from tensor data",
    help = "Extract tensor components from tensor data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['tensors']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

extract_unstructured_grid_filter = FilterMetadata(
    id            = "ExtractUnstructuredGridFilter",
    menu_name          = "Extract &Unstructured Grid",
    class_name = BASE + '.extract_unstructured_grid.ExtractUnstructuredGrid',
    tooltip = "Extract part of an unstructured grid",
    desc = "Extract part of an unstructured grid",
    help = "Extract part of an unstructured grid",
    input_info = PipelineInfo(datasets=['unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])
)

extract_vector_norm_filter = FilterMetadata(
    id            = "ExtractVectorNormFilter",
    menu_name          = "Extract Vector &Norm",
    class_name = BASE + '.extract_vector_norm.ExtractVectorNorm',
    tooltip = "Compute the vector norm for the current vector data",
    desc = "Compute the vector norm for the current vector data",
    help = "Compute the vector norm for the current vector data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

extract_vector_components_filter = FilterMetadata(
    id            = "ExtractVectorComponentsFilter",
    menu_name          = "Extract &Vector Components",
    class_name = BASE + '.extract_vector_components.ExtractVectorComponents',
    tooltip = "Extract vector components from vector data",
    desc = "Extract vector components from vector data",
    help = "Extract vector components from vector data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

gaussian_splatter_filter = FilterMetadata(
    id            = "GaussianSplatterFilter",
    menu_name          = "Gaussian Splatter",
    class_name = BASE + '.gaussian_splatter.GaussianSplatter',
    tooltip = "Builds a structured set of points from a cloud of points, the local density defining the scalar",
    desc = "Builds a structured set of points from a cloud of points, the local density defining the scalar",
    help = """Builds a structured set of points from a cloud of points,
    the local density defining the scalar.  It is essentially equivalent
    to a 3D Gaussian kernel density estimate.""",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['image_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

greedy_terrain_decimation_filter = FilterMetadata(
    id            = "GreedyTerrainDecimationFilter",
    menu_name          = "Greedy Terrain Decimation",
    class_name = BASE + '.greedy_terrain_decimation.GreedyTerrainDecimation',
    tooltip = "Simplifies image data and performs a triangulation",
    desc = "Simplifies image data and performs a triangulation",
    help = "Simplifies image data and performs a triangulation",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

image_change_information_filter = FilterMetadata(
    id            = "ImageChangeInformationFilter",
    menu_name          = "Change &ImageData information",
    class_name = BASE + '.image_change_information.ImageChangeInformation',
    tooltip = "Change the origin, spacing and extents of an image dataset",
    desc = "Change the origin, spacing and extents of an image dataset",
    help = "Change the origin, spacing and extents of an image dataset",
    input_info = PipelineInfo(datasets=['image_data'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['image_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

image_data_probe_filter = FilterMetadata(
    id            = "ImageDataProbeFilter",
    menu_name          = "&Probe data onto image data",
    class_name = BASE + '.image_data_probe.ImageDataProbe',
    tooltip = "Samples arbitrary datasets onto an image dataset (cube of data)",
    desc = "Samples arbitrary datasets onto an image dataset (cube of data)",
    help = "Samples arbitrary datasets onto an image dataset (cube of data)",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['image_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

mask_points_filter = FilterMetadata(
    id            = "MaskPointsFilter",
    menu_name          = "&Mask Points",
    class_name = BASE + '.mask_points.MaskPoints',
    tooltip = "Mask the input points in the data",
    desc = "Mask the input points in the data",
    help = "Mask the input points in the data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

point_to_cell_data_filter = FilterMetadata(
    id            = "PointToCellDataFilter",
    menu_name          = "&PointToCellData",
    class_name = BASE + '.point_to_cell_data.PointToCellData',
    tooltip = "Convert point data to cell data for the active data",
    desc = "Convert point data to cell data for the active data",
    help = "Convert point data to cell data for the active data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['point'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['cell'],
                               attributes=['any'])
)

poly_data_normals_filter = FilterMetadata(
    id            = "PolyDataNormalsFilter",
    menu_name          = "Compute &Normals",
    class_name = BASE + '.poly_data_normals.PolyDataNormals',
    tooltip = "Compute normals and smooth the appearance",
    desc = "Compute normals and smooth the appearance",
    help = "Compute normals and smooth the appearance",
    input_info = PipelineInfo(datasets=['poly_data'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

quadric_decimation_filter = FilterMetadata(
    id            = "QuadricDecimationFilter",
    menu_name          = "Quadric Decimation",
    class_name = BASE + '.quadric_decimation.QuadricDecimation',
    tooltip = "Simplifies a triangular mesh",
    desc = "Simplifies a triangular mesh",
    help = "Simplifies a triangular mesh",
    input_info = PipelineInfo(datasets=['poly_data'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

select_output_filter = FilterMetadata(
    id            = "SelectOutputFilter",
    menu_name          = "&Select Output",
    class_name = BASE + '.select_output.SelectOutput',
    tooltip = "Choose the output of the source that should be used",
    desc = "Choose the output of the source that should be used",
    help = "Choose the output of the source that should be used",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

set_active_attribute_filter = FilterMetadata(
    id            = "SetActiveAttributeFilter",
    menu_name          = "&SetActiveAttribute",
    class_name = BASE + '.set_active_attribute.SetActiveAttribute',
    tooltip = "Set the active attribute (scalar/vector/tensor) to use",
    desc = "Set the active attribute (scalar/vector/tensor) to use",
    help = "Set the active attribute (scalar/vector/tensor) to use",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

stripper = FilterMetadata(
    id            = "Stripper",
    menu_name          = "Stripper",
    class_name = BASE + '.stripper.Stripper',
    tooltip = "Regularizes surfaces by creating triangle strips",
    desc =    "Regularizes surfaces by creating triangle strips",
    help =    "Regularizes surfaces by creating triangle strips",
    input_info = PipelineInfo(datasets=['poly_data'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

transform_data_filter = FilterMetadata(
    id            = "TransformDataFilter",
    menu_name          = "T&ransform Data",
    class_name = BASE + '.transform_data.TransformData',
    tooltip = "Transform (rotate/translate/scale) non ImageData datasets",
    desc = "Transform (rotate/translate/scale) non ImageData datasets",
    help = "Transform (rotate/translate/scale) non ImageData datasets",
    input_info = PipelineInfo(datasets=['poly_data',
                                        'structured_grid',
                                        'unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data',
                                         'structured_grid',
                                         'unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])
)

threshold_filter = FilterMetadata(
    id            = "ThresholdFilter",
    menu_name          = "&Threshold",
    class_name = BASE + '.threshold.Threshold',
    tooltip = "Threshold input data based on scalar values",
    desc = "Threshold input data based on scalar values",
    help = "Threshold input data based on scalar values",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data',
                                         'unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])
)

triangle_filter = FilterMetadata(
    id            = "TriangleFilterFilter",
    menu_name          = "TriangleFilter",
    class_name = BASE + '.triangle_filter.TriangleFilter',
    tooltip = "Convert input polygons and triangle strips to triangles",
    desc = "Convert input polygons and triangle strips to triangles",
    help = "Convert input polygons and triangle strips to triangles",
    input_info = PipelineInfo(datasets=['poly_data'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

tube_filter = FilterMetadata(
    id            = "TubeFilter",
    menu_name          = "Tu&be",
    class_name = BASE + '.tube.Tube',
    tooltip = "Turns lines into tubes",
    desc = "Turns lines into tubes",
    help = "Turns lines into tubes",
    input_info = PipelineInfo(datasets=['poly_data'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])
)

user_defined_filter = FilterMetadata(
    id            = "UserDefinedFilter",
    menu_name          = "&UserDefined",
    factory = make_user_defined_filter,
    tooltip = "Create a UserDefined filter (will popup a selection dialog)",
    desc = "Create a UserDefined filter (will popup a selection dialog)",
    help = "Create a UserDefined filter (will popup a selection dialog)",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

vorticity_filter = FilterMetadata(
    id            = "VorticityFilter",
    menu_name          = "&Vorticity",
    class_name = BASE + '.vorticity.Vorticity',
    tooltip = "Calculate the vorticity (curl) of input vector field",
    desc = "Calculate the vorticity (curl) of input vector field",
    help = "Calculate the vorticity (curl) of input vector field",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

warp_scalar_filter = FilterMetadata(
    id            = "WarpScalarFilter",
    menu_name          = "Warp S&calar",
    class_name = BASE + '.warp_scalar.WarpScalar',
    tooltip = "Move points of data along normals by the scalar data",
    desc = "Move points of data along normals by the scalar data",
    help = "Move points of data along normals by the scalar data",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['scalars']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

warp_vector_filter = FilterMetadata(
    id            = "WarpVectorFilter",
    menu_name          = "Warp &Vector",
    class_name = BASE + '.warp_vector.WarpVector',
    tooltip = "Move points of data along the vector data at point",
    desc = "Move points of data along the vector data at point",
    help = "Move points of data along the vector data at point",
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors']),
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])
)

# Now collect all the filters for the mayavi registry.
filters = [cell_derivatives_filter,
           cell_to_point_data_filter,
           clip_filter,
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
           image_change_information_filter,
           image_data_probe_filter,
           mask_points_filter,
           point_to_cell_data_filter,
           poly_data_normals_filter,
           quadric_decimation_filter,
           select_output_filter,
           set_active_attribute_filter,
           stripper,
           transform_data_filter,
           threshold_filter,
           triangle_filter,
           tube_filter,
           user_defined_filter,
           vorticity_filter,
           warp_scalar_filter,
           warp_vector_filter,
        ]
