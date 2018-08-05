"""A component that provides a selection of implicit widgets
to be used by various modules.
"""
# Author: Suyog Dutt Jain <suyog.jain@aero.iitb.ac.in>
#         Prabhu Ramachandran <prabhu at aero.iitb.ac.in>
# Copyright (c) 2009-2015, Enthought, Inc.
# License: BSD Style.

import pickle

from traits.api import (Instance, Trait, Bool, TraitMap, Enum, Dict,
                        Str, Int, Any)
from traitsui.api import View, Group, Item
from tvtk.api import tvtk
from apptools.persistence.state_pickler import set_state

from mayavi.core.component import Component
from mayavi.core.utils import DataSetHelper


######################################################################
# `ImplicitWidgets` class.
######################################################################
class ImplicitWidgets(Component):

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The widget type to use.
    widget_mode = Enum('Box', 'Sphere', 'Plane','ImplicitPlane',
                       desc='the implicit widget to use')

    # The actual poly data source widget.
    widget = Instance(tvtk.ThreeDWidget, record=True)

    update_mode = Trait('semi-interactive',
                        TraitMap({'interactive':'InteractionEvent',
                                  'semi-interactive': 'EndInteractionEvent'}),
                        desc='speed at which the data should be updated')

    implicit_function = Instance(tvtk.ImplicitFunction, allow_none=False)

    ########################################
    # Private traits.

    _first = Bool(True)
    _busy = Bool(False)
    _observer_id = Int(-1)
    _bounds = Any

    # The actual widgets.
    _widget_dict = Dict(Str, Instance(tvtk.ThreeDWidget,
                        allow_none=False))

    # The actual implicit functions.
    _implicit_function_dict = Dict(Str, Instance(tvtk.ImplicitFunction,
                                   allow_none=False))

    ########################################
    # View related traits.
    ########################################
     # Create the UI for the traits.
    view = View(Group(Item(name='widget_mode'), Item(name='widget',
                            style='custom', resizable=True),
                            label='Widget Source', show_labels=False),
                            resizable=True)

    #####################################################################
    # `object` interface
    ######################################################################
    def __init__(self, **traits):
        # Call parent class' init.
        super(ImplicitWidgets, self).__init__(**traits)

        # Initialize the source to the default widget's instance from
        # the dictionary if needed.
        if 'widget_mode' not in traits:
            self._widget_mode_changed(self.widget_mode)

    ######################################################################
    # `Base` interface
    ######################################################################
    def __get_pure_state__(self):
        d = super(ImplicitWidgets, self).__get_pure_state__()
        for attr in ('_first', '_busy', '_observer_id', 'widget',
                     'implicit_function'):
            d.pop(attr, None)
        # The box widget requires a transformation matrix to be pickled.
        tfm = tvtk.Transform()
        w = self._widget_dict['Box']
        w.get_transform(tfm)
        d['matrix'] = pickle.dumps(tfm.matrix)
        return d

    def __set_pure_state__(self, state):
        # Pop the transformation matrix for the box widget.
        mat = state.pop('matrix')
        # Now set their state.
        set_state(self, state, first=['widget_mode'], ignore=['*'])
        # Set state of rest of the attributes ignoring the widget_mode.
        set_state(self, state, ignore=['widget_mode'])

        # Set the transformation for Box widget.
        tfm = tvtk.Transform()
        tfm.set_matrix(pickle.loads(mat))
        w = self._widget_dict['Box']
        w.set_transform(tfm)

        # Some widgets need some cajoling to get their setup right.
        w = self.widget
        # Set the input.
        if len(self.inputs) > 0:
            self.configure_input(w, self.inputs[0].outputs[0])
        w.update_traits()
        mode = self.widget_mode
        if mode == 'Plane':
            wd = state._widget_dict[mode]
            w.origin = wd.origin
            w.normal = wd.normal
            w.update_placement()
        self.update_implicit_function()
        # Set the widgets trait so that the widget is rendered if needed.
        self.widgets = [w]

    ######################################################################
    # `Component` interface
    ######################################################################
    def setup_pipeline(self):
        """Override this method so that it *creates* the tvtk
        pipeline.
        """
        # Setup the widgets.
        self.widgets = [self.widget]

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
        self._bounds = dsh.get_bounds()

        if self._first:
            w.place_widget(self._bounds)
            self._first = False

        # Set our output.
        if self.outputs != [inp]:
            self.outputs = [inp]
        else:
            self.data_changed = True

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
    def update_implicit_function(self):
        """Update the implicit_function from the widget data.
        """
        dispatch = {'Sphere': 'get_sphere', 'Box': 'get_planes',
                    'Plane': 'get_plane', 'ImplicitPlane': 'get_plane'}
        method = getattr(self.widget, dispatch[self.widget_mode])
        method(self.implicit_function)

    ######################################################################
    # Non-public traits.
    ######################################################################
    def _widget_changed(self, old, value):
        if len(self.inputs) > 0:
            self.configure_input(value, self.inputs[0].outputs[0])
            if self._bounds:
                value.place_widget(self._bounds)
            else:
                value.place_widget()
        self.implicit_function = self._implicit_function_dict[self.widget_mode]

        if old is not None:
            self._connect(old, remove=True)
        self._connect(value, remove=False)
        self.widgets = [value]

    def _connect(self, value, remove=False):
        """Wire up event handlers or tear them down given a widget
        `value`.  If `remove` is True, then tear them down."""
        if remove and self._observer_id > 0:
                value.remove_observer(self._observer_id)
        else:
            self._observer_id = value.add_observer(self.update_mode_,
                                                   self._on_interaction_event)
        if isinstance(value, tvtk.PlaneWidget) or \
            isinstance(value, tvtk.ImplicitPlaneWidget):
            value.on_trait_change(self._on_alignment_set,
                                  'normal_to_x_axis', remove=remove)
            value.on_trait_change(self._on_alignment_set,
                                  'normal_to_y_axis', remove=remove)
            value.on_trait_change(self._on_alignment_set,
                                  'normal_to_z_axis', remove=remove)

        value.on_trait_change(self._on_widget_trait_changed,
                              remove=remove)
        value.on_trait_change(self.render, remove=remove)

    def _on_interaction_event(self, obj, event):
        self.update_implicit_function()

    def _update_mode_changed(self, old, new):
        w = self.widget
        if w is not None:
            w.remove_observer(self._observer_id)
            self._observer_id = w.add_observer(self.update_mode_,
                    self._on_interaction_event)

            w.on_trait_change(self.render)
            self.render()

    def _on_widget_trait_changed(self):
        if (not self._busy) and (self.update_mode != 'non-interactive'):
            self._busy = True
            self.implicit_function = self._implicit_function_dict[self.widget_mode]
            self.update_implicit_function()
            self.render()
            self._busy = False

    def _on_alignment_set(self):
        """Event handler when the widget's normal is reset (if
        applicable)."""
        w = self.widget
        w.place_widget(self._bounds)
        w.update_traits()
        self.render()

    def _scene_changed(self, old, new):
        super(ImplicitWidgets, self)._scene_changed(old, new)
        self._foreground_changed_for_scene(None, new.foreground)

    def _widget_mode_changed(self, value):
        """This method is invoked (automatically) when the `source`
        trait is changed.
        """
        self.widget = self._widget_dict[self.widget_mode]

    def __widget_dict_default(self):
        """Default value for source dict."""
        w = {'Box':tvtk.BoxWidget(place_factor = 0.9),
             'Sphere':tvtk.SphereWidget(place_factor = 0.9),
             'Plane':tvtk.PlaneWidget(place_factor = 0.9),
             'ImplicitPlane':
                tvtk.ImplicitPlaneWidget(place_factor=0.9,
                                         draw_plane=False)}
        return w

    def __implicit_function_dict_default(self):
        """Default value for source dict."""
        ip = {'Box':tvtk.Planes(),
              'Sphere':tvtk.Sphere(),
              'Plane':tvtk.Plane(),
              'ImplicitPlane': tvtk.Plane()}
        return ip
