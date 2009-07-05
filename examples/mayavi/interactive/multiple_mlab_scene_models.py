""" Example showing a dialog with multiple embedded scenes.
"""
import numpy as np

from enthought.traits.api import HasTraits, Instance, Button, \
    on_trait_change
from enthought.traits.ui.api import View, Item, HSplit, Group
from enthought.tvtk.pyface.scene_editor import SceneEditor
from enthought.mayavi.tools.mlab_scene_model import MlabSceneModel

class MyDialog(HasTraits):

    scene1 = Instance(MlabSceneModel, ())
    scene2 = Instance(MlabSceneModel, ())

    button1 = Button('Redraw')
    button2 = Button('Redraw')

    @on_trait_change('button1')
    def redraw_scene1(self):
        self.redraw_scene(self.scene1)


    @on_trait_change('button2')
    def redraw_scene2(self):
        self.redraw_scene(self.scene2)

    def redraw_scene(self, scene):
        scene.mlab.clf()
        x, y, z, s = np.random.random((4, 100))
        scene.mlab.points3d(x, y, z, s)

    # The layout of the dialog created
    view = View(HSplit(
                  Group(
                       Item('scene1',
                            editor=SceneEditor(), height=250, 
                            width=300),
                       'button1', 
                       show_labels=False,
                  ),
                  Group(
                       Item('scene2',
                            editor=SceneEditor(), height=250, 
                            width=300, show_label=False),
                       'button2', 
                       show_labels=False,
                  ),
                ),
                resizable=True,
                )

m = MyDialog()
m.configure_traits()
                                
