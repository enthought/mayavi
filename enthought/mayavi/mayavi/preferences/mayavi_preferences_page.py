"""Preferences for Mayavi
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.preferences.ui.api import PreferencesPage
from enthought.traits.api import Bool
from enthought.traits.ui.api import View, Group, Item

################################################################################
# `MayaviPreferencesPage` class
################################################################################
class MayaviPreferencesPage(PreferencesPage):
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

