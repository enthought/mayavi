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


class ArrayCalculator(DataSetAlgorithm):
    """
    ArrayCalculator - perform mathematical operations on data in field
    data arrays
    
    Superclass: DataSetAlgorithm
    
    ArrayCalculator performs operations on vectors or scalars in field
    data arrays.  It uses FunctionParser to do the parsing and to
    evaluate the function for each entry in the input arrays.  The arrays
    used in a given function must be all in point data or all in cell
    data. The resulting array will be stored as a field data array.  The
    result array can either be stored in a new array or it can overwrite
    an existing array.
    
    The functions that this array calculator understands is:
    
    standard operations: + - * / ^ . build unit vectors: i_hat, j_hat, k_hat
    (ie (1,0,0), (0,1,0), (0,0,1)) abs acos asin atan ceil cos cosh exp
    floor log mag min max norm sign sin sinh sqrt tan tanh  Note that
    some of these operations work on scalars, some on vectors, and some
    on both (e.g., you can multiply a scalar times a vector). The
    operations are performed tuple-wise (i.e., tuple-by-tuple). The user
    must specify which arrays to use as vectors and/or scalars, and the
    name of the output data array.
    
    See Also:
    
    FunctionParser
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArrayCalculator, obj, update, **traits)
    
    coordinate_results = tvtk_base.false_bool_trait(help=\
        """
        Set whether to output results as coordinates.  result_array_name
        will be ignored.  Outputing as coordinates is only valid with
        vector results and if the attribute_mode is
        attribute_mode_to_use_point_data. If a valid output can't be made, an
        error will occur.
        """
    )
    def _coordinate_results_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoordinateResults,
                        self.coordinate_results_)

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

    attribute_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'use_point_data': 1, 'use_cell_data': 2, 'use_edge_data': 4, 'use_vertex_data': 3}), help=\
        """
        Control whether the filter operates on point data or cell data.
        By default (_attribute_mode_to_default), the filter uses point data.
        Alternatively you can explicitly set the filter to use point data
        (_attribute_mode_to_use_point_data) or cell data
        (_attribute_mode_to_use_cell_data). For graphs you can set the filter
        to use vertex data (_attribute_mode_to_use_vertex_data) or edge data
        (_attribute_mode_to_use_edge_data).
        """
    )
    def _attribute_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttributeMode,
                        self.attribute_mode_)

    function = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the function to be evaluated.
        """
    )
    def _function_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFunction,
                        self.function)

    result_array_type = traits.Int(11, enter_set=True, auto_set=False, help=\
        """
        Type of the result array. It is ignored if coordinate_results is
        true. Initial value is VTK_DOUBLE.
        """
    )
    def _result_array_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResultArrayType,
                        self.result_array_type)

    result_array_name = traits.String(r"resultArray", enter_set=True, auto_set=False, help=\
        """
        Set the name of the array in which to store the result of
        evaluating this function.  If this is the name of an existing
        array, that array will be overwritten.  Otherwise a new array
        will be created with the specified name.
        """
    )
    def _result_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResultArrayName,
                        self.result_array_name)

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

    def _get_number_of_scalar_arrays(self):
        return self._vtk_obj.GetNumberOfScalarArrays()
    number_of_scalar_arrays = traits.Property(_get_number_of_scalar_arrays, help=\
        """
        Methods to get information about the current variables.
        """
    )

    def _get_number_of_vector_arrays(self):
        return self._vtk_obj.GetNumberOfVectorArrays()
    number_of_vector_arrays = traits.Property(_get_number_of_vector_arrays, help=\
        """
        Methods to get information about the current variables.
        """
    )

    def get_scalar_array_name(self, *args):
        """
        V.get_scalar_array_name(int) -> string
        C++: char *GetScalarArrayName(int i)
        Methods to get information about the current variables.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarArrayName, *args)
        return ret

    def get_scalar_variable_name(self, *args):
        """
        V.get_scalar_variable_name(int) -> string
        C++: char *GetScalarVariableName(int i)
        Methods to get information about the current variables.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarVariableName, *args)
        return ret

    def get_selected_scalar_component(self, *args):
        """
        V.get_selected_scalar_component(int) -> int
        C++: int GetSelectedScalarComponent(int i)
        Methods to get information about the current variables.
        """
        ret = self._wrap_call(self._vtk_obj.GetSelectedScalarComponent, *args)
        return ret

    def get_vector_array_name(self, *args):
        """
        V.get_vector_array_name(int) -> string
        C++: char *GetVectorArrayName(int i)
        Methods to get information about the current variables.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorArrayName, *args)
        return ret

    def get_vector_variable_name(self, *args):
        """
        V.get_vector_variable_name(int) -> string
        C++: char *GetVectorVariableName(int i)
        Methods to get information about the current variables.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorVariableName, *args)
        return ret

    def add_coordinate_scalar_variable(self, *args):
        """
        V.add_coordinate_scalar_variable(string, int)
        C++: void AddCoordinateScalarVariable(const char *variableName,
            int component=0)
        Add a variable name, a corresponding array name, and which
        components of the array to use.
        """
        ret = self._wrap_call(self._vtk_obj.AddCoordinateScalarVariable, *args)
        return ret

    def add_coordinate_vector_variable(self, *args):
        """
        V.add_coordinate_vector_variable(string, int, int, int)
        C++: void AddCoordinateVectorVariable(const char *variableName,
            int component0=0, int component1=1, int component2=2)
        Add a variable name, a corresponding array name, and which
        components of the array to use.
        """
        ret = self._wrap_call(self._vtk_obj.AddCoordinateVectorVariable, *args)
        return ret

    def add_scalar_array_name(self, *args):
        """
        V.add_scalar_array_name(string, int)
        C++: void AddScalarArrayName(const char *arrayName,
            int component=0)
        Add an array name to the list of arrays used in the function and
        specify which components of the array to use in evaluating the
        function.  The array name must match the name in the function. 
        Use add_scalar_variable or add_vector_variable to use a variable name
        different from the array name.
        """
        ret = self._wrap_call(self._vtk_obj.AddScalarArrayName, *args)
        return ret

    def add_scalar_variable(self, *args):
        """
        V.add_scalar_variable(string, string, int)
        C++: void AddScalarVariable(const char *variableName,
            const char *arrayName, int component=0)
        Add a variable name, a corresponding array name, and which
        components of the array to use.
        """
        ret = self._wrap_call(self._vtk_obj.AddScalarVariable, *args)
        return ret

    def add_vector_array_name(self, *args):
        """
        V.add_vector_array_name(string, int, int, int)
        C++: void AddVectorArrayName(const char *arrayName,
            int component0=0, int component1=1, int component2=2)
        Add an array name to the list of arrays used in the function and
        specify which components of the array to use in evaluating the
        function.  The array name must match the name in the function. 
        Use add_scalar_variable or add_vector_variable to use a variable name
        different from the array name.
        """
        ret = self._wrap_call(self._vtk_obj.AddVectorArrayName, *args)
        return ret

    def add_vector_variable(self, *args):
        """
        V.add_vector_variable(string, string, int, int, int)
        C++: void AddVectorVariable(const char *variableName,
            const char *arrayName, int component0=0, int component1=1,
            int component2=2)
        Add a variable name, a corresponding array name, and which
        components of the array to use.
        """
        ret = self._wrap_call(self._vtk_obj.AddVectorVariable, *args)
        return ret

    def remove_all_variables(self):
        """
        V.remove_all_variables()
        C++: void RemoveAllVariables()
        Remove all the variable names and their associated array names.
        """
        ret = self._vtk_obj.RemoveAllVariables()
        return ret
        

    def remove_coordinate_scalar_variables(self):
        """
        V.remove_coordinate_scalar_variables()
        C++: virtual void RemoveCoordinateScalarVariables()
        Remove all the coordinate variables.
        """
        ret = self._vtk_obj.RemoveCoordinateScalarVariables()
        return ret
        

    def remove_coordinate_vector_variables(self):
        """
        V.remove_coordinate_vector_variables()
        C++: virtual void RemoveCoordinateVectorVariables()
        Remove all the coordinate variables.
        """
        ret = self._vtk_obj.RemoveCoordinateVectorVariables()
        return ret
        

    def remove_scalar_variables(self):
        """
        V.remove_scalar_variables()
        C++: virtual void RemoveScalarVariables()
        Remove all the scalar variable names and their associated array
        names.
        """
        ret = self._vtk_obj.RemoveScalarVariables()
        return ret
        

    def remove_vector_variables(self):
        """
        V.remove_vector_variables()
        C++: virtual void RemoveVectorVariables()
        Remove all the scalar variable names and their associated array
        names.
        """
        ret = self._vtk_obj.RemoveVectorVariables()
        return ret
        

    _updateable_traits_ = \
    (('function', 'GetFunction'), ('attribute_mode', 'GetAttributeMode'),
    ('replacement_value', 'GetReplacementValue'), ('result_array_name',
    'GetResultArrayName'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('replace_invalid_values',
    'GetReplaceInvalidValues'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('coordinate_results', 'GetCoordinateResults'),
    ('result_array_type', 'GetResultArrayType'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'coordinate_results', 'debug',
    'global_warning_display', 'release_data_flag',
    'replace_invalid_values', 'attribute_mode', 'function',
    'progress_text', 'replacement_value', 'result_array_name',
    'result_array_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArrayCalculator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ArrayCalculator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['coordinate_results', 'replace_invalid_values'],
            ['attribute_mode'], ['function', 'replacement_value',
            'result_array_name', 'result_array_type']),
            title='Edit ArrayCalculator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArrayCalculator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

