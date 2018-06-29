"""
A simple VTK widget for PyQt or PySide.
See http://www.trolltech.com for Qt documentation,
http://www.riverbankcomputing.co.uk for PyQt, and
http://pyside.github.io for PySide.

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

Changes by Rodrigo Mologni, Sep. 2013 (Credit to Daniele Esposti)
 Bug fix to PySide: Converts PyCObject to void pointer.

Changes by Greg Schussman, Aug. 2014
 The keyPressEvent function now passes keysym instead of None.

Changes by Alex Tsui, Apr. 2015
 Port from PyQt4 to PyQt5.

Changes by Fabian Wenzel, Jan. 2016
 Support for Python3
"""

import sys

from pyface.qt import qt_api
if qt_api == 'pyqt':
    PyQtImpl = "PyQt4"
elif qt_api == 'pyqt5':
    PyQtImpl = "PyQt5"
elif qt_api == 'pyside2':
    PyQtImpl = "PySide2"
else:
    PyQtImpl = "PySide"

import vtk

from tvtk import messenger

# Check whether a specific QVTKRenderWindowInteractor base
# class was chosen, can be set to "QGLWidget"
QVTKRWIBase = "QWidget"
try:
    import vtk.qt
    QVTKRWIBase = vtk.qt.QVTKRWIBase
except (ImportError, AttributeError):
    pass

if PyQtImpl == "PyQt5":
    if QVTKRWIBase == "QGLWidget":
        try:
            from PyQt5.QtWidgets import QOpenGLWidget as QGLWidget
        except:
            from PyQt5.QtOpenGL import QGLWidget
    from PyQt5.QtWidgets import QWidget, QSizePolicy, QApplication
    from PyQt5.QtGui import QWheelEvent
    from PyQt5.QtCore import Qt, QTimer, QObject, QSize, QEvent
elif PyQtImpl == "PyQt4":
    if QVTKRWIBase == "QGLWidget":
        from PyQt4.QtOpenGL import QGLWidget
    from PyQt4.QtGui import QWidget, QSizePolicy, QApplication, QWheelEvent
    from PyQt4.QtCore import Qt, QTimer, QObject, QSize, QEvent
elif PyQtImpl == "PySide":
    if QVTKRWIBase == "QGLWidget":
        from PySide.QtOpenGL import QGLWidget
    from PySide.QtGui import QWidget, QSizePolicy, QApplication, QWheelEvent
    from PySide.QtCore import Qt, QTimer, QObject, QSize, QEvent
elif PyQtImpl == "PySide2":
    if QVTKRWIBase == "QGLWidget":
        try:
            from PySide2.QtWidgets import QOpenGLWidget as QGLWidget
        except:
            from PySide2.QtOpenGL import QGLWidget
    from PySide2.QtWidgets import QWidget, QSizePolicy, QApplication
    from PySide2.QtGui import QWheelEvent
    from PySide2.QtCore import Qt, QTimer, QObject, QSize, QEvent
else:
    raise ImportError("Unknown PyQt implementation " + repr(PyQtImpl))


# Define types for base class, based on string
if QVTKRWIBase == "QWidget":
    QVTKRWIBaseClass = QWidget
elif QVTKRWIBase == "QGLWidget":
    QVTKRWIBaseClass = QGLWidget
else:
    raise ImportError(
        "Unknown base class for QVTKRenderWindowInteractor " + QVTKRWIBase
    )


