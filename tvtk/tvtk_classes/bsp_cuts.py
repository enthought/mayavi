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


class BSPCuts(DataObject):
    """
    BSPCuts - This class represents an axis-aligned Binary Spatial 
    
    Superclass: DataObject
    
    This class converts between the KdTree
       representation of a tree of KdNodes (used by
    DistributedDataFilter)
       and a compact array representation that might be provided by a
       graph partitioning library like Zoltan.  Such a representation
       could be used in message passing.
    
    See Also:
    
    
         KdTree KdNode DistributedDataFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBSPCuts, obj, update, **traits)
    
    def _get_kd_node_tree(self):
        return wrap_vtk(self._vtk_obj.GetKdNodeTree())
    kd_node_tree = traits.Property(_get_kd_node_tree, help=\
        """
        Return a tree of KdNode's representing the cuts specified
          in this object.  This is our copy, don't delete it.
        """
    )

    def _get_number_of_cuts(self):
        return self._vtk_obj.GetNumberOfCuts()
    number_of_cuts = traits.Property(_get_number_of_cuts, help=\
        """
        Get the number of cuts in the partitioning, which also the size
        of
          the arrays in the array representation of the partitioning.
        """
    )

    def create_cuts(self, *args):
        """
        V.create_cuts(KdNode)
        C++: void CreateCuts(KdNode *kd)
        Initialize the cuts from a tree of KdNode's
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateCuts, *my_args)
        return ret

    def equals(self, *args):
        """
        V.equals(BSPCuts, float) -> int
        C++: int Equals(BSPCuts *other, double tolerance=0.0)
        Compare these cuts with those of the other tree.  Returns true if
        the two trees are the same.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Equals, *my_args)
        return ret

    def print_arrays(self):
        """
        V.print_arrays()
        C++: void PrintArrays()"""
        ret = self._vtk_obj.PrintArrays()
        return ret
        

    def print_tree(self):
        """
        V.print_tree()
        C++: void PrintTree()"""
        ret = self._vtk_obj.PrintTree()
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
            return super(BSPCuts, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BSPCuts properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit BSPCuts properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BSPCuts properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

