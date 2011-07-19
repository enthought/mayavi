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


class SQLDatabaseGraphSource(GraphAlgorithm):
    """
    SQLDatabaseGraphSource - Generates a Graph based on an SQL
    query.
    
    Superclass: GraphAlgorithm
    
    This class combines SQLDatabase, SQLQuery, and QueryToGraph
    to provide a convenience class for generating graphs from databases.
    Also this class can be easily wrapped and used within para_view /
    over_view.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSQLDatabaseGraphSource, obj, update, **traits)
    
    directed = tvtk_base.true_bool_trait(help=\
        """
        If on (default), generate a directed output graph. If off,
        generate an undirected output graph.
        """
    )
    def _directed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirected,
                        self.directed_)

    generate_edge_pedigree_ids = tvtk_base.true_bool_trait(help=\
        """
        If on (default), generate edge pedigree ids. If off, assign an
        array to be edge pedigree ids.
        """
    )
    def _generate_edge_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateEdgePedigreeIds,
                        self.generate_edge_pedigree_ids_)

    edge_query = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _edge_query_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeQuery,
                        self.edge_query)

    url = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _url_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetURL,
                        self.url)

    edge_pedigree_id_array_name = traits.String(r"id", enter_set=True, auto_set=False, help=\
        """
        Use this array name for setting or generating edge pedigree ids.
        """
    )
    def _edge_pedigree_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgePedigreeIdArrayName,
                        self.edge_pedigree_id_array_name)

    vertex_query = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _vertex_query_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexQuery,
                        self.vertex_query)

    def add_link_edge(self, *args):
        """
        V.add_link_edge(string, string)
        C++: void AddLinkEdge(const char *column1, const char *column2)"""
        ret = self._wrap_call(self._vtk_obj.AddLinkEdge, *args)
        return ret

    def add_link_vertex(self, *args):
        """
        V.add_link_vertex(string, string, int)
        C++: void AddLinkVertex(const char *column, const char *domain=0,
            int hidden=0)"""
        ret = self._wrap_call(self._vtk_obj.AddLinkVertex, *args)
        return ret

    def clear_link_edges(self):
        """
        V.clear_link_edges()
        C++: void ClearLinkEdges()"""
        ret = self._vtk_obj.ClearLinkEdges()
        return ret
        

    def clear_link_vertices(self):
        """
        V.clear_link_vertices()
        C++: void ClearLinkVertices()"""
        ret = self._vtk_obj.ClearLinkVertices()
        return ret
        

    def set_password(self, *args):
        """
        V.set_password(string)
        C++: void SetPassword(const StdString &password)"""
        ret = self._wrap_call(self._vtk_obj.SetPassword, *args)
        return ret

    _updateable_traits_ = \
    (('directed', 'GetDirected'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('url', 'GetURL'), ('debug', 'GetDebug'),
    ('generate_edge_pedigree_ids', 'GetGenerateEdgePedigreeIds'),
    ('progress_text', 'GetProgressText'), ('edge_pedigree_id_array_name',
    'GetEdgePedigreeIdArrayName'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('vertex_query',
    'GetVertexQuery'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('edge_query', 'GetEdgeQuery'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'directed', 'generate_edge_pedigree_ids',
    'global_warning_display', 'release_data_flag',
    'edge_pedigree_id_array_name', 'edge_query', 'progress_text', 'url',
    'vertex_query'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SQLDatabaseGraphSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SQLDatabaseGraphSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['directed', 'generate_edge_pedigree_ids'], [],
            ['edge_pedigree_id_array_name', 'edge_query', 'url', 'vertex_query']),
            title='Edit SQLDatabaseGraphSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SQLDatabaseGraphSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

