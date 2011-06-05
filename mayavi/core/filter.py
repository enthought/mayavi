"""The base filter class from which all MayaVi filters derive.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import List, Str

# Local imports
from mayavi.core.source import Source
from mayavi.core.pipeline_base import PipelineBase
from mayavi.core.pipeline_info import (PipelineInfo,
        get_tvtk_dataset_name)


######################################################################
# `Filter` class.
######################################################################
class Filter(Source):
    """ Base class for all the Mayavi filters.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The inputs for this filter.
    inputs = List(PipelineBase, record=False)

    # The icon
    icon = Str('filter.ico')

    # The human-readable type for this object
    type = Str(' filter')

    # Information about what this object can consume.
    input_info = PipelineInfo(datasets=['any'])

    ######################################################################
    # `object` interface.
    ######################################################################
    def __init__(self, **traits):
        super(Filter, self).__init__(**traits)

        # Let the filter setup its pipeline.
        self.setup_pipeline()

    def __get_pure_state__(self):
        d = super(Filter, self).__get_pure_state__()
        # Inputs are setup dynamically, don't pickle them.
        d.pop('inputs', None)
        return d

    ######################################################################
    # `Filter` interface.
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

        # Call parent method to start the children and set the state.
        super(Filter, self).start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.  This is where you remove your actors from the
        scene.
        """
        if not self.running:
            return

        # Teardown event handlers.
        self._teardown_event_handlers()

        # Call parent method to stop the children and set the state.
        super(Filter, self).stop()

    ######################################################################
    # Non-public interface
    ######################################################################
    def _set_outputs(self, new_outputs):
        """Set `self.outputs` to the given list of `new_outputs`.  You
        should always use this method to set `self.outputs`.
        """
        old_outputs = self.outputs
        self.outputs = new_outputs
        if len(new_outputs) > 0:
            self.output_info.datasets = \
                [get_tvtk_dataset_name(new_outputs[0])]
        if old_outputs == self.outputs:
            # Even if the outputs don't change we want to propagate a
            # data_changed event since the data could have changed.
            self.data_changed = True

    def _inputs_changed(self, old, new):
        if self.running:
            self.update_pipeline()
            self._setup_input_events(old, new)

    def _inputs_items_changed(self, list_event):
        if self.running:
            self.update_pipeline()
            self._setup_input_events(list_event.removed, list_event.added)

    def _setup_event_handlers(self):
        self._setup_input_events([], self.inputs)

    def _teardown_event_handlers(self):
        self._setup_input_events(self.inputs, [])

    def _setup_input_events(self, removed, added):
        for input in removed:
            input.on_trait_event(self.update_pipeline, 'pipeline_changed',
                                 remove=True)
            input.on_trait_event(self.update_data, 'data_changed',
                                 remove=True)
        for input in added:
            input.on_trait_event(self.update_pipeline, 'pipeline_changed')
            input.on_trait_event(self.update_data, 'data_changed')

