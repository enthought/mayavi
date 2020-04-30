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
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------
"""A VTK interactor scene widget for the PyFace wxPython backend.  See
the class docs for more details.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.


import sys
import os
import tempfile
import wx

from tvtk.api import tvtk
from tvtk import messenger
from traits.api import Instance, Button, Any, Bool
from traitsui.api import View, Group, Item, InstanceEditor

from pyface.api import Widget, GUI
from tvtk.pyface import picker
from tvtk.pyface import light_manager
from tvtk.pyface.utils import popup_save
from tvtk.pyface.tvtk_scene import TVTKScene

from .wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor


######################################################################
# `FullScreen` class.
######################################################################
class FullScreen(object):
    """Creates a full screen interactor widget.  This will use VTK's
    event loop until the user presses 'q'/'e' on the full screen
    window.  This does not yet support interacting with any widgets on
    the renderered scene.

    This class is really meant to be used for VTK versions earlier
    than 5.1 where there was a bug with reparenting a window.

    """
    def __init__(self, scene):
        self.scene = scene
        self.old_rw = scene.render_window
        self.ren = scene.renderer

    def run(self):
        # Remove the renderer from the current render window.
        self.old_rw.remove_renderer(self.ren)

        # Creates renderwindow tha should be used ONLY for
        # visualization in full screen
        full_rw = tvtk.RenderWindow(stereo_capable_window=True,
                                    full_screen=True
                                    )
        # add the current visualization
        full_rw.add_renderer(self.ren)

        # Under OS X there is no support for creating a full screen
        # window so we set the size of the window here.
        if sys.platform  == 'darwin':
            full_rw.size = tuple(wx.GetDisplaySize())

        # provides a simple interactor
        style = tvtk.InteractorStyleTrackballCamera()
        self.iren = tvtk.RenderWindowInteractor(render_window=full_rw,
                                                interactor_style=style)

        # Gets parameters for stereo visualization
        if self.old_rw.stereo_render:
            full_rw.trait_set(stereo_type=self.old_rw.stereo_type, stereo_render=True)

        # Starts the interactor
        self.iren.initialize()
        self.iren.render()
        self.iren.start()

        # Once the full screen window is quit this releases the
        # renderer before it is destroyed, and return it to the main
        # renderwindow.
        full_rw.remove_renderer(self.ren)
        self.old_rw.add_renderer(self.ren)
        self.old_rw.render()
        self.iren.disable()


######################################################################
# `PopupScene` class.
######################################################################
class PopupScene(object):
    """Pops up a Scene instance with an independent `wx.Frame` in
    order to produce either a standalone window or usually a full
    screen view with *complete* interactivity (including widget
    interaction).
    """
    def __init__(self, scene):
        self.orig_parent = None
        self.orig_size = None
        self.orig_pos = None
        self.frame = None
        self.scene = scene
        self.vtk_control = self.scene._vtk_control

    def _setup_frame(self):
        vtk_control = self.vtk_control
        self.orig_parent = vtk_control.GetParent()
        self.orig_size = vtk_control.GetSize()
        self.orig_pos = vtk_control.GetPosition()
        f = self.frame = wx.Frame(None, -1)
        return f

    def reparent_vtk(self, widget):
        """Reparent VTK control to another widget.
        """
        scene = self.scene
        vc = self.vtk_control
        # We want to disable any rendering at this time so we override
        # the original render with a dummy after saving it.
        orig_disable_render = scene.disable_render
        scene.disable_render = True
        orig_render = vc.Render
        vc.Render = lambda : None
        rw = vc.GetRenderWindow()
        if sys.platform != 'darwin' and wx.Platform != '__WXMSW__':
            rw.SetNextWindowInfo(str(widget.GetHandle()))
            rw.WindowRemap()
        vc.Reparent(widget)
        wx.GetApp().Yield(True)
        # Restore the original render.
        vc.Render = orig_render
        vc.Render()
        scene.disable_render = orig_disable_render

    def popup(self, size=None):
        """Create a popup window of scene and set its default size.
        """
        vc = self.vtk_control
        f = self._setup_frame()
        if size is None:
            f.SetSize(vc.GetSize())
        else:
            f.SetSize(size)
        f.Show(True)
        self.reparent_vtk(f)

    def fullscreen(self):
        """Create a popup window of scene.
        """
        f = self._setup_frame()
        f.Show(True)
        self.reparent_vtk(f)
        f.ShowFullScreen(True)

    def close(self):
        """Close the window and reparent the TVTK scene.
        """
        f = self.frame
        if f is None:
            return

        vc = self.vtk_control
        self.reparent_vtk(self.orig_parent)
        vc.SetSize(self.orig_size)
        vc.SetPosition(self.orig_pos)
        f.ShowFullScreen(False)
        f.Show(False)
        f.Close()
        self.frame = None


######################################################################
# `Scene` class.
######################################################################
class Scene(TVTKScene, Widget):
    """A VTK interactor scene widget for pyface and wxPython.

    This widget uses a RenderWindowInteractor and therefore supports
    interaction with VTK widgets.  The widget uses TVTK.  In addition
    to the features that the base TVTKScene provides this widget
    supports:

    - saving the rendered scene to the clipboard.

    - picking data on screen.  Press 'p' or 'P' when the mouse is over
      a point that you need to pick.

    - The widget also uses a light manager to manage the lighting of
      the scene.  Press 'l' or 'L' to activate a GUI configuration
      dialog for the lights.

    - Pressing the left, right, up and down arrow let you rotate the
      camera in those directions.  When shift-arrow is pressed then
      the camera is panned.  Pressing the '+' (or '=')  and '-' keys
      let you zoom in and out.

    - Pressing the 'f' key will set the camera focal point to the
      current point.

    - full screen rendering via the full_screen button on the UI.

    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    ###########################################################################
    # Traits.
    ###########################################################################

    # Turn on full-screen rendering.
    full_screen = Button('Full Screen')

    # The picker handles pick events.
    picker = Instance(picker.Picker)

    ########################################

    # Render_window's view.
    _stereo_view = Group(Item(name='stereo_render'),
                         Item(name='stereo_type'),
                         show_border=True,
                         label='Stereo rendering',
                         )

    # The default view of this object.
    default_view = View(Group(
                            Group(Item(name='background'),
                                  Item(name='foreground'),
                                  Item(name='parallel_projection'),
                                  Item(name='disable_render'),
                                  Item(name='off_screen_rendering'),
                                  Item(name='jpeg_quality'),
                                  Item(name='jpeg_progressive'),
                                  Item(name='magnification'),
                                  Item(name='anti_aliasing_frames'),
                                  Item(name='full_screen',
                                       show_label=False),
                                  ),
                            Group(Item(name='render_window',
                                       style='custom',
                                       visible_when='object.stereo',
                                       editor=InstanceEditor(view=View(_stereo_view)),
                                       show_label=False),
                                  ),
                            label='Scene'),
                         Group( Item(name='picker',
                                style='custom', show_label=False),
                                label='Picker'),
                         Group( Item(name='light_manager',
                                style='custom', show_label=False),
                                label='Lights'),
                         Group(
                             Item(
                                 name='movie_maker',
                                 style='custom', show_label=False
                             ),
                             label='Movie'),
                         buttons=['OK', 'Cancel']
                        )

    ########################################
    # Private traits.

    _vtk_control = Instance(wxVTKRenderWindowInteractor)
    _fullscreen = Any
    _interacting = Bool

    ###########################################################################
    # 'object' interface.
    ###########################################################################
    def __init__(self, parent=None, **traits):
        """ Initializes the object. """

        # Base class constructor.
        super(Scene, self).__init__(parent, **traits)

        # Setup the default picker.
        self.picker = picker.Picker(self)


    def __get_pure_state__(self):
        """Allows us to pickle the scene."""
        # The control attribute is not picklable since it is a VTK
        # object so we remove it.
        d = super(Scene, self).__get_pure_state__()
        for x in ['_vtk_control', '_fullscreen', '_interacting']:
            d.pop(x, None)
        return d

    ###########################################################################
    # 'Scene' interface.
    ###########################################################################
    def render(self):
        """ Force the scene to be rendered. Nothing is done if the
        `disable_render` trait is set to True."""
        if not self.disable_render:
            self._vtk_control.Render()

    def get_size(self):
        """Return size of the render window."""
        return self._vtk_control.GetSize()

    def set_size(self, size):
        """Set the size of the window."""
        self._vtk_control.SetSize(size)

    def hide_cursor(self):
        """Hide the cursor."""
        self._vtk_control.HideCursor()

    def show_cursor(self):
        """Show the cursor."""
        self._vtk_control.ShowCursor()

    ###########################################################################
    # 'TVTKScene' interface.
    ###########################################################################
    def save_to_clipboard(self):
        """Saves a bitmap of the scene to the clipboard."""
        handler, name = tempfile.mkstemp()
        self.save_bmp(name)
        bmp = wx.Bitmap(name, wx.BITMAP_TYPE_BMP)
        bmpdo = wx.BitmapDataObject(bmp)
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(bmpdo)
        wx.TheClipboard.Close()
        os.close(handler)
        os.unlink(name)

    ###########################################################################
    # `wxVTKRenderWindowInteractor` interface.
    ###########################################################################
    def OnKeyDown(self, event):
        """This method is overridden to prevent the 's'/'w'/'e'/'q'
        keys from doing the default thing which is generally useless.
        It also handles the 'p' and 'l' keys so the picker and light
        manager are called.
        """
        keycode = event.GetKeyCode()
        modifiers = event.HasModifiers()
        camera = self.camera
        if keycode < 256:
            key = chr(keycode)
            if key == '-':
                camera.zoom(0.8)
                self.render()
                self._record_methods('camera.zoom(0.8)\nrender()')
                return
            if key in ['=', '+']:
                camera.zoom(1.25)
                self.render()
                self._record_methods('camera.zoom(1.25)\nrender()')
                return
            if key.lower() in ['q', 'e'] or keycode == wx.WXK_ESCAPE:
                self._disable_fullscreen()
            if key.lower() in ['w']:
                event.Skip()
                return
            if key.lower() in ['r']:
                self._record_methods('reset_zoom()')
            # Handle picking.
            if key.lower() in ['p']:
                # In wxPython-2.6, there appears to be a bug in
                # EVT_CHAR so that event.GetX() and event.GetY() are
                # not correct.  Therefore the picker is called on
                # KeyUp.
                event.Skip()
                return
            # Camera focal point.
            if key.lower() in ['f']:
                event.Skip()
                return
            # Light configuration.
            if key.lower() in ['l'] and not modifiers:
                self.light_manager.configure()
                return
            if key.lower() in ['s'] and not modifiers:
                parent = self._vtk_control.GetParent()
                fname = popup_save(parent)
                if len(fname) != 0:
                    self.save(fname)
                return

        shift = event.ShiftDown()
        if keycode == wx.WXK_LEFT:
            if shift:
                camera.yaw(-5)
                self._record_methods('camera.yaw(-5)')
            else:
                camera.azimuth(5)
                self._record_methods('camera.azimuth(5)')
            self.render()
            self._record_methods('render()')
            return
        elif keycode == wx.WXK_RIGHT:
            if shift:
                camera.yaw(5)
                self._record_methods('camera.yaw(5)')
            else:
                camera.azimuth(-5)
                self._record_methods('camera.azimuth(-5)')
            self.render()
            self._record_methods('render()')
            return
        elif keycode == wx.WXK_UP:
            if shift:
                camera.pitch(-5)
                self._record_methods('camera.pitch(-5)')
            else:
                camera.elevation(-5)
                self._record_methods('camera.elevation(-5)')
            camera.orthogonalize_view_up()
            self.render()
            self._record_methods('camera.orthogonalize_view_up()\nrender()')
            return
        elif keycode == wx.WXK_DOWN:
            if shift:
                camera.pitch(5)
                self._record_methods('camera.pitch(5)')
            else:
                camera.elevation(5)
                self._record_methods('camera.elevation(5)')
            camera.orthogonalize_view_up()
            self.render()
            self._record_methods('camera.orthogonalize_view_up()\nrender()')
            return

        self._vtk_control.OnKeyDown(event)

        # Skipping the event is not ideal but necessary because we
        # have no way of knowing of the event was really handled or
        # not and not skipping will break any keyboard accelerators.
        # In practice this does not seem to pose serious problems.
        event.Skip()

    def OnKeyUp(self, event):
        """This method is overridden to prevent the 's'/'w'/'e'/'q'
        keys from doing the default thing which is generally useless.
        It also handles the 'p' and 'l' keys so the picker and light
        manager are called.  The 'f' key sets the camera focus.
        """
        keycode = event.GetKeyCode()
        modifiers = event.HasModifiers()
        if keycode < 256:
            key = chr(keycode)
            if key.lower() in ['s', 'w', 'e', 'q']:
                event.Skip()
                return
            # Set camera focal point.
            if key.lower() in ['f']:
                if not modifiers:
                    if sys.platform == 'darwin':
                        x, y = self._interactor.event_position
                    else:
                        x = event.GetX()
                        y = self._vtk_control.GetSize()[1] - event.GetY()
                    data = self.picker.pick_world(x, y)
                    coord = data.coordinate
                    if coord is not None:
                        self.camera.focal_point = coord
                        self.render()
                        self._record_methods('camera.focal_point = %r\n'\
                                             'render()'%list(coord))
                        return
            # Handle picking.
            if key.lower() in ['p']:
                if not modifiers:
                    if sys.platform == 'darwin':
                        x, y = self._interactor.event_position
                    else:
                        x = event.GetX()
                        y = self._vtk_control.GetSize()[1] - event.GetY()
                    self.picker.pick(x, y)
                    return
                else:
                    # This is here to disable VTK's own pick handler
                    # which can get called when you press Alt/Ctrl +
                    # 'p'.
                    event.Skip()
                    return
            # Light configuration.
            if key.lower() in ['l']:
                event.Skip()
                return

        self._vtk_control.OnKeyUp(event)
        event.Skip()

    def OnPaint(self, event):
        """This method is overridden temporarily in order to create
        the light manager.  This is necessary because it makes sense
        to create the light manager only when the widget is realized.
        Only when the widget is realized is the VTK render window
        created and only then are the default lights all setup
        correctly.  This handler is removed on the first Paint event
        and the default paint handler of the
        wxVTKRenderWindowInteractor is used instead."""

        if self._vtk_control is None:
            return

        # Call the original handler (this will Show the widget)
        self._vtk_control.OnPaint(event)
        if len(self.renderer.lights) == 0:
            # The renderer is not ready yet, we do not do anything, and
            # we do not remove this callback, so that it will be called
            # later.
            return
        # Now create the light manager.
        self.light_manager = light_manager.LightManager(self)

        renwin = self._renwin
        renwin.update_traits()

        vtk_rw = tvtk.to_vtk(renwin)
        renwin.add_observer('StartEvent', messenger.send)
        messenger.connect(vtk_rw, 'StartEvent', self._start_event_callback)
        renwin.add_observer('EndEvent', messenger.send)
        messenger.connect(vtk_rw, 'EndEvent', self._end_event_callback)

        # Reset the event handler to the default since our job is done.
        self._vtk_control.Bind(wx.EVT_PAINT, None) # Remove the default handler.
        self._vtk_control.Bind(wx.EVT_PAINT, self._vtk_control.OnPaint)

    def OnSize(self, event):
        """Overrides the default OnSize in order to refresh the traits
        of the render window."""
        if self._renwin is not None:
            self._vtk_control.OnSize(event)
            self._renwin.update_traits()

    def OnButtonDown(self, event):
        """Overrides the default on button down method.
        """
        self._interacting = True
        self._vtk_control.OnButtonDown(event)

    def OnButtonUp(self, event):
        self._interacting = False
        self._vtk_control.OnButtonUp(event)

    ###########################################################################
    # 'event' interface.
    ###########################################################################

    def _closed_fired(self):
        super(Scene, self)._closed_fired()
        self.picker = None
        self._vtk_control = None

    ###########################################################################
    # Non-public interface.
    ###########################################################################
    def _create_control(self, parent):
        """ Create the toolkit-specific control that represents the widget. """

        # Create the VTK widget.
        self._vtk_control = window = wxVTKRenderWindowInteractor(parent, -1,
                                                                 stereo=self.stereo)

        # Override these handlers.
        window.Bind(wx.EVT_CHAR, None) # Remove the default handler.
        window.Bind(wx.EVT_CHAR, self.OnKeyDown)
        window.Bind(wx.EVT_KEY_UP, None) # Remove the default handler.
        window.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        window.Bind(wx.EVT_PAINT, None) # Remove the default handler.
        window.Bind(wx.EVT_PAINT, self.OnPaint)
        window.Bind(wx.EVT_SIZE, None) # Remove the default handler.
        window.Bind(wx.EVT_SIZE, self.OnSize)
        # Override the button down and up handlers as well to note the
        # interaction.  This is to toggle the busy status nicely.
        for evt in (wx.EVT_LEFT_DOWN, wx.EVT_RIGHT_DOWN,
                    wx.EVT_MIDDLE_DOWN):
            window.Bind(evt, None)
            window.Bind(evt, self.OnButtonDown)
        for evt in (wx.EVT_LEFT_UP, wx.EVT_RIGHT_UP,
                    wx.EVT_MIDDLE_UP):
            window.Bind(evt, None)
            window.Bind(evt, self.OnButtonUp)

        # Enable the widget.
        window.Enable(1)
        # Switch the default interaction style to the trackball one.
        window.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

        # Grab the renderwindow.
        renwin = self._renwin = tvtk.to_tvtk(window.GetRenderWindow())
        renwin.trait_set(point_smoothing=self.point_smoothing,
                   line_smoothing=self.line_smoothing,
                   polygon_smoothing=self.polygon_smoothing)
        # Create a renderer and add it to the renderwindow
        self._renderer = tvtk.Renderer()
        renwin.add_renderer(self._renderer)
        # Save a reference to our camera so it is not GC'd -- needed for
        # the sync_traits to work.
        self._camera = self.camera

        # Sync various traits.
        self._renderer.background = self.background
        self.sync_trait('background', self._renderer)
        self.renderer.on_trait_change(self.render, 'background')
        self._camera.parallel_projection = self.parallel_projection
        self.sync_trait('parallel_projection', self._camera)
        renwin.off_screen_rendering = self.off_screen_rendering
        self.sync_trait('off_screen_rendering', self._renwin)
        self.render_window.on_trait_change(self.render, 'off_screen_rendering')
        self.render_window.on_trait_change(self.render, 'stereo_render')
        self.render_window.on_trait_change(self.render, 'stereo_type')
        self.camera.on_trait_change(self.render, 'parallel_projection')

        def _show_parent_hack(window, parent):
            """A hack to get the VTK scene properly setup for use."""
            # Force the parent to show itself.
            parent.Show(1)
            # on some platforms, this SetSize() is necessary to cause
            # an OnPaint() when the event loop begins; else we get an
            # empty window until we force a redraw.
            window.SetSize(parent.GetSize())
            # This is necessary on slow machines in order to force the
            # wx events to be handled.
            wx.GetApp().Yield(True)
            window.Render()

        if wx.Platform == '__WXMSW__':
            _show_parent_hack(window, parent)
        else:
            if (wx.VERSION[0] == 2) and (wx.VERSION[1] < 5):
                _show_parent_hack(window, parent)
            window.Update()

        # Because of the way the VTK widget is setup, and because we
        # set the size above, the window sizing is usually completely
        # messed up when the application window is shown.  To work
        # around this a dynamic IDLE event handler is added and
        # immediately removed once it executes.  This event handler
        # simply forces a resize to occur.  The _idle_count allows us
        # to execute the idle function a few times (this seems to work
        # better).
        def _do_idle(event, window=window):
            w = wx.GetTopLevelParent(window)
            # Force a resize
            sz = w.GetSize()
            w.SetSize((sz[0]-1, sz[1]-1))
            w.SetSize(sz)
            window._idle_count -= 1
            if window._idle_count < 1:
                window.Bind(wx.EVT_IDLE, None)
                del window._idle_count

        window._idle_count = 2
        window.Bind(wx.EVT_IDLE, _do_idle)

        self._interactor = tvtk.to_tvtk(window._Iren)
        return window

    def _lift(self):
        """Lift the window to the top. Useful when saving screen to an
        image."""
        if self.render_window.off_screen_rendering:
            # Do nothing if off screen rendering is being used.
            return

        w = self._vtk_control
        while w and not w.IsTopLevel():
            w = w.GetParent()
        if w:
            w.Raise()
            wx.GetApp().Yield(True)
            self.render()

    def _start_event_callback(self, obj, event):
        if self._interacting:
            return
        else:
            self.busy = True

    def _end_event_callback(self, obj, event):
        if self._interacting:
            return
        else:
            self.busy = False

    def _busy_changed(self, val):
        GUI.set_busy(val)

    def _full_screen_fired(self):
        fs = self._fullscreen
        if isinstance(fs, PopupScene):
            fs.close()
            self._fullscreen = None
        elif fs is None:
            ver = tvtk.Version()
            popup = False
            if wx.Platform == '__WXMSW__':
                popup = True
            elif ver.vtk_major_version > 5:
                popup = True
            elif (ver.vtk_major_version == 5) and \
                 ((ver.vtk_minor_version >= 1) or \
                  (ver.vtk_build_version > 2)):
                popup = True
            if popup:
                # There is a bug with earlier versions of VTK that
                # breaks reparenting a window which is why we test for
                # the version above.
                f = PopupScene(self)
                self._fullscreen = f
                f.fullscreen()
            else:
                f = FullScreen(self)
                f.run() # This will block.
                self._fullscreen = None

    def _disable_fullscreen(self):
        fs = self._fullscreen
        if isinstance(fs, PopupScene):
            fs.close()
            self._fullscreen = None
