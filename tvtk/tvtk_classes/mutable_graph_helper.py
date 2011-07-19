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


class MutableGraphHelper(Object):
    """
    MutableGraphHelper - Helper class for building a directed or
    
    Superclass: Object
    
    MutableGraphHelper has helper methods add_vertex and add_edge which
    add vertices/edges to the underlying mutable graph. This is helpful
    in filters which need to (re)construct graphs which may be either
    directed or undirected.
    
    See Also:
    
    Graph MutableDirectedGraph MutableUndirectedGraph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMutableGraphHelper, obj, update, **traits)
    
    def _get_graph(self):
        return wrap_vtk(self._vtk_obj.GetGraph())
    def _set_graph(self, arg):
        old_val = self._get_graph()
        self._wrap_call(self._vtk_obj.SetGraph,
                        deref_vtk(arg))
        self.trait_property_changed('graph', old_val, arg)
    graph = traits.Property(_get_graph, _set_graph, help=\
        """
        Set the underlying graph that you want to modify with this
        helper. The graph must be an instance of MutableDirectedGraph
        or MutableUndirectedGraph.
        """
    )

    def add_graph_edge(self, *args):
        """
        V.add_graph_edge(int, int) -> GraphEdge
        C++: GraphEdge *AddGraphEdge(IdType u, IdType v)
        Add an edge to the underlying mutable graph.
        """
        ret = self._wrap_call(self._vtk_obj.AddGraphEdge, *args)
        return wrap_vtk(ret)

    def add_vertex(self):
        """
        V.add_vertex() -> int
        C++: IdType AddVertex()
        Add a vertex to the underlying mutable graph.
        """
        ret = self._vtk_obj.AddVertex()
        return ret
        

    def remove_edge(self, *args):
        """
        V.remove_edge(int)
        C++: void RemoveEdge(IdType e)
        Remove an edge from the underlying mutable graph.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveEdge, *args)
        return ret

    def remove_edges(self, *args):
        """
        V.remove_edges(IdTypeArray)
        C++: void RemoveEdges(IdTypeArray *edges)
        Remove a collection of edges from the underlying mutable graph.
        """
        my_args = deref_array(args, [['vtkIdTypeArray']])
        ret = self._wrap_call(self._vtk_obj.RemoveEdges, *my_args)
        return ret

    def remove_vertex(self, *args):
        """
        V.remove_vertex(int)
        C++: void RemoveVertex(IdType v)
        Remove a vertex from the underlying mutable graph.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveVertex, *args)
        return ret

    def remove_vertices(self, *args):
        """
        V.remove_vertices(IdTypeArray)
        C++: void RemoveVertices(IdTypeArray *verts)
        Remove a collection of vertices from the underlying mutable
        graph.
        """
        my_args = deref_array(args, [['vtkIdTypeArray']])
        ret = self._wrap_call(self._vtk_obj.RemoveVertices, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MutableGraphHelper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MutableGraphHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit MutableGraphHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MutableGraphHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

