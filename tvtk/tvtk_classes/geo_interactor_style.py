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

from tvtk.tvtk_classes.interactor_style_trackball_camera import InteractorStyleTrackballCamera


class GeoInteractorStyle(InteractorStyleTrackballCamera):
    """
    GeoInteractorStyle - Interaction for a globe
    
    Superclass: InteractorStyleTrackballCamera
    
    GeoInteractorStyle contains interaction capabilities for a
    geographic view including orbit, zoom, and tilt. It also includes a
    compass widget for changing view parameters.
    
    See Also:
    
    CompassWidget InteractorStyle
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoInteractorStyle, obj, update, **traits)
    
    lock_heading = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _lock_heading_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLockHeading,
                        self.lock_heading_)

    def _get_geo_camera(self):
        return wrap_vtk(self._vtk_obj.GetGeoCamera())
    geo_camera = traits.Property(_get_geo_camera, help=\
        """
        
        """
    )

    def get_ray_intersection(self, *args):
        """
        V.get_ray_intersection([float, float, float], [float, float, float],
             [float, float, float]) -> int
        C++: int GetRayIntersection(double origin[3], double direction[3],
             double intersection[3])"""
        ret = self._wrap_call(self._vtk_obj.GetRayIntersection, *args)
        return ret

    def redraw_rectangle(self):
        """
        V.redraw_rectangle()
        C++: void RedrawRectangle()"""
        ret = self._vtk_obj.RedrawRectangle()
        return ret
        

    def reset_camera(self):
        """
        V.reset_camera()
        C++: void ResetCamera()
        This can be used to set the camera to the standard view of the
        earth.
        """
        ret = self._vtk_obj.ResetCamera()
        return ret
        

    def reset_camera_clipping_range(self):
        """
        V.reset_camera_clipping_range()
        C++: void ResetCameraClippingRange()"""
        ret = self._vtk_obj.ResetCameraClippingRange()
        return ret
        

    def rubber_band_zoom(self):
        """
        V.rubber_band_zoom()
        C++: virtual void RubberBandZoom()"""
        ret = self._vtk_obj.RubberBandZoom()
        return ret
        

    def viewport_to_long_lat(self, *args):
        """
        V.viewport_to_long_lat(float, float, float, float)
        C++: void ViewportToLongLat(double x, double y, double &lon,
            double &lat)"""
        ret = self._wrap_call(self._vtk_obj.ViewportToLongLat, *args)
        return ret

    def viewport_to_world(self, *args):
        """
        V.viewport_to_world(float, float, float, float, float) -> int
        C++: int ViewportToWorld(double x, double y, double &wx,
            double &wy, double &wz)"""
        ret = self._wrap_call(self._vtk_obj.ViewportToWorld, *args)
        return ret

    def widget_interaction(self, *args):
        """
        V.widget_interaction(Object)
        C++: void WidgetInteraction(Object *caller)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.WidgetInteraction, *my_args)
        return ret

    def world_to_long_lat(self, *args):
        """
        V.world_to_long_lat(float, float, float, float, float)
        C++: void WorldToLongLat(double wx, double wy, double wz,
            double &lon, double &lat)"""
        ret = self._wrap_call(self._vtk_obj.WorldToLongLat, *args)
        return ret

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('enabled', 'GetEnabled'), ('use_timers',
    'GetUseTimers'), ('pick_color', 'GetPickColor'), ('handle_observers',
    'GetHandleObservers'), ('priority', 'GetPriority'), ('debug',
    'GetDebug'), ('motion_factor', 'GetMotionFactor'),
    ('key_press_activation', 'GetKeyPressActivation'), ('reference_count',
    'GetReferenceCount'), ('timer_duration', 'GetTimerDuration'),
    ('mouse_wheel_motion_factor', 'GetMouseWheelMotionFactor'),
    ('lock_heading', 'GetLockHeading'))
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'lock_heading', 'use_timers', 'key_press_activation_value',
    'motion_factor', 'mouse_wheel_motion_factor', 'pick_color',
    'priority', 'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoInteractorStyle, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'lock_heading',
            'use_timers'], [], ['key_press_activation_value', 'motion_factor',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration']),
            title='Edit GeoInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

