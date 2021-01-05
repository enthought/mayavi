""" A TVTK render window scene UI plugin. """


# Enthought library imports.
from envisage.api import Plugin
from traits.api import List

from pyface.tasks.action.api import SGroup, SMenu, SMenuBar, TaskAction

from tvtk.plugins.scene.ui.actions import *

class SceneUIPlugin(Plugin):
    """ A TVTK render window scene UI plugin.

    This is the plugin that contributes actions, menus, preferences pages
    etc.

    """

    # Extension point Ids.
    #PREFERENCES_PAGES = 'envisage.ui.workbench.preferences_pages'
    PREFERENCES_CATEGORIES = "envisage.ui.tasks.preferences_categories"
    PREFERENCES_PANES = "envisage.ui.tasks.preferences_panes"
    TASK_EXTENSIONS = "envisage.ui.tasks.task_extensions"

    #### 'IPlugin' interface ##################################################

    # The plugin's name (suitable for displaying to the user).
    name = 'TVTK Scene UI Plugin'

    # Our ID.
    id = 'tvtk.scene_ui'

    #### Extension points offered by this plugin ##############################

    # None.

    #### Contributions to extension points made by this plugin ################

    task_extensions = List(contributes_to=TASK_EXTENSIONS)

    def _task_extensions_default(self):
        """ Trait initializer. """
        from envisage.ui.tasks.api import TaskExtension
        from pyface.tasks.action.api import SchemaAddition

        app = self.application

        def tools_menu_factory(): 
            return SMenu(
                SGroup(
                    ResetZoom(application=app),
                    IsometricView(application=app),
                    XPlusView(application=app),
                    XMinusView(application=app),
                    YPlusView(application=app),
                    YMinusView(application=app),
                    ZPlusView(application=app),
                    ZMinusView(application=app),
                    id='TVTKViewGroup'
                ),
                id='Tools',
                name='&Tools'
            )

        tools_menu_schema_adition = SchemaAddition(
            factory=tools_menu_factory,
            before='Help',
            after='View',
            path='MenuBar'
        )

        def scene_group_factory():
            return SGroup(
                SMenu(
                    NewScene(application=app),
                    id='New',
                    name='&New'
                ),
                SMenu(
                    SaveSceneToPNG(application=app),
                    SaveSceneToJPEG(application=app),
                    SaveSceneToBMP(application=app),
                    SaveSceneToTIFF(application=app),
                    SaveSceneToPS(application=app),
                    SaveSceneToGL2PS(application=app),
                    SaveSceneToRIB(application=app),
                    SaveSceneToOOGL(application=app),
                    SaveSceneToIV(application=app),
                    SaveSceneToVRML(application=app),
                    SaveSceneToOBJ(application=app),
                    SaveSceneToPovray(application=app),
                    SaveSceneToX3D(application=app),
                    id='SaveSceneAs',
                    name='Sa&ve Scene As'
                ),
                SaveScene(application=app),
                id='TVTKSceneGroup'
            )

        scene_group_schema_addition = SchemaAddition(
            factory=scene_group_factory,
            path='MenuBar/File'
        )

        return [
            TaskExtension(
                task_id='mayavi.task',
                actions=[
                    scene_group_schema_addition,
                    tools_menu_schema_adition
                ],
            )
        ]

    preferences_categories = List(contributes_to=PREFERENCES_CATEGORIES)

    def _preferences_categories_default(self):
        from envisage.ui.tasks.api import PreferencesCategory
        return [
            PreferencesCategory(
                id='TVTK',
            )
        ]

    preferences_panes = List(contributes_to=PREFERENCES_PANES)

    def _preferences_panes_default(self):
        """ Trait initializer. """

        from tvtk.plugins.scene.ui.scene_preferences_pane import (
            ScenePreferencesPane
        )

        return [ScenePreferencesPane]

#### EOF ######################################################################
