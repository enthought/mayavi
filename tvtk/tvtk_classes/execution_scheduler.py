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


class ExecutionScheduler(Object):
    """
    ExecutionScheduler - Scheduling execution with
    
    Superclass: Object
    
    This is a class for balancing the computing resources throughout the
    network
    
    See Also:
    
    ComputingResources ThreadedStreamingPipeline
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExecutionScheduler, obj, update, **traits)
    
    def _get_global_scheduler(self):
        return wrap_vtk(self._vtk_obj.GetGlobalScheduler())
    global_scheduler = traits.Property(_get_global_scheduler, help=\
        """
        Return the global instance of the scheduler
        """
    )

    def get_inputs_released_lock(self, *args):
        """
        V.get_inputs_released_lock(Executive) -> MutexLock
        C++: MutexLock *GetInputsReleasedLock(Executive *exec)
        Return the mutex lock reserved for the given exec to notify when
        it releases its inputs
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetInputsReleasedLock, *my_args)
        return wrap_vtk(ret)

    def get_inputs_released_messager(self, *args):
        """
        V.get_inputs_released_messager(Executive) -> ThreadMessager
        C++: ThreadMessager *GetInputsReleasedMessager(
            Executive *exec)
        Return the thread messager reserved for the given exec to notify
        when it releases its inputs
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetInputsReleasedMessager, *my_args)
        return wrap_vtk(ret)

    def get_task_done_messager(self, *args):
        """
        V.get_task_done_messager(Executive) -> ThreadMessager
        C++: ThreadMessager *GetTaskDoneMessager(Executive *exec)
        Return the thread messager reserved for the given exec to notify
        when it is done
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetTaskDoneMessager, *my_args)
        return wrap_vtk(ret)

    def reacquire_resources(self, *args):
        """
        V.reacquire_resources(Executive)
        C++: void ReacquireResources(Executive *exec)
        Re-acquire the resource released earlier by release_resource
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReacquireResources, *my_args)
        return ret

    def release_resources(self, *args):
        """
        V.release_resources(Executive)
        C++: void ReleaseResources(Executive *exec)
        Release the resources that are being used by the given exec
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseResources, *my_args)
        return ret

    def reschedule_from(self, *args):
        """
        V.reschedule_from(Executive, ComputingResources)
        C++: void RescheduleFrom(Executive *sink,
            ComputingResources *resources)
        Redistribute the thread resources from a sink given a certain
        amount of resource
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RescheduleFrom, *my_args)
        return ret

    def reschedule_network(self, *args):
        """
        V.reschedule_network(Executive)
        C++: void RescheduleNetwork(Executive *sink)
        Redistribute the thread resources over the network from a sink
        with a maximum resource
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RescheduleNetwork, *my_args)
        return ret

    def schedule(self, *args):
        """
        V.schedule(ExecutiveCollection, Information)
        C++: void Schedule(ExecutiveCollection *execs,
            Information *info)
        Put the current set of executives (modules) to the be scheduled
        given its dependency graph which will be used to compute the set
        topological orders
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Schedule, *my_args)
        return ret

    def schedule_propagate(self, *args):
        """
        V.schedule_propagate(ExecutiveCollection, Information)
        C++: void SchedulePropagate(ExecutiveCollection *execs,
            Information *info)
        Put the current set of executives (modules) to the be scheduled
        given its dependency graph which will be used to compute the set
        topological orders. Then wait for their execution to be complete
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SchedulePropagate, *my_args)
        return ret

    def TASK_PRIORITY(self):
        """
        V.task__priority() -> InformationIntegerKey
        C++: static InformationIntegerKey *TASK_PRIORITY()
        Key to store the priority of a task
        """
        ret = wrap_vtk(self._vtk_obj.TASK_PRIORITY())
        return ret
        

    def wait_for_inputs_released(self, *args):
        """
        V.wait_for_inputs_released(Executive)
        C++: void WaitForInputsReleased(Executive *exec)
        Similar to wait_for_task_done but return whenever input connections
        of a task are released instead of done computing. But exec cannot
        be NULL.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.WaitForInputsReleased, *my_args)
        return ret

    def wait_for_task_done(self, *args):
        """
        V.wait_for_task_done(Executive)
        C++: void WaitForTaskDone(Executive *exec)
        Wait for a task that is on the scheduling queue to be done. If
        the task is not there, this will return immediately. If the exec
        is NULL, any task that is done will trigger this the return
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.WaitForTaskDone, *my_args)
        return ret

    def wait_until_all_done(self):
        """
        V.wait_until_all_done()
        C++: void WaitUntilAllDone()
        Wait for all tasks to be done
        """
        ret = self._vtk_obj.WaitUntilAllDone()
        return ret
        

    def wait_until_done(self, *args):
        """
        V.wait_until_done(ExecutiveCollection)
        C++: void WaitUntilDone(ExecutiveCollection *execs)
        Wait until the current set of executives (modules) have finished
        executing
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.WaitUntilDone, *my_args)
        return ret

    def wait_until_released(self, *args):
        """
        V.wait_until_released(ExecutiveCollection)
        C++: void WaitUntilReleased(ExecutiveCollection *execs)
        Wait until the current set of executives (modules) have their
        inputs released
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.WaitUntilReleased, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExecutionScheduler, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExecutionScheduler properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ExecutionScheduler properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExecutionScheduler properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

