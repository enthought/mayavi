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


class ParallelCoordinatesInteractorStyle(InteractorStyleTrackballCamera):
    """
    ParallelCoordinatesInteractorStyle - interactive manipulation of
    the camera specialized for parallel coordinates
    
    Superclass: InteractorStyleTrackballCamera
    
    ParallelCoordinatesInteractorStyle allows the user to
    interactively manipulate (rotate, pan, zoomm etc.) the camera.
    Several events are overloaded from its superclass
    ParallelCoordinatesInteractorStyle, hence the mouse bindings are
    different. (The bindings keep the camera's view plane normal
    perpendicular to the x-y plane.) In summary the mouse events are as
    follows: + Left Mouse button triggers window level events + CTRL Left
    Mouse spins the camera around its view plane normal + SHIFT Left
    Mouse pans the camera + CTRL SHIFT Left Mouse dollys (a positional
    zoom) the camera + Middle mouse button pans the camera + Right mouse
    button dollys the camera. + SHIFT Right Mouse triggers pick events
    
    Note that the renderer's actors are not moved; instead the camera is
    moved.
    
    See Also:
    
    InteractorStyle InteractorStyleTrackballActor
    InteractorStyleJoystickCamera InteractorStyleJoystickActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParallelCoordinatesInteractorStyle, obj, update, **traits)
    
    def _get_cursor_current_position(self):
        return self._vtk_obj.GetCursorCurrentPosition()
    cursor_current_position = traits.Property(_get_cursor_current_position, help=\
        """
        
        """
    )

    def _get_cursor_last_position(self):
        return self._vtk_obj.GetCursorLastPosition()
    cursor_last_position = traits.Property(_get_cursor_last_position, help=\
        """
        
        """
    )

    def _get_cursor_start_position(self):
        return self._vtk_obj.GetCursorStartPosition()
    cursor_start_position = traits.Property(_get_cursor_start_position, help=\
        """
        
        """
    )

    def end_inspect(self):
        """
        V.end_inspect()
        C++: virtual void EndInspect()"""
        ret = self._vtk_obj.EndInspect()
        return ret
        

    def inspect(self, *args):
        """
        V.inspect(int, int)
        C++: virtual void Inspect(int x, int y)"""
        ret = self._wrap_call(self._vtk_obj.Inspect, *args)
        return ret

    def start_inspect(self, *args):
        """
        V.start_inspect(int, int)
        C++: virtual void StartInspect(int x, int y)"""
        ret = self._wrap_call(self._vtk_obj.StartInspect, *args)
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
    ('mouse_wheel_motion_factor', 'GetMouseWheelMotionFactor'))
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'use_timers', 'key_press_activation_value', 'motion_factor',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParallelCoordinatesInteractorStyle, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ParallelCoordinatesInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'use_timers'], [],
            ['key_press_activation_value', 'motion_factor',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration']),
            title='Edit ParallelCoordinatesInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParallelCoordinatesInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

