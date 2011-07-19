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


class SQLDatabaseSchema(Object):
    """
    SQLDatabaseSchema - represent an SQL database schema
    
    Superclass: Object
    
    This class stores the information required to create an SQL database
    from scratch. Information on each table's columns, indices, and
    triggers is stored. You may also store an arbitrary number of
    preamble statements, intended to be executed before any tables are
    created; this provides a way to create procedures or functions that
    may be invoked as part of a trigger action. Triggers and table
    options may be specified differently for each backend database type
    you wish to support.
    
    Thanks:
    
    Thanks to Philippe Pebay and David Thompson from Sandia National
    Laboratories for implementing this class.
    
    See Also:
    
    SQLDatabase
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSQLDatabaseSchema, obj, update, **traits)
    
    name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the name of the schema.
        """
    )
    def _name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetName,
                        self.name)

    def get_column_attributes_from_handle(self, *args):
        """
        V.get_column_attributes_from_handle(int, int) -> string
        C++: const char *GetColumnAttributesFromHandle(int tblHandle,
            int colHandle)
        Given the handles of a table and a column, get the attributes of
        the column.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnAttributesFromHandle, *args)
        return ret

    def get_column_handle_from_name(self, *args):
        """
        V.get_column_handle_from_name(string, string) -> int
        C++: int GetColumnHandleFromName(const char *tblName,
            const char *colName)
        Given the names of a table and a column, get the handle of the
        column in this table.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnHandleFromName, *args)
        return ret

    def get_column_name_from_handle(self, *args):
        """
        V.get_column_name_from_handle(int, int) -> string
        C++: const char *GetColumnNameFromHandle(int tblHandle,
            int colHandle)
        Given the handles of a table and a column, get the name of the
        column.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnNameFromHandle, *args)
        return ret

    def get_column_size_from_handle(self, *args):
        """
        V.get_column_size_from_handle(int, int) -> int
        C++: int GetColumnSizeFromHandle(int tblHandle, int colHandle)
        Given the handles of a table and a column, get the size of the
        column.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnSizeFromHandle, *args)
        return ret

    def get_column_type_from_handle(self, *args):
        """
        V.get_column_type_from_handle(int, int) -> int
        C++: int GetColumnTypeFromHandle(int tblHandle, int colHandle)
        Given the handles of a table and a column, get the type of the
        column.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnTypeFromHandle, *args)
        return ret

    def get_index_column_name_from_handle(self, *args):
        """
        V.get_index_column_name_from_handle(int, int, int) -> string
        C++: const char *GetIndexColumnNameFromHandle(int tblHandle,
            int idxHandle, int cnmHandle)
        Given the handles of a table, an index, and a column name, get
        the column name.
        """
        ret = self._wrap_call(self._vtk_obj.GetIndexColumnNameFromHandle, *args)
        return ret

    def get_index_handle_from_name(self, *args):
        """
        V.get_index_handle_from_name(string, string) -> int
        C++: int GetIndexHandleFromName(const char *tblName,
            const char *idxName)
        Given the names of a table and an index, get the handle of the
        index in this table.
        """
        ret = self._wrap_call(self._vtk_obj.GetIndexHandleFromName, *args)
        return ret

    def get_index_name_from_handle(self, *args):
        """
        V.get_index_name_from_handle(int, int) -> string
        C++: const char *GetIndexNameFromHandle(int tblHandle,
            int idxHandle)
        Given the handles of a table and an index, get the name of the
        index.
        """
        ret = self._wrap_call(self._vtk_obj.GetIndexNameFromHandle, *args)
        return ret

    def get_index_type_from_handle(self, *args):
        """
        V.get_index_type_from_handle(int, int) -> int
        C++: int GetIndexTypeFromHandle(int tblHandle, int idxHandle)
        Given the handles of a table and an index, get the type of the
        index.
        """
        ret = self._wrap_call(self._vtk_obj.GetIndexTypeFromHandle, *args)
        return ret

    def get_number_of_column_names_in_index(self, *args):
        """
        V.get_number_of_column_names_in_index(int, int) -> int
        C++: int GetNumberOfColumnNamesInIndex(int tblHandle,
            int idxHandle)
        Get the number of column names associated to a particular index
        in a particular table .
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfColumnNamesInIndex, *args)
        return ret

    def get_number_of_columns_in_table(self, *args):
        """
        V.get_number_of_columns_in_table(int) -> int
        C++: int GetNumberOfColumnsInTable(int tblHandle)
        Get the number of columns in a particular table .
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfColumnsInTable, *args)
        return ret

    def get_number_of_indices_in_table(self, *args):
        """
        V.get_number_of_indices_in_table(int) -> int
        C++: int GetNumberOfIndicesInTable(int tblHandle)
        Get the number of indices in a particular table .
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfIndicesInTable, *args)
        return ret

    def get_number_of_options_in_table(self, *args):
        """
        V.get_number_of_options_in_table(int) -> int
        C++: int GetNumberOfOptionsInTable(int tblHandle)
        Get the number of options associated with a particular table.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfOptionsInTable, *args)
        return ret

    def _get_number_of_preambles(self):
        return self._vtk_obj.GetNumberOfPreambles()
    number_of_preambles = traits.Property(_get_number_of_preambles, help=\
        """
        Get the number of preambles.
        """
    )

    def _get_number_of_tables(self):
        return self._vtk_obj.GetNumberOfTables()
    number_of_tables = traits.Property(_get_number_of_tables, help=\
        """
        Get the number of tables.
        """
    )

    def get_number_of_triggers_in_table(self, *args):
        """
        V.get_number_of_triggers_in_table(int) -> int
        C++: int GetNumberOfTriggersInTable(int tblHandle)
        Get the number of triggers defined for a particular table.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfTriggersInTable, *args)
        return ret

    def get_option_backend_from_handle(self, *args):
        """
        V.get_option_backend_from_handle(int, int) -> string
        C++: const char *GetOptionBackendFromHandle(int tblHandle,
            int trgHandle)
        Given the handles of a table and one of its options, get the
        backend of the option.
        """
        ret = self._wrap_call(self._vtk_obj.GetOptionBackendFromHandle, *args)
        return ret

    def get_option_text_from_handle(self, *args):
        """
        V.get_option_text_from_handle(int, int) -> string
        C++: const char *GetOptionTextFromHandle(int tblHandle,
            int optHandle)
        Given the handles of a table and one of its options, return the
        text of the option.
        """
        ret = self._wrap_call(self._vtk_obj.GetOptionTextFromHandle, *args)
        return ret

    def get_preamble_action_from_handle(self, *args):
        """
        V.get_preamble_action_from_handle(int) -> string
        C++: const char *GetPreambleActionFromHandle(int preHandle)
        Given a preamble handle, get its action.
        """
        ret = self._wrap_call(self._vtk_obj.GetPreambleActionFromHandle, *args)
        return ret

    def get_preamble_backend_from_handle(self, *args):
        """
        V.get_preamble_backend_from_handle(int) -> string
        C++: const char *GetPreambleBackendFromHandle(int preHandle)
        Given a preamble handle, get its backend.
        """
        ret = self._wrap_call(self._vtk_obj.GetPreambleBackendFromHandle, *args)
        return ret

    def get_preamble_handle_from_name(self, *args):
        """
        V.get_preamble_handle_from_name(string) -> int
        C++: int GetPreambleHandleFromName(const char *preName)
        Given a preamble name, get its handle.
        """
        ret = self._wrap_call(self._vtk_obj.GetPreambleHandleFromName, *args)
        return ret

    def get_preamble_name_from_handle(self, *args):
        """
        V.get_preamble_name_from_handle(int) -> string
        C++: const char *GetPreambleNameFromHandle(int preHandle)
        Given a preamble handle, get its name.
        """
        ret = self._wrap_call(self._vtk_obj.GetPreambleNameFromHandle, *args)
        return ret

    def get_table_handle_from_name(self, *args):
        """
        V.get_table_handle_from_name(string) -> int
        C++: int GetTableHandleFromName(const char *tblName)
        Given a table name, get its handle.
        """
        ret = self._wrap_call(self._vtk_obj.GetTableHandleFromName, *args)
        return ret

    def get_table_name_from_handle(self, *args):
        """
        V.get_table_name_from_handle(int) -> string
        C++: const char *GetTableNameFromHandle(int tblHandle)
        Given a table hanlde, get its name.
        """
        ret = self._wrap_call(self._vtk_obj.GetTableNameFromHandle, *args)
        return ret

    def get_trigger_action_from_handle(self, *args):
        """
        V.get_trigger_action_from_handle(int, int) -> string
        C++: const char *GetTriggerActionFromHandle(int tblHandle,
            int trgHandle)
        Given the handles of a table and a trigger, get the action of the
        trigger.
        """
        ret = self._wrap_call(self._vtk_obj.GetTriggerActionFromHandle, *args)
        return ret

    def get_trigger_backend_from_handle(self, *args):
        """
        V.get_trigger_backend_from_handle(int, int) -> string
        C++: const char *GetTriggerBackendFromHandle(int tblHandle,
            int trgHandle)
        Given the handles of a table and a trigger, get the backend of
        the trigger.
        """
        ret = self._wrap_call(self._vtk_obj.GetTriggerBackendFromHandle, *args)
        return ret

    def get_trigger_handle_from_name(self, *args):
        """
        V.get_trigger_handle_from_name(string, string) -> int
        C++: int GetTriggerHandleFromName(const char *tblName,
            const char *trgName)
        Given the names of a trigger and a table, get the handle of the
        trigger in this table.
        """
        ret = self._wrap_call(self._vtk_obj.GetTriggerHandleFromName, *args)
        return ret

    def get_trigger_name_from_handle(self, *args):
        """
        V.get_trigger_name_from_handle(int, int) -> string
        C++: const char *GetTriggerNameFromHandle(int tblHandle,
            int trgHandle)
        Given the handles of a table and a trigger, get the name of the
        trigger.
        """
        ret = self._wrap_call(self._vtk_obj.GetTriggerNameFromHandle, *args)
        return ret

    def get_trigger_type_from_handle(self, *args):
        """
        V.get_trigger_type_from_handle(int, int) -> int
        C++: int GetTriggerTypeFromHandle(int tblHandle, int trgHandle)
        Given the handles of a table and a trigger, get the type of the
        trigger.
        """
        ret = self._wrap_call(self._vtk_obj.GetTriggerTypeFromHandle, *args)
        return ret

    def add_column_to_index(self, *args):
        """
        V.add_column_to_index(int, int, int) -> int
        C++: virtual int AddColumnToIndex(int tblHandle, int idxHandle,
            int colHandle)
        V.add_column_to_index(string, string, string) -> int
        C++: virtual int AddColumnToIndex(const char *tblName,
            const char *idxName, const char *colName)
        Add a column to a table index.
        
        The returned value is an index-column handle or -1 if an error
        occurred.
        """
        ret = self._wrap_call(self._vtk_obj.AddColumnToIndex, *args)
        return ret

    def add_column_to_table(self, *args):
        """
        V.add_column_to_table(int, int, string, int, string) -> int
        C++: virtual int AddColumnToTable(int tblHandle, int colType,
            const char *colName, int colSize, const char *colAttribs)
        V.add_column_to_table(string, int, string, int, string) -> int
        C++: virtual int AddColumnToTable(const char *tblName,
            int colType, const char *colName, int colSize,
            const char *colAttribs)
        Add a column to table.
        
        The returned value is a column handle or -1 if an error occurred.
        """
        ret = self._wrap_call(self._vtk_obj.AddColumnToTable, *args)
        return ret

    def add_index_to_table(self, *args):
        """
        V.add_index_to_table(int, int, string) -> int
        C++: virtual int AddIndexToTable(int tblHandle, int idxType,
            const char *idxName)
        V.add_index_to_table(string, int, string) -> int
        C++: virtual int AddIndexToTable(const char *tblName, int idxType,
             const char *idxName)
        Add an index to table.
        
        The returned value is an index handle or -1 if an error occurred.
        """
        ret = self._wrap_call(self._vtk_obj.AddIndexToTable, *args)
        return ret

    def add_option_to_table(self, *args):
        """
        V.add_option_to_table(int, string, string) -> int
        C++: virtual int AddOptionToTable(int tblHandle,
            const char *optStr,
            const char *optBackend=VTK_SQL_ALLBACKENDS)
        V.add_option_to_table(string, string, string) -> int
        C++: virtual int AddOptionToTable(const char *tblName,
            const char *optStr,
            const char *optBackend=VTK_SQL_ALLBACKENDS)
        Add (possibly backend-specific) text to the end of a CREATE TABLE
        (...) statement.
        
        This is most useful for specifying storage semantics of tables
        that are specific to the backend. For example, table options can
        be used to specify the TABLESPACE of a postgre_sql table or the
        ENGINE of a my_sql table.
        
        The returned value is an option handle or -1 if an error
        occurred.
        """
        ret = self._wrap_call(self._vtk_obj.AddOptionToTable, *args)
        return ret

    def add_preamble(self, *args):
        """
        V.add_preamble(string, string, string) -> int
        C++: virtual int AddPreamble(const char *preName,
            const char *preAction,
            const char *preBackend=VTK_SQL_ALLBACKENDS)
        Add a preamble to the schema This can be used, in particular, to
        create functions and/or load languages in a backend-specific
        manner. Example usage: SQLDatabaseSchema* schema =
        SQLDatabaseSchema::New(); schema->_set_name( "Example" );
        schema->_add_preamble( "drop_plpgsql", "DROP LANGUAGE IF EXISTS PLPGSQL
        CASCADE", VTK_SQL_POSTGRESQL ); schema->_add_preamble(
        "load_plpgsql", "CREATE LANGUAGE PLPGSQL", VTK_SQL_POSTGRESQL );
        schema->_add_preamble( "createsomefunction", "CREATE OR REPLACE FUNCTION somefunction() RETURNS TRIGGER AS $btable$
        " "BEGIN " "INSERT INTO btable (somevalue) VALUES (NEW.somenmbr);
        " "RETURN NEW; " "END; $btable$ LANGUAGE PLPGSQL",
         VTK_SQL_POSTGRESQL );
        """
        ret = self._wrap_call(self._vtk_obj.AddPreamble, *args)
        return ret

    def add_table(self, *args):
        """
        V.add_table(string) -> int
        C++: virtual int AddTable(const char *tblName)
        Add a table to the schema
        """
        ret = self._wrap_call(self._vtk_obj.AddTable, *args)
        return ret

    def add_table_multiple_arguments(self, *args):
        """
        V.add_table_multiple_arguments(string) -> int
        C++: int AddTableMultipleArguments(const char *tblName, ...)
        An unwrappable but useful routine to construct built-in schema.
        Example usage: int main() { SQLDatabaseSchema* schema =
        SQLDatabaseSchema::New(); schema->_set_name( "Example" );
        schema->_add_table_multiple_arguments( "atable",
        SQLDatabaseSchema::COLUMN_TOKEN,
        SQLDatabaseSchema::INTEGER, "tablekey",  0, "",
        SQLDatabaseSchema::COLUMN_TOKEN,
        SQLDatabaseSchema::VARCHAR, "somename", 11, "NOT NULL",
        SQLDatabaseSchema::COLUMN_TOKEN, SQLDatabaseSchema::BIGINT,
         "somenmbr", 17, "DEFAULT 0", SQLDatabaseSchema::INDEX_TOKEN,
        SQLDatabaseSchema::PRIMARY_KEY, "bigkey",
        SQLDatabaseSchema::INDEX_COLUMN_TOKEN, "tablekey",
        SQLDatabaseSchema::END_INDEX_TOKEN,
        SQLDatabaseSchema::INDEX_TOKEN,  SQLDatabaseSchema::UNIQUE,
        "reverselookup", SQLDatabaseSchema::INDEX_COLUMN_TOKEN,
        "somename", SQLDatabaseSchema::INDEX_COLUMN_TOKEN, "somenmbr",
        SQLDatabaseSchema::END_INDEX_TOKEN,
        SQLDatabaseSchema::TRIGGER_TOKEN, 
        SQLDatabaseSchema::AFTER_INSERT,
         "_insert_trigger", "DO NOTHING", VTK_SQL_SQLITE,
        SQLDatabaseSchema::TRIGGER_TOKEN, 
        SQLDatabaseSchema::AFTER_INSERT,
         "_insert_trigger", "FOR EACH ROW EXECUTE PROCEDURE somefunction
        ()", VTK_SQL_POSTGRESQL, SQLDatabaseSchema::TRIGGER_TOKEN, 
        SQLDatabaseSchema::AFTER_INSERT,
         "_insert_trigger", "FOR EACH ROW INSERT INTO btable SET some_value =
        new._some_nmbr", VTK_SQL_MYSQL,
        SQLDatabaseSchema::END_TABLE_TOKEN ); return 0; }
        """
        ret = self._wrap_call(self._vtk_obj.AddTableMultipleArguments, *args)
        return ret

    def add_trigger_to_table(self, *args):
        """
        V.add_trigger_to_table(int, int, string, string, string) -> int
        C++: virtual int AddTriggerToTable(int tblHandle, int trgType,
            const char *trgName, const char *trgAction,
            const char *trgBackend=VTK_SQL_ALLBACKENDS)
        V.add_trigger_to_table(string, int, string, string, string) -> int
        C++: virtual int AddTriggerToTable(const char *tblName,
            int trgType, const char *trgName, const char *trgAction,
            const char *trgBackend=VTK_SQL_ALLBACKENDS)
        Add a (possibly backend-specific) trigger action to a table.
        
        Triggers must be given unique, non-NULL names as some database
        backends require them. The returned value is a trigger handle or
        -1 if an error occurred.
        """
        ret = self._wrap_call(self._vtk_obj.AddTriggerToTable, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reset the schema to its initial, empty state.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('name', 'GetName'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SQLDatabaseSchema, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SQLDatabaseSchema properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['name']),
            title='Edit SQLDatabaseSchema properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SQLDatabaseSchema properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

