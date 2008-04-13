""" The TVTK render window scene plugin. """


# Enthought library imports.
from enthought.envisage.api import Plugin
from enthought.traits.api import List


class ScenePlugin(Plugin):
    """ The TVTK render window scene plugin. """

    # Extension point Ids.
    PREFERENCES = 'enthought.envisage.preferences'
    
    #### 'IPlugin' interface ##################################################

    # The plugin's name (suitable for displaying to the user).
    name = 'TVTK Scene Plugin'

    #### Extension points offered by this plugin ##############################

    # None.

    #### Contributions to extension points made by this plugin ################

    preferences = List(contributes_to=PREFERENCES)

    def _preferences_default(self):
        """ Trait initializer. """

        return ['pkgfile://enthought.tvtk.plugins_e3.scene/preferences.ini']

    #### Services offered by this plugin ######################################

    # This plugin creates a 'SceneManager' service per top-level workbench
    # window.

    ###########################################################################
    # Private interface.
    ###########################################################################

    #### Trait change handlers ################################################

    def _application_changed(self, old, new):
        """ Static trait change handler. """

        if old is not None:
            old.on_trait_change(
                self._on_application_started, 'started', remove=True
            )

        if new is not None:
            new.on_trait_change(
                self._on_application_started, 'started'
            )

        return
    
    def _on_application_started(self):
        """ Dynamic trait change handler. """

        # Listen for windows opening so that we can create a scene manager for
        # each window.
        #
        # fixme: Currently we have to listen for 'opening' events (and not
        # 'opened'), because any views that need services will get created
        # before the 'opened' event is fired!
        self.application.workbench.on_trait_change(
            self._on_window_opening, 'window_opening'
        )

        return
    
    def _on_window_opening(self, event):
        """ Dynamic trait change handler. """

        # Register a scene manager for the window.
        self.application.register_service(
            'enthought.tvtk.plugins_e3.scene.scene_manager.SceneManager',
            self._scene_manager_factory, properties={'window' : event.window}
        )

        return

    #### Methods ##############################################################
    
    def _scene_manager_factory(self, protocol, properties):
        """ Factory method for creating scene managers. """

        from enthought.tvtk.plugins_e3.scene.scene_manager import SceneManager
        
        return SceneManager(**properties)

#### EOF ######################################################################
