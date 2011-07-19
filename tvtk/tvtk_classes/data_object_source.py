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

from tvtk.tvtk_classes.source import Source


class DataObjectSource(Source):
    """
    DataObjectSource - abstract class specifies interface for
    
    Superclass: Source
    
    DataObjectSource is an abstract object that specifies behavior and
    interface of field source objects. Field source objects are source
    objects that create FieldData (field data) on output.
    
    Concrete subclasses of DataObjectSource must define Update() and
    Execute() methods. The public method Update() invokes network
    execution and will bring the network up-to-date. The protected
    Execute() method actually does the work of data creation/generation.
    The difference between the two methods is that Update() implements
    input consistency checks and modified time comparisons and then
    invokes the Execute() which is an implementation of a particular
    algorithm.
    
    DataObjectSource provides a mechanism for invoking the methods
    start_method() and end_method() before and after object execution (via
    Execute()). These are convenience methods you can use for any purpose
    (e.g., debugging info, highlighting/notifying user interface, etc.)
    These methods accept a single void* pointer that can be used to send
    data to the methods. It is also possible to specify a function to
    delete the argument via start_method_arg_delete and end_method_arg_delete.
    
    Another method, progress_method() can be specified. Some filters
    invoke this method periodically during their execution. The use is
    similar to that of start_method() and end_method().
    
    An important feature of subclasses of DataObjectSource is that it
    is possible to control the memory-management model (i.e., retain
    output versus delete output data). If enabled the release_data_flag
    enables the deletion of the output data once the downstream process
    object finishes processing the data (please see text).
    
    See Also:
    
    Source Filter FieldDataFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObjectSource, obj, update, **traits)
    
    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    def _set_output(self, obj):
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)
    output = traits.Property(_get_output, _set_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self, idx=None):
        """
        V.get_output() -> DataObject
        C++: DataObject *GetOutput()
        V.get_output(int) -> DataObject
        C++: DataObject *GetOutput(int idx)
        Get the output field of this source.
        """
        if idx is None:
            return wrap_vtk(self._vtk_obj.GetOutput())
        else:
            return wrap_vtk(self._vtk_obj.GetOutput(idx))

    def set_output(self, obj):
        """
        V.set_output(DataObject)
        C++: void SetOutput(DataObject *)"""
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)

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
            return super(DataObjectSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObjectSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['release_data_flag']),
            title='Edit DataObjectSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObjectSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

