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


class MergeGraphs(GraphAlgorithm):
    """
    MergeGraphs - combines two graphs
    
    Superclass: GraphAlgorithm
    
    MergeGraphs combines information from two graphs into one. Both
    graphs must have pedigree ids assigned to the vertices. The output
    will contain the vertices/edges in the first graph, in addition to:
    
    - vertices in the second graph whose pedigree id does not match a
      vertex in the first input
    
    - edges in the second graph
    
    The output will contain the same attribute structure as the input;
    fields associated only with the second input graph will not be passed
    to the output. When possible, the vertex/edge data for new vertices
    and edges will be populated with matching attributes on the second
    graph. To be considered a matching attribute, the array must have the
    same name, type, and number of components.
    
    Caveats:
    
    This filter is not "domain-aware". Pedigree ids are assumed to be
    globally unique, regardless of their domain.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMergeGraphs, obj, update, **traits)
    
    use_edge_window = tvtk_base.false_bool_trait(help=\
        """
        Whether to use an edge window array. The default is to not use a
        window array.
        """
    )
    def _use_edge_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseEdgeWindow,
                        self.use_edge_window_)

    edge_window_array_name = traits.String(r"time", enter_set=True, auto_set=False, help=\
        """
        The edge window array. The default array name is "time".
        """
    )
    def _edge_window_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeWindowArrayName,
                        self.edge_window_array_name)

    edge_window = traits.Float(10000.0, enter_set=True, auto_set=False, help=\
        """
        The time window amount. Edges with values lower than the maximum
        value minus this window will be removed from the graph. The
        default edge window is 10000.
        """
    )
    def _edge_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeWindow,
                        self.edge_window)

    def extend_graph(self, *args):
        """
        V.extend_graph(MutableGraphHelper, Graph) -> int
        C++: int ExtendGraph(MutableGraphHelper *g1, Graph *g2)
        This is the core functionality of the algorithm. Adds edges and
        vertices from g2 into g1.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ExtendGraph, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('edge_window_array_name', 'GetEdgeWindowArrayName'),
    ('progress_text', 'GetProgressText'), ('edge_window',
    'GetEdgeWindow'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('use_edge_window', 'GetUseEdgeWindow'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_edge_window', 'edge_window',
    'edge_window_array_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MergeGraphs, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MergeGraphs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_edge_window'], [], ['edge_window',
            'edge_window_array_name']),
            title='Edit MergeGraphs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MergeGraphs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

