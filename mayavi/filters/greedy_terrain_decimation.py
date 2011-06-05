# Author: Gael Varoquaux <gael _dot_ varoquaux _at_ normalesup _dot_ org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `GreedyTerrainDecimation` class.
######################################################################
class GreedyTerrainDecimation(FilterBase):

    """ Performs a triangulation of image data after simplifying it. """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.GreedyTerrainDecimation, args=(),
                      allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])

