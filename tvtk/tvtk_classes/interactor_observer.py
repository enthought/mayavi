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

from tvtk.tvtk_classes.object import Object


class InteractorObserver(Object):
    """
    InteractorObserver - an abstract superclass for classes observing
    events invoked by RenderWindowInteractor
    
    Superclass: Object
    
    InteractorObserver is an abstract superclass for subclasses that
    observe events invoked by RenderWindowInteractor. These subclasses
    are typically things like 3d widgets; objects that interact with
    actors in the scene, or interactively probe the scene for
    information.
    
    InteractorObserver defines the method set_interactor() and enables
    and disables the processing of events by the InteractorObserver.
    Use the methods enabled_on() or set_enabled(_1) to turn on the
    interactor observer, and the methods enabled_off() or set_enabled(_0) to
    turn off the interactor. Initial value is 0.
    
    To support interactive manipulation of objects, this class (and
    subclasses) invoke the events start_interaction_event,
    interaction_event, and end_interaction_event.  These events are invoked
    when the InteractorObserver enters a state where rapid response is
    desired: mouse motion, etc. The events can be used, for example, to
    set the desired update frame rate (_start_interaction_event), operate on
    data or update a pipeline (_interaction_event), and set the desired
    frame rate back to normal values (_end_interaction_event). Two other
    events, enable_event and disable_event, are invoked when the interactor
    observer is enabled or disabled.
    
    See Also:
    
    ThreeDWidget BoxWidget LineWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorObserver, obj, update, **traits)
    
    key_press_activation = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable of the use of a keypress to turn on and off the
        interactor observer. (By default, the keypress is 'i' for
        "interactor observer".)  Set the key_press_activation_value to
        change which key activates the widget.)
        """
    )
    def _key_press_activation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyPressActivation,
                        self.key_press_activation_)

    enabled = tvtk_base.false_bool_trait(help=\
        """
        Methods for turning the interactor observer on and off, and
        determining its state. All subclasses must provide the
        set_enabled() method. Enabling a InteractorObserver has the
        side effect of adding observers; disabling it removes the
        observers. Prior to enabling the InteractorObserver you must
        set the render window interactor (via set_interactor()). Initial
        value is 0.
        """
    )
    def _enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnabled,
                        self.enabled_)

    priority = traits.Trait(0.5, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the priority at which events are processed. This is used
        when multiple interactor observers are used simultaneously. The
        default value is 0.0 (lowest priority.) Note that when multiple
        interactor observer have the same priority, then the last
        observer added will process the event first. (Note: once the
        set_interactor() method has been called, changing the priority
        does not effect event processing. You will have to
        set_interactor(_null), change priority, and then
        set_interactor(iren) to have the priority take effect.)
        """
    )
    def _priority_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPriority,
                        self.priority)

    key_press_activation_value = traits.String(r"i", enter_set=True, auto_set=False, help=\
        """
        Specify which key press value to use to activate the interactor
        observer (if key press activation is enabled). By default, the
        key press activation value is 'i'. Note: once the set_interactor()
        method is invoked, changing the key press activation value will
        not affect the key press until
        set_interactor(_null)/_set_interactor(iren) is called.
        """
    )
    def _key_press_activation_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyPressActivationValue,
                        self.key_press_activation_value)

    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    def _set_interactor(self, arg):
        old_val = self._get_interactor()
        self._wrap_call(self._vtk_obj.SetInteractor,
                        deref_vtk(arg))
        self.trait_property_changed('interactor', old_val, arg)
    interactor = traits.Property(_get_interactor, _set_interactor, help=\
        """
        This method is used to associate the widget with the render
        window interactor.  Observers of the appropriate events invoked
        in the render window interactor are set up as a result of this
        method invocation. The set_interactor() method must be invoked
        prior to enabling the InteractorObserver.
        """
    )

    def _get_current_renderer(self):
        return wrap_vtk(self._vtk_obj.GetCurrentRenderer())
    def _set_current_renderer(self, arg):
        old_val = self._get_current_renderer()
        self._wrap_call(self._vtk_obj.SetCurrentRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('current_renderer', old_val, arg)
    current_renderer = traits.Property(_get_current_renderer, _set_current_renderer, help=\
        """
        Set/Get the current renderer. Normally when the widget is
        activated (_set_enabled(_1) or when keypress activation takes
        place), the renderer over which the mouse pointer is positioned
        is used and assigned to this Ivar. Alternatively, you might want
        to set the current_renderer explicitly. WARNING: note that if the
        default_renderer Ivar is set (see above), it will always override
        the parameter passed to set_current_renderer, unless it is NULL.
        (i.e., set_current_renderer(foo) =
        set_current_renderer(_default_renderer).
        """
    )

    def _get_default_renderer(self):
        return wrap_vtk(self._vtk_obj.GetDefaultRenderer())
    def _set_default_renderer(self, arg):
        old_val = self._get_default_renderer()
        self._wrap_call(self._vtk_obj.SetDefaultRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('default_renderer', old_val, arg)
    default_renderer = traits.Property(_get_default_renderer, _set_default_renderer, help=\
        """
        Set/Get the default renderer to use when activating the
        interactor observer. Normally when the widget is activated
        (_set_enabled(_1) or when keypress activation takes place), the
        renderer over which the mouse pointer is positioned is used.
        Alternatively, you can specify the renderer to bind the
        interactor to when the interactor observer is activated.
        """
    )

    def compute_display_to_world(self, *args):
        """
        V.compute_display_to_world(Renderer, float, float, float, [float,
            float, float, float])
        C++: static void ComputeDisplayToWorld(Renderer *ren, double x,
             double y, double z, double worldPt[4])
        Convenience methods for outside classes. Make sure that the
        parameter "ren" is not-null.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeDisplayToWorld, *my_args)
        return ret

    def compute_world_to_display(self, *args):
        """
        V.compute_world_to_display(Renderer, float, float, float, [float,
            float, float])
        C++: static void ComputeWorldToDisplay(Renderer *ren, double x,
             double y, double z, double displayPt[3])
        Convenience methods for outside classes. Make sure that the
        parameter "ren" is not-null.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeWorldToDisplay, *my_args)
        return ret

    def grab_focus(self, *args):
        """
        V.grab_focus(Command, Command)
        C++: void GrabFocus(Command *mouseEvents,
            Command *keypressEvents=NULL)
        These methods enable an interactor observer to exclusively grab
        all events invoked by its associated RenderWindowInteractor.
        (This method is typically used by widgets to grab events once an
        event sequence begins.) The grab_focus() signature takes up to two
        Commands corresponding to mouse events and keypress events.
        (These two commands are separated so that the widget can listen
        for its activation keypress, as well as listening for
        delete_events, without actually having to process mouse events.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GrabFocus, *my_args)
        return ret

    def off(self):
        """
        V.off()
        C++: void Off()
        Methods for turning the interactor observer on and off, and
        determining its state. All subclasses must provide the
        set_enabled() method. Enabling a InteractorObserver has the
        side effect of adding observers; disabling it removes the
        observers. Prior to enabling the InteractorObserver you must
        set the render window interactor (via set_interactor()). Initial
        value is 0.
        """
        ret = self._vtk_obj.Off()
        return ret
        

    def on(self):
        """
        V.on()
        C++: void On()
        Methods for turning the interactor observer on and off, and
        determining its state. All subclasses must provide the
        set_enabled() method. Enabling a InteractorObserver has the
        side effect of adding observers; disabling it removes the
        observers. Prior to enabling the InteractorObserver you must
        set the render window interactor (via set_interactor()). Initial
        value is 0.
        """
        ret = self._vtk_obj.On()
        return ret
        

    def on_char(self):
        """
        V.on_char()
        C++: virtual void OnChar()
        Sets up the keypress-i event.
        """
        ret = self._vtk_obj.OnChar()
        return ret
        

    def release_focus(self):
        """
        V.release_focus()
        C++: void ReleaseFocus()
        These methods enable an interactor observer to exclusively grab
        all events invoked by its associated RenderWindowInteractor.
        (This method is typically used by widgets to grab events once an
        event sequence begins.) The grab_focus() signature takes up to two
        Commands corresponding to mouse events and keypress events.
        (These two commands are separated so that the widget can listen
        for its activation keypress, as well as listening for
        delete_events, without actually having to process mouse events.)
        """
        ret = self._vtk_obj.ReleaseFocus()
        return ret
        

    _updateable_traits_ = \
    (('priority', 'GetPriority'), ('debug', 'GetDebug'),
    ('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'), ('key_press_activation',
    'GetKeyPressActivation'), ('enabled', 'GetEnabled'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorObserver, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorObserver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit InteractorObserver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorObserver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

