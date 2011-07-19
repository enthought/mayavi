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


class ConditionVariable(Object):
    """
    ConditionVariable - mutual exclusion locking class
    
    Superclass: Object
    
    ConditionVariable allows the locking of variables which are
    accessed through different threads.  This header file also defines
    SimpleConditionVariable which is not a subclass of Object.
    
    The win32 implementation is based on notes provided by Douglas C.
    Schmidt and Irfan Pyarali, Department of Computer Science, Washington
    University, St. Louis, Missouri.
    http://www.cs.wustl.edu/~schmidt/win32-cv-1.html
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkConditionVariable, obj, update, **traits)
    
    def broadcast(self):
        """
        V.broadcast()
        C++: void Broadcast()
        Wake all threads waiting for the condition to change.
        """
        ret = self._vtk_obj.Broadcast()
        return ret
        

    def signal(self):
        """
        V.signal()
        C++: void Signal()
        Wake one thread waiting for the condition to change.
        """
        ret = self._vtk_obj.Signal()
        return ret
        

    def wait(self, *args):
        """
        V.wait(MutexLock) -> int
        C++: int Wait(MutexLock *mutex)
        Wait for the condition to change. Upon entry, the mutex must be
        locked and the lock held by the calling thread. Upon exit, the
        mutex will be locked and held by the calling thread. Between
        entry and exit, the mutex will be unlocked and may be held by
        other threads.
        
        @param mutex The mutex that should be locked on entry and will be
        locked on exit (but not in between)@retval Normally, this
            function returns 0. Should a thread be interrupted by a
            signal, a non-zero value may be returned.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Wait, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ConditionVariable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ConditionVariable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ConditionVariable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ConditionVariable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

