from traits.api import HasTraits, Instance, Enum, Dict
from traitsui.api import View, Item
from tvtk.pyface.actor_model import ITVTKActorModel
from tvtk.pyface.actor_editor import ActorEditor
from tvtk.pyface import actors
from tvtk.api import tvtk


######################################################################
class ActorModel(ITVTKActorModel):

    # A simple trait to change the actors/widgets.
    actor_type = Enum('cone', 'sphere', 'plane_widget', 'box_widget')

    #########################
    # ITVTKView Model traits.

    # This maintains a dictionary mapping objects (by identity) to lists (or
    # single items) of TVTK Actors or 3D Widgets that represent them in the
    # scene. Adding and removing objects from this dictionary adds and removes
    # them from the scene. This is the trait that will be edited by a
    # ActorEditor.
    actor_map = Dict()

    ######################
    view = View(Item(name='actor_type'),
                Item(name='actor_map',
                     editor=ActorEditor(scene_kwds={'background':(0.2,0.2,0.2)}),
                     show_label=False,
                     resizable=True,
                     height=500,
                     width=500)
                )

    def __init__(self, **traits):
        super(ActorModel, self).__init__(**traits)
        self._actor_type_changed(self.actor_type)

    ####################################
    # Private traits.
    def _actor_type_changed(self, value):
        if value == 'cone':
            a = actors.cone_actor()
            self.actor_map = {'cone': a}
        elif value == 'sphere':
            a = actors.sphere_actor()
            self.actor_map = {'sphere': a}
        elif value == 'plane_widget':
            w = tvtk.PlaneWidget()
            self.actor_map = {'plane_widget': w}
        elif value == 'box_widget':
            w = tvtk.BoxWidget()
            self.actor_map = {'box_widget': w}


if __name__ == '__main__':
    a = ActorModel()
    a.configure_traits()
