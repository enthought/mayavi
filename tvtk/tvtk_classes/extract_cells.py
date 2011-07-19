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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class ExtractCells(UnstructuredGridAlgorithm):
    """
    ExtractCells - subset a DataSet to create a UnstructuredGrid
    
    Superclass: UnstructuredGridAlgorithm
    
    Given a DataSet and a list of cell Ids, create a
    UnstructuredGrid
       composed of these cells.  If the cell list is empty when
    ExtractCells
       executes, it will set up the ugrid, point and cell arrays, with no
    points,
       cells or data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractCells, obj, update, **traits)
    
    def add_cell_list(self, *args):
        """
        V.add_cell_list(IdList)
        C++: void AddCellList(IdList *l)
        Add the supplied list of cell IDs to those that will be included
        in the output UnstructuredGrid.
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.AddCellList, *my_args)
        return ret

    def add_cell_range(self, *args):
        """
        V.add_cell_range(int, int)
        C++: void AddCellRange(IdType from, IdType to)
        Add this range of cell IDs to those that will be included in the
        output UnstructuredGrid.
        """
        ret = self._wrap_call(self._vtk_obj.AddCellRange, *args)
        return ret

    def set_cell_list(self, *args):
        """
        V.set_cell_list(IdList)
        C++: void SetCellList(IdList *l)
        Set the list of cell IDs that the output UnstructuredGrid will
        be composed of.  Replaces any other cell ID list supplied so far.
         (Set to NULL to free memory used by cell list.)
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.SetCellList, *my_args)
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
            return super(ExtractCells, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractCells properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ExtractCells properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractCells properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

