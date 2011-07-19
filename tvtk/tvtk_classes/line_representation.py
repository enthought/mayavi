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


class LineRepresentation(WidgetRepresentation):
    """
    LineRepresentation - a class defining the representation for a
    LineWidget2
    
    Superclass: WidgetRepresentation
    
    This class is a concrete representation for the LineWidget2. It
    represents a straight line with three handles: one at the beginning
    and ending of the line, and one used to translate the line. Through
    interaction with the widget, the line representation can be
    arbitrarily placed in the 3d space.
    
    To use this representation, you normally specify the position of the
    two end points (either in world or display coordinates). The
    place_widget() method is also used to intially position the
    representation.
    
    Caveats:
    
    This class, and LineWidget2, are next generation VTK widgets. An
    earlier version of this functionality was defined in the class
    LineWidget.
    
    See Also:
    
    LineWidget2 LineWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLineRepresentation, obj, update, **traits)
    
    distance_annotation_visibility = tvtk_base.false_bool_trait(help=\
        """
        Show the distance between the points
        """
    )
    def _distance_annotation_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceAnnotationVisibility,
                        self.distance_annotation_visibility_)

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

    point1_world_position = traits.Array(shape=(3,), value=(0.5, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )
    def _point1_world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1WorldPosition,
                        self.point1_world_position)

    tolerance = traits.Trait(5, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the line or end
        point to be active.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    point1display_position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )
    def _point1display_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1DisplayPosition,
                        self.point1display_position)

    point2display_position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )
    def _point2display_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2DisplayPosition,
                        self.point2display_position)

    distance_annotation_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Specify the format to use for labelling the angle. Note that an
        empty string results in no label, or a format string without a
        "%" character will not print the angle value.
        """
    )
    def _distance_annotation_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceAnnotationFormat,
                        self.distance_annotation_format)

    resolution = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the resolution (number of subdivisions) of the line. A
        line with resolution greater than one is useful when points along
        the line are desired; e.g., generating a rake of streamlines.
        """
    )
    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    point2_world_position = traits.Array(shape=(3,), value=(-0.5, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )
    def _point2_world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2WorldPosition,
                        self.point2_world_position)

    def _get_distance(self):
        return self._vtk_obj.GetDistance()
    distance = traits.Property(_get_distance, help=\
        """
        Get the distance between the points.
        """
    )

    def _get_distance_annotation_property(self):
        return wrap_vtk(self._vtk_obj.GetDistanceAnnotationProperty())
    distance_annotation_property = traits.Property(_get_distance_annotation_property, help=\
        """
        Get the distance annotation property
        """
    )

    def _get_end_point2_property(self):
        return wrap_vtk(self._vtk_obj.GetEndPoint2Property())
    end_point2_property = traits.Property(_get_end_point2_property, help=\
        """
        Get the end-point (sphere) properties. The properties of the
        end-points when selected and unselected can be manipulated.
        """
    )

    def _get_end_point_property(self):
        return wrap_vtk(self._vtk_obj.GetEndPointProperty())
    end_point_property = traits.Property(_get_end_point_property, help=\
        """
        Get the end-point (sphere) properties. The properties of the
        end-points when selected and unselected can be manipulated.
        """
    )

    def _get_interaction_state_max_value(self):
        return self._vtk_obj.GetInteractionStateMaxValue()
    interaction_state_max_value = traits.Property(_get_interaction_state_max_value, help=\
        """
        The interaction state may be set from a widget (e.g.,
        LineWidget2) or other object. This controls how the
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
        LineWidget2) or other object. This controls how the
        interaction with the widget proceeds. Normally this method is
        used as part of a handshaking process with the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
    )

    def _get_line_handle_representation(self):
        return wrap_vtk(self._vtk_obj.GetLineHandleRepresentation())
    line_handle_representation = traits.Property(_get_line_handle_representation, help=\
        """
        Get the three handle representations used for the LineWidget2.
        """
    )

    def _get_line_property(self):
        return wrap_vtk(self._vtk_obj.GetLineProperty())
    line_property = traits.Property(_get_line_property, help=\
        """
        Get the line properties. The properties of the line when selected
        and unselected can be manipulated.
        """
    )

    def _get_point1_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Representation())
    point1_representation = traits.Property(_get_point1_representation, help=\
        """
        Get the three handle representations used for the LineWidget2.
        """
    )

    def _get_point2_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Representation())
    point2_representation = traits.Property(_get_point2_representation, help=\
        """
        Get the three handle representations used for the LineWidget2.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Retrieve the polydata (including points) that defines the line. 
        The polydata consists of n+1 points, where n is the resolution of
        the line. These point values are guaranteed to be up-to-date
        whenever any one of the three handles are moved. To use this
        method, the user provides the PolyData as an input argument,
        and the points and polyline are copied into it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_selected_end_point2_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedEndPoint2Property())
    selected_end_point2_property = traits.Property(_get_selected_end_point2_property, help=\
        """
        Get the end-point (sphere) properties. The properties of the
        end-points when selected and unselected can be manipulated.
        """
    )

    def _get_selected_end_point_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedEndPointProperty())
    selected_end_point_property = traits.Property(_get_selected_end_point_property, help=\
        """
        Get the end-point (sphere) properties. The properties of the
        end-points when selected and unselected can be manipulated.
        """
    )

    def _get_selected_line_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedLineProperty())
    selected_line_property = traits.Property(_get_selected_line_property, help=\
        """
        Get the line properties. The properties of the line when selected
        and unselected can be manipulated.
        """
    )

    def _get_text_actor(self):
        return wrap_vtk(self._vtk_obj.GetTextActor())
    text_actor = traits.Property(_get_text_actor, help=\
        """
        Get the text actor
        """
    )

    def instantiate_handle_representation(self):
        """
        V.instantiate_handle_representation()
        C++: void InstantiateHandleRepresentation()
        This method is used to specify the type of handle representation
        to use for the three internal HandleWidgets within
        LineWidget2. To use this method, create a dummy
        HandleWidget (or subclass), and then invoke this method with
        this dummy. Then the LineRepresentation uses this dummy to
        clone three HandleWidgets of the same type. Make sure you set
        the handle representation before the widget is enabled. (The
        method instantiate_handle_representation() is invoked by the
        LineWidget2.)
        """
        ret = self._vtk_obj.InstantiateHandleRepresentation()
        return ret
        

    def place_widget(self, *args):
        """
        V.place_widget([float, float, float, float, float, float])
        C++: virtual void PlaceWidget(double bounds[6])
        These are methods that satisfy WidgetRepresentation's API.
        """
        ret = self._wrap_call(self._vtk_obj.PlaceWidget, *args)
        return ret

    def set_distance_annotation_scale(self, *args):
        """
        V.set_distance_annotation_scale([float, float, float])
        C++: virtual void SetDistanceAnnotationScale(double scale[3])
        Scale text (font size along each dimension).
        """
        ret = self._wrap_call(self._vtk_obj.SetDistanceAnnotationScale, *args)
        return ret

    def set_handle_representation(self, *args):
        """
        V.set_handle_representation(PointHandleRepresentation3D)
        C++: void SetHandleRepresentation(
            PointHandleRepresentation3D *handle)
        This method is used to specify the type of handle representation
        to use for the three internal HandleWidgets within
        LineWidget2. To use this method, create a dummy
        HandleWidget (or subclass), and then invoke this method with
        this dummy. Then the LineRepresentation uses this dummy to
        clone three HandleWidgets of the same type. Make sure you set
        the handle representation before the widget is enabled. (The
        method instantiate_handle_representation() is invoked by the
        LineWidget2.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetHandleRepresentation, *my_args)
        return ret

    def set_interaction_state(self, *args):
        """
        V.set_interaction_state(int)
        C++: void SetInteractionState(int)
        The interaction state may be set from a widget (e.g.,
        LineWidget2) or other object. This controls how the
        interaction with the widget proceeds. Normally this method is
        used as part of a handshaking process with the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
        ret = self._wrap_call(self._vtk_obj.SetInteractionState, *args)
        return ret

    def set_line_color(self, *args):
        """
        V.set_line_color(float, float, float)
        C++: void SetLineColor(double r, double g, double b)
        Convenience method to set the line color. Ideally one should use
        get_line_property()->_set_color().
        """
        ret = self._wrap_call(self._vtk_obj.SetLineColor, *args)
        return ret

    _updateable_traits_ = \
    (('distance_annotation_format', 'GetDistanceAnnotationFormat'),
    ('allocated_render_time', 'GetAllocatedRenderTime'),
    ('point1display_position', 'GetPoint1DisplayPosition'),
    ('need_to_render', 'GetNeedToRender'), ('point2display_position',
    'GetPoint2DisplayPosition'), ('visibility', 'GetVisibility'),
    ('distance_annotation_visibility', 'GetDistanceAnnotationVisibility'),
    ('debug', 'GetDebug'), ('place_factor', 'GetPlaceFactor'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('point1_world_position', 'GetPoint1WorldPosition'), ('use_bounds',
    'GetUseBounds'), ('handle_size', 'GetHandleSize'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('resolution',
    'GetResolution'), ('point2_world_position', 'GetPoint2WorldPosition'),
    ('representation_state', 'GetRepresentationState'),
    ('reference_count', 'GetReferenceCount'), ('pickable', 'GetPickable'),
    ('tolerance', 'GetTolerance'), ('dragable', 'GetDragable'))
    
    _full_traitnames_list_ = \
    (['debug', 'distance_annotation_visibility', 'dragable',
    'global_warning_display', 'need_to_render', 'pickable', 'use_bounds',
    'visibility', 'allocated_render_time', 'distance_annotation_format',
    'estimated_render_time', 'handle_size', 'place_factor',
    'point1_world_position', 'point1display_position',
    'point2_world_position', 'point2display_position',
    'render_time_multiplier', 'representation_state', 'resolution',
    'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LineRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['distance_annotation_visibility', 'need_to_render',
            'use_bounds', 'visibility'], [], ['allocated_render_time',
            'distance_annotation_format', 'estimated_render_time', 'handle_size',
            'place_factor', 'point1_world_position', 'point1display_position',
            'point2_world_position', 'point2display_position',
            'render_time_multiplier', 'representation_state', 'resolution',
            'tolerance']),
            title='Edit LineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

