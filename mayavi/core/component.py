"""The base class for all MayaVi components.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import List

# Local imports.
from mayavi.core.pipeline_base import PipelineBase


######################################################################
# `Component` class.
######################################################################
class Component(PipelineBase):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # A list of inputs for this component.
    inputs = List(record=False)

    # A list of sources for this component.
    sources = List(record=False)


    ######################################################################
    # `object` interface
    ######################################################################
    def __init__(self, **traits):
        super(Component, self).__init__(**traits)

        # Let the filter setup its pipeline.
        self.setup_pipeline()

    def __get_pure_state__(self):
        d = super(Component, self).__get_pure_state__()
        # Remove dynamically set things.
        for x in ['inputs', 'sources']:
            d.pop(x, None)
        return d

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
        pass

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        raise NotImplementedError

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Invoke render to update any changes.
        self.render()
        # Propagate the data_changed event.
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

        # Setup event handlers.
        self._setup_event_handlers()

        # Update the pipeline.
        self.update_pipeline()

        # Call parent method to set the state.
        super(Component, self).start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        if not self.running:
            return

        # Teardown event handlers.
        self._teardown_event_handlers()

        # Call parent method to set the state.
        super(Component, self).stop()

    ######################################################################
    # Non-public interface
    ######################################################################
    def _inputs_changed(self, old, new):
        if self.running:
            self.update_pipeline()
            self._setup_events(old, new)

    def _inputs_items_changed(self, list_event):
        if self.running:
            self.update_pipeline()
            self._setup_events(list_event.removed, list_event.added)

    def _sources_changed(self, old, new):
        if self.running:
            self.update_pipeline()
            self._setup_events(old, new)

    def _sources_items_changed(self, list_event):
        if self.running:
            self.update_pipeline()
            self._setup_events(list_event.removed, list_event.added)

    def _setup_event_handlers(self):
        self._setup_events([], self.inputs)
        self._setup_events([], self.sources)

    def _teardown_event_handlers(self):
        self._setup_events(self.inputs, [])
        self._setup_events(self.sources, [])

    def _setup_events(self, removed, added):
        for object in removed:
            object.on_trait_event(self.update_pipeline, 'pipeline_changed',
                                  remove=True)
            object.on_trait_event(self.update_data, 'data_changed',
                                  remove=True)
        for object in added:
            object.on_trait_event(self.update_pipeline, 'pipeline_changed')
            object.on_trait_event(self.update_data, 'data_changed')
