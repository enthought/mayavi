from enthought.traits.ui.api import Item, Group, View

view = View(Group(Item(name='function'),
                  Item(name='parametric_function',
                       style='custom',
                       resizable=True),
                   label='Function',
                    show_labels=False
                   ),
             Group(Item(name='source',
                        style='custom',
                        resizable=True),
                    label='Source',
                    show_labels=False),
             resizable=True)