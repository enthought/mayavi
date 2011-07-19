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

from tvtk.tvtk_classes.continuous_value_widget_representation import ContinuousValueWidgetRepresentation


class CompassRepresentation(ContinuousValueWidgetRepresentation):
    """
    CompassRepresentation - provide a compass
    
    Superclass: ContinuousValueWidgetRepresentation
    
    This class is used to represent and render a compass.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompassRepresentation, obj, update, **traits)
    
    distance = traits.Float(100000.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistance,
                        self.distance)

    heading = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _heading_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeading,
                        self.heading)

    tilt = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _tilt_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTilt,
                        self.tilt)

    def _get_label_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelProperty())
    label_property = traits.Property(_get_label_property, help=\
        """
        Set/Get the properties for the label and title text.
        """
    )

    def _get_point1_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Coordinate())
    point1_coordinate = traits.Property(_get_point1_coordinate, help=\
        """
        Position the first end point of the slider. Note that this point
        is an instance of Coordinate, meaning that Point 1 can be
        specified in a variety of coordinate systems, and can even be
        relative to another point. To set the point, you'll want to get
        the point1_coordinate and then invoke the necessary methods to put
        it into the correct coordinate system and set the correct initial
        value.
        """
    )

    def _get_point2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Coordinate())
    point2_coordinate = traits.Property(_get_point2_coordinate, help=\
        """
        Position the second end point of the slider. Note that this point
        is an instance of Coordinate, meaning that Point 1 can be
        specified in a variety of coordinate systems, and can even be
        relative to another point. To set the point, you'll want to get
        the point2_coordinate and then invoke the necessary methods to put
        it into the correct coordinate system and set the correct initial
        value.
        """
    )

    def _get_ring_property(self):
        return wrap_vtk(self._vtk_obj.GetRingProperty())
    ring_property = traits.Property(_get_ring_property, help=\
        """
        Get the slider properties. The properties of the slider when
        selected and unselected can be manipulated.
        """
    )

    def _get_selected_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedProperty())
    selected_property = traits.Property(_get_selected_property, help=\
        """
        Get the selection property. This property is used to modify the
        appearance of selected objects (e.g., the slider).
        """
    )

    def distance_widget_interaction(self, *args):
        """
        V.distance_widget_interaction([float, float])
        C++: virtual void DistanceWidgetInteraction(double eventPos[2])
        Methods to interface with the SliderWidget. The place_widget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
        """
        ret = self._wrap_call(self._vtk_obj.DistanceWidgetInteraction, *args)
        return ret

    def end_distance(self):
        """
        V.end_distance()
        C++: virtual void EndDistance()"""
        ret = self._vtk_obj.EndDistance()
        return ret
        

    def end_tilt(self):
        """
        V.end_tilt()
        C++: virtual void EndTilt()"""
        ret = self._vtk_obj.EndTilt()
        return ret
        

    def tilt_widget_interaction(self, *args):
        """
        V.tilt_widget_interaction([float, float])
        C++: virtual void TiltWidgetInteraction(double eventPos[2])
        Methods to interface with the SliderWidget. The place_widget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
        """
        ret = self._wrap_call(self._vtk_obj.TiltWidgetInteraction, *args)
        return ret

    def update_distance(self, *args):
        """
        V.update_distance(float)
        C++: virtual void UpdateDistance(double time)"""
        ret = self._wrap_call(self._vtk_obj.UpdateDistance, *args)
        return ret

    def update_tilt(self, *args):
        """
        V.update_tilt(float)
        C++: virtual void UpdateTilt(double time)"""
        ret = self._wrap_call(self._vtk_obj.UpdateTilt, *args)
        return ret

    _updateable_traits_ = \
    (('distance', 'GetDistance'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('handle_size', 'GetHandleSize'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('tilt',
    'GetTilt'), ('dragable', 'GetDragable'), ('value', 'GetValue'),
    ('use_bounds', 'GetUseBounds'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('visibility', 'GetVisibility'),
    ('need_to_render', 'GetNeedToRender'), ('reference_count',
    'GetReferenceCount'), ('place_factor', 'GetPlaceFactor'), ('pickable',
    'GetPickable'), ('heading', 'GetHeading'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'distance', 'estimated_render_time', 'handle_size', 'heading',
    'place_factor', 'render_time_multiplier', 'tilt', 'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompassRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CompassRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'distance', 'estimated_render_time',
            'handle_size', 'heading', 'place_factor', 'render_time_multiplier',
            'tilt', 'value']),
            title='Edit CompassRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompassRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

