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

from tvtk.tvtk_classes.render_view import RenderView


class GraphLayoutView(RenderView):
    """
    GraphLayoutView - Lays out and displays a graph
    
    Superclass: RenderView
    
    GraphLayoutView performs graph layout and displays a Graph. You
    may color and label the vertices and edges using fields in the graph.
    If coordinates are already assigned to the graph vertices in your
    graph, set the layout strategy to pass_through in this view. The
    default layout is fast2d which is fast but not that good, for better
    layout set the layout to simple2d or force_directed. There are also
    tree and circle layout strategies. :)
    
    .SEE ALSO Fast2DLayoutStrategy Simple2DLayoutStrategy
    ForceDirectedLayoutStrategy
    
    Thanks:
    
    Thanks a bunch to the holographic unfolding pattern.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphLayoutView, obj, update, **traits)
    
    scaled_glyphs = tvtk_base.false_bool_trait(help=\
        """
        Whether to use scaled glyphs or not.  Default is off.
        """
    )
    def _scaled_glyphs_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaledGlyphs,
                        self.scaled_glyphs_)

    edge_visibility = tvtk_base.true_bool_trait(help=\
        """
        Whether to show the edges at all. Default is on
        """
    )
    def _edge_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeVisibility,
                        self.edge_visibility_)

    color_edges = tvtk_base.false_bool_trait(help=\
        """
        Whether to color edges.  Default is off.
        """
    )
    def _color_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorEdges,
                        self.color_edges_)

    edge_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether to show edge labels.  Default is off.
        """
    )
    def _edge_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLabelVisibility,
                        self.edge_label_visibility_)

    icon_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether icons are visible (default off).
        """
    )
    def _icon_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconVisibility,
                        self.icon_visibility_)

    vertex_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether to show vertex labels.  Default is off.
        """
    )
    def _vertex_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexLabelVisibility,
                        self.vertex_label_visibility_)

    hide_vertex_labels_on_interaction = tvtk_base.false_bool_trait(help=\
        """
        Whether to hide vertex labels during mouse interactions.  Default
        is off.
        """
    )
    def _hide_vertex_labels_on_interaction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHideVertexLabelsOnInteraction,
                        self.hide_vertex_labels_on_interaction_)

    hide_edge_labels_on_interaction = tvtk_base.false_bool_trait(help=\
        """
        Whether to hide edge labels during mouse interactions.  Default
        is off.
        """
    )
    def _hide_edge_labels_on_interaction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHideEdgeLabelsOnInteraction,
                        self.hide_edge_labels_on_interaction_)

    color_vertices = tvtk_base.false_bool_trait(help=\
        """
        Whether to color vertices.  Default is off.
        """
    )
    def _color_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorVertices,
                        self.color_vertices_)

    def get_layout_strategy(self):
        """
        V.get_layout_strategy() -> GraphLayoutStrategy
        C++: GraphLayoutStrategy *GetLayoutStrategy()
        The layout strategy to use when performing the graph layout. This
        signature allows an application to create a layout object
        directly and simply set the pointer through this method.
        """
        ret = wrap_vtk(self._vtk_obj.GetLayoutStrategy())
        return ret
        

    def set_layout_strategy_to_clustering2d(self):
        """
        V.set_layout_strategy_to_clustering2d()
        C++: void SetLayoutStrategyToClustering2D()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToClustering2D()

    def set_layout_strategy_to_community2d(self):
        """
        V.set_layout_strategy_to_community2d()
        C++: void SetLayoutStrategyToCommunity2D()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToCommunity2D()

    def set_layout_strategy_to_cone(self):
        """
        V.set_layout_strategy_to_cone()
        C++: void SetLayoutStrategyToCone()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToCone()

    def set_layout_strategy_to_cosmic_tree(self):
        """
        V.set_layout_strategy_to_cosmic_tree()
        C++: void SetLayoutStrategyToCosmicTree()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToCosmicTree()

    def set_layout_strategy_to_fast2d(self):
        """
        V.set_layout_strategy_to_fast2d()
        C++: void SetLayoutStrategyToFast2D()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToFast2D()

    def set_layout_strategy_to_force_directed(self):
        """
        V.set_layout_strategy_to_force_directed()
        C++: void SetLayoutStrategyToForceDirected()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToForceDirected()

    def set_layout_strategy_to_pass_through(self):
        """
        V.set_layout_strategy_to_pass_through()
        C++: void SetLayoutStrategyToPassThrough()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToPassThrough()

    def set_layout_strategy_to_random(self):
        """
        V.set_layout_strategy_to_random()
        C++: void SetLayoutStrategyToRandom()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToRandom()

    def set_layout_strategy_to_simple2d(self):
        """
        V.set_layout_strategy_to_simple2d()
        C++: void SetLayoutStrategyToSimple2D()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToSimple2D()

    def set_layout_strategy_to_span_tree(self):
        """
        V.set_layout_strategy_to_span_tree()
        C++: void SetLayoutStrategyToSpanTree()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToSpanTree()

    def set_layout_strategy_to_tree(self):
        """
        V.set_layout_strategy_to_tree()
        C++: void SetLayoutStrategyToTree()
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
        self._vtk_obj.SetLayoutStrategyToTree()

    def get_edge_layout_strategy(self):
        """
        V.get_edge_layout_strategy() -> EdgeLayoutStrategy
        C++: EdgeLayoutStrategy *GetEdgeLayoutStrategy()
        The layout strategy to use when performing the edge layout. This
        signature allows an application to create a layout object
        directly and simply set the pointer through this method.
        """
        ret = wrap_vtk(self._vtk_obj.GetEdgeLayoutStrategy())
        return ret
        

    def set_edge_layout_strategy_to_arc_parallel(self):
        """
        V.set_edge_layout_strategy_to_arc_parallel()
        C++: void SetEdgeLayoutStrategyToArcParallel()
        The layout strategy to use when performing the edge layout. The
        possible strings are:
          "Arc Parallel"   - Arc parallel edges and self loops.
          "Pass Through"   - Use edge routes assigned to the input.
        Default is "Arc Parallel".
        """
        self._vtk_obj.SetEdgeLayoutStrategyToArcParallel()

    def set_edge_layout_strategy_to_pass_through(self):
        """
        V.set_edge_layout_strategy_to_pass_through()
        C++: void SetEdgeLayoutStrategyToPassThrough()
        The layout strategy to use when performing the edge layout. The
        possible strings are:
          "Arc Parallel"   - Arc parallel edges and self loops.
          "Pass Through"   - Use edge routes assigned to the input.
        Default is "Arc Parallel".
        """
        self._vtk_obj.SetEdgeLayoutStrategyToPassThrough()

    edge_color_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for coloring edges.  Default is "color".
        """
    )
    def _edge_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeColorArrayName,
                        self.edge_color_array_name)

    vertex_label_array_name = traits.String(r"VertexDegree", enter_set=True, auto_set=False, help=\
        """
        The array to use for vertex labeling.  Default is "label".
        """
    )
    def _vertex_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexLabelArrayName,
                        self.vertex_label_array_name)

    edge_label_font_size = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        The size of the font used for edge labeling
        """
    )
    def _edge_label_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLabelFontSize,
                        self.edge_label_font_size)

    enable_edges_by_array = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Whether to color edges.  Default is off.
        """
    )
    def _enable_edges_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableEdgesByArray,
                        self.enable_edges_by_array)

    edge_scalar_bar_visibility = traits.Bool(False, help=\
        """
        Whether the scalar bar for edges is visible.  Default is off.
        """
    )
    def _edge_scalar_bar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeScalarBarVisibility,
                        self.edge_scalar_bar_visibility)

    scaling_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array used for scaling (if scaled_glyphs is ON)
        """
    )
    def _scaling_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalingArrayName,
                        self.scaling_array_name)

    edge_label_array_name = traits.String(r"LabelText", enter_set=True, auto_set=False, help=\
        """
        The array to use for edge labeling.  Default is "label".
        """
    )
    def _edge_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLabelArrayName,
                        self.edge_label_array_name)

    enabled_edges_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for coloring edges.
        """
    )
    def _enabled_edges_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnabledEdgesArrayName,
                        self.enabled_edges_array_name)

    vertex_color_array_name = traits.String(r"VertexDegree", enter_set=True, auto_set=False, help=\
        """
        The array to use for coloring vertices.  The default behavior is
        to color by vertex degree.
        """
    )
    def _vertex_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexColorArrayName,
                        self.vertex_color_array_name)

    vertex_scalar_bar_visibility = traits.Bool(False, help=\
        """
        Whether the scalar bar for vertices is visible.  Default is off.
        """
    )
    def _vertex_scalar_bar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexScalarBarVisibility,
                        self.vertex_scalar_bar_visibility)

    glyph_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        The type of glyph to use for the vertices
        """
    )
    def _glyph_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlyphType,
                        self.glyph_type)

    icon_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array used for assigning icons
        """
    )
    def _icon_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconArrayName,
                        self.icon_array_name)

    enable_vertices_by_array = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Whether to color vertices.  Default is off.
        """
    )
    def _enable_vertices_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableVerticesByArray,
                        self.enable_vertices_by_array)

    enabled_vertices_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for coloring vertices.
        """
    )
    def _enabled_vertices_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnabledVerticesArrayName,
                        self.enabled_vertices_array_name)

    vertex_label_font_size = traits.Int(12, enter_set=True, auto_set=False, help=\
        """
        The size of the font used for vertex labeling
        """
    )
    def _vertex_label_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexLabelFontSize,
                        self.vertex_label_font_size)

    def _get_edge_layout_strategy_name(self):
        return self._vtk_obj.GetEdgeLayoutStrategyName()
    edge_layout_strategy_name = traits.Property(_get_edge_layout_strategy_name, help=\
        """
        The layout strategy to use when performing the edge layout. The
        possible strings are:
          "Arc Parallel"   - Arc parallel edges and self loops.
          "Pass Through"   - Use edge routes assigned to the input.
        Default is "Arc Parallel".
        """
    )

    def _get_layout_strategy_name(self):
        return self._vtk_obj.GetLayoutStrategyName()
    layout_strategy_name = traits.Property(_get_layout_strategy_name, help=\
        """
        The layout strategy to use when performing the graph layout. The
        possible strings are:
        - "Random"         Randomly places vertices in a box.
        - "Force Directed" A layout in 3d or 2d simulating forces on
          edges.
        - "Simple 2d"      A simple 2d force directed layout.
        - "Clustering 2d"  A 2d force directed layout that's just like
          simple 2d but uses some techniques to cluster better.
        - "Community 2d"   A linear-time 2d layout that's just like Fast
          2d but looks for and uses a community array to 'accentuate'
          clusters.
        - "Fast 2d"       A linear-time 2d layout.
        - "Pass Through"  Use locations assigned to the input.
        - "Circular"      Places vertices uniformly on a circle.
        - "Cone"          Cone tree layout.
        - "Span Tree"     Span Tree Layout. Default is "Simple 2d".
        """
    )

    def add_icon_type(self, *args):
        """
        V.add_icon_type(string, int)
        C++: void AddIconType(char *type, int index)
        Associate the icon at index "index" in the Texture to all
        vertices containing "type" as a value in the vertex attribute
        array specified by icon_array_name.
        """
        ret = self._wrap_call(self._vtk_obj.AddIconType, *args)
        return ret

    def clear_icon_types(self):
        """
        V.clear_icon_types()
        C++: void ClearIconTypes()
        Clear all icon mappings.
        """
        ret = self._vtk_obj.ClearIconTypes()
        return ret
        

    def is_layout_complete(self):
        """
        V.is_layout_complete() -> int
        C++: virtual int IsLayoutComplete()
        Is the graph layout complete? This method is useful for when the
        strategy is iterative and the application wants to show the
        iterative progress of the graph layout See Also: update_layout();
        """
        ret = self._vtk_obj.IsLayoutComplete()
        return ret
        

    def set_icon_alignment(self, *args):
        """
        V.set_icon_alignment(int)
        C++: void SetIconAlignment(int alignment)
        Specify where the icons should be placed in relation to the
        vertex. See IconGlyphFilter.h for possible values.
        """
        ret = self._wrap_call(self._vtk_obj.SetIconAlignment, *args)
        return ret

    def update_layout(self):
        """
        V.update_layout()
        C++: virtual void UpdateLayout()
        This method is useful for when the strategy is iterative and the
        application wants to show the iterative progress of the graph
        layout. The application would have something like
        while(!_is_layout_complete())
          {
          update_layout();
          } See Also: is_layout_complete();
        """
        ret = self._vtk_obj.UpdateLayout()
        return ret
        

    def zoom_to_selection(self):
        """
        V.zoom_to_selection()
        C++: void ZoomToSelection()
        Reset the camera based on the bounds of the selected region.
        """
        ret = self._vtk_obj.ZoomToSelection()
        return ret
        

    _updateable_traits_ = \
    (('edge_label_array_name', 'GetEdgeLabelArrayName'),
    ('color_vertices', 'GetColorVertices'), ('render_on_mouse_move',
    'GetRenderOnMouseMove'), ('interaction_mode', 'GetInteractionMode'),
    ('label_render_mode', 'GetLabelRenderMode'),
    ('edge_scalar_bar_visibility', 'GetEdgeScalarBarVisibility'),
    ('selection_mode', 'GetSelectionMode'),
    ('enabled_vertices_array_name', 'GetEnabledVerticesArrayName'),
    ('vertex_label_font_size', 'GetVertexLabelFontSize'), ('icon_size',
    'GetIconSize'), ('display_hover_text', 'GetDisplayHoverText'),
    ('edge_label_visibility', 'GetEdgeLabelVisibility'),
    ('enable_edges_by_array', 'GetEnableEdgesByArray'),
    ('edge_color_array_name', 'GetEdgeColorArrayName'),
    ('vertex_color_array_name', 'GetVertexColorArrayName'),
    ('scaling_array_name', 'GetScalingArrayName'),
    ('hide_edge_labels_on_interaction', 'GetHideEdgeLabelsOnInteraction'),
    ('enable_vertices_by_array', 'GetEnableVerticesByArray'),
    ('label_placement_mode', 'GetLabelPlacementMode'),
    ('hide_vertex_labels_on_interaction',
    'GetHideVertexLabelsOnInteraction'), ('enabled_edges_array_name',
    'GetEnabledEdgesArrayName'), ('scaled_glyphs', 'GetScaledGlyphs'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('vertex_label_visibility', 'GetVertexLabelVisibility'), ('debug',
    'GetDebug'), ('edge_label_font_size', 'GetEdgeLabelFontSize'),
    ('icon_array_name', 'GetIconArrayName'), ('glyph_type',
    'GetGlyphType'), ('edge_visibility', 'GetEdgeVisibility'),
    ('vertex_scalar_bar_visibility', 'GetVertexScalarBarVisibility'),
    ('reference_count', 'GetReferenceCount'), ('icon_visibility',
    'GetIconVisibility'), ('vertex_label_array_name',
    'GetVertexLabelArrayName'), ('color_edges', 'GetColorEdges'))
    
    _full_traitnames_list_ = \
    (['color_edges', 'color_vertices', 'debug', 'display_hover_text',
    'edge_label_visibility', 'edge_visibility', 'global_warning_display',
    'hide_edge_labels_on_interaction',
    'hide_vertex_labels_on_interaction', 'icon_visibility',
    'render_on_mouse_move', 'scaled_glyphs', 'vertex_label_visibility',
    'interaction_mode', 'label_placement_mode', 'label_render_mode',
    'selection_mode', 'edge_color_array_name', 'edge_label_array_name',
    'edge_label_font_size', 'edge_scalar_bar_visibility',
    'enable_edges_by_array', 'enable_vertices_by_array',
    'enabled_edges_array_name', 'enabled_vertices_array_name',
    'glyph_type', 'icon_array_name', 'icon_size', 'scaling_array_name',
    'vertex_color_array_name', 'vertex_label_array_name',
    'vertex_label_font_size', 'vertex_scalar_bar_visibility'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphLayoutView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphLayoutView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['color_edges', 'color_vertices', 'display_hover_text',
            'edge_label_visibility', 'edge_visibility',
            'hide_edge_labels_on_interaction',
            'hide_vertex_labels_on_interaction', 'icon_visibility',
            'render_on_mouse_move', 'scaled_glyphs', 'vertex_label_visibility'],
            ['interaction_mode', 'label_placement_mode', 'label_render_mode',
            'selection_mode'], ['edge_color_array_name', 'edge_label_array_name',
            'edge_label_font_size', 'edge_scalar_bar_visibility',
            'enable_edges_by_array', 'enable_vertices_by_array',
            'enabled_edges_array_name', 'enabled_vertices_array_name',
            'glyph_type', 'icon_array_name', 'icon_size', 'scaling_array_name',
            'vertex_color_array_name', 'vertex_label_array_name',
            'vertex_label_font_size', 'vertex_scalar_bar_visibility']),
            title='Edit GraphLayoutView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphLayoutView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

