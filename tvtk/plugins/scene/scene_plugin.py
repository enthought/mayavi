""" The TVTK render window scene plugin. """


# Enthought library imports.
from envisage.api import Plugin, ServiceOffer
from traits.api import List


# This module's package.
PKG = '.'.join(__name__.split('.')[:-1])


class ScenePlugin(Plugin):
    """ The TVTK render window scene plugin. """

    # Extension point Ids.
    PREFERENCES    = 'envisage.preferences'
    SERVICE_OFFERS = 'envisage.ui.workbench.service_offers'

    #### 'IPlugin' interface ##################################################

    # The plugin's name (suitable for displaying to the user).
    name = 'TVTK Scene Plugin'

    # Our ID.
    id = 'tvtk.scene'

    #### Extension points offered by this plugin ##############################

    # None.

    #### Contributions to extension points made by this plugin ################

    preferences = List(contributes_to=PREFERENCES)

    def _preferences_default(self):
        """ Trait initializer. """

        return ['pkgfile://%s/preferences.ini' % PKG]

    service_offers = List(contributes_to=SERVICE_OFFERS)

    def _service_offers_default(self):
        """ Trait initializer. """

        scene_manager_service_offer = ServiceOffer(
            protocol = PKG + '.i_scene_manager.ISceneManager',
            factory  = PKG + '.scene_manager.SceneManager',
        )

        return [scene_manager_service_offer]

#### EOF ######################################################################
