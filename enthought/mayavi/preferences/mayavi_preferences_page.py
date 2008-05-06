"""Preferences for Mayavi
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Bool, Enum, Tuple, Range
from enthought.traits.ui.api import View, Group, Item, RGBColorEditor
from enthought.preferences.ui.api import PreferencesPage

################################################################################
# `MayaviRootPreferencesPage` class
################################################################################
class MayaviRootPreferencesPage(PreferencesPage):
    """ Preferences page for Mayavi. """

    #### 'PreferencesPage' interface ##########################################

    # The page's category (e.g. 'General/Appearance'). The empty string means
    # that this is a top-level page.
    category = ''

    # The page's help identifier (optional). If a help Id *is* provided then
    # there will be a 'Help' button shown on the preference page.
    help_id = ''

    # The page name (this is what is shown in the preferences dialog.
    name = 'Mayavi'

    # The path to the preferences node that contains the preferences.
    preferences_path = 'enthought.mayavi'

    #### Preferences ##########################################################

    # Specifies if the nodes on the tree may be deleted without a
    # confirmation or not.  If True the user will be prompted before
    # the object is deleted.  If it is False then the user will not be
    # prompted.
    confirm_delete = Bool(desc='if the user is prompted before'
                          ' a node on the MayaVi tree is deleted')

    #### Traits UI views ######################################################

    traits_view = View(Group(Item(name='confirm_delete'),
                            )
                       )


################################################################################
# `MayaviMlabPreferencesPage` class
################################################################################
class MayaviMlabPreferencesPage(PreferencesPage):
    """ Preferences page for Mayavi. """

    #### 'PreferencesPage' interface ##########################################

    # The page's category (e.g. 'General/Appearance'). The empty string means
    # that this is a top-level page.
    category = 'Mayavi'

    # The page's help identifier (optional). If a help Id *is* provided then
    # there will be a 'Help' button shown on the preference page.
    help_id = ''

    # The page name (this is what is shown in the preferences dialog.
    name = 'Mlab'

    # The path to the preferences node that contains the preferences.
    preferences_path = 'enthought.mayavi.mlab'

    #### Preferences ##########################################################

    # The mlab backend to use.  
    backend = Enum('auto', 'envisage', 'simple', 
                   desc='the mlab backend to use')

    # The background color of the renderer.
    background_color = Tuple(Range(0., 1.), Range(0., 1.), Range(0., 1.),
                             editor=RGBColorEditor,
                             desc='the background color of the scene')

    # The foreground color of the renderer.
    foreground_color = Tuple(Range(0., 1.), Range(0., 1.), Range(0., 1.),
                             editor=RGBColorEditor,
                             desc='the foreground color of the scene')

    ######################################################################
    # Traits UI view.

    traits_view = View(Group(
                             Item(name='backend'),
                             Item(name='background_color'),
                             Item(name='foreground_color'),
                             ),
                       resizable=True
                      )

