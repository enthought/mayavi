# Author: Gael Varoquaux <gael _dot_ varoquaux _at_ normalesup _dot_ org> 
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.filters.poly_data_filter_base import \
        PolyDataFilterBase
from enthought.mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `QuadricDecimation` class.
######################################################################
class QuadricDecimation(PolyDataFilterBase):

    """ Simplifies triangles of a mesh """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.QuadricDecimation, args=(), allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['poly_data'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])

