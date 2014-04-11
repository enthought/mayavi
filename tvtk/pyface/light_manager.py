#------------------------------------------------------------------------------
# Copyright (c) 2005, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------
"""This module provides a light manager that may be used to change the
lighting of a VTK scene.

This module is largely ported from MayaVi's Lights.py but the
implementation is considerably different.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

from math import sin, cos, atan2, pi, sqrt

from traits.api import HasTraits, Range, false, \
                                 Instance, Trait, List
from traitsui.api import View, Group, Handler, ListEditor, Item
from tvtk.api import tvtk
from tvtk.tvtk_base import vtk_color_trait, TraitRevPrefixMap
from tvtk.common import is_old_pipeline, configure_input, configure_input_data
from apptools.persistence import state_pickler

######################################################################
# `LightGlyph` class.
######################################################################
class LightGlyph(HasTraits):
    """Manages a glyph that represents a Light source in the scene.
    This gives the user an *idea* of where the light source is placed
    while configuring the lights.
    """
    # The version of this class.  Used for persistence.
    __version__ = 0

    def __init__(self):
        self.el = 0.0
        self.az = 0.0

        # Create an arrow.
        arrow = tvtk.ArrowSource()

        # Transform it suitably so it is oriented correctly.
        t = tvtk.Transform()
        tf = tvtk.TransformFilter()
        tf.transform = t
        t.rotate_y(90.0)
        t.translate((-2, 0, 0))
        configure_input_data(tf, arrow.output)

        mapper = tvtk.PolyDataMapper()
        configure_input(mapper, tf)

        self.actor = actor = tvtk.Follower()
        actor.mapper = mapper
        prop = actor.property
        prop.color = 0, 1, 1
        prop.ambient = 0.5
        prop.diffuse = 0.5

    def __get_pure_state__(self):
        d = self.__dict__.copy()
        for name in ['__sync_trait__',  '__traits_listener__']:
            d.pop(name, None)
        return d

    def __getstate__(self):
        return state_pickler.dumps(self)

    def __setstate__(self, str_state):
        self.__init__()
        state_pickler.set_state(self, state_pickler.loads_state(str_state))

    #################################################################
    # `LightGlyph` interface.
    #################################################################
    def add(self, ren, bounds):
        """Adds the actors to the given renderer (`ren`).  The actors
        are scaled as per the given bounds."""
        scale = max(bounds[1]-bounds[0], bounds[3] - bounds[2],
                    bounds[5]-bounds[4])*0.75
        self.actor.scale = scale, scale, scale
        ren.add_actor(self.actor)
        cam = ren.active_camera
        self.actor.camera = cam

    def remove(self, ren):
        """Removes the actors of the glyph from the given renderer
        (`ren`)."""
        ren.remove_actor(self.actor)

    def move_to(self, elevation=None, azimuth = None):
        """Move the glyphs to the specified elevation and azimuth."""
        self.actor.rotate_x(-self.el)
        self.actor.rotate_y(-self.az)
        if elevation != None:
            self.el = elevation
        if azimuth != None:
            self.az = azimuth
        self.actor.rotate_y(self.az)
        self.actor.rotate_x(self.el)

    def show(self):
        """Show the glyphs on screen."""
        self.actor.visibility = 1

    def hide(self):
        """Hide the glyphs on screen."""
        self.actor.visibility = 0

    def set_color(self, clr):
        """Change the glyphs color."""
        self.actor.property.color = clr



######################################################################
# `CameraLight` class.
######################################################################
class CameraLight(HasTraits):

    """This class manages a tvtk.Light object and a LightGlyph object."""

    # The version of this class.  Used for persistence.
    __version__ = 0

    #################################################################
    # Traits.
    #################################################################
    elevation = Range(-90.0, 90.0, 0.0,
                      desc="the elevation of the light")
    azimuth = Range(-180.0, 180.0, 0.0,
                    desc="the aziumthal angle of the light")
    activate = Trait(False, false,
                     desc="specifies if the light is enabled or not")
    source = Instance(tvtk.Light, ())

    # FIXME: Traits Delegation does not work correctly and changes to
    # this object are not reflected in the delegate nicely.
    #color = Delegate('source', modify=True)
    #intensity = Delegate('source', modify=True)

    # For now we mirror these traits from the source.
    intensity = Range(0.0, 1.0, 1.0,
                      desc="the intensity of the light")
    color = vtk_color_trait((1.0, 1.0, 1.0))
    color.desc = "the color of the light"

    default_view = View(Item(name='activate'), Item(name='elevation'),
                        Item(name='azimuth'), Item(name='intensity'),
                        Item(name='color'))

    #################################################################
    # `object` interface.
    #################################################################
    def __init__(self, renwin, **traits):
        self.glyph = LightGlyph()
        super(CameraLight, self).__init__(**traits)
        self.source.light_type = 'camera_light'
        self._intensity_changed(self.intensity)
        self._activate_changed(self.activate)
        self._color_changed(self.color)

        renwin.renderer.add_light(self.source)
        self.on_trait_change(renwin.render)

    def __get_pure_state__(self):
        d = self.__dict__.copy()
        for name in ['__sync_trait__', '__traits_listener__']:
            d.pop(name, None)
        return d

    def __getstate__(self):
        return state_pickler.dumps(self)

    def __setstate__(self, str_state):
        #self.__init__()
        state_pickler.set_state(self, state_pickler.loads_state(str_state))

    #################################################################
    # `LightGlyph` interface.
    #################################################################
    def close(self, renwin):
        """Remove the light source and the glyph from the
        renderwindow.  This is usually to be called when the Light is
        removed from the scene."""
        ren = renwin.renderer
        self.on_trait_change(renwin.render, remove=True)
        ren.remove_light(self.source)
        self.remove_glyph(ren)

    def add_glyph(self, ren, bounds):
        """Add the light glyph to the passed renderer ('ren').  Scale
        the actors using the bounds (`bounds`) provided."""
        self.glyph.add(ren, bounds)

    def remove_glyph(self, ren):
        """Remove the light glyph from the passed renderer."""
        self.glyph.remove(ren)

    def move_to(self, elevation, azimuth):
        """Move the light to the specified elevation and azimuthal
        angles (in degrees)."""
        self.elevation = elevation
        self.azimuth = azimuth

    #################################################################
    # Trait handlers.
    #################################################################
    def _activate_changed(self, val):
        if val:
            self.source.switch = 1
            self.glyph.show()
        else:
            self.source.switch = 0
            self.glyph.hide()

    def _intensity_changed(self, val):
        self.source.intensity = val

    def _color_changed(self, val):
        if is_old_pipeline():
            self.source.color = val
        else:
            self.source.set_color(val)
        self.glyph.set_color(val)

    def _elevation_changed(self, val):
        self.glyph.move_to(val, self.azimuth)
        self.source.position = self._to_pos(val, self.azimuth)

    def _azimuth_changed(self, val):
        self.glyph.move_to(self.elevation, val)
        self.source.position = self._to_pos(self.elevation, val)

    #################################################################
    # Non-public interface.
    #################################################################
    def _to_pos(self, elevation, azimuth):
        """Convert the given elevation and azimuth angles (degrees) to
        a position vector."""
        theta = azimuth*pi/180.0
        phi = (90.0-elevation)*pi/180.0
        x = sin(theta)*sin(phi)
        y = cos(phi)
        z = cos(theta)*sin(phi)
        return x, y, z

    def _from_pos(self, x, y, z):
        """Given the position vector, return an elevation and azimuth
        angle (in degrees)."""
        theta = atan2(x, z)
        phi = atan2(sqrt(x**2+z**2), y)
        az = theta*180.0/pi
        el = 90.0 - phi*180.0/pi
        return el, az



######################################################################
# `CloseHandler` class.
######################################################################
class CloseHandler(Handler):
    """This class cleans up after the UI for the Light Manager is
    closed."""
    def close(self, info, is_ok):
        """This method is invoked when the user closes the UI."""
        light_manager = info.object
        light_manager.on_ui_close()
        return True


######################################################################
# `LightManager` class.
######################################################################
class LightManager(HasTraits):

    """This class manages all the lights and presents a GUI for the
    lights.

    There are two default lighting modes possible (specified via the
    `light_mode` trait).  The 'vtk' mode uses the default lighting
    mode which is basically a single headlight.  The 'raymond' mode
    creates three lights to give better overall illumination (thanks
    to Raymond Maple).
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    #################################################################
    # Traits.
    #################################################################

    # Valid modes currently are 'vtk' and 'raymond'.  'vtk' is the
    # default VTK light setup with only one light on in headlight
    # mode. 'raymond' is Raymond Maple's default configuration with
    # three active lights.  Please note that this only specifies a
    # default mode used to initialize the lights to a sane default.
    # The user can always change the light configuration via the GUI
    # such that the mode is neither 'vtk' nor 'raymond'.
    light_mode = Trait('raymond', TraitRevPrefixMap({'raymond':1,
                                                     'vtk':2}),
                       desc='specifies a default lighting mode')

    # Specify the number of lights.  If new lights are added they are
    # by default turned off.  Similarly if the number of lights are
    # reduced the last lights alone are removed.
    number_of_lights = Range(3, 8, 4, desc='specifies the number of lights')

    # The list of added lights.
    lights = List(CameraLight, editor=ListEditor(use_notebook=True,
                                                 page_name='Light'),
                  record=True)

    view = View( Group( 'light_mode',
                        'number_of_lights', ),
                Item('lights', style='custom', show_label=False),
                resizable=True,
                buttons=['OK'])


    #################################################################
    # `object` interface.
    #################################################################
    def __init__(self, renwin, **traits):
        super(LightManager, self).__init__(**traits)

        self.ui = None
        self.renwin = renwin
        ren = self.renwin.renderer

        # VTK requires that there always be atleast one light turned
        # on (with SwitchOn).  The renderer already has one headlight
        # already enabled.  We merely set the intensity of this light
        # to zero and never change that.  Note that if this light is
        # turned off, and no other lights are "on", then VTK will
        # create a new light!
        ren.lights[0].intensity = 0.0

        # Create the lights.
        self.lights = []
        for i in range(self.number_of_lights):
            light = CameraLight(self.renwin)
            self.lights.append(light)

        # Setup the light mode.
        self._light_mode_changed(self.light_mode)

    def __get_pure_state__(self):
        d = self.__dict__.copy()
        for name in ['__sync_trait__', 'renwin', 'ui',
                     '__traits_listener__']:
            d.pop(name, None)
        return d

    def __set_pure_state__(self, state):
        first = ['light_mode', 'number_of_lights']
        state_pickler.set_state(self, state, first=first, last=['lights'])

    def __getstate__(self):
        return state_pickler.dumps(self)

    def __setstate__(self, str_state):
        # This method is unnecessary since this object will almost
        # never be pickled by itself and only via the scene, therefore
        # __init__ will be called when the scene is constructed.
        # However, setstate is defined just for completeness.
        #self.__init__()
        state = state_pickler.loads_state(str_state)
        state_pickler.update_state(state)
        self.__set_pure_state__(state)

    #################################################################
    # `LightManager` interface.
    #################################################################
    def configure(self):
        """Pops up the GUI control widget."""
        if self.ui is None:
            self._show_glyphs()
            view = View(Group(Item(name='light_mode'),
                              Item(name='number_of_lights'),
                              label='LightManager'),
                        Group(Item(name='lights', style='custom'),
                              label='Lights',
                              selected=True, show_labels=False),
                        resizable=True,
                        buttons=['OK'],
                        handler=CloseHandler())
            self.ui = view.ui(self)
        else:
            try:
                self.ui.control.Raise()
            except AttributeError:
                pass

    def on_ui_close(self):
        """This method removes the glyphs used to show the lights on
        screen when the GUI dialog is closed.  This is typically only
        called from the CloseHandler."""
        ren = self.renwin.renderer
        for l in self.lights:
            l.remove_glyph(ren)
        self.ui = None

    #################################################################
    # Non-public interface.
    #################################################################
    def _show_glyphs(self):
        """Shows the glyphs when the light config UI is shown."""
        rw = self.renwin
        ren = rw.renderer
        rw.reset_zoom()
        bounds = ren.compute_visible_prop_bounds()
        for light in self.lights:
            light.add_glyph(ren, bounds)
        rw.render()

    def _light_mode_changed(self, mode):
        lights = self.lights
        if mode == 'raymond':
            for i in range(len(lights)):
                if i < 3:
                    lights[i].activate = True
                    lights[i].intensity = 1.0
                    lights[i].color = 1.0, 1.0, 1.0
                else:
                    lights[i].activate = False
                    lights[i].move_to(0.0, 0.0)
                    lights[i].intensity = 1.0
                    lights[i].color = 1.0, 1.0, 1.0

            lights[0].move_to(45.0, 45.0)
            lights[1].move_to(-30.0,-60.0)
            lights[1].intensity = 0.6
            lights[2].move_to(-30.0, 60.0)
            lights[2].intensity = 0.5
        else:
            for i in range(len(lights)):
                lights[i].move_to(0.0, 0.0)
                lights[i].intensity = 1.0
                lights[i].color = 1.0, 1.0, 1.0
                if i == 0 :
                    lights[i].activate  = True
                else:
                    lights[i].activate = False

    def _number_of_lights_changed(self, old, new):
        ren = self.renwin.renderer
        changed = False
        if new == old:
            return
        elif new > old:
            for i in range(new - old):
                light = CameraLight(self.renwin)
                self.lights.append(light)
            changed = True
        elif new < old:
            for i in range(old - new):
                light = self.lights.pop()
                light.close(self.renwin)
            changed = True

