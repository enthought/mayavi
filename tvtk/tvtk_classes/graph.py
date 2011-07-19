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


class Graph(DataObject):
    """
    Graph - Base class for graph data types.
    
    Superclass: DataObject
    
    Graph is the abstract base class that provides all read-only API
    for graph data types. A graph consists of a collection of vertices
    and a collection of edges connecting pairs of vertices. The
    DirectedGraph subclass represents a graph whose edges have
    inherent order from source vertex to target vertex, while
    UndirectedGraph is a graph whose edges have no inherent ordering.
    
    Graph vertices may be traversed in two ways. In the current
    implementation, all vertices are assigned consecutive ids starting at
    zero, so they may be traversed in a simple for loop from 0 to
    graph->_get_number_of_vertices() - 1. You may alternately create a
    VertexListIterator and call graph->_get_vertices(it). it->Next()
    will return the id of the next vertex, while it->_has_next() indicates
    whether there are more vertices in the graph. This is the preferred
    method, since in the future graphs may support filtering or
    subsetting where the vertex ids may not be contiguous.
    
    Graph edges must be traversed through iterators. To traverse all
    edges in a graph, create an instance of EdgeListIterator and call
    graph->_get_edges(it). it->Next() returns lightweight EdgeType
    structures, which contain the public fields Id, Source and Target. Id
    is the identifier for the edge, which may be used to look up values
    in assiciated edge data arrays. Source and Target store the ids of
    the source and target vertices of the edge. Note that the edge list
    iterator DOES NOT necessarily iterate over edges in order of
    ascending id. To traverse edges from wrapper code (Python, Tcl,
    Java), use it->_next_graph_edge() instead of it->Next().  This will
    return a heavyweight, wrappable GraphEdge object, which has the
    same fields as EdgeType accessible through getter methods.
    
    To traverse all edges outgoing from a vertex, create a
    OutEdgeIterator and call graph->_get_out_edges(v, it). it->Next()
    returns a lightweight OutEdgeType containing the fields Id and
    Target. The source of the edge is always the vertex that was passed
    as an argument to get_out_edges(). Incoming edges may be similarly
    traversed with InEdgeIterator, which returns InEdgeType
    structures with Id and Source fields. Both OutEdgeIterator and
    InEdgeIterator also provide the wrapper functions next_graph_edge()
    which return GraphEdge objects.
    
    An additional iterator, AdjacentVertexIterator can traverse
    outgoing vertices directly, instead needing to parse through edges.
    Initialize the iterator by calling graph->_get_adjacent_vertices(v, it).
    
    Graph has two instances of DataSetAttributes for associated
    vertex and edge data. It also has a Points instance which may
    store x,y,z locations for each vertex. This is populated by filters
    such as GraphLayout and AssignCoordinates.
    
    All graph types share the same implementation, so the structure of
    one may be shared among multiple graphs, even graphs of different
    types. Structures from UndirectedGraph and
    MutableUndirectedGraph may be shared directly.  Structures from
    DirectedGraph, MutableDirectedGraph, and Tree may be shared
    directly with the exception that setting a structure to a tree
    requires that a "is a tree" test passes.
    
    For graph types that are known to be compatible, calling
    shallow_copy() or deep_copy() will work as expected.  When the outcome
    of a conversion is unknown (i.e. setting a graph to a tree),
    checked_shallow_copy() and checked_deep_copy() exist which are identical
    to shallow_copy() and deep_copy(), except that instead of emitting an
    error for an incompatible structure, the function returns false. 
    This allows you to programmatically check structure compatibility
    without causing error messages.
    
    To construct a graph, use MutableDirectedGraph or
    MutableUndirectedGraph. You may then use checked_shallow_copy to set
    the contents of a mutable graph type into one of the non-mutable
    types DirectedGraph, UndirectedGraph. To construct a tree, use
    MutableDirectedGraph, with directed edges which point from the
    parent to the child, then use checked_shallow_copy to set the structure
    to a Tree.
    
    Caveats:
    
    All copy operations implement copy-on-write. The structures are
    initially shared, but if one of the graphs is modified, the structure
    is copied so that to the user they function as if they were deep
    copied. This means that care must be taken if different threads are
    accessing different graph instances that share the same structure.
    Race conditions may develop if one thread is modifying the graph at
    the same time that another graph is copying the structure.
    
    Vertex pedigree IDs:
    
    The vertices in a Graph can be associated with pedigree IDs
    through get_vertex_data()->_set_pedigree_ids. In this case, there is a 1-1
    mapping between pedigree Ids and vertices. One can query the vertex
    ID based on the pedigree ID using find_vertex, add new vertices by
    pedigree ID with add_vertex, and add edges based on the pedigree IDs
    of the source and target vertices. For example, add_edge("_here",
    "There") will find (or add) vertices with pedigree ID "Here" and
    "There" and then introduce an edge from "Here" to "There".
    
    To configure the Graph with a pedigree ID mapping, create a
    DataArray that will store the pedigree IDs and set that array as
    the pedigree ID array for the vertices via
    get_vertex_data()->_set_pedigree_ids().
    
    Distributed graphs:
    
    Graph instances can be distributed across multiple machines, to
    allow the construction and manipulation of graphs larger than a
    single machine could handle. A distributed graph will typically be
    distributed across many different nodes within a cluster, using the
    Message Passing Interface (MPI) to allow those cluster nodes to
    communicate.
    
    An empty Graph can be made into a distributed graph by attaching
    an instance of a DistributedGraphHelper via the
    set_distributed_graph_helper() method. To determine whether a graph is
    distributed or not, call get_distributed_graph_helper() and check
    whether the result is non-NULL. For a distributed graph, the number
    of processors across which the graph is distributed can be retrieved
    by extracting the value for the DATA_NUMBER_OF_PIECES key in the
    Information object (retrieved by get_information()) associated with
    the graph. Similarly, the value corresponding to the
    DATA_PIECE_NUMBER key of the Information object describes which
    piece of the data this graph instance provides.
    
    Distributed graphs behave somewhat differently from non-distributed
    graphs, and will require special care. In a distributed graph, each
    of the processors will contain a subset of the vertices in the graph.
    That subset of vertices can be accessed via the VertexListIterator
    produced by get_vertices(). get_number_of_vertices(), therefore, returns
    the number of vertices stored locally: it does not account for
    vertices stored on other processors. A vertex (or edge) is identified
    by both the rank of its owning processor and by its index within that
    processor, both of which are encoded within the IdType value that
    describes that vertex (or edge). The owning processor is a value
    between 0 and P-1, where P is the number of processors across which
    the Graph has been distributed. The local index will be a value
    between 0 and get_number_of_vertices(), for vertices, or
    get_number_of_edges(), for edges, and can be used to access the local
    parts of distributed data arrays. When given a IdType identifying
    a vertex, one can determine the owner of the vertex with
    DistributedGraphHelper::GetVertexOwner() and the local index with
    DistributedGraphHelper::GetVertexIndex(). With edges, the
    appropriate methods are DistributedGraphHelper::GetEdgeOwner() and
    DistributedGraphHelper::GetEdgeIndex(), respectively. To construct
    a IdType representing either a vertex or edge given only its owner
    and local index, use DistributedGraphHelper::MakeDistributedId().
    
    The edges in a distributed graph are always stored on the processors
    that own the vertices named by the edge. For example, given a
    directed edge (u, v), the edge will be stored in the out-edges list
    for vertex u on the processor that owns u, and in the in-edges list
    for vertex v on the processor that owns v. This "row-wise"
    decomposition of the graph means that, for any vertex that is local
    to a processor, that processor can look at all of the incoming and
    outgoing edges of the graph. Processors cannot, however, access the
    incoming or outgoing edge lists of vertex owned by other processors.
    Vertices owned by other processors will not be encountered when
    traversing the vertex list via get_vertices(), but may be encountered
    by traversing the in- and out-edge lists of local vertices or the
    edge list.
    
    Distributed graphs can have pedigree IDs for the vertices in the same
    way that non-distributed graphs can. In this case, the distribution
    of the vertices in the graph is based on pedigree ID. For example, a
    vertex with the pedigree ID "Here" might land on processor 0 while a
    vertex pedigree ID "There" would end up on processor 3. By default,
    the pedigree IDs themselves are hashed to give a random (and,
    hopefully, even) distribution of the vertices. However, one can
    provide a different vertex distribution function by calling
    DistributedGraphHelper::SetVertexPedigreeIdDistribution.  Once a
    distributed graph has pedigree IDs, the no-argument add_vertex()
    method can no longer be used. Additionally, once a vertex has a
    pedigree ID, that pedigree ID should not be changed unless the user
    can guarantee that the vertex distribution will still map that vertex
    to the same processor where it already resides.
    
    See Also:
    
    DirectedGraph UndirectedGraph MutableDirectedGraph
    MutableUndirectedGraph Tree DistributedGraphHelper
    
    Thanks:
    
    Thanks to Brian Wylie, Timothy Shead, Ken Moreland of Sandia National
    Laboratories and Douglas Gregor of Indiana University for designing
    these classes.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraph, obj, update, **traits)
    
    def get_edge_point(self, *args):
        """
        V.get_edge_point(int, int) -> (float, float, float)
        C++: double *GetEdgePoint(IdType e, IdType i)
        Get the x,y,z location of a point along edge e.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdgePoint, *args)
        return ret

    def set_edge_point(self, *args):
        """
        V.set_edge_point(int, int, [float, float, float])
        C++: void SetEdgePoint(IdType e, IdType i, double x[3])
        V.set_edge_point(int, int, float, float, float)
        C++: void SetEdgePoint(IdType e, IdType i, double x,
            double y, double z)
        Set an x,y,z location of a point along an edge. This assumes
        there is already a point at location i, and simply overwrites it.
        """
        ret = self._wrap_call(self._vtk_obj.SetEdgePoint, *args)
        return ret

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    def _set_points(self, arg):
        old_val = self._get_points()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetPoints,
                        my_arg[0])
        self.trait_property_changed('points', old_val, arg)
    points = traits.Property(_get_points, _set_points, help=\
        """
        Returns the points array for this graph. If points is not yet
        constructed, generates and returns a new points array filled with
        (0,0,0) coordinates. In a distributed graph, only the points for
        local vertices can be retrieved or modified.
        """
    )

    def _get_distributed_graph_helper(self):
        return wrap_vtk(self._vtk_obj.GetDistributedGraphHelper())
    def _set_distributed_graph_helper(self, arg):
        old_val = self._get_distributed_graph_helper()
        self._wrap_call(self._vtk_obj.SetDistributedGraphHelper,
                        deref_vtk(arg))
        self.trait_property_changed('distributed_graph_helper', old_val, arg)
    distributed_graph_helper = traits.Property(_get_distributed_graph_helper, _set_distributed_graph_helper, help=\
        """
        Retrieves the distributed graph helper for this graph
        """
    )

    def get_adjacent_vertices(self, *args):
        """
        V.get_adjacent_vertices(int, AdjacentVertexIterator)
        C++: virtual void GetAdjacentVertices(IdType v,
            AdjacentVertexIterator *it)
        Initializes the adjacent vertex iterator to iterate over all
        outgoing vertices from vertex v.  For an undirected graph,
        returns all adjacent vertices. In a distributed graph, the vertex
        v must be local to this processor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetAdjacentVertices, *my_args)
        return ret

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6])
        Return a pointer to the geometry bounding box in the form
        (xmin,xmax, ymin,ymax, zmin,zmax). In a distributed graph, this
        computes the bounds around the local part of the graph.
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def get_degree(self, *args):
        """
        V.get_degree(int) -> int
        C++: virtual IdType GetDegree(IdType v)
        The total of all incoming and outgoing vertices for vertex v. For
        undirected graphs, this is simply the number of edges incident to
        v. In a distributed graph, the vertex v must be local to this
        processor.
        """
        ret = self._wrap_call(self._vtk_obj.GetDegree, *args)
        return ret

    def _get_edge_data(self):
        return wrap_vtk(self._vtk_obj.GetEdgeData())
    edge_data = traits.Property(_get_edge_data, help=\
        """
        Get the vertex or edge data.
        """
    )

    def get_edge_id(self, *args):
        """
        V.get_edge_id(int, int) -> int
        C++: IdType GetEdgeId(IdType a, IdType b)
        Returns the Id of the edge between vertex a and vertex b. This is
        independent of directionality of the edge, that is, if edge A->B
        exists or if edge B->A exists, this function will return its Id.
        If multiple edges exist between a and b, here is no guarantee
        about which one will be returned. Returns -1 if no edge exists
        between a and b.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdgeId, *args)
        return ret

    def get_edges(self, *args):
        """
        V.get_edges(EdgeListIterator)
        C++: virtual void GetEdges(EdgeListIterator *it)
        Initializes the edge list iterator to iterate over all edges in
        the graph. Edges may not be traversed in order of increasing edge
        id. In a distributed graph, this returns edges that are stored
        locally.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetEdges, *my_args)
        return ret

    def get_graph_internals(self, *args):
        """
        V.get_graph_internals(bool) -> GraphInternals
        C++: GraphInternals *GetGraphInternals(bool modifying)
        Returns the internal representation of the graph. If modifying is
        true, then the returned GraphInternals object will be unique
        to this Graph object.
        """
        ret = self._wrap_call(self._vtk_obj.GetGraphInternals, *args)
        return wrap_vtk(ret)

    def get_in_degree(self, *args):
        """
        V.get_in_degree(int) -> int
        C++: virtual IdType GetInDegree(IdType v)
        The number of incoming edges to vertex v. For undirected graphs,
        returns the same as get_degree(). In a distributed graph, the
        vertex v must be local to this processor.
        """
        ret = self._wrap_call(self._vtk_obj.GetInDegree, *args)
        return ret

    def get_in_edge(self, *args):
        """
        V.get_in_edge(int, int, GraphEdge)
        C++: virtual void GetInEdge(IdType v, IdType index,
            GraphEdge *e)
        Random-access method for retrieving incoming edges to vertex v.
        The method fills the GraphEdge instance with the id, source,
        and target of the edge. This method is provided for wrappers,
        get_in_edge(vtk_id_type, IdType) is preferred.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetInEdge, *my_args)
        return ret

    def get_in_edges(self, *args):
        """
        V.get_in_edges(int, InEdgeIterator)
        C++: virtual void GetInEdges(IdType v, InEdgeIterator *it)
        Initializes the in edge iterator to iterate over all incoming
        edges to vertex v.  For an undirected graph, returns all incident
        edges. In a distributed graph, the vertex v must be local to this
        processor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetInEdges, *my_args)
        return ret

    def get_induced_edges(self, *args):
        """
        V.get_induced_edges(IdTypeArray, IdTypeArray)
        C++: void GetInducedEdges(IdTypeArray *verts,
            IdTypeArray *edges)
        Fills a list of edge indices with the edges contained in the
        induced subgraph formed by the vertices in the vertex list.
        """
        my_args = deref_array(args, [('vtkIdTypeArray', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetInducedEdges, *my_args)
        return ret

    def get_number_of_edge_points(self, *args):
        """
        V.get_number_of_edge_points(int) -> int
        C++: IdType GetNumberOfEdgePoints(IdType e)
        Get the number of edge points associated with an edge.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfEdgePoints, *args)
        return ret

    def _get_number_of_edges(self):
        return self._vtk_obj.GetNumberOfEdges()
    number_of_edges = traits.Property(_get_number_of_edges, help=\
        """
        The number of edges in the graph. In a distributed graph, this
        returns the number of edges stored locally.
        """
    )

    def _get_number_of_vertices(self):
        return self._vtk_obj.GetNumberOfVertices()
    number_of_vertices = traits.Property(_get_number_of_vertices, help=\
        """
        The number of vertices in the graph. In a distributed graph,
        returns the number of local vertices in the graph.
        """
    )

    def get_out_degree(self, *args):
        """
        V.get_out_degree(int) -> int
        C++: virtual IdType GetOutDegree(IdType v)
        The number of outgoing edges from vertex v. For undirected
        graphs, returns the same as get_degree(). In a distributed graph,
        the vertex v must be local to this processor.
        """
        ret = self._wrap_call(self._vtk_obj.GetOutDegree, *args)
        return ret

    def get_out_edge(self, *args):
        """
        V.get_out_edge(int, int, GraphEdge)
        C++: virtual void GetOutEdge(IdType v, IdType index,
            GraphEdge *e)
        Random-access method for retrieving outgoing edges from vertex v.
        The method fills the GraphEdge instance with the id, source,
        and target of the edge. This method is provided for wrappers,
        get_out_edge(vtk_id_type, IdType) is preferred.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetOutEdge, *my_args)
        return ret

    def get_out_edges(self, *args):
        """
        V.get_out_edges(int, OutEdgeIterator)
        C++: virtual void GetOutEdges(IdType v, OutEdgeIterator *it)
        Initializes the out edge iterator to iterate over all outgoing
        edges of vertex v.  For an undirected graph, returns all incident
        edges. In a distributed graph, the vertex v must be local to this
        processor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetOutEdges, *my_args)
        return ret

    def get_point(self, *args):
        """
        V.get_point(int, [float, float, float])
        C++: void GetPoint(IdType ptId, double x[3])
        These methods return the point (0,0,0) until the points structure
        is created, when it returns the actual point position. In a
        distributed graph, only the points for local vertices can be
        retrieved.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint, *args)
        return ret

    def get_source_vertex(self, *args):
        """
        V.get_source_vertex(int) -> int
        C++: IdType GetSourceVertex(IdType e)
        Retrieve the source and target vertices for an edge id. NOTE: The
        first time this is called, the graph will build a mapping array
        from edge id to source/target that is the same size as the number
        of edges in the graph. If you have access to a OutEdgeType,
        InEdgeType, EdgeType, or GraphEdge, you should directly
        use these structures to look up the source or target instead of
        this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetSourceVertex, *args)
        return ret

    def get_target_vertex(self, *args):
        """
        V.get_target_vertex(int) -> int
        C++: IdType GetTargetVertex(IdType e)
        Retrieve the source and target vertices for an edge id. NOTE: The
        first time this is called, the graph will build a mapping array
        from edge id to source/target that is the same size as the number
        of edges in the graph. If you have access to a OutEdgeType,
        InEdgeType, EdgeType, or GraphEdge, you should directly
        use these structures to look up the source or target instead of
        this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetTargetVertex, *args)
        return ret

    def _get_vertex_data(self):
        return wrap_vtk(self._vtk_obj.GetVertexData())
    vertex_data = traits.Property(_get_vertex_data, help=\
        """
        Get the vertex or edge data.
        """
    )

    def get_vertices(self, *args):
        """
        V.get_vertices(VertexListIterator)
        C++: virtual void GetVertices(VertexListIterator *it)
        Initializes the vertex list iterator to iterate over all vertices
        in the graph. In a distributed graph, the iterator traverses all
        local vertices.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetVertices, *my_args)
        return ret

    def add_edge_point(self, *args):
        """
        V.add_edge_point(int, [float, float, float])
        C++: void AddEdgePoint(IdType e, double x[3])
        V.add_edge_point(int, float, float, float)
        C++: void AddEdgePoint(IdType e, double x, double y, double z)
        Adds a point to the end of the list of edge points for a certain
        edge.
        """
        ret = self._wrap_call(self._vtk_obj.AddEdgePoint, *args)
        return ret

    def checked_deep_copy(self, *args):
        """
        V.checked_deep_copy(Graph) -> bool
        C++: virtual bool CheckedDeepCopy(Graph *g)
        Performs the same operation as deep_copy(), but instead of
        reporting an error for an incompatible graph, returns false.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CheckedDeepCopy, *my_args)
        return ret

    def checked_shallow_copy(self, *args):
        """
        V.checked_shallow_copy(Graph) -> bool
        C++: virtual bool CheckedShallowCopy(Graph *g)
        Performs the same operation as shallow_copy(), but instead of
        reporting an error for an incompatible graph, returns false.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CheckedShallowCopy, *my_args)
        return ret

    def clear_edge_points(self, *args):
        """
        V.clear_edge_points(int)
        C++: void ClearEdgePoints(IdType e)
        Clear all points associated with an edge.
        """
        ret = self._wrap_call(self._vtk_obj.ClearEdgePoints, *args)
        return ret

    def compute_bounds(self):
        """
        V.compute_bounds()
        C++: void ComputeBounds()
        Compute the bounds of the graph. In a distributed graph, this
        computes the bounds around the local part of the graph.
        """
        ret = self._vtk_obj.ComputeBounds()
        return ret
        

    def copy_structure(self, *args):
        """
        V.copy_structure(Graph)
        C++: virtual void CopyStructure(Graph *g)
        Does a shallow copy of the topological information, but not the
        associated attributes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyStructure, *my_args)
        return ret

    def deep_copy_edge_points(self, *args):
        """
        V.deep_copy_edge_points(Graph)
        C++: void DeepCopyEdgePoints(Graph *g)
        Copy the internal edge point data from another graph into this
        graph. Both graphs must have the same number of edges.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopyEdgePoints, *my_args)
        return ret

    def dump(self):
        """
        V.dump()
        C++: void Dump()
        Dump the contents of the graph to standard output.
        """
        ret = self._vtk_obj.Dump()
        return ret
        

    def find_vertex(self, *args):
        """
        V.find_vertex(Variant) -> int
        C++: IdType FindVertex(const Variant &pedigreeID)
        Retrieve the vertex with the given pedigree ID. If successful,
        returns the ID of the vertex. Otherwise, either the vertex data
        does not have a pedigree ID array or there is no vertex with the
        given pedigree ID, so this function returns -1. If the graph is a
        distributed graph, this method will return the Distributed-ID of
        the vertex.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FindVertex, *my_args)
        return ret

    def is_same_structure(self, *args):
        """
        V.is_same_structure(Graph) -> bool
        C++: bool IsSameStructure(Graph *other)
        Returns true if both graphs point to the same adjacency
        structure. Can be used to test the copy-on-write feature of the
        graph.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsSameStructure, *my_args)
        return ret

    def reorder_out_vertices(self, *args):
        """
        V.reorder_out_vertices(int, IdTypeArray)
        C++: void ReorderOutVertices(IdType v,
            IdTypeArray *vertices)
        Reorder the outgoing vertices of a vertex. The vertex list must
        have the same elements as the current out edge list, just in a
        different order. This method does not change the topology of the
        graph. In a distributed graph, the vertex v must be local.
        """
        my_args = deref_array(args, [('int', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.ReorderOutVertices, *my_args)
        return ret

    def shallow_copy_edge_points(self, *args):
        """
        V.shallow_copy_edge_points(Graph)
        C++: void ShallowCopyEdgePoints(Graph *g)
        Copy the internal edge point data from another graph into this
        graph. Both graphs must have the same number of edges.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopyEdgePoints, *my_args)
        return ret

    def squeeze(self):
        """
        V.squeeze()
        C++: virtual void Squeeze()"""
        ret = self._vtk_obj.Squeeze()
        return ret
        

    def to_directed_graph(self, *args):
        """
        V.to_directed_graph(DirectedGraph) -> bool
        C++: bool ToDirectedGraph(DirectedGraph *g)
        Convert the graph to a directed graph.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ToDirectedGraph, *my_args)
        return ret

    def to_undirected_graph(self, *args):
        """
        V.to_undirected_graph(UndirectedGraph) -> bool
        C++: bool ToUndirectedGraph(UndirectedGraph *g)
        Convert the graph to an undirected graph.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ToUndirectedGraph, *my_args)
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
            return super(Graph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Graph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit Graph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Graph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

