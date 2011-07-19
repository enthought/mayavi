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

from tvtk.tvtk_classes.array_data_algorithm import ArrayDataAlgorithm


class TableToSparseArray(ArrayDataAlgorithm):
    """
    TableToSparseArray - converts a Table into a sparse array.
    
    Superclass: ArrayDataAlgorithm
    
    Converts a Table into a sparse array.  Use add_coordinate_column()
    to designate one-to-many table columns that contain coordinates for
    each array value, and set_value_column() to designate the table column
    that contains array values.
    
    Thus, the number of dimensions in the output array will equal the
    number of calls to add_coordinate_column().
    
    The coordinate columns will also be used to populate dimension labels
    in the output array.
    
    Thanks:
    
    Developed by Timothy M. Shead (tshead@sandia.gov) at Sandia National
    Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableToSparseArray, obj, update, **traits)
    
    value_column = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Specify the input table column that will be mapped to values in
        the output array.
        """
    )
    def _value_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValueColumn,
                        self.value_column)

    def add_coordinate_column(self, *args):
        """
        V.add_coordinate_column(string)
        C++: void AddCoordinateColumn(const char *name)
        Specify the set of input table columns that will be mapped to
        coordinates in the output sparse array.
        """
        ret = self._wrap_call(self._vtk_obj.AddCoordinateColumn, *args)
        return ret

    def clear_coordinate_columns(self):
        """
        V.clear_coordinate_columns()
        C++: void ClearCoordinateColumns()
        Specify the set of input table columns that will be mapped to
        coordinates in the output sparse array.
        """
        ret = self._vtk_obj.ClearCoordinateColumns()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('value_column',
    'GetValueColumn'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'value_column'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableToSparseArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TableToSparseArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['value_column']),
            title='Edit TableToSparseArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableToSparseArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

