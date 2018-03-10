"""A scene object manages a TVTK scene and objects in it.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005,  Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Event, List, Str, Instance
from traitsui.api import View, Group, Item
from apptools.persistence.state_pickler import set_state

# Local imports.
from tvtk.pyface.tvtk_scene import TVTKScene
from mayavi.core.base import Base
from mayavi.core.source import Source
from mayavi.core.common import handle_children_state, exception
from mayavi.core.adder_node import SourceAdderNode

######################################################################
# `Scene` class.
######################################################################
class Scene(Base):
    """ The Mayavi scene class.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The scene (RenderWindow) associated with this component -- we
    # redeclare it here just to be able to record this scene, we don't
    # want it recorded on all objects since the scene is shared
    # (although it isn't an error to register an object twice with the
    # recorder).
    scene = Instance(TVTKScene, record=True)

    # The source objects associated with this object.
    children = List(Source, record=True)

    # The name of this scene.
    name = Str('TVTK Scene')

    # The icon
    icon = Str('scene.ico')

    # The human-readable type for this object
    type = Str(' scene')

    # The objects view.
    view = View(Group(Item(name='scene', style='custom'),
                           show_labels=False)
               )

    # The adder node dialog class
    _adder_node_class = SourceAdderNode

    # The dispatch, to register callbacks on mouse pick
    _mouse_pick_dispatcher = Instance(
        'mayavi.core.mouse_pick_dispatcher.MousePickDispatcher',
        record=False)

    ######################################################################
    # `object` interface
    ######################################################################
    def __get_pure_state__(self):
        # Base removes the scene, but we need to save it!
        d = super(Scene, self).__get_pure_state__()
        d['scene'] = self.scene
        d.pop('_mouse_pick_dispatcher', None)
        return d

    def __set_pure_state__(self, state):
        handle_children_state(self.children, state.children)

        # As `camera.distance` is derived from other camera parameters
        # if camera is defined, we should skip restoring "distance"
        if state.scene and state.scene.camera:
            state.scene.camera.pop("distance", None)

        # Now set our complete state.  Doing the scene last ensures
        # that the camera view is set right.  Before doing this though,
        # if the light_manager is None, the scene hasn't been painted,
        # in that case save the light manager state and set the state later.
        # All we do is set the _saved_light_manager_state and the scene
        # will take care of the rest.
        if self.scene is not None and self.scene.light_manager is None:
            lm_state = state['scene'].pop('light_manager', None)
            self.scene._saved_light_manager_state = lm_state

        set_state(self, state, last=['scene'])

    ######################################################################
    # `Scene` interface
    ######################################################################

    def on_mouse_pick(self, callback, type='point', button='Left',
                            remove=False):
        """ Add a picking callback on mouse click.

            When the mouse button is press, object picking is called, and
            the given callback is invoked with the resulting pick
            as an argument.

            **Keyword arguments**

            :type: 'point', 'cell', or 'world'
                The picker type used for picking.
            :button: 'Left', 'Middle', or 'Right'
                The mouse button triggering the picking event.
            :remove: boolean
                If remove is True, the callback is removed from the
                list of callbacks.

            **Returns**
            picker: a tvtk picker
                The picker that will be used to do the picking.

            **Notes**

            The callback must accept one argument: the TVTK picker.

            The same callback can be added multiple times.
        """
        key = (callback, type, button)
        if remove:
            self._mouse_pick_dispatcher.callbacks.remove(key)
        else:
            self._mouse_pick_dispatcher.callbacks.append(key)
        return self._mouse_pick_dispatcher._active_pickers[type]


    ######################################################################
    # `Base` interface
    ######################################################################
    def start(self):
        """This is invoked when this object is added to the mayavi
        pipeline.
        """
        # Do nothing if we are already running.
        if self.running:
            return

        # Start all our children.
        for obj in self.children:
            obj.start()

        # Disallow the hide action in the context menu
        self._HideShowAction.enabled = False

        super(Scene, self).start()

    def stop(self):
        """Invoked when this object is removed from the mayavi
        pipeline.
        """
        if not self.running:
            return

        # Disable rendering to accelerate shutting down.
        scene = self.scene
        if scene is not None:
            status = scene.disable_render
            scene.disable_render = True
        try:
            # Stop all our children.
            for obj in self.children:
                obj.stop()
        finally:
            # Re-enable rendering.
            if scene is not None:
                scene.disable_render = status
                self.scene = None
        super(Scene, self).stop()

    def add_child(self, child):
        """This method intelligently adds a child to this object in
        the MayaVi pipeline.
        """
        self.children.append(child)

    def remove_child(self, child):
        """Remove specified child from our children.
        """
        self.children.remove(child)

    def remove(self):
        """Remove ourselves from the mayavi pipeline.
        """
        if self.parent is not None:
            self.stop()
            self.parent.close_scene(self)

    ######################################################################
    # `TreeNodeObject` interface
    ######################################################################
    def tno_can_add(self, node, add_object):
        """ Returns whether a given object is droppable on the node.
        """
        try:
            if issubclass(add_object, Source):
                return True
        except TypeError:
            if isinstance(add_object, Source):
                return True
        return False

    def tno_drop_object(self, node, dropped_object):
        """ Returns a droppable version of a specified object.
        """
        if isinstance(dropped_object, Source):
            return dropped_object

    ######################################################################
    # Non-public interface
    ######################################################################
    def _children_changed(self, old, new):
        self._handle_children(old, new)

    def _children_items_changed(self, list_event):
        self._handle_children(list_event.removed, list_event.added)

    def _handle_children(self, removed, added):
        for obj in removed:
            obj.stop()
        for obj in added:
            obj.trait_set(scene=self.scene, parent=self)
            if self.running:
                # It makes sense to start children only if we are running.
                # If not, the children will be started when we start.
                try:
                    obj.start()
                except:
                    exception()

    def _menu_helper_default(self):
        from mayavi.core.traits_menu import SourceMenuHelper
        return SourceMenuHelper(object=self)

    def __mouse_pick_dispatcher_default(self):
        from mayavi.core.mouse_pick_dispatcher import \
                        MousePickDispatcher
        return MousePickDispatcher(scene=self)
