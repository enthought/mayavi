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


class DSPFilterDefinition(Object):
    """
    DSPFilterDefinition - used by the Exodus readers
    
    Superclass: Object
    
    DSPFilterDefinition is used by ExodusReader, ExodusIIReader
    and PExodusReader to do temporal smoothing of data
    
    See Also:
    
    DSPFilterGroup ExodusReader ExodusIIReader PExodusReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDSPFilterDefinition, obj, update, **traits)
    
    output_variable_name = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _output_variable_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputVariableName,
                        self.output_variable_name)

    input_variable_name = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _input_variable_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputVariableName,
                        self.input_variable_name)

    def get_denominator_weight(self, *args):
        """
        V.get_denominator_weight(int) -> float
        C++: double GetDenominatorWeight(int a_which)"""
        ret = self._wrap_call(self._vtk_obj.GetDenominatorWeight, *args)
        return ret

    def get_forward_numerator_weight(self, *args):
        """
        V.get_forward_numerator_weight(int) -> float
        C++: double GetForwardNumeratorWeight(int a_which)"""
        ret = self._wrap_call(self._vtk_obj.GetForwardNumeratorWeight, *args)
        return ret

    def _get_num_denominator_weights(self):
        return self._vtk_obj.GetNumDenominatorWeights()
    num_denominator_weights = traits.Property(_get_num_denominator_weights, help=\
        """
        
        """
    )

    def _get_num_forward_numerator_weights(self):
        return self._vtk_obj.GetNumForwardNumeratorWeights()
    num_forward_numerator_weights = traits.Property(_get_num_forward_numerator_weights, help=\
        """
        
        """
    )

    def _get_num_numerator_weights(self):
        return self._vtk_obj.GetNumNumeratorWeights()
    num_numerator_weights = traits.Property(_get_num_numerator_weights, help=\
        """
        
        """
    )

    def get_numerator_weight(self, *args):
        """
        V.get_numerator_weight(int) -> float
        C++: double GetNumeratorWeight(int a_which)"""
        ret = self._wrap_call(self._vtk_obj.GetNumeratorWeight, *args)
        return ret

    def clear(self):
        """
        V.clear()
        C++: void Clear()"""
        ret = self._vtk_obj.Clear()
        return ret
        

    def copy(self, *args):
        """
        V.copy(DSPFilterDefinition)
        C++: void Copy(DSPFilterDefinition *other)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Copy, *my_args)
        return ret

    def is_this_input_variable_instance_needed(self, *args):
        """
        V.is_this_input_variable_instance_needed(int, int) -> bool
        C++: bool IsThisInputVariableInstanceNeeded(int a_timestep,
            int a_outputTimestep)"""
        ret = self._wrap_call(self._vtk_obj.IsThisInputVariableInstanceNeeded, *args)
        return ret

    def push_back_denominator_weight(self, *args):
        """
        V.push_back_denominator_weight(float)
        C++: void PushBackDenominatorWeight(double a_value)"""
        ret = self._wrap_call(self._vtk_obj.PushBackDenominatorWeight, *args)
        return ret

    def push_back_forward_numerator_weight(self, *args):
        """
        V.push_back_forward_numerator_weight(float)
        C++: void PushBackForwardNumeratorWeight(double a_value)"""
        ret = self._wrap_call(self._vtk_obj.PushBackForwardNumeratorWeight, *args)
        return ret

    def push_back_numerator_weight(self, *args):
        """
        V.push_back_numerator_weight(float)
        C++: void PushBackNumeratorWeight(double a_value)"""
        ret = self._wrap_call(self._vtk_obj.PushBackNumeratorWeight, *args)
        return ret

    _updateable_traits_ = \
    (('output_variable_name', 'GetOutputVariableName'),
    ('input_variable_name', 'GetInputVariableName'), ('reference_count',
    'GetReferenceCount'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'input_variable_name',
    'output_variable_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DSPFilterDefinition, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DSPFilterDefinition properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['input_variable_name',
            'output_variable_name']),
            title='Edit DSPFilterDefinition properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DSPFilterDefinition properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

