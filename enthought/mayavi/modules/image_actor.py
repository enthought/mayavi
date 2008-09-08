"""Displays ImageData efficiently.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from enthought.traits.api import Instance
from enthought.traits.ui.api import View, Group, Item
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.core.module import Module
from enthought.mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `ImageActor` class
######################################################################
class ImageActor(Module):

    # An image actor.
    actor = Instance(tvtk.ImageActor, allow_none=False, listen=True)

    input_info = PipelineInfo(datasets=['image_data'],
                              attribute_types=['any'],
                              attributes=['any'])    

    ########################################
    # The view of this module.

    view = View(Group(Item(name='actor', style='custom',
                           resizable=True),
                      show_labels=False),
                width=500,
                height=500,
                resizable=True)

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        self.actor = tvtk.ImageActor()
        
    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.
        """
        mm = self.module_manager
        if mm is None:
            return
        src = mm.source
        self.actor.input = src.outputs[0]
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.
        """
        # Just set data_changed, the component should do the rest.
        self.data_changed = True

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _actor_changed(self, old, new):
        if old is not None:
            self.actors.remove(old)
            old.on_trait_change(self.render, remove=True)
        self.actors.append(new)
        new.on_trait_change(self.render)


