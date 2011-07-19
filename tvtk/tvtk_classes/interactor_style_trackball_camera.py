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


class InteractorStyleTrackballCamera(InteractorStyle):
    """
    InteractorStyleTrackballCamera - interactive manipulation of the
    camera
    
    Superclass: InteractorStyle
    
    InteractorStyleTrackballCamera allows the user to interactively
    manipulate (rotate, pan, etc.) the camera, the viewpoint of the
    scene.  In trackball interaction, the magnitude of the mouse motion
    is proportional to the camera motion associated with a particular
    mouse binding. For example, small left-button motions cause small
    changes in the rotation of the camera around its focal point. For a
    3-button mouse, the left button is for rotation, the right button for
    zooming, the middle button for panning, and ctrl + left button for
    spinning.  (With fewer mouse buttons, ctrl + shift + left button is
    for zooming, and shift + left button is for panning.)
    
    See Also:
    
    InteractorStyleTrackballActor InteractorStyleJoystickCamera
    InteractorStyleJoystickActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleTrackballCamera, obj, update, **traits)
    
    motion_factor = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set the apparent sensitivity of the interactor style to mouse
        motion.
        """
    )
    def _motion_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMotionFactor,
                        self.motion_factor)

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('use_timers', 'GetUseTimers'),
    ('enabled', 'GetEnabled'), ('pick_color', 'GetPickColor'),
    ('key_press_activation', 'GetKeyPressActivation'),
    ('handle_observers', 'GetHandleObservers'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('motion_factor',
    'GetMotionFactor'), ('reference_count', 'GetReferenceCount'),
    ('timer_duration', 'GetTimerDuration'), ('mouse_wheel_motion_factor',
    'GetMouseWheelMotionFactor'))
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'use_timers', 'key_press_activation_value', 'motion_factor',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleTrackballCamera, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleTrackballCamera properties', scrollable=True, resizable=True,
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
            title='Edit InteractorStyleTrackballCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleTrackballCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

