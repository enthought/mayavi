# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from tvtk.api import tvtk

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `CellDerivatives` class.
######################################################################
class CellDerivatives(FilterBase):

    """Computes derivatives from input point scalar and vector data and
    produces cell data on the gradients.  Can be used to approximately
    calcuate the vorticity for example.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.CellDerivatives, args=(),
                      allow_none=False, record=True)

    # Information about what this object can consume.
    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    # Information about what this object can produce.
    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    def has_output_port(self):
        """ The filter has an output port."""
        return True

    def get_output_object(self):
        """ Return the output port."""
        return self.filter.output_port
