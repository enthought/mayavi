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


class FieldData(Object):
    """
    FieldData - represent and manipulate fields of data
    
    Superclass: Object
    
    FieldData represents and manipulates fields of data. The model of
    a field is a m x n matrix of data values, where m is the number of
    tuples, and n is the number of components. (A tuple is a row of n
    components in the matrix.) The field is assumed to be composed of a
    set of one or more data arrays, where the data in the arrays are of
    different types (e.g., int, double, char, etc.), and there may be
    variable numbers of components in each array. Note that each data
    array is assumed to be "m" in length (i.e., number of tuples), which
    typically corresponds to the number of points or cells in a dataset.
    Also, each data array must have a character-string name. (This is
    used to manipulate data.)
    
    There are two ways of manipulating and interfacing to fields. You can
    do it generically by manipulating components/tuples via a double-type
    data exchange, or you can do it by grabbing the arrays and
    manipulating them directly. The former is simpler but performs type
    conversion, which is bad if your data has non-castable types like
    (void) pointers, or you lose information as a result of the cast.
    The, more efficient method means managing each array in the field. 
    Using this method you can create faster, more efficient algorithms
    that do not lose information.
    
    See Also:
    
    AbstractArray DataSetAttributes PointData CellData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFieldData, obj, update, **traits)
    
    def get_component(self, *args):
        """
        V.get_component(int, int) -> float
        C++: double GetComponent(const IdType i, const int j)
        Get the component value at the ith tuple (or row) and jth
        component (or column).@deprecated as of VTK 5.2. Using this
        method for field_data having arrays that are not subclasses of
        DataArray may yield unexpected results.
        """
        ret = self._wrap_call(self._vtk_obj.GetComponent, *args)
        return ret

    def set_component(self, *args):
        """
        V.set_component(int, int, float)
        C++: void SetComponent(const IdType i, const int j,
            const double c)
        Set the component value at the ith tuple (or row) and jth
        component (or column).  Range checking is not performed, so set
        the object up properly before invoking.@deprecated as of VTK 5.2.
        Using this method for field_data having arrays that are not
        subclasses of DataArray may yield unexpected results.
        """
        ret = self._wrap_call(self._vtk_obj.SetComponent, *args)
        return ret

    number_of_tuples = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of tuples for each data array in the field. This
        method should not be used if the instance is from a subclass of
        FieldData (vtk_point_data or CellData). This is because in
        those cases, the attribute data is stored with the other fields
        and will cause the method to behave in an unexpected way.
        """
    )
    def _number_of_tuples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTuples,
                        self.number_of_tuples)

    def get_abstract_array(self, *args):
        """
        V.get_abstract_array(int) -> AbstractArray
        C++: AbstractArray *GetAbstractArray(int i)
        V.get_abstract_array(string, int) -> AbstractArray
        C++: AbstractArray *GetAbstractArray(const char *arrayName,
            int &index)
        V.get_abstract_array(string) -> AbstractArray
        C++: AbstractArray *GetAbstractArray(const char *arrayName)
        Returns the ith array in the field. Unlike get_array(), this
        method returns a AbstractArray. A NULL is returned only if the
        index i is out of range.
        """
        ret = self._wrap_call(self._vtk_obj.GetAbstractArray, *args)
        return wrap_vtk(ret)

    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the memory in kilobytes consumed by this field data. Used
        to support streaming and reading/writing data. The value returned
        is guaranteed to be greater than or equal to the memory required
        to actually represent the data represented by this object.
        """
    )

    def get_array(self, *args):
        """
        V.get_array(int) -> DataArray
        C++: DataArray *GetArray(int i)
        V.get_array(string, int) -> DataArray
        C++: DataArray *GetArray(const char *arrayName, int &index)
        V.get_array(string) -> DataArray
        C++: DataArray *GetArray(const char *arrayName)
        Return the ith array in the field. A NULL is returned if the
        index i is out of range. A NULL is returned if the array at the
        given index is not a DataArray.
        """
        ret = self._wrap_call(self._vtk_obj.GetArray, *args)
        return wrap_vtk(ret)

    def get_array_containing_component(self, *args):
        """
        V.get_array_containing_component(int, int) -> int
        C++: int GetArrayContainingComponent(int i, int &arrayComp)
        Return the array containing the ith component of the field. The
        return value is an integer number n 0<=n<this->_number_of_arrays.
        Also, an integer value is returned indicating the component in
        the array is returned. Method returns -1 if specified component
        is not in the field.
        """
        ret = self._wrap_call(self._vtk_obj.GetArrayContainingComponent, *args)
        return ret

    def get_array_name(self, *args):
        """
        V.get_array_name(int) -> string
        C++: const char *GetArrayName(int i)
        Get the name of ith array. Note that this is equivalent to:
        get_abstract_array(i)->_get_name() if ith array pointer is not NULL
        """
        ret = self._wrap_call(self._vtk_obj.GetArrayName, *args)
        return ret

    def get_field(self, *args):
        """
        V.get_field(IdList, FieldData)
        C++: void GetField(IdList *ptId, FieldData *f)
        Get a field from a list of ids. Supplied field f should have same
        types and number of data arrays as this one (i.e., like
        copy_structure() creates).  This method should not be used if the
        instance is from a subclass of FieldData (vtk_point_data or
        CellData).  This is because in those cases, the attribute data
        is stored with the other fields and will cause the method to
        behave in an unexpected way.
        """
        my_args = deref_array(args, [('vtkIdList', 'vtkFieldData')])
        ret = self._wrap_call(self._vtk_obj.GetField, *my_args)
        return ret

    def _get_number_of_arrays(self):
        return self._vtk_obj.GetNumberOfArrays()
    number_of_arrays = traits.Property(_get_number_of_arrays, help=\
        """
        Get the number of arrays of data available. This does not include
        NULL array pointers therefore after fd->_allocate_array(n); n_arrays
        = get_number_of_arrays() n_arrays is not necessarily equal to n.
        """
    )

    def _get_number_of_components(self):
        return self._vtk_obj.GetNumberOfComponents()
    number_of_components = traits.Property(_get_number_of_components, help=\
        """
        Get the number of components in the field. This is determined by
        adding up the components in each non-NULL array. This method
        should not be used if the instance is from a subclass of
        FieldData (vtk_point_data or CellData). This is because in
        those cases, the attribute data is stored with the other fields
        and will cause the method to behave in an unexpected way.
        """
    )

    def add_array(self, *args):
        """
        V.add_array(AbstractArray) -> int
        C++: int AddArray(AbstractArray *array)
        Add an array to the array list. If an array with the same name
        already exists - then the added array will replace it.
        """
        my_args = deref_array(args, [['vtkAbstractArray']])
        ret = self._wrap_call(self._vtk_obj.AddArray, *my_args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: int Allocate(const IdType sz, const IdType ext=1000)
        Allocate data for each array. Note that ext is no longer used.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def allocate_arrays(self, *args):
        """
        V.allocate_arrays(int)
        C++: void AllocateArrays(int num)
        allocate_of_arrays actually sets the number of AbstractArray
        pointers in the FieldData object, not the number of used
        pointers (arrays). Adding more arrays will cause the object to
        dynamically adjust the number of pointers if it needs to extend.
        Although allocate_arrays can be used if the number of arrays which
        will be added is known, it can be omitted with a small
        computation cost.
        """
        ret = self._wrap_call(self._vtk_obj.AllocateArrays, *args)
        return ret

    def copy_all_off(self, *args):
        """
        V.copy_all_off(int)
        C++: virtual void CopyAllOff(int unused=0)
        Turn off copying of all data. During the copying/passing, the
        following rules are followed for each array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._wrap_call(self._vtk_obj.CopyAllOff, *args)
        return ret

    def copy_all_on(self, *args):
        """
        V.copy_all_on(int)
        C++: virtual void CopyAllOn(int unused=0)
        Turn on copying of all data. During the copying/passing, the
        following rules are followed for each array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._wrap_call(self._vtk_obj.CopyAllOn, *args)
        return ret

    def copy_field_off(self, *args):
        """
        V.copy_field_off(string)
        C++: void CopyFieldOff(const char *name)
        Turn on/off the copying of the field specified by name. During
        the copying/passing, the following rules are followed for each
        array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._wrap_call(self._vtk_obj.CopyFieldOff, *args)
        return ret

    def copy_field_on(self, *args):
        """
        V.copy_field_on(string)
        C++: void CopyFieldOn(const char *name)
        Turn on/off the copying of the field specified by name. During
        the copying/passing, the following rules are followed for each
        array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._wrap_call(self._vtk_obj.CopyFieldOn, *args)
        return ret

    def copy_structure(self, *args):
        """
        V.copy_structure(FieldData)
        C++: void CopyStructure(FieldData *)
        Copy data array structure from a given field.  The same arrays
        will exist with the same types, but will contain nothing in the
        copy.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyStructure, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(FieldData)
        C++: virtual void DeepCopy(FieldData *da)
        Copy a field by creating new data arrays (i.e., duplicate
        storage).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def has_array(self, *args):
        """
        V.has_array(string) -> int
        C++: int HasArray(const char *name)
        Return 1 if an array with the given name could be found. 0
        otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.HasArray, *args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Release all data but do not delete object. Also, clear the copy
        flags.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def insert_component(self, *args):
        """
        V.insert_component(int, int, float)
        C++: void InsertComponent(const IdType i, const int j,
            const double c)
        Insert the component value at the ith tuple (or row) and jth
        component (or column).  Range checking is performed and memory
        allocated as necessary o hold data.@deprecated as of VTK 5.2.
        Using this method for field_data having arrays that are not
        subclasses of DataArray may yield unexpected results.
        """
        ret = self._wrap_call(self._vtk_obj.InsertComponent, *args)
        return ret

    def insert_next_tuple(self, *args):
        """
        V.insert_next_tuple(int, FieldData) -> int
        C++: IdType InsertNextTuple(const IdType j,
            FieldData *source)
        Insert the jth tuple in source field data  at the end of the
        tuple matrix. Range checking is performed and memory is allocated
        as necessary.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertNextTuple, *my_args)
        return ret

    def insert_tuple(self, *args):
        """
        V.insert_tuple(int, int, FieldData)
        C++: void InsertTuple(const IdType i, const IdType j,
            FieldData *source)
        Insert the jth tuple in source field data at the ith location.
        Range checking is performed and memory allocates as necessary.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertTuple, *my_args)
        return ret

    def pass_data(self, *args):
        """
        V.pass_data(FieldData)
        C++: virtual void PassData(FieldData *fd)
        Pass entire arrays of input data through to output. Obey the
        "copy" flags.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PassData, *my_args)
        return ret

    def remove_array(self, *args):
        """
        V.remove_array(string)
        C++: virtual void RemoveArray(const char *name)
        Remove an array (with the given name) from the list of arrays.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveArray, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Resets each data array in the field (Reset() does not release
        memory but it makes the arrays look like they are empty.)
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def set_tuple(self, *args):
        """
        V.set_tuple(int, int, FieldData)
        C++: void SetTuple(const IdType i, const IdType j,
            FieldData *source)
        Set the jth tuple in source field data at the ith location. Set
        operations mean that no range checking is performed, so they're
        faster.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTuple, *my_args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(FieldData)
        C++: virtual void ShallowCopy(FieldData *da)
        Copy a field by reference counting the data arrays.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def squeeze(self):
        """
        V.squeeze()
        C++: void Squeeze()
        Squeezes each data array in the field (Squeeze() reclaims unused
        memory.)
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('number_of_tuples',
    'GetNumberOfTuples'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_tuples'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FieldData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FieldData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_tuples']),
            title='Edit FieldData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FieldData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

