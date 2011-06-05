# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `GaussianSplatter` class.
######################################################################
class GaussianSplatter(FilterBase):


    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.GaussianSplatter, args=(),
                      allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['image_data'],
                               attribute_types=['any'],
                               attributes=['any'])

