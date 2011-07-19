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


class InteractorStyleJoystickActor(InteractorStyle):
    """
    InteractorStyleJoystickActor - manipulate objects in the scene
    independently of one another
    
    Superclass: InteractorStyle
    
    The class InteractorStyleJoystickActor allows the user to interact
    with (rotate, zoom, etc.) separate objects in the scene independent
    of each other.  The position of the mouse relative to the center of
    the object determines the speed of the object's motion.  The mouse's
    velocity detemines the acceleration of the object's motion, so the
    object will continue moving even when the mouse is not moving. For a
    3-button mouse, the left button is for rotation, the right button for
    zooming, the middle button for panning, and ctrl + left button for
    spinning.  (With fewer mouse buttons, ctrl + shift + left button is
    for zooming, and shift + left button is for panning.)
    
    See Also:
    
    InteractorStyleJoystickCamera InteractorStyleTrackballActor
    InteractorStyleTrackballCamera
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleJoystickActor, obj, update, **traits)
    
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
            return super(InteractorStyleJoystickActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleJoystickActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'use_timers'], [],
            ['key_press_activation_value', 'mouse_wheel_motion_factor',
            'pick_color', 'priority', 'timer_duration']),
            title='Edit InteractorStyleJoystickActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleJoystickActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

