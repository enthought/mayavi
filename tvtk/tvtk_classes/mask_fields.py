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


class MaskFields(DataSetAlgorithm):
    """
    MaskFields - Allow control of which fields get passed
    
    Superclass: DataSetAlgorithm
    
    MaskFields is used to mark which fields in the input dataset get
    copied to the output.  The output will contain only those fields
    marked as on by the filter.
    
    See Also:
    
    FieldData DataSet DataObjectToDataSetFilter
    DataSetAttributes DataArray RearrangeFields SplitField
    MergeFields AssignAttribute
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMaskFields, obj, update, **traits)
    
    def copy_all_off(self):
        """
        V.copy_all_off()
        C++: virtual void CopyAllOff()
        Turn off copying of all data. During the copying/passing, the
        following rules are followed for each array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyAllOff()
        return ret
        

    def copy_all_on(self):
        """
        V.copy_all_on()
        C++: virtual void CopyAllOn()
        Turn on copying of all data. During the copying/passing, the
        following rules are followed for each array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array
        """
        ret = self._vtk_obj.CopyAllOn()
        return ret
        

    def copy_attribute_off(self, *args):
        """
        V.copy_attribute_off(int, int)
        C++: void CopyAttributeOff(int attributeLocation,
            int attributeType)
        V.copy_attribute_off(string, string)
        C++: void CopyAttributeOff(const char *attributeLoc,
            const char *attributeType)
        Turn on/off the copying of the attribute or specified by
        DataSetAttributes:AttributeTypes. During the copying/passing,
        the following rules are followed for each array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array An attribute type and a location must be
           specified. For example:
         mask_fields->_copy_attribute_off(vtk_mask_fields::_point__data, DataSetAttributes::SCALARS);
          causes the scalars on the input point data to not get copied to
        the output.
        """
        ret = self._wrap_call(self._vtk_obj.CopyAttributeOff, *args)
        return ret

    def copy_attribute_on(self, *args):
        """
        V.copy_attribute_on(int, int)
        C++: void CopyAttributeOn(int attributeLocation,
            int attributeType)
        V.copy_attribute_on(string, string)
        C++: void CopyAttributeOn(const char *attributeLoc,
            const char *attributeType)
        Turn on/off the copying of the attribute or specified by
        DataSetAttributes:AttributeTypes. During the copying/passing,
        the following rules are followed for each array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array An attribute type and a location must be
           specified. For example:
         mask_fields->_copy_attribute_off(vtk_mask_fields::_point__data, DataSetAttributes::SCALARS);
          causes the scalars on the input point data to not get copied to
        the output.
        """
        ret = self._wrap_call(self._vtk_obj.CopyAttributeOn, *args)
        return ret

    def copy_attributes_off(self):
        """
        V.copy_attributes_off()
        C++: void CopyAttributesOff()
        Convenience methods which operate on all field data or attribute
        data.  More specific than copy_all_on or copy_all_off
        """
        ret = self._vtk_obj.CopyAttributesOff()
        return ret
        

    def copy_attributes_on(self):
        """
        V.copy_attributes_on()
        C++: void CopyAttributesOn()"""
        ret = self._vtk_obj.CopyAttributesOn()
        return ret
        

    def copy_field_off(self, *args):
        """
        V.copy_field_off(int, string)
        C++: void CopyFieldOff(int fieldLocation, const char *name)
        V.copy_field_off(string, string)
        C++: void CopyFieldOff(const char *fieldLoc, const char *name)
        Turn on/off the copying of the field or specified by name. During
        the copying/passing, the following rules are followed for each
        array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array A field name and a location must be
           specified. For example:
         mask_fields->_copy_field_off(vtk_mask_fields::_cell__data, "foo");
          causes the field "foo" on the input cell data to not get copied
           to the output.
        """
        ret = self._wrap_call(self._vtk_obj.CopyFieldOff, *args)
        return ret

    def copy_field_on(self, *args):
        """
        V.copy_field_on(int, string)
        C++: void CopyFieldOn(int fieldLocation, const char *name)
        V.copy_field_on(string, string)
        C++: void CopyFieldOn(const char *fieldLoc, const char *name)
        Turn on/off the copying of the field or specified by name. During
        the copying/passing, the following rules are followed for each
        array:
        1. If the copy flag for an array is set (on or off), it is
           applied This overrides rule 2.
        2. If copy_all_on is set, copy the array. If copy_all_off is set, do
           not copy the array A field name and a location must be
           specified. For example:
         mask_fields->_copy_field_off(vtk_mask_fields::_cell__data, "foo");
          causes the field "foo" on the input cell data to not get copied
           to the output.
        """
        ret = self._wrap_call(self._vtk_obj.CopyFieldOn, *args)
        return ret

    def copy_fields_off(self):
        """
        V.copy_fields_off()
        C++: void CopyFieldsOff()
        Convenience methods which operate on all field data or attribute
        data.  More specific than copy_all_on or copy_all_off
        """
        ret = self._vtk_obj.CopyFieldsOff()
        return ret
        

    def copy_fields_on(self):
        """
        V.copy_fields_on()
        C++: void CopyFieldsOn()"""
        ret = self._vtk_obj.CopyFieldsOn()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MaskFields, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MaskFields properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit MaskFields properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MaskFields properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

