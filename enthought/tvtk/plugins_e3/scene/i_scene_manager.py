""" The interface for TVTK scene managers. """


# Enthought library imports.
from enthought.pyface.tvtk.scene import Scene
from enthought.pyface.workbench.api import WorkbenchWindow
from enthought.traits.api import Interface, List, Instance


class ISceneManager(Interface):
    """ The interface for TVTK scene managerss. """

    # The currently active scene (None, if no scene is active).
    current_scene = Instance(Scene)

    # A list of all open scenes.
    scenes = List(Scene)
    
    # The workbench window that the manager is in (there is one scene manager
    # per workbench window).
    window = Instance(WorkbenchWindow)
    
#### EOF ######################################################################



