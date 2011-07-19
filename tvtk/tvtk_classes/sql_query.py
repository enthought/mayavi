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

from tvtk.tvtk_classes.row_query import RowQuery


class SQLQuery(RowQuery):
    """
    SQLQuery - executes an sql query and retrieves results
    
    Superclass: RowQuery
    
    The abstract superclass of SQL query classes.  Instances of
    subclasses of SQLQuery are created using the get_query_instance()
    function in SQLDatabase.  To implement a query connection for a
    new database type, subclass both SQLDatabase and SQLQuery, and
    implement the required functions.  For the query class, this involves
    the following:
    
    Execute() - Execute the query on the database.  No results need to be
                retrieved at this point, unless you are performing
    caching.
    
    get_number_of_fields() - After Execute() is performed, returns the
    number
                          of fields in the query results.
    
    get_field_name() - The name of the field at an index.
    
    get_field_type() - The data type of the field at an index.
    
    next_row() - Advances the query results by one row, and returns
    whether
                there are more rows left in the query.
    
    data_value() - Extract a single data value from the current row.
    
    begin/_rollback/_commit_transaction() - These methods are optional but
    recommended if the database supports transactions.
    
    Thanks:
    
    Thanks to Andrew Wilson from Sandia National Laboratories for his
    work on the database classes.
    
    See Also:
    
    SQLDatabase
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSQLQuery, obj, update, **traits)
    
    query = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The query string to be executed.  Since some databases will
        process the query string as soon as it's set, this method returns
        a boolean to indicate success or failure.
        """
    )
    def _query_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuery,
                        self.query)

    def _get_database(self):
        return wrap_vtk(self._vtk_obj.GetDatabase())
    database = traits.Property(_get_database, help=\
        """
        Return the database associated with the query.
        """
    )

    def begin_transaction(self):
        """
        V.begin_transaction() -> bool
        C++: virtual bool BeginTransaction()
        Begin, commit, or roll back a transaction.  If the underlying
        database does not support transactions these calls will do
        nothing.
        """
        ret = self._vtk_obj.BeginTransaction()
        return ret
        

    def bind_parameter(self, *args):
        """
        V.bind_parameter(int, int) -> bool
        C++: virtual bool BindParameter(int index, int value)
        V.bind_parameter(int, int) -> bool
        C++: virtual bool BindParameter(int index, long value)
        V.bind_parameter(int, int) -> bool
        C++: virtual bool BindParameter(int index, TypeInt64 value)
        V.bind_parameter(int, float) -> bool
        C++: virtual bool BindParameter(int index, double value)
        V.bind_parameter(int, string, int) -> bool
        C++: virtual bool BindParameter(int index,
            const char *stringValue, size_t length)
        V.bind_parameter(int, string) -> bool
        C++: virtual bool BindParameter(int index,
            const StdString &string)
        V.bind_parameter(int, Variant) -> bool
        C++: virtual bool BindParameter(int index, Variant var)
        V.bind_parameter(int, , int) -> bool
        C++: virtual bool BindParameter(int index, const void *data,
            size_t length)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BindParameter, *my_args)
        return ret

    def clear_parameter_bindings(self):
        """
        V.clear_parameter_bindings() -> bool
        C++: virtual bool ClearParameterBindings()
        Reset all parameter bindings to NULL.
        """
        ret = self._vtk_obj.ClearParameterBindings()
        return ret
        

    def commit_transaction(self):
        """
        V.commit_transaction() -> bool
        C++: virtual bool CommitTransaction()
        Begin, commit, or roll back a transaction.  If the underlying
        database does not support transactions these calls will do
        nothing.
        """
        ret = self._vtk_obj.CommitTransaction()
        return ret
        

    def escape_string(self, *args):
        """
        V.escape_string(string, bool) -> string
        C++: virtual StdString EscapeString(StdString s,
            bool addSurroundingQuotes=true)
        Escape a string for inclusion into an SQL query. If
        add_surrounding_quotes is true, then quotation marks appropriate to
        the backend database will be added to enclose the escaped string.
        This argument defaults to true.
        
        A default, simple-minded implementation is provided for database
        backends that do not provde a way to escape strings for use
        inside queries.
        """
        ret = self._wrap_call(self._vtk_obj.EscapeString, *args)
        return ret

    def rollback_transaction(self):
        """
        V.rollback_transaction() -> bool
        C++: virtual bool RollbackTransaction()
        Begin, commit, or roll back a transaction.  If the underlying
        database does not support transactions these calls will do
        nothing.
        """
        ret = self._vtk_obj.RollbackTransaction()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('query', 'GetQuery'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('case_sensitive_field_names',
    'GetCaseSensitiveFieldNames'))
    
    _full_traitnames_list_ = \
    (['case_sensitive_field_names', 'debug', 'global_warning_display',
    'query'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SQLQuery, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SQLQuery properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['case_sensitive_field_names'], [], ['query']),
            title='Edit SQLQuery properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SQLQuery properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

