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


class TableToArray(ArrayDataAlgorithm):
    """
    TableToArray - converts a Table to a matrix.
    
    Superclass: ArrayDataAlgorithm
    
    Converts a Table into a dense matrix.  Use add_column() to
    designate one-to-many table columns that will become columns in the
    output matrix.a
    
    Using add_column() it is possible to duplicate / reorder columns in
    arbitrary ways.
    
    Caveats:
    
    Only produces DenseArray, regardless of the input table column
    types.
    
    Thanks:
    
    Developed by Timothy M. Shead (tshead@sandia.gov) at Sandia National
    Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableToArray, obj, update, **traits)
    
    def add_all_columns(self):
        """
        V.add_all_columns()
        C++: void AddAllColumns()
        Add every input table column to the output matrix.
        """
        ret = self._vtk_obj.AddAllColumns()
        return ret
        

    def add_column(self, *args):
        """
        V.add_column(string)
        C++: void AddColumn(const char *name)
        V.add_column(int)
        C++: void AddColumn(IdType index)
        Add a column by name to the list of input table columns that will
        be mapped to columns in the output matrix.
        """
        ret = self._wrap_call(self._vtk_obj.AddColumn, *args)
        return ret

    def clear_columns(self):
        """
        V.clear_columns()
        C++: void ClearColumns()
        Reset the list of input table columns that will be mapped to
        columns in the output matrix.
        """
        ret = self._vtk_obj.ClearColumns()
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
            return super(TableToArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TableToArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit TableToArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableToArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