class QVTKRenderWindowInteractor(QVTKRWIBaseClass):

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
        0:  Qt.ArrowCursor,          # VTK_CURSOR_DEFAULT
        1:  Qt.ArrowCursor,          # VTK_CURSOR_ARROW
        2:  Qt.SizeBDiagCursor,      # VTK_CURSOR_SIZENE
        3:  Qt.SizeFDiagCursor,      # VTK_CURSOR_SIZENWSE
        4:  Qt.SizeBDiagCursor,      # VTK_CURSOR_SIZESW
        5:  Qt.SizeFDiagCursor,      # VTK_CURSOR_SIZESE
        6:  Qt.SizeVerCursor,        # VTK_CURSOR_SIZENS
        7:  Qt.SizeHorCursor,        # VTK_CURSOR_SIZEWE
        8:  Qt.SizeAllCursor,        # VTK_CURSOR_SIZEALL
        9:  Qt.PointingHandCursor,   # VTK_CURSOR_HAND
        10: Qt.CrossCursor,          # VTK_CURSOR_CROSSHAIR
    }

    def __init__(self, parent=None, **kw):
        # the current button
        self._ActiveButton = Qt.NoButton

        # private attributes
        self.__saveX = 0
        self.__saveY = 0
        self.__saveModifiers = Qt.NoModifier
        self.__saveButtons = Qt.NoButton
        self.__wheelDelta = 0

        # do special handling of some keywords:
        # stereo, rw

        try:
            stereo = bool(kw['stereo'])
        except KeyError:
            stereo = False

        try:
            rw = kw['rw']
        except KeyError:
            rw = None

        # create qt-level widget
        if QVTKRWIBase == "QWidget":
            if "wflags" in kw:
                wflags = kw['wflags']
            else:
                wflags = Qt.WindowFlags()
            QWidget.__init__(self, parent, wflags | Qt.MSWindowsOwnDC)
        elif QVTKRWIBase == "QGLWidget":
            QGLWidget.__init__(self, parent)

        if rw:  # user-supplied render window
            self._RenderWindow = rw
        else:
            self._RenderWindow = vtk.vtkRenderWindow()

        wid = self._get_win_id()
        self._RenderWindow.SetWindowInfo(wid)

        self._should_set_parent_info = (sys.platform == 'win32')

        if stereo:  # stereo mode
            self._RenderWindow.StereoCapableWindowOn()
            self._RenderWindow.SetStereoTypeToCrystalEyes()

        try:
            self._Iren = kw['iren']
        except KeyError:
            self._Iren = vtk.vtkGenericRenderWindowInteractor()

        self._Iren.SetRenderWindow(self._RenderWindow)

        if hasattr(self, 'devicePixelRatio'):
            self._pixel_ratio = self.devicePixelRatio()
        else:
            self._pixel_ratio = 1.0

        # do all the necessary qt setup
        self.setAttribute(Qt.WA_OpaquePaintEvent)
        self.setAttribute(Qt.WA_PaintOnScreen)
        self.setMouseTracking(True) # get all mouse events
        self.setFocusPolicy(Qt.WheelFocus)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        self._Timer = QTimer(self)
        self._Timer.timeout.connect(self.TimerEvent)

        # add wheel timer to fix scrolling issue with trackpad
        self.wheel_timer = None
        if PyQtImpl != 'PyQt5':
            self.wheel_timer = QTimer()
            self.wheel_timer.setSingleShot(True)
            self.wheel_timer.setInterval(25)
            self.wheel_timer.timeout.connect(self._emit_wheel_event)
            self._saved_wheel_event_info = ()

        self._Iren.AddObserver('CreateTimerEvent', messenger.send)
        messenger.connect(self._Iren, 'CreateTimerEvent', self.CreateTimer)
        self._Iren.AddObserver('DestroyTimerEvent', messenger.send)
        messenger.connect(self._Iren, 'DestroyTimerEvent', self.DestroyTimer)
        self._RenderWindow.AddObserver('CursorChangedEvent', messenger.send)
        messenger.connect(self._RenderWindow, 'CursorChangedEvent',
                          self.CursorChangedEvent)

        # Create a hidden child widget and connect its destroyed signal to its
        # parent ``Finalize`` slot. The hidden children will be destroyed
        # before its parent thus allowing cleanup of VTK elements.
        self._hidden = QWidget(self)
        self._hidden.hide()
        self._hidden.destroyed.connect(self.Finalize)

    def __getattr__(self, attr):
        """Makes the object behave like a vtkGenericRenderWindowInteractor"""
        if attr == '__vtk__':
            return lambda t=self._Iren: t
        elif hasattr(self._Iren, attr):
            return getattr(self._Iren, attr)
        else:
            raise AttributeError(
                self.__class__.__name__ + " has no attribute named " + attr
            )

    def _get_win_id(self):
        WId = self.winId()

        # Python2
        if type(WId).__name__ == 'PyCObject':
            from ctypes import pythonapi, c_void_p, py_object

            pythonapi.PyCObject_AsVoidPtr.restype  = c_void_p
            pythonapi.PyCObject_AsVoidPtr.argtypes = [py_object]

            WId = pythonapi.PyCObject_AsVoidPtr(WId)

        # Python3
        elif type(WId).__name__ == 'PyCapsule':
            from ctypes import pythonapi, c_void_p, py_object, c_char_p

            pythonapi.PyCapsule_GetName.restype = c_char_p
            pythonapi.PyCapsule_GetName.argtypes = [py_object]

            name = pythonapi.PyCapsule_GetName(WId)

            pythonapi.PyCapsule_GetPointer.restype  = c_void_p
            pythonapi.PyCapsule_GetPointer.argtypes = [py_object, c_char_p]

            WId = pythonapi.PyCapsule_GetPointer(WId, name)
        return str(int(WId))

    def Finalize(self):
        '''
        Call internal cleanup method on VTK objects
        '''
        self._RenderWindow.Finalize()

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
        QTimer.singleShot(0, self.ShowCursor)

    def HideCursor(self):
        """Hides the cursor."""
        self.setCursor(Qt.BlankCursor)

    def ShowCursor(self):
        """Shows the cursor."""
        vtk_cursor = self._Iren.GetRenderWindow().GetCurrentCursor()
        qt_cursor = self._CURSOR_MAP.get(vtk_cursor, Qt.ArrowCursor)
        self.setCursor(qt_cursor)

    def closeEvent(self, evt):
        self.Finalize()

    def sizeHint(self):
        return QSize(400, 400)

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
            winid = self._get_win_id()
            self._RenderWindow.SetWindowInfo(winid)
            parent = self.parent()
            if parent is not None:
                self._RenderWindow.SetParentInfo(winid)
            else:
                self._RenderWindow.SetParentInfo('')

        pxr = self._pixel_ratio
        w = int(self.width()*pxr)
        h = int(self.height()*pxr)

        vtk.vtkRenderWindow.SetSize(self._RenderWindow, w, h)
        self._Iren.SetSize(w, h)
        self._Iren.ConfigureEvent()
        self.update()

    def _GetCtrlShift(self, ev):
        ctrl = shift = False

        if hasattr(ev, 'modifiers'):
            if ev.modifiers() & Qt.ShiftModifier:
                shift = True
            if ev.modifiers() & Qt.ControlModifier:
                ctrl = True
        else:
            if self.__saveModifiers & Qt.ShiftModifier:
                shift = True
            if self.__saveModifiers & Qt.ControlModifier:
                ctrl = True

        return ctrl, shift

    def enterEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        self._Iren.SetEventInformationFlipY(self.__saveX, self.__saveY,
                                            ctrl, shift, chr(0), 0, None)
        self._Iren.EnterEvent()

    def leaveEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        self._Iren.SetEventInformationFlipY(self.__saveX, self.__saveY,
                                            ctrl, shift, chr(0), 0, None)
        self._Iren.LeaveEvent()

    def mousePressEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        repeat = 0
        if ev.type() == QEvent.MouseButtonDblClick:
            repeat = 1

        pxr = self._pixel_ratio
        self._Iren.SetEventInformationFlipY(int(ev.x()*pxr), int(ev.y()*pxr),
                                            ctrl, shift, chr(0), repeat, None)

        self._ActiveButton = ev.button()

        if self._ActiveButton == Qt.LeftButton:
            self._Iren.LeftButtonPressEvent()
        elif self._ActiveButton == Qt.RightButton:
            self._Iren.RightButtonPressEvent()
        elif self._ActiveButton == Qt.MidButton:
            self._Iren.MiddleButtonPressEvent()

    def mouseReleaseEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        pxr = self._pixel_ratio
        self._Iren.SetEventInformationFlipY(int(ev.x()*pxr), int(ev.y()*pxr),
                                            ctrl, shift, chr(0), 0, None)

        if self._ActiveButton == Qt.LeftButton:
            self._Iren.LeftButtonReleaseEvent()
        elif self._ActiveButton == Qt.RightButton:
            self._Iren.RightButtonReleaseEvent()
        elif self._ActiveButton == Qt.MidButton:
            self._Iren.MiddleButtonReleaseEvent()

    def mouseMoveEvent(self, ev):
        self.__saveModifiers = ev.modifiers()
        self.__saveButtons = ev.buttons()
        pxr = self._pixel_ratio
        self.__saveX = int(ev.x()*pxr)
        self.__saveY = int(ev.y()*pxr)

        ctrl, shift = self._GetCtrlShift(ev)
        self._Iren.SetEventInformationFlipY(int(ev.x()*pxr), int(ev.y()*pxr),
                                            ctrl, shift, chr(0), 0, None)
        self._Iren.MouseMoveEvent()

    def keyPressEvent(self, ev):
        """ React to key pressed event.

        If event text contains multiple characters, it is truncated to first
        one.
        """
        ctrl, shift = self._GetCtrlShift(ev)
        key_sym = _qt_key_to_key_sym(ev.key())
        if ev.key() < 256:
            # Sometimes, the OS allows a chord (e.g. Alt-T) to generate
            # a Unicode character outside of the 8-bit Latin-1 range. We will
            # try to pass along Latin-1 characters unchanged, since VTK expects
            # a single `char` byte. If not, we will try to pass on the root key
            # of the chord (e.g. 'T' above).
            if ev.text() and ev.text() <= u'\u00ff':
                key = ev.text().encode('latin-1')
            else:
                # Has modifiers, but an ASCII key code.
                key = chr(ev.key())
        else:
            key = chr(0)

        # Truncating key pressed to first character if slow machine leads to
        # multiple times the same key (required by SetEventInformationFlipY):
        if ev.isAutoRepeat():
            key = key[0]

        self._Iren.SetEventInformationFlipY(self.__saveX, self.__saveY,
                                            ctrl, shift, key, 0, key_sym)
        self._Iren.KeyPressEvent()
        self._Iren.CharEvent()

    def keyReleaseEvent(self, ev):
        ctrl, shift = self._GetCtrlShift(ev)
        key_sym = _qt_key_to_key_sym(ev.key())
        if ev.key() < 256:
            if ev.text() and ev.text() <= u'\u00ff':
                key = ev.text().encode('latin-1')
            else:
                # Has modifiers, but an ASCII key code.
                key = chr(ev.key())
        else:
            key = chr(0)

        self._Iren.SetEventInformationFlipY(self.__saveX, self.__saveY,
                                            ctrl, shift, key, 0, None)
        self._Iren.KeyReleaseEvent()

    def wheelEvent(self, ev):
        """ Reimplemented to work around scrolling bug in Mac.

        Work around https://bugreports.qt-project.org/browse/QTBUG-22269.
        Accumulate wheel events that are within a period of 25ms into a single
        event.  Changes in buttons or modifiers, while a scroll is going on,
        are not handled, since they seem to be too much of a corner case to be
        worth handling.
        """
        if hasattr(ev, 'delta'):
            self.__wheelDelta += ev.delta()
            self._saved_wheel_event_info = (
                ev.pos(),
                ev.globalPos(),
                self.__wheelDelta,
                ev.buttons(),
                ev.modifiers(),
                ev.orientation()
            )
        else:
            self.__wheelDelta += ev.angleDelta().y()
            if self.__wheelDelta >= 60:
                self._Iren.MouseWheelForwardEvent()
                self.__wheelDelta = 0
            elif self.__wheelDelta <= -60:
                self._Iren.MouseWheelBackwardEvent()
                self.__wheelDelta = 0

        if self.wheel_timer and not self.wheel_timer.isActive():
            ev.setAccepted(True)
            self.wheel_timer.start()

    def _emit_wheel_event(self):
        ev = QWheelEvent(*self._saved_wheel_event_info)
        if ev.delta() >= 0:
            self._Iren.MouseWheelForwardEvent()
        else:
            self._Iren.MouseWheelBackwardEvent()
        self.wheel_timer.stop()
        self.__wheelDelta = 0

    def GetRenderWindow(self):
        return self._RenderWindow

    def Render(self):
        self.update()


