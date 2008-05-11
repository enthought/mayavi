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
from enthought.traits.api import (HasTraits, Instance, Int,
    on_trait_change)

# Local imports.
from mayavi_workbench_application import MayaviWorkbenchApplication
from enthought.mayavi.preferences.api import preference_manager

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
    from enthought.tvtk.plugins.scene.scene_plugin import ScenePlugin
    from enthought.tvtk.plugins.scene.ui.scene_ui_plugin import SceneUIPlugin
    from enthought.mayavi.plugins.mayavi_plugin import MayaviPlugin
    from enthought.mayavi.plugins.mayavi_ui_plugin import MayaviUIPlugin
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
    For example, one way to script MayaVi (as a standalone application
    and not interactively) is to subclass this and do the needful.
    """

    # The main envisage application.
    application = Instance('enthought.envisage.ui.workbench.api.WorkbenchApplication')

    # The MayaVi Script instance.
    script = Instance('enthought.mayavi.plugins.script.Script')

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
        prefs = preference_manager.preferences
        app = MayaviWorkbenchApplication(plugins=plugins,
                                         preferences=prefs)
        self.application = app

        # Setup the logger.
        setup_logger(logger, 'mayavi.log', mode=self.log_mode)

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
    @on_trait_change('application.gui:started')
    def _on_application_gui_started(self, obj, trait_name, old, new):

        """This is called as soon as  the Envisage GUI starts
        up.   The method is responsible for setting our script instance   """

        if trait_name != 'started' or not new:
            return
        app = self.application
        from enthought.mayavi.plugins.script import Script
        window = app.workbench.active_window
        # Set our script instance.
        self.script = window.get_service(Script)
        # Call self.run from the GUI thread.
        app.gui.invoke_later(self.run)
  

def main(argv=None):
    """Simple helper to start up the mayavi application.  This returns
    the running application."""
    m = Mayavi()
    m.main(argv)
    return m

if __name__ == '__main__':
    main(sys.argv[1:])
