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

from tvtk.tvtk_classes.data_object import DataObject


class Table(DataObject):
    """
    Table - A table, which contains similar-typed columns of data
    
    Superclass: DataObject
    
    Table is a basic data structure for storing columns of data.
    Internally, columns are stored in a DataSetAttributes structure
    called row_data. However, using the Table API additionally ensures
    that every column has the same number of entries, and provides row
    access (using VariantArray) and single entry access (using
    Variant).
    
    The field data inherited from DataObject may be used to store
    metadata related to the table.
    
    Caveats:
    
    You should use the Table API to change the table data. Performing
    operations on the object returned by get_row_data() may yield
    unexpected results. Table does allow the user to set the field
    data using set_row_data(); the number of rows in the table is
    determined by the number of tuples in the first array (it is assumed
    that all arrays are the same length).
    
    Each column added with add_column musthave its name set to a unique,
    non-empty string in order for get_value() to function properly.
    
    Thanks:
    
    Thanks to Patricia Crossno, Ken Moreland, Andrew Wilson and Brian
    Wylie from Sandia National Laboratories for their help in developing
    this class API.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTable, obj, update, **traits)
    
    def _get_row_data(self):
        return wrap_vtk(self._vtk_obj.GetRowData())
    def _set_row_data(self, arg):
        old_val = self._get_row_data()
        self._wrap_call(self._vtk_obj.SetRowData,
                        deref_vtk(arg))
        self.trait_property_changed('row_data', old_val, arg)
    row_data = traits.Property(_get_row_data, _set_row_data, help=\
        """
        Get/Set the main data (columns) of the table.
        """
    )

    def get_value_by_name(self, *args):
        """
        V.get_value_by_name(int, string) -> Variant
        C++: Variant GetValueByName(IdType row, const char *col)
        Retrieve a value in the table by row index and column name as a
        variant.
        """
        ret = self._wrap_call(self._vtk_obj.GetValueByName, *args)
        return wrap_vtk(ret)

    def set_value_by_name(self, *args):
        """
        V.set_value_by_name(int, string, Variant)
        C++: void SetValueByName(IdType row, const char *col,
            Variant value)
        Set a value in the table by row index and column name as a
        variant.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetValueByName, *my_args)
        return ret

    def get_row(self, *args):
        """
        V.get_row(int) -> VariantArray
        C++: VariantArray *GetRow(IdType row)
        V.get_row(int, VariantArray)
        C++: void GetRow(IdType row, VariantArray *values)
        Get a row of the table as a VariantArray which has one entry
        for each column. NOTE: This version of the method is NOT thread
        safe.
        """
        my_args = deref_array(args, [['int'], ('int', 'vtkVariantArray')])
        ret = self._wrap_call(self._vtk_obj.GetRow, *my_args)
        return wrap_vtk(ret)

    def set_row(self, *args):
        """
        V.set_row(int, VariantArray)
        C++: void SetRow(IdType row, VariantArray *values)
        Set a row of the table with a VariantArray which has one entry
        for each column.
        """
        my_args = deref_array(args, [('int', 'vtkVariantArray')])
        ret = self._wrap_call(self._vtk_obj.SetRow, *my_args)
        return ret

    def get_value(self, *args):
        """
        V.get_value(int, int) -> Variant
        C++: Variant GetValue(IdType row, IdType col)
        Retrieve a value in the table by row and column index as a
        variant. Note that this calls get_value_by_name internally so that
        each column array must have its name set (and that name should be
        unique within the table).
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return wrap_vtk(ret)

    def set_value(self, *args):
        """
        V.set_value(int, int, Variant)
        C++: void SetValue(IdType row, IdType col, Variant value)
        Set a value in the table by row and column index as a variant.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetValue, *my_args)
        return ret

    number_of_rows = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of rows in the table. Note that memory allocation
        might be performed as a result of this, but no memory will be
        released.
        """
    )
    def _number_of_rows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfRows,
                        self.number_of_rows)

    def get_column(self, *args):
        """
        V.get_column(int) -> AbstractArray
        C++: AbstractArray *GetColumn(IdType col)
        Get a column of the table by its column index.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumn, *args)
        return wrap_vtk(ret)

    def get_column_by_name(self, *args):
        """
        V.get_column_by_name(string) -> AbstractArray
        C++: AbstractArray *GetColumnByName(const char *name)
        Get a column of the table by its name.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnByName, *args)
        return wrap_vtk(ret)

    def get_column_name(self, *args):
        """
        V.get_column_name(int) -> string
        C++: const char *GetColumnName(IdType col)"""
        ret = self._wrap_call(self._vtk_obj.GetColumnName, *args)
        return ret

    def _get_number_of_columns(self):
        return self._vtk_obj.GetNumberOfColumns()
    number_of_columns = traits.Property(_get_number_of_columns, help=\
        """
        Get the number of columns in the table.
        """
    )

    def add_column(self, *args):
        """
        V.add_column(AbstractArray)
        C++: void AddColumn(AbstractArray *arr)
        Add a column to the table.
        """
        my_args = deref_array(args, [['vtkAbstractArray']])
        ret = self._wrap_call(self._vtk_obj.AddColumn, *my_args)
        return ret

    def dump(self, *args):
        """
        V.dump(int)
        C++: void Dump(unsigned int colWidth=16)
        Dump table contents.
        """
        ret = self._wrap_call(self._vtk_obj.Dump, *args)
        return ret

    def insert_next_blank_row(self, *args):
        """
        V.insert_next_blank_row(float) -> int
        C++: IdType InsertNextBlankRow(double default_num_val=0.0)
        Insert a blank row at the end of the table.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextBlankRow, *args)
        return ret

    def insert_next_row(self, *args):
        """
        V.insert_next_row(VariantArray) -> int
        C++: IdType InsertNextRow(VariantArray *arr)
        Insert a row specified by a VariantArray.  The number of
        entries in the array should match the number of columns in the
        table.
        """
        my_args = deref_array(args, [['vtkVariantArray']])
        ret = self._wrap_call(self._vtk_obj.InsertNextRow, *my_args)
        return ret

    def remove_column(self, *args):
        """
        V.remove_column(int)
        C++: void RemoveColumn(IdType col)
        Remove a column from the table by its column index.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveColumn, *args)
        return ret

    def remove_column_by_name(self, *args):
        """
        V.remove_column_by_name(string)
        C++: void RemoveColumnByName(const char *name)
        Remove a column from the table by its name.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveColumnByName, *args)
        return ret

    def remove_row(self, *args):
        """
        V.remove_row(int)
        C++: void RemoveRow(IdType row)
        Delete a row from the table.  Rows below the deleted row are
        shifted up.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveRow, *args)
        return ret

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('whole_extent', 'GetWholeExtent'),
    ('update_number_of_pieces', 'GetUpdateNumberOfPieces'),
    ('update_ghost_level', 'GetUpdateGhostLevel'), ('update_extent',
    'GetUpdateExtent'), ('debug', 'GetDebug'), ('number_of_rows',
    'GetNumberOfRows'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('global_release_data_flag', 'GetGlobalReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('request_exact_extent',
    'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'number_of_rows', 'update_extent',
    'update_ghost_level', 'update_number_of_pieces', 'update_piece',
    'whole_bounding_box', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Table, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Table properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'number_of_rows', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit Table properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Table properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

