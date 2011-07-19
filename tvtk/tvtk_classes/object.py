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


class Object(ObjectBase):
    """
    Object - abstract base class for most VTK objects
    
    Superclass: ObjectBase
    
    Object is the base class for most objects in the visualization
    toolkit. Object provides methods for tracking modification time,
    debugging, printing, and event callbacks. Most objects created within
    the VTK framework should be a subclass of Object or one of its
    children.  The few exceptions tend to be very small helper classes
    that usually never get instantiated or situations where multiple
    inheritance gets in the way.  Object also performs reference
    counting: objects that are reference counted exist as long as another
    object uses them. Once the last reference to a reference counted
    object is removed, the object will spontaneously destruct.
    
    Caveats:
    
    Note: in VTK objects should always be created with the New() method
    and deleted with the Delete() method. VTK objects cannot be allocated
    off the stack (i.e., automatic objects) because the constructor is a
    protected method.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkObject, obj, update, **traits)
    
    debug = tvtk_base.false_bool_trait(help=\
        """
        Set the value of the debug flag. A non-zero value turns debugging
        on.
        """
    )
    def _debug_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDebug,
                        self.debug_)

    global_warning_display = tvtk_base.true_bool_trait(help=\
        """
        This is a global flag that controls whether any debug, warning or
        error messages are displayed.
        """
    )
    def _global_warning_display_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalWarningDisplay,
                        self.global_warning_display_)

    def _get_m_time(self):
        return self._vtk_obj.GetMTime()
    m_time = traits.Property(_get_m_time, help=\
        """
        Return this object's modified time.
        """
    )

    def add_observer(self, *args):
        """
        V.add_observer(int, function) -> int
        C++: unsigned long AddObserver(const char *event,
            Command *command, float priority=0.0f)
        Add an event callback function(vtk_object, int) for an event type.
        Returns a handle that can be used with remove_event(int)."""
        ret = self._wrap_call(self._vtk_obj.AddObserver, *args)
        return ret

    def break_on_error(self):
        """
        V.break_on_error()
        C++: static void BreakOnError()
        This method is called when ErrorMacro executes. It allows the
        debugger to break on error.
        """
        ret = self._vtk_obj.BreakOnError()
        return ret
        

    def has_observer(self, *args):
        """
        V.has_observer(int) -> int
        C++: int HasObserver(unsigned long event)
        V.has_observer(string) -> int
        C++: int HasObserver(const char *event)
        Allow people to add/remove/invoke observers (callbacks) to any
        VTK object.  This is an implementation of the subject/observer
        design pattern. An observer is added by specifying an event to
        respond to and a Command to execute. It returns an unsigned
        long tag which can be used later to remove the event or retrieve
        the command. When events are invoked, the observers are called in
        the order they were added. If a priority value is specified, then
        the higher priority commands are called first. A command may set
        an abort flag to stop processing of the event. (See Command.h
        for more information.)
        """
        ret = self._wrap_call(self._vtk_obj.HasObserver, *args)
        return ret

    def invoke_event(self, *args):
        """
        V.invoke_event(int, ) -> int
        C++: int InvokeEvent(unsigned long event, void *callData)
        V.invoke_event(string, ) -> int
        C++: int InvokeEvent(const char *event, void *callData)
        V.invoke_event(int) -> int
        C++: int InvokeEvent(unsigned long event)
        V.invoke_event(string) -> int
        C++: int InvokeEvent(const char *event)
        This method invokes an event and return whether the event was
        aborted or not. If the event was aborted, the return value is 1,
        otherwise it is 0.
        """
        ret = self._wrap_call(self._vtk_obj.InvokeEvent, *args)
        return ret

    def modified(self):
        """
        V.modified()
        C++: virtual void Modified()
        Update the modification time for this object. Many filters rely
        on the modification time to determine if they need to recompute
        their data. The modification time is a unique monotonically
        increasing unsigned long integer.
        """
        ret = self._vtk_obj.Modified()
        return ret
        

    def new_instance(self):
        """
        V.new_instance() -> Object
        C++: Object *NewInstance()"""
        ret = wrap_vtk(self._vtk_obj.NewInstance())
        return ret
        

    def remove_all_observers(self):
        """
        V.remove_all_observers()
        C++: void RemoveAllObservers()
        Allow people to add/remove/invoke observers (callbacks) to any
        VTK object.  This is an implementation of the subject/observer
        design pattern. An observer is added by specifying an event to
        respond to and a Command to execute. It returns an unsigned
        long tag which can be used later to remove the event or retrieve
        the command. When events are invoked, the observers are called in
        the order they were added. If a priority value is specified, then
        the higher priority commands are called first. A command may set
        an abort flag to stop processing of the event. (See Command.h
        for more information.)
        """
        ret = self._vtk_obj.RemoveAllObservers()
        return ret
        

    def remove_observer(self, *args):
        """
        V.remove_observer(int)
        C++: void RemoveObserver(unsigned long tag)
        Allow people to add/remove/invoke observers (callbacks) to any
        VTK object.  This is an implementation of the subject/observer
        design pattern. An observer is added by specifying an event to
        respond to and a Command to execute. It returns an unsigned
        long tag which can be used later to remove the event or retrieve
        the command. When events are invoked, the observers are called in
        the order they were added. If a priority value is specified, then
        the higher priority commands are called first. A command may set
        an abort flag to stop processing of the event. (See Command.h
        for more information.)
        """
        ret = self._wrap_call(self._vtk_obj.RemoveObserver, *args)
        return ret

    def remove_observers(self, *args):
        """
        V.remove_observers(int)
        C++: void RemoveObservers(unsigned long event)
        V.remove_observers(string)
        C++: void RemoveObservers(const char *event)
        Allow people to add/remove/invoke observers (callbacks) to any
        VTK object.  This is an implementation of the subject/observer
        design pattern. An observer is added by specifying an event to
        respond to and a Command to execute. It returns an unsigned
        long tag which can be used later to remove the event or retrieve
        the command. When events are invoked, the observers are called in
        the order they were added. If a priority value is specified, then
        the higher priority commands are called first. A command may set
        an abort flag to stop processing of the event. (See Command.h
        for more information.)
        """
        ret = self._wrap_call(self._vtk_obj.RemoveObservers, *args)
        return ret

    def safe_down_cast(self, *args):
        """
        V.safe_down_cast(Object) -> Object
        C++: Object *SafeDownCast(Object* o)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SafeDownCast, *my_args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Object, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Object properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Object properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Object properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

