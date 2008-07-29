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
from enthought.mayavi.preferences.api import preference_manager

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
        from enthought.mayavi import api
        about_dialog = AboutDialog(
            parent = self.workbench.active_window.control,
            image  = ImageResource('m2_about.jpg',
                                   search_path=[IMG_DIR]),
            additions = ['Authors: Prabhu Ramachandran',
                            'and Gael Varoquaux',
                            '',
                            'Mayavi version %s' % api.__version__],
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

