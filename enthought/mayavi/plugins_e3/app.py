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

######################################################################
# Useful functions.
######################################################################
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

        # Create the application
        app = MayaviWorkbenchApplication(plugins=plugins)
        self.application = app

        setup_logger(logger, 'mayavi.log', mode=self.log_mode)
        # Arrange a the callback to be called on application's started
        # event.  This can be used to script mayavi.
        app.on_trait_change(self._start, 'started')

        # Start the application.
        app.run()


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
