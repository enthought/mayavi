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


class Glyph3DMapper(Mapper):
    """
    Glyph3DMapper - Glyph3D on the GPU.
    
    Superclass: Mapper
    
    Do the same job than Glyph3D but on the GPU. For this reason, it
    is a mapper not a PolyDataAlgorithm. Also, some methods of
    Glyph3D don't make sense in Glyph3DMapper: generate_point_ids,
    old-style set_source, point_ids_name, is_point_visible.
    
    Implementation:
    
    See Also:
    
    Glyph3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGlyph3DMapper, obj, update, **traits)
    
    scaling = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off scaling of source geometry. When turned on,
        scale_factor controls the scale applied. To scale with some data
        array, scale_mode should be set accordingly.
        """
    )
    def _scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaling,
                        self.scaling_)

    source_indexing = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable indexing into table of the glyph sources. When
        disabled, only the 1st source input will be used to generate the
        glyph. Otherwise the source index array will be used to select
        the glyph source. The source index array can be specified using
        set_source_index_array().
        """
    )
    def _source_indexing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSourceIndexing,
                        self.source_indexing_)

    nested_display_lists = tvtk_base.true_bool_trait(help=\
        """
        If immediate mode is off, if nested_display_lists is false, only
        the mappers of each glyph use display lists. If true, in
        addition, matrices transforms and color per glyph are also in a
        parent display list. Not relevant if immediate mode is on. For
        debugging/profiling purpose. Initial value is true.
        """
    )
    def _nested_display_lists_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNestedDisplayLists,
                        self.nested_display_lists_)

    masking = tvtk_base.false_bool_trait(help=\
        """
        Tells the mapper to skip glyphing input points that haves false
        values in the mask array. If there is no mask array (id access
        mode is set and there is no such id, or array name access mode is
        set and the there is no such name), masking is silently ignored.
        A mask array is a BitArray with only one component. Initial
        value is false.
        """
    )
    def _masking_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMasking,
                        self.masking_)

    clamping = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off clamping of data values to scale with to the
        specified range.
        """
    )
    def _clamping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClamping,
                        self.clamping_)

    orient = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off orienting of input geometry. When turned on, the
        orientation array specified using set_orientation_array() will be
        used.
        """
    )
    def _orient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrient,
                        self.orient_)

    scale_mode = traits.Trait('scale_by_magnitude',
    tvtk_base.TraitRevPrefixMap({'no_data_scaling': 0, 'scale_by_magnitude': 1, 'scale_by_vector_components': 2}), help=\
        """
        Either scale by individual components (SCALE_BY_COMPONENTS) or
        magnitude (SCALE_BY_MAGNITUDE) of the chosen array to SCALE with
        or disable scaling using data array all together
        (NO_DATA_SCALING). Default is NO_DATA_SCALING.
        """
    )
    def _scale_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleMode,
                        self.scale_mode_)

    orientation_mode = traits.Trait('direction',
    tvtk_base.TraitRevPrefixMap({'direction': 0, 'rotation': 1}), help=\
        """
        Orientation mode indicates if the orientation_array provides the
        direction vector for the orientation or the rotations around each
        axes. Default is DIRECTION
        """
    )
    def _orientation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientationMode,
                        self.orientation_mode_)

    selection_color_id = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        For selection by color id mode (not for end-user, called by
        GlyphSelectionRenderMode). 0 is reserved for miss. it has to
        start at 1. Initial value is 1.
        """
    )
    def _selection_color_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionColorId,
                        self.selection_color_id)

    range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify scale factor to scale object by. This is used only when
        Scaling is On.
        """
    )
    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource(0))
    def _set_source(self, obj):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource, deref_vtk(obj))
        self.trait_property_changed('source', old_val, obj)
    source = traits.Property(_get_source, _set_source,
                             help="The first source of this object, i.e. the result of `get_source(0)`.")
    
    def get_source(self, *args):
        """
        V.get_source(int) -> PolyData
        C++: PolyData *GetSource(int idx=0)
        Get a pointer to a source object at a specified table location.
        """
        ret = self._wrap_call(self._vtk_obj.GetSource, *args)
        return wrap_vtk(ret)

    def set_source(self, *args):
        """
        V.set_source(int, PolyData)
        C++: void SetSource(int idx, PolyData *pd)
        V.set_source(PolyData)
        C++: void SetSource(PolyData *pd)
        Specify a source object at a specified table location.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSource, *my_args)
        return ret

    def set_mask_array(self, *args):
        """
        V.set_mask_array(string)
        C++: void SetMaskArray(const char *maskarrayname)
        V.set_mask_array(int)
        C++: void SetMaskArray(int fieldAttributeType)
        Set the name of the point array to use as a mask for generating
        the glyphs. This is a convenience method. The same effect can be
        achieved by using set_input_array_to_process(vtk_glyph3d_mapper::_mask,
        0, 0,
           DataObject::FIELD_ASSOCIATION_POINTS, maskarrayname)
        """
        ret = self._wrap_call(self._vtk_obj.SetMaskArray, *args)
        return ret

    def set_orientation_array(self, *args):
        """
        V.set_orientation_array(string)
        C++: void SetOrientationArray(const char *orientationarrayname)
        V.set_orientation_array(int)
        C++: void SetOrientationArray(int fieldAttributeType)
        Tells the mapper to use an orientation array if Orient is true.
        An orientation array is a DataArray with 3 components. The
        first component is the angle of rotation along the X axis. The
        second component is the angle of rotation along the Y axis. The
        third component is the angle of rotation along the Z axis.
        Orientation is specified in X,Y,Z order but the rotations are
        performed in Z,X an Y. This definition is compliant with
        set_orientation method on Prop3D. By using vector or normal
        there is a degree of freedom or rotation left (underconstrained).
        With the orientation array, there is no degree of freedom left.
        This is convenience method. The same effect can be achieved by
        using set_input_array_to_process(vtk_glyph3d_mapper::_orientation, 0, 0,
           DataObject::FIELD_ASSOCIATION_POINTS,
        orientationarrayname);
        """
        ret = self._wrap_call(self._vtk_obj.SetOrientationArray, *args)
        return ret

    def set_scale_array(self, *args):
        """
        V.set_scale_array(string)
        C++: void SetScaleArray(const char *scalarsarrayname)
        V.set_scale_array(int)
        C++: void SetScaleArray(int fieldAttributeType)
        Convenience method to set the array to scale with. This is same
        as calling set_input_array_to_process(vtk_glyph3d_mapper::_scale, 0, 0,
           DataObject::FIELD_ASSOCIATION_POINTS, scalarsarrayname).
        """
        ret = self._wrap_call(self._vtk_obj.SetScaleArray, *args)
        return ret

    def set_select_mode(self, *args):
        """
        V.set_select_mode(int)
        C++: void SetSelectMode(int a)
        Called by GlyphSelectionRenderMode.
        """
        ret = self._wrap_call(self._vtk_obj.SetSelectMode, *args)
        return ret

    def set_source_connection(self, *args):
        """
        V.set_source_connection(int, AlgorithmOutput)
        C++: void SetSourceConnection(int idx,
            AlgorithmOutput *algOutput)
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify a source object at a specified table location. New style.
        Source connection is stored in port 1. This method is equivalent
        to set_input_connection(_1, id, output_port).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_index_array(self, *args):
        """
        V.set_source_index_array(string)
        C++: void SetSourceIndexArray(const char *arrayname)
        V.set_source_index_array(int)
        C++: void SetSourceIndexArray(int fieldAttributeType)
        Convenience method to set the array to use as index within the
        sources. This is same as calling
        set_input_array_to_process(vtk_glyph3d_mapper::_source__index, 0, 0,
           DataObject::FIELD_ASSOCIATION_POINTS, arrayname).
        """
        ret = self._wrap_call(self._vtk_obj.SetSourceIndexArray, *args)
        return ret

    _updateable_traits_ = \
    (('immediate_mode_rendering', 'GetImmediateModeRendering'),
    ('scale_factor', 'GetScaleFactor'), ('source_indexing',
    'GetSourceIndexing'), ('orientation_mode', 'GetOrientationMode'),
    ('progress_text', 'GetProgressText'), ('nested_display_lists',
    'GetNestedDisplayLists'), ('scaling', 'GetScaling'), ('debug',
    'GetDebug'), ('color_mode', 'GetColorMode'), ('static', 'GetStatic'),
    ('resolve_coincident_topology', 'GetResolveCoincidentTopology'),
    ('force_compile_only', 'GetForceCompileOnly'),
    ('resolve_coincident_topology_z_shift',
    'GetResolveCoincidentTopologyZShift'), ('scalar_visibility',
    'GetScalarVisibility'), ('orient', 'GetOrient'), ('clamping',
    'GetClamping'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('interpolate_scalars_before_mapping',
    'GetInterpolateScalarsBeforeMapping'), ('scale_mode', 'GetScaleMode'),
    ('selection_color_id', 'GetSelectionColorId'),
    ('use_lookup_table_scalar_range', 'GetUseLookupTableScalarRange'),
    ('range', 'GetRange'), ('abort_execute', 'GetAbortExecute'),
    ('scalar_mode', 'GetScalarMode'), ('scalar_material_mode',
    'GetScalarMaterialMode'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('masking', 'GetMasking'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('render_time', 'GetRenderTime'),
    ('global_immediate_mode_rendering',
    'GetGlobalImmediateModeRendering'), ('scalar_range',
    'GetScalarRange'),
    ('resolve_coincident_topology_polygon_offset_faces',
    'GetResolveCoincidentTopologyPolygonOffsetFaces'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clamping', 'debug',
    'global_immediate_mode_rendering', 'global_warning_display',
    'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
    'masking', 'nested_display_lists', 'orient', 'release_data_flag',
    'scalar_visibility', 'scaling', 'source_indexing', 'static',
    'use_lookup_table_scalar_range', 'color_mode', 'orientation_mode',
    'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode',
    'scale_mode', 'force_compile_only', 'progress_text', 'range',
    'render_time', 'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range', 'scale_factor',
    'selection_color_id'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Glyph3DMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Glyph3DMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clamping', 'global_immediate_mode_rendering',
            'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
            'masking', 'nested_display_lists', 'orient', 'scalar_visibility',
            'scaling', 'source_indexing', 'static',
            'use_lookup_table_scalar_range'], ['color_mode', 'orientation_mode',
            'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode',
            'scale_mode'], ['force_compile_only', 'range', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range', 'scale_factor',
            'selection_color_id']),
            title='Edit Glyph3DMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Glyph3DMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

