from enthought.traits.ui.api import Item, Group, View, ImageEnumEditor
from enthought.mayavi.core import lut 
from enthought.mayavi.core.lut_manager import lut_mode_list
import os
lut_image_dir = os.path.dirname(lut.__file__)



# The view of this object.
view = View(Group(Item(name='lut_mode',
                   editor=ImageEnumEditor( values=lut_mode_list() , 
                                            cols=6,
                                            path=lut_image_dir)),
                  Item(name='file_name', visible_when="lut_mode=='file'"), 
                  Item(name='show_scalar_bar'),
                  Item(name='reverse_lut'),
                  Item(name='number_of_colors'),
                  Item(name='number_of_labels'),
                  Item(name='shadow'),
                  Item(name='use_default_name'),
                  Item(name='data_name'),
                  Item(name='use_default_range'),
                  Item(name='data_range',
                       enabled_when='not object.use_default_range'),
                  label='LUT Manager',
                  ),
            Group(Item(name='_title_text_property',
                       style='custom',
                       resizable=True),
                  show_labels=False,
                  label='Title'),
            Group(Item(name='_label_text_property',
                       style='custom',
                       resizable=True),
                  show_labels=False,
                  label='Labels'),
            resizable=True
            )
