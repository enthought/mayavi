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

from tvtk.tvtk_classes.rendered_graph_representation import RenderedGraphRepresentation


class RenderedHierarchyRepresentation(RenderedGraphRepresentation):
    """
    RenderedHierarchyRepresentation - 
    
    Superclass: RenderedGraphRepresentation
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderedHierarchyRepresentation, obj, update, **traits)
    
    graph_edge_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _graph_edge_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelVisibility,
                        self.graph_edge_label_visibility_)

    color_graph_edges_by_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _color_graph_edges_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorGraphEdgesByArray,
                        self.color_graph_edges_by_array_)

    graph_visibility = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _graph_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphVisibility,
                        self.graph_visibility_)

    def get_graph_spline_type(self, *args):
        """
        V.get_graph_spline_type(int) -> int
        C++: virtual int GetGraphSplineType(int idx)
        Sets the spline type for the graph edges.
        SplineGraphEdges::CUSTOM uses a CardinalSpline.
        SplineGraphEdges::BSPLINE uses a b-spline. The default is
        BSPLINE.
        """
        ret = self._wrap_call(self._vtk_obj.GetGraphSplineType, *args)
        return ret

    def set_graph_spline_type(self, *args):
        """
        V.set_graph_spline_type(int, int)
        C++: virtual void SetGraphSplineType(int type, int idx)
        Sets the spline type for the graph edges.
        SplineGraphEdges::CUSTOM uses a CardinalSpline.
        SplineGraphEdges::BSPLINE uses a b-spline. The default is
        BSPLINE.
        """
        ret = self._wrap_call(self._vtk_obj.SetGraphSplineType, *args)
        return ret

    graph_edge_color_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _graph_edge_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeColorArrayName,
                        self.graph_edge_color_array_name)

    bundling_strength = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _bundling_strength_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBundlingStrength,
                        self.bundling_strength)

    graph_edge_label_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _graph_edge_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelArrayName,
                        self.graph_edge_label_array_name)

    graph_edge_label_font_size = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _graph_edge_label_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelFontSize,
                        self.graph_edge_label_font_size)

    def set_graph_edge_color_to_spline_fraction(self, *args):
        """
        V.set_graph_edge_color_to_spline_fraction()
        C++: virtual void SetGraphEdgeColorToSplineFraction()
        V.set_graph_edge_color_to_spline_fraction(int)
        C++: virtual void SetGraphEdgeColorToSplineFraction(int idx)"""
        ret = self._wrap_call(self._vtk_obj.SetGraphEdgeColorToSplineFraction, *args)
        return ret

    _updateable_traits_ = \
    (('edge_icon_visibility', 'GetEdgeIconVisibility'),
    ('vertex_icon_alignment', 'GetVertexIconAlignment'),
    ('vertex_icon_priority_array_name', 'GetVertexIconPriorityArrayName'),
    ('edge_scalar_bar_visibility', 'GetEdgeScalarBarVisibility'),
    ('enabled_vertices_array_name', 'GetEnabledVerticesArrayName'),
    ('vertex_icon_selection_mode', 'GetVertexIconSelectionMode'),
    ('abort_execute', 'GetAbortExecute'), ('selection_array_name',
    'GetSelectionArrayName'), ('enable_edges_by_array',
    'GetEnableEdgesByArray'), ('graph_edge_label_font_size',
    'GetGraphEdgeLabelFontSize'), ('scaling_array_name',
    'GetScalingArrayName'), ('hide_edge_labels_on_interaction',
    'GetHideEdgeLabelsOnInteraction'), ('enable_vertices_by_array',
    'GetEnableVerticesByArray'), ('edge_icon_array_name',
    'GetEdgeIconArrayName'), ('enabled_edges_array_name',
    'GetEnabledEdgesArrayName'), ('vertex_icon_visibility',
    'GetVertexIconVisibility'), ('edge_icon_alignment',
    'GetEdgeIconAlignment'), ('edge_icon_priority_array_name',
    'GetEdgeIconPriorityArrayName'), ('progress_text', 'GetProgressText'),
    ('graph_visibility', 'GetGraphVisibility'), ('debug', 'GetDebug'),
    ('color_edges_by_array', 'GetColorEdgesByArray'),
    ('label_render_mode', 'GetLabelRenderMode'), ('glyph_type',
    'GetGlyphType'), ('vertex_hover_array_name',
    'GetVertexHoverArrayName'), ('edge_visibility', 'GetEdgeVisibility'),
    ('vertex_scalar_bar_visibility', 'GetVertexScalarBarVisibility'),
    ('progress', 'GetProgress'), ('color_vertices_by_array',
    'GetColorVerticesByArray'), ('graph_edge_color_array_name',
    'GetGraphEdgeColorArrayName'), ('edge_hover_array_name',
    'GetEdgeHoverArrayName'), ('edge_label_visibility',
    'GetEdgeLabelVisibility'), ('edge_label_array_name',
    'GetEdgeLabelArrayName'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('selection_type', 'GetSelectionType'), ('vertex_icon_array_name',
    'GetVertexIconArrayName'), ('use_edge_icon_type_map',
    'GetUseEdgeIconTypeMap'), ('bundling_strength',
    'GetBundlingStrength'), ('scaling', 'GetScaling'),
    ('color_graph_edges_by_array', 'GetColorGraphEdgesByArray'),
    ('graph_edge_label_visibility', 'GetGraphEdgeLabelVisibility'),
    ('edge_color_array_name', 'GetEdgeColorArrayName'),
    ('vertex_color_array_name', 'GetVertexColorArrayName'), ('selectable',
    'GetSelectable'), ('hide_vertex_labels_on_interaction',
    'GetHideVertexLabelsOnInteraction'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('vertex_selected_icon',
    'GetVertexSelectedIcon'), ('vertex_default_icon',
    'GetVertexDefaultIcon'), ('graph_edge_label_array_name',
    'GetGraphEdgeLabelArrayName'), ('vertex_label_visibility',
    'GetVertexLabelVisibility'), ('vertex_label_priority_array_name',
    'GetVertexLabelPriorityArrayName'), ('use_vertex_icon_type_map',
    'GetUseVertexIconTypeMap'), ('edge_label_priority_array_name',
    'GetEdgeLabelPriorityArrayName'), ('reference_count',
    'GetReferenceCount'), ('vertex_label_array_name',
    'GetVertexLabelArrayName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'color_edges_by_array',
    'color_graph_edges_by_array', 'color_vertices_by_array', 'debug',
    'edge_icon_visibility', 'edge_label_visibility', 'edge_visibility',
    'enable_edges_by_array', 'enable_vertices_by_array',
    'global_warning_display', 'graph_edge_label_visibility',
    'graph_visibility', 'hide_edge_labels_on_interaction',
    'hide_vertex_labels_on_interaction', 'release_data_flag', 'scaling',
    'selectable', 'use_edge_icon_type_map', 'use_vertex_icon_type_map',
    'vertex_icon_visibility', 'vertex_label_visibility',
    'vertex_icon_selection_mode', 'bundling_strength',
    'edge_color_array_name', 'edge_hover_array_name',
    'edge_icon_alignment', 'edge_icon_array_name',
    'edge_icon_priority_array_name', 'edge_label_array_name',
    'edge_label_priority_array_name', 'edge_scalar_bar_visibility',
    'enabled_edges_array_name', 'enabled_vertices_array_name',
    'glyph_type', 'graph_edge_color_array_name',
    'graph_edge_label_array_name', 'graph_edge_label_font_size',
    'label_render_mode', 'progress_text', 'scaling_array_name',
    'selection_array_name', 'selection_type', 'vertex_color_array_name',
    'vertex_default_icon', 'vertex_hover_array_name',
    'vertex_icon_alignment', 'vertex_icon_array_name',
    'vertex_icon_priority_array_name', 'vertex_label_array_name',
    'vertex_label_priority_array_name', 'vertex_scalar_bar_visibility',
    'vertex_selected_icon'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderedHierarchyRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderedHierarchyRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['color_edges_by_array', 'color_graph_edges_by_array',
            'color_vertices_by_array', 'edge_icon_visibility',
            'edge_label_visibility', 'edge_visibility', 'enable_edges_by_array',
            'enable_vertices_by_array', 'graph_edge_label_visibility',
            'graph_visibility', 'hide_edge_labels_on_interaction',
            'hide_vertex_labels_on_interaction', 'scaling', 'selectable',
            'use_edge_icon_type_map', 'use_vertex_icon_type_map',
            'vertex_icon_visibility', 'vertex_label_visibility'],
            ['vertex_icon_selection_mode'], ['bundling_strength',
            'edge_color_array_name', 'edge_hover_array_name',
            'edge_icon_alignment', 'edge_icon_array_name',
            'edge_icon_priority_array_name', 'edge_label_array_name',
            'edge_label_priority_array_name', 'edge_scalar_bar_visibility',
            'enabled_edges_array_name', 'enabled_vertices_array_name',
            'glyph_type', 'graph_edge_color_array_name',
            'graph_edge_label_array_name', 'graph_edge_label_font_size',
            'label_render_mode', 'scaling_array_name', 'selection_array_name',
            'selection_type', 'vertex_color_array_name', 'vertex_default_icon',
            'vertex_hover_array_name', 'vertex_icon_alignment',
            'vertex_icon_array_name', 'vertex_icon_priority_array_name',
            'vertex_label_array_name', 'vertex_label_priority_array_name',
            'vertex_scalar_bar_visibility', 'vertex_selected_icon']),
            title='Edit RenderedHierarchyRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderedHierarchyRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

