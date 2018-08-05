"""A meta-component that allows a component to be optionally enabled
or disabled.  This component is mostly for illustration and is not
used anywhere.  This is because it is usually much easier to simply
add a trait in the module to enable/disable a particular component.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2005-2018, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Bool, Str, Property
from traitsui.api import View, Group, Item

# Local imports.
from mayavi.core.component import Component


######################################################################
# `Optional` class.
######################################################################
class Optional(Component):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The outputs of this component is a property and not a list.
    outputs = Property

    # The component that is enabled or disabled.
    component = Instance(Component)

    # Is the component enabled or not.
    enabled = Bool(True, desc='if the component is enabled')

    # The label of the checkbox to use in the view.
    label = Str

    ########################################
    # The component's view

    # This is defined outside the view so that the label may be easily
    # changed.
    enabled_item = Item(name='enabled')
    view = View(Group(Group(enabled_item),
                      Group(Item(name='component', style='custom',
                                 visible_when='object.enabled'),
                            show_labels=False)
                      )
                )

    ######################################################################
    # `Component` interface
    ######################################################################
    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        comp = self.component
        if self.inputs != comp.inputs:
            comp.inputs = self.inputs
        self.pipeline_changed = True

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        self.data_changed = True

    ######################################################################
    # `Base` interface
    ######################################################################
    def start(self):
        """This is invoked when this object is added to the mayavi
        pipeline.  Note that when start is invoked, all the other
        information for the pipeline should be already set.
        """
        # Do nothing if we are already running.
        if self.running:
            return

        super(Optional, self).start()
        self.component.start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        if not self.running:
            return

        self.component.stop()
        super(Optional, self).stop()

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _get_outputs(self):
        if self.enabled:
            return self.component.outputs
        else:
            return self.inputs[0].outputs

    def _enabled_changed(self, value):
        # Force downstream modules to update.
        self.pipeline_changed = True

    def _label_changed(self, value):
        # Change the displayed label for the enable trait in the view.
        item = self.trait_view_elements().content['enabled_item']
        item.label = value

    def _component_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self._fire_pipeline_changed,
                                'pipeline_changed', remove=True)
            old.on_trait_change(self._fire_data_changed,
                                'data_changed', remove=True)

        new.on_trait_change(self._fire_pipeline_changed, 'pipeline_changed')
        new.on_trait_change(self._fire_data_changed, 'data_changed')

    def _fire_pipeline_changed(self):
        self.pipeline_changed = True

    def _fire_data_changed(self):
        self.data_changed = True
