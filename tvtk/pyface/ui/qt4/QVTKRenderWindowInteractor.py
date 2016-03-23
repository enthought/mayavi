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

from tvtk import messenger
import vtk
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor as _QVTKRenderWindowInteractor   # noqa

# pyface does not support PyQt5 yet
from pyface.qt import qt_api
if qt_api == 'pyqt':
    PyQtImpl = "PyQt4"
else:
    PyQtImpl = "PySide"

if PyQtImpl == "PyQt4":
    from PyQt4.QtGui import QApplication, QWheelEvent
    from PyQt4.QtCore import Qt, QTimer
elif PyQtImpl == "PySide":
    from PySide.QtGui import QApplication, QWheelEvent
    from PySide.QtCore import Qt, QTimer
else:
    raise ImportError("Unknown PyQt implementation " + repr(PyQtImpl))


class QVTKRenderWindowInteractor(_QVTKRenderWindowInteractor):

    def __init__(self, parent=None, wflags=Qt.WindowFlags(), **kw):

        super(QVTKRenderWindowInteractor, self).__init__(parent=parent,
                                                         wflags=wflags,
                                                         **kw)

        # private attributes
        self.__oldFocus = None

        if vtk.VTK_MAJOR_VERSION < 7:
            # This function is added to the __init__ in VTK 7.0.0
            wid = self._get_win_id()
            self._RenderWindow.SetWindowInfo(wid)

        # add wheel timer to fix scrolling issue with trackpad
        self.wheel_timer = QTimer()
        self.wheel_timer.setSingleShot(True)
        self.wheel_timer.setInterval(25)
        self.wheel_timer.timeout.connect(self._emit_wheel_event)
        self.wheel_accumulator = 0
        self._saved_wheel_event_info = ()

        # tvtk events
        self._Iren.AddObserver('CreateTimerEvent', messenger.send)
        messenger.connect(self._Iren, 'CreateTimerEvent', self.CreateTimer)
        self._Iren.AddObserver('DestroyTimerEvent', messenger.send)
        messenger.connect(self._Iren, 'DestroyTimerEvent', self.DestroyTimer)
        self._RenderWindow.AddObserver('CursorChangedEvent', messenger.send)
        messenger.connect(self._RenderWindow, 'CursorChangedEvent',
                          self.CursorChangedEvent)

    def _get_win_id(self):
        # This function is called from __init__ function and
        # from the resizeEvent if the machine is a Windows system
        # This function is embeded in the __init__ function in VTK 7.0.0
        WId = self.winId()

        # Python2
        if type(WId).__name__ == 'PyCObject':
            from ctypes import pythonapi, c_void_p, py_object

            pythonapi.PyCObject_AsVoidPtr.restype = c_void_p
            pythonapi.PyCObject_AsVoidPtr.argtypes = [py_object]

            WId = pythonapi.PyCObject_AsVoidPtr(WId)

        # Python3
        elif type(WId).__name__ == 'PyCapsule':
            from ctypes import pythonapi, c_void_p, py_object, c_char_p

            pythonapi.PyCapsule_GetName.restype = c_char_p
            pythonapi.PyCapsule_GetName.argtypes = [py_object]

            name = pythonapi.PyCapsule_GetName(WId)

            pythonapi.PyCapsule_GetPointer.restype = c_void_p
            pythonapi.PyCapsule_GetPointer.argtypes = [py_object, c_char_p]

            WId = pythonapi.PyCapsule_GetPointer(WId, name)
        return str(int(WId))

    def paintEvent(self, ev):
        super(QVTKRenderWindowInteractor, self).paintEvent(ev)
        self._RenderWindow.Render()

    def resizeEvent(self, ev):
        if sys.platform == "win32":
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

        super(QVTKRenderWindowInteractor, self).resizeEvent(ev)

    def enterEvent(self, ev):
        if not self.hasFocus():
            self.__oldFocus = self.focusWidget()
            self.setFocus()

        super(QVTKRenderWindowInteractor, self).enterEvent(ev)

    def leaveEvent(self, ev):
        if self.__saveButtons == Qt.NoButton and self.__oldFocus:
            self.__oldFocus.setFocus()
            self.__oldFocus = None

        super(QVTKRenderWindowInteractor, self).leaveEvent(ev)

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
                                            ctrl, shift, key, 0, key_sym)
        self._Iren.KeyReleaseEvent()

    def wheelEvent(self, ev):
        """ Reimplemented to work around scrolling bug in Mac.

        Work around https://bugreports.qt-project.org/browse/QTBUG-22269.
        Accumulate wheel events that are within a period of 25ms into a single
        event.  Changes in buttons or modifiers, while a scroll is going on,
        are not handled, since they seem to be too much of a corner case to be
        worth handling.
        """
        self.wheel_accumulator += ev.delta()
        self._saved_wheel_event_info = (
                                        ev.pos(),
                                        ev.globalPos(),
                                        self.wheel_accumulator,
                                        ev.buttons(),
                                        ev.modifiers(),
                                        ev.orientation()
                                    )
        ev.setAccepted(True)

        if not self.wheel_timer.isActive():
            self.wheel_timer.start()

    def _emit_wheel_event(self):
        ev = QWheelEvent(*self._saved_wheel_event_info)
        if ev.delta() >= 0:
            self._Iren.MouseWheelForwardEvent()
        else:
            self._Iren.MouseWheelBackwardEvent()
        self.wheel_timer.stop()
        self.wheel_accumulator = 0


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
        return None

    return _keysyms[key]


if __name__ == "__main__":
    QVTKRenderWidgetConeExample()
