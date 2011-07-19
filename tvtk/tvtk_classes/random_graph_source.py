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


class RandomGraphSource(GraphAlgorithm):
    """
    RandomGraphSource - a graph with random edges
    
    Superclass: GraphAlgorithm
    
    Generates a graph with a specified number of vertices, with the
    density of edges specified by either an exact number of edges or the
    probability of an edge.  You may additionally specify whether to
    begin with a random tree (which enforces graph connectivity).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRandomGraphSource, obj, update, **traits)
    
    directed = tvtk_base.false_bool_trait(help=\
        """
        When set, creates a directed graph, as opposed to an undirected
        graph.
        """
    )
    def _directed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirected,
                        self.directed_)

    start_with_tree = tvtk_base.false_bool_trait(help=\
        """
        When set, builds a random tree structure first, then adds
        additional random edges.
        """
    )
    def _start_with_tree_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartWithTree,
                        self.start_with_tree_)

    generate_pedigree_ids = tvtk_base.true_bool_trait(help=\
        """
        Add pedigree ids to vertex and edge data.
        """
    )
    def _generate_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePedigreeIds,
                        self.generate_pedigree_ids_)

    allow_self_loops = tvtk_base.false_bool_trait(help=\
        """
        If this flag is set to true, edges where the source and target
        vertex are the same can be generated.  The default is to forbid
        such loops.
        """
    )
    def _allow_self_loops_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowSelfLoops,
                        self.allow_self_loops_)

    allow_parallel_edges = tvtk_base.false_bool_trait(help=\
        """
        When set, multiple edges from a source to a target vertex are
        allowed. The default is to forbid such loops.
        """
    )
    def _allow_parallel_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowParallelEdges,
                        self.allow_parallel_edges_)

    use_edge_probability = tvtk_base.false_bool_trait(help=\
        """
        When set, uses the edge_probability parameter to determine the
        density of edges.  Otherwise, number_of_edges is used.
        """
    )
    def _use_edge_probability_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseEdgeProbability,
                        self.use_edge_probability_)

    include_edge_weights = tvtk_base.false_bool_trait(help=\
        """
        When set, includes edge weights in an array named "edge_weights".
        Defaults to off.  Weights are random between 0 and 1.
        """
    )
    def _include_edge_weights_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIncludeEdgeWeights,
                        self.include_edge_weights_)

    edge_weight_array_name = traits.String(r"edge weight", enter_set=True, auto_set=False, help=\
        """
        The name of the edge weight array. Default "edge weight".
        """
    )
    def _edge_weight_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeWeightArrayName,
                        self.edge_weight_array_name)

    vertex_pedigree_id_array_name = traits.String(r"vertex id", enter_set=True, auto_set=False, help=\
        """
        The name of the vertex pedigree id array. Default "vertex id".
        """
    )
    def _vertex_pedigree_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexPedigreeIdArrayName,
                        self.vertex_pedigree_id_array_name)

    number_of_edges = traits.Trait(10, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        If use_edge_probability is off, creates a graph with the specified
        number of edges.  Duplicate (parallel) edges are allowed.
        """
    )
    def _number_of_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfEdges,
                        self.number_of_edges)

    number_of_vertices = traits.Trait(10, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        The number of vertices in the graph.
        """
    )
    def _number_of_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfVertices,
                        self.number_of_vertices)

    edge_pedigree_id_array_name = traits.String(r"edge id", enter_set=True, auto_set=False, help=\
        """
        The name of the edge pedigree id array. Default "edge id".
        """
    )
    def _edge_pedigree_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgePedigreeIdArrayName,
                        self.edge_pedigree_id_array_name)

    seed = traits.Int(1177, enter_set=True, auto_set=False, help=\
        """
        Control the seed used for pseudo-random-number generation. This
        ensures that RandomGraphSource can produce repeatable results.
        """
    )
    def _seed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSeed,
                        self.seed)

    edge_probability = traits.Trait(0.5, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        If use_edge_probability is on, adds an edge with this probability
        between 0 and 1 for each pair of vertices in the graph.
        """
    )
    def _edge_probability_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeProbability,
                        self.edge_probability)

    _updateable_traits_ = \
    (('directed', 'GetDirected'), ('start_with_tree', 'GetStartWithTree'),
    ('number_of_vertices', 'GetNumberOfVertices'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('allow_parallel_edges', 'GetAllowParallelEdges'),
    ('allow_self_loops', 'GetAllowSelfLoops'), ('edge_probability',
    'GetEdgeProbability'), ('progress_text', 'GetProgressText'),
    ('vertex_pedigree_id_array_name', 'GetVertexPedigreeIdArrayName'),
    ('debug', 'GetDebug'), ('number_of_edges', 'GetNumberOfEdges'),
    ('edge_pedigree_id_array_name', 'GetEdgePedigreeIdArrayName'),
    ('seed', 'GetSeed'), ('generate_pedigree_ids',
    'GetGeneratePedigreeIds'), ('include_edge_weights',
    'GetIncludeEdgeWeights'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('edge_weight_array_name', 'GetEdgeWeightArrayName'),
    ('abort_execute', 'GetAbortExecute'), ('use_edge_probability',
    'GetUseEdgeProbability'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'allow_parallel_edges', 'allow_self_loops',
    'debug', 'directed', 'generate_pedigree_ids',
    'global_warning_display', 'include_edge_weights', 'release_data_flag',
    'start_with_tree', 'use_edge_probability',
    'edge_pedigree_id_array_name', 'edge_probability',
    'edge_weight_array_name', 'number_of_edges', 'number_of_vertices',
    'progress_text', 'seed', 'vertex_pedigree_id_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RandomGraphSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RandomGraphSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['allow_parallel_edges', 'allow_self_loops',
            'directed', 'generate_pedigree_ids', 'include_edge_weights',
            'start_with_tree', 'use_edge_probability'], [],
            ['edge_pedigree_id_array_name', 'edge_probability',
            'edge_weight_array_name', 'number_of_edges', 'number_of_vertices',
            'seed', 'vertex_pedigree_id_array_name']),
            title='Edit RandomGraphSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RandomGraphSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

