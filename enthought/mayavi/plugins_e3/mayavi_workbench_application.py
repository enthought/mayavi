"""Mayavi specific workbench application.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc. 
# License: BSD Style.

# Standard library imports.
from os.path import dirname

# Enthought library imports.
from enthought.envisage.ui.workbench.api import WorkbenchApplication
from enthought.pyface.api import AboutDialog, ImageResource, SplashScreen

# Local imports.
import enthought.mayavi.api

IMG_DIR = dirname(enthought.mayavi.api.__file__)


class MayaviWorkbenchApplication(WorkbenchApplication):
    """ The mayavi application. """

    #### 'IApplication' interface #############################################

    # The application's globally unique Id.
    id = 'enthought.mayavi_e3'

    #### 'WorkbenchApplication' interface #####################################

    # Branding information.
    #
    # The icon used on window title bars etc.
    icon = ImageResource('m2.ico', search_path=[IMG_DIR])

    # The name of the application (also used on window title bars etc).
    name = 'Mayavi2'

    ###########################################################################
    # 'WorkbenchApplication' interface.
    ###########################################################################

    def _about_dialog_default(self):
        """ Trait initializer. """

        about_dialog = AboutDialog(
            parent = self.workbench.active_window.control,
            image  = ImageResource('m2_about.jpg',
                                   search_path=[IMG_DIR]),
            additions = ['Authors: Prabhu Ramachandran',
                         'and Gael Varoquaux'],
        )

        return about_dialog

    def _splash_screen_default(self):
        """ Trait initializer. """

        splash_screen = SplashScreen(
            image             = ImageResource('m2_about.jpg',
                                              search_path=[IMG_DIR]),
            show_log_messages = True,
        )

        return splash_screen

