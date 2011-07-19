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

from tvtk.tvtk_classes.xml_composite_data_writer import XMLCompositeDataWriter


class XMLMultiBlockDataWriter(XMLCompositeDataWriter):
    """
    XMLMultiBlockDataWriter - writer for MultiBlockDataSet.
    
    Superclass: XMLCompositeDataWriter
    
    XMLMultiBlockDataWriter is a XMLCompositeDataWriter subclass to
    handle MultiBlockDataSet.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLMultiBlockDataWriter, obj, update, **traits)
    
    _updateable_traits_ = \
    (('byte_order', 'GetByteOrder'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('time_step', 'GetTimeStep'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('data_mode', 'GetDataMode'), ('id_type',
    'GetIdType'), ('time_step_range', 'GetTimeStepRange'),
    ('number_of_time_steps', 'GetNumberOfTimeSteps'), ('progress',
    'GetProgress'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('write_meta_file', 'GetWriteMetaFile'), ('reference_count',
    'GetReferenceCount'), ('ghost_level', 'GetGhostLevel'), ('block_size',
    'GetBlockSize'), ('abort_execute', 'GetAbortExecute'),
    ('encode_appended_data', 'GetEncodeAppendedData'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'encode_appended_data',
    'global_warning_display', 'release_data_flag', 'byte_order',
    'data_mode', 'id_type', 'block_size', 'file_name', 'ghost_level',
    'number_of_time_steps', 'progress_text', 'time_step',
    'time_step_range', 'write_meta_file'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLMultiBlockDataWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLMultiBlockDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['encode_appended_data'], ['byte_order', 'data_mode',
            'id_type'], ['block_size', 'file_name', 'ghost_level',
            'number_of_time_steps', 'time_step', 'time_step_range',
            'write_meta_file']),
            title='Edit XMLMultiBlockDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLMultiBlockDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

