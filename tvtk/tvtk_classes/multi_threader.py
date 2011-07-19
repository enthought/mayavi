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


class MultiThreader(Object):
    """
    MultiThreader - A class for performing multithreaded execution
    
    Superclass: Object
    
    Multithreader is a class that provides support for multithreaded
    execution using sproc() on an SGI, or pthread_create on any platform
    supporting POSIX threads.  This class can be used to execute a single
    method on multiple threads, or to specify a method per thread.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMultiThreader, obj, update, **traits)
    
    global_maximum_number_of_threads = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum number of threads to use when multithreading.
        This limits and overrides any other settings for multithreading.
        A value of zero indicates no limit.
        """
    )
    def _global_maximum_number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalMaximumNumberOfThreads,
                        self.global_maximum_number_of_threads)

    number_of_threads = traits.Trait(2, traits.Range(1, 32, enter_set=True, auto_set=False), help=\
        """
        Get/Set the number of threads to create. It will be clamped to
        the range 1 - VTK_MAX_THREADS, so the caller of this method
        should check that the requested number of threads was accepted.
        """
    )
    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

    global_default_number_of_threads = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/Get the value which is used to initialize the number_of_threads
        in the constructor.  Initially this default is set to the number
        of processors or VTK_MAX_THREADS (which ever is less).
        """
    )
    def _global_default_number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalDefaultNumberOfThreads,
                        self.global_default_number_of_threads)

    def is_thread_active(self, *args):
        """
        V.is_thread_active(int) -> int
        C++: int IsThreadActive(int threadID)
        Determine if a thread is still active
        """
        ret = self._wrap_call(self._vtk_obj.IsThreadActive, *args)
        return ret

    def multiple_method_execute(self):
        """
        V.multiple_method_execute()
        C++: void MultipleMethodExecute()
        Execute the multiple_methods (as define by calling
        set_multiple_method for each of the required this->_number_of_threads
        methods) using this->_number_of_threads threads.
        """
        ret = self._vtk_obj.MultipleMethodExecute()
        return ret
        

    def single_method_execute(self):
        """
        V.single_method_execute()
        C++: void SingleMethodExecute()
        Execute the single_method (as define by set_single_method) using
        this->_number_of_threads threads.
        """
        ret = self._vtk_obj.SingleMethodExecute()
        return ret
        

    def terminate_thread(self, *args):
        """
        V.terminate_thread(int)
        C++: void TerminateThread(int thread_id)
        Terminate the thread that was created with a spawn_thread_execute()
        """
        ret = self._wrap_call(self._vtk_obj.TerminateThread, *args)
        return ret

    _updateable_traits_ = \
    (('global_default_number_of_threads',
    'GetGlobalDefaultNumberOfThreads'),
    ('global_maximum_number_of_threads',
    'GetGlobalMaximumNumberOfThreads'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_threads',
    'GetNumberOfThreads'), ('reference_count', 'GetReferenceCount'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display',
    'global_default_number_of_threads',
    'global_maximum_number_of_threads', 'number_of_threads'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MultiThreader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MultiThreader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['global_default_number_of_threads',
            'global_maximum_number_of_threads', 'number_of_threads']),
            title='Edit MultiThreader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MultiThreader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

