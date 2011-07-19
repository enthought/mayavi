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


class AbstractArray(Object):
    """
    AbstractArray - Abstract superclass for all arrays
    
    Superclass: Object
    
    AbstractArray is an abstract superclass for data array objects.
    This class defines an API that all subclasses must support.  The data
    type must be assignable and copy-constructible, but no other
    assumptions about its type are made.  Most of the subclasses of this
    array deal with numeric data either as scalars or tuples of scalars. 
    A program can use the is_numeric() method to check whether an instance
    of AbstractArray contains numbers.  It is also possible to test
    for this by attempting to safe_down_cast an array to an instance of
    DataArray, although this assumes that all numeric arrays will
    always be descended from DataArray.
    
    Every array has a character-string name. The naming of the array
    occurs automatically when it is instantiated, but you are free to
    change this name using the set_name() method.  (The array name is used
    for data manipulation.)
    
    See Also:
    
    DataArray StringArray CellArray
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractArray, obj, update, **traits)
    
    component_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name for a component. Must be >= 1.
        """
    )
    def _component_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentName,
                        self.component_name)

    number_of_components = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the dimention (n) of the components. Must be >= 1. Make
        sure that this is set before allocation.
        """
    )
    def _number_of_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfComponents,
                        self.number_of_components)

    name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/get array's name
        """
    )
    def _name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetName,
                        self.name)

    def get_variant_value(self, *args):
        """
        V.get_variant_value(int) -> Variant
        C++: virtual Variant GetVariantValue(IdType idx)
        Retrieve value from the array as a variant.
        """
        ret = self._wrap_call(self._vtk_obj.GetVariantValue, *args)
        return wrap_vtk(ret)

    def set_variant_value(self, *args):
        """
        V.set_variant_value(int, Variant)
        C++: virtual void SetVariantValue(IdType idx, Variant value)
        Set a value in the array from a variant.  This method does NOT do
        bounds checking.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVariantValue, *my_args)
        return ret

    number_of_tuples = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of tuples (a component group) in the array. Note
        that this may allocate space depending on the number of
        components. Also note that if allocation is performed no copy is
        performed so existing data will be lost (if data conservation is
        sought, one may use the Resize method instead).
        """
    )
    def _number_of_tuples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTuples,
                        self.number_of_tuples)

    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the memory in kilobytes consumed by this data array. Used
        to support streaming and reading/writing data. The value returned
        is guaranteed to be greater than or equal to the memory required
        to actually represent the data represented by this object. The
        information returned is valid only after the pipeline has been
        updated.
        """
    )

    def _get_data_size(self):
        return self._vtk_obj.GetDataSize()
    data_size = traits.Property(_get_data_size, help=\
        """
        Returns the size of the data in data_type_size units. Thus, the
        number of bytes for the data can be computed by get_data_size() *
        get_data_type_size(). Non-contiguous or variable- size arrays need
        to override this method.
        """
    )

    def _get_data_type(self):
        return self._vtk_obj.GetDataType()
    data_type = traits.Property(_get_data_type, help=\
        """
        Return the underlying data type. An integer indicating data type
        is returned as specified in SetGet.h.
        """
    )

    def _get_data_type_as_string(self):
        return self._vtk_obj.GetDataTypeAsString()
    data_type_as_string = traits.Property(_get_data_type_as_string, help=\
        """
        Get the name of a data type as a string.
        """
    )

    def _get_data_type_size(self):
        return self._vtk_obj.GetDataTypeSize()
    data_type_size = traits.Property(_get_data_type_size, help=\
        """
        Return the size of the underlying data type.  For a bit, 0 is
        returned.  For string 0 is returned. Arrays with variable length
        components return 0.
        """
    )

    def _get_element_component_size(self):
        return self._vtk_obj.GetElementComponentSize()
    element_component_size = traits.Property(_get_element_component_size, help=\
        """
        Return the size, in bytes, of the lowest-level element of an
        array.  For DataArray and subclasses this is the size of the
        data type.  For StringArray, this is
        sizeof(vtk_std_string::value_type), which winds up being
        sizeof(char).
        """
    )

    def _get_information(self):
        return wrap_vtk(self._vtk_obj.GetInformation())
    information = traits.Property(_get_information, help=\
        """
        Get an information object that can be used to annotate the array.
        This will always return an instance of Information, if one is
        not currently associated with the array it will be created.
        """
    )

    def _get_max_id(self):
        return self._vtk_obj.GetMaxId()
    max_id = traits.Property(_get_max_id, help=\
        """
        What is the maximum id currently in the array.
        """
    )

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        Return the size of the data.
        """
    )

    def get_tuples(self, *args):
        """
        V.get_tuples(IdList, AbstractArray)
        C++: virtual void GetTuples(IdList *ptIds,
            AbstractArray *output)
        V.get_tuples(int, int, AbstractArray)
        C++: virtual void GetTuples(IdType p1, IdType p2,
            AbstractArray *output)
        Given a list of point ids, return an array of tuples. You must
        insure that the output array has been previously allocated with
        enough space to hold the data.
        """
        my_args = deref_array(args, [('vtkIdList', 'vtkAbstractArray'), ('int', 'int', 'vtkAbstractArray')])
        ret = self._wrap_call(self._vtk_obj.GetTuples, *my_args)
        return ret

    def get_void_pointer(self, *args):
        """
        V.get_void_pointer(int) ->
        C++: virtual void *GetVoidPointer(IdType id)
        Return a void pointer. For image pipeline interface and other
        special pointer manipulation.
        """
        ret = self._wrap_call(self._vtk_obj.GetVoidPointer, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: virtual int Allocate(IdType sz, IdType ext=1000)
        Allocate memory for this array. Delete old storage only if
        necessary. Note that ext is no longer used.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def clear_lookup(self):
        """
        V.clear_lookup()
        C++: virtual void ClearLookup()
        Delete the associated fast lookup data structure on this array,
        if it exists.  The lookup will be rebuilt on the next call to a
        lookup function.
        """
        ret = self._vtk_obj.ClearLookup()
        return ret
        

    def copy_component_names(self, *args):
        """
        V.copy_component_names(AbstractArray) -> int
        C++: int CopyComponentNames(AbstractArray *da)
        Copies the component names from the inputed array to the current
        array make sure that the current array has the same number of
        components as the input array
        """
        my_args = deref_array(args, [['vtkAbstractArray']])
        ret = self._wrap_call(self._vtk_obj.CopyComponentNames, *my_args)
        return ret

    def copy_information(self, *args):
        """
        V.copy_information(Information, int) -> int
        C++: virtual int CopyInformation(Information *infoFrom,
            int deep=1)
        Copy information instance. Arrays use information objects in a
        variety of ways. It is important to have flexibility in this
        regard because certain keys should not be coppied, while others
        must be.
        
        NOTE: Subclasses must always call their superclass's
        copy_information method, so that all classes in the hierarchy get
        a chance to remove keys they do not wish to be coppied. The
        subclass will not need to explicilty copy the keys as it's
        handled here.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyInformation, *my_args)
        return ret

    def create_array(self, *args):
        """
        V.create_array(int) -> AbstractArray
        C++: static AbstractArray *CreateArray(int dataType)
        Creates an array for data_type where data_type is one of VTK_BIT,
        VTK_CHAR, VTK_UNSIGNED_CHAR, VTK_SHORT, VTK_UNSIGNED_SHORT,
        VTK_INT, VTK_UNSIGNED_INT, VTK_LONG, VTK_UNSIGNED_LONG,
        VTK_DOUBLE, VTK_DOUBLE, VTK_ID_TYPE, VTK_STRING. Note that the
        data array returned has to be deleted by the user.
        """
        ret = self._wrap_call(self._vtk_obj.CreateArray, *args)
        return wrap_vtk(ret)

    def data_changed(self):
        """
        V.data_changed()
        C++: virtual void DataChanged()
        Tell the array explicitly that the data has changed. This is only
        necessary to call when you modify the array contents without
        using the array's API (i.e. you retrieve a pointer to the data
        and modify the array contents).  You need to call this so that
        the fast lookup will know to rebuild itself.  Otherwise, the
        lookup functions will give incorrect results.
        """
        ret = self._vtk_obj.DataChanged()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(AbstractArray)
        C++: virtual void DeepCopy(AbstractArray *da)
        Deep copy of data. Implementation left to subclasses, which
        should support as many type conversions as possible given the
        data type.
        
        Subclasses should call AbstractArray::DeepCopy() so that the
        information object (if one exists) is copied from da.
        """
        my_args = deref_array(args, [['vtkAbstractArray']])
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def export_to_void_pointer(self):
        """
        V.export_to_void_pointer()
        C++: virtual void ExportToVoidPointer(void *out_ptr)
        This method copies the array data to the void pointer specified
        by the user.  It is up to the user to allocate enough memory for
        the void pointer.
        """
        ret = self._vtk_obj.ExportToVoidPointer()
        return ret
        

    def GUI_HIDE(self):
        """
        V.gui__hide() -> InformationIntegerKey
        C++: static InformationIntegerKey *GUI_HIDE()
        This key is a hint to end user interface that this array is
        internal and should not be shown to the end user.
        """
        ret = wrap_vtk(self._vtk_obj.GUI_HIDE())
        return ret
        

    def has_a_component_name(self):
        """
        V.has_a_component_name() -> bool
        C++: bool HasAComponentName()
        Returns if any component has had a name assigned
        """
        ret = self._vtk_obj.HasAComponentName()
        return ret
        

    def has_information(self):
        """
        V.has_information() -> bool
        C++: bool HasInformation()
        Inquire if this array has an instance of Information already
        associated with it.
        """
        ret = self._vtk_obj.HasInformation()
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Release storage and reset array to initial state.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def insert_next_tuple(self, *args):
        """
        V.insert_next_tuple(int, AbstractArray) -> int
        C++: virtual IdType InsertNextTuple(IdType j,
            AbstractArray *source)
        Insert the jth tuple in the source array, at the end in this
        array. Note that memory allocation is performed as necessary to
        hold the data. Returns the location at which the data was
        inserted.
        """
        my_args = deref_array(args, [('int', 'vtkAbstractArray')])
        ret = self._wrap_call(self._vtk_obj.InsertNextTuple, *my_args)
        return ret

    def insert_tuple(self, *args):
        """
        V.insert_tuple(int, int, AbstractArray)
        C++: virtual void InsertTuple(IdType i, IdType j,
            AbstractArray *source)
        Insert the jth tuple in the source array, at ith location in this
        array. Note that memory allocation is performed as necessary to
        hold the data.
        """
        my_args = deref_array(args, [('int', 'int', 'vtkAbstractArray')])
        ret = self._wrap_call(self._vtk_obj.InsertTuple, *my_args)
        return ret

    def insert_variant_value(self, *args):
        """
        V.insert_variant_value(int, Variant)
        C++: virtual void InsertVariantValue(IdType idx,
            Variant value)
        Insert a value into the array from a variant.  This method does
        bounds checking.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertVariantValue, *my_args)
        return ret

    def interpolate_tuple(self, *args):
        """
        V.interpolate_tuple(int, int, AbstractArray, int,
            AbstractArray, float)
        C++: virtual void InterpolateTuple(IdType i, IdType id1,
            AbstractArray *source1, IdType id2,
            AbstractArray *source2, double t)"""
        my_args = deref_array(args, [('int', 'int', 'vtkAbstractArray', 'int', 'vtkAbstractArray', 'float')])
        ret = self._wrap_call(self._vtk_obj.InterpolateTuple, *my_args)
        return ret

    def is_numeric(self):
        """
        V.is_numeric() -> int
        C++: virtual int IsNumeric()
        This method is here to make backward compatibility easier.  It
        must return true if and only if an array contains numeric data.
        """
        ret = self._vtk_obj.IsNumeric()
        return ret
        

    def lookup_value(self, *args):
        """
        V.lookup_value(Variant) -> int
        C++: virtual IdType LookupValue(Variant value)
        V.lookup_value(Variant, IdList)
        C++: virtual void LookupValue(Variant value, IdList *ids)
        Return the indices where a specific value appears.
        """
        my_args = deref_array(args, [['vtkVariant'], ('vtkVariant', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.LookupValue, *my_args)
        return ret

    def new_iterator(self):
        """
        V.new_iterator() -> ArrayIterator
        C++: virtual ArrayIterator *NewIterator()
        Subclasses must override this method and provide the right kind
        of templated ArrayIteratorTemplate.
        """
        ret = wrap_vtk(self._vtk_obj.NewIterator())
        return ret
        

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reset to an empty state, without freeing any memory.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def resize(self, *args):
        """
        V.resize(int) -> int
        C++: virtual int Resize(IdType numTuples)
        Resize the array while conserving the data.  Returns 1 if
        resizing succeeded and 0 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.Resize, *args)
        return ret

    def set_tuple(self, *args):
        """
        V.set_tuple(int, int, AbstractArray)
        C++: virtual void SetTuple(IdType i, IdType j,
            AbstractArray *source)
        Set the tuple at the ith location using the jth tuple in the
        source array. This method assumes that the two arrays have the
        same type and structure. Note that range checking and memory
        allocation is not performed; use in conjunction with
        set_number_of_tuples() to allocate space.
        """
        my_args = deref_array(args, [('int', 'int', 'vtkAbstractArray')])
        ret = self._wrap_call(self._vtk_obj.SetTuple, *my_args)
        return ret

    def set_void_array(self, *args):
        """
        V.set_void_array(, int, int)
        C++: virtual void SetVoidArray(void *array, IdType size,
            int save)
        This method lets the user specify data to be held by the array. 
        The array argument is a pointer to the data.  size is the size of
        the array supplied by the user.  Set save to 1 to keep the class
        from deleting the array when it cleans up or reallocates memory.
        The class uses the actual array provided; it does not copy the
        data from the supplied array.
        """
        ret = self._wrap_call(self._vtk_obj.SetVoidArray, *args)
        return ret

    def squeeze(self):
        """
        V.squeeze()
        C++: virtual void Squeeze()
        Resize object to just fit data requirement. Reclaims extra
        memory.
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('name', 'GetName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'), ('number_of_tuples',
    'GetNumberOfTuples'), ('number_of_components',
    'GetNumberOfComponents'), ('component_name', 'GetComponentName'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'component_name', 'name',
    'number_of_components', 'number_of_tuples'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['component_name', 'name',
            'number_of_components', 'number_of_tuples']),
            title='Edit AbstractArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

