"""The Mayavi UI plugin
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.


from enthought.traits.api import List
from enthought.envisage.api import Plugin
from enthought.pyface.workbench.api import Perspective, PerspectiveItem

# This module's package.
PKG = '.'.join(__name__.split('.')[:-1])

###############################################################################
# `MayaviPerspective` class.
###############################################################################
class MayaviPerspective(Perspective):
    """ A default perspective for Mayavi. """

    # The perspective's name.
    name = 'Mayavi'

    # Should this perspective be enabled or not?
    enabled = True

    # Should the editor area be shown in this perspective?
    show_editor_area = True

    # View IDs.
    ENGINE_VIEW = PKG + '.engine_view.EngineView'
    CURRENT_SELECTION_VIEW = PKG + '.current_selection'
    SHELL_VIEW = 'enthought.plugins.python_shell.view.python_shell_view.PythonShellView'

    # The contents of the perspective.
    contents = [
        PerspectiveItem(id=ENGINE_VIEW, position='left'),
        PerspectiveItem(id=CURRENT_SELECTION_VIEW, position='bottom',
                        relative_to=ENGINE_VIEW),
        PerspectiveItem(id=SHELL_VIEW, position='bottom')
    ]

###############################################################################
# `MayaviUIPlugin` class.
###############################################################################
class MayaviUIPlugin(Plugin):

    # Extension point Ids.
    VIEWS             = 'enthought.envisage.ui.workbench.views'
    PERSPECTIVES      = 'enthought.envisage.ui.workbench.perspectives'
    PREFERENCES_PAGES = 'enthought.envisage.ui.workbench.preferences_pages'
    ACTION_SETS       = 'enthought.envisage.ui.workbench.action_sets'

    # The plugins name.
    name = 'Mayavi UI plugin'

    ###### Contributions to extension points made by this plugin ######

    # Views.
    views = List(contributes_to=VIEWS)

    # Perspectives.
    perspectives = List(contributes_to=PERSPECTIVES)

    # Preferences pages.
    preferences_pages = List(contributes_to=PREFERENCES_PAGES)

    # Our action sets.
    action_sets = List(contributes_to=ACTION_SETS)

    def _views_default(self):
        """ Trait initializer. """
        return [self._engine_view_factory,
                self._current_selection_view_factory]

    def _perspectives_default(self):
        """ Trait initializer. """
        return [MayaviPerspective]

    def _preferences_pages_default(self):
        """ Trait initializer. """
        from enthought.mayavi.preferences.mayavi_preferences_page import \
            MayaviPreferencesPage
        return [MayaviPreferencesPage]

    def _action_sets_default(self):
        """ Trait initializer. """
        from enthought.mayavi.plugins_e3.mayavi_ui_action_set import (
            MayaviUIActionSet
        )
        return [MayaviUIActionSet]


    ######################################################################
    # Private methods.
    def _engine_view_factory(self, window, **traits):
        """ Factory method for engine views. """
        from enthought.pyface.workbench.traits_ui_view import \
                TraitsUIView
        from enthought.mayavi.plugins_e3.engine_view import \
                            EngineView

        engine_view = EngineView(engine=self._get_engine(window))
        tui_engine_view = TraitsUIView(obj=engine_view,
                                       id=PKG + '.engine_view.EngineView',
                                       name='Mayavi',
                                       window=window,
                                       position='left',
                                       **traits
                                       )
        return tui_engine_view
    
    def _current_selection_view_factory(self, window, **traits):
        """ Factory method for the current selection of the engine. """

        from enthought.pyface.workbench.traits_ui_view import \
                TraitsUIView

        engine = self._get_engine(window)
        tui_engine_view = TraitsUIView(obj=engine,
                                       view='current_selection_view',
                                       id=PKG + '.current_selection',
                                       name='Mayavi object editor',
                                       window=window,
                                       position='bottom',
                                       relative_to=PKG + '.engine_view.EngineView',
                                       **traits
                                       )
        return tui_engine_view

    def _get_engine(self, window):
        """Return the Mayavi engine of the particular window."""
        from enthought.mayavi.engine import Engine
        return window.get_service(Engine)
