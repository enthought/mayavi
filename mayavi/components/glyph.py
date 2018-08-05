"""A component that allows one to place colored and scaled glyphs at
input point data.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
#         KK Rai (kk.rai [at] iitb.ac.in)
#         R. Ambareesha (ambareesha [at] iitb.ac.in)
# Copyright (c) 2005-2018, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Trait, Bool
from traits.api import Enum
from traitsui.api import View, Group, Item
from tvtk.api import tvtk
from tvtk.tvtk_base import TraitRevPrefixMap

# Local imports.
from mayavi.core.component import Component
from mayavi.core.module import Module
from mayavi.components import glyph_source


######################################################################
# `Glyph` class.
######################################################################
class Glyph(Component):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # Type of Glyph: 'tensor' or 'vector'
    glyph_type = Enum('vector', 'tensor',
                      desc = 'if the glyph is vector or tensor')

    # The scaling mode to use when scaling the glyphs.  We could have
    # used the glyph's own scale mode but it allows users to set the
    # mode to use vector components for the scaling which I'd like to
    # disallow.
    scale_mode = Trait('scale_by_scalar',
                       TraitRevPrefixMap({'scale_by_vector': 1,
                                          'scale_by_vector_components': 2,
                                          'data_scaling_off': 3,
                                          'scale_by_scalar': 0}),
                       desc="if scaling is done using scalar or vector/normal magnitude"
                       )

    # The color mode to use when coloring the glyphs.  We could have
    # used the glyph's own color_mode trait but it allows users to set
    # the mode to use vector components for the scaling which I'd
    # like to disallow.
    color_mode = Trait('color_by_scalar',
                       TraitRevPrefixMap({'color_by_vector': 2,
                                          'color_by_scalar': 1,
                                          'no_coloring': 0}),
                       desc="if coloring is done by scalar or vector/normal magnitude"
                       )
    color_mode_tensor = Trait('scalar',
                              TraitRevPrefixMap({'scalars': 1,
                                                 'eigenvalues':2,
                                                 'no_coloring': 0}),
                              desc="if coloring is done by scalar or eigenvalues"
                             )

    # Specify if the input points must be masked.  By mask we mean
    # that only a subset of the input points must be displayed.
    mask_input_points = Bool(False, desc="if input points are masked")

    # The MaskPoints filter.
    mask_points = Instance(tvtk.MaskPoints, args=(),
                           kw={'random_mode': True}, record=True)

    # The Glyph3D instance.
    glyph = Instance(tvtk.Object, allow_none=False, record=True)

    # The Source to use for the glyph.  This is chosen from
    # `self._glyph_list` or `self.glyph_dict`.
    glyph_source = Instance(glyph_source.GlyphSource,
                            allow_none=False, record=True)

    # The module associated with this component.  This is used to get
    # the data range of the glyph when the scale mode changes.  This
    # *must* be set if this module is to work correctly.
    module = Instance(Module)

    # Should we show the GUI option for changing the scalar mode or
    # not?  This is useful for vector glyphing modules where there it
    # does not make sense to scale the data based on scalars.
    show_scale_mode = Bool(True)

    ########################################
    # Private traits.

    # Used for optimization.
    _updating = Bool(False)

    ########################################
    # View related traits.

    view = View(Group(Item(name='mask_input_points'),
                      Group(Item(name='mask_points',
                                 enabled_when='object.mask_input_points',
                                 style='custom', resizable=True),
                            show_labels=False,
                            ),
                      label='Masking',
                      ),
                Group(Group(Item(name='scale_mode',
                                 enabled_when='show_scale_mode',
                                 visible_when='show_scale_mode'),
                            Item(name='color_mode',
                                 enabled_when= 'glyph_type == "vector"',
                                 visible_when= 'glyph_type == "vector"'),
                            Item(name='color_mode_tensor',
                                 enabled_when= 'glyph_type == "tensor"',
                                 visible_when= 'glyph_type == "tensor"'),
                            ),
                      Group(Item(name='glyph', style='custom',
                                 resizable=True),
                            show_labels=False),
                      label='Glyph',
                      selected=True,
                      ),
                Group(Item(name='glyph_source',
                                 style='custom', resizable=True),
                      show_labels=False,
                      label='Glyph Source',
                      ),
                resizable=True
                )

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(Glyph, self).__get_pure_state__()
        for attr in ('module', '_updating'):
            d.pop(attr, None)
        return d


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
        self._glyph_type_changed(self.glyph_type)
        self.glyph_source = glyph_source.GlyphSource()

        # Handlers to setup our source when the sources pipeline changes.
        self.glyph_source.on_trait_change(self._update_source, 'pipeline_changed')
        self.mask_points.on_trait_change(self.render)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        if ((len(self.inputs) == 0) or (len(self.inputs[0].outputs) == 0)):
            return

        self._mask_input_points_changed(self.mask_input_points)
        if self.glyph_type == 'vector':
            self._color_mode_changed(self.color_mode)
        else:
            self._color_mode_tensor_changed(self.color_mode_tensor)
        self._scale_mode_changed(self.scale_mode)

        # Set our output.
        self.outputs = [self.glyph]
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        self._scale_mode_changed(self.scale_mode)
        self.data_changed = True

    def render(self):
        if not self._updating:
            super(Glyph, self).render()

    def start(self):
        """Overridden method.
        """
        if self.running:
            return
        self.glyph_source.start()
        super(Glyph, self).start()

    def stop(self):
        if not self.running:
            return
        self.glyph_source.stop()
        super(Glyph, self).stop()

    def has_output_port(self):
        """ The filter has an output port."""
        return True

    def get_output_object(self):
        """ Returns the output port."""
        return self.glyph.output_port

    ######################################################################
    # Non-public methods.
    ######################################################################
    def _update_source(self):
        self.configure_source_data(self.glyph, self.glyph_source.outputs[0])

    def _glyph_source_changed(self, value):
        self.configure_source_data(self.glyph, value.outputs[0])

    def _color_mode_changed(self, value):
        if len(self.inputs) == 0:
            return
        if value != 'no_coloring':
            self.glyph.color_mode = value

    def _color_mode_tensor_changed(self, value):
        if len(self.inputs) == 0:
            return
        self._updating = True
        if value != 'no_coloring':
            self.glyph.color_mode = value
            self.glyph.color_glyphs = True
        else:
            self.glyph.color_glyphs = False
        self._updating = False
        self.render()

    def _scale_mode_changed(self, value):
        if (self.module is None) or (len(self.inputs) == 0)\
                                 or self.glyph_type == 'tensor':
            return

        self._updating = True
        try:
            glyph = self.glyph
            glyph.scale_mode = value

            mm = self.module.module_manager
            if glyph.scale_mode == 'scale_by_scalar':
                glyph.range = tuple(mm.scalar_lut_manager.data_range)
            else:
                glyph.range = tuple(mm.vector_lut_manager.data_range)
        finally:
            self._updating = False
            self.render()

    def _mask_input_points_changed(self, value):
        inputs = self.inputs
        if len(inputs) == 0:
            return
        if value:
            mask = self.mask_points
            self.configure_connection(mask, inputs[0].outputs[0])
            self.configure_connection(self.glyph, mask)
        else:
            self.configure_connection(self.glyph, inputs[0])
        self.glyph.update()

    def _glyph_type_changed(self, value):
        if self.glyph_type == 'vector':
            self.glyph = tvtk.Glyph3D(clamping=True)
        else:
            self.glyph = tvtk.TensorGlyph(scale_factor=0.1)
            self.show_scale_mode = False
        self.glyph.on_trait_change(self.render)

    def _scene_changed(self, old, new):
        super(Glyph, self)._scene_changed(old, new)
        self.glyph_source.scene = new
