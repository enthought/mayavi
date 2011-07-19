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

from tvtk.tvtk_classes.algorithm import Algorithm


class ProcessObject(Algorithm):
    """
    ProcessObject - abstract class specifies interface for
    visualization filters
    
    Superclass: Algorithm
    
    ProcessObject is an abstract object that specifies behavior and
    interface of visualization network process objects (sources, filters,
    mappers). Source objects are creators of visualization data; filters
    input, process, and output visualization data; and mappers transform
    data into another form (like rendering primitives or write data to a
    file).
    
    ProcessObject fires events for Start and End events before and
    after object execution (via Execute()). These events can be used for
    any purpose (e.g., debugging info, highlighting/notifying user
    interface, etc.)
    
    Another event, Progress, can be observed. Some filters fire this
    event periodically during their execution. The use is similar to that
    of Start and End events. Filters may also check their abort_execute
    flag to determine whether to prematurely end their execution.
    
    An important feature of subclasses of ProcessObject is that it is
    possible to control the memory-management model (i.e., retain output
    versus delete output data). If enabled the release_data_flag enables
    the deletion of the output data once the downstream process object
    finishes processing the data (please see text).
    
    See Also:
    
    DataObject Source Filter Mapper Writer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProcessObject, obj, update, **traits)
    
    def _get_number_of_inputs(self):
        return self._vtk_obj.GetNumberOfInputs()
    number_of_inputs = traits.Property(_get_number_of_inputs, help=\
        """
        Return an array with all the inputs of this process object. This
        is useful for tracing back in the pipeline to construct graphs
        etc.
        """
    )

    def set_nth_input_connection(self, *args):
        """
        V.set_nth_input_connection(int, int, AlgorithmOutput)
        C++: virtual void SetNthInputConnection(int port, int index,
            AlgorithmOutput *input)
        Reimplemented from Algorithm to maintain backward
        compatibility for ProcessObject.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetNthInputConnection, *my_args)
        return ret

    def set_number_of_input_connections(self, *args):
        """
        V.set_number_of_input_connections(int, int)
        C++: virtual void SetNumberOfInputConnections(int port, int n)
        Reimplemented from Algorithm to maintain backward
        compatibility for ProcessObject.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfInputConnections, *args)
        return ret

    def squeeze_input_array(self):
        """
        V.squeeze_input_array()
        C++: void SqueezeInputArray()
        This method will rearrange the input array so that all NULL
        entries are removed.
        """
        ret = self._vtk_obj.SqueezeInputArray()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProcessObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ProcessObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ProcessObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProcessObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

