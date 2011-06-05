""" A TVTK render window scene UI plugin. """


# Enthought library imports.
from envisage.api import Plugin
from traits.api import List


class SceneUIPlugin(Plugin):
    """ A TVTK render window scene UI plugin.

    This is the plugin that contributes actions, menus, preferences pages
    etc.

    """

    # Extension point Ids.
    ACTION_SETS       = 'envisage.ui.workbench.action_sets'
    PREFERENCES_PAGES = 'envisage.ui.workbench.preferences_pages'

    #### 'IPlugin' interface ##################################################

    # The plugin's name (suitable for displaying to the user).
    name = 'TVTK Scene UI Plugin'

    # Our ID.
    id = 'tvtk.scene_ui'

    #### Extension points offered by this plugin ##############################

    # None.

    #### Contributions to extension points made by this plugin ################

    action_sets = List(contributes_to=ACTION_SETS)

    def _action_sets_default(self):
        """ Trait initializer. """

        from tvtk.plugins.scene.ui.scene_ui_action_set import (
            SceneUIActionSet
        )

        return [SceneUIActionSet]

    preferences_pages = List(contributes_to=PREFERENCES_PAGES)

    def _preferences_pages_default(self):
        """ Trait initializer. """

        from tvtk.plugins.scene.ui.scene_preferences_page import (
            ScenePreferencesPage
        )

        return [ScenePreferencesPage]

#### EOF ######################################################################
