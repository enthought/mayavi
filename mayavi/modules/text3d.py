""" This module allows the user to place text in 3D at a location on the
scene.

Unlike the 'Text' module, this module positions text in 3D in the scene,
and in 2D on the screen. As a result the text resizes with the figure,
and can be masked by objects in the foreground.
"""
# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2009, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Str, CArray, Bool
from traitsui.api import View, Group, Item

# Local imports
from tvtk.api import tvtk
from mayavi.core.module import Module
from mayavi.core.pipeline_info import PipelineInfo
from mayavi.components.actor import Actor

######################################################################
# `Text3D` class.
######################################################################

class Text3D(Module):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The Mayavi Actor.
    actor = Instance(Actor, allow_none=False, record=True)

    # And the text source
    vector_text = Instance(tvtk.VectorText, allow_none=False, record=True)

    # The text to be displayed.
    text = Str('Text', desc='the text to be displayed',
                       enter_set=True, auto_set=False)

    # The position of the actor
    position = CArray(value=(0., 0., 0.), cols=3,
                      desc='the world coordinates of the text',
                      enter_set=True, auto_set=False)

    # The scale of the actor
    scale = CArray(value=(1., 1., 1.), cols=3,
                      desc='the scale of the text',
                      enter_set=True, auto_set=False)

    # The orientation of the actor
    orientation = CArray(value=(0., 0., 0.), cols=3,
                      desc='the orientation angles of the text',
                      enter_set=True, auto_set=False)

    # Orient actor to camera
    orient_to_camera = Bool(True,
                      desc='if the text is kept facing the camera')

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    ########################################
    # The view of this object.

    view = View(Group(Item(name='text'),
                      Group(Item(name='position'),
                        show_labels=False, show_border=True,
                        label='Position'),
                      Group(Item(name='scale'),
                        show_labels=False, show_border=True,
                        label='Scale'),
                      Group(
                           Item(name='orient_to_camera'),
                           Item(name='orientation',
                                 label='Angles'),
                        show_border=True,
                        label='Orientation'),
                      label='Text',
                      ),
                  Group(Item(name='actor', style='custom',
                             show_label=False),
                      label='Actor'),
                )

    ######################################################################
    # `Module` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.  You should also
        set the `actors` attribute up at this point.
        """
        self.vector_text = tvtk.VectorText(text=self.text)
        self.outputs = [self.vector_text]
        self.actor = Actor()
        self._text_changed(self.text)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        self.pipeline_changed = True

    def has_output_port(self):
        """ Return True as the text3d has output port. """
        return True

    def get_output_object(self):
        return self.vector_text.output_port

    ######################################################################
    # Non-public interface
    ######################################################################
    def _text_changed(self, value):
        vector_text = self.vector_text
        if vector_text is None:
            return
        vector_text.text = str(value)
        self.render()

    def _actor_changed(self, old, new):
        new.scene = self.scene
        new.inputs = [self]
        self._change_components(old, new)
        old_actor = None
        if old is not None:
            old_actor = old.actor
        new.actor = self._get_actor_or_follower(old=old_actor)
        self.actors = new.actors
        self.render()

    def _orient_to_camera_changed(self):
        self.actor.actor = \
                    self._get_actor_or_follower(old=self.actor.actor)


    def _get_actor_or_follower(self, old=None):
        """ Get a tvtk.Actor or a tvtk.Follower for the actor of the
            object and wire the callbacks to it.
            If old is given, it is the old actor, to remove its
            callbacks.
        """
        if self.orient_to_camera:
            new = tvtk.Follower()
            if self.scene is not None:
                new.camera = self.scene.camera
        else:
            new = tvtk.Actor()
        if old is not None:
            self.sync_trait('position', old, 'position', remove=True)
            self.sync_trait('scale', old, 'scale', remove=True)
            self.sync_trait('orientation', old, 'orientation', remove=True)

        self.sync_trait('position', new, 'position')
        self.sync_trait('scale', new, 'scale')
        self.sync_trait('orientation', new, 'orientation')
        return new

    def _scene_changed(self, old, new):
        super(Text3D, self)._scene_changed(old, new)
        if new is not None and self.orient_to_camera:
            self.actor.actor.camera = new.camera
