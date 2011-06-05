"""Defines a Collection filter which is a collection of mayavi
filters/components bundled into one.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Bool, List
from traitsui.api import Item, Group, View, ListEditor

# Local imports.
from mayavi.core.pipeline_base import PipelineBase
from mayavi.core.filter import Filter
from mayavi.core.common import handle_children_state


################################################################################
# `Collection` class.
################################################################################
class Collection(Filter):
    """
    Defines a Collection filter which is a collection of mayavi
    filters/components bundled into one.
    """

    # The filters we manage.
    filters = List(Instance(PipelineBase), record=True)

    ########################################
    # Private traits.

    # Is the pipeline ready?  Used internally.
    _pipeline_ready = Bool(False)

    ######################################################################
    # `object` interface.
    ######################################################################
    def __set_pure_state__(self, state):
        # Create and set the filters.
        handle_children_state(self.filters, state.filters)
        # Restore our state using the super class method.
        super(Collection, self).__set_pure_state__(state)

    ######################################################################
    # HasTraits interface.
    ######################################################################
    def default_traits_view(self):
        """Returns the default traits view for this object."""
        le = ListEditor(use_notebook=True,
                        deletable=False,
                        export='DockWindowShell',
                        page_name='.name')
        view = View(Group(Item(name='filters',
                               style='custom',
                               show_label=False,
                               editor=le,
                               resizable=True),
                              show_labels=False),
                    resizable=True)
        return view

    ######################################################################
    # `Filter` interface.
    ######################################################################
    def setup_pipeline(self):
        """Setup the pipeline."""
        # Needed because a user may have defined the filters by setting
        # the default value of the trait in the subclass in which case
        # the filters_changed handler will never be called leading to
        # problems.
        if len(self.filters) > 0 and not self._pipeline_ready:
            self._filters_changed([], self.filters)

    def stop(self):
        # There is no need to override start since the wrapped filters
        # are always started automatically in the filters_changed
        # handler.
        super(Collection, self).stop()
        for filter in self.filters:
            filter.stop()

    def update_pipeline(self):
        """This method *updates* the tvtk pipeline when data upstream is
        known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        self._setup_pipeline()
        # Propagate the event.
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
    def _setup_pipeline(self):
        """Sets up the objects in the pipeline."""
        if len(self.inputs) == 0 or len(self.filters) == 0:
            return
        # Our input.
        my_input = self.inputs[0]
        filters = self.filters
        if not self._pipeline_ready:
            # Hook up our first filter.
            first = self.filters[0]
            first.inputs = [my_input]
            # Hook up the others to each other.
            for i in range(1, len(filters)):
                filter = filters[i]
                filter.inputs = [filters[i-1]]
            self._pipeline_ready = True
        # Start filters.
        for filter in filters:
            filter.start()
        # Set our outputs
        last = filters[-1]
        self._set_outputs(last.outputs)

    def _filters_changed(self, old, new):
        """Static traits handler."""
        self._handle_filters_changed(old, new)

    def _filters_items_changed(self, list_event):
        """Static traits handler."""
        self._handle_filters_changed(list_event.removed,
                                     list_event.added)

    def _scene_changed(self, old, new):
        """Static traits handler."""
        for filter in self.filters:
            filter.scene = new
        super(Collection, self)._scene_changed(old, new)

    def _handle_filters_changed(self, removed, added):
        for filter in removed:
            self._setup_events(filter, remove=True)
            filter.stop()
        for filter in added:
            if self.scene is not None:
                filter.scene = self.scene
            if len(filter.name) == 0:
                filter.name = filter.__class__.__name__
            if filter is self.filters[-1]:
                self._setup_events(filter)
        self._pipeline_ready = False
        self._setup_pipeline()

    def _fire_pipeline_changed(self):
        # When the last filter fires a pipeline changed we should reset
        # our outputs to that of its outputs.  Calling _setup_pipeline
        # is expensive and will cause a recursion error.
        self._set_outputs(self.filters[-1].outputs)

    def _setup_events(self, obj, remove=False):
        obj.on_trait_change(self.update_data, 'data_changed',
                            remove=remove)
        obj.on_trait_change(self._fire_pipeline_changed,
                            'pipeline_changed', remove=remove)

    def _visible_changed(self, value):
        for filter in self.filters:
            filter.visible = value
        super(Collection, self)._visible_changed(value)

    def _recorder_changed(self, old, new):
        super(Collection, self)._recorder_changed(old, new)
        for filter in self.filters:
            filter.recorder = new
