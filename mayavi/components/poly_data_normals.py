"""This component computes normals for input poly data.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk

# Local imports.
from mayavi.core.component import Component
from mayavi.components.common import convert_to_poly_data


######################################################################
# `PolyDataNormals` class.
######################################################################
class PolyDataNormals(Component):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The filter that generates the normals.
    filter = Instance(tvtk.PolyDataNormals, args=(),
                      kw={'feature_angle': 45.0}, record=True)

    ########################################
    # The component's view

    _filter_group = Group(Item(name='feature_angle'))

    view = View(Group(Item(name='filter', style='custom',
                           editor=InstanceEditor(view=View(_filter_group))),
                      show_labels=False
                      )
                )

    ######################################################################
    # `Component` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* its tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.
        """
        self.filter.on_trait_change(self.update_data)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        if (len(self.inputs) == 0) or \
           (len(self.inputs[0].outputs) == 0):
            return
        f = self.filter
        input = self.inputs[0].outputs[0]
        self.configure_input(f, convert_to_poly_data(input))
        f.update()
        self.outputs = [f]

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        self.data_changed = True

    def has_output_port(self):
        """ The filter has an output port."""
        return True

    def get_output_object(self):
        """ Returns the output port."""
        return self.filter.output_port
