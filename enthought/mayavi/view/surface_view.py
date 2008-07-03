from enthought.traits.ui.api import Item, Group, View, InstanceEditor
from enthought.mayavi.view.actor_view import actor_view, texture_view

view = View(Group(Item(name='enable_contours', label='Enable Contours'),
                  Group(Item(name='contour', style='custom',
                             enabled_when='object.enable_contours'),
                        show_labels=False,
                  ),
                  show_labels=True,
                  label='Contours'
            ),
            
            Group(Item('actor', 
                       resizable=True, style='custom',
                       editor=InstanceEditor(view=actor_view)),
                  label='Actor',
                  show_labels=False,
            ),
                  
            Group(Item('actor', 
                       resizable=True, style='custom',
                       editor=InstanceEditor(view=texture_view)),
                  label='Texturing',
                  show_labels=False,
            ),       
        )
