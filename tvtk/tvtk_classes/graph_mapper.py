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

from tvtk.tvtk_classes.mapper import Mapper


class GraphMapper(Mapper):
    """
    GraphMapper - map Graph and derived 
    
    Superclass: Mapper
    
    GraphMapper is a mapper to map Graph (and all derived classes)
    to graphics primitives.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphMapper, obj, update, **traits)
    
    scaled_glyphs = tvtk_base.false_bool_trait(help=\
        """
        Whether scaled glyphs are on or not.  Default is off. By default
        this mapper uses vertex glyphs that do not scale. If you turn
        this option on you will get circles at each vertex and they will
        scale as you zoom in/out.
        """
    )
    def _scaled_glyphs_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaledGlyphs,
                        self.scaled_glyphs_)

    enable_edges_by_array = tvtk_base.false_bool_trait(help=\
        """
        Whether to enable/disable edges using array values.  Default is
        off.
        """
    )
    def _enable_edges_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableEdgesByArray,
                        self.enable_edges_by_array_)

    edge_visibility = tvtk_base.true_bool_trait(help=\
        """
        Whether to show edges or not.  Default is on.
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

    icon_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether to show icons.  Default is off.
        """
    )
    def _icon_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconVisibility,
                        self.icon_visibility_)

    enable_vertices_by_array = tvtk_base.false_bool_trait(help=\
        """
        Whether to enable/disable vertices using array values.  Default
        is off.
        """
    )
    def _enable_vertices_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableVerticesByArray,
                        self.enable_vertices_by_array_)

    color_vertices = tvtk_base.false_bool_trait(help=\
        """
        Whether to color vertices.  Default is off.
        """
    )
    def _color_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorVertices,
                        self.color_vertices_)

    edge_color_array_name = traits.String(r"weight", enter_set=True, auto_set=False, help=\
        """
        The array to use for coloring edges.  Default is "color".
        """
    )
    def _edge_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeColorArrayName,
                        self.edge_color_array_name)

    enabled_edges_array_name = traits.String(r"weight", enter_set=True, auto_set=False, help=\
        """
        The array to use for coloring edges.  Default is "color".
        """
    )
    def _enabled_edges_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnabledEdgesArrayName,
                        self.enabled_edges_array_name)

    vertex_color_array_name = traits.String(r"VertexDegree", enter_set=True, auto_set=False, help=\
        """
        The array to use for coloring vertices.  Default is "color".
        """
    )
    def _vertex_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexColorArrayName,
                        self.vertex_color_array_name)

    vertex_point_size = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the vertex point size
        """
    )
    def _vertex_point_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexPointSize,
                        self.vertex_point_size)

    edge_line_width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the edge line width
        """
    )
    def _edge_line_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLineWidth,
                        self.edge_line_width)

    icon_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for assigning icons.
        """
    )
    def _icon_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconArrayName,
                        self.icon_array_name)

    scaling_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Glyph scaling array name. Default is "scale"
        """
    )
    def _scaling_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalingArrayName,
                        self.scaling_array_name)

    enabled_vertices_array_name = traits.String(r"VertexDegree", enter_set=True, auto_set=False, help=\
        """
        The array to use for coloring edges.  Default is "color".
        """
    )
    def _enabled_vertices_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnabledVerticesArrayName,
                        self.enabled_vertices_array_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the Input of this mapper.
        """
    )

    def _get_icon_texture(self):
        return wrap_vtk(self._vtk_obj.GetIconTexture())
    def _set_icon_texture(self, arg):
        old_val = self._get_icon_texture()
        self._wrap_call(self._vtk_obj.SetIconTexture,
                        deref_vtk(arg))
        self.trait_property_changed('icon_texture', old_val, arg)
    icon_texture = traits.Property(_get_icon_texture, _set_icon_texture, help=\
        """
        The texture containing the icon sheet.
        """
    )

    def _get_edge_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetEdgeLookupTable())
    edge_lookup_table = traits.Property(_get_edge_lookup_table, help=\
        """
        Access to the lookup tables used by the vertex and edge mappers.
        """
    )

    def _get_vertex_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetVertexLookupTable())
    vertex_lookup_table = traits.Property(_get_vertex_lookup_table, help=\
        """
        Access to the lookup tables used by the vertex and edge mappers.
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

    def apply_view_theme(self, *args):
        """
        V.apply_view_theme(ViewTheme)
        C++: virtual void ApplyViewTheme(ViewTheme *theme)
        Apply the theme to this view.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyViewTheme, *my_args)
        return ret

    def clear_icon_types(self):
        """
        V.clear_icon_types()
        C++: void ClearIconTypes()
        Clear all icon mappings.
        """
        ret = self._vtk_obj.ClearIconTypes()
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

    _updateable_traits_ = \
    (('immediate_mode_rendering', 'GetImmediateModeRendering'),
    ('color_vertices', 'GetColorVertices'), ('vertex_point_size',
    'GetVertexPointSize'), ('edge_line_width', 'GetEdgeLineWidth'),
    ('scalar_mode', 'GetScalarMode'), ('edge_visibility',
    'GetEdgeVisibility'), ('scaled_glyphs', 'GetScaledGlyphs'),
    ('enabled_vertices_array_name', 'GetEnabledVerticesArrayName'),
    ('edge_color_array_name', 'GetEdgeColorArrayName'), ('static',
    'GetStatic'), ('resolve_coincident_topology',
    'GetResolveCoincidentTopology'), ('force_compile_only',
    'GetForceCompileOnly'), ('enable_edges_by_array',
    'GetEnableEdgesByArray'), ('resolve_coincident_topology_z_shift',
    'GetResolveCoincidentTopologyZShift'), ('vertex_color_array_name',
    'GetVertexColorArrayName'), ('scalar_visibility',
    'GetScalarVisibility'), ('scaling_array_name', 'GetScalingArrayName'),
    ('enable_vertices_by_array', 'GetEnableVerticesByArray'),
    ('enabled_edges_array_name', 'GetEnabledEdgesArrayName'),
    ('icon_visibility', 'GetIconVisibility'), ('color_mode',
    'GetColorMode'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interpolate_scalars_before_mapping',
    'GetInterpolateScalarsBeforeMapping'), ('scalar_material_mode',
    'GetScalarMaterialMode'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('use_lookup_table_scalar_range',
    'GetUseLookupTableScalarRange'), ('icon_array_name',
    'GetIconArrayName'), ('abort_execute', 'GetAbortExecute'),
    ('color_edges', 'GetColorEdges'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'),
    ('resolve_coincident_topology_polygon_offset_faces',
    'GetResolveCoincidentTopologyPolygonOffsetFaces'),
    ('global_immediate_mode_rendering',
    'GetGlobalImmediateModeRendering'), ('scalar_range',
    'GetScalarRange'), ('render_time', 'GetRenderTime'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'color_edges', 'color_vertices', 'debug',
    'edge_visibility', 'enable_edges_by_array',
    'enable_vertices_by_array', 'global_immediate_mode_rendering',
    'global_warning_display', 'icon_visibility',
    'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
    'release_data_flag', 'scalar_visibility', 'scaled_glyphs', 'static',
    'use_lookup_table_scalar_range', 'color_mode',
    'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode',
    'edge_color_array_name', 'edge_line_width',
    'enabled_edges_array_name', 'enabled_vertices_array_name',
    'force_compile_only', 'icon_array_name', 'progress_text',
    'render_time', 'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range',
    'scaling_array_name', 'vertex_color_array_name', 'vertex_point_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['color_edges', 'color_vertices', 'edge_visibility',
            'enable_edges_by_array', 'enable_vertices_by_array',
            'global_immediate_mode_rendering', 'icon_visibility',
            'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
            'scalar_visibility', 'scaled_glyphs', 'static',
            'use_lookup_table_scalar_range'], ['color_mode',
            'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode'],
            ['edge_color_array_name', 'edge_line_width',
            'enabled_edges_array_name', 'enabled_vertices_array_name',
            'force_compile_only', 'icon_array_name', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range',
            'scaling_array_name', 'vertex_color_array_name',
            'vertex_point_size']),
            title='Edit GraphMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

