"""
Traits View definition file.

The view trait of the parent class is extracted from the model definition
file.  This file can either be exec()ed or imported.  See
core/base.py:Base.trait_view() for what is currently used.  Using exec()
allows view changes without needing to restart Mayavi, but is slower than
importing.
"""
# Authors: Prabhu Ramachandran <prabhu_r@users.sf.net>
#          Judah De Paula <judah@enthought.com>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

from traits.etsconfig.api import ETSConfig
from traitsui.api \
    import Item, Group, View, ImageEnumEditor, InstanceEditor, HGroup
from mayavi.core.lut_manager import lut_mode_list, \
            lut_image_dir

def _number_of_lut_cols():
    return 1 if ETSConfig.toolkit == 'qt4' else 6

# The view of the LUT Manager object.
view = View(Group(Item(name='lut_mode',
                       editor=ImageEnumEditor(values=lut_mode_list(),
                                              cols=_number_of_lut_cols(),
                                              path=lut_image_dir)),
                  Item(name='file_name', visible_when="lut_mode=='file'"),
                  Item(name='number_of_colors'),
                  Item(name='reverse_lut'),
                  Item(name='lut',
                       show_label=False,
                       editor=InstanceEditor(label='Edit LUT properties',
                                             id='mayavi.core.lut_manager.edit_lut')),
                  Item(name='scalar_bar_representation',
                       show_label=False,
                       visible_when='scalar_bar_representation is not None',
                       editor=InstanceEditor(label='Edit Legend representation',
                                             id='mayavi.core.lut_manager.edit_represetation')),
                  Item(name='create_lut', show_label=False),

                  Group(Item(name='show_legend'),
                      Group(
                          Item(name='number_of_labels'),
                          enabled_when='show_scalar_bar==True',
                      ),
                      Group(
                          Item(name='shadow'),
                          Item(name='use_default_name'),
                          Item(name='data_name',
                               enabled_when='not object.use_default_name'),
                          HGroup(
                              Item(name='_title_text_property',
                                   show_label=False,
                                   editor=InstanceEditor(label='Edit bar Title',
                                        id='mayavi.core.lut_manager.bar_title_text')),
                              Item(name='_label_text_property',
                                   show_label=False,
                                   editor=InstanceEditor(label='Edit bar Text',
                                        id='mayavi.core.lut_manager.bar_label_text'),
                                   label='Edit bar Text'),
                          ),
                          HGroup(
                              Item(name='scalar_bar',
                                   show_label=False,
                                   editor=InstanceEditor(label='Edit bar Actor',
                                       id='mayavi.core.lut_manager.bar_actor'),
                                   ),
                              Item(name='scalar_bar_widget',
                                   show_label=False,
                                   editor=InstanceEditor(label='Edit bar Widget',
                                        id='mayavi.core.lut_manager.bar_widget'),
                                  ),
                          ),
                          enabled_when='show_scalar_bar==True',
                      ),
                      show_border=True,
                  ),
                  Group(
                      Item(name='use_default_range'),
                      Item(name='data_range',
                          enabled_when='not object.use_default_range'),
                      show_border=True,
                  ),
                  label='LUT (Look Up Table) Manager',
             ),

# Delete this once we're sure we want to keep the new integrated format.
#            Group(Item(name='_title_text_property',
#                       style='custom',
#                       resizable=True),
#                  show_labels=False,
#                  defined_when='show_scalar_bar==True',
#                  label='Title'),
#            Group(Item(name='_label_text_property',
#                       style='custom',
#                       resizable=True),
#                  enabled_when='show_scalar_bar==True',
#                  show_labels=False,
#                  label='Labels'),

            resizable=True,
        )
