# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `Stripper` class.
######################################################################
class Stripper(FilterBase):

    """ Create triangle strips and/or poly-lines. Useful for regularizing
        broken up surfaces, such as those created by the Tube
        filter.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.Stripper, args=(), allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['poly_data'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['poly_data'],
                               attribute_types=['any'],
                               attributes=['any'])

