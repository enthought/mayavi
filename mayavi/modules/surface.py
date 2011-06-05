"""Draws a surface for any input dataset with optional contouring.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance, Bool
from tvtk.api import tvtk

# Local imports
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.module import Module
from mayavi.components.contour import Contour
from mayavi.components.actor import Actor


######################################################################
# `Surface` class.
######################################################################
class Surface(Module):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # Specifies if contouring is to be done or not.
    enable_contours = Bool(False, desc='if contours are generated')

    # The contour component that contours the data.
    contour = Instance(Contour, allow_none=False, record=True)

    # The actor component that represents the visualization.
    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.  You should also
        set the `actors` attribute up at this point.
        """
        # Setup the objects.
        self.contour = Contour(auto_contours=True, number_of_contours=10)
        self.actor = Actor()
        # Setup the actor suitably for this module.
        self.actor.property.line_width = 2.0

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        # This makes sure that any changes made to enable_contours
        # when the module is not running are updated when it is
        # started.  Also sets up the pipeline and inputs correctly.
        self._enable_contours_changed(self.enable_contours)
        # Set the LUT for the mapper.
        self.actor.set_lut(mm.scalar_lut_manager.lut)

        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the components should do the rest if
        # they are connected.
        self.data_changed = True

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _filled_contours_changed(self, value):
        """When filled contours are enabled, the mapper should use the
        the cell data, otherwise it should use the default scalar
        mode.
        """
        if value:
            self.actor.mapper.scalar_mode = 'use_cell_data'
        else:
            self.actor.mapper.scalar_mode = 'default'
        self.render()

    def _enable_contours_changed(self, value):
        """Turns on and off the contours."""
        if self.module_manager is None:
            return
        if value:
            self.contour.inputs = [self.module_manager.source]
            self.actor.inputs = [self.contour]
            if self.contour.filled_contours:
                self.actor.mapper.scalar_mode = 'use_cell_data'
        else:
            old_inputs = self.actor.inputs
            self.actor.inputs = [self.module_manager.source]
            self.actor.mapper.scalar_mode = 'default'
        self.render()

    def _contour_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self._filled_contours_changed,
                                'filled_contours',
                                remove=True)
        new.on_trait_change(self._filled_contours_changed,
                            'filled_contours')
        self._change_components(old, new)

    def _actor_changed(self, old, new):
        if old is None:
            # First time the actor is set.
            new.mapper = tvtk.DataSetMapper(use_lookup_table_scalar_range=1)
        new.scene = self.scene
        mm = self.module_manager
        if mm is not None:
            new.inputs = [mm.source]
        self._change_components(old, new)

