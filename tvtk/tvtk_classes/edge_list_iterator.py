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

from tvtk.tvtk_classes.object import Object


class EdgeListIterator(Object):
    """
    EdgeListIterator - Iterates through all edges in a graph.
    
    Superclass: Object
    
    EdgeListIterator iterates through all the edges in a graph, by
    traversing the adjacency list for each vertex. You may instantiate
    this class directly and call set_graph() to traverse a certain graph.
    You may also call the graph's get_edges() method to set up the
    iterator for a certain graph.
    
    Note that this class does NOT guarantee that the edges will be
    processed in order of their ids (i.e. it will not necessarily return
    edge 0, then edge 1, etc.).
    
    See Also:
    
    Graph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEdgeListIterator, obj, update, **traits)
    
    def _get_graph(self):
        return wrap_vtk(self._vtk_obj.GetGraph())
    def _set_graph(self, arg):
        old_val = self._get_graph()
        self._wrap_call(self._vtk_obj.SetGraph,
                        deref_vtk(arg))
        self.trait_property_changed('graph', old_val, arg)
    graph = traits.Property(_get_graph, _set_graph, help=\
        """
        
        """
    )

    def has_next(self):
        """
        V.has_next() -> bool
        C++: bool HasNext()
        Whether this iterator has more edges.
        """
        ret = self._vtk_obj.HasNext()
        return ret
        

    def next_graph_edge(self):
        """
        V.next_graph_edge() -> GraphEdge
        C++: GraphEdge *NextGraphEdge()
        Just like Next(), but returns heavy-weight GraphEdge object
        instead of the EdgeType struct, for use with wrappers. The
        graph edge is owned by this iterator, and changes after each call
        to next_graph_edge().
        """
        ret = wrap_vtk(self._vtk_obj.NextGraphEdge())
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EdgeListIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit EdgeListIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit EdgeListIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EdgeListIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

