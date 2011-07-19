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

from tvtk.tvtk_classes.composite_data_pipeline import CompositeDataPipeline


class ThreadedStreamingPipeline(CompositeDataPipeline):
    """
    ThreadedStreamingPipeline - Executive supporting multi-threads
    
    Superclass: CompositeDataPipeline
    
    ThreadeStreamingDemandDrivenPipeline is an executive that supports
    updating input ports based on the number of threads available.
    
    See Also:
    
    ExecutionScheduler
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThreadedStreamingPipeline, obj, update, **traits)
    
    def _get_resources(self):
        return wrap_vtk(self._vtk_obj.GetResources())
    resources = traits.Property(_get_resources, help=\
        """
        Return the scheduling for this executive
        """
    )

    def AUTO_PROPAGATE(self):
        """
        V.auto__propagate() -> InformationIntegerKey
        C++: static InformationIntegerKey *AUTO_PROPAGATE()
        Key to store the priority of a task
        """
        ret = wrap_vtk(self._vtk_obj.AUTO_PROPAGATE())
        return ret
        

    def EXTRA_INFORMATION(self):
        """
        V.extra__information() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *EXTRA_INFORMATION()
        Key to store the additional information for an update request
        """
        ret = wrap_vtk(self._vtk_obj.EXTRA_INFORMATION())
        return ret
        

    def force_update_data(self, *args):
        """
        V.force_update_data(int, Information) -> int
        C++: int ForceUpdateData(int processingUnit, Information *info)
        Send a direct REQUEST_DATA (on all ports) to this executive
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ForceUpdateData, *my_args)
        return ret

    def pull(self, *args):
        """
        V.pull(ExecutiveCollection)
        C++: static void Pull(ExecutiveCollection *execs)
        V.pull(ExecutiveCollection, Information)
        C++: static void Pull(ExecutiveCollection *execs,
            Information *info)
        V.pull(Executive)
        C++: static void Pull(Executive *exec)
        V.pull(Executive, Information)
        C++: static void Pull(Executive *exec, Information *info)
        V.pull()
        C++: void Pull()
        V.pull(Information)
        C++: void Pull(Information *info)
        Trigger the updates on certain execs and asking all of its
        upstream modules to be updated as well (propagate up)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Pull, *my_args)
        return ret

    def push(self, *args):
        """
        V.push(ExecutiveCollection)
        C++: static void Push(ExecutiveCollection *execs)
        V.push(ExecutiveCollection, Information)
        C++: static void Push(ExecutiveCollection *execs,
            Information *info)
        V.push(Executive)
        C++: static void Push(Executive *exec)
        V.push(Executive, Information)
        C++: static void Push(Executive *exec, Information *info)
        V.push()
        C++: void Push()
        V.push(Information)
        C++: void Push(Information *info)
        Trigger the updates on certain execs and asking all of its
        downstream modules to be updated as well (propagate down)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Push, *my_args)
        return ret

    def release_inputs(self):
        """
        V.release_inputs()
        C++: void ReleaseInputs()
        Release all the locks for input ports living upstream
        """
        ret = self._vtk_obj.ReleaseInputs()
        return ret
        

    def set_auto_propagate_push(self, *args):
        """
        V.set_auto_propagate_push(bool)
        C++: static void SetAutoPropagatePush(bool enabled)
        Enable/Disable automatic propagation of Push events
        """
        ret = self._wrap_call(self._vtk_obj.SetAutoPropagatePush, *args)
        return ret

    def set_multi_threaded_enabled(self, *args):
        """
        V.set_multi_threaded_enabled(bool)
        C++: static void SetMultiThreadedEnabled(bool enabled)
        Enable/Disable Multi-Threaded updating mechanism
        """
        ret = self._wrap_call(self._vtk_obj.SetMultiThreadedEnabled, *args)
        return ret

    def update_request_data_time_from_source(self):
        """
        V.update_request_data_time_from_source()
        C++: void UpdateRequestDataTimeFromSource()
        Update the last_data_request_time_from_source using its upstream time
        """
        ret = self._vtk_obj.UpdateRequestDataTimeFromSource()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThreadedStreamingPipeline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ThreadedStreamingPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ThreadedStreamingPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThreadedStreamingPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

