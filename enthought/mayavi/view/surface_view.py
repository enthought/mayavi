from enthought.traits.ui.api import Item, Group, View

view = View(Group(Item(name='enable_contours', label='Enable Contours'),
                  Group(Item(name='contour', style='custom',
                             enabled_when='object.enable_contours'),
                        show_labels=False,
                  ),
                  show_labels=True,
                  label='Contours'
            ),
            
            Group(
                  Item(name='actor', style='custom'),
                  show_labels=False,
                  label='Actor / Texturing',
            ),       
        )
