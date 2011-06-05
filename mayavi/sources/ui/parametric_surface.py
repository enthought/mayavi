"""
Traits View definition file.

The view trait of the parent class is extracted from the model definition
file.  This file can either be exec()ed or imported.  See
core/base.py:Base.trait_view() for what is currently used.  Using exec()
allows view changes without needing to restart Mayavi, but is slower than
importing.
"""
# Authors: Prabhu Ramachandran <prabhu_r@users.sf.net>
#          Vibha Srinivasan <vibha@enthought.com>
#          Judah De Paula <judah@enthought.com>
# Copyright (c) 2005-2008, Enthought, Inc.
# License: BSD Style.
from traitsui.api import Item, Group, View

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
