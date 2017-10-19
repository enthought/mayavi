"""This module allows the user to place text on the screen.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

from distutils.version import StrictVersion

# Enthought library imports.
from traits.api import Instance, Range, Str, Bool, Property, \
                                    Float
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk
from apptools.persistence import state_pickler

# Local imports
from mayavi.core.module import Module
from mayavi.core.pipeline_info import PipelineInfo

VTK_VER = StrictVersion(tvtk.Version().vtk_version)


######################################################################
# `Text` class.
######################################################################
class Text(Module):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The tvtk TextActor.
    actor = Instance(tvtk.TextActor, allow_none=False, record=True)

    # The property of the axes (color etc.).
    property = Property(record=True)

    # The text to be displayed.  Note that this should really be `Str`
    # but wxGTK only returns unicode.
    text = Str('Text', desc='the text to be displayed')

    # The x-position of this actor.
    x_position = Float(0.0, desc='the x-coordinate of the text')

    # The y-position of this actor.
    y_position = Float(0.0, desc='the y-coordinate of the text')

    # The z-position of this actor.
    z_position = Float(0.0, desc='the z-coordinate of the text')

    # Shadow the positions as ranges for 2D. Simply using a RangeEditor
    # does not work as it resets the 3D positions to 1 when the dialog is
    # loaded.
    _x_position_2d = Range(0., 1., 0., enter_set=True, auto_set=False,
                           desc='the x-coordinate of the text')
    _y_position_2d = Range(0., 1., 0., enter_set=True, auto_set=False,
                           desc='the y-coordinate of the text')

    # 3D position
    position_in_3d = Bool(False,
                    desc='whether the position of the object is given in 2D or in 3D')

    # The width of the text.
    width = Range(0.0, 1.0, 0.4, enter_set=True, auto_set=False,
                  desc='the width of the text as a fraction of the viewport')

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    ########################################
    # The view of this object.

    if VTK_VER > '5.1':
        _text_actor_group = Group(Item(name='visibility'),
                                  Item(name='text_scale_mode'),
                                  Item(name='alignment_point'),
                                  Item(name='minimum_size'),
                                  Item(name='maximum_line_height'),
                                  show_border=True,
                                  label='Text Actor')
    else:
        _text_actor_group = Group(Item(name='visibility'),
                                  Item(name='scaled_text'),
                                  Item(name='alignment_point'),
                                  Item(name='minimum_size'),
                                  Item(name='maximum_line_height'),
                                  show_border=True,
                                  label='Text Actor')

    _position_group_2d = Group(Item(name='_x_position_2d',
                                    label='X position'),
                               Item(name='_y_position_2d',
                                    label='Y position'),
                               visible_when='not position_in_3d')

    _position_group_3d = Group(Item(name='x_position', label='X',
                                            springy=True),
                               Item(name='y_position', label='Y',
                                            springy=True),
                               Item(name='z_position', label='Z',
                                            springy=True),
                               show_border=True,
                               label='Position',
                               orientation='horizontal',
                               visible_when='position_in_3d')

    view = View(Group(Group(Item(name='text'),
                            Item(name='position_in_3d'),
                            _position_group_2d,
                            _position_group_3d,
                            Item(name='width',
                                 enabled_when='object.actor.scaled_text'),
                            ),
                      Group(Item(name='actor', style='custom',
                                 editor=\
                                 InstanceEditor(view=View(_text_actor_group))
                                 ),
                            show_labels=False),
                      label='TextActor',
                      show_labels=False
                      ),
                Group(Item(name='_property', style='custom', resizable=True),
                      label='TextProperty',
                      show_labels=False),
                )

    ########################################
    # Private traits.
    _updating = Bool(False)
    _property = Instance(tvtk.TextProperty)

    ######################################################################
    # `object` interface
    ######################################################################
    def __set_pure_state__(self, state):
        self._updating = True
        state_pickler.set_state(self, state, first=['actor'],
                                ignore=['_updating'])
        self._updating = False

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.  You should also
        set the `actors` attribute up at this point.
        """
        actor = self.actor = tvtk.TextActor(input=str(self.text))
        if VTK_VER > '5.1':
            actor.trait_set(text_scale_mode='prop', width=0.4, height=1.0)
        else:
            actor.trait_set(scaled_text=True, width=0.4, height=1.0)

        c = actor.position_coordinate
        c.trait_set(coordinate_system='normalized_viewport',
              value=(self.x_position, self.y_position, 0.0))
        c = actor.position2_coordinate
        c.trait_set(coordinate_system='normalized_viewport')

        self._property.opacity = 1.0

        self._text_changed(self.text)
        self._width_changed(self.width)
        self._shadow_positions(True)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the component should do the rest.
        self.data_changed = True

    ######################################################################
    # Non-public interface
    ######################################################################
    def _text_changed(self, value):
        actor = self.actor
        if actor is None:
            return
        if self._updating:
            return
        actor.input = str(value)
        self.render()

    def _shadow_positions(self, value):
        self.sync_trait('x_position', self, '_x_position_2d',
                            remove=(not value))
        self.sync_trait('y_position', self, '_y_position_2d',
                            remove=(not value))
        if not value:
            self._x_position_2d = self.x_position
            self._y_position_2d = self.y_position

    def _position_in_3d_changed(self, value):
        if value:
            self.actor.position_coordinate.coordinate_system='world'
            self.actor.position2_coordinate.coordinate_system='world'
        else:
            self.actor.position2_coordinate.coordinate_system=\
                                            'normalized_viewport'
            self.actor.position_coordinate.coordinate_system=\
                                            'normalized_viewport'
            x = self.x_position
            y = self.y_position
            if x < 0:
                x = 0
            elif x > 1:
                x = 1
            if y < 0:
                y = 0
            elif y > 1:
                y = 1
            self.trait_set(x_position=x, y_position=y,
                                                    trait_change_notify=False)
        self._shadow_positions(not value)
        self._change_position()
        self.actor._width_changed(self.width, self.width)
        self.pipeline_changed = True

    def _change_position(self):
        """ Callback for _x_position, _y_position, and z_position.
        """
        actor = self.actor
        if actor is None:
            return
        if self._updating:
            return
        x = self.x_position
        y = self.y_position
        z = self.z_position
        if self.position_in_3d:
            actor.position_coordinate.value = x, y, z
        else:
            actor.position = x, y
        self.render()

    _x_position_changed = _change_position

    _y_position_changed = _change_position

    _z_position_changed = _change_position

    def _width_changed(self, value):
        actor = self.actor
        if actor is None:
            return
        if self._updating:
            return
        actor.width = value
        self.render()

    def _update_traits(self):
        self._updating = True
        try:
            actor = self.actor
            self.text = actor.input
            pos = actor.position
            self.x_position, self.y_position = pos
            self.width = actor.width
        finally:
            self._updating = False

    def _get_property(self):
        return self._property

    def _actor_changed(self, old, new):
        if old is not None:
            for obj in (old, self._property):
                obj.on_trait_change(self.render, remove=True)
            old.on_trait_change(self._update_traits, remove=True)

        self._property = new.text_property
        for obj in (new, self._property):
            obj.on_trait_change(self.render)
        new.on_trait_change(self._update_traits)

        self.actors = [new]
        self.render()

    def _foreground_changed_for_scene(self, old, new):
        # Change the default color for the actor.
        self.property.color = new
        self.render()

    def _scene_changed(self, old, new):
        super(Text, self)._scene_changed(old, new)
        self._foreground_changed_for_scene(None, new.foreground)
