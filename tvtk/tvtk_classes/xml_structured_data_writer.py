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

from tvtk.tvtk_classes.xml_writer import XMLWriter


class XMLStructuredDataWriter(XMLWriter):
    """
    XMLStructuredDataWriter - Superclass for VTK XML structured data
    writers.
    
    Superclass: XMLWriter
    
    XMLStructuredDataWriter provides VTK XML writing functionality
    that is common among all the structured data formats.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLStructuredDataWriter, obj, update, **traits)
    
    def _get_extent_translator(self):
        return wrap_vtk(self._vtk_obj.GetExtentTranslator())
    def _set_extent_translator(self, arg):
        old_val = self._get_extent_translator()
        self._wrap_call(self._vtk_obj.SetExtentTranslator,
                        deref_vtk(arg))
        self.trait_property_changed('extent_translator', old_val, arg)
    extent_translator = traits.Property(_get_extent_translator, _set_extent_translator, help=\
        """
        Get/Set the extent translator used for streaming.
        """
    )

    number_of_pieces = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Get/Set the number of pieces used to stream the image through the
        pipeline while writing to the file.
        """
    )
    def _number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPieces,
                        self.number_of_pieces)

    write_extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _write_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteExtent,
                        self.write_extent)

    _updateable_traits_ = \
    (('byte_order', 'GetByteOrder'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('abort_execute', 'GetAbortExecute'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('data_mode',
    'GetDataMode'), ('time_step_range', 'GetTimeStepRange'),
    ('number_of_time_steps', 'GetNumberOfTimeSteps'),
    ('encode_appended_data', 'GetEncodeAppendedData'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress',
    'GetProgress'), ('reference_count', 'GetReferenceCount'),
    ('time_step', 'GetTimeStep'), ('block_size', 'GetBlockSize'),
    ('write_extent', 'GetWriteExtent'), ('number_of_pieces',
    'GetNumberOfPieces'), ('id_type', 'GetIdType'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'encode_appended_data',
    'global_warning_display', 'release_data_flag', 'byte_order',
    'data_mode', 'id_type', 'block_size', 'file_name', 'number_of_pieces',
    'number_of_time_steps', 'progress_text', 'time_step',
    'time_step_range', 'write_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLStructuredDataWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLStructuredDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['encode_appended_data'], ['byte_order', 'data_mode',
            'id_type'], ['block_size', 'file_name', 'number_of_pieces',
            'number_of_time_steps', 'time_step', 'time_step_range',
            'write_extent']),
            title='Edit XMLStructuredDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLStructuredDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

