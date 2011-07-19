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

from tvtk.tvtk_classes.data_object import DataObject


class CompositeDataSet(DataObject):
    """
    CompositeDataSet - abstract superclass for composite 
    
    Superclass: DataObject
    
    CompositeDataSet is an abstract class that represents a collection
    of datasets (including other composite datasets). It provides an
    interface to access the datasets through iterators.
    CompositeDataSet provides methods that are used by subclasses to
    store the datasets. CompositeDataSet provides the datastructure
    for a full tree representation. Subclasses provide the semantics for
    it and control how this tree is built.
    
    See Also:
    
    CompositeDataIterator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositeDataSet, obj, update, **traits)
    
    def get_data_set(self, *args):
        """
        V.get_data_set(CompositeDataIterator) -> DataObject
        C++: virtual DataObject *GetDataSet(
            CompositeDataIterator *iter)
        Returns the dataset located at the positiong pointed by the
        iterator. The iterator does not need to be iterating over this
        dataset itself. It can be an iterator for composite dataset with
        similar structure (achieved by using copy_structure).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDataSet, *my_args)
        return wrap_vtk(ret)

    def set_data_set(self, *args):
        """
        V.set_data_set(CompositeDataIterator, DataObject)
        C++: virtual void SetDataSet(CompositeDataIterator *iter,
            DataObject *dataObj)
        Sets the data set at the location pointed by the iterator. The
        iterator does not need to be iterating over this dataset itself.
        It can be any composite datasite with similar structure (achieved
        by using copy_structure).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataSet, *my_args)
        return ret

    def get_meta_data(self, *args):
        """
        V.get_meta_data(CompositeDataIterator) -> Information
        C++: virtual Information *GetMetaData(
            CompositeDataIterator *iter)
        Returns the meta-data associated with the position pointed by the
        iterator. This will create a new Information object if none
        already exists. Use has_meta_data to avoid creating the
        Information object unnecessarily. The iterator does not need
        to be iterating over this dataset itself. It can be an iterator
        for composite dataset with similar structure (achieved by using
        copy_structure).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetMetaData, *my_args)
        return wrap_vtk(ret)

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Returns the total number of points of all blocks. This will
        iterate over all blocks and call get_number_of_points() so it might
        be expansive.
        """
    )

    def copy_structure(self, *args):
        """
        V.copy_structure(CompositeDataSet)
        C++: virtual void CopyStructure(CompositeDataSet *input)
        Copies the tree structure from the input. All pointers to
        non-composite data objects are intialized to NULL. This also
        shallow copies the meta data associated with all the nodes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyStructure, *my_args)
        return ret

    def has_meta_data(self, *args):
        """
        V.has_meta_data(CompositeDataIterator) -> int
        C++: virtual int HasMetaData(CompositeDataIterator *iter)
        Returns if any meta-data associated with the position pointed by
        the iterator. The iterator does not need to be iterating over
        this dataset itself. It can be an iterator for composite dataset
        with similar structure (achieved by using copy_structure).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasMetaData, *my_args)
        return ret

    def NAME(self):
        """
        V.name() -> InformationStringKey
        C++: static InformationStringKey *NAME()
        Key used to put node name in the meta-data associated with a
        node.
        """
        ret = wrap_vtk(self._vtk_obj.NAME())
        return ret
        

    def new_iterator(self):
        """
        V.new_iterator() -> CompositeDataIterator
        C++: virtual CompositeDataIterator *NewIterator()
        Return a new iterator (the iterator has to be deleted by user).
        """
        ret = wrap_vtk(self._vtk_obj.NewIterator())
        return ret
        

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('whole_extent', 'GetWholeExtent'),
    ('update_number_of_pieces', 'GetUpdateNumberOfPieces'),
    ('update_ghost_level', 'GetUpdateGhostLevel'), ('update_extent',
    'GetUpdateExtent'), ('debug', 'GetDebug'), ('release_data_flag',
    'GetReleaseDataFlag'), ('global_release_data_flag',
    'GetGlobalReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('maximum_number_of_pieces', 'GetMaximumNumberOfPieces'),
    ('request_exact_extent', 'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
    'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompositeDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositeDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit CompositeDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositeDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

