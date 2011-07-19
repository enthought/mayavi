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


class Array(Object):
    """
    Array - Abstract interface for N-dimensional arrays.
    
    Superclass: Object
    
    Array is the root of a hierarchy of arrays that can be used to
    store data with any number of dimensions.  It provides an abstract
    interface for retrieving and setting array attributes that are
    independent of the type of values stored in the array - such as the
    number of dimensions, extents along each dimension, and number of
    values stored in the array.
    
    To get and set array values, the TypedArray template class derives
    from Array and provides type-specific methods for retrieval and
    update.
    
    Two concrete derivatives of TypedArray are provided at the moment:
    DenseArray and SparseArray, which provide dense and sparse
    storage for arbitrary-dimension data, respectively.  Toolkit users
    can create their own concrete derivatives that implement alternative
    storage strategies, such as compressed-sparse-row, etc.  You could
    also create an array that provided read-only access to 'virtual'
    data, such as an array that returned a Fibonacci sequence, etc.
    
    See Also:
    
    TypedArray, DenseArray, SparseArray
    
    Thanks:
    
    Developed by Timothy M. Shead (tshead@sandia.gov) at  Sandia National
    Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArray, obj, update, **traits)
    
    def get_dimension_label(self, *args):
        """
        V.get_dimension_label(int) -> string
        C++: StdString GetDimensionLabel(DimensionT i)
        Returns the label for the i-th array dimension.
        """
        ret = self._wrap_call(self._vtk_obj.GetDimensionLabel, *args)
        return ret

    def set_dimension_label(self, *args):
        """
        V.set_dimension_label(int, string)
        C++: void SetDimensionLabel(DimensionT i,
            const StdString &label)
        Sets the label for the i-th array dimension.
        """
        ret = self._wrap_call(self._vtk_obj.SetDimensionLabel, *args)
        return ret

    name = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Sets the array name.
        """
    )
    def _name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetName,
                        self.name)

    def get_variant_value(self, *args):
        """
        V.get_variant_value(int) -> Variant
        C++: Variant GetVariantValue(CoordinateT i)
        V.get_variant_value(int, int) -> Variant
        C++: Variant GetVariantValue(CoordinateT i, CoordinateT j)
        V.get_variant_value(int, int, int) -> Variant
        C++: Variant GetVariantValue(CoordinateT i, CoordinateT j,
            CoordinateT k)
        V.get_variant_value(ArrayCoordinates) -> Variant
        C++: virtual Variant GetVariantValue(
            const ArrayCoordinates &coordinates)
        Returns the value stored in the array at the given coordinates.
        Note that the number of dimensions in the supplied coordinates
        must match the number of dimensions in the array.
        """
        my_args = deref_array(args, [['int'], ('int', 'int'), ('int', 'int', 'int'), ['vtkArrayCoordinates']])
        ret = self._wrap_call(self._vtk_obj.GetVariantValue, *my_args)
        return wrap_vtk(ret)

    def set_variant_value(self, *args):
        """
        V.set_variant_value(int, Variant)
        C++: void SetVariantValue(CoordinateT i, const Variant &value)
        V.set_variant_value(int, int, Variant)
        C++: void SetVariantValue(CoordinateT i, CoordinateT j,
            const Variant &value)
        V.set_variant_value(int, int, int, Variant)
        C++: void SetVariantValue(CoordinateT i, CoordinateT j,
            CoordinateT k, const Variant &value)
        V.set_variant_value(ArrayCoordinates, Variant)
        C++: virtual void SetVariantValue(
            const ArrayCoordinates &coordinates,
            const Variant &value)
        Overwrites the value stored in the array at the given
        coordinates. Note that the number of dimensions in the supplied
        coordinates must match the number of dimensions in the array.
        """
        my_args = deref_array(args, [('int', 'vtkVariant'), ('int', 'int', 'vtkVariant'), ('int', 'int', 'int', 'vtkVariant'), ('vtkArrayCoordinates', 'vtkVariant')])
        ret = self._wrap_call(self._vtk_obj.SetVariantValue, *my_args)
        return ret

    def get_variant_value_n(self, *args):
        """
        V.get_variant_value_n(int) -> Variant
        C++: virtual Variant GetVariantValueN(const SizeT n)
        Returns the n-th value stored in the array, where n is in the
        range [0, get_non_null_size()).  This is useful for efficiently
        visiting every value in the array.  Note that the order in which
        values are visited is undefined, but is guaranteed to match the
        order used by Array::GetCoordinatesN().
        """
        ret = self._wrap_call(self._vtk_obj.GetVariantValueN, *args)
        return wrap_vtk(ret)

    def set_variant_value_n(self, *args):
        """
        V.set_variant_value_n(int, Variant)
        C++: virtual void SetVariantValueN(const SizeT n,
            const Variant &value)
        Overwrites the n-th value stored in the array, where n is in the
        range [0, get_non_null_size()).  This is useful for efficiently
        visiting every value in the array.  Note that the order in which
        values are visited is undefined, but is guaranteed to match the
        order used by Array::GetCoordinatesN().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVariantValueN, *my_args)
        return ret

    def get_coordinates_n(self, *args):
        """
        V.get_coordinates_n(int, ArrayCoordinates)
        C++: virtual void GetCoordinatesN(const SizeT n,
            ArrayCoordinates &coordinates)
        Returns the coordinates of the n-th value in the array, where n
        is in the range [0, get_non_null_size()).  Note that the order in
        which coordinates are visited is undefined, but is guaranteed to
        match the order in which values are visited using
        TypedArray::GetValueN() and TypedArray::SetValueN().
        """
        my_args = deref_array(args, [('int', 'vtkArrayCoordinates')])
        ret = self._wrap_call(self._vtk_obj.GetCoordinatesN, *my_args)
        return ret

    def _get_dimensions(self):
        return self._vtk_obj.GetDimensions()
    dimensions = traits.Property(_get_dimensions, help=\
        """
        Returns the number of dimensions stored in the array.  Note that
        this is the same as calling get_extents()._get_dimensions().
        """
    )

    def get_extent(self, *args):
        """
        V.get_extent(int) -> ArrayRange
        C++: const ArrayRange GetExtent(DimensionT dimension)
        Returns the extent (valid coordinate range) along the given
        dimension.
        """
        ret = self._wrap_call(self._vtk_obj.GetExtent, *args)
        return wrap_vtk(ret)

    def _get_extents(self):
        return wrap_vtk(self._vtk_obj.GetExtents())
    extents = traits.Property(_get_extents, help=\
        """
        Returns the extents (the number of dimensions and size along each
        dimension) of the array.
        """
    )

    def _get_non_null_size(self):
        return self._vtk_obj.GetNonNullSize()
    non_null_size = traits.Property(_get_non_null_size, help=\
        """
        Returns the number of non-null values stored in the array.  Note
        that this value will equal get_size() for dense arrays, and will
        be less-than-or-equal to get_size() for sparse arrays.
        """
    )

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        Returns the number of values stored in the array.  Note that this
        is the same as calling get_extents()._get_size(), and represents the
        maximum number of values that could ever be stored using the
        current extents.  This is equal to the number of values stored in
        a  dense array, but may be larger than the number of values
        stored in a sparse array.
        """
    )

    def copy_value(self, *args):
        """
        V.copy_value(Array, ArrayCoordinates, ArrayCoordinates)
        C++: virtual void CopyValue(Array *source,
            const ArrayCoordinates &source_coordinates,
            const ArrayCoordinates &target_coordinates)
        V.copy_value(Array, int, ArrayCoordinates)
        C++: virtual void CopyValue(Array *source,
            const SizeT source_index,
            const ArrayCoordinates &target_coordinates)
        V.copy_value(Array, ArrayCoordinates, int)
        C++: virtual void CopyValue(Array *source,
            const ArrayCoordinates &source_coordinates,
            const SizeT target_index)
        Overwrites a value with a value retrieved from another array. 
        Both arrays must store the same data types.
        """
        my_args = deref_array(args, [('vtkArray', 'vtkArrayCoordinates', 'vtkArrayCoordinates'), ('vtkArray', 'int', 'vtkArrayCoordinates'), ('vtkArray', 'vtkArrayCoordinates', 'int')])
        ret = self._wrap_call(self._vtk_obj.CopyValue, *my_args)
        return ret

    def create_array(self, *args):
        """
        V.create_array(int, int) -> Array
        C++: static Array *CreateArray(int StorageType, int ValueType)
        Creates a new array where storage_type is one of Array::DENSE
        or Array::SPARSE, and value_type is one of VTK_CHAR,
        VTK_UNSIGNED_CHAR, VTK_SHORT, VTK_UNSIGNED_SHORT,  VTK_INT,
        VTK_UNSIGNED_INT, VTK_LONG, VTK_UNSIGNED_LONG, VTK_DOUBLE,
        VTK_ID_TYPE, or VTK_STRING.  The caller is responsible for the
        lifetime of the returned object.
        """
        ret = self._wrap_call(self._vtk_obj.CreateArray, *args)
        return wrap_vtk(ret)

    def deep_copy(self):
        """
        V.deep_copy() -> Array
        C++: virtual Array *DeepCopy()
        Returns a new array that is a deep copy of this array.
        """
        ret = wrap_vtk(self._vtk_obj.DeepCopy())
        return ret
        

    def is_dense(self):
        """
        V.is_dense() -> bool
        C++: virtual bool IsDense()
        Returns true iff the underlying array storage is "dense", i.e.
        that get_size() and get_non_null_size() will always return the same
        value. If not, the array is "sparse".
        """
        ret = self._vtk_obj.IsDense()
        return ret
        

    def resize(self, *args):
        """
        V.resize(int)
        C++: void Resize(const CoordinateT i)
        V.resize(int, int)
        C++: void Resize(const CoordinateT i, const CoordinateT j)
        V.resize(int, int, int)
        C++: void Resize(const CoordinateT i, const CoordinateT j,
            const CoordinateT k)
        V.resize(ArrayRange)
        C++: void Resize(const ArrayRange &i)
        V.resize(ArrayRange, ArrayRange)
        C++: void Resize(const ArrayRange &i, const ArrayRange &j)
        V.resize(ArrayRange, ArrayRange, ArrayRange)
        C++: void Resize(const ArrayRange &i, const ArrayRange &j,
            const ArrayRange &k)
        V.resize(ArrayExtents)
        C++: void Resize(const ArrayExtents &extents)
        Resizes the array to the given extents (number of dimensions and
        size of each dimension).  Note that concrete implementations of
        Array may place constraints on the the extents that they will
        store, so you cannot assume that get_extents() will always return
        the same value passed to Resize().
        
        The contents of the array are undefined after calling Resize() -
        you should initialize its contents accordingly.  In particular,
        dimension-labels will be undefined, dense array values will be
        undefined, and sparse arrays will be empty.
        """
        my_args = deref_array(args, [['int'], ('int', 'int'), ('int', 'int', 'int'), ['vtkArrayRange'], ('vtkArrayRange', 'vtkArrayRange'), ('vtkArrayRange', 'vtkArrayRange', 'vtkArrayRange'), ['vtkArrayExtents']])
        ret = self._wrap_call(self._vtk_obj.Resize, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('dimension_label', 'GetDimensionLabel'),
    ('name', 'GetName'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'),
    ('variant_value', 'GetVariantValue'), ('variant_value_n',
    'GetVariantValueN'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'dimension_label', 'name',
    'variant_value', 'variant_value_n'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Array, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Array properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['dimension_label', 'name', 'variant_value',
            'variant_value_n']),
            title='Edit Array properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Array properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

