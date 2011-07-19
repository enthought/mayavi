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

from tvtk.tvtk_classes.composite_data_set import CompositeDataSet


class MultiPieceDataSet(CompositeDataSet):
    """
    MultiPieceDataSet - composite dataset to encapsulates pieces of
    
    Superclass: CompositeDataSet
    
    A MultiPieceDataSet dataset groups multiple data pieces together.
    For example, say that a simulation broke a volume into 16 piece so
    that each piece can be processed with 1 process in parallel. We want
    to load this volume in a visualization cluster of 4 nodes. Each node
    will get 4 pieces, not necessarily forming a whole rectangular piece.
    In this case, it is not possible to append the 4 pieces together into
    a ImageData. In this case, these 4 pieces can be collected
    together using a MultiPieceDataSet. Note that MultiPieceDataSet
    is intended to be included in other composite datasets eg.
    MultiBlockDataSet, HierarchicalBoxDataSet. Hence the lack of
    algorithms producting MultiPieceDataSet.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMultiPieceDataSet, obj, update, **traits)
    
    def get_piece(self, *args):
        """
        V.get_piece(int) -> DataSet
        C++: DataSet *GetPiece(unsigned int pieceno)
        Returns the piece at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetPiece, *args)
        return wrap_vtk(ret)

    def set_piece(self, *args):
        """
        V.set_piece(int, DataObject)
        C++: void SetPiece(unsigned int pieceno, DataObject *piece)
        Sets the data object as the given piece. The total number of
        pieces will be resized to fit the requested piece no.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPiece, *my_args)
        return ret

    number_of_pieces = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of pieces. This will cause allocation if the new
        number of pieces is greater than the current size. All new pieces
        are initialized to null.
        """
    )
    def _number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPieces,
                        self.number_of_pieces)

    def get_piece_as_data_object(self, *args):
        """
        V.get_piece_as_data_object(int) -> DataObject
        C++: DataObject *GetPieceAsDataObject(unsigned int pieceno)
        Returns the piece at the given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetPieceAsDataObject, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('request_exact_extent', 'GetRequestExactExtent'),
    ('update_number_of_pieces', 'GetUpdateNumberOfPieces'),
    ('maximum_number_of_pieces', 'GetMaximumNumberOfPieces'),
    ('update_ghost_level', 'GetUpdateGhostLevel'), ('update_extent',
    'GetUpdateExtent'), ('debug', 'GetDebug'), ('release_data_flag',
    'GetReleaseDataFlag'), ('global_release_data_flag',
    'GetGlobalReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('whole_extent', 'GetWholeExtent'), ('number_of_pieces',
    'GetNumberOfPieces'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'number_of_pieces', 'update_extent',
    'update_ghost_level', 'update_number_of_pieces', 'update_piece',
    'whole_bounding_box', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MultiPieceDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MultiPieceDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit MultiPieceDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MultiPieceDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

