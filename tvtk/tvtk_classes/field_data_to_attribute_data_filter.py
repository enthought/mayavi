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


class FieldDataToAttributeDataFilter(DataSetAlgorithm):
    """
    FieldDataToAttributeDataFilter - map field data to dataset
    attribute data
    
    Superclass: DataSetAlgorithm
    
    FieldDataToAttributeDataFilter is a class that maps field data
    into dataset attributes. The input to this filter is any type of
    dataset and the output is the same dataset (geometry/topology) with
    new attribute data (attribute data is passed through if not replaced
    during filter execution).
    
    To use this filter you must specify which field data from the input
    dataset to use. There are three possibilities: the cell field data,
    the point field data, or the field data associated with the data
    object superclass. Then you specify which attribute data to create:
    either cell attribute data or point attribute data.  Finally, you
    must define how to construct the various attribute data types (e.g.,
    scalars, vectors, normals, etc.) from the arrays and the components
    of the arrays from the field data. This is done by associating
    components in the input field with components making up the attribute
    data. For example, you would specify a scalar with three components
    (RGB) by assigning components from the field for the R, then G, then
    B values of the scalars.  You may also have to specify component
    ranges (for each R-G-B) to make sure that the number of R, G, and B
    values is the same. Also, you may want to normalize the components
    which helps distribute the data uniformly.
    
    This filter is often used in conjunction with
    DataObjectToDataSetFilter.  DataObjectToDataSetFilter filter
    generates dataset topology and geometry and passes its input field
    data along to its output. Then this filter is used to generate the
    attribute data to go along with the dataset.
    
    Caveats:
    
    Make sure that the data you extract is consistent. That is, if you
    have N points, extract N point attributes (scalars, vectors, etc.).
    
    See Also:
    
    FieldData DataSet DataObjectToDataSetFilter
    DataSetAttributes DataArray
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFieldDataToAttributeDataFilter, obj, update, **traits)
    
    default_normalize = tvtk_base.false_bool_trait(help=\
        """
        Set the default Normalize() flag for those methods setting a
        default Normalize value (e.g., set_scalar_components).
        """
    )
    def _default_normalize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultNormalize,
                        self.default_normalize_)

    input_field = traits.Trait('data_object_field',
    tvtk_base.TraitRevPrefixMap({'point_data_field': 1, 'data_object_field': 0, 'cell_data_field': 2}), help=\
        """
        Specify which field data to use to generate the output attribute
        data. There are three choices: the field data associated with the
        DataObject superclass; the point field attribute data; and the
        cell field attribute data.
        """
    )
    def _input_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputField,
                        self.input_field_)

    output_attribute_data = traits.Trait('point_data',
    tvtk_base.TraitRevPrefixMap({'cell_data': 0, 'point_data': 1}), help=\
        """
        Specify which attribute data to output: point or cell data
        attributes.
        """
    )
    def _output_attribute_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputAttributeData,
                        self.output_attribute_data_)

    def get_field_array(self, *args):
        """
        V.get_field_array(FieldData, string, int) -> DataArray
        C++: static DataArray *GetFieldArray(FieldData *fd,
            char *name, int comp)
        Return an array of a particular name from field data and do error
        checking.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetFieldArray, *my_args)
        return wrap_vtk(ret)

    def get_normal_component_array_component(self, *args):
        """
        V.get_normal_component_array_component(int) -> int
        C++: int GetNormalComponentArrayComponent(int comp)
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetNormalComponentArrayComponent, *args)
        return ret

    def get_normal_component_array_name(self, *args):
        """
        V.get_normal_component_array_name(int) -> string
        C++: const char *GetNormalComponentArrayName(int comp)
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetNormalComponentArrayName, *args)
        return ret

    def get_normal_component_max_range(self, *args):
        """
        V.get_normal_component_max_range(int) -> int
        C++: int GetNormalComponentMaxRange(int comp)
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetNormalComponentMaxRange, *args)
        return ret

    def get_normal_component_min_range(self, *args):
        """
        V.get_normal_component_min_range(int) -> int
        C++: int GetNormalComponentMinRange(int comp)
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetNormalComponentMinRange, *args)
        return ret

    def get_normal_component_normalize_flag(self, *args):
        """
        V.get_normal_component_normalize_flag(int) -> int
        C++: int GetNormalComponentNormalizeFlag(int comp)
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetNormalComponentNormalizeFlag, *args)
        return ret

    def get_scalar_component_array_component(self, *args):
        """
        V.get_scalar_component_array_component(int) -> int
        C++: int GetScalarComponentArrayComponent(int comp)
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarComponentArrayComponent, *args)
        return ret

    def get_scalar_component_array_name(self, *args):
        """
        V.get_scalar_component_array_name(int) -> string
        C++: const char *GetScalarComponentArrayName(int comp)
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarComponentArrayName, *args)
        return ret

    def get_scalar_component_max_range(self, *args):
        """
        V.get_scalar_component_max_range(int) -> int
        C++: int GetScalarComponentMaxRange(int comp)
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarComponentMaxRange, *args)
        return ret

    def get_scalar_component_min_range(self, *args):
        """
        V.get_scalar_component_min_range(int) -> int
        C++: int GetScalarComponentMinRange(int comp)
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarComponentMinRange, *args)
        return ret

    def get_scalar_component_normalize_flag(self, *args):
        """
        V.get_scalar_component_normalize_flag(int) -> int
        C++: int GetScalarComponentNormalizeFlag(int comp)
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarComponentNormalizeFlag, *args)
        return ret

    def get_t_coord_component_array_component(self, *args):
        """
        V.get_t_coord_component_array_component(int) -> int
        C++: int GetTCoordComponentArrayComponent(int comp)
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTCoordComponentArrayComponent, *args)
        return ret

    def get_t_coord_component_array_name(self, *args):
        """
        V.get_t_coord_component_array_name(int) -> string
        C++: const char *GetTCoordComponentArrayName(int comp)
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTCoordComponentArrayName, *args)
        return ret

    def get_t_coord_component_max_range(self, *args):
        """
        V.get_t_coord_component_max_range(int) -> int
        C++: int GetTCoordComponentMaxRange(int comp)
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTCoordComponentMaxRange, *args)
        return ret

    def get_t_coord_component_min_range(self, *args):
        """
        V.get_t_coord_component_min_range(int) -> int
        C++: int GetTCoordComponentMinRange(int comp)
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTCoordComponentMinRange, *args)
        return ret

    def get_t_coord_component_normalize_flag(self, *args):
        """
        V.get_t_coord_component_normalize_flag(int) -> int
        C++: int GetTCoordComponentNormalizeFlag(int comp)
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTCoordComponentNormalizeFlag, *args)
        return ret

    def get_tensor_component_array_component(self, *args):
        """
        V.get_tensor_component_array_component(int) -> int
        C++: int GetTensorComponentArrayComponent(int comp)
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTensorComponentArrayComponent, *args)
        return ret

    def get_tensor_component_array_name(self, *args):
        """
        V.get_tensor_component_array_name(int) -> string
        C++: const char *GetTensorComponentArrayName(int comp)
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTensorComponentArrayName, *args)
        return ret

    def get_tensor_component_max_range(self, *args):
        """
        V.get_tensor_component_max_range(int) -> int
        C++: int GetTensorComponentMaxRange(int comp)
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTensorComponentMaxRange, *args)
        return ret

    def get_tensor_component_min_range(self, *args):
        """
        V.get_tensor_component_min_range(int) -> int
        C++: int GetTensorComponentMinRange(int comp)
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTensorComponentMinRange, *args)
        return ret

    def get_tensor_component_normalize_flag(self, *args):
        """
        V.get_tensor_component_normalize_flag(int) -> int
        C++: int GetTensorComponentNormalizeFlag(int comp)
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetTensorComponentNormalizeFlag, *args)
        return ret

    def get_vector_component_array_component(self, *args):
        """
        V.get_vector_component_array_component(int) -> int
        C++: int GetVectorComponentArrayComponent(int comp)
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorComponentArrayComponent, *args)
        return ret

    def get_vector_component_array_name(self, *args):
        """
        V.get_vector_component_array_name(int) -> string
        C++: const char *GetVectorComponentArrayName(int comp)
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorComponentArrayName, *args)
        return ret

    def get_vector_component_max_range(self, *args):
        """
        V.get_vector_component_max_range(int) -> int
        C++: int GetVectorComponentMaxRange(int comp)
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorComponentMaxRange, *args)
        return ret

    def get_vector_component_min_range(self, *args):
        """
        V.get_vector_component_min_range(int) -> int
        C++: int GetVectorComponentMinRange(int comp)
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorComponentMinRange, *args)
        return ret

    def get_vector_component_normalize_flag(self, *args):
        """
        V.get_vector_component_normalize_flag(int) -> int
        C++: int GetVectorComponentNormalizeFlag(int comp)
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorComponentNormalizeFlag, *args)
        return ret

    def construct_array(self, *args):
        """
        V.construct_array(DataArray, int, DataArray, int, int, int,
            int) -> int
        C++: static int ConstructArray(DataArray *da, int comp,
            DataArray *frray, int fieldComp, IdType min,
            IdType max, int normalize)
        Construct a portion of a data array (the comp portion) from
        another data array and its component. The variables min and max
        control the range of the data to use from the other data array;
        normalize is a flag that when set will normalize the data between
        (0,1).
        """
        my_args = deref_array(args, [('vtkDataArray', 'int', 'vtkDataArray', 'int', 'int', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.ConstructArray, *my_args)
        return ret

    def set_normal_component(self, *args):
        """
        V.set_normal_component(int, string, int, int, int, int)
        C++: void SetNormalComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.set_normal_component(int, string, int)
        C++: void SetNormalComponent(int comp, const char *arrayName,
            int arrayComp)
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.SetNormalComponent, *args)
        return ret

    def set_scalar_component(self, *args):
        """
        V.set_scalar_component(int, string, int, int, int, int)
        C++: void SetScalarComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.set_scalar_component(int, string, int)
        C++: void SetScalarComponent(int comp, const char *arrayName,
            int arrayComp)
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.SetScalarComponent, *args)
        return ret

    def set_t_coord_component(self, *args):
        """
        V.set_t_coord_component(int, string, int, int, int, int)
        C++: void SetTCoordComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.set_t_coord_component(int, string, int)
        C++: void SetTCoordComponent(int comp, const char *arrayName,
            int arrayComp)
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ret = self._wrap_call(self._vtk_obj.SetTCoordComponent, *args)
        return ret

    def set_tensor_component(self, *args):
        """
        V.set_tensor_component(int, string, int, int, int, int)
        C++: void SetTensorComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.set_tensor_component(int, string, int)
        C++: void SetTensorComponent(int comp, const char *arrayName,
            int arrayComp)
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.SetTensorComponent, *args)
        return ret

    def set_vector_component(self, *args):
        """
        V.set_vector_component(int, string, int, int, int, int)
        C++: void SetVectorComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.set_vector_component(int, string, int)
        C++: void SetVectorComponent(int comp, const char *arrayName,
            int arrayComp)
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ret = self._wrap_call(self._vtk_obj.SetVectorComponent, *args)
        return ret

    def update_component_range(self, *args):
        """
        V.update_component_range(DataArray, [int, int]) -> int
        C++: static int UpdateComponentRange(DataArray *da,
            IdType compRange[2])
        Update the maximum and minimum component range values. Returns a
        flag indicating whether the range was updated.
        """
        my_args = deref_array(args, [('vtkDataArray', ['int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.UpdateComponentRange, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('default_normalize',
    'GetDefaultNormalize'), ('output_attribute_data',
    'GetOutputAttributeData'), ('debug', 'GetDebug'), ('input_field',
    'GetInputField'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'default_normalize',
    'global_warning_display', 'release_data_flag', 'input_field',
    'output_attribute_data', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FieldDataToAttributeDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FieldDataToAttributeDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['default_normalize'], ['input_field',
            'output_attribute_data'], []),
            title='Edit FieldDataToAttributeDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FieldDataToAttributeDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

