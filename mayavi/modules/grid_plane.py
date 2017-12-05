"""A simple grid plane module.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item

# Local imports
from mayavi.core.module import Module
from mayavi.components import grid_plane
from mayavi.components.actor import Actor
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `GridPlane` class.
######################################################################
class GridPlane(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    grid_plane = Instance(grid_plane.GridPlane, allow_none=False,
                          record=True)

    actor = Instance(Actor, allow_non=False, record=True)

    input_info = PipelineInfo(datasets=['image_data',
                                        'structured_grid',
                                        'rectilinear_grid'],
                              attribute_types=['any'],
                              attributes=['any'])


    view = View(Group(Item(name='grid_plane', style='custom'),
                      Item(name='actor', style='custom'),
                      show_labels=False))

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
        # Create the components
        self.grid_plane = grid_plane.GridPlane()
        self.actor = Actor()

        # Setup the actor suitably for this module.
        prop = self.actor.property
        prop.trait_set(backface_culling=0, frontface_culling=0,
                 representation='w')
        self.actor.mapper.scalar_visibility = 0

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        # Data is available, so set the input for the grid plane.
        self.grid_plane.inputs = [mm.source]
        # Set the LUT for the mapper.
        self.actor.set_lut(mm.scalar_lut_manager.lut)

        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the component should do the rest.
        self.data_changed = True

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _grid_plane_changed(self, old, new):
        actor = self.actor
        if actor is not None:
            actor.inputs = [new]
        self._change_components(old, new)

    def _actor_changed(self, old, new):
        new.scene = self.scene
        gp = self.grid_plane
        if gp is not None:
            new.inputs = [gp]
        self._change_components(old, new)

