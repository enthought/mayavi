# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class ImplicitPlaneRepresentation(WidgetRepresentation):
    """
    ImplicitPlaneRepresentation - a class defining the representation
    for a ImplicitPlaneWidget2
    
    Superclass: WidgetRepresentation
    
    This class is a concrete representation for the
    ImplicitPlaneWidget2. It represents an infinite plane defined by a
    normal and point in the context of a bounding box. Through
    interaction with the widget, the plane can be manipulated by
    adjusting the plane normal or moving the origin point.
    
    To use this representation, you normally define a (plane) origin and
    (plane) normal. The place_widget() method is also used to intially
    position the representation.
    
    Caveats:
    
    This class, and ImplicitPlaneWidget2, are next generation VTK
    widgets. An earlier version of this functionality was defined in the
    class ImplicitPlaneWidget.
    
    See Also:
    
    ImplicitPlaneWidget2 ImplicitPlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitPlaneRepresentation, obj, update, **traits)
    
    normal_to_x_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a modified_event is invoked. This can
        be used to snap the plane to the axes if it is orginally not
        aligned.
        """
    )
    def _normal_to_x_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToXAxis,
                        self.normal_to_x_axis_)

    normal_to_z_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a modified_event is invoked. This can
        be used to snap the plane to the axes if it is orginally not
        aligned.
        """
    )
    def _normal_to_z_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToZAxis,
                        self.normal_to_z_axis_)

    outline_translation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to translate the bounding box by grabbing
        it with the left mouse button.
        """
    )
    def _outline_translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutlineTranslation,
                        self.outline_translation_)

    normal_to_y_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a modified_event is invoked. This can
        be used to snap the plane to the axes if it is orginally not
        aligned.
        """
    )
    def _normal_to_y_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToYAxis,
                        self.normal_to_y_axis_)

    outside_bounds = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to move the widget outside of the bounds
        specified in the initial place_widget() invocation.
        """
    )
    def _outside_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutsideBounds,
                        self.outside_bounds_)

    draw_plane = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
    )
    def _draw_plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawPlane,
                        self.draw_plane_)

    tubing = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a TubeFilter.
        """
    )
    def _tubing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTubing,
                        self.tubing_)

    scale_enabled = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to scale the widget with the mouse.
        """
    )
    def _scale_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleEnabled,
                        self.scale_enabled_)

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Get the origin of the plane.
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    representation_state = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Sets the visual appearance of the representation based on the
        state it is in. This state is usually the same as
        interaction_state.
        """
    )
    def _representation_state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepresentationState,
                        self.representation_state)

    normal = traits.Array(shape=(3,), value=(1.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Get the normal to the plane.
        """
    )
    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    def _get_edges_property(self):
        return wrap_vtk(self._vtk_obj.GetEdgesProperty())
    edges_property = traits.Property(_get_edges_property, help=\
        """
        Get the property of the intersection edges. (This property also
        applies to the edges when tubed.)
        """
    )

    def _get_interaction_state_max_value(self):
        return self._vtk_obj.GetInteractionStateMaxValue()
    interaction_state_max_value = traits.Property(_get_interaction_state_max_value, help=\
        """
        The interaction state may be set from a widget (e.g.,
        ImplicitPlaneWidget2) or other object. This controls how the
        interaction with the widget proceeds. Normally this method is
        used as part of a handshaking process with the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
    )

    def _get_interaction_state_min_value(self):
        return self._vtk_obj.GetInteractionStateMinValue()
    interaction_state_min_value = traits.Property(_get_interaction_state_min_value, help=\
        """
        The interaction state may be set from a widget (e.g.,
        ImplicitPlaneWidget2) or other object. This controls how the
        interaction with the widget proceeds. Normally this method is
        used as part of a handshaking process with the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
    )

    def _get_normal_property(self):
        return wrap_vtk(self._vtk_obj.GetNormalProperty())
    normal_property = traits.Property(_get_normal_property, help=\
        """
        Get the properties on the normal (line and cone).
        """
    )

    def _get_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetOutlineProperty())
    outline_property = traits.Property(_get_outline_property, help=\
        """
        Get the property of the outline.
        """
    )

    def get_plane(self, *args):
        """
        V.get_plane(Plane)
        C++: void GetPlane(Plane *plane)
        Get the implicit function for the plane. The user must provide
        the instance of the class Plane. Note that Plane is a
        subclass of ImplicitFunction, meaning that it can be used by a
        variety of filters to perform clipping, cutting, and selection of
        data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlane, *my_args)
        return ret

    def _get_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetPlaneProperty())
    plane_property = traits.Property(_get_plane_property, help=\
        """
        Get the plane properties. The properties of the plane when
        selected and unselected can be manipulated.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata that defines the plane. The polydata contains a
        single polygon that is clipped by the bounding box.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_poly_data_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetPolyDataAlgorithm())
    poly_data_algorithm = traits.Property(_get_poly_data_algorithm, help=\
        """
        Satisfies superclass API.  This returns a pointer to the
        underlying poly_data (which represents the plane).
        """
    )

    def _get_selected_normal_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedNormalProperty())
    selected_normal_property = traits.Property(_get_selected_normal_property, help=\
        """
        Get the properties on the normal (line and cone).
        """
    )

    def _get_selected_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedOutlineProperty())
    selected_outline_property = traits.Property(_get_selected_outline_property, help=\
        """
        Get the property of the outline.
        """
    )

    def _get_selected_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedPlaneProperty())
    selected_plane_property = traits.Property(_get_selected_plane_property, help=\
        """
        Get the plane properties. The properties of the plane when
        selected and unselected can be manipulated.
        """
    )

    def place_widget(self, *args):
        """
        V.place_widget([float, float, float, float, float, float])
        C++: virtual void PlaceWidget(double bounds[6])
        Methods to interface with the SliderWidget.
        """
        ret = self._wrap_call(self._vtk_obj.PlaceWidget, *args)
        return ret

    def set_interaction_state(self, *args):
        """
        V.set_interaction_state(int)
        C++: void SetInteractionState(int)
        The interaction state may be set from a widget (e.g.,
        ImplicitPlaneWidget2) or other object. This controls how the
        interaction with the widget proceeds. Normally this method is
        used as part of a handshaking process with the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
        ret = self._wrap_call(self._vtk_obj.SetInteractionState, *args)
        return ret

    def update_placement(self):
        """
        V.update_placement()
        C++: void UpdatePlacement(void)
        Satisfies the superclass API.  This will change the state of the
        widget to match changes that have been made to the underlying
        poly_data_source
        """
        ret = self._vtk_obj.UpdatePlacement()
        return ret
        

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('handle_size', 'GetHandleSize'),
    ('normal', 'GetNormal'), ('need_to_render', 'GetNeedToRender'),
    ('dragable', 'GetDragable'), ('normal_to_x_axis', 'GetNormalToXAxis'),
    ('draw_plane', 'GetDrawPlane'), ('normal_to_z_axis',
    'GetNormalToZAxis'), ('debug', 'GetDebug'), ('visibility',
    'GetVisibility'), ('normal_to_y_axis', 'GetNormalToYAxis'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('place_factor', 'GetPlaceFactor'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('outside_bounds', 'GetOutsideBounds'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('scale_enabled', 'GetScaleEnabled'),
    ('outline_translation', 'GetOutlineTranslation'),
    ('representation_state', 'GetRepresentationState'),
    ('reference_count', 'GetReferenceCount'), ('tubing', 'GetTubing'),
    ('pickable', 'GetPickable'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'draw_plane', 'global_warning_display',
    'need_to_render', 'normal_to_x_axis', 'normal_to_y_axis',
    'normal_to_z_axis', 'outline_translation', 'outside_bounds',
    'pickable', 'scale_enabled', 'tubing', 'use_bounds', 'visibility',
    'allocated_render_time', 'estimated_render_time', 'handle_size',
    'normal', 'origin', 'place_factor', 'render_time_multiplier',
    'representation_state'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitPlaneRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitPlaneRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['draw_plane', 'need_to_render', 'normal_to_x_axis',
            'normal_to_y_axis', 'normal_to_z_axis', 'outline_translation',
            'outside_bounds', 'scale_enabled', 'tubing', 'use_bounds',
            'visibility'], [], ['allocated_render_time', 'estimated_render_time',
            'handle_size', 'normal', 'origin', 'place_factor',
            'render_time_multiplier', 'representation_state']),
            title='Edit ImplicitPlaneRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitPlaneRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

