"""
A simple VTK widget for PyQt v4, the Qt v4 bindings for Python.
See http://www.trolltech.com for Qt documentation, and
http://www.riverbankcomputing.co.uk for PyQt.

This class is based on the vtkGenericRenderWindowInteractor and is
therefore fairly powerful.  It should also play nicely with the
vtk3DWidget code.

Created by Prabhu Ramachandran, May 2002
Based on David Gobbi's QVTKRenderWidget.py

Changes by Gerard Vermeulen Feb. 2003
 Win32 support.

Changes by Gerard Vermeulen, May 2003
 Bug fixes and better integration with the Qt framework.

Changes by Phil Thompson, Nov. 2006
 Ported to PyQt v4.
 Added support for wheel events.

Changes by Phil Thompson, Oct. 2007
 Bug fixes.

Changes by Phil Thompson, Mar. 2008
 Added cursor support.
"""

import sys

import os
qt_api = os.environ.get('QT_API', 'pyqt') 
if qt_api == 'pyqt':
    from PyQt4 import QtGui, QtCore
else:
    from PySide import QtGui, QtCore
    from ctypes import pythonapi, c_void_p, py_object
    pythonapi.PyCObject_AsVoidPtr.restype = c_void_p
    pythonapi.PyCObject_AsVoidPtr.argtypes = [ py_object ]

import vtk

from enthought.tvtk import messenger


