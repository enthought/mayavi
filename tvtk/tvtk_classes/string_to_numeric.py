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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class StringToNumeric(DataObjectAlgorithm):
    """
    StringToNumeric - Converts string arrays to numeric arrays
    
    Superclass: DataObjectAlgorithm
    
    StringToNumeric is a filter for converting a string array into a
    numeric arrays.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStringToNumeric, obj, update, **traits)
    
    convert_edge_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert edge data arrays.  Default is on.
        """
    )
    def _convert_edge_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertEdgeData,
                        self.convert_edge_data_)

    convert_vertex_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert vertex data arrays.  Default is on.
        """
    )
    def _convert_vertex_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertVertexData,
                        self.convert_vertex_data_)

    convert_row_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert row data arrays.  Default is on.
        """
    )
    def _convert_row_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertRowData,
                        self.convert_row_data_)

    convert_point_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert cell data arrays.  Default is on.
        """
    )
    def _convert_point_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertPointData,
                        self.convert_point_data_)

    convert_cell_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert point data arrays.  Default is on.
        """
    )
    def _convert_cell_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertCellData,
                        self.convert_cell_data_)

    convert_field_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert field data arrays.  Default is on.
        """
    )
    def _convert_field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertFieldData,
                        self.convert_field_data_)

    _updateable_traits_ = \
    (('convert_edge_data', 'GetConvertEdgeData'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('progress_text', 'GetProgressText'),
    ('convert_field_data', 'GetConvertFieldData'), ('convert_cell_data',
    'GetConvertCellData'), ('convert_point_data', 'GetConvertPointData'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('convert_vertex_data', 'GetConvertVertexData'), ('convert_row_data',
    'GetConvertRowData'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'convert_cell_data', 'convert_edge_data',
    'convert_field_data', 'convert_point_data', 'convert_row_data',
    'convert_vertex_data', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StringToNumeric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StringToNumeric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['convert_cell_data', 'convert_edge_data',
            'convert_field_data', 'convert_point_data', 'convert_row_data',
            'convert_vertex_data'], [], []),
            title='Edit StringToNumeric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StringToNumeric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

