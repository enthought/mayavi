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

from tvtk.tvtk_classes.poly_data_mapper import PolyDataMapper


class PainterPolyDataMapper(PolyDataMapper):
    """
    PainterPolyDataMapper - poly_data_mapper using painters
    
    Superclass: PolyDataMapper
    
    poly_data_mapper that uses painters to do the actual rendering.
    
    Thanks:
    
    Support for generic vertex attributes in VTK was contributed in
    collaboration with Stephane Ploix at EDF.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPainterPolyDataMapper, obj, update, **traits)
    
    def _get_painter(self):
        return wrap_vtk(self._vtk_obj.GetPainter())
    def _set_painter(self, arg):
        old_val = self._get_painter()
        self._wrap_call(self._vtk_obj.SetPainter,
                        deref_vtk(arg))
        self.trait_property_changed('painter', old_val, arg)
    painter = traits.Property(_get_painter, _set_painter, help=\
        """
        Get/Set the painter used to do the actual rendering. By default,
        DefaultPainter is used to build the rendering painter chain
        for color mapping/clipping etc. followed by a ChooserPainter
        which renders the primitives.
        """
    )

    def _get_selection_painter(self):
        return wrap_vtk(self._vtk_obj.GetSelectionPainter())
    def _set_selection_painter(self, arg):
        old_val = self._get_selection_painter()
        self._wrap_call(self._vtk_obj.SetSelectionPainter,
                        deref_vtk(arg))
        self.trait_property_changed('selection_painter', old_val, arg)
    selection_painter = traits.Property(_get_selection_painter, _set_selection_painter, help=\
        """
        Get/Set the painter used when rendering the selection pass.
        """
    )

    _updateable_traits_ = \
    (('immediate_mode_rendering', 'GetImmediateModeRendering'),
    ('resolve_coincident_topology_polygon_offset_faces',
    'GetResolveCoincidentTopologyPolygonOffsetFaces'), ('scalar_mode',
    'GetScalarMode'), ('scalar_material_mode', 'GetScalarMaterialMode'),
    ('debug', 'GetDebug'), ('static', 'GetStatic'), ('force_compile_only',
    'GetForceCompileOnly'), ('resolve_coincident_topology_z_shift',
    'GetResolveCoincidentTopologyZShift'), ('ghost_level',
    'GetGhostLevel'), ('scalar_visibility', 'GetScalarVisibility'),
    ('color_mode', 'GetColorMode'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interpolate_scalars_before_mapping',
    'GetInterpolateScalarsBeforeMapping'), ('progress_text',
    'GetProgressText'), ('global_immediate_mode_rendering',
    'GetGlobalImmediateModeRendering'), ('use_lookup_table_scalar_range',
    'GetUseLookupTableScalarRange'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_sub_pieces', 'GetNumberOfSubPieces'),
    ('resolve_coincident_topology', 'GetResolveCoincidentTopology'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('piece',
    'GetPiece'), ('number_of_pieces', 'GetNumberOfPieces'),
    ('scalar_range', 'GetScalarRange'), ('render_time', 'GetRenderTime'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_immediate_mode_rendering',
    'global_warning_display', 'immediate_mode_rendering',
    'interpolate_scalars_before_mapping', 'release_data_flag',
    'scalar_visibility', 'static', 'use_lookup_table_scalar_range',
    'color_mode', 'resolve_coincident_topology', 'scalar_material_mode',
    'scalar_mode', 'force_compile_only', 'ghost_level',
    'number_of_pieces', 'number_of_sub_pieces', 'piece', 'progress_text',
    'render_time', 'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PainterPolyDataMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PainterPolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_immediate_mode_rendering',
            'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
            'scalar_visibility', 'static', 'use_lookup_table_scalar_range'],
            ['color_mode', 'resolve_coincident_topology', 'scalar_material_mode',
            'scalar_mode'], ['force_compile_only', 'ghost_level',
            'number_of_pieces', 'number_of_sub_pieces', 'piece', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range']),
            title='Edit PainterPolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PainterPolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

