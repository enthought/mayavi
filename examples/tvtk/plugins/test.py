#!/usr/bin/env python

""" This is a simple test envisage3 application to demonstrate how one
can use TVTK's scene and browser plugins to create a simple application.
"""

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import os.path
import logging

# Enthought library imports.
from apptools.logger.api import LogFileHandler, FORMATTER
from traits.etsconfig.api import ETSConfig
from traits.api import List
from envisage.api import Plugin
from envisage.ui.workbench.api import WorkbenchApplication
from envisage.core_plugin import CorePlugin
from envisage.ui.workbench.workbench_plugin import WorkbenchPlugin
from envisage.plugins.python_shell.python_shell_plugin import PythonShellPlugin
from tvtk.plugins.scene.scene_plugin import ScenePlugin
from tvtk.plugins.scene.ui.scene_ui_plugin import SceneUIPlugin
from tvtk.plugins.browser.browser_plugin import BrowserPlugin
from pyface.workbench.api import Perspective, PerspectiveItem


logger = logging.getLogger()

###############################################################################
# `TestPerspective` class.
###############################################################################
class TestPerspective(Perspective):
    """ An default perspective for the app. """

    # The perspective's name.
    name = 'Test'

    # Should this perspective be enabled or not?
    enabled = True

    # Should the editor area be shown in this perspective?
    show_editor_area = True

    # View IDs.
    BROWSER_VIEW = 'tvtk.plugins.browser.browser_view.BrowserView'
    SHELL_VIEW = 'envisage.plugins.python_shell.view.python_shell_view.PythonShellView'

    # The contents of the perspective.
    contents = [
        PerspectiveItem(id=BROWSER_VIEW, position='left'),
        PerspectiveItem(id=SHELL_VIEW, position='bottom')
    ]

###############################################################################
# `MyPlugin` class.
###############################################################################
class MyPlugin(Plugin):

    # Extension points we contribute to.
    PERSPECTIVES = 'envisage.ui.workbench.perspectives'

    # The plugin's unique identifier.
    id = 'tvtk_example_plugin'

    # The plugin's name (suitable for displaying to the user).
    name = 'TVTK example plugin'

    # Perspectives.
    perspectives = List(contributes_to=PERSPECTIVES)

    def _perspectives_default(self):
        """ Trait initializer. """
        return [TestPerspective]


###############################################################################
# Useful functions.
###############################################################################
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


def bind_object(value, app):
    """Binds the scene manager service to the Python shell."""
    if not value:
        # value is False when the GUI is stopped.
        return
    id = 'envisage.plugins.python_shell.view.python_shell_view.PythonShellView'
    py = app.workbench.active_window.get_view_by_id(id)

    id = 'tvtk.plugins.scene.i_scene_manager.ISceneManager'
    sm = app.workbench.active_window.get_service(id)
    if py is not None:
        py.bind('scene_manager', sm)


def main():
    """The main application is created and launched here."""
    # Setup the logger.

    plugins = [CorePlugin(),
               WorkbenchPlugin(),
               MyPlugin(),
               ScenePlugin(),
               SceneUIPlugin(),
               BrowserPlugin(),
               PythonShellPlugin(),
               ]
    # Create an Envisage application.
    id = 'tvtk.examples.plugins.test'
    application = WorkbenchApplication(id=id,
                                       plugins = plugins
                                       )
    # This needs to be done here since the ETSConfig.application_home is
    # not set correctly up to this point.
    setup_logger(logger, 'test.log', mode=logging.DEBUG)

    application.gui.on_trait_change(lambda value: bind_object(value, application),
                                    'started')
    # Start the application.
    application.run()


if __name__ == '__main__':
    main()

