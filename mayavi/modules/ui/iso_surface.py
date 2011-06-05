"""
Traits View definition file.

The view trait of the parent class has been extracted from the model
definition file.  This file can either be exec()ed or imported.  See
core/base.py:Base.trait_view() for what is currently used.  Using exec()
allows view changes without needing to restart Mayavi, but is slower than
importing.
"""
# Authors: Prabhu Ramachandran <prabhu_r@users.sf.net>
#          Judah De Paula <judah@enthought.com>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.

from traitsui.api import Item, Group, View, InstanceEditor
from mayavi.components.ui.actor import actor_view, texture_view

view = View(Group(
                Group(
                     Item( name  = 'contour',
                           style = 'custom' ),
                     show_labels = False,
                     show_border = True,
                     label       = 'Contours' ),
                 Group(
                     Item( name = 'compute_normals' ),
                     Item( name         = 'normals',
                           style        = 'custom',
                           show_label   = False,
                           enabled_when = 'compute_normals' ),
                     show_border = True,
                     label       = 'Normals' ),
                 label='Contours',
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
            resizable=True
            )

