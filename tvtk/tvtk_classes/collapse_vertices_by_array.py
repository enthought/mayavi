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


class CollapseVerticesByArray(GraphAlgorithm):
    """
    CollapseVerticesByArray - Collapse the graph given a vertex array
    
    Superclass: GraphAlgorithm
    
    CollapseVerticesByArray is a class which collapses the graph using
    a vertex array as the key. So if the graph has vertices sharing
    common traits then this class combines all these vertices into one.
    This class does not perform aggregation on vertex data but allow to
    do so for edge data. Users can choose one or more edge data arrays
    for aggregation using add_aggregate_edge_array function.
    
    Thanks:
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCollapseVerticesByArray, obj, update, **traits)
    
    allow_self_loops = tvtk_base.false_bool_trait(help=\
        """
        Boolean to allow self loops during collapse.
        """
    )
    def _allow_self_loops_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowSelfLoops,
                        self.allow_self_loops_)

    count_vertices_collapsed = tvtk_base.false_bool_trait(help=\
        """
        Get/Set if count should be made of how many vertices collapsed.
        """
    )
    def _count_vertices_collapsed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCountVerticesCollapsed,
                        self.count_vertices_collapsed_)

    count_edges_collapsed = tvtk_base.false_bool_trait(help=\
        """
        Set if count should be made of how many edges collapsed.
        """
    )
    def _count_edges_collapsed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCountEdgesCollapsed,
                        self.count_edges_collapsed_)

    vertices_collapsed_array = traits.String(r"VerticesCollapsedCountArray", enter_set=True, auto_set=False, help=\
        """
        Name of the array where the count of how many vertices collapsed
        will be stored. By default name of the array is
        "_vertices_collapsed_count_array".
        """
    )
    def _vertices_collapsed_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticesCollapsedArray,
                        self.vertices_collapsed_array)

    edges_collapsed_array = traits.String(r"EdgesCollapsedCountArray", enter_set=True, auto_set=False, help=\
        """
        Name of the array where the count of how many edges collapsed
        will be stored.By default the name of array is
        "_edges_collapsed_count_array".
        """
    )
    def _edges_collapsed_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgesCollapsedArray,
                        self.edges_collapsed_array)

    vertex_array = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the array using which perform the collapse.
        """
    )
    def _vertex_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexArray,
                        self.vertex_array)

    def add_aggregate_edge_array(self, *args):
        """
        V.add_aggregate_edge_array(string)
        C++: void AddAggregateEdgeArray(const char *arrName)
        Add arrays on which aggregation of data is allowed. Default if
        replaced by the last value.
        """
        ret = self._wrap_call(self._vtk_obj.AddAggregateEdgeArray, *args)
        return ret

    def clear_aggregate_edge_array(self):
        """
        V.clear_aggregate_edge_array()
        C++: void ClearAggregateEdgeArray()
        Clear the list of arrays on which aggregation was set to allow.
        """
        ret = self._vtk_obj.ClearAggregateEdgeArray()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('edges_collapsed_array', 'GetEdgesCollapsedArray'),
    ('vertices_collapsed_array', 'GetVerticesCollapsedArray'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('vertex_array',
    'GetVertexArray'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('count_vertices_collapsed', 'GetCountVerticesCollapsed'),
    ('allow_self_loops', 'GetAllowSelfLoops'), ('count_edges_collapsed',
    'GetCountEdgesCollapsed'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'allow_self_loops', 'count_edges_collapsed',
    'count_vertices_collapsed', 'debug', 'global_warning_display',
    'release_data_flag', 'edges_collapsed_array', 'progress_text',
    'vertex_array', 'vertices_collapsed_array'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CollapseVerticesByArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CollapseVerticesByArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['allow_self_loops', 'count_edges_collapsed',
            'count_vertices_collapsed'], [], ['edges_collapsed_array',
            'vertex_array', 'vertices_collapsed_array']),
            title='Edit CollapseVerticesByArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CollapseVerticesByArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

