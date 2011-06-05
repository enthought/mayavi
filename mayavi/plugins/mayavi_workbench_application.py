"""Mayavi specific workbench application.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
from os.path import dirname
import logging

# Enthought library imports.
from traits.api import Bool
from envisage.ui.workbench.api import WorkbenchApplication
from pyface.api import AboutDialog, ImageResource, SplashScreen

# Local imports.
import mayavi.api
from mayavi.preferences.api import preference_manager

IMG_DIR = dirname(mayavi.api.__file__)
logger = logging.getLogger(__name__)


class MayaviWorkbenchApplication(WorkbenchApplication):
    """ The mayavi application. """

    #### MayaviWorkbenchApplication interface #################################

    # Turn this off if you don't want the workbench to start a GUI
    # event loop.
    start_gui_event_loop = Bool(True, desc='start a GUI event loop')

    #### 'IApplication' interface #############################################

    # The application's globally unique Id.
    id = 'mayavi_e3'

    #### 'WorkbenchApplication' interface #####################################

    # Branding information.
    #
    # The icon used on window title bars etc.
    icon = ImageResource('m2.ico', search_path=[IMG_DIR])

    # The name of the application (also used on window title bars etc).
    name = 'Mayavi2 - The 3D data visualizer'

    ###########################################################################
    # 'WorkbenchApplication' interface.
    ###########################################################################
    def run(self):
        """ Run the application.

        This does the following:

        1) Starts the application
        2) Creates and opens a workbench window
        3) Starts the GUI event loop (only if start_gui_event_loop is
           True)
        4) When the event loop terminates, stops the application

        This particular method is overridden from the parent class to
        allow the user to not run the gui event loop as would be
        necessary when the loop is started elsewhere or when run fron
        IPython.

        """

        logger.debug('---------- workbench application ----------')

        # Make sure the GUI has been created (so that, if required, the splash
        # screen is shown).
        gui = self.gui

        # Start the application.
        if self.start():
            # Create and open the first workbench window.
            window = self.workbench.create_window(
                position=self.window_position, size=self.window_size
            )
            window.open()

            # We stop the application when the workbench has exited.
            self.workbench.on_trait_change(self._on_workbench_exited, 'exited')

            # Start the GUI event loop if needed.
            if self.start_gui_event_loop:
                # THIS CALL DOES NOT RETURN UNTIL THE GUI IS CLOSED.
                gui.start_event_loop()

        return


    ######################################################################
    # Non-public interface.
    ######################################################################
    def _about_dialog_default(self):
        """ Trait initializer. """
        from mayavi import api
        from vtk import vtkVersion
        vtk_version = vtkVersion().GetVTKVersion()
        about_dialog = AboutDialog(
            parent = self.workbench.active_window.control,
            image  = ImageResource('m2_about.jpg',
                                   search_path=[IMG_DIR]),
            additions = ['Authors: Prabhu Ramachandran',
                            'and Gael Varoquaux',
                            '',
                            'Mayavi version %s \t - \t VTK version %s' %
                            (api.__version__, vtk_version)],
        )

        return about_dialog

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

