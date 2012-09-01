"""
HasTraits class providing window with a mayavi engine, to preview pipeline
elements.
"""

from traits.api import HasTraits, Instance
from traitsui.api import View, Item
from tvtk.pyface.scene_editor import SceneEditor
from tvtk.pyface.scene_model import SceneModel
from tvtk.pyface.scene import Scene

from mayavi.core.engine import Engine


##############################################################################
# PreviewWindow class
##############################################################################
class PreviewWindow(HasTraits):
    """ A window with a mayavi engine, to preview pipeline elements.
    """

    # The engine that manages the preview view
    _engine = Instance(Engine)

    _scene = Instance(SceneModel, ())

    view = View(Item('_scene', editor=SceneEditor(scene_class=Scene),
                        show_label=False),
                width=500, height=500)

    #-----------------------------------------------------------------------
    # Public API
    #-----------------------------------------------------------------------

    def add_source(self, src):
        self._engine.add_source(src)

    def add_module(self, module):
        self._engine.add_module(module)

    def add_filter(self, filter):
        self._engine.add_module(filter)

    def clear(self):
        self._engine.current_scene.scene.disable_render = True
        self._engine.current_scene.children[:] = []
        self._engine.current_scene.scene.disable_render = False

    #-----------------------------------------------------------------------
    # Private API
    #-----------------------------------------------------------------------

    def __engine_default(self):
        e = Engine()
        e.start()
        e.new_scene(self._scene)
        return e

if __name__ == '__main__':
    from pyface.api import GUI
    from mayavi.sources.api import ParametricSurface
    from mayavi.modules.api import Outline, Surface
    pw = PreviewWindow()
    pw.add_source(ParametricSurface())
    pw.add_module(Outline())
    pw.add_module(Surface())

    pw.edit_traits()
