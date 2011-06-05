"""
A filter that lets you change the spacing and origin of an input
ImageData dataset.
"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `ImageChangeInformation` class.
######################################################################
class ImageChangeInformation(FilterBase):

    """
    A filter that lets you change the spacing and origin of an input
    ImageData dataset.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.ImageChangeInformation, args=(),
                      allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['image_data'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['image_data'],
                               attribute_types=['any'],
                               attributes=['any'])

