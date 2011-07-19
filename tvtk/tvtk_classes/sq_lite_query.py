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

from tvtk.tvtk_classes.sql_query import SQLQuery


class SQLiteQuery(SQLQuery):
    """
    SQLiteQuery - SQLQuery implementation for SQLite databases
    
    Superclass: SQLQuery
    
    This is an implementation of SQLQuery for SQLite databases.  See
    the documentation for SQLQuery for information about what the
    methods do.
    
    Bugs:
    
    Sometimes Execute() will return false (meaning an error) but
    get_last_error_text() winds up null.  I am not certain why this is
    happening.
    
    Thanks:
    
    Thanks to Andrew Wilson from Sandia National Laboratories for
    implementing this class.
    
    See Also:
    
    SQLDatabase SQLQuery SQLiteDatabase
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSQLiteQuery, obj, update, **traits)
    
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
            return super(SQLiteQuery, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SQLiteQuery properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['case_sensitive_field_names'], [], ['query']),
            title='Edit SQLiteQuery properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SQLiteQuery properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

