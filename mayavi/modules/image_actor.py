"""Displays ImageData efficiently.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance, Bool, on_trait_change, \
        Property
from traitsui.api import View, Group, Item
from tvtk.api import tvtk

# Local imports
from mayavi.core.module import Module
from mayavi.core.pipeline_info import PipelineInfo

######################################################################
# `ImageActor` class
######################################################################
class ImageActor(Module):

    # An image actor.
    actor = Instance(tvtk.ImageActor, allow_none=False, record=True)

    input_info = PipelineInfo(datasets=['image_data'],
                              attribute_types=['any'],
                              attributes=['any'])

    # An ImageMapToColors TVTK filter to adapt datasets without color
    # information
    image_map_to_color = Instance(tvtk.ImageMapToColors, (),
                                  allow_none=False, record=True)

    map_scalars_to_color = Bool

    _force_map_scalars_to_color = Property(depends_on='module_manager.source')

    ########################################
    # The view of this module.

    view = View(Group(Item(name='actor', style='custom',
                           resizable=True),
                      show_labels=False, label='Actor'),
                Group(
                      Group(Item('map_scalars_to_color',
                            enabled_when='not _force_map_scalars_to_color')),
                      Item('image_map_to_color', style='custom',
                           enabled_when='map_scalars_to_color',
                           show_label=False),
                      label='Map Scalars',
                     ),
                width=500,
                height=600,
                resizable=True)

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        self.actor = tvtk.ImageActor()

    @on_trait_change('map_scalars_to_color,'
                     'image_map_to_color.[output_format,pass_alpha_to_output],'
                     'module_manager.scalar_lut_manager.lut_mode,'
                     'module_manager.vector_lut_manager.lut_mode')
    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.
        """
        mm = self.module_manager
        if mm is None:
            return
        src = mm.source
        if self._force_map_scalars_to_color:
            self.trait_set(map_scalars_to_color=True,
                           trait_change_notify=False)
        if self.map_scalars_to_color:
            self.configure_connection(self.image_map_to_color, src)
            self.image_map_to_color.lookup_table = mm.scalar_lut_manager.lut
            self.image_map_to_color.update()
            self.configure_input(self.actor.mapper,
                                 self.image_map_to_color)
        else:
            self.configure_input(self.actor.mapper, src.outputs[0])
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

    def _get__force_map_scalars_to_color(self):
        mm = self.module_manager
        if mm is None:
            return False
        src = mm.source
        return not isinstance(src.get_output_dataset().point_data.scalars,
                              tvtk.UnsignedCharArray)
