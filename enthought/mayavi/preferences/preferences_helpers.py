"""Various preference helpers for the mayavi preferences.
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports
from enthought.traits.api import Bool
from enthought.traits.ui.api import View, Group, Item
from enthought.preferences.api import PreferencesHelper

################################################################################
# `RootPreferencesHelper` class
################################################################################
class RootPreferencesHelper(PreferencesHelper):

    # The preferences path for which we use.
    preferences_path = 'enthought.mayavi'

    ######################################################################
    # Our preferences.

    # Specifies if the nodes on the tree may be deleted without a
    # confirmation or not.  If True the user will be prompted before
    # the object is deleted.  If it is False then the user will not be
    # prompted.
    confirm_delete = Bool(desc='if the user is prompted before'
                          ' a node on the MayaVi tree is deleted')

    ######################################################################
    # Traits UI view.

    traits_view = View(Group(
                             Item(name='confirm_delete'),
                             ),
                       resizable=True
                      )

