# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `ExtractUnstructuredGrid` class.
######################################################################
class ExtractUnstructuredGrid(FilterBase):
    """Allows a user to select a part of an unstructured grid.
    """
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.ExtractUnstructuredGrid, args=(),
                      allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['unstructured_grid'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['unstructured_grid'],
                               attribute_types=['any'],
                               attributes=['any'])

