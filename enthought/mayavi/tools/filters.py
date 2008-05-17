"""
Filter factories and their associated functions for mlab.

Module functions meant to be applied to a data source object should take
only one positional argument, the data object, to be easily used in
helper functions. 
"""

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc. 
# License: BSD Style.

from pipe_base import PipeFactory, make_function
import enthought.mayavi.filters.api as filters
from enthought.traits.api import Instance, CFloat, CInt, CArray, Trait, \
            Enum
from enthought.mayavi.filters.filter_base import FilterBase

__all__ = [ 'extractedges', 'extractvectornorm', 'tube', 'warpscalar',
    'delaunay2d', 'selectoutput', 'threshold', 'pointtocelldata', 'elevationfilter',
    'quadricdecimation', 'celltopointdata', 'decimatepro', 'delaunay3d',
    'extractgrid', 'extracttensorcomponents', 'extractvectorcomponents',
    'extractunstructuredgrid', 'gaussiansplatter', 'greedyterraindecimation',
    'maskpoints', 'polydatanormals', 'transformdata', 'trianglefilter',
    'warpvector',
]


##############################################################################
class ExtractEdgesFactory(PipeFactory):
    """Applies the ExtractEdges mayavi filter to the given VTK object."""
    
    _target = Instance(filters.ExtractEdges, ())


extractedges = make_function(ExtractEdgesFactory)


##############################################################################
class ExtractVectorNormFactory(PipeFactory):
    """Applies the ExtractVectorNormaFactory mayavi filter to the given VTK
    object."""
    
    _target = Instance(filters.ExtractVectorNorm, ())


extractvectornorm = make_function(ExtractVectorNormFactory)


##############################################################################
class TubeFactory(PipeFactory):
    """Applies the Tube mayavi filter to the given VTK object."""
    
    _target = Instance(filters.Tube, ())

    tube_sides = CInt(6, adapts='filter.number_of_sides',
                        desc = """number of sides of the tubes used to 
                        represent the lines.""")


    tube_radius = CFloat(0.05, adapts='filter.radius',
                        desc = """radius of the tubes used to represent the
                        lines.""")


tube = make_function(TubeFactory)


##############################################################################
class WarpScalarFactory(PipeFactory):
    """Applies the WarpScalar mayavi filter to the given VTK object."""
    
    _target = Instance(filters.WarpScalar, ())

    warp_scale = CFloat(1.0, adapts="filter.scale_factor",
                            help="scale of the warp scalar")

warpscalar = make_function(WarpScalarFactory)


##############################################################################
class Delaunay2DFactory(PipeFactory):
    """Applies the Delaunay mayavi filter to the given VTK object."""
    
    _target = Instance(filters.Delaunay2D, ())

delaunay2d = make_function(Delaunay2DFactory)


##############################################################################
class ThresholdFactory(PipeFactory):
    """Applies the Threshold mayavi filter to the given VTK object."""
    
    _target = Instance(filters.Threshold, ())

    filter_type = Enum('cells', 'points', adapts='filter_type',
                    help="If thresholding is done on cells or points")

    low  = Trait(None, None, CFloat, help="The lower threshold")

    def _low_changed(self):
        if self.low == None:
            pass
        else:
            self._target.lower_threshold = self.low

    up   = Trait(None, None, CFloat, help="The upper threshold")

    def _up_changed(self):
        if self.up == None:
            pass
        else:
            self._target.upper_threshold = self.up


threshold = make_function(ThresholdFactory)


##############################################################################
class PointToCellDataFactory(PipeFactory):
    """Applies the Point to Cell Data mayavi filter to the given VTK object."""
    
    _target = Instance(filters.PointToCellData, ())

pointtocelldata = make_function(PointToCellDataFactory)


##############################################################################
class ElevationFilterFactory(PipeFactory):
    """Applies the Elevation Filter mayavi filter to the given VTK object."""

    high_point = CArray(default=[0, 0, 1], shape=(3,),
                    adapts="filter.high_point",
                    help="The end point of the projection line")

    low_point = CArray(default=[0, 0, 0], shape=(3,),
                    adapts="filter.low_point",
                    help="The start point of the projection line")

    _target = Instance(filters.ElevationFilter, ())

elevationfilter = make_function(ElevationFilterFactory)


##############################################################################
class QuadricDecimationFactory(PipeFactory):
    """Applies the Quadric Decimation mayavi filter to the given VTK object.

    The input data must be composed of triangles."""
    
    _target = Instance(filters.QuadricDecimation, ())

