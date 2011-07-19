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


class InEdgeIterator(Object):
    """
    InEdgeIterator - Iterates through all incoming edges to a vertex.
    
    Superclass: Object
    
    InEdgeIterator iterates through all edges whose target is a
    particular vertex. Instantiate this class directly and call
    Initialize() to traverse the vertex of a graph. Alternately, use
    get_in_edges() on the graph to initialize the iterator. it->Next()
    returns a InEdgeType structure, which contains Id, the edge's id, and Source, the
    edge's source vertex.
    
    See Also:
    
    Graph OutEdgeIterator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInEdgeIterator, obj, update, **traits)
    
    def _get_graph(self):
        return wrap_vtk(self._vtk_obj.GetGraph())
    graph = traits.Property(_get_graph, help=\
        """
        Get the graph and vertex associated with this iterator.
        """
    )

    def _get_vertex(self):
        return self._vtk_obj.GetVertex()
    vertex = traits.Property(_get_vertex, help=\
        """
        Get the graph and vertex associated with this iterator.
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
        

    def initialize(self, *args):
        """
        V.initialize(Graph, int)
        C++: void Initialize(Graph *g, IdType v)
        Initialize the iterator with a graph and vertex.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
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
            return super(InEdgeIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InEdgeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit InEdgeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InEdgeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

