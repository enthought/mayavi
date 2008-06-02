"""Actions to start various filters.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.pyface.action.api import Action

# Local imports.
from enthought.mayavi.plugins.script import  get_imayavi

######################################################################
# `CellDerivativesFilter` class.
######################################################################
class CellDerivativesFilter(Action):

    tooltip       = "Calculate derivatives of input point/vector data "\
                    "and output these as cell data"

    description   = "Calculate derivatives of input point/vector data "\
                    "and output these as cell data"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.cell_derivatives import CellDerivatives
        f = CellDerivatives()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `CellToPointDataFilter` class.
######################################################################
class CellToPointDataFilter(Action):

    tooltip       = "Convert cell data to point data for the active data"

    description   = "Convert cell data to point data for the active data"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.cell_to_point_data import CellToPointData
        f = CellToPointData()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `ContourFilter` class.
######################################################################
class ContourFilter(Action):

    tooltip       = "Compute contours of the input dataset"

    description   = "Compute contours of the input dataset"
    
    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.contour import Contour
        f = Contour()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

######################################################################
# `CutPlaneFilter` class.
######################################################################
class CutPlaneFilter(Action):

    tooltip       = "Slice the input dataset with a cut plane"

    description   = "Slice the input dataset with a cut plane"
    
    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.cut_plane import CutPlane
        f = CutPlane()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `DecimateProFilter` class.
######################################################################
class DecimateProFilter(Action):
    """ An action that starts a DecimatePro  filter. """

    tooltip       = "Simpilies a mesh using the DecimatePro filter"

    description   = "Simpilies a mesh using the DecimatePro filter"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.decimatepro import DecimatePro
        f = DecimatePro()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `Delaunay2DFilter` class.
######################################################################
class Delaunay2DFilter(Action):
    """ An action that starts a delaunay 2d filter. """

    tooltip       = "Perform a 2D Delaunay triangulation for the given data"

    description   = "Perform a 2D Delaunay triangulation for the given data"

    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.delaunay2d import Delaunay2D
        f = Delaunay2D()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `Delaunay3DFilter` class.
######################################################################
class Delaunay3DFilter(Action):
    """ An action that starts a delaunay 3d filter. """

    tooltip       = "Perform a 3D Delaunay triangulation for the given data"

    description   = "Perform a 3D Delaunay triangulation for the given data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.delaunay3d import Delaunay3D
        f = Delaunay3D()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `ElevationFilter` class.
######################################################################
class ElevationFilter(Action):
    """ An action that starts an Elevation filter. """

    tooltip       = "Creates scalar data from the elevation along a" \
                        "direction"

    description   = "Creates scalar data from the elevation along a" \
                        "direction"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.elevation_filter import \
                ElevationFilter
        t = ElevationFilter()
        mv = get_imayavi(self.window)
        mv.add_filter(t)


######################################################################
# `ExtractGridFilter` class.
######################################################################
class ExtractEdgesFilter(Action):

    tooltip       = "Turns edges into lines."
    description   = "Turns edges into lines."

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.extract_edges import ExtractEdges
        f = ExtractEdges()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `ExtractGridFilter` class.
######################################################################
class ExtractGridFilter(Action):

    tooltip       = "Extract/subsample part of any structured grid"
    description   = "Extract/subsample part of any structured grid"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.extract_grid import ExtractGrid
        f = ExtractGrid()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

######################################################################
# `ExtractTensorComponentsFilter` class.
######################################################################
class ExtractTensorComponentsFilter(Action):

    tooltip       = "Extract tensor components from tensor data"
    description   = "Extract tensor components from tensor data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.extract_tensor_components import ExtractTensorComponents
        f = ExtractTensorComponents()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `ExtractUnstructuredGridFilter` class.
######################################################################
class ExtractUnstructuredGridFilter(Action):

    tooltip       = "Extract part of an unstructured grid"
    description   = "Extract part of an unstructured grid"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.extract_unstructured_grid import ExtractUnstructuredGrid
        f = ExtractUnstructuredGrid()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `ExtractVectorNormFilter` class.
######################################################################
class ExtractVectorNormFilter(Action):

    tooltip       = "Compute the vector norm for the current vector data"
    description   = "Compute the vector norm for the current vector data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.extract_vector_norm import ExtractVectorNorm
        f = ExtractVectorNorm()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

######################################################################
# `ExtractVectorComponentsFilter` class.
######################################################################
class ExtractVectorComponentsFilter(Action):

    tooltip       = "Extract vector components from vector data"
    description   = "Extract vector components from vector data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.extract_vector_components import ExtractVectorComponents
        f = ExtractVectorComponents()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

######################################################################
# `GaussianSplatter` class.
######################################################################
class GaussianSplatterFilter(Action):

    tooltip       = "Builds a structured set of points from a cloud of "\
                        "points, the local density defining the scalar"
    description   = "Builds a structured set of points from a cloud of "\
                        "points, the local density defining the scalar"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.gaussian_splatter import \
                GaussianSplatter
        f = GaussianSplatter()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `GreddyTerrainDecimation` class.
######################################################################
class GreedyTerrainDecimationFilter(Action):

    tooltip       = "Simplifies image data and performs a triangulation"
    description   = "Simplifies image data and performs a triangulation"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.greedy_terrain_decimation import \
                GreedyTerrainDecimation
        f = GreedyTerrainDecimation()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `ImageDataProbeFilter` class.
######################################################################
class ImageDataProbeFilter(Action):

    tooltip     = "Samples arbitrary datasets onto an image dataset (cube of data)"
    description = "Samples arbitrary datasets onto an image dataset (cube of data)"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.image_data_probe import ImageDataProbe
        f = ImageDataProbe()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `MaskPointsFilter` class.
######################################################################
class MaskPointsFilter(Action):
    """ An action that starts a mask points filter. """

    tooltip       = "Mask the input points in the data"
    description   = "Mask the input points in the data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.mask_points import MaskPoints
        f = MaskPoints()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `PointToCellDataFilter` class.
######################################################################
class PointToCellDataFilter(Action):
    """ An action that starts a mask points filter. """

    tooltip       = "Convert point data to cell data for the active data"

    description   = "Convert point data to cell data for the active data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.point_to_cell_data import PointToCellData
        f = PointToCellData()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

######################################################################
# `PolyDataNormalsFilter` class.
######################################################################
class PolyDataNormalsFilter(Action):
    """ An action that starts a mask points filter. """

    tooltip       = "Compute normals and smooth the appearance"

    description   = "Compute normals and smooth the appearance"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.poly_data_normals import PolyDataNormals
        f = PolyDataNormals()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `QuadricDecimation` class.
######################################################################
class QuadricDecimationFilter(Action):

    tooltip       = "Simplifies a triangular mesh"

    description   = "Simplifies a triangular mesh"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.quadric_decimation import \
                QuadricDecimation
        f = QuadricDecimation()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

######################################################################
# `SelectOutput` class.
######################################################################
class SelectOutputFilter(Action):
    """ An action that creates a SelectOutput filter. """

    tooltip       = "Choose the output of the source that should be used"

    description   = "Choose the output of the source that should be used"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.select_output import SelectOutput
        f = SelectOutput()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

######################################################################
# `SetActiveAttributeFilter` class.
######################################################################
class SetActiveAttributeFilter(Action):

    tooltip       = "Set the active attribute (scalar/vector/tensor) to use"

    description   = "Set the active attribute (scalar/vector/tensor) to use"
    
    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.set_active_attribute import SetActiveAttribute
        f = SetActiveAttribute()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `TransformData` class.
######################################################################
class TransformDataFilter(Action):
    """ An action that starts a TransformData filter. """

    tooltip       = "Transform (rotate/translate/scale) non ImageData datasets"

    description   = "Transform (rotate/translate/scale) non ImageData datasets"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.transform_data import TransformData
        t = TransformData()
        mv = get_imayavi(self.window)
        mv.add_filter(t)


######################################################################
# `ThresholdFilter` class.
######################################################################
class ThresholdFilter(Action):
    """ An action that starts a threshold filter. """

    tooltip       = "Threshold input data based on scalar values"

    description   = "Threshold input data based on scalar values"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.threshold import Threshold
        t = Threshold()
        mv = get_imayavi(self.window)
        mv.add_filter(t)


######################################################################
# `TriangleFilter` class.
######################################################################
class TriangleFilter(Action):
    """ An action that starts a triangle filter. """

    tooltip       = "Convert input polygons and triangle strips to triangles"

    description   = "Convert input polygons and triangle strips to triangles"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.triangle_filter import TriangleFilter
        t = TriangleFilter()
        mv = get_imayavi(self.window)
        mv.add_filter(t)

######################################################################
# `TubeFilter` class.
######################################################################
class TubeFilter(Action):
    """ An action that starts a tube filter. """

    tooltip       = "Turns lines into tubes"

    description   = "Turns lines into tubes"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.tube import Tube
        t = Tube()
        mv = get_imayavi(self.window)
        mv.add_filter(t)

######################################################################
# `UserDefinedFilter` class.
######################################################################
class UserDefinedFilter(Action):

    tooltip       = "Create a UserDefined filter (will popup a selection dialog)"

    description   = "Create a UserDefined filter (will popup a selection dialog)"
    
    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.user_defined import UserDefined
        f = UserDefined()
        f.setup_filter()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

######################################################################
# `VorticityFilter` class.
######################################################################
class VorticityFilter(Action):

    tooltip       = "Calculate the vorticity (curl) of input vector field"

    description   = "Calculate the vorticity (curl) of input vector field"
    
    ###########################################################################
    # 'Action' interface.
    ###########################################################################

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.vorticity import Vorticity
        f = Vorticity()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

######################################################################
# `WarpScalarFilter` class.
######################################################################
class WarpScalarFilter(Action):
    """ An action that starts a mask points filter. """

    tooltip       = "Move points of data along normals by the scalar data"

    description   = "Move points of data along normals by the scalar data"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.warp_scalar import WarpScalar
        f = WarpScalar()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `WarpVectorFilter` class.
######################################################################
class WarpVectorFilter(Action):
    """ An action that starts a mask points filter. """

    tooltip       = "Move points of data along the vector data at point"

    description   = "Move points of data along the vector data at point"

    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.warp_vector import WarpVector
        f = WarpVector()
        mv = get_imayavi(self.window)
        mv.add_filter(f)

