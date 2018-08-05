"""A simple actor component.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2016, Enthought, Inc.
# License: BSD Style.

import vtk

# Enthought library imports.
from traits.api import Instance, Bool, Enum
from tvtk.api import tvtk
from traits.api import DelegatesTo
from tvtk.common import is_old_pipeline

# Local imports.
from mayavi.core.component import Component
from mayavi.core.source import Source
from mayavi.core.utils import get_new_output


######################################################################
# `Actor` class.
######################################################################
class Actor(Component):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The mapper.
    mapper = Instance(tvtk.Mapper, record=True)

    # The actor.
    actor = Instance(tvtk.Actor, record=True)

    # The actor's property.
    property = Instance(tvtk.Property, record=True)

    # FIXME: None of the texture stuff is picklable.  This will NOT be
    # supported till the pickling infrastructure is cleaned up and
    # fixed.

    # If texturing is enabled for the actor or not
    enable_texture = Bool(False, desc='if texturing is enabled')

    # The source of the texture's image
    texture_source_object = Instance(Source)

    # The actors texture
    texture = Instance(tvtk.Texture, record=True)

    # The texture coord generation mode.
    tcoord_generator_mode = Enum('none', 'cylinder', 'sphere', 'plane',
                                 desc='the mode for texture coord generation')

    # Texture coord generator.
    tcoord_generator = Instance(tvtk.Object, allow_none=True)

    # Composite data filter.
    comp_data_geom_filter = Instance(tvtk.CompositeDataGeometryFilter)

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(Actor, self).__get_pure_state__()
        for attr in ('texture', 'texture_source_object',
                     'enable_texture', 'tcoord_generator_mode',
                     'tcoord_generator'):
            d.pop(attr,None)
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
        self.mapper = tvtk.PolyDataMapper(use_lookup_table_scalar_range=1)
        self.actor = tvtk.Actor()
        self.property = self.actor.property
        self.texture = tvtk.Texture()

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        if (len(self.inputs) == 0) or \
               (len(self.inputs[0].outputs) == 0):
            return

        input = self.inputs[0].outputs[0]
        if input is None:
            return

        self._connect_mapper(input)
        self._tcoord_generator_mode_changed(self.tcoord_generator_mode)
        self.render()

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Invoke render to update any changes.
        if not is_old_pipeline():
            from mayavi.modules.outline import Outline
            from mayavi.components.glyph import Glyph
            #FIXME: A bad hack, but without these checks results in seg fault
            input = self.inputs[0]
            if isinstance(input, Outline) or isinstance(input, Glyph):
                self.mapper.update(0)
            else:
                self.mapper.update()
        self.render()

    ######################################################################
    # `Actor` interface
    ######################################################################
    def set_lut(self, lut):
        """Set the Lookup table to use."""
        self.mapper.lookup_table = lut
        # A hack to avoid a problem with the VRML output that seems to
        # ignore the use_lookup_table_scalar_range setting
        # on the mapping
        self.mapper.scalar_range = lut.table_range

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _setup_handlers(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)
        new.on_trait_change(self.render)

    def _get_correct_input(self, input):
        do = get_new_output(input)
        if do.is_a('vtkCompositeDataSet'):
            cdgf = self.comp_data_geom_filter
            cdgf.input_connection = input.output_port
            return cdgf
        else:
            return input

    def _comp_data_geom_filter_default(self):
        return tvtk.CompositeDataGeometryFilter()

    def _connect_mapper(self, input):
        if input is None:
            return
        inp = self._get_correct_input(input)
        self.configure_input(self.mapper, inp)

    def _mapper_changed(self, old, new):
        # Setup the handlers.
        self._setup_handlers(old, new)
        # Setup the LUT.
        if old is not None:
            self.set_lut(old.lookup_table)
        # Setup the inputs to the mapper.
        if (len(self.inputs) > 0) and (len(self.inputs[0].outputs) > 0):
            self._connect_mapper(self.inputs[0].outputs[0])
        # Setup the actor's mapper.
        actor = self.actor
        if actor is not None:
            actor.mapper = new
        self.render()

    def _actor_changed(self, old, new):
        # Setup the handlers.
        self._setup_handlers(old, new)
        # Set the mapper.
        mapper = self.mapper
        if mapper is not None:
            new.mapper = mapper
        # Set the property.
        prop = self.property
        if prop is not None:
            new.property = prop
        # Setup the `actors` trait.
        self.actors = [new]

    def _property_changed(self, old, new):
        # Setup the handlers.
        self._setup_handlers(old, new)
        # Setup the actor.
        actor = self.actor
        if new is not actor.property:
            actor.property = new

    def _foreground_changed_for_scene(self, old, new):
        # Change the default color for the actor.
        self.property.color = new
        self.render()

    def _scene_changed(self, old, new):
        super(Actor, self)._scene_changed(old, new)
        self._foreground_changed_for_scene(None, new.foreground)

    def _enable_texture_changed(self, value):
        if self.texture_source_object is None :
            self.actor.texture = None
            return
        if value:
            self.actor.texture = self.texture
        else:
            self.actor.texture = None

    def _can_object_give_image_data(self, source):
        if source is None:
            return False
        if not isinstance(source, Source):
            return False
        if source.get_output_dataset().is_a('vtkImageData'):
            return True
        return False

    def _change_texture_input(self):
        if self._can_object_give_image_data(self.texture_source_object):
            self.configure_connection(
                self.texture, self.texture_source_object
            )
            self.actor.texture = self.texture
        else:
            self.texture_source_object = None

    def _texture_source_object_changed(self,old,new):
        if old is not None :
            old.on_trait_change(self._change_texture_input,
                                'pipeline_changed',
                                remove=True)
        if new is not None :
            new.on_trait_change(self._change_texture_input,
                                'pipeline_changed' )

        if new is not None:
            self._change_texture_input()
        else:
            self.actor.texture = None
            self.texture.input = None
            self.texture.input_connection = None

    def _texture_changed(self,value):
        # Setup the actor's texture.
        actor = self.actor
        if actor is not None and (value.input is not None
                                  or value.input_connection is not None):
            actor.texture = value
            self.texture.on_trait_change(self.render)

        self.render()

    def _tcoord_generator_mode_changed(self, value):
        inp = self.inputs
        if (len(inp) == 0) or \
               (len(inp[0].outputs) == 0):
            return
        old_tg = self.tcoord_generator
        if old_tg is not None:
            old_tg.on_trait_change(self.render, remove=True)
        if value == 'none':
            self.tcoord_generator = None
            self._connect_mapper(inp[0].outputs[0])
        else:
            tg_dict = {'cylinder': tvtk.TextureMapToCylinder,
                       'sphere': tvtk.TextureMapToSphere,
                       'plane': tvtk.TextureMapToPlane}
            tg = tg_dict[value]()
            self.tcoord_generator = tg
            actual_input = self._get_correct_input(inp[0].outputs[0])
            self.configure_connection(tg, actual_input)
            self.configure_connection(self.mapper, tg)
        tg = self.tcoord_generator
        if tg is not None:
            tg.on_trait_change(self.render)
        self.render()
