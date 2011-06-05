# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.poly_data_normals import PolyDataNormals
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `WarpVector` class.
######################################################################
class WarpVector(PolyDataNormals):

    """Warps the input data along a the point vector attribute scaled
    as per a scale factor.  Useful for showing flow profiles or
    displacements.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.WarpVector, args=(), allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

