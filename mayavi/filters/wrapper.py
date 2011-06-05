"""The `Wrapper` filter is one which wraps around any mayavi filter or
component.  By default it does not allow the user to set it on and off
from the UI, for that see the `Optional` filter.
"""

# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Bool, Str
from traitsui.api import Item, Group, View
from apptools.persistence import state_pickler

# Local imports.
from mayavi.core.pipeline_base import PipelineBase
from mayavi.core.filter import Filter
from mayavi.core.common import handle_children_state

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
    filter = Instance(PipelineBase, allow_none=False, record=True)

    # The text to show in the UI of form "Enable SomeFilter"
    label_text = Str('Enable Filter')

    # Are we enabled or not.
    enabled = Bool(True, desc='if the filter is enabled or not')

    ########################################
    # Private traits.

    # Should we show enabled in the UI or not.  This defaults to False,
    # the `Optional` filter merely changes this to True.  This trait is
    # not meant for interactive changing.
    _show_enabled = Bool(False)

    ######################################################################
    # `object` interface.
    ######################################################################
    def __set_pure_state__(self, state):
        # Create and set the filter.
        children = [f for f in [self.filter] if f is not None]
        handle_children_state(children, [state.filter])
        self.filter = children[0]
        # Restore our state.
        super(Wrapper, self).__set_pure_state__(state)

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
    def setup_pipeline(self):
        """Setup the pipeline."""
        # Needed because a user may have defined a filter by setting the
        # default value of the trait in the subclass in which case the
        # filter changed handler will never be called leading to
        # problems.
        if self.filter is not None:
            self._setup_events(self.filter)

    def stop(self):
        # There is no need to override start since the wrapped filter is
        # always started automatically in the _enabled_changed handler.
        super(Wrapper, self).stop()
        if self.filter is not None:
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
        if len(self.inputs) == 0 or self.filter is None:
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
        self.render()

    def _filter_changed(self, old, new):
        """Static traits handler."""
        if old is not None:
            self._setup_events(old, remove=True)
            old.stop()
        if self.scene is not None:
            new.scene = self.scene
        self._setup_events(new, remove=False)
        self._enabled_changed(self.enabled)

    def _scene_changed(self, old, new):
        """Static traits handler."""
        if self.filter is not None:
            self.filter.scene = new
        super(Wrapper, self)._scene_changed(old, new)

    def _filter_pipeline_changed(self):
        if self.enabled:
            self._set_outputs(self.filter.outputs)

    def _setup_events(self, obj, remove=False):
        obj.on_trait_change(self._filter_pipeline_changed,
                            'pipeline_changed',
                            remove=remove)
        obj.on_trait_change(self.update_data,
                            'data_changed',
                            remove=remove)

    def _visible_changed(self, value):
        self.filter.visible = value
        super(Wrapper, self)._visible_changed(value)

