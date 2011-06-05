from traitsui.api import View, HGroup, Item
from tvtk.tvtk_base import TVTKBaseHandler

view = View((['generate_texture_coordinates'], ['scalar_mode'],
    HGroup(Item('u_resolution', label = 'u'),
          Item('v_resolution', label = 'v'),
          Item('w_resolution', label = 'w'),
          label = 'Resolution', show_border = True)),
    handler = TVTKBaseHandler,
    title='Edit ParametricFunctionSource properties', scrollable=True,
    buttons=['OK', 'Cancel'])


