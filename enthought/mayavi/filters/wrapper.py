"""The `Wrapper` filter is one which wraps around any mayavi filter or
component.  By default it does not allow the user to set it on and off
from the UI, for that see the `Optional` filter.  
"""

# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance, Bool, Str
from enthought.traits.ui.api import Item, Group, View

# Local imports.
from enthought.mayavi.core.pipeline_base import PipelineBase
from enthought.mayavi.core.filter import Filter

# FIXME:  This filter cannot be persisted due to the broken nature of
# our persistence framework.  This should work when we use the new
# pickle approach.

################################################################################
# `Wrapper` class.
################################################################################
class Wrapper(Filter):
    """
    The `Wrapper` filter is one which wraps around any mayavi filter or
    component.  By default it does not allow the user to set it on and
    off from the UI, for that see the `Optional` filter.  
    """

    # The filter we wrap.
    filter = Instance(PipelineBase, allow_none=False)

    # The text to show in the UI of form "Enable SomeFilter"
    label_text = Str('Enable Filter')

    # Are we enabled or not.
    enabled = Bool(True, desc='if the wrapped filter is enabled or not')

    ########################################
    # Private traits.

    # Should we show enabled in the UI or not.  This defaults to False,
    # the `Optional` filter merely changes this to True.  This trait is
    # not meant for interactive changing.
    _show_enabled = Bool(False)

    ######################################################################
    # HasTraits interface.
    ###################################################################### 
    def default_traits_view(self):
        """Returns the default traits view for this object."""
        if self._show_enabled:
            view = View(Group(Group(Item(name='enabled',
                                         label=self.label_text)),
                            Group(Item(name='filter', 
                                       style='custom',
                                       enabled_when='enabled',
                                       resizable=True),
                                  show_labels=False)),
                        resizable=True)
        else:
            view = View(Group(Item(name='filter', 
                                   style='custom',
                                   enabled_when='enabled',
                                   resizable=True),
                              show_labels=False),
                        resizable=True)

        return view

    ######################################################################
    # `Filter` interface.
    ###################################################################### 
    def stop(self):
        # There is no need to override start since the wrapped filter is
        # always started automatically in the _enabled_changed handler.
        super(Wrapper, self).stop()
        self.filter.stop()

    def update_pipeline(self):
        """This method *updates* the tvtk pipeline when data upstream is
        known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        self._enabled_changed(self.enabled)
        self.pipeline_changed = True

    def update_data(self):
        """This method does what is necessary when upstream data
        changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Propagate the data_changed event.
        self.data_changed = True

    ######################################################################
    # Private interface.
    ###################################################################### 
    def _enabled_changed(self, value):
        """Static traits handler."""
        if len(self.inputs) == 0:
            return
        my_input = self.inputs[0]
        filter = self.filter
        if len(filter.name) == 0:
            name = filter.__class__.__name__
        else:
            name = filter.name
        if value and filter is not None:
            filter.inputs = [my_input]
            if not filter.running:
                filter.start()
            self._set_outputs(self.filter.outputs)
        else:
            self._set_outputs(my_input.outputs)
            name += ' (disabled)'
        self.name = name

    def _filter_changed(self, old, new):
        """Static traits handler."""
        if old is not None:
            old.stop()
        if self.scene is not None:
            new.scene = self.scene
        self._enabled_changed(self.enabled)

    def _scene_changed(self, old, new):
        """Static traits handler."""
        self.filter.scene = new
        super(Wrapper, self)._scene_changed(old, new)

    def _data_changed_for_filter(self):
         self.data_changed = True

    def _pipeline_changed_for_filter(self):
        self.pipeline_changed = True

