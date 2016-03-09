"""The base class for many filters.
"""
# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
# Copyright (c) 2006, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item
from tvtk.api import tvtk

# Local imports
from mayavi.core.filter import Filter

######################################################################
# `FilterBase` class.
######################################################################
class FilterBase(Filter):
    """The base class for many of the filters.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.Object, allow_none=False, record=True)

    # The view of these filters.

    view = View(Group(Item(name='filter', style='custom', resizable=True,
                      show_label=False), springy=True),
                scrollable=True,
                resizable=True
                )

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
        f = self.filter
        if f is not None:
            # Just hook up the filter so the update_data method is
            # called when the traits change.
            f.on_trait_change(self.update_data)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        # Do nothing if there is no input.
        inputs = self.inputs
        fil = self.filter
        if len(inputs) == 0 or fil is None:
            return

        # By default we set the input to the first output of the first
        # input.
        self.configure_connection(fil, inputs[0])
        fil.update()
        self._set_outputs([fil])

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Do nothing if there is no input and we aren't running.
        if len(self.inputs) == 0 or not self.running:
            return

        self.filter.update()
        # Propagate the data_changed event.
        self.data_changed = True

    def _filter_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.update_data, remove=True)

        new.on_trait_change(self.update_data)

        if old is not None:
            self.update_pipeline()
