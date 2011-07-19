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

from tvtk.tvtk_classes.render_window_interactor import RenderWindowInteractor


class XRenderWindowInteractor(RenderWindowInteractor):
    """
    XRenderWindowInteractor - an X event driven interface for a
    render_window
    
    Superclass: RenderWindowInteractor
    
    XRenderWindowInteractor is a convenience object that provides
    event bindings to common graphics functions. For example, camera and
    actor functions such as zoom-in/zoom-out, azimuth, roll, and pan. IT
    is one of the window system specific subclasses of
    RenderWindowInteractor. Please see RenderWindowInteractor
    documentation for event bindings.
    
    See Also:
    
    RenderWindowInteractor XRenderWindow
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXRenderWindowInteractor, obj, update, **traits)
    
    break_loop_flag = tvtk_base.true_bool_trait(help=\
        """
        The break_loop_flag is checked in the Start() method. Setting it to
        anything other than zero will cause the interactor loop to
        terminate and return to the calling function.
        """
    )
    def _break_loop_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBreakLoopFlag,
                        self.break_loop_flag_)

    _updateable_traits_ = \
    (('desired_update_rate', 'GetDesiredUpdateRate'),
    ('last_event_position', 'GetLastEventPosition'), ('shift_key',
    'GetShiftKey'), ('still_update_rate', 'GetStillUpdateRate'),
    ('repeat_count', 'GetRepeatCount'), ('use_t_dx', 'GetUseTDx'),
    ('control_key', 'GetControlKey'), ('enable_render',
    'GetEnableRender'), ('alt_key', 'GetAltKey'), ('size', 'GetSize'),
    ('break_loop_flag', 'GetBreakLoopFlag'), ('event_position',
    'GetEventPosition'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('timer_event_duration',
    'GetTimerEventDuration'), ('timer_duration', 'GetTimerDuration'),
    ('key_sym', 'GetKeySym'), ('timer_event_type', 'GetTimerEventType'),
    ('debug', 'GetDebug'), ('key_code', 'GetKeyCode'),
    ('number_of_fly_frames', 'GetNumberOfFlyFrames'), ('dolly',
    'GetDolly'), ('reference_count', 'GetReferenceCount'),
    ('timer_event_platform_id', 'GetTimerEventPlatformId'),
    ('timer_event_id', 'GetTimerEventId'), ('event_size', 'GetEventSize'),
    ('light_follow_camera', 'GetLightFollowCamera'))
    
    _full_traitnames_list_ = \
    (['break_loop_flag', 'debug', 'enable_render',
    'global_warning_display', 'light_follow_camera', 'alt_key',
    'control_key', 'desired_update_rate', 'dolly', 'event_position',
    'event_size', 'key_code', 'key_sym', 'last_event_position',
    'number_of_fly_frames', 'repeat_count', 'shift_key', 'size',
    'still_update_rate', 'timer_duration', 'timer_event_duration',
    'timer_event_id', 'timer_event_platform_id', 'timer_event_type',
    'use_t_dx'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XRenderWindowInteractor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XRenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['break_loop_flag', 'enable_render',
            'light_follow_camera'], [], ['alt_key', 'control_key',
            'desired_update_rate', 'dolly', 'event_position', 'event_size',
            'key_code', 'key_sym', 'last_event_position', 'number_of_fly_frames',
            'repeat_count', 'shift_key', 'size', 'still_update_rate',
            'timer_duration', 'timer_event_duration', 'timer_event_id',
            'timer_event_platform_id', 'timer_event_type', 'use_t_dx']),
            title='Edit XRenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XRenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

