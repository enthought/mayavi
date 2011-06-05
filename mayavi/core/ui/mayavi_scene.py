""" A viewer for mlab scene. Adds a button to open up the engine.
"""

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Standard library imports
from os.path import join

# Enthought library imports
from tvtk.tools.ivtk import IVTK
from tvtk.pyface.api import DecoratedScene
from traits.api import Callable
from pyface.api import ImageResource
from pyface.action.api import Action, Group
from pyface.resource.api import resource_path

# Local imports
from mayavi.core.common import error
from mayavi.preferences.api import set_scene_preferences, \
        get_scene_preferences

###############################################################################
# A decorated scene with an additional button.
###############################################################################
class MayaviScene(DecoratedScene):
    """ A scene UI, similar to a decorated scene, but with more buttons.
    """

    image_search_path = [join(resource_path(), 'images'), ]

    ##########################################################################
    # Non-public interface.
    ##########################################################################
    def show_engine(self):
        """ Open the engine view corresponding to the engine of the
            scene.
        """
        from mayavi.core.registry import registry
        from mayavi.core.ui.engine_rich_view import EngineRichView
        try:
            engine = registry.find_scene_engine(self)
        except TypeError:
            error('This scene is not managed by Mayavi')
        return EngineRichView(engine=engine).scene_editing_view(scene=self)

    ######################################################################
    # Trait handlers.
    ######################################################################
    def _actions_default(self):
        actions = [ Group(
                    Action(tooltip="View the Mayavi pipeline",
                        image=ImageResource('m2',
                                search_path=self.image_search_path),
                        on_perform=self.show_engine,
                        ),
                        ),
                        ]
        actions.extend(DecoratedScene._actions_default(self))
        return actions


def mayavi_scene_factory(parent):
    """A mayavi scene factory that creates a scene with preferences
    appropriately set."""
    p = get_scene_preferences()
    s = MayaviScene(parent, stereo=p['stereo'])
    set_scene_preferences(s, p)
    return s

###############################################################################
# A viewer making use of the MayaviScene
###############################################################################
class MayaviViewer(IVTK):
    """ A viewer window for mlab.
    """

    _scene_factory = Callable(mayavi_scene_factory)

    def _size_default(self):
        return (400, 300)


def viewer_factory(size=(400, 350)):
    viewer = MayaviViewer()
    viewer.menu_bar_manager = None
    viewer.size=size
    viewer.open()
    return viewer

if __name__ == '__main__':
    from mayavi.tools.show import show
    viewer_factory()
    show()

