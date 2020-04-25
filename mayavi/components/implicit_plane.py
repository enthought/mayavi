"""A component to manage an implicit plane widget.
"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Instance, Bool, Property, Any
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk

# Local imports.
from mayavi.core.component import Component
from mayavi.core.utils import DataSetHelper

VTK_VER = tvtk.Version().vtk_version


######################################################################
# `ImplicitPlane` class.
######################################################################
class ImplicitPlane(Component):
    # The version of this class.  Used for persistence.
    __version__ = 0

    # The widget that controls the plane.
    widget = Instance(tvtk.ImplicitPlaneWidget, args=(),
                      kw={'key_press_activation': False,
                          'place_factor':1.2,
                          'draw_plane':False,
                          'outline_translation':False},
                      record=True)

    # The plane that the widget controls.  Do not change the
    # attributes of the plane, do it via the widget.
    plane = Instance(tvtk.Plane, args=(),
                     kw={'origin':(0.0, 0.0, 0.0),
                         'normal':(0,0,1)},
                     record=True)

    # Convenience property for the normal delegated to the widget.
    normal = Property

    # Convenience property for the origin delegated to the widget.
    origin = Property

    ########################################
    # Private traits

    _first = Bool(True)
    _busy = Bool(False)
    _bounds = Any

    ########################################
    # View related traits.

    if VTK_VER[:3] in ['4.2', '4.4']:
        _widget_group = Group(Item(name='enabled'),
                              Item(name='normal_to_x_axis'),
                              Item(name='normal_to_y_axis'),
                              Item(name='normal_to_z_axis'),
                              Item(name='outline_translation'),
                              Item(name='tubing'),
                              Item(name='draw_plane'),
                              Item(name='normal'),
                              Item(name='origin')
                              )
    else:
        _widget_group = Group(Item(name='enabled'),
                              Item(name='normal_to_x_axis'),
                              Item(name='normal_to_y_axis'),
                              Item(name='normal_to_z_axis'),
                              Item(name='outline_translation'),
                              Item(name='scale_enabled'),
                              Item(name='tubing'),
                              Item(name='draw_plane'),
                              Item(name='normal'),
                              Item(name='origin')
                              )

    view = View(Group(Item(name='widget', style='custom',
                           editor=InstanceEditor(view=View(_widget_group))),
                      show_labels=False)
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
        # Setup our widgets and hook up all handlers.
        self.widgets = [self.widget]
        self._connect()

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when the input fires a
        `pipeline_changed` event.
        """
        if len(self.inputs) == 0 or len(self.inputs[0].outputs) == 0:
            return
        inp = self.inputs[0].outputs[0]
        w = self.widget
        self.configure_input(w, inp)
        if self._first:
            dsh = DataSetHelper(self.inputs[0].outputs[0])
            self._bounds = dsh.get_bounds()
            w.place_widget(*self._bounds)
            self.origin = dsh.get_center()
            self._first = False
        else:
            n = self.normal
            # A hack to update the widget when data changes upstream.
            # This is perhaps a VTK bug, not sure.
            self.normal = n[0], n[1], n[2] + 0.001
            self.normal = n

        # Just pass the inputs back out.  This may trigger a pipeline
        # changed downstream if it does not then fire a data_changed.
        if self.outputs != [inp]:
            self.outputs = [inp]
        else:
            self.data_changed = True

    def update_data(self):
        """Override this method to do what is necessary when upstream
        data changes.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        self.data_changed = True

    def update_plane(self):
        """Convenience method to update the plane once the widget is
        changed.
        """
        self.widget.get_plane(self.plane)
        self.update_data()

    ######################################################################
    # Non-public interface.
    ######################################################################
    def _get_normal(self):
        return self.widget.normal

    def _set_normal(self, value):
        w = self.widget
        old = w.normal
        w.normal = value
        self.trait_property_changed('normal', old, value)
        self.update_plane()

    def _get_origin(self):
        return self.widget.origin
    def _set_origin(self, value):
        # Ugly, but needed.
        w = tvtk.to_vtk(self.widget)
        old = w.GetOrigin()
        w.SetOrigin(list(value))
        self.trait_property_changed('origin', old, value)
        self.update_plane()

    def _on_interaction_event(self, obj, event):
        if not self._busy:
            self._busy = True
            self.update_plane()
            self._busy = False

    def _on_normal_set(self):
        w = self.widget
        w.place_widget(*self._bounds)
        w.update_traits()

    def _connect(self):
        """Wires up all the event handlers."""
        w = self.widget
        w.add_observer('InteractionEvent',
                       self._on_interaction_event)
        w.on_trait_change(self._on_normal_set, 'normal_to_x_axis')
        w.on_trait_change(self._on_normal_set, 'normal_to_y_axis')
        w.on_trait_change(self._on_normal_set, 'normal_to_z_axis')
        w.on_trait_change(self._on_interaction_event)

        for obj in (self.plane, w):
            obj.on_trait_change(self.render)
