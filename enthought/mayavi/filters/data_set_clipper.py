"""This filter enables one to clip a selection from an input dataset
using various Implicit Widgets.
"""
# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu at aero.iitb.ac.in>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance, Button, Delegate
from enthought.traits.ui.api import View, Group, Item

from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.core.filter import Filter
from enthought.mayavi.core.pipeline_info import PipelineInfo
from enthought.mayavi.components.implicit_widgets import ImplicitWidgets


######################################################################
# `DataSetClipper` class.
######################################################################
class DataSetClipper(Filter):

    # The version of this class.  Used for persistence.
    __version__ = 0
    
    # The widgets to be used for the Clipping Filter.
    widget = Instance(ImplicitWidgets, allow_none=False)

    # The clipping filter.
    filter = Instance(tvtk.Object, allow_none=False)

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

       
    ######################################################################
    # `Filter` interface
    ######################################################################
    def setup_pipeline(self):
        self.widget = ImplicitWidgets()
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
        filter.input = inputs[0].outputs[0]
        widget.update_implicit_function()
        filter.clip_function = widget.implicit_function
        filter.update()
        self._set_outputs([filter.output])
        
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
    def _widget_changed(self, old, new):
        self.widgets = self.widget.widgets

        if len(self.inputs) > 0:
            new.inputs = self.inputs
            new.update_pipeline()      

    def _filter_changed(self, old, new):
        if old is not None:
                old.on_trait_change(self.render, remove=True)
        new.on_trait_change(self.render)
        if len(self.inputs) > 0:
            inp = self.inputs[0].outputs[0]
            new.input = inp
            self.outputs = [new.output]
    
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
    
