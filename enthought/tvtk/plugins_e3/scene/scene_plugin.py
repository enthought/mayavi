""" The TVTK render window scene plugin. """


# Enthought library imports.
from enthought.envisage.api import Plugin, ServiceOffer
from enthought.traits.api import List


# This module's package.
PKG = '.'.join(__name__.split('.')[:-1])


class ScenePlugin(Plugin):
    """ The TVTK render window scene plugin. """

    # Extension point Ids.
    PREFERENCES = 'enthought.envisage.preferences'
    SERVICES    = 'enthought.envisage.services'
    
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

    services = List(contributes_to=SERVICES)

    def _services_default(self):
        """ Trait initializer. """

        scene_manager_service = ServiceOffer(
            protocol = '%s.i_scene_manager.ISceneManager' % PKG,
            factory  = '%s.scene_manager.SceneManager' % PKG,
            scope    = 'window'
        )

        return [scene_manager_service]

#### EOF ######################################################################
