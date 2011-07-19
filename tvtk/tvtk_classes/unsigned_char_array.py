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

from tvtk.tvtk_classes.data_array import DataArray


class UnsignedCharArray(DataArray):
    """
    UnsignedCharArray - dynamic, self-adjusting array of unsigned char
    
    Superclass: DataArray
    
    UnsignedCharArray is an array of values of type unsigned char. It
    provides methods for insertion and retrieval of values and will
    automatically resize itself to hold new data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnsignedCharArray, obj, update, **traits)
    
    def get_value(self, *args):
        """
        V.get_value(int) ->
        C++: unsigned char GetValue(IdType id)
        Get the data at a particular index.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, )
        C++: void SetValue(IdType id, unsigned char value)
        Set the data at a particular index. Does not do range checking.
        Make sure you use the method set_number_of_values() before inserting
        data.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    def _get_tuple_value(self):
        return self._vtk_obj.GetTupleValue()
    def _set_tuple_value(self, arg):
        old_val = self._get_tuple_value()
        self._wrap_call(self._vtk_obj.SetTupleValue,
                        arg)
        self.trait_property_changed('tuple_value', old_val, arg)
    tuple_value = traits.Property(_get_tuple_value, _set_tuple_value, help=\
        """
        Copy the tuple value into a user-provided array.
        """
    )

    def _get_data_type_value_max(self):
        return self._vtk_obj.GetDataTypeValueMax()
    data_type_value_max = traits.Property(_get_data_type_value_max, help=\
        """
        Get the maximum data value in its native type.
        """
    )

    def _get_data_type_value_min(self):
        return self._vtk_obj.GetDataTypeValueMin()
    data_type_value_min = traits.Property(_get_data_type_value_min, help=\
        """
        Get the minimum data value in its native type.
        """
    )

    def _get_value_range(self):
        return self._vtk_obj.GetValueRange()
    value_range = traits.Property(_get_value_range, help=\
        """
        Get the range of array values for the given component in the
        native data type.
        """
    )

    def insert_next_tuple_value(self, *args):
        """
        V.insert_next_tuple_value((, ...)) -> int
        C++: IdType InsertNextTupleValue(const unsigned char *tuple)
        Insert (memory allocation performed) the tuple onto the end of
        the array.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextTupleValue, *args)
        return ret

    def insert_next_value(self):
        """
        V.insert_next_value() -> int
        C++: IdType InsertNextValue(unsigned char f)
        Insert data at the end of the array. Return its location in the
        array.
        """
        ret = self._vtk_obj.InsertNextValue()
        return ret
        

    def insert_tuple_value(self, *args):
        """
        V.insert_tuple_value(int, (, ...))
        C++: void InsertTupleValue(IdType i,
            const unsigned char *tuple)
        Insert (memory allocation performed) the tuple into the ith
        location in the array.
        """
        ret = self._wrap_call(self._vtk_obj.InsertTupleValue, *args)
        return ret

    def insert_value(self, *args):
        """
        V.insert_value(int, )
        C++: void InsertValue(IdType id, unsigned char f)
        Insert data at a specified position in the array.
        """
        ret = self._wrap_call(self._vtk_obj.InsertValue, *args)
        return ret

    def set_number_of_values(self, *args):
        """
        V.set_number_of_values(int)
        C++: void SetNumberOfValues(IdType number)
        Specify the number of values for this object to hold. Does an
        allocation as well as setting the max_id ivar. Used in conjunction
        with set_value() method for fast insertion.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfValues, *args)
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
            return super(UnsignedCharArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UnsignedCharArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['component_name', 'name',
            'number_of_components', 'number_of_tuples']),
            title='Edit UnsignedCharArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnsignedCharArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

