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


class ExtractSelectedGraph(GraphAlgorithm):
    """
    ExtractSelectedGraph - return a subgraph of a Graph
    
    Superclass: GraphAlgorithm
    
    The first input is a Graph to take a subgraph from. The second
    input (optional) is a Selection containing selected indices. The
    third input (optional) is a AnnotationsLayers whose annotations
    contain selected specifying selected indices. The Selection may
    have FIELD_TYPE set to POINTS (a vertex selection) or CELLS (an edge
    selection).  A vertex selection preserves all edges that connect
    selected vertices.  An edge selection preserves all vertices that are
    adjacent to at least one selected edge.  Alternately, you may
    indicate that an edge selection should maintain the full set of
    vertices, by turning remove_isolated_vertices off.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractSelectedGraph, obj, update, **traits)
    
    remove_isolated_vertices = tvtk_base.false_bool_trait(help=\
        """
        If set, removes vertices with no adjacent edges in an edge
        selection. A vertex selection ignores this flag and always
        returns the full set of selected vertices.  Default is on.
        """
    )
    def _remove_isolated_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRemoveIsolatedVertices,
                        self.remove_isolated_vertices_)

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)
        Specify the first Graph input and the second Selection
        input.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    def set_annotation_layers_connection(self, *args):
        """
        V.set_annotation_layers_connection(AlgorithmOutput)
        C++: void SetAnnotationLayersConnection(AlgorithmOutput *in)
        A convenience method for setting the third input (i.e. the
        annotation layers).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetAnnotationLayersConnection, *my_args)
        return ret

    def set_selection_connection(self, *args):
        """
        V.set_selection_connection(AlgorithmOutput)
        C++: void SetSelectionConnection(AlgorithmOutput *in)
        A convenience method for setting the second input (i.e. the
        selection).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSelectionConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('progress_text', 'GetProgressText'),
    ('remove_isolated_vertices', 'GetRemoveIsolatedVertices'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'remove_isolated_vertices', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractSelectedGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractSelectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['remove_isolated_vertices'], [], []),
            title='Edit ExtractSelectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractSelectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

