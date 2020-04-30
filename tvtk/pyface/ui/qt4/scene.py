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

"""A VTK interactor scene widget for the PyFace PyQt backend.  See the class
docs for more details.
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2004-2020, Enthought, Inc.
# License: BSD Style.


import os
import tempfile

from pyface.qt import QtCore, QtGui

from tvtk.api import tvtk
from tvtk import messenger
from traits.api import Instance, Button, Any
from traitsui.api import View, Group, Item, InstanceEditor

from pyface.api import Widget, GUI
from tvtk.pyface import picker
from tvtk.pyface import light_manager
from tvtk.pyface.utils import popup_save
from tvtk.pyface.tvtk_scene import TVTKScene

from .QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


######################################################################
# `_VTKRenderWindowInteractor` class.
######################################################################
class _VTKRenderWindowInteractor(QVTKRenderWindowInteractor):
    """ This is a thin wrapper around the standard VTK PyQt interactor.
    """
    def __init__(self, scene, parent, **kwargs):
        QVTKRenderWindowInteractor.__init__(self, parent, **kwargs)

        self._scene = scene
        self._interacting = False

    def resizeEvent(self, e):
        """ Reimplemented to refresh the traits of the render window.
        """
        QVTKRenderWindowInteractor.resizeEvent(self, e)

        self._scene._renwin.update_traits()

    def paintEvent(self, e):
        """ Reimplemented to create the light manager only when needed.  This
        is necessary because it makes sense to create the light manager only
        when the widget is realized.  Only when the widget is realized is the
        VTK render window created and only then are the default lights all
        setup correctly.
        """
        QVTKRenderWindowInteractor.paintEvent(self, e)

        scene = self._scene

        if scene.light_manager is None:
            scene.light_manager = light_manager.LightManager(scene)
            renwin = scene._renwin
            renwin.update_traits()
            vtk_rw = tvtk.to_vtk(renwin)
            renwin.add_observer('StartEvent', messenger.send)
            messenger.connect(vtk_rw, 'StartEvent', self._start_event_callback)
            renwin.add_observer('EndEvent', messenger.send)
            messenger.connect(vtk_rw, 'EndEvent', self._end_event_callback)

    def keyPressEvent(self, e):
        """ This method is overridden to prevent the 's'/'w'/'e'/'q' keys from
        doing the default thing which is generally useless.  It also handles
        the 'p' and 'l' keys so the picker and light manager are called.
        """
        key = e.key()
        modifiers = e.modifiers()

        scene = self._scene
        camera = scene.camera

        if key in [QtCore.Qt.Key_Minus]:
            camera.zoom(0.8)
            scene.render()
            scene._record_methods('camera.zoom(0.8)\nrender()')
            return

        if key in [QtCore.Qt.Key_Equal, QtCore.Qt.Key_Plus]:
            camera.zoom(1.25)
            scene.render()
            scene._record_methods('camera.zoom(1.25)\nrender()')
            return

        if key in [QtCore.Qt.Key_E, QtCore.Qt.Key_Q, QtCore.Qt.Key_Escape]:
            scene._disable_fullscreen()
            return

        if key in [QtCore.Qt.Key_W]:
            return

        if key in [QtCore.Qt.Key_R]:
            scene._record_methods('reset_zoom()')
            return

        if key in [QtCore.Qt.Key_P] and modifiers == QtCore.Qt.NoModifier:
            pos = self.mapFromGlobal(QtGui.QCursor.pos())
            x = pos.x()
            y = self.height() - pos.y()
            scene.picker.pick(x*self._pixel_ratio, y*self._pixel_ratio)
            return

        if key in [QtCore.Qt.Key_F] and modifiers == QtCore.Qt.NoModifier:
            pos = self.mapFromGlobal(QtGui.QCursor.pos())
            x = pos.x()
            y = self.height() - pos.y()
            data = scene.picker.pick_world(x*self._pixel_ratio, y*self._pixel_ratio)
            coord = data.coordinate
            if coord is not None:
                camera.focal_point = coord
                scene.render()
                scene._record_methods('camera.focal_point = %r\n'\
                                      'render()'%list(coord))
            return

        if key in [QtCore.Qt.Key_L] and modifiers == QtCore.Qt.NoModifier:
            scene.light_manager.configure()
            return

        if key in [QtCore.Qt.Key_S] and modifiers == QtCore.Qt.NoModifier:
            fname = popup_save(self.parent())
            if len(fname) != 0:
                self._scene.save(fname)
            return

        shift = ((modifiers & QtCore.Qt.ShiftModifier) == QtCore.Qt.ShiftModifier)

        if key == QtCore.Qt.Key_Left:
            if shift:
                camera.yaw(-5)
                scene._record_methods('camera.yaw(-5)')
            else:
                camera.azimuth(5)
                scene._record_methods('camera.azimuth(5)')

            scene.render()
            scene._record_methods('render()')
            return

        if key == QtCore.Qt.Key_Right:
            if shift:
                camera.yaw(5)
                scene._record_methods('camera.yaw(5)')
            else:
                camera.azimuth(-5)
                scene._record_methods('camera.azimuth(-5)')

            scene.render()
            scene._record_methods('render()')
            return

        if key == QtCore.Qt.Key_Up:
            if shift:
                camera.pitch(-5)
                scene._record_methods('camera.pitch(-5)')
            else:
                camera.elevation(-5)
                scene._record_methods('camera.elevation(-5)')

            camera.orthogonalize_view_up()
            scene.render()
            scene._record_methods('camera.orthogonalize_view_up()\nrender()')
            return

        if key == QtCore.Qt.Key_Down:
            if shift:
                camera.pitch(5)
                scene._record_methods('camera.pitch(5)')
            else:
                camera.elevation(5)
                scene._record_methods('camera.elevation(5)')

            camera.orthogonalize_view_up()
            scene.render()
            scene._record_methods('camera.orthogonalize_view_up()\nrender()')
            return

        QVTKRenderWindowInteractor.keyPressEvent(self, e)

    def mousePressEvent(self, ev):
        """Override for mouse presses."""
        self._interacting = True
        QVTKRenderWindowInteractor.mousePressEvent(self, ev)

    def mouseReleaseEvent(self, ev):
        """Override for mouse releases."""
        self._interacting = False
        QVTKRenderWindowInteractor.mouseReleaseEvent(self, ev)

    def _start_event_callback(self, obj, event):
        if self._interacting:
            return
        else:
            self._scene.busy = True

    def _end_event_callback(self, obj, event):
        if self._interacting:
            return
        else:
            self._scene.busy = False



######################################################################
# `Scene` class.
######################################################################
class Scene(TVTKScene, Widget):
    """A VTK interactor scene widget for pyface and PyQt.

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

    _vtk_control = Instance(_VTKRenderWindowInteractor)
    _fullscreen = Any(False)

    ###########################################################################
    # 'object' interface.
    ###########################################################################
    def __init__(self, parent=None, **traits):
        """ Initializes the object. """

        # Base class constructor.
        super(Scene, self).__init__(parent, **traits)

        # Setup the default picker.
        self.picker = picker.Picker(self)

        # The light manager needs creating.
        self.light_manager = None

        self._cursor = QtCore.Qt.ArrowCursor

    def __get_pure_state__(self):
        """Allows us to pickle the scene."""
        # The control attribute is not picklable since it is a VTK
        # object so we remove it.
        d = super(Scene, self).__get_pure_state__()
        for x in ['_vtk_control', '_fullscreen', '_cursor']:
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
        sz = self._vtk_control.size()

        return (sz.width(), sz.height())

    def set_size(self, size):
        """Set the size of the window."""
        self._vtk_control.resize(*size)

    def hide_cursor(self):
        """Hide the cursor."""
        self._cursor = self._vtk_control.cursor().shape()
        self._vtk_control.setCursor(QtCore.Qt.BlankCursor)

    def show_cursor(self):
        """Show the cursor."""
        self._vtk_control.setCursor(self._cursor)

    ###########################################################################
    # 'TVTKScene' interface.
    ###########################################################################
    def save_to_clipboard(self):
        """Saves a bitmap of the scene to the clipboard."""
        handler, name = tempfile.mkstemp()
        self.save_bmp(name)
        QtGui.QApplication.clipboard().setImage(QtGui.QImage(name))
        os.close(handler)
        os.unlink(name)

    ###########################################################################
    # 'event' interface.
    ###########################################################################
    def _closed_fired(self):
        super(Scene, self)._closed_fired()
        self.picker = None
        self._vtk_control = None
        self.control = None

    ###########################################################################
    # Non-public interface.
    ###########################################################################
    def _create_control(self, parent):
        """ Create the toolkit-specific control that represents the widget. """

        # Create the VTK widget.
        self._vtk_control = window = _VTKRenderWindowInteractor(
            self, parent, stereo=self.stereo)

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
        renwin.off_screen_rendering = self.off_screen_rendering
        self._camera.parallel_projection = self.parallel_projection
        self.sync_trait('parallel_projection', self._camera)
        self.sync_trait('off_screen_rendering', self._renwin)
        self.render_window.on_trait_change(self.render, 'off_screen_rendering')
        self.render_window.on_trait_change(self.render, 'stereo_render')
        self.render_window.on_trait_change(self.render, 'stereo_type')
        self.camera.on_trait_change(self.render, 'parallel_projection')

        self._interactor = tvtk.to_tvtk(window._Iren)

        return window

    def _lift(self):
        """Lift the window to the top. Useful when saving screen to an
        image."""
        if self.render_window.off_screen_rendering:
            # Do nothing if off screen rendering is being used.
            return

        self._vtk_control.window().raise_()
        QtCore.QCoreApplication.processEvents()

    def _full_screen_fired(self):
        fs = self._fullscreen
        if fs:
            self._vtk_control.window().showNormal()
            self._fullscreen = False
        else:
            self._vtk_control.window().showFullScreen()
            self._fullscreen = True

    def _disable_fullscreen(self):
        fs = self._fullscreen
        if fs:
            self._vtk_control.window().showNormal()
            self._fullscreen = False

    def _busy_changed(self, val):
        GUI.set_busy(val)
