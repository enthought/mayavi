"""Mayavi specific Tasks application.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import dirname
import logging

# Enthought library imports.
from traits.api import Bool
from envisage.ui.tasks.api import TasksApplication
from pyface.api import AboutDialog, ImageResource, SplashScreen

# Local imports.
import mayavi.api
from mayavi.preferences.api import preference_manager

IMG_DIR = dirname(mayavi.api.__file__)
logger = logging.getLogger(__name__)


class MayaviTasksApplication(TasksApplication):
    """ The mayavi application. """

    #### MayaviTasksApplication interface #################################

    # Turn this off if you don't want the task to start a GUI
    # event loop.
    start_gui_event_loop = Bool(True, desc='start a GUI event loop')

    #### 'IApplication' interface #############################################

    # The application's globally unique Id.
    id = 'mayavi_e3'

    #### 'Application' interface #####################################

    # Branding information.
    #
    # The icon used on window title bars etc.
    icon = ImageResource('m2.ico', search_path=[IMG_DIR])

    # The name of the application (also used on window title bars etc).
    name = 'Mayavi2 - The 3D data visualizer'

    ###########################################################################
    # 'IApplication' interface.
    ###########################################################################

    def run(self):
        """ Run the application.

        This particular method is overridden from the parent class to
        allow the user to not run the gui event loop as would be
        necessary when the loop is started elsewhere or when run fron
        IPython.

        Returns
        -------
        bool
            Whether the application started successfully (i.e., without a
            veto).
        """
        # Make sure the GUI has been created (so that, if required, the splash
        # screen is shown).
        gui = self.gui

        started = self.start()
        if started:
            # Create windows from the default or saved application layout.
            self._create_windows()

            # Start the GUI event loop.
            gui.set_trait_later(self, "application_initialized", self)

            if self.start_gui_event_loop:
                # THIS CALL DOES NOT RETURN UNTIL THE GUI IS CLOSED.
                gui.start_event_loop()

        return started

    ###########################################################################
    # 'TasksApplication' interface.
    ###########################################################################

    def _default_layout_default(self):
        pass


    ######################################################################
    # Non-public interface.
    ######################################################################

    def _splash_screen_default(self):
        """ Trait initializer. """
        if preference_manager.root.show_splash_screen:
            splash_screen = SplashScreen(
                image             = ImageResource('m2_about.jpg',
                                                  search_path=[IMG_DIR]),
                show_log_messages = True,
            )
        else:
            splash_screen = None

        return splash_screen
