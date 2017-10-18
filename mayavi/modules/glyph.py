"""Displays different types of glyphs oriented and colored as per scalar or vector data at the input points.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item

# Local imports
from mayavi.core.module import Module
from mayavi.components import glyph
from mayavi.components.actor import Actor
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `Glyph` class.
######################################################################
class Glyph(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The Glyph component.
    glyph = Instance(glyph.Glyph, allow_none=False, record=True)

    # The Glyph component.
    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    ########################################
    # View related traits.

    view = View(Group(Item(name='glyph', style='custom',
                           resizable=True),
                      label='Glyph',
                      show_labels=False),
                Group(Item(name='actor', style='custom'),
                      label='Actor',
                      show_labels=False),
                )

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
        # Setup the glyphs.
        self.glyph = glyph.Glyph(scale_mode='scale_by_scalar',
                                 color_mode='color_by_scalar',
                                 show_scale_mode=True)

        # Create the components
        actor = self.actor = Actor()
        actor.mapper.scalar_visibility = 1
        actor.property.trait_set(line_width=2,
                                 backface_culling=False,
                                 frontface_culling=False)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return

        self.glyph.inputs = [mm.source]

        # Set the LUT for the mapper.
        self._color_mode_changed(self.glyph.color_mode)

        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the other components should do the rest.
        self.data_changed = True

    ######################################################################
    # Non-public traits.
    ######################################################################
    def _color_mode_changed(self, value):
        # This is a listner for the glyph component's color_mode trait
        # so that the the lut can be changed when the a different
        # color mode is requested.
        if self.module_manager is None:
            return
        actor = self.actor
        if value == 'color_by_scalar':
            actor.mapper.scalar_visibility = 1
            lut_mgr = self.module_manager.scalar_lut_manager
            actor.set_lut(lut_mgr.lut)
        elif value == 'color_by_vector':
            lut_mgr = self.module_manager.vector_lut_manager
            actor.set_lut(lut_mgr.lut)
        else:
            actor.mapper.scalar_visibility = 0

        self.render()

    def _glyph_changed(self, old, new):
        # Hookup a callback to set the lut appropriately.
        if old is not None:
            old.on_trait_change(self._color_mode_changed,
                                'color_mode',
                                remove=True)
        new.on_trait_change(self._color_mode_changed, 'color_mode')

        # Set the glyph's module attribute -- this is important!
        new.module = self

        # Setup actors inputs.
        actor = self.actor
        if actor is not None:
            actor.inputs = [new]
        self._change_components(old, new)

    def _actor_changed(self, old, new):
        # Setup the actors scene and inputs.
        new.scene = self.scene
        g = self.glyph
        if g is not None:
            new.inputs = [g]
        self._change_components(old, new)


