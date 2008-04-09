""" The TVTK render window scene plugin. """


# Enthought library imports.
from enthought.envisage.api import Plugin
from enthought.traits.api import List, Instance


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

    scene_manager = Instance(
        'enthought.tvtk.plugins_e3.scene.scene_manager.SceneManager',
        service=True
    )

    def _scene_manager_default(self):
        """ Trait initializer. """

        from enthought.tvtk.plugins_e3.scene.scene_manager import SceneManager
        
        return SceneManager()

#### EOF ######################################################################
