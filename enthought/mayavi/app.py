"""The MayaVi Envisage application.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2007, Enthought, Inc.
# License: BSD Style.

# On systems with multiple wx installations installed, pick one that works
# with the libraries Mayavi depends on.
from enthought.util import wxversioncheck
wxversioncheck.ensureMinimal('2.6')

# Standard library imports.
import sys

# Enthought library imports.
from enthought.envisage import _set_using_workbench
from enthought.envisage.api import Application
from enthought.envisage.workbench.services import IWORKBENCH
from enthought.traits.api import HasTraits, Instance

# We use the Workbench plugin.
_set_using_workbench(True)

# Local imports.
from enthought.mayavi.services import IMAYAVI
from enthought.mayavi.plugin_definitions \
     import PLUGIN_DEFINITIONS, NONGUI_PLUGIN_DEFINITIONS

# GLOBALS
# Indicates if we are being run from ipython -wthread or -pylab.  This
# is set the first time the application is run.
WTHREAD_MODE = None

######################################################################
# Private function.
######################################################################
def _set_wthread_mode():
    """Sets the wthread mode global.
    """
    import wx
    global WTHREAD_MODE
    # We check to see if a wxApp is already running (this happens
    # mayavi is used via ipython -pylab/-wthread) in which case
    # special care is necessary in starting and stopping the
    # envisage app.
    if WTHREAD_MODE is None:
        wx_app = wx.GetApp()
        if wx_app is not None:
            if sys.platform == 'darwin':
                # This is not optimal at all!  There ought to be a
                # better way to see if the wxMainloop is running on
                # the Mac.
                WTHREAD_MODE = ('-wthread' in sys.argv) or \
                               ('-pylab' in sys.argv)
            else:
                # For some strange reason this does not work on Mac
                # OSX!
                WTHREAD_MODE = wx_app.IsMainLoopRunning()


###########################################################################
# `Mayavi` class.
###########################################################################
class Mayavi(HasTraits):
    """The Mayavi application class.

    This class may be easily subclassed to do something different.
    For example, the way to script MayaVi (as a standalone application
    and not interactively) is to subclass this and do the needful.
    """

    # The main envisage application.
    application = Instance('enthought.envisage.core.application.Application')

    # The MayaVi Script instance.
    script = Instance('enthought.mayavi.script.Script')

    def main(self, argv=None, plugin_defs=PLUGIN_DEFINITIONS):
        """The main application is created and launched here.

        Parameters
        ----------

        - argv : `list` of `strings`

          The list of command line arguments.  The default is `None`
          where no command line arguments are parsed.  To support
          command line arguments you can pass `sys.argv[1:]`.

        - plugin_defs : `list`

          A list of plugins to load.  Defaults to the GUI MayaVi
          plugin.  By changing this one can change the plugins
          started.
        """
        # Parse any cmd line args.
        if argv is None:
            argv = []
        self.parse_command_line(argv)

        # FIXME: This forces wxPython to be imported first.  This eliminates
        # some very wierd problems with certain builds of VTK and wxPython
        # that produce Pango errors under Linux.
        from enthought.pyface.api import GUI

        # Setup the wthread mode if necessary.
        _set_wthread_mode()

        gui = GUI()
        # Create the application
        self.application = app = Application(argv=sys.argv,
                                             id='enthought.mayavi',
                                             gui=gui,
                                             plugin_definitions=plugin_defs,
                                             requires_gui=False)

        # Arrange a the callback to be called on application's started
        # event.  This can be used to script mayavi.
        app.on_trait_change(self._start, 'started')

        # Start the application.
        app.start()

        # Start the GUI event loop.  Usually this call does not return
        # until the GUI is closed.  However, if we are running via
        # 'ipython -wthread/-pylab' then this will return immediately!
        gui.start_event_loop()

        if not WTHREAD_MODE:
            app.stop()

    def parse_command_line(self, argv):
        """Parse command line options.

        Parameters
        ----------

        - argv : `list` of `strings`

          The list of command line arguments.  The default is `None`
          where no command line arguments are parsed.  To support
          command line arguments you can pass `sys.argv[1:]`.

        """
        # XXX: TODO.
        from optparse import OptionParser
        usage = "usage: %prog [options]"
        parser = OptionParser(usage)

        (options, args) = parser.parse_args(argv)

    def run(self):
        """This function is called after the GUI has started.
        Override this to do whatever you want to do as a MayaVi
        script.  If this is not overridden then an empty MayaVi
        application will be started.

        *Make sure all other MayaVi specific imports are made here!*
        If you import MayaVi related code earlier you will run into
        difficulties.  Use 'self.script' to script the mayavi engine.
        """
        pass

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _start(self, app):
        """This callback is called as soon as Envisage starts up.  The
        argument to this function is the
        enthought.envisage.Application singleton instance.
        """
        # Setup the script instances.
        self.script = app.get_service(IMAYAVI)
        
        # This in turn calls the testing code once the GUI mainloop is
        # running.
        g = app.gui
        g.on_trait_change(lambda : g.invoke_later(self.run), 'started')

        if WTHREAD_MODE:
            # This calls the application's stop method when the
            # workbench fires the 'window_closed' event and when there
            # are no windows left.  This is necessary since when we
            # are started from an `ipython -wthread` session this is
            # the only way to shutdown cleanly.
            def _window_closed(obj, name, value):
                """This function stops the envisage application if the
                last window is closed.
                """
                if len(obj.windows) == 0:
                    app.stop()

            wb = app.get_service(IWORKBENCH)
            wb.on_trait_change(_window_closed, 'window_closed')


def main(argv=None):
    """Simple helper to start up the mayavi application.  This returns
    the running ``Script`` instance."""
    m = Mayavi()
    m.main(argv)
    return m.script

if __name__ == '__main__':
    main(sys.argv[1:])
