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

from tvtk.tvtk_classes.volume_mapper import VolumeMapper


class VolumeProMapper(VolumeMapper):
    """
    VolumeProMapper - Superclass for volume_pro volume rendering mappers
    
    Superclass: VolumeMapper
    
    VolumeProMapper is the superclass for volume_pro volume rendering
    mappers. Any functionality that is general across all volume_pro
    implementations is placed here in this class. Subclasses of this
    class are for the specific board implementations. Subclasses of that
    are for underlying graphics languages. Users should not create
    subclasses directly - a VolumeProMapper will automatically create
    the object of the right type.
    
    If you do not have the volume_pro libraries when building this object,
    then the New method will create a default renderer that will not
    render. You can check the number_of_boards ivar to see if it is a real
    rendering class. To build with the volume_pro board see
    VolumeProVP1000Mapper.h for instructions.
    
    For more information on the volume_pro hardware, please see:
    
    
      http://www.terarecon.com/products/volumepro_prod.html
    
    If you encounter any problems with this class, please inform Kitware,
    Inc. at kitware@kitware.com.
    
    See Also:
    
    VolumeMapper VolumeProVP1000Mapper
    OpenGLVolumeProVP1000Mapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeProMapper, obj, update, **traits)
    
    gradient_opacity_modulation = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the gradient magnitude opacity modulation
        """
    )
    def _gradient_opacity_modulation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGradientOpacityModulation,
                        self.gradient_opacity_modulation_)

    intermix_intersecting_geometry = tvtk_base.false_bool_trait(help=\
        """
        Specify whether any geometry intersects the volume.
        """
    )
    def _intermix_intersecting_geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntermixIntersectingGeometry,
                        self.intermix_intersecting_geometry_)

    auto_adjust_mipmap_levels = tvtk_base.false_bool_trait(help=\
        """
        If set to 1, this mapper will select a mipmap level to use based
        on the allocated_render_time of the volume and the amount of time
        used by the previous render.
        """
    )
    def _auto_adjust_mipmap_levels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdjustMipmapLevels,
                        self.auto_adjust_mipmap_levels_)

    cursor = tvtk_base.false_bool_trait(help=\
        """
        Turn the cursor on / off
        """
    )
    def _cursor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCursor,
                        self.cursor_)

    gradient_specular_modulation = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the gradient magnitude specular modulation
        """
    )
    def _gradient_specular_modulation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGradientSpecularModulation,
                        self.gradient_specular_modulation_)

    gradient_diffuse_modulation = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the gradient magnitude diffuse modulation
        """
    )
    def _gradient_diffuse_modulation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGradientDiffuseModulation,
                        self.gradient_diffuse_modulation_)

    super_sampling = tvtk_base.false_bool_trait(help=\
        """
        Turn supersampling on/off
        """
    )
    def _super_sampling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSuperSampling,
                        self.super_sampling_)

    cut_plane = tvtk_base.false_bool_trait(help=\
        """
        Turn on / off the cut plane
        """
    )
    def _cut_plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCutPlane,
                        self.cut_plane_)

    cursor_type = traits.Trait('cross_hair',
    tvtk_base.TraitRevPrefixMap({'cross_hair': 0, 'plane': 1}), help=\
        """
        Set the type of the cursor
        """
    )
    def _cursor_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCursorType,
                        self.cursor_type_)

    cut_plane_equation = traits.Array(shape=(4,), value=(1.0, 0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _cut_plane_equation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCutPlaneEquation,
                        self.cut_plane_equation)

    cursor_position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _cursor_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCursorPosition,
                        self.cursor_position)

    cut_plane_fall_off_distance = traits.Trait(0, traits.Range(0, 16, enter_set=True, auto_set=False), help=\
        """
        Set / Get the cut plane falloff value for intensities
        """
    )
    def _cut_plane_fall_off_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCutPlaneFallOffDistance,
                        self.cut_plane_fall_off_distance)

    cursor_z_axis_color = tvtk_base.vtk_color_trait((0.0, 0.0, 1.0), help=\
        """
        
        """
    )
    def _cursor_z_axis_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCursorZAxisColor,
                        self.cursor_z_axis_color, False)

    cut_plane_thickness = traits.Trait(0.0, traits.Range(0.0, 99900000000.0, enter_set=True, auto_set=False), help=\
        """
        Set / Get the cut plane thickness
        """
    )
    def _cut_plane_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCutPlaneThickness,
                        self.cut_plane_thickness)

    maximum_mipmap_level = traits.Trait(4, traits.Range(0, 32, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum mipmap level to use -- the lowest resolution.
        Defaults to 4. It will not help to set the level larger than this
        unless your volume is very large because for each successive
        mipmap level, the number of voxels along each axis is cut in
        half.
        """
    )
    def _maximum_mipmap_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumMipmapLevel,
                        self.maximum_mipmap_level)

    mipmap_level = traits.Trait(0, traits.Range(0, 32, enter_set=True, auto_set=False), help=\
        """
        Choose a mipmap level. If auto_adjust_mipmap_levels is off, then
        this specifies the mipmap level to use during interaction. If
        auto_adjust_mipmap_levels is on, then this specifies the initial
        mipmap level to use.
        """
    )
    def _mipmap_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMipmapLevel,
                        self.mipmap_level)

    super_sampling_factor = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the supersampling factors
        """
    )
    def _super_sampling_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSuperSamplingFactor,
                        self.super_sampling_factor)

    blend_mode = traits.Trait(0, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set the blend mode
        """
    )
    def _blend_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlendMode,
                        self.blend_mode)

    cursor_x_axis_color = tvtk_base.vtk_color_trait((1.0, 0.0, 0.0), help=\
        """
        
        """
    )
    def _cursor_x_axis_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCursorXAxisColor,
                        self.cursor_x_axis_color, False)

    minimum_mipmap_level = traits.Trait(0, traits.Range(0, 32, enter_set=True, auto_set=False), help=\
        """
        Specify the minimum mipmap level to use -- the highest
        resolution. Defaults to 0. This is the mipmap level that is used
        when interaction stops.
        """
    )
    def _minimum_mipmap_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumMipmapLevel,
                        self.minimum_mipmap_level)

    cursor_y_axis_color = tvtk_base.vtk_color_trait((0.0, 1.0, 0.0), help=\
        """
        
        """
    )
    def _cursor_y_axis_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCursorYAxisColor,
                        self.cursor_y_axis_color, False)

    sub_volume = traits.Array(shape=(6,), value=(-1, -1, -1, -1, -1, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _sub_volume_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubVolume,
                        self.sub_volume)

    def _get_auto_adjust_mipmap_levels_max_value(self):
        return self._vtk_obj.GetAutoAdjustMipmapLevelsMaxValue()
    auto_adjust_mipmap_levels_max_value = traits.Property(_get_auto_adjust_mipmap_levels_max_value, help=\
        """
        If set to 1, this mapper will select a mipmap level to use based
        on the allocated_render_time of the volume and the amount of time
        used by the previous render.
        """
    )

    def _get_auto_adjust_mipmap_levels_min_value(self):
        return self._vtk_obj.GetAutoAdjustMipmapLevelsMinValue()
    auto_adjust_mipmap_levels_min_value = traits.Property(_get_auto_adjust_mipmap_levels_min_value, help=\
        """
        If set to 1, this mapper will select a mipmap level to use based
        on the allocated_render_time of the volume and the amount of time
        used by the previous render.
        """
    )

    def _get_available_board_memory(self):
        return self._vtk_obj.GetAvailableBoardMemory()
    available_board_memory = traits.Property(_get_available_board_memory, help=\
        """
        Access methods for some board info
        """
    )

    def _get_blend_mode_as_string(self):
        return self._vtk_obj.GetBlendModeAsString()
    blend_mode_as_string = traits.Property(_get_blend_mode_as_string, help=\
        """
        Set the blend mode
        """
    )

    def _get_cursor_max_value(self):
        return self._vtk_obj.GetCursorMaxValue()
    cursor_max_value = traits.Property(_get_cursor_max_value, help=\
        """
        Turn the cursor on / off
        """
    )

    def _get_cursor_min_value(self):
        return self._vtk_obj.GetCursorMinValue()
    cursor_min_value = traits.Property(_get_cursor_min_value, help=\
        """
        Turn the cursor on / off
        """
    )

    def _get_cut_plane_max_value(self):
        return self._vtk_obj.GetCutPlaneMaxValue()
    cut_plane_max_value = traits.Property(_get_cut_plane_max_value, help=\
        """
        Turn on / off the cut plane
        """
    )

    def _get_cut_plane_min_value(self):
        return self._vtk_obj.GetCutPlaneMinValue()
    cut_plane_min_value = traits.Property(_get_cut_plane_min_value, help=\
        """
        Turn on / off the cut plane
        """
    )

    def _get_gradient_diffuse_modulation_max_value(self):
        return self._vtk_obj.GetGradientDiffuseModulationMaxValue()
    gradient_diffuse_modulation_max_value = traits.Property(_get_gradient_diffuse_modulation_max_value, help=\
        """
        Set/Get the gradient magnitude diffuse modulation
        """
    )

    def _get_gradient_diffuse_modulation_min_value(self):
        return self._vtk_obj.GetGradientDiffuseModulationMinValue()
    gradient_diffuse_modulation_min_value = traits.Property(_get_gradient_diffuse_modulation_min_value, help=\
        """
        Set/Get the gradient magnitude diffuse modulation
        """
    )

    def _get_gradient_opacity_modulation_max_value(self):
        return self._vtk_obj.GetGradientOpacityModulationMaxValue()
    gradient_opacity_modulation_max_value = traits.Property(_get_gradient_opacity_modulation_max_value, help=\
        """
        Set/Get the gradient magnitude opacity modulation
        """
    )

    def _get_gradient_opacity_modulation_min_value(self):
        return self._vtk_obj.GetGradientOpacityModulationMinValue()
    gradient_opacity_modulation_min_value = traits.Property(_get_gradient_opacity_modulation_min_value, help=\
        """
        Set/Get the gradient magnitude opacity modulation
        """
    )

    def _get_gradient_specular_modulation_max_value(self):
        return self._vtk_obj.GetGradientSpecularModulationMaxValue()
    gradient_specular_modulation_max_value = traits.Property(_get_gradient_specular_modulation_max_value, help=\
        """
        Set/Get the gradient magnitude specular modulation
        """
    )

    def _get_gradient_specular_modulation_min_value(self):
        return self._vtk_obj.GetGradientSpecularModulationMinValue()
    gradient_specular_modulation_min_value = traits.Property(_get_gradient_specular_modulation_min_value, help=\
        """
        Set/Get the gradient magnitude specular modulation
        """
    )

    def _get_intermix_intersecting_geometry_max_value(self):
        return self._vtk_obj.GetIntermixIntersectingGeometryMaxValue()
    intermix_intersecting_geometry_max_value = traits.Property(_get_intermix_intersecting_geometry_max_value, help=\
        """
        Specify whether any geometry intersects the volume.
        """
    )

    def _get_intermix_intersecting_geometry_min_value(self):
        return self._vtk_obj.GetIntermixIntersectingGeometryMinValue()
    intermix_intersecting_geometry_min_value = traits.Property(_get_intermix_intersecting_geometry_min_value, help=\
        """
        Specify whether any geometry intersects the volume.
        """
    )

    def _get_major_board_version(self):
        return self._vtk_obj.GetMajorBoardVersion()
    major_board_version = traits.Property(_get_major_board_version, help=\
        """
        Access methods for some board info
        """
    )

    def _get_minor_board_version(self):
        return self._vtk_obj.GetMinorBoardVersion()
    minor_board_version = traits.Property(_get_minor_board_version, help=\
        """
        Access methods for some board info
        """
    )

    def _get_no_hardware(self):
        return self._vtk_obj.GetNoHardware()
    no_hardware = traits.Property(_get_no_hardware, help=\
        """
        Conveniece methods for debugging
        """
    )

    def _get_number_of_boards(self):
        return self._vtk_obj.GetNumberOfBoards()
    number_of_boards = traits.Property(_get_number_of_boards, help=\
        """
        Access methods for some board info
        """
    )

    def _get_super_sampling_max_value(self):
        return self._vtk_obj.GetSuperSamplingMaxValue()
    super_sampling_max_value = traits.Property(_get_super_sampling_max_value, help=\
        """
        Turn supersampling on/off
        """
    )

    def _get_super_sampling_min_value(self):
        return self._vtk_obj.GetSuperSamplingMinValue()
    super_sampling_min_value = traits.Property(_get_super_sampling_min_value, help=\
        """
        Turn supersampling on/off
        """
    )

    def _get_wrong_vli_version(self):
        return self._vtk_obj.GetWrongVLIVersion()
    wrong_vli_version = traits.Property(_get_wrong_vli_version, help=\
        """
        Conveniece methods for debugging
        """
    )

    _updateable_traits_ = \
    (('gradient_specular_modulation', 'GetGradientSpecularModulation'),
    ('intermix_intersecting_geometry', 'GetIntermixIntersectingGeometry'),
    ('cut_plane_thickness', 'GetCutPlaneThickness'), ('scalar_mode',
    'GetScalarMode'), ('gradient_opacity_modulation',
    'GetGradientOpacityModulation'), ('debug', 'GetDebug'),
    ('cursor_position', 'GetCursorPosition'), ('cursor_z_axis_color',
    'GetCursorZAxisColor'), ('cursor_type', 'GetCursorType'),
    ('super_sampling', 'GetSuperSampling'), ('mipmap_level',
    'GetMipmapLevel'), ('gradient_diffuse_modulation',
    'GetGradientDiffuseModulation'), ('cursor_y_axis_color',
    'GetCursorYAxisColor'), ('sub_volume', 'GetSubVolume'),
    ('minimum_mipmap_level', 'GetMinimumMipmapLevel'), ('cut_plane',
    'GetCutPlane'), ('cut_plane_equation', 'GetCutPlaneEquation'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('cut_plane_fall_off_distance', 'GetCutPlaneFallOffDistance'),
    ('super_sampling_factor', 'GetSuperSamplingFactor'), ('progress_text',
    'GetProgressText'), ('maximum_mipmap_level', 'GetMaximumMipmapLevel'),
    ('cursor', 'GetCursor'), ('cropping_region_flags',
    'GetCroppingRegionFlags'), ('cursor_x_axis_color',
    'GetCursorXAxisColor'), ('cropping_region_planes',
    'GetCroppingRegionPlanes'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('cropping', 'GetCropping'),
    ('blend_mode', 'GetBlendMode'), ('abort_execute', 'GetAbortExecute'),
    ('auto_adjust_mipmap_levels', 'GetAutoAdjustMipmapLevels'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_adjust_mipmap_levels', 'cropping', 'cursor',
    'cut_plane', 'debug', 'global_warning_display',
    'gradient_diffuse_modulation', 'gradient_opacity_modulation',
    'gradient_specular_modulation', 'intermix_intersecting_geometry',
    'release_data_flag', 'super_sampling', 'blend_mode',
    'cropping_region_flags', 'cursor_type', 'scalar_mode', 'blend_mode',
    'cropping_region_planes', 'cursor_position', 'cursor_x_axis_color',
    'cursor_y_axis_color', 'cursor_z_axis_color', 'cut_plane_equation',
    'cut_plane_fall_off_distance', 'cut_plane_thickness',
    'maximum_mipmap_level', 'minimum_mipmap_level', 'mipmap_level',
    'progress_text', 'sub_volume', 'super_sampling_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeProMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeProMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_mipmap_levels', 'cropping', 'cursor',
            'cut_plane', 'gradient_diffuse_modulation',
            'gradient_opacity_modulation', 'gradient_specular_modulation',
            'intermix_intersecting_geometry', 'super_sampling'], ['blend_mode',
            'cropping_region_flags', 'cursor_type', 'scalar_mode'], ['blend_mode',
            'cropping_region_planes', 'cursor_position', 'cursor_x_axis_color',
            'cursor_y_axis_color', 'cursor_z_axis_color', 'cut_plane_equation',
            'cut_plane_fall_off_distance', 'cut_plane_thickness',
            'maximum_mipmap_level', 'minimum_mipmap_level', 'mipmap_level',
            'sub_volume', 'super_sampling_factor']),
            title='Edit VolumeProMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeProMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

