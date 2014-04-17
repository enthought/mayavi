"""A simple actor component.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk

# Local imports.
from mayavi.core.component import Component


######################################################################
# `Actor2D` class.
######################################################################
class Actor2D(Component):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The mapper.
    mapper = Instance(tvtk.AbstractMapper, record=True)

    # The actor.
    actor = Instance(tvtk.Prop, record=True)

    # The actor's property.
    property = Instance(tvtk.Property2D, record=True)


    ########################################
    # View related traits.

    # The Actor's view group.
    _actor_group = Group(Item(name='visibility'),
                         Item(name='height'),
                         Item(name='width'),
                         show_border=True, label='Actor')

    # The View for this object.
    view = View(Group(Item(name='actor', style='custom',
                           editor=InstanceEditor(view=View(_actor_group))),
                      show_labels=False,
                      label='Actor'
                      ),
                Group(Item(name='mapper',
                           style='custom',
                           resizable=True),
                      show_labels=False,
                      label='Mapper'),
                Group(Item(name='property',
                           style='custom',
                           resizable=True),
                      show_labels=False,
                      label='Property'),
                resizable=True,
                )

    ######################################################################
    # `Component` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* its tvtk
        pipeline.

        This method is invoked when the object is initialized via
        `__init__`.  Note that at the time this method is called, the
        tvtk data pipeline will *not* yet be setup.  So upstream data
        will not be available.  The idea is that you simply create the
        basic objects and setup those parts of the pipeline not
        dependent on upstream sources and filters.
        """
        if self.mapper is None:
            self.mapper = tvtk.TextMapper()
        self.actor = tvtk.Actor2D()
        self.property = self.actor.property

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        if (len(self.inputs) == 0) or \
               (len(self.inputs[0].outputs) == 0):
            return
        self.configure_connection(self.mapper, self.inputs[0])
        self.render()

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Invoke render to update any changes.
        self.render()

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _setup_handlers(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)
        new.on_trait_change(self.render)

    def _mapper_changed(self, old, new):
        # Setup the handlers.
        self._setup_handlers(old, new)
        # Setup the inputs to the mapper.
        if (len(self.inputs) > 0) and (len(self.inputs[0].outputs) > 0):
            self.configure_connection(new, self.inputs[0])
        # Setup the actor's mapper.
        actor = self.actor
        if actor is not None:
            actor.mapper = new
        self.render()

    def _actor_changed(self, old, new):
        # Setup the handlers.
        self._setup_handlers(old, new)
        # Set the mapper.
        mapper = self.mapper
        if mapper is not None:
            new.mapper = mapper
        # Set the property.
        prop = self.property
        if prop is not None:
            new.property = prop
        # Setup the `actors` trait.
        self.actors = [new]

    def _property_changed(self, old, new):
        # Setup the handlers.
        self._setup_handlers(old, new)
        # Setup the actor.
        actor = self.actor
        if new is not actor.property:
            actor.property = new

    def _foreground_changed_for_scene(self, old, new):
        # Change the default color for the actor.
        self.property.color = new
        self.render()

    def _scene_changed(self, old, new):
        super(Actor2D, self)._scene_changed(old, new)
        self._foreground_changed_for_scene(None, new.foreground)
