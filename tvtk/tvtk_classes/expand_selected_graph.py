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

from tvtk.tvtk_classes.selection_algorithm import SelectionAlgorithm


class ExpandSelectedGraph(SelectionAlgorithm):
    """
    ExpandSelectedGraph - expands a selection set of a Graph
    
    Superclass: SelectionAlgorithm
    
    The first input is a Selection containing the selected vertices.
    The second input is a Graph. This filter 'grows' the selection set
    in one of the following ways
    1) set_bfs_distance controls how many 'hops' the selection is grown
       from each seed point in the selection set (defaults to 1)
    2) include_shortest_paths controls whether this filter tries to
       'connect' the vertices in the selection set by computing the
       shortest path between the vertices (if such a path exists) Note:
       include_shortest_paths is currently non-functional
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExpandSelectedGraph, obj, update, **traits)
    
    include_shortest_paths = tvtk_base.false_bool_trait(help=\
        """
        Set/Get include_shortest_paths controls whether this filter tries
        to 'connect' the vertices in the selection set by computing the
        shortest path between the vertices (if such a path exists) Note:
        include_shortest_paths is currently non-functional
        """
    )
    def _include_shortest_paths_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIncludeShortestPaths,
                        self.include_shortest_paths_)

    use_domain = tvtk_base.false_bool_trait(help=\
        """
        Whether or not to use the domain when deciding to add a vertex to
        the expansion. Defaults to false.
        """
    )
    def _use_domain_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDomain,
                        self.use_domain_)

    bfs_distance = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get BFSDistance which controls how many 'hops' the selection
        is grown from each seed point in the selection set (defaults to
        1)
        """
    )
    def _bfs_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBFSDistance,
                        self.bfs_distance)

    domain = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the vertex domain to use in the expansion.
        """
    )
    def _domain_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDomain,
                        self.domain)

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)
        Specify the first Selection input and the second Graph
        input.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    def set_graph_connection(self, *args):
        """
        V.set_graph_connection(AlgorithmOutput)
        C++: void SetGraphConnection(AlgorithmOutput *in)
        A convenience method for setting the second input (i.e. the
        graph).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGraphConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('domain', 'GetDomain'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('use_domain', 'GetUseDomain'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('include_shortest_paths',
    'GetIncludeShortestPaths'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('bfs_distance', 'GetBFSDistance'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'include_shortest_paths', 'release_data_flag', 'use_domain',
    'bfs_distance', 'domain', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExpandSelectedGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExpandSelectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['include_shortest_paths', 'use_domain'], [],
            ['bfs_distance', 'domain']),
            title='Edit ExpandSelectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExpandSelectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

