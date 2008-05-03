"""The Mayavi Envisage application.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import sys
import os.path
import logging

# Enthought library imports.
from enthought.logger.api import LogFileHandler, FORMATTER
from enthought.etsconfig.api import ETSConfig
from enthought.traits.api import HasTraits, Instance, Int

# Local imports.
from mayavi_workbench_application import MayaviWorkbenchApplication


# GLOBALS
logger = logging.getLogger()

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


def setup_logger(logger, fname, stream=True, mode=logging.ERROR):
    """Setup a log file and the logger in `ETSConfig.application_home`.

    Parameters:
    -----------

    fname -- file name the logger should use.

    stream -- Add a stream handler.

    mode -- the logging mode.
    
    """
    path = os.path.join(ETSConfig.application_home, fname)
    handler = LogFileHandler(path)
    logger.addHandler(handler)
    if stream:
        s = logging.StreamHandler()
        s.setFormatter(FORMATTER)
        s.setLevel(mode)
        logger.addHandler(s)
    logger.info("*"*80)
    logger.info("logfile is: '%s'", os.path.abspath(path))
    logger.info("*"*80)


def get_plugins():
    from enthought.envisage.core_plugin import CorePlugin
    from enthought.envisage.ui.workbench.workbench_plugin import WorkbenchPlugin
    from enthought.plugins.python_shell.python_shell_plugin import PythonShellPlugin
    from enthought.tvtk.plugins_e3.scene.scene_plugin import ScenePlugin
    from enthought.tvtk.plugins_e3.scene.ui.scene_ui_plugin import SceneUIPlugin
    from enthought.mayavi.plugins_e3.mayavi_plugin import MayaviPlugin
    from enthought.mayavi.plugins_e3.mayavi_ui_plugin import MayaviUIPlugin
    plugins = [CorePlugin(),
               WorkbenchPlugin(),
               MayaviPlugin(),
               MayaviUIPlugin(),
               ScenePlugin(),
               SceneUIPlugin(),
               PythonShellPlugin(),
               ]
    return plugins



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
    application = Instance('enthought.envisage.ui.workbench.api.WorkbenchApplication')

    # The MayaVi Script instance.
    script = Instance('enthought.mayavi.plugins_e3.script.Script')

    # The logging mode.
    log_mode = Int(logging.ERROR, desc='the logging mode to use')

    def main(self, argv=None, plugins=None):
        """The main application is created and launched here.

        Parameters
        ----------

        - argv : `list` of `strings`

          The list of command line arguments.  The default is `None`
          where no command line arguments are parsed.  To support
          command line arguments you can pass `sys.argv[1:]`.

        - plugins : `list` of `Plugin`s

          List of plugins to start.  If none is provided it defaults to
          something meaningful.

        - log_mode : The logging mode to use.

        """
        # Parse any cmd line args.
        if argv is None:
            argv = []
        self.parse_command_line(argv)

        if plugins is None:
            plugins = get_plugins()

        # Setup the wthread mode if necessary.
        _set_wthread_mode()

        # Create the application
        app = MayaviWorkbenchApplication(plugins=plugins)
        self.application = app

        setup_logger(logger, 'mayavi.log', mode=self.log_mode)
        # Arrange a the callback to be called on application's started
        # event.  This can be used to script mayavi.
        app.on_trait_change(self._start, 'started')

        # Start the application.
        app.run()

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
    def _start(self, app_event):
        """This callback is called as soon as Envisage starts up.  The
        argument to this function is the
        enthought.envisage.Application singleton instance.
        """
        app = app_event.application
        
        # This in turn calls the testing code once the GUI mainloop is
        # running.
        g = app.gui
        g.on_trait_change(lambda value: self._bind_name_to_shell(value,app),
                          'started') 
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

            wb = app.workbench
            wb.on_trait_change(_window_closed, 'window_closed')

    def _bind_name_to_shell(self, value, app):
        if not value:
            return
        # Setup the script instances.
        from enthought.mayavi.plugins_e3.script import Script
        self.script = app.workbench.active_window.get_service(Script)
        script = self.script
        script.engine.start()

        id = 'enthought.plugins.python_shell.view.python_shell_view.PythonShellView'
        py = app.workbench.active_window.get_view_by_id(id)
        if py is None:
            logger.error('*'*80)
            logger.error("Can't find the Python shell view to bind variables")
            return

        py.bind('mayavi', script)
        py.bind('mayavi_app', script.engine)
   

def main(argv=None):
    """Simple helper to start up the mayavi application.  This returns
    the running ``Script`` instance."""
    m = Mayavi()
    m.main(argv)
    return m.script

if __name__ == '__main__':
    main(sys.argv[1:])
