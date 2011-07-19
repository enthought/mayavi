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

from tvtk.tvtk_classes.selection_algorithm import SelectionAlgorithm


class ConvertSelection(SelectionAlgorithm):
    """
    ConvertSelection - Convert a selection from one type to another
    
    Superclass: SelectionAlgorithm
    
    ConvertSelection converts an input selection from one type to
    another in the context of a data object being selected. The first
    input is the selection, while the second input is the data object
    that the selection relates to.
    
    See Also:
    
    Selection SelectionNode ExtractSelection
    ExtractSelectedGraph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkConvertSelection, obj, update, **traits)
    
    match_any_values = tvtk_base.false_bool_trait(help=\
        """
        When on, creates a separate selection node for each array.
        Defaults to OFF.
        """
    )
    def _match_any_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMatchAnyValues,
                        self.match_any_values_)

    array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The output array name for value or threshold selections.
        """
    )
    def _array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayName,
                        self.array_name)

    output_type = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        The output selection content type. This should be one of the
        constants defined in SelectionNode.h.
        """
    )
    def _output_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputType,
                        self.output_type)

    input_field_type = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        The input field type. If this is set to a number other than -1,
        ignores the input selection field type and instead assumes that
        all selection nodes have the field type specified. This should be
        one of the constants defined in SelectionNode.h. Default is
        -1.
        """
    )
    def _input_field_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputFieldType,
                        self.input_field_type)

    def _get_array_names(self):
        return wrap_vtk(self._vtk_obj.GetArrayNames())
    def _set_array_names(self, arg):
        old_val = self._get_array_names()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetArrayNames,
                        my_arg[0])
        self.trait_property_changed('array_names', old_val, arg)
    array_names = traits.Property(_get_array_names, _set_array_names, help=\
        """
        The output array names for value selection.
        """
    )

    def get_selected_cells(self, *args):
        """
        V.get_selected_cells(Selection, DataSet, IdTypeArray)
        C++: static void GetSelectedCells(Selection *input,
            DataSet *data, IdTypeArray *indices)
        Static methods for easily obtaining selected items from a data
        object. The array argument will be filled with the selected
        items.
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkDataSet', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedCells, *my_args)
        return ret

    def get_selected_edges(self, *args):
        """
        V.get_selected_edges(Selection, Graph, IdTypeArray)
        C++: static void GetSelectedEdges(Selection *input,
            Graph *data, IdTypeArray *indices)
        Static methods for easily obtaining selected items from a data
        object. The array argument will be filled with the selected
        items.
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkGraph', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedEdges, *my_args)
        return ret

    def get_selected_items(self, *args):
        """
        V.get_selected_items(Selection, DataObject, int,
            IdTypeArray)
        C++: static void GetSelectedItems(Selection *input,
            DataObject *data, int fieldType, IdTypeArray *indices)
        Static generic method for obtaining selected items from a data
        object. Other static methods (e.g. get_selected_vertices) call this
        one.
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkDataObject', 'int', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedItems, *my_args)
        return ret

    def get_selected_points(self, *args):
        """
        V.get_selected_points(Selection, DataSet, IdTypeArray)
        C++: static void GetSelectedPoints(Selection *input,
            DataSet *data, IdTypeArray *indices)
        Static methods for easily obtaining selected items from a data
        object. The array argument will be filled with the selected
        items.
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkDataSet', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedPoints, *my_args)
        return ret

    def get_selected_rows(self, *args):
        """
        V.get_selected_rows(Selection, Table, IdTypeArray)
        C++: static void GetSelectedRows(Selection *input,
            Table *data, IdTypeArray *indices)
        Static methods for easily obtaining selected items from a data
        object. The array argument will be filled with the selected
        items.
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkTable', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedRows, *my_args)
        return ret

    def get_selected_vertices(self, *args):
        """
        V.get_selected_vertices(Selection, Graph, IdTypeArray)
        C++: static void GetSelectedVertices(Selection *input,
            Graph *data, IdTypeArray *indices)
        Static methods for easily obtaining selected items from a data
        object. The array argument will be filled with the selected
        items.
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkGraph', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedVertices, *my_args)
        return ret

    def add_array_name(self, *args):
        """
        V.add_array_name(string)
        C++: void AddArrayName(const char *)
        Convenience methods used by UI
        """
        ret = self._wrap_call(self._vtk_obj.AddArrayName, *args)
        return ret

    def clear_array_names(self):
        """
        V.clear_array_names()
        C++: void ClearArrayNames()
        Convenience methods used by UI
        """
        ret = self._vtk_obj.ClearArrayNames()
        return ret
        

    def set_data_object_connection(self, *args):
        """
        V.set_data_object_connection(AlgorithmOutput)
        C++: void SetDataObjectConnection(AlgorithmOutput *in)
        A convenience method for setting the second input (i.e. the data
        object).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataObjectConnection, *my_args)
        return ret

    def to_global_id_selection(self, *args):
        """
        V.to_global_id_selection(Selection, DataObject) -> Selection
        C++: static Selection *ToGlobalIdSelection(Selection *input,
             DataObject *data)
        Static methods for easily converting between selection types.
        NOTE: The returned selection pointer IS reference counted, so be
        sure to Delete() it when you are done with it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ToGlobalIdSelection, *my_args)
        return wrap_vtk(ret)

    def to_index_selection(self, *args):
        """
        V.to_index_selection(Selection, DataObject) -> Selection
        C++: static Selection *ToIndexSelection(Selection *input,
            DataObject *data)
        Static methods for easily converting between selection types.
        NOTE: The returned selection pointer IS reference counted, so be
        sure to Delete() it when you are done with it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ToIndexSelection, *my_args)
        return wrap_vtk(ret)

    def to_pedigree_id_selection(self, *args):
        """
        V.to_pedigree_id_selection(Selection, DataObject)
            -> Selection
        C++: static Selection *ToPedigreeIdSelection(
            Selection *input, DataObject *data)
        Static methods for easily converting between selection types.
        NOTE: The returned selection pointer IS reference counted, so be
        sure to Delete() it when you are done with it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ToPedigreeIdSelection, *my_args)
        return wrap_vtk(ret)

    def to_selection_type(self, *args):
        """
        V.to_selection_type(Selection, DataObject, int,
            StringArray, int) -> Selection
        C++: static Selection *ToSelectionType(Selection *input,
            DataObject *data, int type, StringArray *arrayNames=0,
            int inputFieldType=-1)
        A generic static method for converting selection types. The type
        should be an integer constant defined in SelectionNode.h.
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkDataObject', 'int', 'vtkStringArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.ToSelectionType, *my_args)
        return wrap_vtk(ret)

    def to_value_selection(self, *args):
        """
        V.to_value_selection(Selection, DataObject, string)
            -> Selection
        C++: static Selection *ToValueSelection(Selection *input,
            DataObject *data, const char *arrayName)
        V.to_value_selection(Selection, DataObject, StringArray)
            -> Selection
        C++: static Selection *ToValueSelection(Selection *input,
            DataObject *data, StringArray *arrayNames)
        Static methods for easily converting between selection types.
        NOTE: The returned selection pointer IS reference counted, so be
        sure to Delete() it when you are done with it.
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkDataObject', 'string'), ('vtkSelection', 'vtkDataObject', 'vtkStringArray')])
        ret = self._wrap_call(self._vtk_obj.ToValueSelection, *my_args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('input_field_type',
    'GetInputFieldType'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('match_any_values', 'GetMatchAnyValues'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress',
    'GetProgress'), ('reference_count', 'GetReferenceCount'),
    ('output_type', 'GetOutputType'), ('array_name', 'GetArrayName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'match_any_values', 'release_data_flag', 'array_name',
    'input_field_type', 'output_type', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ConvertSelection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ConvertSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['match_any_values'], [], ['array_name',
            'input_field_type', 'output_type']),
            title='Edit ConvertSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ConvertSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

