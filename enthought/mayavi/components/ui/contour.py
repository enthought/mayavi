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

from traitsui.api import Item, Group, View

view = View(Group(Item(name='filled_contours',
                       defined_when='show_filled_contours'),
                  Item(name='auto_contours'),

                  # One group or the other, but not both.
                  Group(
                       Item(name='contours',
                            style='custom',
                            visible_when='not auto_contours',
                            show_label=False),
                  ),
                  Group(
                      Item(name='number_of_contours'),
                      Item(name='minimum_contour'),
                      Item(name='maximum_contour'),
                      visible_when='auto_contours',
                  ),

                  Item(name='auto_update_range'),
                  Group(
                        Item(name='_data_min',
                             label='Data minimum'),
                        Item(name='_data_max',
                             label='Data maximum'),
                             visible_when='not auto_update_range',
                  )
               )
           )
