""" A viewer for mlab scene. Adds a open to open up the engine.
"""

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org> 
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports
from os.path import join

# Enthought library imports
from enthought.tvtk.tools.ivtk import IVTK
from enthought.tvtk.pyface.api import DecoratedScene
from enthought.traits.api import Callable
from enthought.pyface.api import ImageResource
from enthought.pyface.action.api import Action
from enthought.resource.api import resource_path

# Local imports
from enthought.mayavi.core.common import error
from enthought.mayavi.preferences.api import set_scene_preferences 

###############################################################################
# A decorated scene with an additional button.
###############################################################################
class MayaviScene(DecoratedScene):
    """ Like a decorated scene, but with more buttons.
    """

    image_search_path = [join(resource_path(), 'images'), ]

    ##########################################################################
    # Non-public interface.
    ##########################################################################
    def show_engine(self):
        """ Open the engine view corresponding to the engine of the
            scene.
        """
        from enthought.mayavi.core.registry import registry
        from enthought.mayavi.core.ui.engine_view import EngineView
        try:
            engine = registry.find_scene_engine(self)
            return EngineView(engine=engine).edit_traits()
        except TypeError:
            error('This scene is not managed by Mayavi')

    ######################################################################
    # Trait handlers.
    ######################################################################
    def _actions_default(self):
        actions = DecoratedScene._actions_default(self)
        actions.extend([
                    Action(tooltip="View the Mayavi pipeline",
                        image=ImageResource('m2', 
                                search_path=self.image_search_path),
                        on_perform=self.show_engine,
                        ),
                        ])
        return actions


###############################################################################
# A viewer making use of the MayaviScene 
###############################################################################
class MayaviViewer(IVTK):
    """ A viewer window for mlab.
    """
    size=(400, 350)

    _scene_factory = Callable(MayaviScene)


def viewer_factory(size=(400, 350)):
    viewer = MayaviViewer()
    viewer.menu_bar_manager = None
    viewer.size=size
    viewer.open()
    set_scene_preferences(viewer.scene)
    return viewer

if __name__ == '__main__':
    from enthought.mayavi.tools.show import show
    viewer_factory()
    show()

