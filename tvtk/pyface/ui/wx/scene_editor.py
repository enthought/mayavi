#------------------------------------------------------------------------------
#
#  Copyright (c) 2007, Enthought, Inc.
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#
#  Authors: Prabhu Ramachandran <prabhu [at] aero.iitb.ac.in>
#           Robert Kern <robert.kern [at] gmail.com>
#
#------------------------------------------------------------------------------

""" A `SceneEditor` for the `SceneModel`.
"""

import wx

# Enthought library imports.
from traits.api import Any, Bool, Callable
from traitsui.wx.editor import Editor
from traitsui.basic_editor_factory import BasicEditorFactory

from .decorated_scene import DecoratedScene

#####################################################################
# `_SceneEditor` class
#####################################################################
class _SceneEditor(Editor):
    """ An editor for SceneModels.
    """

    # The editor is scrollable, so override the default.
    scrollable = Bool(True)

    # Internal GUI traits.
    _sizer = Any()
    _scene = Any()


    #### Public 'Editor' interface #############################################

    def init(self, parent):
        """ Finishes initializing the editor by creating the underlying toolkit
        widget.
        """

        factory = self.factory
        self.control = wx.Panel(parent, -1)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.control.SetSizer(self._sizer)

        assert self.value.scene_editor is None, \
                "The SceneModel may only have one active editor!"
        self._create_scene()
        self.value.activated = True

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

        self.value.closing = True
        self.value.scene_editor = None
        self._setup_scene_notifications(remove=True)

        # Remove the current scene.
        if self._scene is not None:
            self._scene.close()
            self._scene = None

        self._sizer = None

        # This will destroy self.control and all of its children, including the
        # scene's control.
        super(_SceneEditor, self).dispose()

    #### Private '_SceneEditor' interface ##################################

    def _create_scene(self):
        """ Create the TVTK scene widget.
        """

        factory = self.factory
        self._scene = factory.scene_class(self.control)
        scene = self._scene
        self.value.scene_editor = scene

        # Disable rendering on the scene until we're finished.
        scene.disable_render = True
        # Add all of the actors in the current actor map.
        for obj, actors in self.value.actor_map.items():
            self._add_actors_widgets(actors)
        # Add all of the actors in the current actor map.
        self._add_actors_widgets(self.value.actor_list)
        # Set up Traits notifications.
        self._setup_scene_notifications()
        # Re-enable rendering.
        scene.disable_render = False

        # Ensure the scene's wx control is sized to fill our view's area.  Note
        # that the sizer doesn't automatically layout its contents upon adding
        # a new child so we have to force it to do a layout.
        self._sizer.Add(scene.control, 1, wx.EXPAND)
        self._sizer.Layout()

        wx.EVT_IDLE(scene.control, None)

        # Force a render.
        scene.render()

    def _setup_scene_notifications(self, remove=False):
        """ Set up or remove all of the Trait notifications that control the
        scene widget.
        """

        traits_to_sync = ['foreground', 'anti_aliasing_frames',
                          'stereo',  'background', 'off_screen_rendering',
                          'polygon_smoothing', 'jpeg_progressive',
                          'point_smoothing', 'busy', 'disable_render',
                          'magnification', 'jpeg_quality',
                          'parallel_projection', 'line_smoothing']

        model = self.value
        scene = self._scene
        if not remove:
            scene.trait_set(**model.trait_get(traits_to_sync))
        for trait in traits_to_sync:
            scene.sync_trait(trait, model, mutual=True, remove=remove)

        model.on_trait_change(
            scene.render,
            name='do_render',
            remove=remove,
        )
        model.on_trait_change(
            self._actors_changed,
            name='actor_map_items',
            remove=remove,
        )
        model.on_trait_change(
            self._actor_map_changed,
            name='actor_map',
            remove=remove,
        )

        model.on_trait_change(
            self._actor_list_items_changed,
            name='actor_list_items',
            remove=remove,
        )
        model.on_trait_change(
            self._actor_list_changed,
            name='actor_list',
            remove=remove,
        )

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
                self._add_actors_widgets(self.value.actor_map[obj])
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

    def _actor_list_items_changed(self, event):
        self._actor_list_changed(self.value, 'actor_list', event.removed,
                                 event.added)

    def _actor_list_changed(self, object, name, old, new):
        """ Handle the event of the actors in the actor map changing.
        """

        scene = self._scene
        # Temporarily turn off rendering. We (re)store the old value of
        # disable_render because it may already be True.
        old_disable_render = scene.disable_render
        scene.disable_render = True
        try:
            self._remove_actors_widgets(old)
            self._add_actors_widgets(new)
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
            if actor.is_a('vtk3DWidget') or actor.is_a('vtkInteractorObserver'):
                widgets.append(actor)
            else:
                actors.append(actor)
        return actors, widgets

    def _add_actors_widgets(self, actors_widgets):
        """Add actors and widgets to scene."""
        scene = self._scene
        actors, widgets = self._separate_actors_widgets(actors_widgets)
        scene.add_actors(actors)
        enabled_info = self.value.enabled_info
        for widget in widgets:
            scene.add_widgets(widget, enabled_info.get(widget, True))

    def _remove_actors_widgets(self, actors_widgets):
        """Remove actors and widgets from scene."""
        scene = self._scene
        actors, widgets = self._separate_actors_widgets(actors_widgets)
        scene.remove_actors(actors)
        scene.remove_widgets(widgets)


#####################################################################
# `SceneEditor` class
#####################################################################
class SceneEditor(BasicEditorFactory):
    """ A TraitsUI editor factory for SceneModel instances.
    """

    # The class of the editor object to be constructed.
    klass = _SceneEditor

    # The class or factory function for creating the actual scene object.
    scene_class = Callable(DecoratedScene)

#### EOF #######################################################################
