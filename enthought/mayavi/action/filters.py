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
# `CellToPointDataFilter` class.
######################################################################
class CellToPointDataFilter(Action):
    """ An action that starts a delaunay 2d filter. """

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
# `DecimateProFilter` class.
######################################################################
class DecimateProFilter(Action):
    """ An action that starts a DecimatePro  filter. """

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
    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.greedy_terrain_decimation import \
                GreedyTerrainDecimation
        f = GreedyTerrainDecimation()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `MaskPointsFilter` class.
######################################################################
class MaskPointsFilter(Action):
    """ An action that starts a mask points filter. """
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
    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.select_output import SelectOutput
        f = SelectOutput()
        mv = get_imayavi(self.window)
        mv.add_filter(f)


######################################################################
# `TransformData` class.
######################################################################
class TransformDataFilter(Action):
    """ An action that starts a TransformData filter. """
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
    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.tube import Tube
        t = Tube()
        mv = get_imayavi(self.window)
        mv.add_filter(t)



######################################################################
# `WarpScalarFilter` class.
######################################################################
class WarpScalarFilter(Action):
    """ An action that starts a mask points filter. """
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
    def perform(self, event):
        """ Performs the action. """
        from enthought.mayavi.filters.warp_vector import WarpVector
        f = WarpVector()
        mv = get_imayavi(self.window)
        mv.add_filter(f)
