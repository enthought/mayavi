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


class DataArraySelection(Object):
    """
    DataArraySelection - Store on/off settings for data arrays for a
    Source.
    
    Superclass: Object
    
    DataArraySelection can be used by Source subclasses to store
    on/off settings for whether each DataArray in its input should be
    passed in the source's output.  This is primarily intended to allow
    file readers to configure what data arrays are read from the file.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataArraySelection, obj, update, **traits)
    
    def get_array_index(self, *args):
        """
        V.get_array_index(string) -> int
        C++: int GetArrayIndex(const char *name)
        Get an index of the array containing name within the enabled
        arrays
        """
        ret = self._wrap_call(self._vtk_obj.GetArrayIndex, *args)
        return ret

    def get_array_name(self, *args):
        """
        V.get_array_name(int) -> string
        C++: const char *GetArrayName(int index)
        Get the name of the array entry at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetArrayName, *args)
        return ret

    def get_array_setting(self, *args):
        """
        V.get_array_setting(string) -> int
        C++: int GetArraySetting(const char *name)
        V.get_array_setting(int) -> int
        C++: int GetArraySetting(int index)
        Get whether the array at the given index is enabled.
        """
        ret = self._wrap_call(self._vtk_obj.GetArraySetting, *args)
        return ret

    def get_enabled_array_index(self, *args):
        """
        V.get_enabled_array_index(string) -> int
        C++: int GetEnabledArrayIndex(const char *name)
        Get the index of an array with the given name among those that
        are enabled.  Returns -1 if the array is not enabled.
        """
        ret = self._wrap_call(self._vtk_obj.GetEnabledArrayIndex, *args)
        return ret

    def _get_number_of_arrays(self):
        return self._vtk_obj.GetNumberOfArrays()
    number_of_arrays = traits.Property(_get_number_of_arrays, help=\
        """
        Get the number of arrays that currently have an entry.
        """
    )

    def _get_number_of_arrays_enabled(self):
        return self._vtk_obj.GetNumberOfArraysEnabled()
    number_of_arrays_enabled = traits.Property(_get_number_of_arrays_enabled, help=\
        """
        Get the number of arrays that are enabled.
        """
    )

    def add_array(self, *args):
        """
        V.add_array(string) -> int
        C++: int AddArray(const char *name)
        Add to the list of arrays that have entries.  For arrays that
        already have entries, the settings are untouched.  For arrays
        that don't already have an entry, they are assumed to be enabled.
        This method should be called only by the filter owning this
        object.
        """
        ret = self._wrap_call(self._vtk_obj.AddArray, *args)
        return ret

    def array_exists(self, *args):
        """
        V.array_exists(string) -> int
        C++: int ArrayExists(const char *name)
        Return whether the array with the given name exists.
        """
        ret = self._wrap_call(self._vtk_obj.ArrayExists, *args)
        return ret

    def array_is_enabled(self, *args):
        """
        V.array_is_enabled(string) -> int
        C++: int ArrayIsEnabled(const char *name)
        Return whether the array with the given name is enabled.  If
        there is no entry, the array is assumed to be disabled.
        """
        ret = self._wrap_call(self._vtk_obj.ArrayIsEnabled, *args)
        return ret

    def copy_selections(self, *args):
        """
        V.copy_selections(DataArraySelection)
        C++: void CopySelections(DataArraySelection *selections)
        Copy the selections from the given DataArraySelection
        instance.
        """
        my_args = deref_array(args, [['vtkDataArraySelection']])
        ret = self._wrap_call(self._vtk_obj.CopySelections, *my_args)
        return ret

    def disable_all_arrays(self):
        """
        V.disable_all_arrays()
        C++: void DisableAllArrays()
        Disable all arrays that currently have an entry.
        """
        ret = self._vtk_obj.DisableAllArrays()
        return ret
        

    def disable_array(self, *args):
        """
        V.disable_array(string)
        C++: void DisableArray(const char *name)
        Disable the array with the given name.  Creates a new entry if
        none exists.
        """
        ret = self._wrap_call(self._vtk_obj.DisableArray, *args)
        return ret

    def enable_all_arrays(self):
        """
        V.enable_all_arrays()
        C++: void EnableAllArrays()
        Enable all arrays that currently have an entry.
        """
        ret = self._vtk_obj.EnableAllArrays()
        return ret
        

    def enable_array(self, *args):
        """
        V.enable_array(string)
        C++: void EnableArray(const char *name)
        Enable the array with the given name.  Creates a new entry if
        none exists.
        """
        ret = self._wrap_call(self._vtk_obj.EnableArray, *args)
        return ret

    def remove_all_arrays(self):
        """
        V.remove_all_arrays()
        C++: void RemoveAllArrays()
        Remove all array entries.
        """
        ret = self._vtk_obj.RemoveAllArrays()
        return ret
        

    def remove_array_by_index(self, *args):
        """
        V.remove_array_by_index(int)
        C++: void RemoveArrayByIndex(int index)
        Remove an array setting given its index.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveArrayByIndex, *args)
        return ret

    def remove_array_by_name(self, *args):
        """
        V.remove_array_by_name(string)
        C++: void RemoveArrayByName(const char *name)
        Remove an array setting given its name.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveArrayByName, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataArraySelection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataArraySelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit DataArraySelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataArraySelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

