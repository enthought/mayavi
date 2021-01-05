""" Preferences page for a TVTK scene. """

# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from envisage.ui.tasks.api import PreferencesPane
from apptools.preferences.api import PreferencesHelper
from traits.api import Instance, Range, Str
from traitsui.api import View, Group, Item
from tvtk.tvtk_base import false_bool_trait, vtk_color_trait

from mayavi.preferences.api import preference_manager

class ScenePreferencesPane(PreferencesPane):
    """ Preferences page for a TVTK scene. """

    #### 'Controller' interface ###############################################

    #: The preferences helper for which this pane is a view.
    model = Instance(PreferencesHelper)

    #### 'PreferencesPane' interface ##########################################

    #: An identifier for the pane (unique within a category).
    id = Str("TVTK Scene")

    #: The ID of the category in which to place the pane.
    category = Str("TVTK")

    #: The pane appears after the pane with this ID.
    before = Str

    #: The pane appears after the pane with this ID.
    after = Str

    def _model_default(self):
        prefs = preference_manager.preferences
        return ScenePreferencesHelper(preferences=prefs)


    traits_view = View(
        Group(
            Item(name='background_color'),
            Item(name='foreground_color'),
            Item(name='stereo'),
            Item(name='magnification')
        )
    )


class ScenePreferencesHelper(PreferencesHelper):

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
