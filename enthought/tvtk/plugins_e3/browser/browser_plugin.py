""" The TVTK pipeline browser plugin. """


# Enthought library imports.
from enthought.envisage.api import Plugin
from enthought.traits.api import List, Instance


class BrowserPlugin(Plugin):
    """ The TVTK pipeline browser plugin. """

    # Extension point Ids.
    VIEWS = 'enthought.envisage.ui.workbench.views'
    
    #### 'IPlugin' interface ##################################################

    # The plugin's name (suitable for displaying to the user).
    name = 'TVTK Pipeline Browser'

    #### Extension points offered by this plugin ##############################

    # None.

    #### Contributions to extension points made by this plugin ################

    views = List(contributes_to=VIEWS)

    def _views_default(self):
        """ Trait initializer. """
        
        return [self._browser_view_factory]

    #### Services offered by this plugin ######################################

    # None.

    ###########################################################################
    # Private interface.
    ###########################################################################

    def _browser_view_factory(self, **traits):
        """ Factory method for browser views. """

        from enthought.tvtk.plugins_e3.browser.browser_view import (
            BrowserView
        )

        scene_manager = self.application.get_service(
            'enthought.tvtk.plugins_e3.scene.scene_manager.SceneManager'
        )

        return BrowserView(scene_manager=scene_manager, **traits)

#### EOF ######################################################################
