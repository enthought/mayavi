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

from tvtk.tvtk_classes.process_object import ProcessObject


class Source(ProcessObject):
    """
    Source - abstract class specifies interface for visualization
    network source
    
    Superclass: ProcessObject
    
    Source is an abstract object that specifies behavior and interface
    of source objects. Source objects are objects that begin
    visualization pipeline. Sources include readers (read data from file
    or communications port) and procedural sources (generate data
    programmatically). Source objects are also objects that generate
    output data. In this sense Source is used as a superclass to
    Filter.
    
    Concrete subclasses of Source must define Update() and Execute()
    methods. The public method Update() invokes network execution and
    will bring the network up-to-date. The protected Execute() method
    actually does the work of data creation/generation. The difference
    between the two methods is that Update() implements input consistency
    checks and modified time comparisons and then invokes the Execute()
    which is an implementation of a particular algorithm.
    
    An important feature of subclasses of Source is that it is
    possible to control the memory-management model (i.e., retain output
    versus delete output data). If enabled the release_data_flag enables
    the deletion of the output data once the downstream process object
    finishes processing the data (please see text).
    
    See Also:
    
    ProcessObject DataSetReader Filter PolyDataSource
    StructuredGridSource StructuredPointsSource
    UnstructuredGridSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSource, obj, update, **traits)
    
    release_data_flag = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Turn on/off flag to control whether this object's data is
        released after being used by a source.
        """
    )
    def _release_data_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReleaseDataFlag,
                        self.release_data_flag)

    def _get_number_of_outputs(self):
        return self._vtk_obj.GetNumberOfOutputs()
    number_of_outputs = traits.Property(_get_number_of_outputs, help=\
        """
        Return an array with all the inputs of this process object. This
        is useful for tracing back in the pipeline to construct graphs
        etc.
        """
    )

    def get_output_index(self, *args):
        """
        V.get_output_index(DataObject) -> int
        C++: int GetOutputIndex(DataObject *out)
        Return what index output the passed in output is, return -1 if it
        does not match any of the outputs
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetOutputIndex, *my_args)
        return ret

    def compute_input_update_extents(self, *args):
        """
        V.compute_input_update_extents(DataObject)
        C++: virtual void ComputeInputUpdateExtents(DataObject *output)
        What is the input update extent that is required to produce the
        desired output? By default, the whole input is always required
        but this is overridden in many subclasses.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeInputUpdateExtents, *my_args)
        return ret

    def propagate_update_extent(self, *args):
        """
        V.propagate_update_extent(DataObject)
        C++: virtual void PropagateUpdateExtent(DataObject *output)
        WARNING: INTERNAL METHOD - NOT FOR GENERAL USE. THIS METHOD IS
        PART OF THE PIPELINE UPDATE FUNCTIONALITY. The update extent for
        this object is propagated up the pipeline. This propagation may
        early terminate based on the pipeline_m_time.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PropagateUpdateExtent, *my_args)
        return ret

    def trigger_asynchronous_update(self):
        """
        V.trigger_asynchronous_update()
        C++: virtual void TriggerAsynchronousUpdate()
        WARNING: INTERNAL METHOD - NOT FOR GENERAL USE. THIS METHOD IS
        PART OF THE PIPELINE UPDATE FUNCTIONALITY. Propagate back up the
        pipeline for ports and trigger the update on the other side of
        the port to allow for asynchronous parallel processing in the
        pipeline. This propagation may early terminate based on the
        pipeline_m_time.
        """
        ret = self._vtk_obj.TriggerAsynchronousUpdate()
        return ret
        

    def un_register_all_outputs(self):
        """
        V.un_register_all_outputs()
        C++: void UnRegisterAllOutputs(void)
        Release/disconnect all outputs of this source. This is intended
        to be called prior to Delete() if the user is concerned about
        outputs holding on to the filter/source.
        """
        ret = self._vtk_obj.UnRegisterAllOutputs()
        return ret
        

    def update_data(self, *args):
        """
        V.update_data(DataObject)
        C++: virtual void UpdateData(DataObject *output)
        WARNING: INTERNAL METHOD - NOT FOR GENERAL USE. THIS METHOD IS
        PART OF THE PIPELINE UPDATE FUNCTIONALITY. Propagate the update
        back up the pipeline, and perform the actual work of updating on
        the way down. When the propagate arrives at a port, block and
        wait for the asynchronous update to finish on the other side.
        This propagation may early terminate based on the pipeline_m_time.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateData, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'release_data_flag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Source, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Source properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['release_data_flag']),
            title='Edit Source properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Source properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

