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

from tvtk.tvtk_classes.interactor_style import InteractorStyle


class InteractorStyleSwitch(InteractorStyle):
    """
    InteractorStyleSwitch - class to swap between interactory styles
    
    Superclass: InteractorStyle
    
    The class InteractorStyleSwitch allows handles interactively
    switching between four interactor styles -- joystick actor, joystick
    camera, trackball actor, and trackball camera.  Type 'j' or 't' to
    select joystick or trackball, and type 'c' or 'a' to select camera or
    actor. The default interactor style is joystick camera.
    
    See Also:
    
    InteractorStyleJoystickActor InteractorStyleJoystickCamera
    InteractorStyleTrackballActor InteractorStyleTrackballCamera
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleSwitch, obj, update, **traits)
    
    def get_current_style(self):
        """
        V.get_current_style() -> InteractorStyle
        C++: InteractorStyle *GetCurrentStyle()
        Set/Get current style
        """
        ret = wrap_vtk(self._vtk_obj.GetCurrentStyle())
        return ret
        

    def set_current_style_to_joystick_camera(self):
        """
        V.set_current_style_to_joystick_camera()
        C++: void SetCurrentStyleToJoystickCamera()
        Set/Get current style
        """
        self._vtk_obj.SetCurrentStyleToJoystickCamera()

    def set_current_style_to_trackball_actor(self):
        """
        V.set_current_style_to_trackball_actor()
        C++: void SetCurrentStyleToTrackballActor()
        Set/Get current style
        """
        self._vtk_obj.SetCurrentStyleToTrackballActor()

    def set_current_style_to_trackball_camera(self):
        """
        V.set_current_style_to_trackball_camera()
        C++: void SetCurrentStyleToTrackballCamera()
        Set/Get current style
        """
        self._vtk_obj.SetCurrentStyleToTrackballCamera()

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('use_timers', 'GetUseTimers'),
    ('enabled', 'GetEnabled'), ('pick_color', 'GetPickColor'),
    ('key_press_activation', 'GetKeyPressActivation'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('handle_observers',
    'GetHandleObservers'), ('reference_count', 'GetReferenceCount'),
    ('timer_duration', 'GetTimerDuration'), ('mouse_wheel_motion_factor',
    'GetMouseWheelMotionFactor'))
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'use_timers', 'key_press_activation_value',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleSwitch, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleSwitch properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'use_timers'], [],
            ['key_press_activation_value', 'mouse_wheel_motion_factor',
            'pick_color', 'priority', 'timer_duration']),
            title='Edit InteractorStyleSwitch properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleSwitch properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

