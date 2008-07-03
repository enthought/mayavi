from enthought.traits.ui.api import Item, Group, View, EnumEditor
from enthought.mayavi.core.module_manager import LUT_DATA_MODE_TYPES

view = View(Group(Item('scalar_lut_manager', style='custom'),
                  label='Scalar LUT', show_labels=False,
                  selected=True),
            Group(Item('vector_lut_manager', style='custom'),
                  label='Vector LUT', show_labels=False),
            Group(Item('lut_data_mode',
                       style='custom',
                       editor = EnumEditor(values=LUT_DATA_MODE_TYPES)),
                  label='ModuleManager', 
                  selected=False),
            )
