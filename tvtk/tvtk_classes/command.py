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

from tvtk.tvtk_classes.object_base import ObjectBase


class Command(ObjectBase):
    """
    Command - superclass for callback/observer methods
    
    Superclass: ObjectBase
    
    Command is an implementation of the observer/command design
    pattern.  In this design pattern, any instance of Object can be
    "observed" for any events it might invoke. For example, Renderer
    invokes a start_event as it begins to render and a end_event when it
    finishes rendering. Filters (subclasses of ProcessObject) invoke
    start_event, progress_event, and end_event as the filter processes data.
    Observers of events are added with the add_observer() method found in
    Object.  add_observer(), besides requiring an event id or name,
    also takes an instance of Command (or a subclasses). Note that
    Command is meant to be subclassed, so that you can package the
    information necessary to support your callback.
    
    Event processing can be organized in priority lists, so it is
    possible to truncate the processing of a particular event by setting
    the abort_flag variable. The priority is set using the add_observer()
    method.  By default the priority is 0, events of the same priority
    are processed in last-in-first-processed order. The ordering/aborting
    of events is important for things like 3d widgets, which handle an
    event if the widget is selected (and then aborting further processing
    of that event).  Otherwise. the event is passed along for further
    processing.
    
    When an instance of Object invokes an event, it also passes an
    optional void pointer to a call_data. This call_data is NULL most of
    the time. The call_data is not specific to a type of event but
    specific to a type of Object invoking a specific event. For
    instance, Command::PickEvent is invoked by Prop with a NULL
    call_data but is invoked by InteractorStyleImage with a pointer to
    the InteractorStyleImage object itself.
    
    Here is the list of events that may be invoked with a none NULL
    call_data.
    - Command::ProgressEvent
    - most of the objects return a pointer to a double value ranged
      between 0.0 and 1.0
    - infovis/vtk_fixed_width_text_reader returns a pointer to a float value
      equal to the number of lines read so far.
    - Command::ErrorEvent
    - an error message as a const char * string
    - Command::WarningEvent
    - a warning message as a const char * string
    - Command::StartAnimationCueEvent
    - a pointer to a AnimationCue::AnimationCueInfo object
    - Command::EndAnimationCueEvent
    - a pointer to a AnimationCue::AnimationCueInfo object
    - Command::AnimationCueTickEvent
    - a pointer to a AnimationCue::AnimationCueInfo object
    - Command::PickEvent
    - common/vtk_prop returns NULL
    - rendering/vtk_interactor_style_image returns a pointer to itself
    - Command::StartPickEvent
    - rendering/vtk_prop_picker returns NULL
    - rendering/vtk_interactor_style_image returns a pointer to itself
    - Command::EndPickEvent
    - rendering/vtk_prop_picker returns NULL
    - rendering/vtk_interactor_style_image returns a pointer to itself
    - Command::WrongTagEvent
    - parallel/vtk_socket_communicator returns a received tag as a char *
    - Command::SelectionChangedEvent
    - views/vtk_view returns NULL
    - views/vtk_data_representation returns a pointer to a Selection
    - rendering/vtk_interactor_style_rubber_band2d returns an array of 5
      unsigned integers (p1x, p1y, p2x, p2y, mode), where mode is
      InteractorStyleRubberBand2D::SELECT_UNION or
      InteractorStyleRubberBand2D::SELECT_NORMAL
    - Command::AnnotationChangedEvent
    - gui_support/_qt/vtk_qt_annotation_view returns a pointer to a
      AnnotationLayers
    - Command::PlacePointEvent
    - widgets/vtk_seed_widget returns a pointer to an int, being the
      current handle number
    - Command::ResetWindowLevelEvent
    - widgets/vtk_image_plane_widget returns an array of 2 double values
      (window and level)
    - rendering/vtk_interactor_style_image returns a pointer to itself
    - Command::StartWindowLevelEvent
    - widgets/vtk_image_plane_widget returns an array of 2 double values
      (window and level)
    - rendering/vtk_interactor_style_image returns a pointer to itself
    - Command::EndWindowLevelEvent
    - widgets/vtk_image_plane_widget returns an array of 2 double values
      (window and level)
    - rendering/vtk_interactor_style_image returns a pointer to itself
    - Command::WindowLevelEvent
    - widgets/vtk_image_plane_widget returns an array of 2 double values
      (window and level)
    - rendering/vtk_interactor_style_image returns a pointer to itself
    - Command::CharEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_key_event *
    - Command::TimerEvent
    - most of the objects return a to an int representing a timer id
    - rendering/vtk_x_render_window_tcl_interactor returns NULL
    - widgets/vtk_hover_widget returns NULL
    - Command::CreateTimerEvent
    - rendering/vtk_generic_render_window_interactor returns a to an int
      representing a timer id
    - Command::DestroyTimerEvent
    - rendering/vtk_generic_render_window_interactor returns a to an int
      representing a timer id
    - Command::UserEvent
    - most of the objects return NULL
    - infovis/vtk_interactor_style_tree_map_hover returns a pointer to a
      IdType representing a pedigree id
    - Command::KeyPressEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_key_event*
    - Command::KeyReleaseEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_key_event*
    - Command::LeftButtonPressEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_mouse_event*
    - Command::LeftButtonReleaseEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_mouse_event*
    - Command::MouseMoveEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_mouse_event*
    - Command::MouseWheelForwardEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_wheel_event*
    - Command::MouseWheelBackwardEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_wheel_event*
    - Command::RightButtonPressEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_mouse_event*
    - Command::RightButtonReleaseEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_mouse_event*
    - Command::MiddleButtonPressEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_mouse_event*
    - Command::MiddleButtonReleaseEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a q_mouse_event*
    - Command::CursorChangedEvent
    - most of the objects return a pointer to an int representing a shape
    - rendering/vtk_interactor_observer returns NULL
    - Command::ResetCameraEvent
    - rendering/vtk_renderer returns a pointer to itself
    - Command::ResetCameraClippingRangeEvent
    - rendering/vtk_renderer returns a pointer to itself
    - Command::ActiveCameraEvent
    - rendering/vtk_renderer returns a pointer to the active camera
    - Command::CreateCameraEvent
    - rendering/vtk_renderer returns a pointer to the created camera
    - Command::EnterEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a QEvent*
    - Command::LeaveEvent
    - most of the objects return NULL
    - GUISupport/Qt/QVTKWidget returns a QEvent*
    - Command::RenderWindowMessageEvent
    - rendering/vtk_win32_open_gl_render_window return a pointer to a UINT
      message
    - Command::ComputeVisiblePropBoundsEvent
    - rendering/vtk_renderer returns a pointer to itself
    - qvtk_widget::_context_menu_event
    - GUISupport/Qt/QVTKWidget returns a q_context_menu_event*
    - qvtk_widget::_drag_enter_event
    - GUISupport/Qt/QVTKWidget returns a q_drag_enter_event*
    - qvtk_widget::_drag_move_event
    - GUISupport/Qt/QVTKWidget returns a q_drag_move_event*
    - qvtk_widget::_drag_leave_event
    - GUISupport/Qt/QVTKWidget returns a q_drag_leave_event*
    - qvtk_widget::_drop_event
    - GUISupport/Qt/QVTKWidget returns a q_drop_event*
    - Command::ViewProgressEvent
    - view/vtk_view returns a view_progress_event_call_data*
    - Command::VolumeMapperRenderProgressEvent
    - A pointer to a double value between 0.0 and 1.0
    - Command::VolumeMapperComputeGradientsProgressEvent
    - A pointer to a double value between 0.0 and 1.0
    - Command::TDxMotionEvent (_t_dx=_3d_connexion)
    - A TDxMotionEventInfo*
    - Command::TDxButtonPressEvent
    - A int* being the number of the button
    - Command::TDxButtonReleaseEvent
    - A int* being the number of the button
    
    See Also:
    
    Object CallbackCommand OldStyleCallbackCommand
    InteractorObserver ThreeDWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCommand, obj, update, **traits)
    
    passive_observer = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the passive observer flag. If this is set to true, this
        indicates that this command does not change the state of the
        system in any way. Passive observers are processed first, and are
        not called even when another command has focus.
        """
    )
    def _passive_observer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassiveObserver,
                        self.passive_observer_)

    abort_flag = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the abort flag. If this is set to true no further
        commands are executed.
        """
    )
    def _abort_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbortFlag,
                        self.abort_flag_)

    def get_event_id_from_string(self, *args):
        """
        V.get_event_id_from_string(string) -> int
        C++: static unsigned long GetEventIdFromString(const char *event)
        Convenience methods for translating between event names and event
        ids.
        """
        ret = self._wrap_call(self._vtk_obj.GetEventIdFromString, *args)
        return ret

    def get_string_from_event_id(self, *args):
        """
        V.get_string_from_event_id(int) -> string
        C++: static const char *GetStringFromEventId(unsigned long event)
        Convenience methods for translating between event names and event
        ids.
        """
        ret = self._wrap_call(self._vtk_obj.GetStringFromEventId, *args)
        return ret

    def execute(self, *args):
        """
        V.execute(Object, int, )
        C++: virtual void Execute(Object *caller,
            unsigned long eventId, void *callData)
        All derived classes of Command must implement this method.
        This is the method that actually does the work of the callback.
        The caller argument is the object invoking the event, the event_id
        parameter is the id of the event, and call_data parameter is data
        that can be passed into the execute method. (Note:
        Object::InvokeEvent() takes two parameters: the event id (or
        name) and call data. Typically call data is NULL, but the user
        can package data and pass it this way. Alternatively, a derived
        class of Command can be used to pass data.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Execute, *my_args)
        return ret

    def new_instance(self):
        """
        V.new_instance() -> Command
        C++: Command *NewInstance()"""
        ret = wrap_vtk(self._vtk_obj.NewInstance())
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('passive_observer',
    'GetPassiveObserver'), ('abort_flag', 'GetAbortFlag'))
    
    _full_traitnames_list_ = \
    (['abort_flag', 'passive_observer'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Command, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Command properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['abort_flag', 'passive_observer'], [], []),
            title='Edit Command properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Command properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

