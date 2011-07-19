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


class GenericRenderWindowInteractor(RenderWindowInteractor):
    """
    GenericRenderWindowInteractor - platform-independent programmable
    render window interactor.
    
    Superclass: RenderWindowInteractor
    
    GenericRenderWindowInteractor provides a way to translate native
    mouse and keyboard events into vtk Events.   By calling the methods
    on this class, vtk events will be invoked.   This will allow
    scripting languages to use InteractorStyles and 3d widgets.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericRenderWindowInteractor, obj, update, **traits)
    
    timer_event_resets_timer = tvtk_base.true_bool_trait(help=\
        """
        Flag that indicates whether the timer_event method should call
        reset_timer to simulate repeating timers with an endless stream of
        one shot timers. By default this flag is on and all repeating
        timers are implemented as a stream of sequential one shot timers.
        If the observer of create_timer_event actually creates a "natively
        repeating" timer, setting this flag to off will prevent (perhaps
        many many) unnecessary calls to reset_timer. Having the flag on by
        default means that "natively one shot" timers can be either one
        shot or repeating timers with no additional work. Also, "natively
        repeating" timers still work with the default setting, but with
        potentially many create and destroy calls.
        """
    )
    def _timer_event_resets_timer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimerEventResetsTimer,
                        self.timer_event_resets_timer_)

    def timer_event(self):
        """
        V.timer_event()
        C++: virtual void TimerEvent()
        Fire timer_event. set_event_information should be called just prior
        to calling any of these methods. These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.TimerEvent()
        return ret
        

    _updateable_traits_ = \
    (('desired_update_rate', 'GetDesiredUpdateRate'),
    ('last_event_position', 'GetLastEventPosition'), ('shift_key',
    'GetShiftKey'), ('still_update_rate', 'GetStillUpdateRate'),
    ('repeat_count', 'GetRepeatCount'), ('use_t_dx', 'GetUseTDx'),
    ('control_key', 'GetControlKey'), ('enable_render',
    'GetEnableRender'), ('alt_key', 'GetAltKey'), ('size', 'GetSize'),
    ('event_position', 'GetEventPosition'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('timer_event_duration',
    'GetTimerEventDuration'), ('timer_duration', 'GetTimerDuration'),
    ('key_sym', 'GetKeySym'), ('timer_event_type', 'GetTimerEventType'),
    ('debug', 'GetDebug'), ('key_code', 'GetKeyCode'),
    ('number_of_fly_frames', 'GetNumberOfFlyFrames'), ('dolly',
    'GetDolly'), ('timer_event_resets_timer', 'GetTimerEventResetsTimer'),
    ('reference_count', 'GetReferenceCount'), ('timer_event_platform_id',
    'GetTimerEventPlatformId'), ('timer_event_id', 'GetTimerEventId'),
    ('event_size', 'GetEventSize'), ('light_follow_camera',
    'GetLightFollowCamera'))
    
    _full_traitnames_list_ = \
    (['debug', 'enable_render', 'global_warning_display',
    'light_follow_camera', 'timer_event_resets_timer', 'alt_key',
    'control_key', 'desired_update_rate', 'dolly', 'event_position',
    'event_size', 'key_code', 'key_sym', 'last_event_position',
    'number_of_fly_frames', 'repeat_count', 'shift_key', 'size',
    'still_update_rate', 'timer_duration', 'timer_event_duration',
    'timer_event_id', 'timer_event_platform_id', 'timer_event_type',
    'use_t_dx'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericRenderWindowInteractor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericRenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enable_render', 'light_follow_camera',
            'timer_event_resets_timer'], [], ['alt_key', 'control_key',
            'desired_update_rate', 'dolly', 'event_position', 'event_size',
            'key_code', 'key_sym', 'last_event_position', 'number_of_fly_frames',
            'repeat_count', 'shift_key', 'size', 'still_update_rate',
            'timer_duration', 'timer_event_duration', 'timer_event_id',
            'timer_event_platform_id', 'timer_event_type', 'use_t_dx']),
            title='Edit GenericRenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericRenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

