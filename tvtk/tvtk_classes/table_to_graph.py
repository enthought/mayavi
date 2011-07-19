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

from tvtk.tvtk_classes.graph_algorithm import GraphAlgorithm


class TableToGraph(GraphAlgorithm):
    """
    TableToGraph - convert a Table into a Graph
    
    Superclass: GraphAlgorithm
    
    TableToGraph converts a table to a graph using an auxilliary link
    graph.  The link graph specifies how each row in the table should be
    converted to an edge, or a collection of edges.  It also specifies
    which columns of the table should be considered part of the same
    domain, and which columns should be hidden.
    
    A second, optional, table may be provided as the vertex table. This
    vertex table must have one or more domain columns whose values match
    values in the edge table.  The linked column name is specified in the
    domain array in the link graph.  The output graph will only contain
    vertices corresponding to a row in the vertex table.  For
    heterogenous graphs, you may want to use MergeTables to create a
    single vertex table.
    
    The link graph contains the following arrays:
    
    (1) The "column" array has the names of the columns to connect in
    each table row. This array is required.
    
    (2) The optional "domain" array provides user-defined domain names
    for each column. Matching domains in multiple columns will merge
    vertices with the same value from those columns.  By default, all
    columns are in the same domain. If a vertex table is supplied, the
    domain indicates the column in the vertex table that the edge table
    column associates with.  If the user provides a vertex table but no
    domain names, the output will be an empty graph. Hidden columns do
    not need valid domain names.
    
    (3) The optional "hidden" array is a bit array specifying whether the
    column should be hidden.  The resulting graph will contain edges
    representing connections "through" the hidden column, but the
    vertices for that column will not be present.  By default, no columns
    are hidden.  Hiding a column in a particular domain hides all columns
    in that domain.
    
    The output graph will contain three additional arrays in the vertex
    data. The "domain" column is a string array containing the domain of
    each vertex. The "label" column is a string version of the distinct
    value that, along with the domain, defines that vertex. The "ids"
    column also contains the distinguishing value, but as a Variant
    holding the raw value instead of being converted to a string. The
    "ids" column is set as the vertex pedigree ID attribute.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableToGraph, obj, update, **traits)
    
    directed = tvtk_base.false_bool_trait(help=\
        """
        Specify the directedness of the output graph.
        """
    )
    def _directed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirected,
                        self.directed_)

    def _get_link_graph(self):
        return wrap_vtk(self._vtk_obj.GetLinkGraph())
    def _set_link_graph(self, arg):
        old_val = self._get_link_graph()
        self._wrap_call(self._vtk_obj.SetLinkGraph,
                        deref_vtk(arg))
        self.trait_property_changed('link_graph', old_val, arg)
    link_graph = traits.Property(_get_link_graph, _set_link_graph, help=\
        """
        The graph describing how to link the columns in the table.
        """
    )

    def add_link_edge(self, *args):
        """
        V.add_link_edge(string, string)
        C++: void AddLinkEdge(const char *column1, const char *column2)
        Add an edge to the link graph.  Specify the names of the columns
        to link.
        """
        ret = self._wrap_call(self._vtk_obj.AddLinkEdge, *args)
        return ret

    def add_link_vertex(self, *args):
        """
        V.add_link_vertex(string, string, int)
        C++: void AddLinkVertex(const char *column, const char *domain=0,
            int hidden=0)
        Add a vertex to the link graph.  Specify the column name, the
        domain name for the column, and whether the column is hidden.
        """
        ret = self._wrap_call(self._vtk_obj.AddLinkVertex, *args)
        return ret

    def clear_link_edges(self):
        """
        V.clear_link_edges()
        C++: void ClearLinkEdges()
        Clear the link graph edges.  The graph vertices will remain.
        """
        ret = self._vtk_obj.ClearLinkEdges()
        return ret
        

    def clear_link_vertices(self):
        """
        V.clear_link_vertices()
        C++: void ClearLinkVertices()
        Clear the link graph vertices.  This also clears all edges.
        """
        ret = self._vtk_obj.ClearLinkVertices()
        return ret
        

    def link_column_path(self, *args):
        """
        V.link_column_path(StringArray, StringArray, BitArray)
        C++: void LinkColumnPath(StringArray *column,
            StringArray *domain=0, BitArray *hidden=0)
        Links the columns in a specific order. This creates a simple path
        as the link graph.
        """
        my_args = deref_array(args, [('vtkStringArray', 'vtkStringArray', 'vtkBitArray')])
        ret = self._wrap_call(self._vtk_obj.LinkColumnPath, *my_args)
        return ret

    def set_vertex_table_connection(self, *args):
        """
        V.set_vertex_table_connection(AlgorithmOutput)
        C++: void SetVertexTableConnection(AlgorithmOutput *in)
        A convenience method for setting the vertex table input.  This is
        mainly for the benefit of the VTK client/server layer, vanilla
        VTK code should use e.g:
        
        table_to_graph->_set_input_connection(_1, vertex_table->output());
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVertexTableConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('directed', 'GetDirected'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'directed', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableToGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TableToGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['directed'], [], []),
            title='Edit TableToGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableToGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

