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

from tvtk.tvtk_classes.graph_layout_view import GraphLayoutView


class HierarchicalGraphView(GraphLayoutView):
    """
    HierarchicalGraphView - Accepts a graph and a hierarchy - currently
    
    Superclass: GraphLayoutView
    
    Takes a graph and a hierarchy (currently a tree) and lays out the
    graph vertices based on their categorization within the hierarchy.
    
    .SEE ALSO GraphLayoutView
    
    Thanks:
    
    Thanks to the turtle with jets for feet, without you this class
    wouldn't have been possible.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHierarchicalGraphView, obj, update, **traits)
    
    graph_edge_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether to show edge labels.  Default is off.
        """
    )
    def _graph_edge_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelVisibility,
                        self.graph_edge_label_visibility_)

    color_graph_edges_by_array = tvtk_base.false_bool_trait(help=\
        """
        Whether to color edges.  Default is off.
        """
    )
    def _color_graph_edges_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorGraphEdgesByArray,
                        self.color_graph_edges_by_array_)

    graph_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether the graph edges are visible (default off).
        """
    )
    def _graph_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphVisibility,
                        self.graph_visibility_)

    graph_edge_color_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for coloring edges.  Default is "color".
        """
    )
    def _graph_edge_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeColorArrayName,
                        self.graph_edge_color_array_name)

    bundling_strength = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the bundling strength.
        """
    )
    def _bundling_strength_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBundlingStrength,
                        self.bundling_strength)

    graph_edge_label_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for edge labeling.  Default is "label".
        """
    )
    def _graph_edge_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelArrayName,
                        self.graph_edge_label_array_name)

    graph_edge_label_font_size = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The size of the font used for edge labeling
        """
    )
    def _graph_edge_label_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelFontSize,
                        self.graph_edge_label_font_size)

    def set_graph_edge_color_to_spline_fraction(self):
        """
        V.set_graph_edge_color_to_spline_fraction()
        C++: virtual void SetGraphEdgeColorToSplineFraction()
        Set the color to be the spline fraction
        """
        ret = self._vtk_obj.SetGraphEdgeColorToSplineFraction()
        return ret
        

    def set_graph_from_input(self, *args):
        """
        V.set_graph_from_input(DataObject) -> DataRepresentation
        C++: DataRepresentation *SetGraphFromInput(
            DataObject *input)
        Set the tree and graph representations to the appropriate input
        ports.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGraphFromInput, *my_args)
        return wrap_vtk(ret)

    def set_graph_from_input_connection(self, *args):
        """
        V.set_graph_from_input_connection(AlgorithmOutput)
            -> DataRepresentation
        C++: DataRepresentation *SetGraphFromInputConnection(
            AlgorithmOutput *conn)
        Set the tree and graph representations to the appropriate input
        ports.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGraphFromInputConnection, *my_args)
        return wrap_vtk(ret)

    def set_hierarchy_from_input(self, *args):
        """
        V.set_hierarchy_from_input(DataObject) -> DataRepresentation
        C++: DataRepresentation *SetHierarchyFromInput(
            DataObject *input)
        Set the tree and graph representations to the appropriate input
        ports.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetHierarchyFromInput, *my_args)
        return wrap_vtk(ret)

    def set_hierarchy_from_input_connection(self, *args):
        """
        V.set_hierarchy_from_input_connection(AlgorithmOutput)
            -> DataRepresentation
        C++: DataRepresentation *SetHierarchyFromInputConnection(
            AlgorithmOutput *conn)
        Set the tree and graph representations to the appropriate input
        ports.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetHierarchyFromInputConnection, *my_args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('edge_label_array_name', 'GetEdgeLabelArrayName'),
    ('color_vertices', 'GetColorVertices'), ('render_on_mouse_move',
    'GetRenderOnMouseMove'), ('interaction_mode', 'GetInteractionMode'),
    ('label_render_mode', 'GetLabelRenderMode'),
    ('edge_scalar_bar_visibility', 'GetEdgeScalarBarVisibility'),
    ('selection_mode', 'GetSelectionMode'), ('bundling_strength',
    'GetBundlingStrength'), ('vertex_label_font_size',
    'GetVertexLabelFontSize'), ('reference_count', 'GetReferenceCount'),
    ('display_hover_text', 'GetDisplayHoverText'),
    ('graph_edge_label_visibility', 'GetGraphEdgeLabelVisibility'),
    ('enabled_vertices_array_name', 'GetEnabledVerticesArrayName'),
    ('edge_label_visibility', 'GetEdgeLabelVisibility'),
    ('vertex_color_array_name', 'GetVertexColorArrayName'),
    ('edge_color_array_name', 'GetEdgeColorArrayName'),
    ('enable_edges_by_array', 'GetEnableEdgesByArray'),
    ('scaling_array_name', 'GetScalingArrayName'),
    ('graph_edge_label_font_size', 'GetGraphEdgeLabelFontSize'),
    ('enable_vertices_by_array', 'GetEnableVerticesByArray'),
    ('label_placement_mode', 'GetLabelPlacementMode'),
    ('hide_vertex_labels_on_interaction',
    'GetHideVertexLabelsOnInteraction'), ('enabled_edges_array_name',
    'GetEnabledEdgesArrayName'), ('icon_visibility', 'GetIconVisibility'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('color_graph_edges_by_array', 'GetColorGraphEdgesByArray'),
    ('hide_edge_labels_on_interaction', 'GetHideEdgeLabelsOnInteraction'),
    ('graph_edge_label_array_name', 'GetGraphEdgeLabelArrayName'),
    ('vertex_label_visibility', 'GetVertexLabelVisibility'),
    ('edge_label_font_size', 'GetEdgeLabelFontSize'), ('graph_visibility',
    'GetGraphVisibility'), ('debug', 'GetDebug'), ('icon_array_name',
    'GetIconArrayName'), ('glyph_type', 'GetGlyphType'),
    ('edge_visibility', 'GetEdgeVisibility'),
    ('vertex_scalar_bar_visibility', 'GetVertexScalarBarVisibility'),
    ('icon_size', 'GetIconSize'), ('scaled_glyphs', 'GetScaledGlyphs'),
    ('graph_edge_color_array_name', 'GetGraphEdgeColorArrayName'),
    ('vertex_label_array_name', 'GetVertexLabelArrayName'),
    ('color_edges', 'GetColorEdges'))
    
    _full_traitnames_list_ = \
    (['color_edges', 'color_graph_edges_by_array', 'color_vertices',
    'debug', 'display_hover_text', 'edge_label_visibility',
    'edge_visibility', 'global_warning_display',
    'graph_edge_label_visibility', 'graph_visibility',
    'hide_edge_labels_on_interaction',
    'hide_vertex_labels_on_interaction', 'icon_visibility',
    'render_on_mouse_move', 'scaled_glyphs', 'vertex_label_visibility',
    'interaction_mode', 'label_placement_mode', 'label_render_mode',
    'selection_mode', 'bundling_strength', 'edge_color_array_name',
    'edge_label_array_name', 'edge_label_font_size',
    'edge_scalar_bar_visibility', 'enable_edges_by_array',
    'enable_vertices_by_array', 'enabled_edges_array_name',
    'enabled_vertices_array_name', 'glyph_type',
    'graph_edge_color_array_name', 'graph_edge_label_array_name',
    'graph_edge_label_font_size', 'icon_array_name', 'icon_size',
    'scaling_array_name', 'vertex_color_array_name',
    'vertex_label_array_name', 'vertex_label_font_size',
    'vertex_scalar_bar_visibility'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HierarchicalGraphView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HierarchicalGraphView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['color_edges', 'color_graph_edges_by_array',
            'color_vertices', 'display_hover_text', 'edge_label_visibility',
            'edge_visibility', 'graph_edge_label_visibility', 'graph_visibility',
            'hide_edge_labels_on_interaction',
            'hide_vertex_labels_on_interaction', 'icon_visibility',
            'render_on_mouse_move', 'scaled_glyphs', 'vertex_label_visibility'],
            ['interaction_mode', 'label_placement_mode', 'label_render_mode',
            'selection_mode'], ['bundling_strength', 'edge_color_array_name',
            'edge_label_array_name', 'edge_label_font_size',
            'edge_scalar_bar_visibility', 'enable_edges_by_array',
            'enable_vertices_by_array', 'enabled_edges_array_name',
            'enabled_vertices_array_name', 'glyph_type',
            'graph_edge_color_array_name', 'graph_edge_label_array_name',
            'graph_edge_label_font_size', 'icon_array_name', 'icon_size',
            'scaling_array_name', 'vertex_color_array_name',
            'vertex_label_array_name', 'vertex_label_font_size',
            'vertex_scalar_bar_visibility']),
            title='Edit HierarchicalGraphView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HierarchicalGraphView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

