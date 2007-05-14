"""Preferences for a TVTK scene.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.workbench.preference import WorkbenchPreferencePage
from enthought.traits.api import Range
from enthought.traits.ui.api import View, Group, Item
from enthought.tvtk.tvtk_base import false_bool_trait, vtk_color_trait

# Local imports.
from enthought.tvtk.plugins.scene.services import ITVTKSCENE


##############################################################################
# ScenePreferencePage class.
##############################################################################
class ScenePreferencePage(WorkbenchPreferencePage):

    # Turn on/off stereo rendering.  Note that this is useful only at
    # startup and not at runtime.
    stereo = false_bool_trait(desc='specifies if stereo rendering is turned on')

    # The maginification to use when dumping the screen to an image.
    magnification = Range(1, 2048, 1,
                          desc='specifies the magnification to use while generating images')

    # The background color of the renderer.
    background_color = vtk_color_trait((0.5, 0.5, 0.5))

    # The background color of the renderer.
    foreground_color = vtk_color_trait((1.0, 1.0, 1.0))

    traits_view = View(Group(Item(name='background_color'),
                             Item(name='foreground_color'),
                             Item(name='stereo'),
                             Item(name='magnification')))

    ###########################################################################
    # Protected 'WorkbenchPreferencePage' interface.
    ###########################################################################
    def _get_preferences(self):
        """ Returns the preferences that this page is editing. """
        app = self._application
        return app.get_service(ITVTKSCENE).preferences
