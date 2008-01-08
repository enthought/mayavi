"""Draws a simple axes using tvtk.CubeAxesActor2D.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2006, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance, Property
from enthought.traits.ui.api import View, Group, Item
from enthought.tvtk.api import tvtk
from enthought.persistence import state_pickler

# Local imports
from enthought.mayavi.core.module import Module


######################################################################
# `Axes` class.
######################################################################
class Axes(Module):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The tvtk axes actor.
    axes = Instance(tvtk.CubeAxesActor2D, allow_none=False)

    # The property of the axes (color etc.).
    property = Property
    
    # The title text property of the axes.
    title_text_property = Property
    
    # The label text property of the axes.
    label_text_property = Property

    ########################################
    # Private traits.
    _property = Instance(tvtk.Property2D)
    _title_text_property = Instance(tvtk.TextProperty)
    _label_text_property = Instance(tvtk.TextProperty)

    ########################################
    # The view of this object.

    view = View(Group(Item(name='axes', style='custom', resizable=True),
                      label='Axes',
                      show_labels=False),
                Group(Item(name='_property', style='custom',
                           resizable=True),
                      label='Property',
                      show_labels=False),
                Group(Item(name='_title_text_property', style='custom',
                           resizable=True),
                      label='Title Text',
                      show_labels=False),
                Group(Item(name='_label_text_property', style='custom',
                           resizable=True),
                      label='Label Text',
                      show_labels=False),
                resizable=True, width=500, height=600
                )

    ######################################################################
    # `object` interface
    ######################################################################
    def __set_pure_state__(self, state):
        for prop in ['axes', '_property', '_title_text_property',
                     '_label_text_property']:
            obj = getattr(self, prop)
            state_pickler.set_state(obj, state[prop])

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
        # Create the axes and set things up.
        axes = tvtk.CubeAxesActor2D(number_of_labels= 2,
                                    font_factor=1.5,
                                    fly_mode='outer_edges',
                                    corner_offset=0.0,
                                    scaling=False)
        axes.axis_title_text_property.shadow = False
        axes.axis_label_text_property.shadow = False

        # Set the axes.
        self.axes = axes

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        mm = self.module_manager
        if mm is None:
            return
        src = mm.source
        self.axes.input = src.outputs[0]
        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        # Just set data_changed, the component should do the rest.
        self.data_changed = True

    ######################################################################
    # Non-public interface
    ######################################################################
    def _scene_changed(self, old, new):
        super(Axes, self)._scene_changed(old, new)
        self.axes.camera = new.camera
        self._foreground_changed_for_scene(None, new.foreground)

    def _foreground_changed_for_scene(self, old, new):
        # Change the default color for the actor.
        self.property.color = new
        self.label_text_property.color = new
        self.title_text_property.color = new
        self.render()

    def _axes_changed(self, old, new):
        if old is not None:
            for obj in (old, self._property, self._title_text_property,
                        self._label_text_property):
                obj.on_trait_change(self.render, remove=True)
            self.actors.remove(old)
        # Setup the axes.
        scene = self.scene
        if scene is not None:
            new.camera = scene.camera

        # Setup the private traits.
        self._property = new.property
        for prop in ['_title_text_property',
                     '_label_text_property']:
            setattr(self,  prop, getattr(new, 'axis' + prop))
        # The handlers.
        for obj in (new, self._property, self._title_text_property,
                    self._label_text_property):
            obj.on_trait_change(self.render)
        self.actors.append(new)
        if old is not None:
            self.update_pipeline()

    def _get_property(self):
        return self._property

    def _get_title_text_property(self):
        return self._title_text_property

    def _get_label_text_property(self):
        return self._label_text_property
