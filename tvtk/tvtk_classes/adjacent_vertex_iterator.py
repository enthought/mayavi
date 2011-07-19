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


class AdjacentVertexIterator(Object):
    """
    AdjacentVertexIterator - Iterates through adjacent vertices in a
    graph.
    
    Superclass: Object
    
    AdjacentVertexIterator iterates through all vertices adjacent to a
    vertex, i.e. the vertices which may be reached by traversing an out
    edge of the source vertex. Use graph->_get_adjacent_vertices(v, it) to
    initialize the iterator.
    
    See Also:
    
    Thanks:
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAdjacentVertexIterator, obj, update, **traits)
    
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

    def next(self):
        """
        V.next() -> int
        C++: IdType Next()
        Returns the next edge in the graph.
        """
        ret = self._vtk_obj.Next()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AdjacentVertexIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AdjacentVertexIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit AdjacentVertexIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AdjacentVertexIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

