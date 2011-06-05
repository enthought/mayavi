"""A very silly example of using a scene editor.  More complex examples are
available in mayavi.  """

# Author: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

from traits.api import HasTraits, Enum, Instance, Any
from traitsui.api import View, Item
from tvtk.pyface.scene_model import SceneModel
from tvtk.pyface.scene_editor import SceneEditor
from tvtk.pyface import actors
from tvtk.api import tvtk


######################################################################
class ActorViewer(HasTraits):

    # A simple trait to change the actors/widgets.
    actor_type = Enum('cone', 'sphere', 'plane_widget', 'box_widget')

    # The scene model.
    scene = Instance(SceneModel, ())

    _current_actor = Any

    ######################
    view = View(Item(name='actor_type'),
                Item(name='scene',
                     editor=SceneEditor(),
                     show_label=False,
                     resizable=True,
                     height=500,
                     width=500)
                )

    def __init__(self, **traits):
        super(ActorViewer, self).__init__(**traits)
        self._actor_type_changed(self.actor_type)

    ####################################
    # Private traits.
    def _actor_type_changed(self, value):
        scene = self.scene
        if self._current_actor is not None:
            scene.remove_actors(self._current_actor)
        if value == 'cone':
            a = actors.cone_actor()
            scene.add_actors(a)
        elif value == 'sphere':
            a = actors.sphere_actor()
            scene.add_actors(a)
        elif value == 'plane_widget':
            a = tvtk.PlaneWidget()
            scene.add_actors(a)
        elif value == 'box_widget':
            a = tvtk.BoxWidget()
            scene.add_actors(a)
        self._current_actor = a


if __name__ == '__main__':
    a = ActorViewer()
    a.configure_traits()
