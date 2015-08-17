""" A mostly-general Traits UI editor for viewing things in TVTK scenes.
"""

# Authors: Robert Kern <robert.kern [at] gmail.com>
#          Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Major library imports.
import os
from pyface.qt import QtGui

# Enthought library imports.
from traits.api import Any, Bool, Callable, Dict, Str
from traitsui.qt4.editor import Editor
from traitsui.basic_editor_factory import BasicEditorFactory

from .decorated_scene import DecoratedScene

#####################################################################
# `_ActorEditor` class
#####################################################################
class _ActorEditor(Editor):
    """ An editor for TVTK scenes.
    """

    # The editor is scrollable, so override the default.
    scrollable = Bool(True)

    # Internal GUI traits.
    _scene = Any()


    #### Public 'Editor' interface #############################################

    def init(self, parent):
        """ Finishes initializing the editor by creating the underlying toolkit
        widget.
        """

        factory = self.factory
        self.control = QtGui.QWidget()
        lay = QtGui.QVBoxLayout(self.control)
        lay.setContentsMargins(0, 0, 0, 0)

        self._create_scene()


    def update_editor(self):
        """ Updates the editor when the object trait changes external to the
        editor.
        """

        # Everything should really be handled elsewhere in trait notifications.
        # Just pass here.
        pass


    def dispose(self):
        """ Disposes of the contents of an editor.
        """

        # Remove notifications.
        self._setup_scene_notifications(remove=True)

        # Remove the current scene.
        if self._scene is not None:
            self._scene.close()
            self._scene = None

        # This will destroy self.control and all of its children, including the
        # scene's control.
        super(_ActorEditor, self).dispose()


    #### Private '_ActorEditor' interface ##################################

    def _create_scene(self):
        """ Create the TVTK scene widget.
        """

        factory = self.factory
        self._scene = factory.scene_class(self.control, **factory.scene_kwds)
        scene = self._scene

        # Disable rendering on the scene until we're finished.
        scene.disable_render = True
        # Add all of the actors in the current actor map.
        for obj, actors in self.value.items():
            self._add_actors_widgets(actors)
        # Set up Traits notifications.
        self._setup_scene_notifications()
        # Re-enable rendering.
        scene.disable_render = False

        self.control.layout().addWidget(scene.control)

        # Force a render.
        scene.render()


    def _setup_scene_notifications(self, remove=False):
        """ Set up or remove all of the Trait notifications that control the
        scene widget.
        """

        self.object.on_trait_change(
            self._set_scene_disable_render,
            name=self.factory.disable_render_name,
            remove=remove,
        )
        self.object.on_trait_event(
            self._scene.render,
            name=self.factory.do_render_name,
            remove=remove,
        )
        self.object.on_trait_change(
            self._actors_changed,
            name=self.name+'_items',
            remove=remove,
        )
        self.object.on_trait_change(
            self._actor_map_changed,
            name=self.name,
            remove=remove,
        )


    def _set_scene_disable_render(self, new):
        """ A callback for Traits notifications.
        """

        self._scene.disable_render = new


    def _actors_changed(self, event):
        """ Handle the event of the actors in the actor map changing.
        """

        scene = self._scene
        # Temporarily turn off rendering. We (re)store the old value of
        # disable_render because it may already be True.
        old_disable_render = scene.disable_render
        scene.disable_render = True
        try:
            for obj, actors in event.removed.items():
                self._remove_actors_widgets(actors)
            for obj, actors in event.added.items():
                self._add_actors_widgets(actors)
            for obj, actors in event.changed.items():
                # The actors in the event are the old ones. Grab the new ones
                # from the actor map itself.
                self._remove_actors_widgets(actors)
                self._add_actors_widgets(self.value[obj])
        finally:
            scene.disable_render = old_disable_render
            scene.render()


    def _actor_map_changed(self, object, name, old, new):
        """ Handle the case when the entire actor map is set to something else.
        """

        scene = self._scene
        # Temporarily turn off rendering. We (re)store the old value of
        # disable_render because it may already be True.
        old_disable_render = scene.disable_render
        scene.disable_render = True
        try:
            for obj, actors in old.items():
                self._remove_actors_widgets(actors)
            for obj, actors in new.items():
                self._add_actors_widgets(actors)
        finally:
            scene.disable_render = old_disable_render
            scene.render()

    def _separate_actors_widgets(self, actors_widgets):
        """Given a sequence (or single) of actors or widgets, this returns a
        list of just the actors and another of just the widgets.
        """
        if not hasattr(actors_widgets, '__getitem__'):
            actors_widgets = [actors_widgets]
        actors = []
        widgets = []
        for actor in actors_widgets:
            if actor.is_a('vtk3DWidget'):
                widgets.append(actor)
            else:
                actors.append(actor)
        return actors, widgets

    def _add_actors_widgets(self, actors_widgets):
        """Add actors and widgets to scene."""
        scene = self._scene
        actors, widgets = self._separate_actors_widgets(actors_widgets)
        scene.add_actors(actors)
        scene.add_widgets(widgets)

    def _remove_actors_widgets(self, actors_widgets):
        """Remove actors and widgets from scene."""
        scene = self._scene
        actors, widgets = self._separate_actors_widgets(actors_widgets)
        scene.remove_actors(actors)
        scene.remove_widgets(widgets)


#####################################################################
# `ActorEditor` class
#####################################################################
class ActorEditor(BasicEditorFactory):
    """ An editor factory for TVTK scenes.
    """

    # The class of the editor object to be constructed.
    klass = _ActorEditor

    # The class or factory function for creating the actual scene object.
    scene_class = Callable(DecoratedScene)

    # Keyword arguments to pass to the scene factory.
    scene_kwds = Dict()

    # The name of the trait used for ITVTKActorModel.disable_render.
    disable_render_name = Str('disable_render')

    # The name of the trait used for ITVTKActorModel.do_render.
    do_render_name = Str('do_render')

#### EOF #######################################################################
