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


class SQLGraphReader(GraphAlgorithm):
    """
    SQLGraphReader - read a Graph from a database
    
    Superclass: GraphAlgorithm
    
    Creates a Graph using one or two SQLQuery's.  The first
    (required) query must have one row for each arc in the graph. The
    query must have two columns which represent the source and target
    node ids.
    
    The second (optional) query has one row for each node in the graph.
    The table must have a field whose values match those in the arc
    table. If the node table is not given, a node will be created for
    each unique source or target identifier in the arc table.
    
    The source, target, and node ID fields must be of the same type, and
    must be either StringArray or a subclass of DataArray.
    
    All columns in the queries, including the source, target, and node
    index fields, are copied into the arc data and node data of the
    resulting Graph.  If the node query is not given, the node data
    will contain a single "id" column with the same type as the
    source/target id arrays.
    
    If parallel arcs are collected, not all the arc data is not copied
    into the output.  Only the source and target id arrays will be
    transferred. An additional IdTypeArray column called "weight" is
    created which contains the number of times each arc appeared in the
    input.
    
    If the node query contains positional data, the user may specify the
    names of these fields. These arrays must be data arrays.  The
    z-coordinate array is optional, and if not given the z-coordinates
    are set to zero.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSQLGraphReader, obj, update, **traits)
    
    directed = tvtk_base.false_bool_trait(help=\
        """
        When set, creates a directed graph, as opposed to an undirected
        graph.
        """
    )
    def _directed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirected,
                        self.directed_)

    collapse_edges = tvtk_base.false_bool_trait(help=\
        """
        When set, creates a graph with no parallel arcs. Parallel arcs
        are combined into one arc. No cell fields are passed to the
        output, except the GhostLevels array if it exists, but a new
        field "weight" is created that holds the number of duplicates of
        that arc in the input.
        """
    )
    def _collapse_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCollapseEdges,
                        self.collapse_edges_)

    y_field = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the field in the node query for the node's y
        coordinate.
        """
    )
    def _y_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYField,
                        self.y_field)

    source_field = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the field in the arc query for the source node of
        each arc.
        """
    )
    def _source_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSourceField,
                        self.source_field)

    def _get_edge_query(self):
        return wrap_vtk(self._vtk_obj.GetEdgeQuery())
    def _set_edge_query(self, arg):
        old_val = self._get_edge_query()
        self._wrap_call(self._vtk_obj.SetEdgeQuery,
                        deref_vtk(arg))
        self.trait_property_changed('edge_query', old_val, arg)
    edge_query = traits.Property(_get_edge_query, _set_edge_query, help=\
        """
        The query that retrieves the arc information.
        """
    )

    target_field = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the field in the arc query for the target node of
        each arc.
        """
    )
    def _target_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetField,
                        self.target_field)

    def _get_vertex_query(self):
        return wrap_vtk(self._vtk_obj.GetVertexQuery())
    def _set_vertex_query(self, arg):
        old_val = self._get_vertex_query()
        self._wrap_call(self._vtk_obj.SetVertexQuery,
                        deref_vtk(arg))
        self.trait_property_changed('vertex_query', old_val, arg)
    vertex_query = traits.Property(_get_vertex_query, _set_vertex_query, help=\
        """
        The query that retrieves the node information.
        """
    )

    z_field = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the field in the node query for the node's z
        coordinate.
        """
    )
    def _z_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZField,
                        self.z_field)

    vertex_id_field = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the field in the node query for the node ID.
        """
    )
    def _vertex_id_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexIdField,
                        self.vertex_id_field)

    x_field = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the field in the node query for the node's x
        coordinate.
        """
    )
    def _x_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXField,
                        self.x_field)

    _updateable_traits_ = \
    (('vertex_id_field', 'GetVertexIdField'), ('directed', 'GetDirected'),
    ('source_field', 'GetSourceField'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('z_field', 'GetZField'), ('x_field',
    'GetXField'), ('progress_text', 'GetProgressText'), ('collapse_edges',
    'GetCollapseEdges'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('y_field', 'GetYField'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('target_field', 'GetTargetField'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'collapse_edges', 'debug', 'directed',
    'global_warning_display', 'release_data_flag', 'progress_text',
    'source_field', 'target_field', 'vertex_id_field', 'x_field',
    'y_field', 'z_field'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SQLGraphReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SQLGraphReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['collapse_edges', 'directed'], [], ['source_field',
            'target_field', 'vertex_id_field', 'x_field', 'y_field', 'z_field']),
            title='Edit SQLGraphReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SQLGraphReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

