"""
Traits View definition file.

The view trait of the parent class is extracted from the model definition
file.  This file can either be exec()ed or imported.  See
core/base.py:Base.trait_view() for what is currently used.  Using exec()
allows view changes without needing to restart Mayavi, but is slower than
importing.
"""
# Authors: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
#          Judah De Paula <judah@enthought.com>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

from traitsui.api import (View, Group, Item, InstanceEditor,
                          DropEditor, Tabbed)
from tvtk.api import tvtk
from tvtk.common import vtk_major_version

VTK_VER = tvtk.Version().vtk_version

# The properties view group.
_prop_base_group = Group(Item(name='representation'),
                         Item(name='color'),
                         Item(name='line_width'),
                         Item(name='point_size'),
                         Item(name='opacity'))

_prop_group = Group(Item(name='property', style='custom', show_label=False,
                         editor=InstanceEditor(view=View(_prop_base_group))),
                    Item(name='property',
                         show_label=False,
                         editor=InstanceEditor(label='More options ...')),
                    show_border=True, label='Property')


# The mapper's view group.
if VTK_VER[:3] in ['4.2', '4.4']:
    _mapper_base_group = Group(Item(name='scalar_visibility'))
else:
    _mapper_base_group = Group(
        Item(name='scalar_visibility'),
        Item(name='interpolate_scalars_before_mapping'),
    )

_mapper_group = Group(
    Item(name='mapper', style='custom', show_label=False,
         editor=InstanceEditor(view=View(_mapper_base_group))),
    Item(name='mapper',
         show_label=False,
         editor=InstanceEditor(label='More options ...')),
    show_border=True, label='Mapper'
)

# The Texture's view group
if vtk_major_version > 7:
    _texture_group = Group(Item(name='interpolate'),
                           Item(name='color_mode'),
                           Item(name='repeat'),
                           show_border=True)
else:
    _texture_group = Group(Item(name='interpolate'),
                           Item(name='map_color_scalars_through_lookup_table'),
                           Item(name='repeat'),
                           show_border=True)

# The Actor's view group.
_actor_base_group = Group(Item(name='visibility'))
_actor_group = Group(Item(name='actor', style='custom', show_label=False,
                          editor=InstanceEditor(view=View(_actor_base_group))),
                     Item(name='actor',
                          show_label=False,
                          editor=InstanceEditor(label='More options ...')),
                     show_border=True, label='Actor')

actor_group = Group(
    _actor_group,
    _mapper_group,
    _prop_group,
    label='Actor',
    show_labels=False,
)

texture_group = Group(
    Item(name='enable_texture'),
    Group(Item(name='texture_source_object',
               editor=DropEditor()),
          Item(name='tcoord_generator_mode'),
          Tabbed(
              Item(name='texture',
                   style='custom',
                   show_label=False,
                   editor=InstanceEditor(view=View(_texture_group))),
              Item(name='tcoord_generator',
                   style='custom',
                   show_label=False,
                   resizable=True,
                   visible_when='texture_mode != "none"'),
          ),
          show_labels=True,
          label='Texture Properties',
          enabled_when='object.enable_texture',
          show_border=True),
    label='Texture'
)


# The Views for this object.  Pick the one that you need.
actor_view = View(actor_group, resizable=True)
texture_view = View(texture_group, resizable=True)
view = View(actor_group, texture_group, resizable=True)
