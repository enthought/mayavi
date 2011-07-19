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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class PassArrays(DataObjectAlgorithm):
    """
    PassArrays - Passes a subset of arrays to the output
    
    Superclass: DataObjectAlgorithm
    
    This filter preserves all the topology of the input, but only a
    subset of arrays are passed to the output. Add an array to be passed
    to the output data object with add_array(). If remove_arrays is on, the
    specified arrays will be the ones that are removed instead of the
    ones that are kept.
    
    Arrays with special attributes (scalars, pedigree ids, etc.) will
    retain those attributes in the output.
    
    By default, only those field types with at least one array specified
    through add_array will be processed. If instead use_field_types is
    turned on, you explicitly set which field types to process with
    add_field_type.
    
    Example 1:
    
    pass_array->_add_array(vtk_data_object::_point, "velocity"); 
    
    The output will have only that one array "velocity" in the point
    data, but cell and field data will be untouched.
    
    Example 2:
    
    pass_array->_add_array(vtk_data_object::_point, "velocity");
    pass_array->_use_field_types_on();
    pass_array->_add_field_type(vtk_data_object::_point);
    pass_array->_add_field_type(vtk_data_object::_cell); 
    
    The point data would still contain the single array, but the cell
    data would be cleared since you did not specify any arrays to pass.
    Field data would still be untouched.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPassArrays, obj, update, **traits)
    
    remove_arrays = tvtk_base.false_bool_trait(help=\
        """
        Instead of passing only the specified arrays, remove the
        specified arrays and keep all other arrays. Default is off.
        """
    )
    def _remove_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRemoveArrays,
                        self.remove_arrays_)

    use_field_types = tvtk_base.false_bool_trait(help=\
        """
        Process only those field types explicitly specified with
        add_field_type. Otherwise, processes field types associated with at
        least one specified array. Default is off.
        """
    )
    def _use_field_types_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseFieldTypes,
                        self.use_field_types_)

    def add_array(self, *args):
        """
        V.add_array(int, string)
        C++: virtual void AddArray(int fieldType, const char *name)
        Adds an array to pass through. field_type where the array that
        should be passed (point data, cell data, etc.). It should be one
        of the constants defined in the DataObject::AttributeTypes
        enumeration.
        """
        ret = self._wrap_call(self._vtk_obj.AddArray, *args)
        return ret

    def add_field_type(self, *args):
        """
        V.add_field_type(int)
        C++: virtual void AddFieldType(int fieldType)
        Add a field type to process. field_type where the array that
        should be passed (point data, cell data, etc.). It should be one
        of the constants defined in the DataObject::AttributeTypes
        enumeration. NOTE: These are only used if use_field_type is turned
        on.
        """
        ret = self._wrap_call(self._vtk_obj.AddFieldType, *args)
        return ret

    def clear_arrays(self):
        """
        V.clear_arrays()
        C++: virtual void ClearArrays()
        Clear all arrays to pass through.
        """
        ret = self._vtk_obj.ClearArrays()
        return ret
        

    def clear_field_types(self):
        """
        V.clear_field_types()
        C++: virtual void ClearFieldTypes()
        Clear all field types to process.
        """
        ret = self._vtk_obj.ClearFieldTypes()
        return ret
        

    _updateable_traits_ = \
    (('use_field_types', 'GetUseFieldTypes'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('remove_arrays', 'GetRemoveArrays'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'remove_arrays', 'use_field_types',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PassArrays, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PassArrays properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['remove_arrays', 'use_field_types'], [], []),
            title='Edit PassArrays properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PassArrays properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

