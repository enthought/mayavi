# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.poly_data_filter_base import \
        PolyDataFilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `PolyDataNormals` class.
######################################################################
class PolyDataNormals(PolyDataFilterBase):

    """Computes normals from input data.  This gives meshes a smoother
    appearance.  This should work for any input dataset.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.PolyDataNormals, args=(), allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['poly_data'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])

