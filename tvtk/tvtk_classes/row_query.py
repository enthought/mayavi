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


class RowQuery(Object):
    """
    RowQuery - abstract interface for queries that return
    
    Superclass: Object
    
    The abstract superclass of query classes that return row-oriented
    (table) results.  A subclass will provide database-specific query
    parameters and implement the RowQuery API to return query results:
    
    Execute() - Execute the query.  No results need to be retrieved at
    this
                point, unless you are performing caching.
    
    get_number_of_fields() - After Execute() is performed, returns the
    number
                          of fields in the query results.
    
    get_field_name() - The name of the field at an index.
    
    get_field_type() - The data type of the field at an index.
    
    next_row() - Advances the query results by one row, and returns
    whether
                there are more rows left in the query.
    
    data_value() - Extract a single data value from the current row.
    
    Thanks:
    
    Thanks to Andrew Wilson from Sandia National Laboratories for his
    work on the database classes.
    
    See Also:
    
    RowQueryToTable
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRowQuery, obj, update, **traits)
    
    case_sensitive_field_names = tvtk_base.false_bool_trait(help=\
        """
        Many databases do not preserve case in field names.  This can
        cause get_field_index to fail if you search for a field named
        some_field_name when the database actually stores it as
        SOMEFIELDNAME.  This ivar controls whether get_field_index()
        expects field names to be case-sensitive.  The default is OFF,
        i.e. case is not preserved.
        """
    )
    def _case_sensitive_field_names_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCaseSensitiveFieldNames,
                        self.case_sensitive_field_names_)

    def get_field_index(self, *args):
        """
        V.get_field_index(string) -> int
        C++: int GetFieldIndex(char *name)
        Return the index of the specified query field. Uses
        get_number_of_fields() and get_field_name() to match field name.
        """
        ret = self._wrap_call(self._vtk_obj.GetFieldIndex, *args)
        return ret

    def get_field_name(self, *args):
        """
        V.get_field_name(int) -> string
        C++: virtual const char *GetFieldName(int i)
        Return the name of the specified query field.
        """
        ret = self._wrap_call(self._vtk_obj.GetFieldName, *args)
        return ret

    def get_field_type(self, *args):
        """
        V.get_field_type(int) -> int
        C++: virtual int GetFieldType(int i)
        Return the type of the field, using the constants defined in
        Type.h.
        """
        ret = self._wrap_call(self._vtk_obj.GetFieldType, *args)
        return ret

    def _get_last_error_text(self):
        return self._vtk_obj.GetLastErrorText()
    last_error_text = traits.Property(_get_last_error_text, help=\
        """
        Get the last error text from the query
        """
    )

    def _get_number_of_fields(self):
        return self._vtk_obj.GetNumberOfFields()
    number_of_fields = traits.Property(_get_number_of_fields, help=\
        """
        The number of fields in the query result.
        """
    )

    def data_value(self, *args):
        """
        V.data_value(int) -> Variant
        C++: virtual Variant DataValue(IdType c)
        Return data in current row, field c
        """
        ret = self._wrap_call(self._vtk_obj.DataValue, *args)
        return wrap_vtk(ret)

    def execute(self):
        """
        V.execute() -> bool
        C++: virtual bool Execute()
        Execute the query.  This must be performed before any field name
        or data access functions are used.
        """
        ret = self._vtk_obj.Execute()
        return ret
        

    def has_error(self):
        """
        V.has_error() -> bool
        C++: virtual bool HasError()
        Returns true if an error is set, otherwise false.
        """
        ret = self._vtk_obj.HasError()
        return ret
        

    def is_active(self):
        """
        V.is_active() -> bool
        C++: virtual bool IsActive()
        Return true if the query is active (i.e. execution was successful
        and results are ready to be fetched).  Returns false on error or
        inactive query.
        """
        ret = self._vtk_obj.IsActive()
        return ret
        

    def next_row(self, *args):
        """
        V.next_row() -> bool
        C++: virtual bool NextRow()
        V.next_row(VariantArray) -> bool
        C++: bool NextRow(VariantArray *rowArray)
        Advance row, return false if past end.
        """
        my_args = deref_array(args, [None, ['vtkVariantArray']])
        ret = self._wrap_call(self._vtk_obj.NextRow, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('case_sensitive_field_names', 'GetCaseSensitiveFieldNames'))
    
    _full_traitnames_list_ = \
    (['case_sensitive_field_names', 'debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RowQuery, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RowQuery properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['case_sensitive_field_names'], [], []),
            title='Edit RowQuery properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RowQuery properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

