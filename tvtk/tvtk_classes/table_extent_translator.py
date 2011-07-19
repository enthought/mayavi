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

from tvtk.tvtk_classes.extent_translator import ExtentTranslator


class TableExtentTranslator(ExtentTranslator):
    """
    TableExtentTranslator - Extent translation through lookup table.
    
    Superclass: ExtentTranslator
    
    TableExtentTranslator provides a ExtentTranslator that is
    programmed with a specific extent corresponding to each piece number.
     Readers can provide this to an application to allow the pipeline to
    execute using the same piece breakdown that is provided in the input
    file.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableExtentTranslator, obj, update, **traits)
    
    number_of_pieces_in_table = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the real number of pieces in the extent table.
        """
    )
    def _number_of_pieces_in_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPiecesInTable,
                        self.number_of_pieces_in_table)

    maximum_ghost_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the maximum ghost level that can be requested.  This can be
        used by a reader to make sure an extent request does not go
        outside the boundaries of the piece's file.
        """
    )
    def _maximum_ghost_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumGhostLevel,
                        self.maximum_ghost_level)

    def get_piece_available(self, *args):
        """
        V.get_piece_available(int) -> int
        C++: virtual int GetPieceAvailable(int piece)
        Get/Set whether the given piece is available.  Requesting a piece
        that is not available will produce errors in the pipeline.
        """
        ret = self._wrap_call(self._vtk_obj.GetPieceAvailable, *args)
        return ret

    def set_piece_available(self, *args):
        """
        V.set_piece_available(int, int)
        C++: virtual void SetPieceAvailable(int piece, int available)
        Get/Set whether the given piece is available.  Requesting a piece
        that is not available will produce errors in the pipeline.
        """
        ret = self._wrap_call(self._vtk_obj.SetPieceAvailable, *args)
        return ret

    _updateable_traits_ = \
    (('whole_extent', 'GetWholeExtent'), ('maximum_ghost_level',
    'GetMaximumGhostLevel'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_pieces_in_table',
    'GetNumberOfPiecesInTable'), ('debug', 'GetDebug'), ('extent',
    'GetExtent'), ('reference_count', 'GetReferenceCount'),
    ('ghost_level', 'GetGhostLevel'), ('piece', 'GetPiece'),
    ('number_of_pieces', 'GetNumberOfPieces'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'extent', 'ghost_level',
    'maximum_ghost_level', 'number_of_pieces',
    'number_of_pieces_in_table', 'piece', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableExtentTranslator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TableExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['extent', 'ghost_level',
            'maximum_ghost_level', 'number_of_pieces',
            'number_of_pieces_in_table', 'piece', 'whole_extent']),
            title='Edit TableExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableExtentTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

