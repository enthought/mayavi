"""Creates a small axes on the side that indicates the position of the
co-ordinate axes and thereby marks the orientation of the scene.  It
uses the OrientationMarkerWidget which requires VTK-4.5 and above.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.


# Enthought library imports.
from traits.api import Instance, Property
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk
from apptools.persistence import state_pickler

# Local imports
from mayavi.core.module import Module
from mayavi.core.common import error
from mayavi.core.pipeline_info import PipelineInfo

if not hasattr(tvtk, 'OrientationMarkerWidget'):
    msg = 'The OrientationAxes module requires VTK version >= 4.5'
    error(msg)
    raise ImportError(msg)

######################################################################
# `OrientationAxes` class.
######################################################################
class OrientationAxes(Module):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The tvtk orientation marker widget.
    marker = Instance(tvtk.OrientationMarkerWidget, allow_none=False)

    # The tvtk axes that will be shown.
    axes = Instance(tvtk.AxesActor, allow_none=False, record=True)

    # The property of the axes (color etc.).
    text_property = Property(record=True)

    input_info = PipelineInfo(datasets=['any'],
                              attribute_types=['any'],
                              attributes=['any'])

    ########################################
    # Private traits.
    _text_property = Instance(tvtk.TextProperty)

    ########################################
    # The view of this object.

    _marker_group = Group(Item(name='enabled'),
                          Item(name='interactive'),
                          show_border=True,
                          label='Widget')
    _axes_group = Group(Item(name='axis_labels'),
                        Item(name='visibility'),
                        Item(name='x_axis_label_text'),
                        Item(name='y_axis_label_text'),
                        Item(name='z_axis_label_text'),
                        Item(name='cone_radius'),
                        Item(name='cone_resolution'),
                        Item(name='cylinder_radius'),
                        Item(name='cylinder_resolution'),
                        Item(name='normalized_label_position'),
                        Item(name='normalized_shaft_length'),
                        Item(name='normalized_tip_length'),
                        Item(name='total_length'),
                        show_border=True,
                        label='Axes')

    view = View(Group(Item(name='marker', style='custom',
                           editor=InstanceEditor(view=View(_marker_group))),
                      Item(name='axes', style='custom',
                           editor=InstanceEditor(view=View(_axes_group))),
                      label='Widget/Axes',
                      show_labels=False),
                Group(Item(name='_text_property', style='custom',
                           resizable=True),
                      label='Text Property',
                      show_labels=False),
                )

    ######################################################################
    # `object` interface
    ######################################################################
    def __set_pure_state__(self, state):
        for prop in ['axes', 'marker', '_text_property']:
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
        # Setup the default objects.
        self.axes = tvtk.AxesActor(normalized_tip_length=(0.4, 0.4, 0.4),
                                   normalized_shaft_length=(0.6, 0.6, 0.6),
                                   shaft_type='cylinder')
        self.text_property.trait_set(color=(1,1,1), shadow=False, italic=False)

        self.marker = tvtk.OrientationMarkerWidget(key_press_activation=False)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
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
    def _marker_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)
            self.widgets.remove(old)
        axes = self.axes
        if axes is not None:
            new.orientation_marker = axes
        new.on_trait_change(self.render)

        self.widgets.append(new)
        self.render()

    def _axes_changed(self, old, new):
        if old is not None:
            old.on_trait_change(self.render, remove=True)
            self._text_property.on_trait_change(self.render, remove=True)
        marker = self.marker
        if marker is not None:
            marker.orientation_marker = new

        p = new.x_axis_caption_actor2d.caption_text_property
        new.y_axis_caption_actor2d.caption_text_property = p
        new.z_axis_caption_actor2d.caption_text_property = p
        self._text_property = p

        # XXX: The line of code below is a stop-gap solution. Without it,
        # Some observers in the AxesActor trigger a modification of the
        # font_size each time the mouse is moved over the OrientationAxes
        # (this can be seen when running the record mode, for instance),
        # and thus a render, which is very slow. On the other hand, font
        # size does not work for the AxesActor, with or without the
        # line of code below. So we probably haven't found the true
        # cause of the problem.
        p.teardown_observers()

        new.on_trait_change(self.render)
        p.on_trait_change(self.render)

        self.render()

    def _get_text_property(self):
        return self._text_property

    def _foreground_changed_for_scene(self, old, new):
        # Change the default color for the actor.
        self.text_property.color = new
        self.render()

    def _scene_changed(self, old, new):
        super(OrientationAxes, self)._scene_changed(old, new)
        self._foreground_changed_for_scene(None, new.foreground)
        self._visible_changed(self.visible)

    def _visible_changed(self, value):
        if self.scene is not None and self.marker.interactor:
            # Enabling an OrientationAxes without an interactor will
            # lead to a segfault
            super(OrientationAxes, self)._visible_changed(value)
