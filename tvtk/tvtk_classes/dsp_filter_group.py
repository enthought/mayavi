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


class DSPFilterGroup(Object):
    """
    DSPFilterGroup - used by the Exodus readers
    
    Superclass: Object
    
    DSPFilterGroup is used by ExodusReader, ExodusIIReader and
    PExodusReader to do temporal smoothing of data
    
    See Also:
    
    DSPFilterDefinition ExodusReader ExodusIIReader
    PExodusReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDSPFilterGroup, obj, update, **traits)
    
    def get_cached_input(self, *args):
        """
        V.get_cached_input(int, int) -> FloatArray
        C++: FloatArray *GetCachedInput(int a_whichFilter,
            int a_whichTimestep)"""
        ret = self._wrap_call(self._vtk_obj.GetCachedInput, *args)
        return wrap_vtk(ret)

    def get_cached_output(self, *args):
        """
        V.get_cached_output(int, int) -> FloatArray
        C++: FloatArray *GetCachedOutput(int a_whichFilter,
            int a_whichTimestep)"""
        ret = self._wrap_call(self._vtk_obj.GetCachedOutput, *args)
        return wrap_vtk(ret)

    def get_filter(self, *args):
        """
        V.get_filter(int) -> DSPFilterDefinition
        C++: DSPFilterDefinition *GetFilter(int a_whichFilter)"""
        ret = self._wrap_call(self._vtk_obj.GetFilter, *args)
        return wrap_vtk(ret)

    def get_input_variable_name(self, *args):
        """
        V.get_input_variable_name(int) -> string
        C++: const char *GetInputVariableName(int a_whichFilter)"""
        ret = self._wrap_call(self._vtk_obj.GetInputVariableName, *args)
        return ret

    def _get_num_filters(self):
        return self._vtk_obj.GetNumFilters()
    num_filters = traits.Property(_get_num_filters, help=\
        """
        
        """
    )

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self):
        """
        V.get_output(int, int, int) -> FloatArray
        C++: FloatArray *GetOutput(int a_whichFilter,
            int a_whichTimestep, int &a_instancesCalculated)"""
        return wrap_vtk(self._vtk_obj.GetOutput())

    def add_filter(self, *args):
        """
        V.add_filter(DSPFilterDefinition)
        C++: void AddFilter(DSPFilterDefinition *filter)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddFilter, *my_args)
        return ret

    def add_input_variable_instance(self, *args):
        """
        V.add_input_variable_instance(string, int, FloatArray)
        C++: void AddInputVariableInstance(const char *a_name,
            int a_timestep, FloatArray *a_data)"""
        my_args = deref_array(args, [('string', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.AddInputVariableInstance, *my_args)
        return ret

    def copy(self, *args):
        """
        V.copy(DSPFilterGroup)
        C++: void Copy(DSPFilterGroup *other)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Copy, *my_args)
        return ret

    def is_this_input_variable_instance_cached(self, *args):
        """
        V.is_this_input_variable_instance_cached(string, int) -> bool
        C++: bool IsThisInputVariableInstanceCached(const char *a_name,
            int a_timestep)"""
        ret = self._wrap_call(self._vtk_obj.IsThisInputVariableInstanceCached, *args)
        return ret

    def is_this_input_variable_instance_needed(self, *args):
        """
        V.is_this_input_variable_instance_needed(string, int, int) -> bool
        C++: bool IsThisInputVariableInstanceNeeded(const char *a_name,
            int a_timestep, int a_outputTimestep)"""
        ret = self._wrap_call(self._vtk_obj.IsThisInputVariableInstanceNeeded, *args)
        return ret

    def remove_filter(self, *args):
        """
        V.remove_filter(string)
        C++: void RemoveFilter(char *a_outputVariableName)"""
        ret = self._wrap_call(self._vtk_obj.RemoveFilter, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DSPFilterGroup, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DSPFilterGroup properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit DSPFilterGroup properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DSPFilterGroup properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

