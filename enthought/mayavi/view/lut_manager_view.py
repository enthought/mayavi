from enthought.traits.ui.api import Item, Group, View, ImageEnumEditor, InstanceEditor
from enthought.mayavi.core import lut 
from enthought.mayavi.core.lut_manager import lut_mode_list
import os
lut_image_dir = os.path.dirname(lut.__file__)



# The view of the LUT Manager object.
view = View(Group(Item(name='lut_mode',
                       editor=ImageEnumEditor(values=lut_mode_list(), 
                                              cols=6,
                                              path=lut_image_dir)),
                  Item(name='file_name', visible_when="lut_mode=='file'"), 
                  Item(name='number_of_colors'),
                  Item(name='reverse_lut'),
                  
                  Group(Item(name='show_scalar_bar'),
                      Group(   
                          Item(name='number_of_labels'),
                          Item(name='shadow'),
                          Item(name='use_default_name'),
                          Item(name='data_name',
                               enabled_when='not object.use_default_name'),
                          Item(name='use_default_range'),
                          Item(name='data_range',
                               enabled_when='not object.use_default_range'),
                          Item(name='_title_text_property',
                               show_label=False,
                               editor=InstanceEditor(label='Edit bar Title')),
                          Item(name='_label_text_property',
                               show_label=False,
                               editor=InstanceEditor(label='Edit bar Text'),
                               label='Edit bar Text'),
                          enabled_when='show_scalar_bar==True',
                      ),    
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
