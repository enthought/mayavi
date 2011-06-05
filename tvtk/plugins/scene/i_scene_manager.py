""" The interface for TVTK scene managers. """


# Enthought library imports.
from tvtk.pyface.tvtk_scene import TVTKScene
from pyface.workbench.api import WorkbenchWindow
from traits.api import Interface, List, Instance


class ISceneManager(Interface):
    """ The interface for TVTK scene managerss. """

    # The currently active scene (None, if no scene is active).
    current_scene = Instance(TVTKScene)

    # A list of all open scenes.
    scenes = List(TVTKScene)

    # The workbench window that the manager is in (there is one scene manager
    # per workbench window).
    window = Instance(WorkbenchWindow)

#### EOF ######################################################################