class QVTKRenderWindowInteractor(QtGui.QWidget):

    """ A QVTKRenderWindowInteractor for Python and Qt.  Uses a
    vtkGenericRenderWindowInteractor to handle the interactions.  Use
    GetRenderWindow() to get the vtkRenderWindow.  Create with the
    keyword stereo=1 in order to generate a stereo-capable window.

    The user interface is summarized in vtkInteractorStyle.h:

    - Keypress j / Keypress t: toggle between joystick (position
      sensitive) and trackball (motion sensitive) styles. In joystick
      style, motion occurs continuously as long as a mouse button is
      pressed. In trackball style, motion occurs when the mouse button
      is pressed and the mouse pointer moves.

    - Keypress c / Keypress o: toggle between camera and object
      (actor) modes. In camera mode, mouse events affect the camera
      position and focal point. In object mode, mouse events affect
      the actor that is under the mouse pointer.

    - Button 1: rotate the camera around its focal point (if camera
      mode) or rotate the actor around its origin (if actor mode). The
      rotation is in the direction defined from the center of the
      renderer's viewport towards the mouse position. In joystick mode,
      the magnitude of the rotation is determined by the distance the
      mouse is from the center of the render window.

    - Button 2: pan the camera (if camera mode) or translate the actor
      (if object mode). In joystick mode, the direction of pan or
      translation is from the center of the viewport towards the mouse
      position. In trackball mode, the direction of motion is the
      direction the mouse moves. (Note: with 2-button mice, pan is
      defined as <Shift>-Button 1.)

    - Button 3: zoom the camera (if camera mode) or scale the actor
      (if object mode). Zoom in/increase scale if the mouse position is
      in the top half of the viewport; zoom out/decrease scale if the
      mouse position is in the bottom half. In joystick mode, the amount
      of zoom is controlled by the distance of the mouse pointer from
      the horizontal centerline of the window.

    - Keypress 3: toggle the render window into and out of stereo
      mode.  By default, red-blue stereo pairs are created. Some systems
      support Crystal Eyes LCD stereo glasses; you have to invoke
      SetStereoTypeToCrystalEyes() on the rendering window.  Note: to
      use stereo you also need to pass a stereo=1 keyword argument to
      the constructor.

    - Keypress e: exit the application.

    - Keypress f: fly to the picked point

    - Keypress p: perform a pick operation. The render window interactor
      has an internal instance of vtkCellPicker that it uses to pick.

    - Keypress r: reset the camera view along the current view
      direction. Centers the actors and moves the camera so that all actors
      are visible.

    - Keypress s: modify the representation of all actors so that they
      are surfaces.

    - Keypress u: invoke the user-defined function. Typically, this
      keypress will bring up an interactor that you can type commands in.

    - Keypress w: modify the representation of all actors so that they
      are wireframe.
    """

    # Map between VTK and Qt cursors.
    _CURSOR_MAP = {
        0:  QtCore.Qt.ArrowCursor,          # VTK_CURSOR_DEFAULT
        1:  QtCore.Qt.ArrowCursor,          # VTK_CURSOR_ARROW
        2:  QtCore.Qt.SizeBDiagCursor,      # VTK_CURSOR_SIZENE
        3:  QtCore.Qt.SizeFDiagCursor,      # VTK_CURSOR_SIZENWSE
        4:  QtCore.Qt.SizeBDiagCursor,      # VTK_CURSOR_SIZESW
        5:  QtCore.Qt.SizeFDiagCursor,      # VTK_CURSOR_SIZESE
        6:  QtCore.Qt.SizeVerCursor,        # VTK_CURSOR_SIZENS
        7:  QtCore.Qt.SizeHorCursor,        # VTK_CURSOR_SIZEWE
        8:  QtCore.Qt.SizeAllCursor,        # VTK_CURSOR_SIZEALL
        9:  QtCore.Qt.PointingHandCursor,   # VTK_CURSOR_HAND
        10: QtCore.Qt.CrossCursor,          # VTK_CURSOR_CROSSHAIR
    }

    # Map from Qt key codes to VTK key names
    _KEY_MAP = {
        QtCore.Qt.Key_Escape: "Esc",
        QtCore.Qt.Key_Tab: "Tab",
        QtCore.Qt.Key_Backtab: "Backtab",
        QtCore.Qt.Key_Backspace: "Backspace",
        QtCore.Qt.Key_Return: "Return",
        QtCore.Qt.Key_Enter: "Enter",
        QtCore.Qt.Key_Insert: "Insert",
        QtCore.Qt.Key_Delete: "Delete",
        QtCore.Qt.Key_Pause: "Pause",
        QtCore.Qt.Key_Print: "Print",
        QtCore.Qt.Key_SysReq: "Sysreq",
        QtCore.Qt.Key_Clear: "Clear",
        QtCore.Qt.Key_Home: "Home",
        QtCore.Qt.Key_End: "End",
        QtCore.Qt.Key_Left: "Left",
        QtCore.Qt.Key_Up: "Up",
        QtCore.Qt.Key_Right: "Right",
        QtCore.Qt.Key_Down: "Down",
        QtCore.Qt.Key_PageUp: "Prior",
        QtCore.Qt.Key_PageDown: "Next",
        QtCore.Qt.Key_Meta: "Meta",
        QtCore.Qt.Key_CapsLock: "Caps_Lock",
        QtCore.Qt.Key_NumLock: "Num_Lock",
        QtCore.Qt.Key_ScrollLock: "Scroll_Lock",
        QtCore.Qt.Key_F1: "F1",
        QtCore.Qt.Key_F2: "F2",
        QtCore.Qt.Key_F3: "F3",
        QtCore.Qt.Key_F4: "F4",
        QtCore.Qt.Key_F5: "F5",
        QtCore.Qt.Key_F6: "F6",
        QtCore.Qt.Key_F7: "F7",
        QtCore.Qt.Key_F8: "F8",
        QtCore.Qt.Key_F9: "F9",
        QtCore.Qt.Key_F10: "F10",
        QtCore.Qt.Key_F11: "F11",
        QtCore.Qt.Key_F12: "F12",
    }

    def __init__(self, parent=None, wflags=QtCore.Qt.WindowFlags(), **kw):
        # the current button
        self._ActiveButton = QtCore.Qt.NoButton

        # private attributes
        self.__oldFocus = None
        self.__saveX = 0
        self.__saveY = 0
        self.__saveModifiers = QtCore.Qt.NoModifier
        self.__saveButtons = QtCore.Qt.NoButton

        # do special handling of some keywords:
        # stereo, rw

        stereo = 0

        if kw.has_key('stereo'):
            if kw['stereo']:
                stereo = 1

        rw = None

        if kw.has_key('rw'):
            rw = kw['rw']

        # create qt-level widget
        QtGui.QWidget.__init__(self, parent, wflags|QtCore.Qt.MSWindowsOwnDC)

        if rw: # user-supplied render window
            self._RenderWindow = rw
        else:
            self._RenderWindow = vtk.vtkRenderWindow()
        
        if qt_api == 'pyqt':
            self._RenderWindow.SetWindowInfo(str(int(self.winId())))
        else:
            
            # On Windows PySide has a bug with winID() function, so this is fix:
            if sys.platform == "win32":
                self._RenderWindow.SetWindowInfo(str(int(pythonapi.PyCObject_AsVoidPtr(self.winId()))))
        self._should_set_parent_info = (sys.platform == 'win32')

        if stereo: # stereo mode
            self._RenderWindow.StereoCapableWindowOn()
            self._RenderWindow.SetStereoTypeToCrystalEyes()

        self._Iren = vtk.vtkGenericRenderWindowInteractor()
        self._Iren.SetRenderWindow(self._RenderWindow)

        # do all the necessary qt setup
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)
        self.setAttribute(QtCore.Qt.WA_PaintOnScreen)
        self.setMouseTracking(True) # get all mouse events
        self.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))

        self._Timer = QtCore.QTimer(self)
        self.connect(self._Timer, QtCore.SIGNAL('timeout()'), self.TimerEvent)

        self._Iren.AddObserver('CreateTimerEvent', messenger.send)
        messenger.connect(self._Iren, 'CreateTimerEvent', self.CreateTimer)
        self._Iren.AddObserver('DestroyTimerEvent', messenger.send)
        messenger.connect(self._Iren, 'DestroyTimerEvent', self.DestroyTimer)
        render_window = self._Iren.GetRenderWindow()
        render_window.AddObserver('CursorChangedEvent', messenger.send)
        messenger.connect(render_window, 'CursorChangedEvent', self.CursorChangedEvent)

    def __getattr__(self, attr):
        """Makes the object behave like a vtkGenericRenderWindowInteractor"""
        if attr == '__vtk__':
            return lambda t=self._Iren: t
        elif hasattr(self._Iren, attr):
            return getattr(self._Iren, attr)
        else:
            raise AttributeError, self.__class__.__name__ + \
                  " has no attribute named " + attr

    def CreateTimer(self, obj, evt):
        self._Timer.start(10)

    def DestroyTimer(self, obj, evt):
        self._Timer.stop()
        return 1

    def TimerEvent(self):
        self._Iren.TimerEvent()

    def CursorChangedEvent(self, obj, evt):
        """Called when the CursorChangedEvent fires on the render window."""
        # This indirection is needed since when the event fires, the current
        # cursor is not yet set so we defer this by which time the current
        # cursor should have been set.
        QtCore.QTimer.singleShot(0, self.ShowCursor)

    def HideCursor(self):
        """Hides the cursor."""
        self.setCursor(QtCore.Qt.BlankCursor)

    def ShowCursor(self):
        """Shows the cursor."""
        vtk_cursor = self._Iren.GetRenderWindow().GetCurrentCursor()
        qt_cursor = self._CURSOR_MAP.get(vtk_cursor, QtCore.Qt.ArrowCursor)
        self.setCursor(qt_cursor)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def paintEngine(self):
        return None

    def paintEvent(self, ev):
        self._RenderWindow.Render()

    def resizeEvent(self, ev):
        if self._should_set_parent_info:
            # Set the window info and parent info on every resize.
            # vtkWin32OpenGLRenderWindow will render using incorrect offsets if
            # the parent info is not given to it because it assumes that it
            # needs to make room for the title bar.
            if qt_api == 'pyqt':
                self._RenderWindow.SetWindowInfo(str(int(self.winId())))
            else:
            
                # On Windows PySide has a bug with winID() function, so this is fix:
                if sys.platform == "win32":
                    self._RenderWindow.SetWindowInfo(str(int(pythonapi.PyCObject_AsVoidPtr(self.winId()))))
            parent = self.parent()
            if parent is not None:
                if qt_api == 'pyqt':
                    self._RenderWindow.SetParentInfo(str(int(self.winId())))
                else:
                    
                    # On Windows PySide has a bug with winID() function, so this is fix:
                    if sys.platform == "win32":
                        self._RenderWindow.SetParentInfo(str(int(pythonapi.PyCObject_AsVoidPtr(self.winId()))))
            else:
                self._RenderWindow.SetParentInfo('')

        w = self.width()
        h = self.height()

        self._RenderWindow.SetSize(w, h)
        self._Iren.SetSize(w, h)

    def _GetCtrlShift(self, ev):
        ctrl = shift = False

        if hasattr(ev, 'modifiers'):
            if ev.modifiers() & QtCore.Qt.ShiftModifier:
                shift = True
            if ev.modifiers() & QtCore.Qt.ControlModifier:
                ctrl = True
        else:
            if self.__saveModifiers & QtCore.Qt.ShiftModifier:
                shift = True
            if self.__saveModifiers & QtCore.Qt.ControlModifier:
                ctrl = True

        return ctrl, shift

    def enterEvent(self, ev):
        if not self.hasFocus():
            self.__oldFocus = self.focusWidget()
            self.setFocus()

        ctrl, shift = self._GetCtrlShift(ev)
        self._Iren.SetEventInformationFlipY(self.__saveX, self.__saveY,
                                            ctrl, shift, chr(0), 0, None)
        self._Iren.EnterEvent()

    def leaveEvent(self, ev):
        if self.__saveButtons == QtCore.Qt.NoButton and self.__oldFocus:
            self.__oldFocus.setFocus()
            self.__oldFocus = None

        ctrl, shift = self._GetCtrlShift(ev)
        self._Iren.SetEventInformationFlipY(self.__saveX, self.__saveY,
                                            ctrl, shift, chr(0), 0, None)
        self._Iren.LeaveEvent()

    def mousePressEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        repeat = 0
        if ev.type() == QtCore.QEvent.MouseButtonDblClick:
            repeat = 1
        self._Iren.SetEventInformationFlipY(ev.x(), ev.y(),
                                            ctrl, shift, chr(0), repeat, None)

        self._ActiveButton = ev.button()

        if self._ActiveButton == QtCore.Qt.LeftButton:
            self._Iren.LeftButtonPressEvent()
        elif self._ActiveButton == QtCore.Qt.RightButton:
            self._Iren.RightButtonPressEvent()
        elif self._ActiveButton == QtCore.Qt.MidButton:
            self._Iren.MiddleButtonPressEvent()

    def mouseReleaseEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        self._Iren.SetEventInformationFlipY(ev.x(), ev.y(),
                                            ctrl, shift, chr(0), 0, None)

        if self._ActiveButton == QtCore.Qt.LeftButton:
            self._Iren.LeftButtonReleaseEvent()
        elif self._ActiveButton == QtCore.Qt.RightButton:
            self._Iren.RightButtonReleaseEvent()
        elif self._ActiveButton == QtCore.Qt.MidButton:
            self._Iren.MiddleButtonReleaseEvent()

    def mouseMoveEvent(self, ev):
        self.__saveModifiers = ev.modifiers()
        self.__saveButtons = ev.buttons()
        self.__saveX = ev.x()
        self.__saveY = ev.y()

        ctrl, shift = self._GetCtrlShift(ev)
        self._Iren.SetEventInformationFlipY(ev.x(), ev.y(),
                                            ctrl, shift, chr(0), 0, None)
        self._Iren.MouseMoveEvent()

    def keyPressEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        key_sym = self._KEY_MAP.get(ev.key(), None)
        if ev.key() < 256:
            if ev.text():
                key = str(ev.text())
            else:
                # Has modifiers, but an ASCII key code.
                key = chr(ev.key())
        else:
            key = chr(0)

        self._Iren.SetEventInformationFlipY(self.__saveX, self.__saveY,
                                            ctrl, shift, key, 0, key_sym)
        self._Iren.KeyPressEvent()
        self._Iren.CharEvent()

    def keyReleaseEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        key_sym = self._KEY_MAP.get(ev.key(), None)
        if ev.key() < 256:
            key = chr(ev.key())
        else:
            key = chr(0)

        self._Iren.SetEventInformationFlipY(self.__saveX, self.__saveY,
                                            ctrl, shift, key, 0, key_sym)
        self._Iren.KeyReleaseEvent()

    def wheelEvent(self, ev):
        if ev.delta() >= 0:
            self._Iren.MouseWheelForwardEvent()
        else:
            self._Iren.MouseWheelBackwardEvent()

    def GetRenderWindow(self):
        return self._RenderWindow

    def Render(self):
        self.update()


def QVTKRenderWidgetConeExample():
    """A simple example that uses the QVTKRenderWindowInteractor class."""

    # every QT app needs an app
    app = QtGui.QApplication(['QVTKRenderWindowInteractor'])

    # create the widget
    widget = QVTKRenderWindowInteractor()
    widget.Initialize()
    widget.Start()
    # if you dont want the 'q' key to exit comment this.
    widget.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())

    ren = vtk.vtkRenderer()
    widget.GetRenderWindow().AddRenderer(ren)

    cone = vtk.vtkConeSource()
    cone.SetResolution(8)

    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInput(cone.GetOutput())

    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)

    ren.AddActor(coneActor)

    # show the widget
    widget.show()
    # start event processing
    app.exec_()

if __name__ == "__main__":
    QVTKRenderWidgetConeExample()
