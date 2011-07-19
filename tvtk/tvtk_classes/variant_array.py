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

from tvtk.tvtk_classes.abstract_array import AbstractArray


class VariantArray(AbstractArray):
    """
    VariantArray - An array holding Variants.
    
    Superclass: AbstractArray
    
    Thanks:
    
    Thanks to Patricia Crossno, Ken Moreland, Andrew Wilson and Brian
    Wylie from Sandia National Laboratories for their help in developing
    this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVariantArray, obj, update, **traits)
    
    number_of_values = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the number of values for this object to hold. Does an
        allocation as well as setting the max_id ivar. Used in conjunction
        with set_value() method for fast insertion.
        """
    )
    def _number_of_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfValues,
                        self.number_of_values)

    def get_value(self, *args):
        """
        V.get_value(int) -> Variant
        C++: Variant &GetValue(IdType id)
        Get the data at a particular index.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return wrap_vtk(ret)

    def set_value(self, *args):
        """
        V.set_value(int, Variant)
        C++: void SetValue(IdType id, Variant value)
        Set the data at a particular index. Does not do range checking.
        Make sure you use the method set_number_of_values() before inserting
        data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetValue, *my_args)
        return ret

    def data_element_changed(self, *args):
        """
        V.data_element_changed(int)
        C++: virtual void DataElementChanged(IdType id)
        Tell the array explicitly that a single data element has changed.
        Like data_changed(), then is only necessary when you modify the
        array contents without using the array's API.
        """
        ret = self._wrap_call(self._vtk_obj.DataElementChanged, *args)
        return ret

    def insert_next_value(self, *args):
        """
        V.insert_next_value(Variant) -> int
        C++: IdType InsertNextValue(Variant value)
        Expand the array by one and set the value at that location.
        Return the array index of the inserted value.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertNextValue, *my_args)
        return ret

    def insert_value(self, *args):
        """
        V.insert_value(int, Variant)
        C++: void InsertValue(IdType id, Variant value)
        If id < get_number_of_values(), overwrite the array at that index.
        If id >= get_number_of_values(), expand the array size to id+1 and
        set the final value to the specified value.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertValue, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('name', 'GetName'), ('number_of_values',
    'GetNumberOfValues'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'),
    ('number_of_tuples', 'GetNumberOfTuples'), ('number_of_components',
    'GetNumberOfComponents'), ('component_name', 'GetComponentName'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'component_name', 'name',
    'number_of_components', 'number_of_tuples', 'number_of_values'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VariantArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VariantArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['component_name', 'name',
            'number_of_components', 'number_of_tuples', 'number_of_values']),
            title='Edit VariantArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VariantArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

