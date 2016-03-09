# Author: Gael Varoquaux <gael _dot_ varoquaux _at_ normalesup _dot_ org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.components.common import convert_to_poly_data


######################################################################
# `PolyDataFilterBase` class.
######################################################################
class PolyDataFilterBase(FilterBase):

    """ Base class for a filter requiring polydata input. Converts the
        source to polydata.
    """

    ######################################################################
    # `Filter` interface.
    ######################################################################
    def update_pipeline(self):
        # Do nothing if there is no input.
        inputs = self.inputs
        if len(inputs) == 0:
            return

        # By default we set the input to the first output of the first
        # input.
        fil = self.filter
        self.configure_input(fil, convert_to_poly_data(inputs[0].outputs[0]))
        fil.update()
        self._set_outputs([fil])
