#------------------------------------------------------------------------------
# Copyright (c) 2005-2020, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought mayavi package component>
#------------------------------------------------------------------------------
"""This module provides basic picking functionality.  Using this, one
can interactively select a point and/or a cell in the data.  One can
also can use a world point picker (i.e. a generic point in space) and
probe for the data at that point.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.

from traits.api import HasTraits, Trait, Int, Array, Any, Float, \
                                Instance, Range, true, Str, false
from traitsui.api import View, Group, Item, Handler
from tvtk.api import tvtk
from tvtk.tvtk_base import RevPrefixMap, false_bool_trait
from tvtk.pyface.tvtk_scene import TVTKScene
from tvtk.common import configure_input
from apptools.persistence import state_pickler
from tvtk.common import vtk_major_version
import numpy as np


######################################################################
# Utility functions.
######################################################################
def get_last_input(data):
    """Attempts to get the deepest possible data value in the
    pipeline.  Used when probing a selected point."""
    tmp = inp = data
    while tmp:
        try:
            tmp = inp.input
            if tmp:
                inp = tmp
        except AttributeError:
            tmp = None
    return inp


######################################################################
# `PickedData` class.
######################################################################
class PickedData(HasTraits):
    """This class stores the picked data."""

    # Was there a valid picked point?
    valid = Trait(false_bool_trait,
                  desc='specifies the validity of the pick event')
    # Id of picked point (-1 implies none was picked)
    point_id = Int(-1, desc='the picked point ID')
    # Id of picked cell (-1 implies none was picked)
    cell_id = Int(-1, desc='the picked cell ID')
    # World pick -- this has no ID.
    world_pick = Trait(false_bool_trait,
                       desc='specifies if the pick is a world pick.')
    # Coordinate of picked point.
    coordinate = Array('d', (3,), labels=['x', 'y', 'z'], cols=3,
                       desc='the coordinate of the picked point')

    text_actor = Instance(tvtk.TextActor)

    renwin = Instance(TVTKScene)

    # renwin = Any
    # The picked data -- usually a tvtk.PointData or tvtk.CellData of
    # the object picked.  The user can use this data and extract any
    # necessary values.
    data = Any


######################################################################
# `PickerHandler` class.
######################################################################
class PickHandler(HasTraits):
    """This is the handler for the picked data.  Subclass this to do
    what you need.  Each time a pick occurs the handle_pick is called
    by the `Picker` class."""

    def handle_pick(self, data):
        """Called when a pick event happens.

        Parameters
        ----------

        - data : `PickedData` instance.
        """
        pass


######################################################################
# `DefaultPickerHandler` class.
######################################################################
class DefaultPickHandler(PickHandler):
    """The default handler for the picked data."""
    # Traits.
    ID = Trait(None, None, Int, desc='the picked ID')

    coordinate = Trait(None, None, Array('d', (3,)),
                       desc='the coordinate of the picked point')

    scalar = Trait(None, None, Array, Float, desc='the scalar at picked point')

    vector = Trait(None, None, Array('d', (3,)),
                   desc='the vector at picked point')

    tensor = Trait(None, None, Array('d', (3, 3)),
                   desc='the tensor at picked point')

    # History of picked data.
    history = Str

    default_view = View(Item(name='ID', style='readonly'),
                        Item(name='coordinate', style='readonly'),
                        Item(name='scalar', style='readonly'),
                        Item(name='vector', style='readonly'),
                        Item(name='tensor', style='readonly'),
                        Item(name='history', style='custom'),
                        )

    def __init__(self, **traits):
        super(DefaultPickHandler, self).__init__(**traits)
        # This saves all the data picked earlier.
        self.data = {'ID': [], 'coordinate': [], 'scalar': [], 'vector': [],
                     'tensor': []}

    #################################################################
    # `DefaultPickHandler` interface.
    #################################################################
    def handle_pick(self, data):
        """Called when a pick event happens.
        """
        if data.valid_:
            if data.point_id > -1:
                self.ID = data.point_id
            elif data.cell_id > -1:
                self.ID = data.cell_id
            self.coordinate = list(data.coordinate)

            if data.data:
                array_data = {'scalar': data.data.scalars,
                              'vector': data.data.vectors,
                              'tensor': data.data.tensors}
            else:
                array_data = {'scalar': None,
                              'vector': None,
                              'tensor': None}
            for name in array_data.keys():
                if array_data[name]:
                    setattr(self, name, array_data[name][self.ID])
                else:
                    setattr(self, name, None)
        else:
            for name in ['ID', 'coordinate', 'scalar', 'vector', 'tensor']:
                setattr(self, name, None)

        self._update_data(data.renwin, data.text_actor)

    #################################################################
    # Non-public interface.
    #################################################################

    def _update_data(self, renwin, text_actor):
        for name in ['ID', 'coordinate', 'scalar', 'vector', 'tensor']:
            value = getattr(self, name)
            self.data.get(name).append(getattr(self, name))
            self.history += '%s: %r\n' % (name, value)

        x_coord = np.format_float_scientific(self.coordinate[0], precision=3)
        y_coord = np.format_float_scientific(self.coordinate[1], precision=3)
        z_coord = np.format_float_scientific(self.coordinate[2], precision=3)

        if(self.vector is not None and
           self.scalar is not None and
           self.tensor is not None):
            text_actor.trait_set(
                input=("ID : %s\nx : %s\ny : %s\nz : %s " +
                       "\nscalar : %s\nvector : %s\ntensor : %s ")
                % (self.ID, x_coord, y_coord, z_coord,
                   self.scalar, self.vector, self.tensor)
            )

        elif self.vector is not None and self.scalar is not None:
            scalar = np.format_float_scientific(self.scalar, precision=3)
            vector = np.zeros(3)
            for i in range(3):
                vector[i] = np.format_float_scientific(self.vector[i],
                                                       precision=3)

            text_actor.trait_set(
                input=("ID : %s\nx : %s\ny : %s\nz : %s" +
                       "\nscalar : %s\nvector : %s ")
                % (self.ID, x_coord, y_coord, z_coord, scalar, vector)
            )

        elif self.scalar is not None:
            scalar = np.format_float_scientific(self.scalar, precision=3)
            text_actor.trait_set(
                input="ID : %s\nx : %s\ny : %s\nz : %s\nscalar : %s"
                % (self.ID, x_coord, y_coord, z_coord, scalar)
            )

        else:
            text_actor.trait_set(
                input="ID : %s\nx : %s\ny : %s\nz : %s "
                % (self.ID, x_coord, y_coord, z_coord)
            )


######################################################################
# `Picker` class.
######################################################################
class Picker(HasTraits):
    """This module creates a 'Picker' that can interactively select a
    point and/or a cell in the data.  It also can use a world point
    picker (i.e. a generic point in space) and will probe for the data
    at that point.

    The Picker is usually called via a callback from the GUI
    interactor window.  After performing a pick on the VTK scene, a
    Picker object creates a `PickedData` object and passes it on to
    the pick_handler trait for further handling.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # Speficifies the pick type.  The 'point_picker' and 'cell_picker'
    # options are self-explanatory.  The 'world_picker' picks a point
    # using a WorldPointPicker and additionally uses a ProbeFilter to
    # probe the data at the picked point.
    pick_type = RevPrefixMap({'point_picker': 1,
                              'cell_picker': 2,
                              'world_picker': 3},
                             default_value='point_picker',
                             desc='specifies the picker type to use')

    # The pick_handler.  Set this to your own subclass if you want do
    # do something different from the default.
    pick_handler = Trait(DefaultPickHandler(), Instance(PickHandler))

    # Picking tolerance.
    tolerance = Range(0.0, 0.1, 0.025)

    # Raise the GUI on pick ?
    auto_raise = false(desc="whether to raise the picker GUI on pick")

    default_view = View(Group(Group(Item(name='pick_type'),
                                    Item(name='tolerance'), show_border=True),
                              Group(Item(name='pick_handler', style='custom'),
                                    show_border=True, show_labels=False),
                              ),
                        resizable=True,
                        buttons=['OK'])

    #################################################################
    # `object` interface.
    #################################################################
    def __init__(self, renwin, **traits):
        super(Picker, self).__init__(**traits)

        self.pointpicker = tvtk.PointPicker()
        self.cellpicker = tvtk.CellPicker()
        self.worldpicker = tvtk.WorldPointPicker()
        self.probe_data = tvtk.PolyData()
        # Use a set of axis to show the picked point.
        self.p_source = tvtk.Axes()
        self.p_mapper = tvtk.PolyDataMapper()
        self.p_actor = tvtk.Actor()
        self.p_source.symmetric = 1
        self.p_actor.pickable = 0
        self.p_actor.visibility = 0
        prop = self.p_actor.property
        prop.line_width = 2
        prop.ambient = 1.0
        prop.diffuse = 0.0
        configure_input(self.p_mapper, self.p_source)
        self.p_actor.mapper = self.p_mapper

        self.probe_data.points = [[0.0, 0.0, 0.0]]

        self.text_rep = tvtk.TextRepresentation()
        self.text_widget = tvtk.TextWidget()
        self.data = PickedData(renwin=renwin)
        self.data.text_actor = tvtk.TextActor()
        self.text_setup()
        self.widgets = False

    def __get_pure_state__(self):
        d = self.__dict__.copy()
        for x in ['renwin', 'ui', 'pick_handler', '__sync_trait__',
                  '__traits_listener__']:
            d.pop(x, None)
        return d

    def __getstate__(self):
        return state_pickler.dumps(self)

    def __setstate__(self, str_state):
        # This method is unnecessary since this object will almost
        # never be pickled by itself and only via the scene, therefore
        # __init__ will be called when the scene is constructed.
        # However, setstate is defined just for completeness.
        state_pickler.set_state(self, state_pickler.loads_state(str_state))

    #################################################################
    # `Picker` interface.
    #################################################################
    def pick(self, x, y):
        """Calls one of the current pickers and then passes the
        obtained data to the `self.pick_handler` object's
        `handle_pick` method.

        Parameters
        ----------

        - x : X position of the mouse in the window.

        - y : Y position of the mouse in the window.

        Note that the origin of x, y must be at the left bottom
        corner of the window.  Thus, for most GUI toolkits, y must
        be flipped appropriately such that y=0 is the bottom of the
        window.
        """
        if self.pick_type_ == 1:
            self.data = self.pick_point(x, y)
        elif self.pick_type_ == 2:
            self.data = self.pick_cell(x, y)
        elif self.pick_type_ == 3:
            self.data = self.pick_world(x, y)

        if self.widgets is False:
            self.setup_widgets()

        if self.data.valid:
            self.text_widget.enabled = 1
            self.pick_handler.handle_pick(self.data)
            self.data.text_actor._get_text_property().trait_set(
                justification="left"
            )
        else:
            self.close_picker()

        text_color = self.data.text_actor._get_text_property().color
        if not self.data.renwin.background == text_color:
            pass
        else:
            self.set_text_color()

    def pick_point(self, x, y):
        """ Picks the nearest point. Returns a `PickedData` instance."""
        self.pointpicker.pick((float(x), float(y), 0.0),
                              self.data.renwin.renderer)

        pp = self.pointpicker
        id = pp.point_id
        picked_data = PickedData(renwin=self.data.renwin,
                                 text_actor=self.data.text_actor)
        coord = pp.pick_position
        picked_data.coordinate = coord
        if id > -1:
            data = pp.mapper.input.point_data
            bounds = pp.mapper.input.bounds

            picked_data.valid = 1
            picked_data.point_id = id
            picked_data.data = data

            self._update_actor(coord, bounds)
        else:
            self.p_actor.visibility = 0

        self.data.renwin.render()

        return picked_data

    def pick_cell(self, x, y):
        """ Picks the nearest cell. Returns a `PickedData` instance."""
        try:
            self.cellpicker.pick(float(x), float(y), 0.0,
                                 self.data.renwin.renderer)
        except TypeError:
            # On old versions of VTK, the signature used to be different
            self.cellpicker.pick((float(x), float(y), 0.0),
                                 self.data.renwin.renderer)

        cp = self.cellpicker
        id = cp.cell_id
        picked_data = PickedData(renwin=self.data.renwin,
                                 text_actor=self.data.text_actor)
        coord = cp.pick_position
        picked_data.coordinate = coord

        if id > -1:
            data = cp.mapper.input.cell_data
            bounds = cp.mapper.input.bounds

            picked_data.valid = 1
            picked_data.cell_id = id
            picked_data.data = data

            self._update_actor(coord, bounds)
        else:
            self.p_actor.visibility = 0

        self.data.renwin.render()
        return picked_data

    def pick_world(self, x, y):
        """ Picks a world point and probes for data there. Returns a
        `PickedData` instance."""
        self.worldpicker.pick((float(x), float(y), 0.0),
                              self.data.renwin.renderer)

        # Use the cell picker to get the data that needs to be probed.
        try:
            self.cellpicker.pick((float(x), float(y), 0.0),
                                 self.data.renwin.renderer)
        except TypeError:
            self.cellpicker.pick(float(x), float(y), 0.0,
                                 self.data.renwin.renderer)

        wp = self.worldpicker
        cp = self.cellpicker
        coord = wp.pick_position
        self.probe_data.points = [list(coord)]
        picked_data = PickedData(renwin=self.data.renwin,
                                 text_actor=self.data.text_actor)
        picked_data.coordinate = coord

        if cp.mapper:
            data = get_last_input(cp.mapper.input)
            # Need to create the probe each time because otherwise it
            # does not seem to work properly.
            probe = tvtk.ProbeFilter()
            if vtk_major_version >= 6:
                probe.set_source_data(data)
                probe.set_input_data(self.probe_data)
            else:
                probe.source = data
                probe.input = self.probe_data
            probe.update()
            data = probe.output.point_data
            bounds = cp.mapper.input.bounds

            picked_data.valid = 1
            picked_data.world_pick = 1
            picked_data.point_id = 0
            picked_data.data = data

            self._update_actor(coord, bounds)
        else:
            self.p_actor.visibility = 0

        self.data.renwin.render()
        return picked_data

    def close_picker(self):
        """This method makes the picker actor invisible when a non
        data point is selected"""
        self.p_actor.visibility = 0
        self.data.renwin.renderer.remove_actor(self.p_actor)
        self.data.text_actor.visibility = 0
        self.data.renwin.renderer.remove_actor(self.data.text_actor)
        self.text_widget.enabled = 0
        self.widgets = False

    #################################################################
    # Non-public interface.
    #################################################################
    def text_setup(self):
        """Sets the properties of the text widget"""
        self.data.text_actor._get_text_property().font_size = 100
        self.text_rep._get_position_coordinate().trait_set(value=(.15, .15, 0))
        self.text_rep._get_position2_coordinate().trait_set(value=(.3, .2, 0))
        self.text_widget.trait_set(representation=self.text_rep)
        self.text_widget.trait_set(text_actor=self.data.text_actor)
        self.text_widget.selectable = 0

    def _update_actor(self, coordinate, bounds):
        """Updates the actor by setting its position and scale."""
        dx = 0.3*(bounds[1]-bounds[0])
        dy = 0.3*(bounds[3]-bounds[2])
        dz = 0.3*(bounds[5]-bounds[4])
        scale = max(dx, dy, dz)
        self.p_source.origin = coordinate
        self.p_source.scale_factor = scale
        self.p_actor.visibility = 1
        self.data.text_actor.visibility = 1

    def setup_widgets(self):
        """Sets up the picker actor and text actor"""

        self.text_widget.trait_set(interactor=self.data.renwin.interactor)
        self.data.renwin.renderer.add_actor(self.p_actor)
        self.data.renwin.renderer.add_actor(self.data.text_actor)
        self.p_actor.visibility = 1
        self.data.text_actor.visibility = 1
        self.widgets = True

    def set_picker_props(self, pick_type, tolerance, text_color):
        """Lets you set the picker properties"""
        self.pick_type = pick_type
        self.tolerance = tolerance
        self.set_text_color(text_color)

    def set_text_color(self, color=None):
        if color is None:
            bgcolor = self.data.renwin.background
            text_color = [0, 0, 0]
            for i in range(3):
                text_color[i] = abs(bgcolor[i]-1)
            self.data.text_actor._get_text_property().color = tuple(text_color)
        else:
            self.data.text_actor._get_text_property().color = color