quadricdecimation = make_function(QuadricDecimationFactory)


##############################################################################
class CellToPointDataFactory(PipeFactory):
    """Applies the CellToPointData mayavi filter to the given VTK object."""
    _target = Instance(filters.CellToPointData, ())

celltopointdata = make_function(CellToPointDataFactory)


##############################################################################
class DecimateProFactory(PipeFactory):
    """Applies the DecimatePro mayavi filter to the given VTK object.

    The input data must be composed of triangles."""
    _target = Instance(filters.DecimatePro, ())

decimatepro = make_function(DecimateProFactory)


##############################################################################
class Delaunay3DFactory(PipeFactory):
    """Applies the Delaunay3D mayavi filter to the given VTK object."""
    _target = Instance(filters.Delaunay3D, ())

delaunay3d = make_function(Delaunay3DFactory)


##############################################################################
class ExtractGridFactory(PipeFactory):
    """Applies the ExtractGrid mayavi filter to the given VTK object."""
    _target = Instance(filters.ExtractGrid, ())

extractgrid = make_function(ExtractGridFactory)


##############################################################################
class ExtractTensorComponentsFactory(PipeFactory):
    """Applies the ExtractTensorComponents mayavi filter to the given VTK object."""
    _target = Instance(filters.ExtractTensorComponents, ())

extracttensorcomponents = make_function(ExtractTensorComponentsFactory)

##############################################################################
class ExtractVectorComponentsFactory(PipeFactory):
    """Applies the ExtractVectorComponents mayavi filter to the given VTK object."""
    _target = Instance(filters.ExtractVectorComponents, ())

extractvectorcomponents = make_function(ExtractVectorComponentsFactory)


##############################################################################
class ExtractUnstructuredGridFactory(PipeFactory):
    """Applies the ExtractUnstructuredGrid mayavi filter to the given VTK object."""
    _target = Instance(filters.ExtractUnstructuredGrid, ())

extractunstructuredgrid = make_function(ExtractUnstructuredGridFactory)


##############################################################################
class GaussianSplatterFactory(PipeFactory):
    """Applies the GaussianSplatter mayavi filter to the given VTK object.

    This filter converts scattered point data into continuous volume data. It is
    essentially equivalent to a 3D Gaussian kernel density estimate."""
    _target = Instance(filters.GaussianSplatter, ())

gaussiansplatter = make_function(GaussianSplatterFactory)


##############################################################################
class GreedyTerrainDecimationFactory(PipeFactory):
    """Applies the GreedyTerrainDecimation mayavi filter to the given VTK object.

    The input must be an ImageData data source."""
    _target = Instance(filters.GreedyTerrainDecimation, ())

greedyterraindecimation = make_function(GreedyTerrainDecimationFactory)


##############################################################################
class MaskPointsFactory(PipeFactory):
    """Applies the MaskPoints mayavi filter to the given VTK object."""
    _target = Instance(filters.MaskPoints, ())

maskpoints = make_function(MaskPointsFactory)


##############################################################################
class PolyDataNormalsFactory(PipeFactory):
    """Applies the PolyDataNormals mayavi filter to the given VTK object."""
    _target = Instance(filters.PolyDataNormals, ())

polydatanormals = make_function(PolyDataNormalsFactory)

##############################################################################
class SelectOutputFactory(PipeFactory):
    """Applies the SelectOutput mayavi filter to the given source."""
    _target = Instance(filters.SelectOutput, ())

selectoutput = make_function(SelectOutputFactory)

##############################################################################
class TransformDataFactory(PipeFactory):
    """Applies the TransformData mayavi filter to the given VTK object."""
    _target = Instance(filters.TransformData, ())

transformdata = make_function(TransformDataFactory)


##############################################################################
class TriangleFilterFactory(PipeFactory):
    """Applies the TriangleFilter mayavi filter to the given VTK object.

    This is useful in between modules which produce non-triangular polygon data
    and filters which need to consume triangular data, notably the decimation
    filters."""
    _target = Instance(filters.TriangleFilter, ())

trianglefilter = make_function(TriangleFilterFactory)


##############################################################################
class WarpVectorFactory(PipeFactory):
    """Applies the WarpVector mayavi filter to the given VTK object."""
    _target = Instance(filters.WarpVector, ())

warpvector = make_function(WarpVectorFactory)


