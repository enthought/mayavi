""" Preferences page for a TVTK scene. """

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from apptools.preferences.ui.api import PreferencesPage
from traits.api import Range
from traitsui.api import View, Group, Item
from tvtk.tvtk_base import false_bool_trait, vtk_color_trait


class ScenePreferencesPage(PreferencesPage):
    """ Preferences page for a TVTK scene. """

    #### 'PreferencesPage' interface ##########################################

    # The page's category (e.g. 'General/Appearance'). The empty string means
    # that this is a top-level page.
    category = ''

    # The page's help identifier (optional). If a help Id *is* provided then
    # there will be a 'Help' button shown on the preference page.
    help_id = ''

    # The page name (this is what is shown in the preferences dialog.
    name = 'TVTK Scene'

    # The path to the preferences node that contains the preferences.
    preferences_path = 'tvtk.scene'

    #### Preferences ##########################################################

    # Turn on/off stereo rendering. Note that this is useful only at startup
    # and not at runtime.
    stereo = false_bool_trait(
        desc='specifies if stereo rendering is turned on'
    )

    # The magnification to use when dumping the screen to an image.
    magnification = Range(
        1, 2048, 1,
        desc='specifies the magnification to use while generating images'
    )

    # The background color of the renderer.
    background_color = vtk_color_trait((0.5, 0.5, 0.5))

    # The foreground color of the renderer.
    foreground_color = vtk_color_trait((1.0, 1.0, 1.0))

    #### Traits UI views ######################################################

    traits_view = View(
        Group(
            Item(name='background_color'),
            Item(name='foreground_color'),
            Item(name='stereo'),
            Item(name='magnification')
        )
    )

#### EOF ######################################################################
