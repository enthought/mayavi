# Enthought library imports.
from traits.api import Callable, Instance, List, Str, on_trait_change
from envisage.api import Plugin
from envisage.ui.tasks.api import TaskWindow
from pyface.tasks.api import Splitter, Tabbed, Task, TaskLayout, PaneItem
from pyface.action.api import StatusBarManager
from pyface.tasks.action.api import MenuBarSchema, ToolBarSchema, SchemaAddition
from pyface.tasks.contrib.python_shell import PythonShellPane
from pyface.tasks.api import AdvancedEditorAreaPane
from mayavi.core.ui.python_shell_dock_pane import PythonShellDockPane
from mayavi.core.ui.logger_dock_pane import LoggerDockPane

#from mayavi.plugins.mayavi_ui_menu_bar import mayavi_ui_menu_bar

from mayavi.core.ui.engine_dock_pane import EngineDockPane
from mayavi.core.ui.current_selection_dock_pane import CurrentSelectionDockPane

from pyface.tasks.api import TaskPane


from pyface.tasks.action.api import SGroup, SMenu, SMenuBar, TaskAction
from pyface.tasks.action.api import DockPaneToggleGroup

from mayavi.action.filters import *
from mayavi.action.help import *
from mayavi.action.modules import *
from mayavi.action.save_load import *
from mayavi.action.sources import *

from mayavi.core.registry import registry


###############################################################################
# `MayaviPerspective` class.
###############################################################################
class MayaviTask(Task):

    """ A collection of pane, menu, tool bar, and status bar factories.

    The central class in the Tasks plugin, a Task is responsible for
    describing a set of user interface elements, as well as mediating between
    its view (a TaskWindow) and an application-specific model.
    """

    # The task's identifier.
    id = "mayavi.task"

    # The task's user-visible name.
    name = "Mayavi Task"

    # The (optional) status bar for the task.
    status_bar = Instance(StatusBarManager)

    # The list of tool bars for the tasks.
    tool_bars = List(ToolBarSchema)

    # A list of extra actions, groups, and menus that are inserted into menu
    # bars and tool bars constructed from the above schemas.
    extra_actions = List(SchemaAddition)

    # The menu bar for the task.
    def _menu_bar_default(self):

        SOURCE_ACTIONS = []
        for src in registry.sources:
            if len(src.extensions) == 0:
                action = globals()[src.id]
                SOURCE_ACTIONS.append(action(name=src.menu_name))

        MODULE_ACTIONS = []
        for module in registry.modules:
            action = globals()[module.id]
            MODULE_ACTIONS.append(action(name=module.menu_name))

        FILTER_ACTIONS = []
        for filter in registry.filters:
            action = globals()[filter.id]
            FILTER_ACTIONS.append(action(name=filter.menu_name))

        mayavi_ui_menu_bar = SMenuBar(
            SMenu(
                SGroup(
                    SMenu(
                        OpenFile(
                            id="OpenFile",
                            name="&Open file ...",
                            application=self.window.application
                        ),
                        *SOURCE_ACTIONS,
                        id='',
                        name='&Load data'
                    ),
                    SaveVisualization(
                        id="SaveVisualization",
                        name="&Save Visualization",
                    ),
                    LoadVisualization(
                        id="LoadVisualization",
                        name="&Load Visualization",
                    ),
                    RunScript(
                        id="RunScript",
                        name="&Run Python Script",
                    ),
                    id="MayaviFileGroup"
                ),
                id='File',
                name='&File'
            ),
            SMenu(
                SMenu(
                    *MODULE_ACTIONS,
                    id='Modules',
                    name='&Modules'
                ),
                SMenu(
                    *FILTER_ACTIONS,
                    id='Filters',
                    name='&Filters'
                ),
                AddModuleManager(
                    id="AddModuleManager",
                    name="&Add ModuleManager",
                    application=self.window.application,
                ),
                id='Visualize',
                name='&Visualize'
            ),
            # This should be included by default, but without this it is not
            # showing up...
            SMenu(
                id='View',
                name='&View'  
            ),
            # likewise this allows us to see preferences under the "Python" tab
            # of the menu bar, although it should be included by default...
            SMenu(
                id='Edit',
                name='&Edit'
            ),
            SMenu(
                HelpIndex(name="&User Guide"),
                TVTKClassBrowser(name="&VTK Class Browser"),
                id='Help',
                name='&Help'
            )
        )

        return mayavi_ui_menu_bar

    def _default_layout_default(self):
        return TaskLayout(
            left=Splitter(
                PaneItem('engine_pane'),
                PaneItem('current_selection_dock_pane'),
                orientation='vertical'
            ),
            bottom=Tabbed(
                PaneItem('python_shell_dock_pane'),
                PaneItem('logger_dock_pane')
            )
        )

    # ------------------------------------------------------------------------
    # 'Task' interface.
    # ------------------------------------------------------------------------

    def activated(self):
        """ Called after the task has been activated in a TaskWindow.
        """
        pass

    def create_central_pane(self):
        """ Create and return the central pane, which must implement ITaskPane.
        """
        return AdvancedEditorAreaPane()

    def create_dock_panes(self):
        """ Create and return the task's dock panes (IDockPane instances).

        This method is called *after* create_central_pane() when the task is
        added to a TaskWindow.
        """
        return [
            EngineDockPane(),
            CurrentSelectionDockPane(),
            PythonShellDockPane(),
            LoggerDockPane()
        ]

    def initialized(self):
        """ Called when the task is about to be activated in a TaskWindow for
        the first time.

        Override this method to perform any initialization that requires the
        Task's panes to be instantiated. Note that this method, when called, is
        called before activated().
        """
        pass

    def prepare_destroy(self):
        """ Called when the task is about to be removed from its TaskWindow.

        Override this method to perform any cleanup before the task's controls
        are destroyed.
        """
        pass

###############################################################################
# `MayaviUITasksPlugin` class.
###############################################################################
class MayaviUITasksPlugin(Plugin):

    # Extension point Ids.
    PREFERENCES_CATEGORIES = "envisage.ui.tasks.preferences_categories"
    PREFERENCES_PANES = "envisage.ui.tasks.preferences_panes"
    TASKS = "envisage.ui.tasks.tasks"
    TASK_EXTENSIONS = "envisage.ui.tasks.task_extensions"

    # The plugins name.
    name = 'Mayavi UI plugin'

    # Our ID.
    id = 'mayavi_ui'

    ###### Contributions to extension points made by this plugin ######

    # Tasks.
    tasks = List(contributes_to=TASKS)

    def _tasks_default(self):
        from envisage.ui.tasks.api import TaskFactory
        return [
            TaskFactory(
                id="mayavi.task",
                name='Mayavi UI Task',
                factory=MayaviTask
            )
        ]

    # Task Extensions.
    tasks_extensions = List(contributes_to=TASK_EXTENSIONS)

    # Preferences categories.
    preferences_categories = List(contributes_to=PREFERENCES_CATEGORIES)

    def _preferences_categories_default(self):
        from envisage.ui.tasks.api import PreferencesCategory
        return [
            PreferencesCategory(
                id='Mayavi',
            ),
            PreferencesCategory(
                id='TVTK',
            )
        ]

    # Preference Panes.
    preferences_panes = List(contributes_to=PREFERENCES_PANES)
    def _preferences_panes_default(self):
        from mayavi.preferences.mayavi_preferences_pane import (
            MayaviRootPreferencesPane, MayaviMlabPreferencesPane)
        return [MayaviRootPreferencesPane, MayaviMlabPreferencesPane]
