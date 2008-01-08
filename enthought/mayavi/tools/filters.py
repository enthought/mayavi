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
from enthought.traits.api import Instance, CFloat, CInt
from enthought.mayavi.filters.filter_base import FilterBase

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




