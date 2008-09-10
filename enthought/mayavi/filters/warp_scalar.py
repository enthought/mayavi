# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.filters.poly_data_normals import PolyDataNormals
from enthought.mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `WarpScalar` class.
######################################################################
class WarpScalar(PolyDataNormals):

    """Warps the input data along a particular direction (either the
    normals or a specified direction) with a scale specified by the
    local scalar value.  Useful for making carpet plots.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.WarpScalar, args=(), allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['scalars'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

