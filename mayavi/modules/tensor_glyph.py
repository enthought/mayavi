""" Displays tensor glyphs oriented and colored as per scalar or vector data at
the input points.

"""
# Authors: KK Rai (kk.rai [at] iitb.ac.in)
#          R. Ambareesha (ambareesha [at] iitb.ac.in)
#          Prabhu Ramachandran <prabhu_r@users.sf.net>

# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item

# Local imports
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.core.module import Module
from mayavi.components.actor import Actor
from mayavi.components import glyph

######################################################################
# `TensorGlyph` class.
######################################################################
class TensorGlyph(Module):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The glyph component we use to do the actual glyphing.
    glyph = Instance(glyph.Glyph, allow_none=False, record=True)

    # The actor.
    actor = Instance(Actor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['tensors'])

    # Create the UI for the traits.
    view = View(Group(Item(name='actor', style='custom'),
                      show_labels=False,
                      label='Actor'),
                Group(Item(name='glyph', style='custom',
                           resizable=True),
                      label='Tensor Glyph',
                      selected=True,
                      show_labels=False
                      ))

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`. Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.  You should also
        set the `actors` attribute up at this point.
        """
        # Setup the glyphs.
        self.glyph = glyph.Glyph(glyph_type='tensor')
        self.glyph.glyph_source.glyph_source = self.glyph.glyph_source.glyph_list[4]
        self.actor = Actor()

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

    def _glyph_changed(self, old, new):
        # Set the glyph's module attribute -- this is important!
        new.module = self
        # Setup actors inputs.
        actor = self.actor
        if actor is not None:
            actor.inputs = [new]
        self._change_components(old, new)


    def _actor_changed(self, old, new):
        new.scene = self.scene
        #new.inputs = [self]
        g = self.glyph
        if g is not None:
            new.inputs = [g]
        self._change_components(old, new)
