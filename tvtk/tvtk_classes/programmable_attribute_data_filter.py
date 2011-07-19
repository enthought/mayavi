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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class ProgrammableAttributeDataFilter(DataSetAlgorithm):
    """
    ProgrammableAttributeDataFilter - manipulate attribute (cell and
    point) data via a user-specified function
    
    Superclass: DataSetAlgorithm
    
    ProgrammableAttributeDataFilter is a filter that allows you to
    write a custom procedure to manipulate attribute data - either point
    or cell data. For example, you could generate scalars based on a
    complex formula; convert vectors to normals; compute scalar values as
    a function of vectors, texture coords, and/or any other point data
    attribute; and so on. The filter takes multiple inputs (input plus an
    auxiliary input list), so you can write procedures that combine
    several dataset point attributes. Note that the output of the filter
    is the same type (topology/geometry) as the input.
    
    The filter works as follows. It operates like any other filter (i.e.,
    checking and managing modified and execution times, processing
    Update() and Execute() methods, managing release of data, etc.), but
    the difference is that the Execute() method simply invokes a
    user-specified function with an optional (void *) argument (typically
    the "this" pointer in C++). It is also possible to specify a function
    to delete the argument via execute_method_arg_delete().
    
    To use the filter, you write a procedure to process the input
    datasets, process the data, and generate output data. Typically, this
    means grabbing the input point or cell data (using get_input() and
    maybe get_input_list()), operating on it (creating new point and cell
    attributes such as scalars, vectors, etc.), and then setting the
    point and/or cell attributes in the output dataset (you'll need to
    use get_output() to access the output). (Note: besides C++, it is
    possible to do the same thing in Tcl, Java, or other languages that
    wrap the C++ core.) Remember, proper filter protocol requires that
    you don't modify the input data - you create new output data from the
    input.
    
    Caveats:
    
    This filter operates on any combination of the filter input plus a
    list of additional inputs (at a minimum you must set the filter input
    via set_input()).  It is up to you check whether the input is valid,
    and to insure that the output is valid. Also, you have to write the
    control structure for the traversal and operation on the point and
    cell attribute data.
    
    By default the output point and cell data will be copied through from
    the input point data (using reference counting).  You can control
    this using the output's copy_all_off() flag, or by using individual
    flags for each point data field (i.e., scalars, vectors, etc.)
    
    The output of this filter is the abstract type DataSet, even if
    your input is a concrete type like PolyData. Thus you may need to
    use CastToConcrete to obtain the output as a particular concrete
    type, or one of the special methods of the superclass (e.g.,
    DataSetAlgorithm::GetPolyDataOutput) to retrieve output of the
    correct type.
    
    The filter correctly manages modified time and network execution in
    most cases. However, if you change the definition of the filter
    function, you'll want to send a manual Modified() method to the
    filter to force it to reexecute.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProgrammableAttributeDataFilter, obj, update, **traits)
    
    def _get_input_list(self):
        return wrap_vtk(self._vtk_obj.GetInputList())
    input_list = traits.Property(_get_input_list, help=\
        """
        Return the list of inputs.
        """
    )

    def remove_input(self, *args):
        """
        V.remove_input(DataSet)
        C++: void RemoveInput(DataSet *in)
        Remove a dataset from the list of data to process.
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    def set_execute_method(self, *args):
        """
        V.set_execute_method(function)
        C++: void SetExecuteMethod(void (*f)(void *) , void *arg)
        Specify the function to use to operate on the point attribute
        data. Note that the function takes a single (void *) argument.
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
            return super(ProgrammableAttributeDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ProgrammableAttributeDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ProgrammableAttributeDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProgrammableAttributeDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

