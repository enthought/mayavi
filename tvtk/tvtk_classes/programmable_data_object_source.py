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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class ProgrammableDataObjectSource(DataObjectAlgorithm):
    """
    ProgrammableDataObjectSource - generate source data object via a
    user-specified function
    
    Superclass: DataObjectAlgorithm
    
    ProgrammableDataObjectSource is a source object that is
    programmable by the user. The output of the filter is a data object
    (vtk_data_object) which represents data via an instance of field data.
    To use this object, you must specify a function that creates the
    output.
    
    Example use of this filter includes reading tabular data and encoding
    it as FieldData. You can then use filters like
    DataObjectToDataSetFilter to convert the data object to a dataset
    and then visualize it.  Another important use of this class is that
    it allows users of interpreters (e.g., Tcl or Java) the ability to
    write source objects without having to recompile C++ code or generate
    new libraries.
    
    See Also:
    
    ProgrammableFilter ProgrammableAttributeDataFilter
    ProgrammableSource DataObjectToDataSetFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProgrammableDataObjectSource, obj, update, **traits)
    
    def set_execute_method(self, *args):
        """
        V.set_execute_method(function)
        C++: void SetExecuteMethod(void (*f)(void *) , void *arg)
        Specify the function to use to generate the output data object.
        Note that the function takes a single (void *) argument.
        """
        ret = self._wrap_call(self._vtk_obj.SetExecuteMethod, *args)
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
            return super(ProgrammableDataObjectSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ProgrammableDataObjectSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ProgrammableDataObjectSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProgrammableDataObjectSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

