# Author: Varun Hiremath <varun@debian.org>

# Enthought library imports.
from traits.api import Instance, Enum
from traitsui.api import View, Group, Item
from tvtk.api import tvtk

# Local imports
from mayavi.filters.filter_base import FilterBase
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `ExtractVectorComponents` class.
######################################################################
class ExtractVectorComponents(FilterBase):
    """ This wraps the TVTK ExtractVectorComponents filter and allows
    one to select any of the three components of an input vector data
    attribute."""

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.ExtractVectorComponents, args=(), allow_none=False)

    # The Vector Component to be extracted
    component = Enum('x-component', 'y-component', 'z-component',
                     desc='component of the vector to be extracted')

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])

    output_info = PipelineInfo(datasets=['any'],
                               attribute_types=['any'],
                               attributes=['any'])

    view = View(Group(Item(name='component')),
                resizable=True
                )

    ######################################################################
    # `Filter` interface.
    ######################################################################
    def update_pipeline(self):
        # Do nothing if there is no input.
        inputs = self.inputs
        if len(inputs) == 0 or len(inputs[0].outputs) == 0:
            return

        fil = self.filter
        self.configure_connection(fil, inputs[0])
        fil.update()
        self._component_changed(self.component)

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _component_changed(self, value):
        # Obtain output from the TVTK ExtractVectorComponents filter
        # corresponding to the selected vector component

        if len(self.inputs) == 0 or len(self.inputs[0].outputs) == 0:
            return

        if value == 'x-component':
            self._set_outputs([self.filter.vx_component])
        elif value == 'y-component':
            self._set_outputs([self.filter.vy_component])
        elif value == 'z-component':
            self._set_outputs([self.filter.vz_component])
        self.render()
