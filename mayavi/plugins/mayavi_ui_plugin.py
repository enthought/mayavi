"""The Mayavi UI plugin
"""
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports.
import logging

# Enthought library imports.
from traits.api import List, on_trait_change
from envisage.api import Plugin
from pyface.workbench.api import Perspective, PerspectiveItem
from traits.etsconfig.api import ETSConfig

logger = logging.getLogger()

# View IDs.
ENGINE_VIEW = 'mayavi.core.ui.engine_view.EngineView'
CURRENT_SELECTION_VIEW = 'mayavi.core.engine.Engine.current_selection'
SHELL_VIEW = 'envisage.plugins.python_shell_view'
LOGGER_VIEW = 'apptools.logger.plugin.view.logger_view.LoggerView'

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

    # The contents of the perspective.
    contents = List()

    def _contents_default(self):
        contents = [
            PerspectiveItem(id=ENGINE_VIEW, position='left'),
            PerspectiveItem(id=CURRENT_SELECTION_VIEW, position='bottom',
                            relative_to=ENGINE_VIEW),
            PerspectiveItem(id=SHELL_VIEW, position='bottom'),
        ]
        show_logger = True
        if ETSConfig.toolkit == 'wx':
            # XXX: Bugware: avoid a crash in Wx with the logger
            import wx
            if wx.__version__.split('.')[:2] == ['2', '6']:
                show_logger = False

        if show_logger:
            contents.append(PerspectiveItem(id=LOGGER_VIEW, position='with',
                                            relative_to=SHELL_VIEW))
        return contents


###############################################################################
# `MayaviUIPlugin` class.
###############################################################################
class MayaviUIPlugin(Plugin):

    # Extension point Ids.
    VIEWS             = 'envisage.ui.workbench.views'
    PERSPECTIVES      = 'envisage.ui.workbench.perspectives'
    PREFERENCES_PAGES = 'envisage.ui.workbench.preferences_pages'
    ACTION_SETS       = 'envisage.ui.workbench.action_sets'
    BANNER            = 'envisage.plugins.ipython_shell.banner'


    # The plugins name.
    name = 'Mayavi UI plugin'

    # Our ID.
    id = 'mayavi_ui'

    ###### Contributions to extension points made by this plugin ######

    # Views.
    views = List(contributes_to=VIEWS)

    # Perspectives.
    perspectives = List(contributes_to=PERSPECTIVES)

    # Preferences pages.
    preferences_pages = List(contributes_to=PREFERENCES_PAGES)

    # Our action sets.
    action_sets = List(contributes_to=ACTION_SETS)

    # IPython banner
    banner = List(contributes_to=BANNER)

    def _views_default(self):
        """ Trait initializer. """
        return [self._engine_view_factory,
                self._current_selection_view_factory]

    def _perspectives_default(self):
        """ Trait initializer. """
        return [MayaviPerspective]

    def _preferences_pages_default(self):
        """ Trait initializer. """
        from mayavi.preferences.mayavi_preferences_page import (
            MayaviRootPreferencesPage, MayaviMlabPreferencesPage)
        return [MayaviRootPreferencesPage, MayaviMlabPreferencesPage]

    def _action_sets_default(self):
        """ Trait initializer. """
        from mayavi.plugins.mayavi_ui_action_set import (
            MayaviUIActionSet
        )
        return [MayaviUIActionSet]

    def _banner_default(self):
        """Trait initializer """
        return ["""Welcome to Mayavi, this is the interactive IPython shell.

If this is your first time using Mayavi, take a quick look at the tutorial examples section of the user guide, accessible via the help menu.
To use Mayavi, you need to load your data in "data sources" and apply "visualization modules" to it.
"""]

    ######################################################################
    # Private methods.
    def _engine_view_factory(self, window, **traits):
        """ Factory method for engine views. """
        from pyface.workbench.traits_ui_view import \
                TraitsUIView
        from mayavi.core.ui.engine_view import \
                            EngineView

        engine_view = EngineView(engine=self._get_engine(window))
        tui_engine_view = TraitsUIView(obj=engine_view,
                                       id=ENGINE_VIEW,
                                       name='Mayavi',
                                       window=window,
                                       position='left',
                                       **traits
                                       )
        return tui_engine_view

    def _current_selection_view_factory(self, window, **traits):
        """ Factory method for the current selection of the engine. """

        from pyface.workbench.traits_ui_view import \
                TraitsUIView

        engine = self._get_engine(window)
        tui_engine_view = TraitsUIView(obj=engine,
                                       view='current_selection_view',
                                       id=CURRENT_SELECTION_VIEW,
                                       name='Mayavi object editor',
                                       window=window,
                                       position='bottom',
                                       relative_to=ENGINE_VIEW,
                                       **traits
                                       )
        return tui_engine_view

    def _get_engine(self, window):
        """Return the Mayavi engine of the particular window."""
        from mayavi.core.engine import Engine
        return window.get_service(Engine)

    def _get_script(self, window):
        """Return the `mayavi.plugins.script.Script` instance
        of the window."""
        from mayavi.plugins.script import Script
        return window.get_service(Script)

    ######################################################################
    # Trait handlers.
    @on_trait_change('application.gui:started')
    def _on_application_gui_started(self, obj, trait_name, old, new):
        """This is called when the application's GUI is started.  The
        method binds the `Script` and `Engine` instance on the
        interpreter.
        """
        # This is called when the application trait is set but we don't
        # want to do anything at that point.
        if trait_name != 'started' or not new:
            return

        # Get the script service.
        app = self.application
        window = app.workbench.active_window
        script = self._get_script(window)

        # Get a hold of the Python shell view.
        id = SHELL_VIEW
        py = window.get_view_by_id(id)
        if py is None:
            logger.warn('*'*80)
            logger.warn("Can't find the Python shell view to bind variables")
            return

        # Bind the script and engine instances to names on the
        # interpreter.
        try:
            py.bind('mayavi', script)
            py.bind('engine', script.engine)
            try:
                # The following will fail under Qt, as it needs the Pyface
                # Tree that has not been ported from Wx yet.
                from apptools.naming.ui.api import explore
                py.bind('explore', explore)
            except ImportError:
                pass
        except AttributeError as msg:
            # This can happen when the shell is not visible.
            # FIXME: fix this when the shell plugin is improved.
            logger.warn(msg)
            logger.warn("Can't find the Python shell to bind variables")
