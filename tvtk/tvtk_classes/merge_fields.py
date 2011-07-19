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


class MergeFields(DataSetAlgorithm):
    """
    MergeFields - Merge multiple fields into one.
    
    Superclass: DataSetAlgorithm
    
    MergeFields is used to merge mutliple field into one. The new
    field is put in the same field data as the original field. For
    example
     mf->_set_output_field("foo", MergeFields::POINT_DATA);
     mf->_set_number_of_components(_2);
     mf->Merge(0, "array1", 1);
     mf->Merge(1, "array2", 0);
      will tell MergeFields to use the 2nd component of array1 and the
    1st component of array2 to create a 2 component field called foo. The
    same can be done using Tcl:
     mf set_output_field foo POINT_DATA
     mf Merge 0 array1 1
     mf Merge 1 array2 0
    
     Field locations: DATA_OBJECT, POINT_DATA, CELL_DATA
     
    
    See Also:
    
    FieldData DataSet DataObjectToDataSetFilter
    DataSetAttributes DataArray RearrangeFields SplitField
    AssignAttribute
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMergeFields, obj, update, **traits)
    
    number_of_components = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of the components in the output field. This has to
        be set before execution. Default value is 0.
        """
    )
    def _number_of_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfComponents,
                        self.number_of_components)

    def merge(self, *args):
        """
        V.merge(int, string, int)
        C++: void Merge(int component, const char *arrayName,
            int sourceComp)
        Add a component (array_name,source_comp) to the output field.
        """
        ret = self._wrap_call(self._vtk_obj.Merge, *args)
        return ret

    def set_output_field(self, *args):
        """
        V.set_output_field(string, int)
        C++: void SetOutputField(const char *name, int fieldLoc)
        V.set_output_field(string, string)
        C++: void SetOutputField(const char *name, const char *fieldLoc)
        The output field will have the given name and it will be in
        field_loc (the input fields also have to be in field_loc).
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputField, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('number_of_components',
    'GetNumberOfComponents'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_components', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MergeFields, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MergeFields properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_components']),
            title='Edit MergeFields properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MergeFields properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

