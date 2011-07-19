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

from tvtk.tvtk_classes.interactor_observer import InteractorObserver


class InteractorStyle(InteractorObserver):
    """
    InteractorStyle - provide event-driven interface to the rendering
    window (defines trackball mode)
    
    Superclass: InteractorObserver
    
    InteractorStyle is a base class implementing the majority of
    motion control routines and defines an event driven interface to
    support RenderWindowInteractor. RenderWindowInteractor
    implements platform dependent key/mouse routing and timer control,
    which forwards events in a neutral form to InteractorStyle.
    
    InteractorStyle implements the "joystick" style of interaction.
    That is, holding down the mouse keys generates a stream of events
    that cause continuous actions (e.g., rotate, translate, pan, zoom).
    (The class InteractorStyleTrackball implements a grab and move
    style.) The event bindings for this class include the following:
    - Keypress j / Keypress t: toggle between joystick (position
      sensitive) and trackball (motion sensitive) styles. In joystick
      style, motion occurs continuously as long as a mouse button is
      pressed. In trackball style, motion occurs when the mouse button is
    pressed and the mouse pointer moves.
    - Keypress c / Keypress a: toggle between camera and actor modes. In
      camera mode, mouse events affect the camera position and focal
      point. In actor mode, mouse events affect the actor that is under
      the mouse pointer.
    - Button 1: rotate the camera around its focal point (if camera mode)
    or rotate the actor around its origin (if actor mode). The rotation
      is in the direction defined from the center of the renderer's
      viewport towards the mouse position. In joystick mode, the
      magnitude of the rotation is determined by the distance the mouse
      is from the center of the render window.
    - Button 2: pan the camera (if camera mode) or translate the actor
      (if actor mode). In joystick mode, the direction of pan or
      translation is from the center of the viewport towards the mouse
      position. In trackball mode, the direction of motion is the
      direction the mouse moves. (Note: with 2-button mice, pan is
      defined as <Shift>-Button 1.)
    - Button 3: zoom the camera (if camera mode) or scale the actor (if
      actor mode). Zoom in/increase scale if the mouse position is in the
    top half of the viewport; zoom out/decrease scale if the mouse
      position is in the bottom half. In joystick mode, the amount of
      zoom is controlled by the distance of the mouse pointer from the
      horizontal centerline of the window.
    - Keypress 3: toggle the render window into and out of stereo mode.
      By default, red-blue stereo pairs are created. Some systems support
    Crystal Eyes LCD stereo glasses; you have to invoke
      set_stereo_type_to_crystal_eyes() on the rendering window.
    - Keypress e: exit the application.
    - Keypress f: fly to the picked point
    - Keypress p: perform a pick operation. The render window interactor
      has an internal instance of CellPicker that it uses to pick.
    - Keypress r: reset the camera view along the current view direction.
    Centers the actors and moves the camera so that all actors are
      visible.
    - Keypress s: modify the representation of all actors so that they
      are surfaces.
    - Keypress u: invoke the user-defined function. Typically, this
      keypress will bring up an interactor that you can type commands in.
      Typing u calls user_call_back() on the RenderWindowInteractor,
      which invokes a Command::UserEvent. In other words, to define a
      user-defined callback, just add an observer to the
      Command::UserEvent on the RenderWindowInteractor object.
    - Keypress w: modify the representation of all actors so that they
      are wireframe.
    
    InteractorStyle can be subclassed to provide new interaction
    styles and a facility to override any of the default mouse/key
    operations which currently handle trackball or joystick styles is
    provided. Note that this class will fire a variety of events that can
    be watched using an observer, such as left_button_press_event,
    left_button_release_event, middle_button_press_event,
    middle_button_release_event, right_button_press_event,
    right_button_release_event, enter_event, leave_event, key_press_event,
    key_release_event, char_event, expose_event, configure_event, timer_event,
    mouse_move_event,
    
    See Also:
    
    InteractorStyleTrackball
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyle, obj, update, **traits)
    
    use_timers = tvtk_base.false_bool_trait(help=\
        """
        Set/Get timer hint
        """
    )
    def _use_timers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseTimers,
                        self.use_timers_)

    auto_adjust_camera_clipping_range = tvtk_base.true_bool_trait(help=\
        """
        If auto_adjust_camera_clipping_range is on, then before each render
        the camera clipping range will be adjusted to "fit" the whole
        scene. Clipping will still occur if objects in the scene are
        behind the camera or come very close. If
        auto_adjust_camera_clipping_range is off, no adjustment will be made
        per render, but the camera clipping range will still be reset
        when the camera is reset.
        """
    )
    def _auto_adjust_camera_clipping_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdjustCameraClippingRange,
                        self.auto_adjust_camera_clipping_range_)

    handle_observers = tvtk_base.true_bool_trait(help=\
        """
        Does process_events handle observers on this class or not
        """
    )
    def _handle_observers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleObservers,
                        self.handle_observers_)

    def _get_t_dx_style(self):
        return wrap_vtk(self._vtk_obj.GetTDxStyle())
    def _set_t_dx_style(self, arg):
        old_val = self._get_t_dx_style()
        self._wrap_call(self._vtk_obj.SetTDxStyle,
                        deref_vtk(arg))
        self.trait_property_changed('t_dx_style', old_val, arg)
    t_dx_style = traits.Property(_get_t_dx_style, _set_t_dx_style, help=\
        """
        3dconnexion device interactor style. Initial value is a pointer
        to an object of class TdxInteractorStyleCamera.
        """
    )

    pick_color = tvtk_base.vtk_color_trait((1.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _pick_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPickColor,
                        self.pick_color, False)

    timer_duration = traits.Trait(10, traits.Range(1, 100000, enter_set=True, auto_set=False), help=\
        """
        If using timers, specify the default timer interval (in
        milliseconds). Care must be taken when adjusting the timer
        interval from the default value of 10 milliseconds--it may
        adversely affect the interactors.
        """
    )
    def _timer_duration_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimerDuration,
                        self.timer_duration)

    mouse_wheel_motion_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the mouse wheel motion factor. Default to 1.0. Set it to
        a different value to emphasize or de-emphasize the action
        triggered by mouse wheel motion.
        """
    )
    def _mouse_wheel_motion_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMouseWheelMotionFactor,
                        self.mouse_wheel_motion_factor)

    def _get_auto_adjust_camera_clipping_range_max_value(self):
        return self._vtk_obj.GetAutoAdjustCameraClippingRangeMaxValue()
    auto_adjust_camera_clipping_range_max_value = traits.Property(_get_auto_adjust_camera_clipping_range_max_value, help=\
        """
        If auto_adjust_camera_clipping_range is on, then before each render
        the camera clipping range will be adjusted to "fit" the whole
        scene. Clipping will still occur if objects in the scene are
        behind the camera or come very close. If
        auto_adjust_camera_clipping_range is off, no adjustment will be made
        per render, but the camera clipping range will still be reset
        when the camera is reset.
        """
    )

    def _get_auto_adjust_camera_clipping_range_min_value(self):
        return self._vtk_obj.GetAutoAdjustCameraClippingRangeMinValue()
    auto_adjust_camera_clipping_range_min_value = traits.Property(_get_auto_adjust_camera_clipping_range_min_value, help=\
        """
        If auto_adjust_camera_clipping_range is on, then before each render
        the camera clipping range will be adjusted to "fit" the whole
        scene. Clipping will still occur if objects in the scene are
        behind the camera or come very close. If
        auto_adjust_camera_clipping_range is off, no adjustment will be made
        per render, but the camera clipping range will still be reset
        when the camera is reset.
        """
    )

    def _get_state(self):
        return self._vtk_obj.GetState()
    state = traits.Property(_get_state, help=\
        """
        Some useful information for interaction
        """
    )

    def delegate_t_dx_event(self, *args):
        """
        V.delegate_t_dx_event(int, )
        C++: void DelegateTDxEvent(unsigned long event, void *calldata)
        Called by the callback to process 3d_connexion device events.
        """
        ret = self._wrap_call(self._vtk_obj.DelegateTDxEvent, *args)
        return ret

    def dolly(self):
        """
        V.dolly()
        C++: virtual void Dolly()
        These methods for the different interactions in different modes
        are overridden in subclasses to perform the correct motion. Since
        they might be called from on_timer, they do not have mouse coord
        parameters (use interactor's get_event_position and
        get_last_event_position)
        """
        ret = self._vtk_obj.Dolly()
        return ret
        

    def end_dolly(self):
        """
        V.end_dolly()
        C++: virtual void EndDolly()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.EndDolly()
        return ret
        

    def end_pan(self):
        """
        V.end_pan()
        C++: virtual void EndPan()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.EndPan()
        return ret
        

    def end_rotate(self):
        """
        V.end_rotate()
        C++: virtual void EndRotate()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.EndRotate()
        return ret
        

    def end_spin(self):
        """
        V.end_spin()
        C++: virtual void EndSpin()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.EndSpin()
        return ret
        

    def end_timer(self):
        """
        V.end_timer()
        C++: virtual void EndTimer()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.EndTimer()
        return ret
        

    def end_uniform_scale(self):
        """
        V.end_uniform_scale()
        C++: virtual void EndUniformScale()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.EndUniformScale()
        return ret
        

    def end_zoom(self):
        """
        V.end_zoom()
        C++: virtual void EndZoom()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.EndZoom()
        return ret
        

    def find_poked_renderer(self, *args):
        """
        V.find_poked_renderer(int, int)
        C++: void FindPokedRenderer(int, int)
        When an event occurs, we must determine which Renderer the event
        occurred within, since one render_window may contain multiple
        renderers.
        """
        ret = self._wrap_call(self._vtk_obj.FindPokedRenderer, *args)
        return ret

    def highlight_actor2d(self, *args):
        """
        V.highlight_actor2d(Actor2D)
        C++: virtual void HighlightActor2D(Actor2D *actor2D)
        When picking successfully selects an actor, this method
        highlights the picked prop appropriately. Currently this is done
        by placing a bounding box around a picked Prop3D, and using
        the pick_color to highlight a Prop2D.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HighlightActor2D, *my_args)
        return ret

    def highlight_prop(self, *args):
        """
        V.highlight_prop(Prop)
        C++: virtual void HighlightProp(Prop *prop)
        When picking successfully selects an actor, this method
        highlights the picked prop appropriately. Currently this is done
        by placing a bounding box around a picked Prop3D, and using
        the pick_color to highlight a Prop2D.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HighlightProp, *my_args)
        return ret

    def highlight_prop3d(self, *args):
        """
        V.highlight_prop3d(Prop3D)
        C++: virtual void HighlightProp3D(Prop3D *prop3D)
        When picking successfully selects an actor, this method
        highlights the picked prop appropriately. Currently this is done
        by placing a bounding box around a picked Prop3D, and using
        the pick_color to highlight a Prop2D.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HighlightProp3D, *my_args)
        return ret

    def on_configure(self):
        """
        V.on_configure()
        C++: virtual void OnConfigure()
        These are more esoteric events, but are useful in some cases.
        """
        ret = self._vtk_obj.OnConfigure()
        return ret
        

    def on_enter(self):
        """
        V.on_enter()
        C++: virtual void OnEnter()
        These are more esoteric events, but are useful in some cases.
        """
        ret = self._vtk_obj.OnEnter()
        return ret
        

    def on_expose(self):
        """
        V.on_expose()
        C++: virtual void OnExpose()
        These are more esoteric events, but are useful in some cases.
        """
        ret = self._vtk_obj.OnExpose()
        return ret
        

    def on_key_down(self):
        """
        V.on_key_down()
        C++: virtual void OnKeyDown()"""
        ret = self._vtk_obj.OnKeyDown()
        return ret
        

    def on_key_press(self):
        """
        V.on_key_press()
        C++: virtual void OnKeyPress()"""
        ret = self._vtk_obj.OnKeyPress()
        return ret
        

    def on_key_release(self):
        """
        V.on_key_release()
        C++: virtual void OnKeyRelease()"""
        ret = self._vtk_obj.OnKeyRelease()
        return ret
        

    def on_key_up(self):
        """
        V.on_key_up()
        C++: virtual void OnKeyUp()"""
        ret = self._vtk_obj.OnKeyUp()
        return ret
        

    def on_leave(self):
        """
        V.on_leave()
        C++: virtual void OnLeave()
        These are more esoteric events, but are useful in some cases.
        """
        ret = self._vtk_obj.OnLeave()
        return ret
        

    def on_left_button_down(self):
        """
        V.on_left_button_down()
        C++: virtual void OnLeftButtonDown()
        Generic event bindings can be overridden in subclasses
        """
        ret = self._vtk_obj.OnLeftButtonDown()
        return ret
        

    def on_left_button_up(self):
        """
        V.on_left_button_up()
        C++: virtual void OnLeftButtonUp()
        Generic event bindings can be overridden in subclasses
        """
        ret = self._vtk_obj.OnLeftButtonUp()
        return ret
        

    def on_middle_button_down(self):
        """
        V.on_middle_button_down()
        C++: virtual void OnMiddleButtonDown()
        Generic event bindings can be overridden in subclasses
        """
        ret = self._vtk_obj.OnMiddleButtonDown()
        return ret
        

    def on_middle_button_up(self):
        """
        V.on_middle_button_up()
        C++: virtual void OnMiddleButtonUp()
        Generic event bindings can be overridden in subclasses
        """
        ret = self._vtk_obj.OnMiddleButtonUp()
        return ret
        

    def on_mouse_move(self):
        """
        V.on_mouse_move()
        C++: virtual void OnMouseMove()
        Generic event bindings can be overridden in subclasses
        """
        ret = self._vtk_obj.OnMouseMove()
        return ret
        

    def on_mouse_wheel_backward(self):
        """
        V.on_mouse_wheel_backward()
        C++: virtual void OnMouseWheelBackward()
        Generic event bindings can be overridden in subclasses
        """
        ret = self._vtk_obj.OnMouseWheelBackward()
        return ret
        

    def on_mouse_wheel_forward(self):
        """
        V.on_mouse_wheel_forward()
        C++: virtual void OnMouseWheelForward()
        Generic event bindings can be overridden in subclasses
        """
        ret = self._vtk_obj.OnMouseWheelForward()
        return ret
        

    def on_right_button_down(self):
        """
        V.on_right_button_down()
        C++: virtual void OnRightButtonDown()
        Generic event bindings can be overridden in subclasses
        """
        ret = self._vtk_obj.OnRightButtonDown()
        return ret
        

    def on_right_button_up(self):
        """
        V.on_right_button_up()
        C++: virtual void OnRightButtonUp()
        Generic event bindings can be overridden in subclasses
        """
        ret = self._vtk_obj.OnRightButtonUp()
        return ret
        

    def on_timer(self):
        """
        V.on_timer()
        C++: virtual void OnTimer()
        on_timer calls Rotate, Rotate etc which should be overridden by
        style subclasses.
        """
        ret = self._vtk_obj.OnTimer()
        return ret
        

    def pan(self):
        """
        V.pan()
        C++: virtual void Pan()
        These methods for the different interactions in different modes
        are overridden in subclasses to perform the correct motion. Since
        they might be called from on_timer, they do not have mouse coord
        parameters (use interactor's get_event_position and
        get_last_event_position)
        """
        ret = self._vtk_obj.Pan()
        return ret
        

    def rotate(self):
        """
        V.rotate()
        C++: virtual void Rotate()
        These methods for the different interactions in different modes
        are overridden in subclasses to perform the correct motion. Since
        they might be called from on_timer, they do not have mouse coord
        parameters (use interactor's get_event_position and
        get_last_event_position)
        """
        ret = self._vtk_obj.Rotate()
        return ret
        

    def spin(self):
        """
        V.spin()
        C++: virtual void Spin()
        These methods for the different interactions in different modes
        are overridden in subclasses to perform the correct motion. Since
        they might be called from on_timer, they do not have mouse coord
        parameters (use interactor's get_event_position and
        get_last_event_position)
        """
        ret = self._vtk_obj.Spin()
        return ret
        

    def start_animate(self):
        """
        V.start_animate()
        C++: virtual void StartAnimate()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.StartAnimate()
        return ret
        

    def start_dolly(self):
        """
        V.start_dolly()
        C++: virtual void StartDolly()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.StartDolly()
        return ret
        

    def start_pan(self):
        """
        V.start_pan()
        C++: virtual void StartPan()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.StartPan()
        return ret
        

    def start_rotate(self):
        """
        V.start_rotate()
        C++: virtual void StartRotate()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.StartRotate()
        return ret
        

    def start_spin(self):
        """
        V.start_spin()
        C++: virtual void StartSpin()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.StartSpin()
        return ret
        

    def start_state(self, *args):
        """
        V.start_state(int)
        C++: virtual void StartState(int newstate)
        utility routines used by state changes
        """
        ret = self._wrap_call(self._vtk_obj.StartState, *args)
        return ret

    def start_timer(self):
        """
        V.start_timer()
        C++: virtual void StartTimer()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.StartTimer()
        return ret
        

    def start_uniform_scale(self):
        """
        V.start_uniform_scale()
        C++: virtual void StartUniformScale()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.StartUniformScale()
        return ret
        

    def start_zoom(self):
        """
        V.start_zoom()
        C++: virtual void StartZoom()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.StartZoom()
        return ret
        

    def stop_animate(self):
        """
        V.stop_animate()
        C++: virtual void StopAnimate()
        Interaction mode entry points used internally.
        """
        ret = self._vtk_obj.StopAnimate()
        return ret
        

    def stop_state(self):
        """
        V.stop_state()
        C++: virtual void StopState()
        utility routines used by state changes
        """
        ret = self._vtk_obj.StopState()
        return ret
        

    def uniform_scale(self):
        """
        V.uniform_scale()
        C++: virtual void UniformScale()
        These methods for the different interactions in different modes
        are overridden in subclasses to perform the correct motion. Since
        they might be called from on_timer, they do not have mouse coord
        parameters (use interactor's get_event_position and
        get_last_event_position)
        """
        ret = self._vtk_obj.UniformScale()
        return ret
        

    def zoom(self):
        """
        V.zoom()
        C++: virtual void Zoom()
        These methods for the different interactions in different modes
        are overridden in subclasses to perform the correct motion. Since
        they might be called from on_timer, they do not have mouse coord
        parameters (use interactor's get_event_position and
        get_last_event_position)
        """
        ret = self._vtk_obj.Zoom()
        return ret
        

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('key_press_activation',
    'GetKeyPressActivation'), ('enabled', 'GetEnabled'), ('pick_color',
    'GetPickColor'), ('handle_observers', 'GetHandleObservers'),
    ('priority', 'GetPriority'), ('debug', 'GetDebug'),
    ('reference_count', 'GetReferenceCount'), ('use_timers',
    'GetUseTimers'), ('timer_duration', 'GetTimerDuration'),
    ('mouse_wheel_motion_factor', 'GetMouseWheelMotionFactor'))
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'use_timers', 'key_press_activation_value',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyle, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'use_timers'], [],
            ['key_press_activation_value', 'mouse_wheel_motion_factor',
            'pick_color', 'priority', 'timer_duration']),
            title='Edit InteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

