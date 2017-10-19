"""Takes an arbitrary slice of the input data using an implicit cut
plane and places glyphs according to the vector field data.  The
glyphs may be colored using either the vector magnitude or the scalar
attributes.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item

# Local imports
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.module import Module
from mayavi.components.implicit_plane import ImplicitPlane
from mayavi.components.cutter import Cutter
from mayavi.components.glyph import Glyph
from mayavi.components.actor import Actor


######################################################################
# `VectorCutPlane` class.
######################################################################
class VectorCutPlane(Module):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The implicit plane widget used to place the implicit function.
    implicit_plane = Instance(ImplicitPlane, allow_none=False,
                              record=True)

    # The cutter.  Takes a cut of the data on the implicit plane.
    cutter = Instance(Cutter, allow_none=False, record=True)

    # The Glyph component.
    glyph = Instance(Glyph, allow_none=False, record=True)

    # The Glyph component.
    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['vectors'])

    ########################################
    # View related traits.

    view = View(Group(Item(name='implicit_plane', style='custom'),
                      label='ImplicitPlane',
                      show_labels=False),
                Group(Item(name='glyph', style='custom', resizable=True),
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
        # Create the objects and set them up.
        self.implicit_plane = ImplicitPlane()
        self.cutter = Cutter()
        self.glyph = Glyph(module=self,
                           scale_mode='scale_by_vector',
                           color_mode='color_by_vector',
                           show_scale_mode=False)
        self.glyph.glyph_source.glyph_position='tail'
        actor = self.actor = Actor()
        actor.mapper.scalar_visibility = 1
        actor.property.trait_set(line_width=2, backface_culling=False,
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

        self.implicit_plane.inputs = [mm.source]

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

    def _implicit_plane_changed(self, old, new):
        cutter = self.cutter
        if cutter is not None:
            cutter.cut_function = new.plane
            cutter.inputs = [new]
        self._change_components(old, new)

    def _cutter_changed(self, old, new):
        ip = self.implicit_plane
        if ip is not None:
            new.cut_function = ip.plane
            new.inputs = [ip]
        g = self.glyph
        if g is not None:
            g.inputs = [new]
        self._change_components(old, new)

    def _glyph_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self._color_mode_changed,
                                'color_mode',
                                remove=True)
        new.module = self
        cutter = self.cutter
        if cutter:
            new.inputs = [cutter]
        new.on_trait_change(self._color_mode_changed,
                            'color_mode')
        self._change_components(old, new)

    def _actor_changed(self, old, new):
        new.scene = self.scene
        glyph = self.glyph
        if glyph is not None:
            new.inputs = [glyph]
        self._change_components(old, new)

