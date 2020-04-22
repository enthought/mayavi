""" Example showing a dialog with multiple embedded scenes.

When using several embedded scenes with mlab, you should be very careful
always to pass the scene you want to use for plotting to the mlab
function used, elsewhere it uses the current scene. In this example,
failing to do so would result in only one scene being used, the last
one created.

The trick is to use the 'mayavi_scene' attribute of the MlabSceneModel,
and pass it as a keyword argument to the mlab functions.

For more examples on embedding mlab scenes in dialog, see also:
the examples :ref:`example_mlab_interactive_dialog`, and
:ref:`example_lorenz_ui`, as well as the section of the user manual
:ref:`embedding_mayavi_traits`.
"""
import numpy as np

from traits.api import HasTraits, Instance, Button, \
    on_trait_change
from traitsui.api import View, Item, HSplit, Group

from mayavi import mlab
from mayavi.core.ui.api import MlabSceneModel, SceneEditor


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
        # Notice how each mlab call points explicitly to the figure it
        # applies to.
        mlab.clf(figure=scene.mayavi_scene)
        x, y, z, s = np.random.random((4, 100))
        mlab.points3d(x, y, z, s, figure=scene.mayavi_scene)

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
