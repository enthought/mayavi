"""Draws a simple axes using tvtk.CubeAxesActor2D.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Bool, Instance, Property
from traitsui.api import View, Group, HGroup, \
        Item, BooleanEditor
from tvtk.api import tvtk
from apptools.persistence import state_pickler

# Local imports
from mayavi.core.module import Module
from mayavi.core.pipeline_info import PipelineInfo


######################################################################
# `CubeAxesActor2D` class.
######################################################################
class CubeAxesActor2D(tvtk.CubeAxesActor2D):
    """ Just has a different view than the tvtk.CubesAxesActor2D, with an
        additional tick box.
    """

    # Automaticaly fit the bounds of the axes to the data
    use_data_bounds = Bool(True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    ########################################
    # The view of this object.

    traits_view = View(Group(
                        Group(
                            Item('visibility'),
                            HGroup(
                                 Item('x_axis_visibility', label='X axis'),
                                 Item('y_axis_visibility', label='Y axis'),
                                 Item('z_axis_visibility', label='Z axis'),
                                ),
                            show_border=True, label='Visibity'),
                        Group(
                            Item('use_ranges'),
                            HGroup(
                                 Item('ranges', enabled_when='use_ranges'),
                                ),
                            show_border=True),
                        Group(
                            Item('use_data_bounds'),
                            HGroup(
                                 Item('bounds',
                                      enabled_when='not use_data_bounds'),
                                ),
                            show_border=True),
                        Group(
                            Item('x_label'),
                            Item('y_label'),
                            Item('z_label'),
                            Item('label_format'),
                            Item('number_of_labels'),
                            Item('font_factor'),
                            show_border=True),
                        HGroup(Item('show_actual_bounds',
                                    label='Use size bigger than screen',
                                    editor=BooleanEditor())),
                        Item('fly_mode'),
                        Item('corner_offset'),
                        Item('layer_number'),
                       springy=True),
                       scrollable=True,
                       resizable=True)


######################################################################
# `Axes` class.
######################################################################
class Axes(Module):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The tvtk axes actor.
    axes = Instance(CubeAxesActor2D, allow_none=False, record=True)

    # The property of the axes (color etc.).
    property = Property(record=True)

    # The title text property of the axes.
    title_text_property = Property(record=True)

    # The label text property of the axes.
    label_text_property = Property(record=True)

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
                scrollable=True, resizable=True,
                width=500, height=600
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
        axes = CubeAxesActor2D(number_of_labels=2,
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
        if mm is None or not self.axes.use_data_bounds:
            self.configure_input_data(self.axes, None)
            return
        src = mm.source
        self.configure_input(self.axes, src.outputs[0])
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

    def _use_data_bounds_changed_for_axes(self):
        """ Updating the pipeline for this module is inexpensive and fits
            the actor to the source (if any). We are using it here.
        """
        self.update_pipeline()
