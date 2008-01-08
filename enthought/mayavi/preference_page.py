"""The preference page for the MayaVi preferences.

"""
# Author: Prabhu Ramachandran <prabhu@aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.workbench.preference import WorkbenchPreferencePage
from enthought.traits.api import Bool
from enthought.traits.ui.api import View, Group, Item

# Local imports.
from enthought.mayavi.services import IMAYAVI_ENGINE

##############################################################################
# `MayaviPreferencePage` class.
##############################################################################
class MayaviPreferencePage(WorkbenchPreferencePage):

    # Specifies if the nodes on the tree may be deleted without a
    # confirmation or not.  If True the user will be prompted before
    # the object is deleted.  If it is False then the user will not be
    # prompted.
    confirm_delete = Bool(True, desc='if the user is prompted before'
                          ' a node on the MayaVi tree is deleted')

    traits_view = View(Item(name='confirm_delete'),
                       )

    ###########################################################################
    # Protected 'WorkbenchPreferencePage' interface.
    ###########################################################################
    def _get_preferences(self):
        """ Returns the preferences that this page is editing. """
        app = self._application
        engine = app.get_service(IMAYAVI_ENGINE)
        return engine.preference_manager.preferences

