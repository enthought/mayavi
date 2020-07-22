"""A component that provides a selection of poly data source widgets
to be used by various modules.

"""
# Author: Prabhu Ramachandran <prabhu_r@users.sf.net>
# Copyright (c) 2005-2020, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from traits.api import Event, Instance, List, Trait, Bool
from traitsui.api import View, Group, Item, InstanceEditor
from tvtk.api import tvtk
from tvtk.tvtk_base import PrefixList
from apptools.persistence.state_pickler import set_state

# Local imports.
from mayavi.core.common import handle_children_state
from mayavi.core.component import Component
from mayavi.core.utils import DataSetHelper

######################################################################
# `SourceWidget` class.
######################################################################
class SourceWidget(Component):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual poly data source widget.
    widget = Instance(tvtk.ThreeDWidget, record=True)

    # Specifies the updation mode of the poly_data attribute.  There
    # are three modes: 1) 'interactive' -- the poly_data attribute is
    # updated as the widget is interacted with, 2) 'semi-interactive'
    # -- poly_data attribute is updated when the traits of the widget
    # change and when the widget interaction is complete, 3)
    # 'non-interactive' -- poly_data is updated only explicitly at
    # users request by calling `object.update_poly_data`.
    update_mode = PrefixList(
        ['interactive', 'semi-interactive', 'non-interactive'],
        default_value='interactive',
        desc='the speed at which the poly data is updated')

    # A list of predefined glyph sources that can be used.
    widget_list = List(tvtk.Object, record=False)

    # The poly data that the widget manages.
    poly_data = Instance(tvtk.PolyData, args=())

    ########################################
    # Private traits.

    _first = Bool(True)
    _busy = Bool(False)
    _unpickling = Bool(False)
    _bounds = List

    ########################################
    # View related traits.

    view = View(Group(Item(name='widget', style='custom', resizable=True,
                           editor=InstanceEditor(name='widget_list')),
                      label='Source Widget',
                      show_labels=False,
                      ),
                resizable=True,
                )

    ######################################################################
    # `Base` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(SourceWidget, self).__get_pure_state__()
        for attr in ('poly_data', '_unpickling', '_first', '_busy'):
            d.pop(attr, None)
        return d

    def __set_pure_state__(self, state):
        self._unpickling = True
        # First create all the allowed widgets in the widget_list attr.
        handle_children_state(self.widget_list, state.widget_list)
        # Now set their state.
        set_state(self, state, first=['widget_list'], ignore=['*'])
        # Set the widget attr depending on value saved.
        m = [x.__class__.__name__ for x in self.widget_list]
        w_c_name = state.widget.__metadata__['class_name']
        w = self.widget = self.widget_list[m.index(w_c_name)]
        # Set the input.
        if len(self.inputs) > 0:
            self.configure_input(w, self.inputs[0].outputs[0])
        # Fix for the point widget.
        if w_c_name == 'PointWidget':
            w.place_widget()
        # Set state of rest of the attributes ignoring the widget_list.
        set_state(self, state, ignore=['widget_list'])
        # Some widgets need some cajoling to get their setup right.
        w.update_traits()
        if w_c_name == 'PlaneWidget':
            w.origin = state.widget.origin
            w.normal = state.widget.normal
            w.center = state.widget.center
            w.update_placement()
            w.get_poly_data(self.poly_data)
        elif w_c_name == 'SphereWidget':
            # XXX: This hack is necessary because the sphere widget
            # does not update its poly data even when its ivars are
            # set (plus it does not have an update_placement method
            # which is a bug).  So we force this by creating a similar
            # sphere source and copy its output.
            s = tvtk.SphereSource(center=w.center, radius=w.radius,
                                  theta_resolution=w.theta_resolution,
                                  phi_resolution=w.phi_resolution,
                                  lat_long_tessellation=True)
            s.update()
            self.poly_data.shallow_copy(s.output)
        else:
            w.get_poly_data(self.poly_data)
        self._unpickling = False
        # Set the widgets trait so that the widget is rendered if needed.
        self.widgets = [w]

    ######################################################################
    # `Component` interface
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
        # Setup the glyphs.
        sources = [tvtk.SphereWidget(theta_resolution=8, phi_resolution=6),
                   tvtk.LineWidget(clamp_to_bounds=False),
                   tvtk.PlaneWidget(),
                   tvtk.PointWidget(outline=False, x_shadows=False,
                                    y_shadows=False, z_shadows=False),
                   ]
        self.widget_list = sources
        # The 'widgets' trait is set in the '_widget_changed' handler.
        self.widget = sources[0]

        for s in sources:
            self._connect(s)

    def update_pipeline(self):
        """Override this method so that it *updates* the tvtk pipeline
        when data upstream is known to have changed.

        This method is invoked (automatically) when any of the inputs
        sends a `pipeline_changed` event.
        """
        if len(self.inputs) == 0:
            return
        inp = self.inputs[0].outputs[0]
        w = self.widget
        self.configure_input(w, inp)
        dsh = DataSetHelper(self.inputs[0].outputs[0])
        b = dsh.get_bounds()
        self._bounds = list(b)
        if self._first:
            w.place_widget(b)
            self._first = False

        # If the dataset is effectively 2D switch to using the line
        # widget since that works best.
        l = [(b[1]-b[0]), (b[3]-b[2]), (b[5]-b[4])]
        max_l = max(l)
        for i, x in enumerate(l):
            if x/max_l < 1.0e-6:
                w = self.widget = self.widget_list[1]
                w.clamp_to_bounds = True
                w.align = ['z_axis', 'z_axis', 'y_axis'][i]
                break

        # Set our output.
        w.get_poly_data(self.poly_data)
        self.outputs = [self.poly_data]

        self.pipeline_changed = True

    def update_data(self):
        """Override this method so that it flushes the vtk pipeline if
        that is necessary.

        This method is invoked (automatically) when any of the inputs
        sends a `data_changed` event.
        """
        self.data_changed = True

    ######################################################################
    # `SourceWidget` interface
    ######################################################################
    def update_poly_data(self):
        self.widget.get_poly_data(self.poly_data)

    ######################################################################
    # Non-public traits.
    ######################################################################
    def _widget_changed(self, value):
        # If we are being unpickled do nothing.
        if self._unpickling:
            return
        if value not in self.widget_list:
            classes = [o.__class__ for o in self.widget_list]
            vc = value.__class__
            self._connect(value)
            if vc in classes:
                self.widget_list[classes.index(vc)] = value
            else:
                self.widget_list.append(value)

        recorder = self.recorder
        if recorder is not None:
            idx = self.widget_list.index(value)
            name = recorder.get_script_id(self)
            lhs = '%s.widget'%name
            rhs = '%s.widget_list[%d]'%(name, idx)
            recorder.record('%s = %s'%(lhs, rhs))

        if len(self.inputs) > 0:
            self.configure_input(value, self.inputs[0].outputs[0])
            value.place_widget(self._bounds)

        value.on_trait_change(self.render)
        self.widgets = [value]

    def _update_mode_changed(self, value):
        if value in ['interactive', 'semi-interactive']:
            self.update_poly_data()
            self.render()

    def _on_interaction_event(self, obj, event):
        if (not self._busy) and (self.update_mode == 'interactive'):
            self._busy = True
            self.update_poly_data()
            self._busy = False

    def _on_widget_trait_changed(self):
        if (not self._busy) and (self.update_mode != 'non-interactive'):
            self._busy = True
            # This render call forces any changes to the trait to be
            # rendered only then will updating the poly data make
            # sense.
            self.render()
            self.update_poly_data()
            self._busy = False

    def _on_alignment_set(self):
        w = self.widget
        w.place_widget(self._bounds)
        w.update_traits()

    def _connect(self, obj):
        """Wires up all the event handlers."""
        obj.add_observer('InteractionEvent',
                         self._on_interaction_event)
        if isinstance(obj, tvtk.PlaneWidget):
            obj.on_trait_change(self._on_alignment_set, 'normal_to_x_axis')
            obj.on_trait_change(self._on_alignment_set, 'normal_to_y_axis')
            obj.on_trait_change(self._on_alignment_set, 'normal_to_z_axis')
        elif isinstance(obj, tvtk.LineWidget):
            obj.on_trait_change(self._on_alignment_set, 'align')

        # Setup the widgets colors.
        fg = (1,1,1)
        if self.scene is not None:
            fg = self.scene.foreground
        self._setup_widget_colors(obj, fg)

        obj.on_trait_change(self._on_widget_trait_changed)
        obj.on_trait_change(self.render)

    def _setup_widget_colors(self, widget, color):
        trait_names = widget.trait_names()
        props = [x for x in trait_names
                 if 'property' in x and 'selected' not in x]
        sel_props = [x for x in trait_names
                     if 'property' in x and 'selected' in x]
        for p in props:
            setattr(getattr(widget, p), 'color', color)
            setattr(getattr(widget, p), 'line_width', 2)
        for p in sel_props:
            # Set the selected color to 'red'.
            setattr(getattr(widget, p), 'color', (1,0,0))
            setattr(getattr(widget, p), 'line_width', 2)
        self.render()

    def _foreground_changed_for_scene(self, old, new):
        # Change the default color for the actor.
        for w in self.widget_list:
            self._setup_widget_colors(w, new)
        self.render()

    def _scene_changed(self, old, new):
        super(SourceWidget, self)._scene_changed(old, new)
        self._foreground_changed_for_scene(None, new.foreground)
