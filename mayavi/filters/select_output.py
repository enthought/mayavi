"""Filter that allows a user to select one among several of the outputs
of a given input.  This is typically very useful for a multi-block data
source.  """

# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Prabhu Ramachandran
# License: BSD Style.

# Enthought library imports.
from traits.api import Any, Int, Range
from traitsui.api import View, Group, Item

from tvtk.api import tvtk
from mayavi.core.filter import Filter
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.utils import get_new_output


###############################################################################
# `SelectOutput` class.
###############################################################################
class SelectOutput(Filter):

    """This filter lets a user select one among several of the output blocks of
    a given input. This is very useful for a multi-block data source.
    """

    # The output index in the input to choose from.
    output_index = Range(value=0,
                         enter_set=True,
                         auto_set=False,
                         low='_min_index',
                         high='_max_index')

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    # The minimum output index of our input.
    _min_index = Int(0, desc='the minimum output index')
    # The maximum output index of our input.
    _max_index = Int(0, desc='the maximum output index')

    _my_input = Any(transient=True)

    ########################################
    # Traits View.

    view = View(Group(Item('output_index',
                           enabled_when='_max_index > 0')),
                resizable=True)

    ######################################################################
    # `object` interface.
    def __get_pure_state__(self):
        d = super(SelectOutput, self).__get_pure_state__()
        d['output_index'] = self.output_index
        return d

    def __set_pure_state__(self, state):
        super(SelectOutput, self).__set_pure_state__(state)
        # Force an update of the output index -- if not this doesn't
        # change.
        self._output_index_changed(state.output_index)

    ######################################################################
    # `Filter` interface.
    def update_pipeline(self):
        # Do nothing if there is no input.
        inputs = self.inputs
        if len(inputs) == 0:
            return

        # Set the maximum index.
        obj = get_new_output(inputs[0].outputs[0])
        self._my_input = obj
        if hasattr(obj, 'number_of_blocks'):
            self._max_index = obj.number_of_blocks - 1
        else:
            self._max_index = len(inputs[0].outputs) - 1
        self._output_index_changed(self.output_index)

    def update_data(self):
        # Propagate the event.
        self.data_changed = True

    ######################################################################
    # Trait handlers.
    def _setup_output(self, value):
        obj = self._my_input
        tp = tvtk.TrivialProducer()
        if hasattr(obj, 'number_of_blocks'):
            tp.set_output(obj.get_block(value))
        else:
            tp.set_output(self.inputs[0].outputs[value])
        self._set_outputs([tp])

    def _output_index_changed(self, value):
        """Static trait handler."""
        if value > self._max_index:
            self.output_index = self._max_index
        elif value < self._min_index:
            self.output_index = self._min_index
        else:
            self._setup_output(value)
            s = self.scene
            if s is not None:
                s.renderer.reset_camera_clipping_range()
                s.render()
