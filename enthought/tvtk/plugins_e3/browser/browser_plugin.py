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
        
        return [self._create_browser_view]

    #### Services offered by this plugin ######################################

    browser_manager = Instance(
        'enthought.tvtk.plugins_e3.browser.browser_manager.BrowserManager',
        service=True
    )

    def _browser_manager_default(self):
        """ Trait initializer. """

        from enthought.tvtk.plugins_e3.browser.browser_manager import (
            BrowserManager
        )
        
        return BrowserManager()

    ###########################################################################
    # Private interface.
    ###########################################################################

    def _create_browser_view(self, **traits):
        """ Factory method for browser views. """
        
        from enthought.tvtk.plugins_e3.browser.browser_view import (
            BrowserView
        )

        browser_manager = self.application.get_service(
            'enthought.tvtk.plugins_e3.browser.browser_manager.BrowserManager'
        )

        return BrowserView(browser_manager=browser_manager, **traits)

#### EOF ######################################################################
