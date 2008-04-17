""" The TVTK render window scene plugin. """


# Enthought library imports.
from enthought.envisage.api import Plugin, ServiceFactory
from enthought.traits.api import List


# This module's package.
PKG = '.'.join(__name__.split('.')[:-1])


class ScenePlugin(Plugin):
    """ The TVTK render window scene plugin. """

    # Extension point Ids.
    PREFERENCES       = 'enthought.envisage.preferences'
    SERVICE_FACTORIES = 'enthought.envisage.service_factories'
    
    #### 'IPlugin' interface ##################################################

    # The plugin's name (suitable for displaying to the user).
    name = 'TVTK Scene Plugin'

    #### Extension points offered by this plugin ##############################

    # None.

    #### Contributions to extension points made by this plugin ################

    preferences = List(contributes_to=PREFERENCES)
        
    def _preferences_default(self):
        """ Trait initializer. """

        return ['pkgfile://%s/preferences.ini' % PKG]

    service_factories = List(contributes_to=SERVICE_FACTORIES)

    def _service_factories_default(self):
        """ Trait initializer. """

        scene_manager_service_factory = ServiceFactory(
            protocol = PKG + '.i_scene_manager.ISceneManager',
            factory  = PKG + '.scene_manager.SceneManager',
            scope    = 'window'
        )

        return [scene_manager_service_factory]

#### EOF ######################################################################
