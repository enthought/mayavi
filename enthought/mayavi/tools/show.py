# Author: Prabhu Ramachandran <prabhu[at]aero[dot]iitb[dot]ac[dot]in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from enthought.pyface.api import GUI, ApplicationWindow
from enthought.traits.api import HasTraits, Int
from enthought.traits.ui.api import toolkit
from enthought.etsconfig.api import ETSConfig

# Globals.
# The GUI instance.
_gui = None

def is_ui_running():
    """Returns True if the UI event loop is running."""
    tk = ETSConfig.toolkit
    from engine_manager import options
    if options.offscreen:
        return True 

    if tk == 'wx':
        import wx
        return wx.App.IsMainLoopRunning()
    elif tk == 'qt4':
        from PyQt4 import QtGui
        app = QtGui.QApplication.instance()
        if app is not None:
            # Hack gleaned from enthought.traits.ui.qt4.view_application
            if hasattr(app, '_in_event_loop'):
                if _gui is None:
                    return app._in_event_loop
                else:
                    return _gui.started

    return False


def show(func=None):
    """ Start interacting with the figure.
    
    By default, this function simply creates a GUI and starts its
    event loop if needed.
    
    If it is used as a decorator, then it may be used to decorate a
    function which requires a UI.   If the GUI event loop is already
    running it simply runs the function.  If not the event loop is
    started and function is run in the toolkit's event loop.  The choice
    of UI is via `ETSConfig.toolkit`.  

    """
    global _gui
    if func is None:
        if not is_ui_running():
            g = GUI()
            _gui = g
            g.start_event_loop()
        return

    def wrapper(*args, **kw):
        """Wrapper function to run given function inside the GUI event
        loop.
        """
        global _gui
        tk = ETSConfig.toolkit

        if is_ui_running():
            return func(*args, **kw)
        else:
            g = GUI()
            if tk == 'wx':
                # Create a dummy app so invoke later works on wx.
                a = ApplicationWindow(size=(1,1))
                GUI.invoke_later(lambda: a.close())
                a.open()

            GUI.invoke_later(func, *args, **kw)
            _gui = g
            g.start_event_loop()

    return wrapper

