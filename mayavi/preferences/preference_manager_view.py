"""
A view for the Mayavi preferences outside of Envisage.
"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Standard library imports
from os.path import join

# Enthought library imports.
from traits.api import List
from apptools.preferences.ui.api import PreferencesManager, \
    PreferencesPage
from pyface.api import ImageResource
from pyface.resource.api import resource_path
from apptools.preferences.ui.preferences_node import PreferencesNode

# Local imports.
from mayavi.preferences.mayavi_preferences_page import \
    MayaviRootPreferencesPage, MayaviMlabPreferencesPage

from mayavi.preferences.preference_manager import \
    preference_manager

################################################################################
# `PreferenceManagerView` class
################################################################################
class PreferenceManagerView(PreferencesManager):
    """ A preference manager UI for Mayavi, to be used outside of
        Envisage.
    """

    # Path used to search for images
    _image_path = [join(resource_path(), 'images'), ]

    # The icon of the dialog
    icon = ImageResource('preferences.ico', search_path=_image_path)

    # The preference pages displayed
    pages = List(PreferencesPage)

    def _pages_default(self):
        return [
                MayaviRootPreferencesPage(
                    preferences=preference_manager.root.preferences),
                MayaviMlabPreferencesPage(
                    preferences=preference_manager.mlab.preferences),
                ]

    def dialog_view(self):
        """ Poor-man's subclassing of view to overload size.
        """
        view = self.trait_view()
        view.width = 0.7
        view.height = 0.5
        view.title = 'Mayavi preferences'
        view.icon = self.icon
        ui = self.edit_traits(
                view=view,
                scrollable=True,
                id='mayavi.preferences.preference_view')
        return ui

    def _get_root(self):
        """ Subclass the root getter, to work outside of envisage, with
            no well-defined root.
        """
        root = PreferencesNode(page=self.pages[0])
        for page in self.pages:
            root.append(PreferencesNode(page=page))
        return root

    def apply(self):
        super(PreferenceManagerView, self).apply()
        for page in self.pages:
            page.preferences.save()


preference_manager_view = PreferenceManagerView()


