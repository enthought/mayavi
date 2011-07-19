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


class InteractorStyleRubberBandPick(InteractorStyleTrackballCamera):
    """
    InteractorStyleRubberBandPick - Like track_ball_camera, but this can
    pick props underneath a rubber band selection rectangle.
    
    Superclass: InteractorStyleTrackballCamera
    
    This interactor style allows the user to draw a rectangle in the
    render window by hitting 'r' and then using the left mouse button.
    When the mouse button is released, the attached picker operates on
    the pixel in the center of the selection rectangle. If the picker
    happens to be a AreaPicker it will operate on the entire selection
    rectangle. When the 'p' key is hit the above pick operation occurs on
    a 1x1 rectangle. In other respects it behaves the same as its parent
    class.
    
    See Also:
    
    AreaPicker
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleRubberBandPick, obj, update, **traits)
    
    def start_select(self):
        """
        V.start_select()
        C++: void StartSelect()"""
        ret = self._vtk_obj.StartSelect()
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
            return super(InteractorStyleRubberBandPick, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleRubberBandPick properties', scrollable=True, resizable=True,
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
            title='Edit InteractorStyleRubberBandPick properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleRubberBandPick properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

