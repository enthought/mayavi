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


class Selection(DataObject):
    """
    Selection - A node in a selection tree. Used to store selection
    results.
    
    Superclass: DataObject
    
    See Also:
    
    SelectionNode
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSelection, obj, update, **traits)
    
    def get_node(self, *args):
        """
        V.get_node(int) -> SelectionNode
        C++: virtual SelectionNode *GetNode(unsigned int idx)
        Returns a node given it's index. Performs bound checking and will
        return 0 if out-of-bounds.
        """
        ret = self._wrap_call(self._vtk_obj.GetNode, *args)
        return wrap_vtk(ret)

    def _get_number_of_nodes(self):
        return self._vtk_obj.GetNumberOfNodes()
    number_of_nodes = traits.Property(_get_number_of_nodes, help=\
        """
        Returns the number of nodes in this selection. Each node contains
        information about part of the selection.
        """
    )

    def add_node(self, *args):
        """
        V.add_node(SelectionNode)
        C++: virtual void AddNode(SelectionNode *)
        Adds a selection node.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddNode, *my_args)
        return ret

    def dump(self):
        """
        V.dump()
        C++: virtual void Dump()
        Dumps the contents of the selection, giving basic information
        only.
        """
        ret = self._vtk_obj.Dump()
        return ret
        

    def remove_all_nodes(self):
        """
        V.remove_all_nodes()
        C++: virtual void RemoveAllNodes()
        Removes a selection node.
        """
        ret = self._vtk_obj.RemoveAllNodes()
        return ret
        

    def remove_node(self, *args):
        """
        V.remove_node(int)
        C++: virtual void RemoveNode(unsigned int idx)
        V.remove_node(SelectionNode)
        C++: virtual void RemoveNode(SelectionNode *)
        Removes a selection node.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveNode, *my_args)
        return ret

    def union(self, *args):
        """
        V.union(Selection)
        C++: virtual void Union(Selection *selection)
        V.union(SelectionNode)
        C++: virtual void Union(SelectionNode *node)
        Union this selection with the specified selection. Attempts to
        reuse selection nodes in this selection if properties match
        exactly. Otherwise, creates new selection nodes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Union, *my_args)
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
            return super(Selection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Selection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit Selection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Selection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

