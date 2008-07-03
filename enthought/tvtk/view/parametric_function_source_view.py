from enthought.traits.ui.api import View, HGroup, Item
    
view = View((['generate_texture_coordinates'], ['scalar_mode'],
    HGroup(Item('u_resolution', label = 'u'), 
          Item('v_resolution', label = 'v'),
          Item('w_resolution', label = 'w'),
          label = 'Resolution', show_border = True)),
    title='Edit ParametricFunctionSource properties', scrollable=True,
    buttons=['OK', 'Cancel'])
    

