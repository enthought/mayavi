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


class FunctionParser(Object):
    """
    FunctionParser - Parse and evaluate a mathematical expression
    
    Superclass: Object
    
    FunctionParser is a class that takes in a mathematical expression
    as a char string, parses it, and evaluates it at the specified values
    of the variables in the input string.
    
    You can use the "if" operator to create conditional expressions such
    as if ( test, trueresult, falseresult). These evaluate the boolean
    valued test expression and then evaluate either the trueresult or the
    falseresult expression to produce a final (scalar or vector valued)
    value. "test" may contain <,>,=,|,&, and () and all three
    subexpressions can evaluate arbitrary function operators (ln, cos, +,
    if, etc)
    
    Thanks:
    
    Juha Nieminen (juha.nieminen@gmail.com) for relicensing this branch
    of the function parser code that this class is based upon under the
    new BSD license so that it could be used in VTK. Note, the BSD
    license applies to this version of the function parser only (by
    permission of the author), and not the original library.
    
    Thomas Dunne (thomas.dunne@iwr.uni-heidelberg.de) for adding code for
    two-parameter-parsing and a few functions (sign, min, max).
    
    Sid Sydoriak (sxs@lanl.gov) for adding boolean operations and
    conditional expressions and for fixing a variety of bugs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFunctionParser, obj, update, **traits)
    
    replace_invalid_values = tvtk_base.false_bool_trait(help=\
        """
        When replace_invalid_values is on, all invalid values (such as
        sqrt(-2), note that function parser does not handle complex
        numbers) will be replaced by replacement_value. Otherwise an error
        will be reported
        """
    )
    def _replace_invalid_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplaceInvalidValues,
                        self.replace_invalid_values_)

    function = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _function_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFunction,
                        self.function)

    def get_vector_variable_value(self, *args):
        """
        V.get_vector_variable_value(string) -> (float, float, float)
        C++: double *GetVectorVariableValue(const char *variableName)
        V.get_vector_variable_value(string, [float, float, float])
        C++: void GetVectorVariableValue(const char *variableName,
            double value[3])
        V.get_vector_variable_value(int) -> (float, float, float)
        C++: double *GetVectorVariableValue(int i)
        V.get_vector_variable_value(int, [float, float, float])
        C++: void GetVectorVariableValue(int i, double value[3])
        Get the value of a vector variable.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorVariableValue, *args)
        return ret

    def set_vector_variable_value(self, *args):
        """
        V.set_vector_variable_value(string, float, float, float)
        C++: void SetVectorVariableValue(const char *variableName,
            double xValue, double yValue, double zValue)
        V.set_vector_variable_value(string, (float, float, float))
        C++: void SetVectorVariableValue(const char *variableName,
            const double values[3])
        V.set_vector_variable_value(int, float, float, float)
        C++: void SetVectorVariableValue(int i, double xValue,
            double yValue, double zValue)
        V.set_vector_variable_value(int, (float, float, float))
        C++: void SetVectorVariableValue(int i, const double values[3])
        Set the value of a vector variable.  If a variable with this name
        exists, then its value will be set to the new value.  If there is
        not already a variable with this name, variable_name will be added
        to the list of variables, and its value will be set to the new
        value.
        """
        ret = self._wrap_call(self._vtk_obj.SetVectorVariableValue, *args)
        return ret

    def get_scalar_variable_value(self, *args):
        """
        V.get_scalar_variable_value(string) -> float
        C++: double GetScalarVariableValue(const char *variableName)
        V.get_scalar_variable_value(int) -> float
        C++: double GetScalarVariableValue(int i)
        Get the value of a scalar variable.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarVariableValue, *args)
        return ret

    def set_scalar_variable_value(self, *args):
        """
        V.set_scalar_variable_value(string, float)
        C++: void SetScalarVariableValue(const char *variableName,
            double value)
        V.set_scalar_variable_value(int, float)
        C++: void SetScalarVariableValue(int i, double value)
        Set the value of a scalar variable.  If a variable with this name
        exists, then its value will be set to the new value.  If there is
        not already a variable with this name, variable_name will be added
        to the list of variables, and its value will be set to the new
        value.
        """
        ret = self._wrap_call(self._vtk_obj.SetScalarVariableValue, *args)
        return ret

    replacement_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        When replace_invalid_values is on, all invalid values (such as
        sqrt(-2), note that function parser does not handle complex
        numbers) will be replaced by replacement_value. Otherwise an error
        will be reported
        """
    )
    def _replacement_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplacementValue,
                        self.replacement_value)

    def _get_number_of_scalar_variables(self):
        return self._vtk_obj.GetNumberOfScalarVariables()
    number_of_scalar_variables = traits.Property(_get_number_of_scalar_variables, help=\
        """
        Get the number of scalar variables.
        """
    )

    def _get_number_of_vector_variables(self):
        return self._vtk_obj.GetNumberOfVectorVariables()
    number_of_vector_variables = traits.Property(_get_number_of_vector_variables, help=\
        """
        Get the number of vector variables.
        """
    )

    def _get_scalar_result(self):
        return self._vtk_obj.GetScalarResult()
    scalar_result = traits.Property(_get_scalar_result, help=\
        """
        Get a scalar result from evaluating the input function.
        """
    )

    def get_scalar_variable_name(self, *args):
        """
        V.get_scalar_variable_name(int) -> string
        C++: char *GetScalarVariableName(int i)
        Get the ith scalar variable name.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarVariableName, *args)
        return ret

    def _get_vector_result(self):
        return self._vtk_obj.GetVectorResult()
    vector_result = traits.Property(_get_vector_result, help=\
        """
        Get a vector result from evaluating the input function.
        """
    )

    def get_vector_variable_name(self, *args):
        """
        V.get_vector_variable_name(int) -> string
        C++: char *GetVectorVariableName(int i)
        Get the ith vector variable name.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorVariableName, *args)
        return ret

    def is_scalar_result(self):
        """
        V.is_scalar_result() -> int
        C++: int IsScalarResult()
        Check whether the result is a scalar result.  If it isn't, then
        either the result is a vector or an error has occurred.
        """
        ret = self._vtk_obj.IsScalarResult()
        return ret
        

    def is_vector_result(self):
        """
        V.is_vector_result() -> int
        C++: int IsVectorResult()
        Check whether the result is a vector result.  If it isn't, then
        either the result is scalar or an error has occurred.
        """
        ret = self._vtk_obj.IsVectorResult()
        return ret
        

    def remove_all_variables(self):
        """
        V.remove_all_variables()
        C++: void RemoveAllVariables()
        Remove all the current variables.
        """
        ret = self._vtk_obj.RemoveAllVariables()
        return ret
        

    def remove_scalar_variables(self):
        """
        V.remove_scalar_variables()
        C++: void RemoveScalarVariables()
        Remove all the scalar variables.
        """
        ret = self._vtk_obj.RemoveScalarVariables()
        return ret
        

    def remove_vector_variables(self):
        """
        V.remove_vector_variables()
        C++: void RemoveVectorVariables()
        Remove all the vector variables.
        """
        ret = self._vtk_obj.RemoveVectorVariables()
        return ret
        

    _updateable_traits_ = \
    (('function', 'GetFunction'), ('debug', 'GetDebug'),
    ('replacement_value', 'GetReplacementValue'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('replace_invalid_values', 'GetReplaceInvalidValues'),
    ('reference_count', 'GetReferenceCount'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'replace_invalid_values',
    'function', 'replacement_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FunctionParser, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FunctionParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['replace_invalid_values'], [], ['function',
            'replacement_value']),
            title='Edit FunctionParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FunctionParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

