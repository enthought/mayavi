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

from traitsui.api import Item, Group, View, EnumEditor
from mayavi.core.module_manager import LUT_DATA_MODE_TYPES

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
