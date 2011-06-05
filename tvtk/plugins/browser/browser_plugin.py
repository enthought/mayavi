""" The TVTK pipeline browser plugin. """


# Enthought library imports.
from envisage.api import Plugin
from traits.api import List


class BrowserPlugin(Plugin):
    """ The TVTK pipeline browser plugin. """

    # Extension point Ids.
    VIEWS = 'envisage.ui.workbench.views'

    #### 'IPlugin' interface ##################################################

    # The plugin's name (suitable for displaying to the user).
    name = 'TVTK Pipeline Browser'

    # Our ID.
    id = 'tvtk.browser'

    #### Extension points offered by this plugin ##############################

    # None.

    #### Contributions to extension points made by this plugin ################

    views = List(contributes_to=VIEWS)

    def _views_default(self):
        """ Trait initializer. """

        return [self._browser_view_factory]

    ###########################################################################
    # Private interface.
    ###########################################################################

    def _browser_view_factory(self, window, **traits):
        """ Factory method for browser views. """

        from tvtk.plugins.browser.browser_view import (
            BrowserView
        )

        browser_view = BrowserView(
            scene_manager = self._get_scene_manager(window),
            window        = window,
            **traits
        )

        return browser_view

    def _get_scene_manager(self, window):
        """ Lookup the window's scene manager service. """

        # Get the scene manager (a 'per window' service, so we look it up via
        # the window!).
        from tvtk.plugins.scene.i_scene_manager import (
            ISceneManager
        )

        return window.get_service(ISceneManager)

#### EOF ######################################################################
