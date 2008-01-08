# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.filters.filter_base import FilterBase
from enthought.mayavi.components.common import convert_to_poly_data


######################################################################
# `PolyDataNormals` class.
######################################################################
class PolyDataNormals(FilterBase):

    """Computes normals from input data.  This gives meshes a smoother
    appearance.  This should work for any input dataset.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.PolyDataNormals, args=(), allow_none=False)

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
        fil.input = convert_to_poly_data(inputs[0].outputs[0])
        fil.update()
        self._set_outputs([fil.output])
