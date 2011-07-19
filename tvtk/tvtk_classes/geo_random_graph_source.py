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

from tvtk.tvtk_classes.random_graph_source import RandomGraphSource


class GeoRandomGraphSource(RandomGraphSource):
    """
    GeoRandomGraphSource - A geospatial graph with random edges
    
    Superclass: RandomGraphSource
    
    Generates a graph with a specified number of vertices, with the
    density of edges specified by either an exact number of edges or the
    probability of an edge.  You may additionally specify whether to
    begin with a random tree (which enforces graph connectivity).
    
    The filter also adds random vertex attributes called latitude and
    longitude. The latitude is distributed uniformly from -90 to 90,
    while longitude is distributed uniformly from -180 to 180.
    
    See Also:
    
    RandomGraphSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoRandomGraphSource, obj, update, **traits)
    
    _updateable_traits_ = \
    (('directed', 'GetDirected'), ('start_with_tree', 'GetStartWithTree'),
    ('edge_probability', 'GetEdgeProbability'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('allow_parallel_edges',
    'GetAllowParallelEdges'), ('debug', 'GetDebug'),
    ('use_edge_probability', 'GetUseEdgeProbability'),
    ('number_of_vertices', 'GetNumberOfVertices'), ('progress_text',
    'GetProgressText'), ('vertex_pedigree_id_array_name',
    'GetVertexPedigreeIdArrayName'), ('allow_self_loops',
    'GetAllowSelfLoops'), ('number_of_edges', 'GetNumberOfEdges'),
    ('reference_count', 'GetReferenceCount'), ('seed', 'GetSeed'),
    ('include_edge_weights', 'GetIncludeEdgeWeights'),
    ('release_data_flag', 'GetReleaseDataFlag'),
    ('edge_pedigree_id_array_name', 'GetEdgePedigreeIdArrayName'),
    ('progress', 'GetProgress'), ('edge_weight_array_name',
    'GetEdgeWeightArrayName'), ('abort_execute', 'GetAbortExecute'),
    ('generate_pedigree_ids', 'GetGeneratePedigreeIds'))
    
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
            return super(GeoRandomGraphSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoRandomGraphSource properties', scrollable=True, resizable=True,
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
            title='Edit GeoRandomGraphSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoRandomGraphSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

