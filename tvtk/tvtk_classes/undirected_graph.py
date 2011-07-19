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

from tvtk.tvtk_classes.graph import Graph


class UndirectedGraph(Graph):
    """
    UndirectedGraph - An undirected graph.
    
    Superclass: Graph
    
    UndirectedGraph is a collection of vertices along with a
    collection of undirected edges (they connect two vertices in no
    particular order). shallow_copy(), deep_copy(), checked_shallow_copy(),
    checked_deep_copy() accept instances of UndirectedGraph and
    MutableUndirectedGraph. get_out_edges(v, it) and get_in_edges(v, it)
    return the same list of edges, which is the list of all edges which
    have a v as an endpoint. get_in_degree(v), get_out_degree(v) and
    get_degree(v) all return the full degree of vertex v.
    
    UndirectedGraph is read-only. To create an undirected graph, use
    an instance of MutableUndirectedGraph, then you may set the
    structure to a UndirectedGraph using shallow_copy().
    
    See Also:
    
    Graph MutableUndirectedGraph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUndirectedGraph, obj, update, **traits)
    
    def is_structure_valid(self, *args):
        """
        V.is_structure_valid(Graph) -> bool
        C++: virtual bool IsStructureValid(Graph *g)
        Check the structure, and accept it if it is a valid undirected
        graph. This is public to allow the to_directed/_undirected_graph to
        work.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsStructureValid, *my_args)
        return ret

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('update_number_of_pieces',
    'GetUpdateNumberOfPieces'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('update_ghost_level',
    'GetUpdateGhostLevel'), ('update_extent', 'GetUpdateExtent'),
    ('debug', 'GetDebug'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('global_release_data_flag', 'GetGlobalReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('whole_extent',
    'GetWholeExtent'), ('request_exact_extent', 'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
    'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UndirectedGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UndirectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit UndirectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UndirectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

