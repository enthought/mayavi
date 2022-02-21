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
# `CellToPointData` class.
######################################################################
class CellToPointData(FilterBase):

    """Transforms cell attribute data to point data by averaging the
    cell data from the cells at the point.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.CellDataToPointData,
                      args=(), kw={'pass_cell_data':1},
                      allow_none=False, record=True)

    # Information about what this object can consume/produce.
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['cell'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    def has_output_port(self):
        """ The filter has an output port."""
        return True

    def get_output_object(self):
        """ Return the output port."""
        return self.filter.output_port
