# Author: Prabhu Ramachandran <prabhu[at]aero[dot]iitb[dot]ac[dot]in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

from traits.etsconfig.api import ETSConfig
from pyface.api import GUI, ApplicationWindow
from traits.api import HasTraits, Button, Any
from traitsui.api import View, Group, Item
from pyface.util import guisupport

# Globals.
# The GUI instance.
_gui = None
# The stop show instance.
_stop_show = None


def is_ui_running():
    """ Returns True if the UI event loop is running.
    """
    from .engine_manager import options
    if options.offscreen:
        return True
    elif ETSConfig.toolkit == 'wx':
        return guisupport.is_event_loop_running_wx()
    elif ETSConfig.toolkit == 'qt4':
        return guisupport.is_event_loop_running_qt4()
    else:
        return False


###############################################################################
# `StopShow` class.
###############################################################################
class StopShow(HasTraits):

    ########################################
    # Traits

    stop = Button('Stop interaction',
                  desc='if the UI interaction is to be stopped')

    # Private traits.
    # Stores a reference to the UI object so it can be disposed when the
    # interaction is stopped.
    _ui = Any

    view = View(Group(Item('stop'), show_labels=False),
                buttons=[], title='Control Show')

    ######################################################################
    # `object` interface.
    ######################################################################
    def __init__(self, **traits):
        super(StopShow, self).__init__(**traits)
        self._ui = self.edit_traits()

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _stop_fired(self):
        _gui.stop_event_loop()
        self._ui.dispose()


def show(func=None, stop=False):
    """ Start interacting with the figure.

    By default, this function simply creates a GUI and starts its
    event loop if needed.

    If it is used as a decorator, then it may be used to decorate a
    function which requires a UI.   If the GUI event loop is already
    running it simply runs the function.  If not the event loop is
    started and function is run in the toolkit's event loop.  The choice
    of UI is via `ETSConfig.toolkit`.

    If the argument stop is set to True then it pops up a UI where the
    user can stop the event loop.  Subsequent calls to `show` will
    restart the event loop.

    **Parameters**

      :stop:  A boolean which specifies if a UI dialog is displayed which
              allows the event loop to be stopped.

    **Examples**

    Here is a simple example demonstrating the use of show::

      >>> from mayavi import mlab
      >>> mlab.test_contour3d()
      >>> mlab.show()

    You can stop interaction via a simple pop up UI like so::

      >>> mlab.test_contour3d()
      >>> mlab.show(stop=True)

    The decorator can be used like so::

      >>> @mlab.show
      ... def do():
      ...    mlab.test_contour3d()
      ...
      >>> do()

    The decorator can also be passed the stop argument::

      >>> @mlab.show(stop=True)
      ... def do():
      ...    mlab.test_contour3d()
      ...
      >>> do()

    """
    global _gui, _stop_show
    if func is None:
        if not is_ui_running():
            g = GUI()
            _gui = g
            if stop:
                _stop_show = StopShow()
            g.start_event_loop()
        return

    def wrapper(*args, **kw):
        """Wrapper function to run given function inside the GUI event
        loop.
        """
        global _gui, _stop_show
        tk = ETSConfig.toolkit

        if is_ui_running():
            # In this case we should not pop up the UI since we likely
            # don't want to stop the mainloop.
            return func(*args, **kw)
        else:
            g = GUI()
            if tk == 'wx':
                # Create a dummy app so invoke later works on wx.
                a = ApplicationWindow(size=(1, 1))
                GUI.invoke_later(lambda: a.close())
                a.open()

            GUI.invoke_later(func, *args, **kw)
            _gui = g
            if stop:
                # Pop up the UI to stop the mainloop.
                _stop_show = StopShow()
            g.start_event_loop()

    return wrapper
