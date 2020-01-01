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


from traitsui.api import Item, Group, View, InstanceEditor
from mayavi.components.ui.actor import actor_view, texture_view

view = View(
            Group(Item(name='enable_contours', label='Enable Contours'),
                  Group(Item(name='contour',
                             style='custom',
                             enabled_when='object.enable_contours'
                             ),
                        show_labels=False,
                  ),
                  show_labels=True,
                  label='Contours'
            ),

            Group(Item('actor',
                       resizable=True,
                       style='custom',
                       editor=InstanceEditor(view=actor_view)
                       ),
                  label='Actor',
                  show_labels=False,
            ),

            Group(Item('actor',
                       resizable=True,
                       style='custom',
                       editor=InstanceEditor(view=texture_view)
                       ),
                  label='Texturing',
                  show_labels=False,
            ),
        )