def QVTKRenderWidgetConeExample():
    """A simple example that uses the QVTKRenderWindowInteractor class."""

    # every QT app needs an app
    app = QApplication(['QVTKRenderWindowInteractor'])

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
    coneMapper.SetInputConnection(cone.GetOutputPort())

    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)

    ren.AddActor(coneActor)

    # show the widget
    widget.show()
    # start event processing
    app.exec_()


_keysyms = {
    Qt.Key_Backspace: 'BackSpace',
    Qt.Key_Tab: 'Tab',
    Qt.Key_Backtab: 'Tab',
    # Qt.Key_Clear : 'Clear',
    Qt.Key_Return: 'Return',
    Qt.Key_Enter: 'Return',
    Qt.Key_Shift: 'Shift_L',
    Qt.Key_Control: 'Control_L',
    Qt.Key_Alt: 'Alt_L',
    Qt.Key_Pause: 'Pause',
    Qt.Key_CapsLock: 'Caps_Lock',
    Qt.Key_Escape: 'Escape',
    Qt.Key_Space: 'space',
    # Qt.Key_Prior : 'Prior',
    # Qt.Key_Next : 'Next',
    Qt.Key_End: 'End',
    Qt.Key_Home: 'Home',
    Qt.Key_Left: 'Left',
    Qt.Key_Up: 'Up',
    Qt.Key_Right: 'Right',
    Qt.Key_Down: 'Down',
    Qt.Key_SysReq: 'Snapshot',
    Qt.Key_Insert: 'Insert',
    Qt.Key_Delete: 'Delete',
    Qt.Key_Help: 'Help',
    Qt.Key_0: '0',
    Qt.Key_1: '1',
    Qt.Key_2: '2',
    Qt.Key_3: '3',
    Qt.Key_4: '4',
    Qt.Key_5: '5',
    Qt.Key_6: '6',
    Qt.Key_7: '7',
    Qt.Key_8: '8',
    Qt.Key_9: '9',
    Qt.Key_A: 'a',
    Qt.Key_B: 'b',
    Qt.Key_C: 'c',
    Qt.Key_D: 'd',
    Qt.Key_E: 'e',
    Qt.Key_F: 'f',
    Qt.Key_G: 'g',
    Qt.Key_H: 'h',
    Qt.Key_I: 'i',
    Qt.Key_J: 'j',
    Qt.Key_K: 'k',
    Qt.Key_L: 'l',
    Qt.Key_M: 'm',
    Qt.Key_N: 'n',
    Qt.Key_O: 'o',
    Qt.Key_P: 'p',
    Qt.Key_Q: 'q',
    Qt.Key_R: 'r',
    Qt.Key_S: 's',
    Qt.Key_T: 't',
    Qt.Key_U: 'u',
    Qt.Key_V: 'v',
    Qt.Key_W: 'w',
    Qt.Key_X: 'x',
    Qt.Key_Y: 'y',
    Qt.Key_Z: 'z',
    Qt.Key_Asterisk: 'asterisk',
    Qt.Key_Plus: 'plus',
    Qt.Key_Minus: 'minus',
    Qt.Key_Period: 'period',
    Qt.Key_Slash: 'slash',
    Qt.Key_F1: 'F1',
    Qt.Key_F2: 'F2',
    Qt.Key_F3: 'F3',
    Qt.Key_F4: 'F4',
    Qt.Key_F5: 'F5',
    Qt.Key_F6: 'F6',
    Qt.Key_F7: 'F7',
    Qt.Key_F8: 'F8',
    Qt.Key_F9: 'F9',
    Qt.Key_F10: 'F10',
    Qt.Key_F11: 'F11',
    Qt.Key_F12: 'F12',
    Qt.Key_F13: 'F13',
    Qt.Key_F14: 'F14',
    Qt.Key_F15: 'F15',
    Qt.Key_F16: 'F16',
    Qt.Key_F17: 'F17',
    Qt.Key_F18: 'F18',
    Qt.Key_F19: 'F19',
    Qt.Key_F20: 'F20',
    Qt.Key_F21: 'F21',
    Qt.Key_F22: 'F22',
    Qt.Key_F23: 'F23',
    Qt.Key_F24: 'F24',
    Qt.Key_NumLock: 'Num_Lock',
    Qt.Key_ScrollLock: 'Scroll_Lock',
    }


def _qt_key_to_key_sym(key):
    """ Convert a Qt key into a vtk keysym.

    This is essentially copied from the c++ implementation in
    GUISupport/Qt/QVTKInteractorAdapter.cxx.
    """

    if key not in _keysyms:
        return 'None'

    return _keysyms[key]


if __name__ == "__main__":
    QVTKRenderWidgetConeExample()
