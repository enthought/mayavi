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


class SQLDatabase(Object):
    """
    SQLDatabase - maintain a connection to an sql database
    
    Superclass: Object
    
    Abstract base class for all SQL database connection classes. Manages
    a connection to the database, and is responsible for creating
    instances of the associated SQLQuery objects associated with this
    class in order to perform execute queries on the database. To allow
    connections to a new type of database, create both a subclass of this
    class and SQLQuery, and implement the required functions:
    
    Open() - open the database connection, if possible. Close() - close
    the connection. get_query_instance() - create and return an instance of
    the SQLQuery
                         subclass associated with the database type.
    
    The subclass should also provide API to set connection parameters.
    
    This class also provides the function effect_schema to transform a
    database schema into a SQL database.
    
    Thanks:
    
    Thanks to Andrew Wilson from Sandia National Laboratories for his
    work on the database classes and for the SQLite example. Thanks to
    David Thompson and Philippe Pebay from Sandia National Laboratories
    for implementing this class.
    
    See Also:
    
    SQLQuery SQLDatabaseSchema
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSQLDatabase, obj, update, **traits)
    
    def get_column_specification(self, *args):
        """
        V.get_column_specification(SQLDatabaseSchema, int, int) -> string
        C++: virtual StdString GetColumnSpecification(
            SQLDatabaseSchema *schema, int tblHandle, int colHandle)
        Return the SQL string with the syntax to create a column inside a "CREATE
        TABLE" SQL statement. NB: this method implements the following
        minimally-portable syntax: <column name> <column type> <column
        attributes> It must be overwritten for those SQL backends which
        have a different syntax such as, e.g., my_sql.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetColumnSpecification, *my_args)
        return ret

    def _get_database_type(self):
        return self._vtk_obj.GetDatabaseType()
    database_type = traits.Property(_get_database_type, help=\
        """
        Get the type of the database (e.g. mysql, psql,..).
        """
    )

    def get_index_specification(self, *args):
        """
        V.get_index_specification(SQLDatabaseSchema, int, int, bool)
            -> string
        C++: virtual StdString GetIndexSpecification(
            SQLDatabaseSchema *schema, int tblHandle, int idxHandle,
            bool &skipped)
        Return the SQL string with the syntax to create an index inside a "CREATE
        TABLE" SQL statement. NB1: this method implements the following
        minimally-portable syntax: <index type> [<index name>] (<column
        name 1>,... ) It must be overwritten for those SQL backends which
        have a different syntax such as, e.g., my_sql. NB2: this method
        does not assume that INDEX creation is supported within a CREATE
        TABLE statement. Therefore, should such an INDEX arise in the
        schema, a CREATE INDEX statement is returned and skipped is set
        to true. Otherwise, skipped will always be returned false.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetIndexSpecification, *my_args)
        return ret

    def _get_last_error_text(self):
        return self._vtk_obj.GetLastErrorText()
    last_error_text = traits.Property(_get_last_error_text, help=\
        """
        Get the last error text from the database I'm using const so that
        people do NOT use the standard GetStringMacro in their
        implementation, because 99% of the time that will not be the
        correct thing to do...
        """
    )

    def _get_query_instance(self):
        return wrap_vtk(self._vtk_obj.GetQueryInstance())
    query_instance = traits.Property(_get_query_instance, help=\
        """
        Return an empty query on this database.
        """
    )

    def get_record(self, *args):
        """
        V.get_record(string) -> StringArray
        C++: virtual StringArray *GetRecord(const char *table)
        Get the list of fields for a particular table.
        """
        ret = self._wrap_call(self._vtk_obj.GetRecord, *args)
        return wrap_vtk(ret)

    def get_table_preamble(self, *args):
        """
        V.get_table_preamble(bool) -> string
        C++: virtual StdString GetTablePreamble(bool)
        Return the SQL string with the syntax of the preamble following a "CREATE
        TABLE" SQL statement. NB: by default, this method returns an
        empty string. It must be overwritten for those SQL backends which
        allow such preambles such as, e.g., my_sql.
        """
        ret = self._wrap_call(self._vtk_obj.GetTablePreamble, *args)
        return ret

    def _get_tables(self):
        return wrap_vtk(self._vtk_obj.GetTables())
    tables = traits.Property(_get_tables, help=\
        """
        Get the list of tables from the database.
        """
    )

    def get_trigger_specification(self, *args):
        """
        V.get_trigger_specification(SQLDatabaseSchema, int, int)
            -> string
        C++: virtual StdString GetTriggerSpecification(
            SQLDatabaseSchema *schema, int tblHandle, int trgHandle)
        Return the SQL string with the syntax to create a trigger using a "CREATE
        TRIGGER" SQL statement. NB1: support is contingent on
        VTK_FEATURE_TRIGGERS being recognized as a supported feature. Not
        all backends (e.g., SQLite) support it. NB2: this method
        implements the following minimally-portable syntax: <trigger
        name> {BEFORE | AFTER} ON <table name> FOR EACH ROW <trigger
        action> It must be overwritten for those SQL backends which have
        a different syntax such as, e.g., postgre_sql.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetTriggerSpecification, *my_args)
        return ret

    def _get_url(self):
        return self._vtk_obj.GetURL()
    url = traits.Property(_get_url, help=\
        """
        Get the URL of the database.
        """
    )

    def close(self):
        """
        V.close()
        C++: virtual void Close()
        Close the connection to the database.
        """
        ret = self._vtk_obj.Close()
        return ret
        

    def create_from_url(self, *args):
        """
        V.create_from_url(string) -> SQLDatabase
        C++: static SQLDatabase *CreateFromURL(const char *URL)
        Create a the proper subclass given a URL. The URL format for SQL
        databases is a true URL of the form:
         
        'protocol://'[[username[':'password]'@']hostname[':'port]]'/'[dbna
        me] .
        """
        ret = self._wrap_call(self._vtk_obj.CreateFromURL, *args)
        return wrap_vtk(ret)

    def DATABASE(self):
        """
        V.database() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *DATABASE()
        Stores the database class pointer as an information key. This is
        currently used to store database pointers as part of 'data on
        demand' data objects. For example: The application may have a
        table/tree/whatever of documents, the data structure is storing
        the meta-data but not the full text. Further down the pipeline
        algorithms or views may want to retrieve additional information
        (full text)for specific documents.
        """
        ret = wrap_vtk(self._vtk_obj.DATABASE())
        return ret
        

    def effect_schema(self, *args):
        """
        V.effect_schema(SQLDatabaseSchema, bool) -> bool
        C++: virtual bool EffectSchema(SQLDatabaseSchema *,
            bool dropIfExists=false)
        Effect a database schema.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.EffectSchema, *my_args)
        return ret

    def has_error(self):
        """
        V.has_error() -> bool
        C++: virtual bool HasError()
        Did the last operation generate an error
        """
        ret = self._vtk_obj.HasError()
        return ret
        

    def is_open(self):
        """
        V.is_open() -> bool
        C++: virtual bool IsOpen()
        Return whether the database has an open connection.
        """
        ret = self._vtk_obj.IsOpen()
        return ret
        

    def is_supported(self, *args):
        """
        V.is_supported(int) -> bool
        C++: virtual bool IsSupported(int feature)
        Return whether a feature is supported by the database.
        """
        ret = self._wrap_call(self._vtk_obj.IsSupported, *args)
        return ret

    def open(self, *args):
        """
        V.open(string) -> bool
        C++: virtual bool Open(const char *password)
        Open a new connection to the database. You need to set up any
        database parameters before calling this function. For database
        connections that do not require a password, pass an empty string.
        Returns true is the database was opened sucessfully, and false
        otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.Open, *args)
        return ret

    def un_register_all_create_from_url_callbacks(self):
        """
        V.un_register_all_create_from_url_callbacks()
        C++: static void UnRegisterAllCreateFromURLCallbacks()
        Provides mechanism to register/unregister additional callbacks to
        create concrete subclasses of SQLDatabase to handle different
        protocols. The registered callbacks are tried in the order they
        are registered.
        """
        ret = self._vtk_obj.UnRegisterAllCreateFromURLCallbacks()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SQLDatabase, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SQLDatabase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit SQLDatabase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SQLDatabase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

