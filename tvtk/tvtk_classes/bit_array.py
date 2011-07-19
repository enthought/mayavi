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


class BitArray(DataArray):
    """
    BitArray - dynamic, self-adjusting array of bits
    
    Superclass: DataArray
    
    BitArray is an array of bits (0/1 data value). The array is packed
    so that each byte stores eight bits. BitArray provides methods for
    insertion and retrieval of bits, and will automatically resize itself
    to hold new data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBitArray, obj, update, **traits)
    
    def get_value(self, *args):
        """
        V.get_value(int) -> int
        C++: int GetValue(IdType id)
        Get the data at a particular index.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, int)
        C++: void SetValue(IdType id, int value)
        Set the data at a particular index. Does not do range checking.
        Make sure you use the method set_number_of_values() before inserting
        data.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    def get_tuple(self, *args):
        """
        V.get_tuple(int) -> (float, ...)
        C++: double *GetTuple(IdType i)
        V.get_tuple(int, [float, ...])
        C++: void GetTuple(IdType i, double *tuple)
        Get a pointer to a tuple at the ith location. This is a dangerous
        method (it is not thread safe since a pointer is returned).
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple, *args)
        return ret

    def set_tuple(self, *args):
        """
        V.set_tuple(int, int, AbstractArray)
        C++: virtual void SetTuple(IdType i, IdType j,
            AbstractArray *source)
        V.set_tuple(int, (float, ...))
        C++: void SetTuple(IdType i, const double *tuple)
        Set the tuple at the ith location using the jth tuple in the
        source array. This method assumes that the two arrays have the
        same type and structure. Note that range checking and memory
        allocation is not performed; use in conjunction with
        set_number_of_tuples() to allocate space.
        """
        my_args = deref_array(args, [('int', 'int', 'vtkAbstractArray'), ('int', 'tuple')])
        ret = self._wrap_call(self._vtk_obj.SetTuple, *my_args)
        return ret

    def insert_next_value(self, *args):
        """
        V.insert_next_value(int) -> int
        C++: IdType InsertNextValue(int i)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextValue, *args)
        return ret

    def insert_value(self, *args):
        """
        V.insert_value(int, int)
        C++: void InsertValue(IdType id, int i)
        Insets values and checks to make sure there is enough memory
        """
        ret = self._wrap_call(self._vtk_obj.InsertValue, *args)
        return ret

    def set_number_of_values(self, *args):
        """
        V.set_number_of_values(int)
        C++: void SetNumberOfValues(IdType number)
        Fast method based setting of values without memory checks. First
        use set_number_of_values then use set_value to actually set them.
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
            return super(BitArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BitArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['component_name', 'name',
            'number_of_components', 'number_of_tuples']),
            title='Edit BitArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BitArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

