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
# `ExtractVectorNorm` class.
######################################################################
class ExtractVectorNorm(FilterBase):
    """Computes the norm (Eucliedean) of the input vector data (with
    optional scaling between [0, 1]).  This is useful when the input
    data has vector input but no scalar data for the magnitude of the
    vectors.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.VectorNorm, args=(), allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    ######################################################################
    # `Filter` interface.
    ######################################################################
    def update_pipeline(self):
        # Do nothing if there is no input.
        inputs = self.inputs
        if len(inputs) == 0 or len(inputs[0].outputs) == 0:
            return

        # By default we set the input to the first output of the first
        # input.
        fil = self.filter
        self.configure_connection(fil, inputs[0])
        fil.update()
        self._set_array_name(fil)
        self._set_outputs([fil])

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Do nothing if there is no input.
        inputs = self.inputs
        if len(inputs) == 0 or len(inputs[0].outputs) == 0:
            return

        self.filter.update()
        self._set_array_name(self.filter)
        # Propagate the data_changed event.
        self.data_changed = True

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _set_array_name(self, filter):
        # Do nothing if there is no input.
        if len(self.inputs) == 0 or len(self.inputs[0].outputs) == 0:
            return

        o = filter.output
        pd = o.point_data
        ps = pd.scalars
        cd = o.cell_data
        cs = cd.scalars
        if (ps is not None) and (not ps.name):
            ps.name = pd.vectors.name + ' magnitude'
        elif (cs is not None) and (not cs.name):
            cs.name = cd.vectors.name + ' magnitude'
