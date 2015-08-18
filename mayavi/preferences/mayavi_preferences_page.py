"""Preferences for Mayavi
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import (Bool, Enum, Tuple, Range, List,
        Str, Instance, HasTraits)
from traitsui.api import View, Group, Item, RGBColorEditor
from apptools.preferences.ui.api import PreferencesPage

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
    preferences_path = 'mayavi'

    #### Preferences ##########################################################

    # Specifies if the nodes on the tree may be deleted without a
    # confirmation or not.  If True the user will be prompted before
    # the object is deleted.  If it is False then the user will not be
    # prompted.
    confirm_delete = Bool(desc='if the user is prompted before'
                          ' a node on the MayaVi tree is deleted')

    # Specifies if the splash screen is shown when mayavi starts.
    show_splash_screen = Bool(desc='if the splash screen is shown at'
                              ' startup')

    # Specifies if the adder nodes are shown on the mayavi tree view.
    show_helper_nodes = Bool(desc='if the helper (adder) nodes are shown'
                             ' on the tree view')

    # Specifies if the adder nodes are shown on the mayavi tree view.
    open_help_in_light_browser = Bool(
                    desc='if the help pages are opened in a chromeless'
                             'browser window (only works with Firefox')

    # Contrib directories to load on startup.
    contrib_packages = List(Str, desc='contrib packages to load on startup')

    # Whether or not to use IPython for the Shell.
    use_ipython = Bool(desc='use IPython for the embedded shell '
                            '(if available)')

    ########################################
    # Private traits.
    _contrib_finder = Instance(HasTraits)

    #### Traits UI views ######################################################

    traits_view = View(
                    Group(
                        Group(
                            Item(name='confirm_delete'),
                            Item(name='show_splash_screen'),
                            Item(name='show_helper_nodes'),
                            Item(name='open_help_in_light_browser'),
                            Item(name='use_ipython'),
                            label='General settings',
                            show_border=True,
                            ),
                        Group(
                            Group(
                                Item('_contrib_finder',
                                     style='custom',
                                     show_label=False,
                                     resizable=True,
                                     ),
                                ),
                            label='Contribution settings',
                            show_border=True,
                            ),
                        ),
                    resizable=True
                    )

    ######################################################################
    # Non-public interface.
    ######################################################################
    def __contrib_finder_default(self):
        from .contrib_finder import ContribFinder
        return ContribFinder()


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
    preferences_path = 'mayavi.mlab'

    #### Preferences ##########################################################

    # The mlab backend to use.
    backend = Enum('auto', 'envisage', 'simple', 'test',
                   desc='the mlab backend to use')

    # The background color of the renderer.
    background_color = Tuple(Range(0., 1., 1.),
                             Range(0., 1., 1.),
                             Range(0., 1., 1.),
                             editor=RGBColorEditor,
                             desc='the background color of the scene')

    # The foreground color of the renderer.
    foreground_color = Tuple(Range(0., 1., 0.),
                             Range(0., 1., 0.),
                             Range(0., 1., 0.),
                             editor=RGBColorEditor,
                             desc='the foreground color of the scene')

    # Offscreen rendering.
    offscreen = Bool(desc='if mlab should use offscreen rendering'
                          ' (no window will show up in this case)')


    ######################################################################
    # Traits UI view.

    traits_view = View(Group(
                             Item('backend'),
                             Item('background_color'),
                             Item('foreground_color'),
                             Item('offscreen'),
                             ),
                       resizable=True
                      )
