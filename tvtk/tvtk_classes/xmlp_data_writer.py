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


class XMLPDataWriter(XMLWriter):
    """
    XMLPDataWriter - Write data in a parallel XML format.
    
    Superclass: XMLWriter
    
    XMLPDataWriter is the superclass for all XML parallel data set
    writers.  It provides functionality needed for writing parallel
    formats, such as the selection of which writer writes the summary
    file and what range of pieces are assigned to each serial writer.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLPDataWriter, obj, update, **traits)
    
    write_summary_file = tvtk_base.false_bool_trait(help=\
        """
        Get/Set whether this instance of the writer should write the
        summary file that refers to all of the pieces' individual files.
        Default is yes only for piece 0 writer.
        """
    )
    def _write_summary_file_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteSummaryFile,
                        self.write_summary_file_)

    start_piece = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the range of pieces assigned to this writer.
        """
    )
    def _start_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartPiece,
                        self.start_piece)

    ghost_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the ghost level used for this writer's piece.
        """
    )
    def _ghost_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGhostLevel,
                        self.ghost_level)

    number_of_pieces = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Get/Set the number of pieces that are being written in parallel.
        """
    )
    def _number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPieces,
                        self.number_of_pieces)

    end_piece = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the range of pieces assigned to this writer.
        """
    )
    def _end_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndPiece,
                        self.end_piece)

    _updateable_traits_ = \
    (('ghost_level', 'GetGhostLevel'), ('byte_order', 'GetByteOrder'),
    ('write_summary_file', 'GetWriteSummaryFile'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('end_piece',
    'GetEndPiece'), ('file_name', 'GetFileName'), ('abort_execute',
    'GetAbortExecute'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('data_mode', 'GetDataMode'), ('start_piece',
    'GetStartPiece'), ('time_step_range', 'GetTimeStepRange'),
    ('number_of_time_steps', 'GetNumberOfTimeSteps'),
    ('encode_appended_data', 'GetEncodeAppendedData'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress',
    'GetProgress'), ('reference_count', 'GetReferenceCount'),
    ('time_step', 'GetTimeStep'), ('block_size', 'GetBlockSize'),
    ('number_of_pieces', 'GetNumberOfPieces'), ('id_type', 'GetIdType'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'encode_appended_data',
    'global_warning_display', 'release_data_flag', 'write_summary_file',
    'byte_order', 'data_mode', 'id_type', 'block_size', 'end_piece',
    'file_name', 'ghost_level', 'number_of_pieces',
    'number_of_time_steps', 'progress_text', 'start_piece', 'time_step',
    'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLPDataWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLPDataWriter properties', scrollable=True, resizable=True,
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
            title='Edit XMLPDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLPDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

