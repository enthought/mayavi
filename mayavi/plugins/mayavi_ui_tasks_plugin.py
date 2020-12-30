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



from mayavi.core.ui.engine_dock_pane import EngineDockPane
from mayavi.core.ui.current_selection_dock_pane import CurrentSelectionDockPane

from pyface.tasks.api import TaskPane
class DumbPane(TaskPane):
    id = 'dumb_pane'
    name = 'Dumb Pane'




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


    # Actions -------------------------------------------------------------#

    # The menu bar for the task.
    menu_bar = Instance(MenuBarSchema)

    # The (optional) status bar for the task.
    status_bar = Instance(StatusBarManager)

    # The list of tool bars for the tasks.
    tool_bars = List(ToolBarSchema)

    # A list of extra actions, groups, and menus that are inserted into menu
    # bars and tool bars constructed from the above schemas.
    extra_actions = List(SchemaAddition)


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
        #DumbPane(task=self)

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

    # Views.
    tasks = List(contributes_to=TASKS)

    # Perspectives.
    tasks_extensions = List(contributes_to=TASK_EXTENSIONS)

    # Preferences pages.
    preferences_categories = List(contributes_to=PREFERENCES_CATEGORIES)

    # Our action sets.
    preferences_panes = List(contributes_to=PREFERENCES_PANES)

    def _tasks_default(self):
        from envisage.ui.tasks.api import TaskFactory
        return [
            TaskFactory(
                id="mayavi.task",
                name='Mayavi UI Task',
                factory=MayaviTask
            )
        ]

    