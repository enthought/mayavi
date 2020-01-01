"""This filter enables one to clip a selection from an input dataset
using various Implicit Widgets.
"""
# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu at aero.iitb.ac.in>
# Copyright (c) 2009-2020, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
try:
    import cPickle
except ImportError:
    import pickle as cPickle

# Enthought library imports.
from traits.api import Instance, Button, Delegate
from traitsui.api import View, Group, Item
from apptools.persistence import state_pickler

from tvtk.api import tvtk

# Local imports
from mayavi.core.filter import Filter
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.components.implicit_widgets import ImplicitWidgets


######################################################################
# `DataSetClipper` class.
######################################################################
class DataSetClipper(Filter):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The widgets to be used for the Clipping Filter.
    widget = Instance(ImplicitWidgets, allow_none=False, record=True)

    # The clipping filter.
    filter = Instance(tvtk.Object, allow_none=False, record=True)

    # The update mode of the widget-- this is delegated to the
    # ImplicitWidgets.
    update_mode = Delegate('widget', modify=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    output_info = PipelineInfo(datasets=['any'],
                               attributes=['any'])

    ########################################
    # View related traits.

    # Button to reset the boundaries of the implicit_widget.
    reset_button = Button('Reset Boundaries')

    view = View(Group(Group(Item('update_mode'),
                            ),
                      Group(Item('reset_button'),
                            Item(name='widget', style='custom', resizable=True),
                            show_labels=False
                            ),
                      label='ImplicitWidget'
                      ),
                Group(Group(Item('filter', style='custom'),
                            show_labels=False),
                      label='Clipper'
                     ),
                resizable=True
                )

    ########################################
    # Private traits.
    _transform = Instance(tvtk.Transform, allow_none=False)


    ######################################################################
    # `object` interface.
    ######################################################################
    def __get_pure_state__(self):
        d = super(DataSetClipper, self).__get_pure_state__()
        for name in ('_first', '_observer_id'):
            d.pop(name, None)
        d['matrix'] = cPickle.dumps(self._transform.matrix)
        return d

    def __set_pure_state__(self, state):
        mat = state.pop('matrix')
        super(DataSetClipper, self).__set_pure_state__(state)
        state_pickler.set_state(self, state)
        self._transform.set_matrix(cPickle.loads(mat))
        self.widget.set_transform(self._transform)


    ######################################################################
    # `Filter` interface
    ######################################################################
    def setup_pipeline(self):
        self.widget = ImplicitWidgets()
        self._transform = tvtk.Transform()
        self.filter = tvtk.ClipDataSet()
        self.widget.on_trait_change(self._handle_widget, 'widget')
        super(DataSetClipper, self).setup_pipeline()

    def update_pipeline(self):
        inputs = self.inputs
        if len(inputs) == 0:
            return

        widget = self.widget
        widget.inputs = inputs
        widget.update_pipeline()

        filter = self.filter
        self.configure_connection(filter, inputs[0])
        widget.update_implicit_function()
        filter.clip_function = widget.implicit_function
        filter.update()
        self._set_outputs([filter])

        self.pipeline_changed = True

    def update_data(self):
        # Do nothing if there is no input.
        if len(self.inputs) == 0:
            return

        self.filter.update()
        # Propagate the data_changed event.
        self.data_changed = True

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _on_interaction_event(self, obj, event):
        tfm = self._transform
        self.widget.widget.get_transform(tfm)
        recorder = self.recorder
        if recorder is not None:
            state = {}
            state['elements'] = tfm.matrix.__getstate__()['elements']
            name = recorder.get_script_id(self)
            recorder.record('%s._transform.matrix.__setstate__(%s)'\
                            %(name, state))
            recorder.record('%s.widget.widget.set_transform(%s._transform)'\
                            %(name, name))
            recorder.record('%s.widget.update_implicit_function()' % name)
            recorder.record('%s.render()' % name)

    def _widget_changed(self, old, new):
        self.widgets = self.widget.widgets

        if len(self.inputs) > 0:
            new.inputs = self.inputs
            new.update_pipeline()
        self._observer_id = new.widget.add_observer(self.update_mode_,
                                             self._on_interaction_event)


    def _filter_changed(self, old, new):
        if old is not None:
                old.on_trait_change(self.render, remove=True)
        new.on_trait_change(self.render)
        if len(self.inputs) > 0:
            self.configure_connection(new, self.inputs[0])
            self.outputs = [new]

    def _reset_button_fired(self):
        self.widget.widget.place_widget()
        self.widget.update_implicit_function()
        self.filter.update()
        self.render()

    def _handle_widget(self, value):
        self.widgets = self.widget.widgets
        f = self.filter
        f.clip_function = self.widget.implicit_function
        f.update()
        self.update_pipeline()
