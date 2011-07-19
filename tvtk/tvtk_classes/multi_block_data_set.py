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


class MultiBlockDataSet(CompositeDataSet):
    """
    MultiBlockDataSet - Composite dataset that organizes datasets into
    
    Superclass: CompositeDataSet
    
    MultiBlockDataSet is a CompositeDataSet that stores a hierarchy
    of datasets. The dataset collection consists of multiple blocks. Each
     block can itself be a MultiBlockDataSet, thus providing for a
    full tree structure. Sub-blocks are usually used to distribute blocks
    across processors. For example, a 1 block dataset can be distributed
    as following:
     proc 0:
     Block 0:
       * ds 0
       * (null)
    
     proc 1:
     Block 0:
       * (null)
       * ds 1
     
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMultiBlockDataSet, obj, update, **traits)
    
    number_of_blocks = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of blocks. This will cause allocation if the new
        number of blocks is greater than the current size. All new blocks
        are initialized to null.
        """
    )
    def _number_of_blocks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfBlocks,
                        self.number_of_blocks)

    def get_block(self, *args):
        """
        V.get_block(int) -> DataObject
        C++: DataObject *GetBlock(unsigned int blockno)
        Returns the block at the given index. It is recommended that one
        uses the iterators to iterate over composite datasets rather than
        using this API.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlock, *args)
        return wrap_vtk(ret)

    def set_block(self, *args):
        """
        V.set_block(int, DataObject)
        C++: void SetBlock(unsigned int blockno, DataObject *block)
        Sets the data object as the given block. The total number of
        blocks will be resized to fit the requested block no.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetBlock, *my_args)
        return ret

    def remove_block(self, *args):
        """
        V.remove_block(int)
        C++: void RemoveBlock(unsigned int blockno)
        Remove the given block from the dataset.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveBlock, *args)
        return ret

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('update_number_of_pieces',
    'GetUpdateNumberOfPieces'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('update_ghost_level',
    'GetUpdateGhostLevel'), ('global_release_data_flag',
    'GetGlobalReleaseDataFlag'), ('update_extent', 'GetUpdateExtent'),
    ('debug', 'GetDebug'), ('number_of_blocks', 'GetNumberOfBlocks'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('whole_extent', 'GetWholeExtent'),
    ('request_exact_extent', 'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'number_of_blocks', 'update_extent',
    'update_ghost_level', 'update_number_of_pieces', 'update_piece',
    'whole_bounding_box', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MultiBlockDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MultiBlockDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'number_of_blocks', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit MultiBlockDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MultiBlockDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

