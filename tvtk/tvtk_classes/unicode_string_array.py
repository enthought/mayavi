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


class UnicodeStringArray(AbstractArray):
    """
    UnicodeStringArray - Subclass of AbstractArray that holds
    UnicodeStrings
    
    Superclass: AbstractArray
    
    Thanks:
    
    Developed by Timothy M. Shead (tshead@sandia.gov) at Sandia National
    Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnicodeStringArray, obj, update, **traits)
    
    utf8_value = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _utf8_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUTF8Value,
                        self.utf8_value)

    def get_value(self, *args):
        """
        V.get_value(int) -> unicode
        C++: UnicodeString &GetValue(IdType i)"""
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, unicode)
        C++: void SetValue(IdType i, const UnicodeString &)"""
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    def get_variant_value(self, *args):
        """
        V.get_variant_value(int) -> Variant
        C++: virtual Variant GetVariantValue(IdType idx)"""
        ret = self._wrap_call(self._vtk_obj.GetVariantValue, *args)
        return wrap_vtk(ret)

    def set_variant_value(self, *args):
        """
        V.set_variant_value(int, Variant)
        C++: virtual void SetVariantValue(IdType idx, Variant value)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVariantValue, *my_args)
        return ret

    def insert_next_utf8_value(self, *args):
        """
        V.insert_next_utf8_value(string)
        C++: void InsertNextUTF8Value(const char *)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextUTF8Value, *args)
        return ret

    def insert_next_value(self, *args):
        """
        V.insert_next_value(unicode) -> int
        C++: IdType InsertNextValue(const UnicodeString &)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextValue, *args)
        return ret

    def insert_value(self, *args):
        """
        V.insert_value(int, unicode)
        C++: void InsertValue(IdType idx, const UnicodeString &)"""
        ret = self._wrap_call(self._vtk_obj.InsertValue, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('name', 'GetName'), ('utf8_value',
    'GetUTF8Value'), ('reference_count', 'GetReferenceCount'),
    ('number_of_tuples', 'GetNumberOfTuples'), ('number_of_components',
    'GetNumberOfComponents'), ('component_name', 'GetComponentName'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'component_name', 'name',
    'number_of_components', 'number_of_tuples', 'utf8_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnicodeStringArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UnicodeStringArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['component_name', 'name',
            'number_of_components', 'number_of_tuples', 'utf8_value']),
            title='Edit UnicodeStringArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnicodeStringArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

