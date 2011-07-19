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

from tvtk.tvtk_classes.xmlp_data_writer import XMLPDataWriter


class XMLPUnstructuredDataWriter(XMLPDataWriter):
    """
    XMLPUnstructuredDataWriter - Superclass for PVTK XML unstructured
    data writers.
    
    Superclass: XMLPDataWriter
    
    XMLPUnstructuredDataWriter provides PVTK XML writing functionality
    that is common among all the parallel unstructured data formats.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLPUnstructuredDataWriter, obj, update, **traits)
    
    _updateable_traits_ = \
    (('id_type', 'GetIdType'), ('byte_order', 'GetByteOrder'),
    ('write_summary_file', 'GetWriteSummaryFile'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('time_step', 'GetTimeStep'), ('abort_execute',
    'GetAbortExecute'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('data_mode', 'GetDataMode'), ('start_piece',
    'GetStartPiece'), ('time_step_range', 'GetTimeStepRange'),
    ('number_of_time_steps', 'GetNumberOfTimeSteps'), ('progress',
    'GetProgress'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('end_piece', 'GetEndPiece'), ('reference_count',
    'GetReferenceCount'), ('ghost_level', 'GetGhostLevel'), ('block_size',
    'GetBlockSize'), ('number_of_pieces', 'GetNumberOfPieces'),
    ('encode_appended_data', 'GetEncodeAppendedData'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'encode_appended_data',
    'global_warning_display', 'release_data_flag', 'write_summary_file',
    'byte_order', 'data_mode', 'id_type', 'block_size', 'end_piece',
    'file_name', 'ghost_level', 'number_of_pieces',
    'number_of_time_steps', 'progress_text', 'start_piece', 'time_step',
    'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLPUnstructuredDataWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLPUnstructuredDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['encode_appended_data', 'write_summary_file'],
            ['byte_order', 'data_mode', 'id_type'], ['block_size', 'end_piece',
            'file_name', 'ghost_level', 'number_of_pieces',
            'number_of_time_steps', 'start_piece', 'time_step',
            'time_step_range']),
            title='Edit XMLPUnstructuredDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLPUnstructuredDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

