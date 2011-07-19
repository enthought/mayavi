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


class FixedPointVolumeRayCastMapper(VolumeMapper):
    """
    FixedPointVolumeRayCastMapper - A fixed point mapper for volumes
    
    Superclass: VolumeMapper
    
    This is a software ray caster for rendering volumes in ImageData.
    It works with all input data types and up to four components. It
    performs composite or MIP rendering, and can be intermixed with
    geometric data. Space leaping is used to speed up the rendering
    process. In addition, calculation are performed in 15 bit fixed point
    precision. This mapper is threaded, and will interleave scan lines
    across processors.
    
    This mapper is a good replacement for VolumeRayCastMapper EXCEPT:
    - it does not do isosurface ray casting
    - it does only interpolate before classify compositing
    - it does only maximum scalar value MIP
    
    The VolumeRayCastMapper CANNOT be used in these instances when a
    FixedPointVolumeRayCastMapper can be used:
    - if the data is not unsigned char or unsigned short
    - if the data has more than one component
    
    This mapper handles all data type from unsigned char through double.
    However, some of the internal calcultions are performed in float and
    therefore even the full float range may cause problems for this
    mapper (both in scalar data values and in spacing between samples).
    
    Space leaping is performed by creating a sub-sampled volume. 4x4x4
    cells in the original volume are represented by a min, max, and
    combined gradient and flag value. The min max volume has three
    unsigned shorts per 4x4x4 group of cells from the original volume -
    one reprenting the minumum scalar index (the scalar value adjusted to
    fit in the 15 bit range), the maximum scalar index, and a third
    unsigned short which is both the maximum gradient opacity in the
    neighborhood (an unsigned char) and the flag that is filled in for
    the current lookup tables to indicate whether this region can be
    skipped.
    
    See Also:
    
    VolumeMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFixedPointVolumeRayCastMapper, obj, update, **traits)
    
    intermix_intersecting_geometry = tvtk_base.true_bool_trait(help=\
        """
        If intermix_intersecting_geometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
    )
    def _intermix_intersecting_geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntermixIntersectingGeometry,
                        self.intermix_intersecting_geometry_)

    lock_sample_distance_to_input_spacing = tvtk_base.false_bool_trait(help=\
        """
        Automatically compute the sample distance from the data spacing. 
        When the number of voxels is 8, the sample distance will be
        roughly 1/200 the average voxel size. The distance will grow
        proportionally to num_voxels^(_1/_3) until it reaches 1/2 average
        voxel size when number of voxels is 1e6. Note that
        scalar_opacity_unit_distance is still taken into account and if
        different than 1, will effect the sample distance.
        """
    )
    def _lock_sample_distance_to_input_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLockSampleDistanceToInputSpacing,
                        self.lock_sample_distance_to_input_spacing_)

    auto_adjust_sample_distances = tvtk_base.true_bool_trait(help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        and the sample_distance will be varied to achieve the allocated
        render time of this prop (controlled by the desired update rate
        and any culling in use). If this is an interactive render (more
        than 1 frame per second) the sample_distance will be increased,
        otherwise it will not be altered (a binary decision, as opposed
        to the image_sample_distance which will vary continuously).
        """
    )
    def _auto_adjust_sample_distances_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdjustSampleDistances,
                        self.auto_adjust_sample_distances_)

    maximum_image_sample_distance = traits.Trait(10.0, traits.Range(0.10000000149011612, 100.0, enter_set=True, auto_set=False), help=\
        """
        This is the maximum image sample distance allow when the image
        sample distance is being automatically adjusted.
        """
    )
    def _maximum_image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumImageSampleDistance,
                        self.maximum_image_sample_distance)

    image_sample_distance = traits.Trait(1.0, traits.Range(0.10000000149011612, 100.0, enter_set=True, auto_set=False), help=\
        """
        Sampling distance in the XY image dimensions. Default value of 1
        meaning 1 ray cast per pixel. If set to 0.5, 4 rays will be cast
        per pixel. If set to 2.0, 1 ray will be cast for every 4 (2 by 2)
        pixels. This value will be adjusted to meet a desired frame rate
        when auto_adjust_sample_distances is on.
        """
    )
    def _image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageSampleDistance,
                        self.image_sample_distance)

    def _get_ray_cast_image(self):
        return wrap_vtk(self._vtk_obj.GetRayCastImage())
    def _set_ray_cast_image(self, arg):
        old_val = self._get_ray_cast_image()
        self._wrap_call(self._vtk_obj.SetRayCastImage,
                        deref_vtk(arg))
        self.trait_property_changed('ray_cast_image', old_val, arg)
    ray_cast_image = traits.Property(_get_ray_cast_image, _set_ray_cast_image, help=\
        """
        Set / Get the underlying image object. One will be automatically
        created - only need to set it when using from an AMR mapper which
        renders multiple times into the same image.
        """
    )

    sample_distance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the distance between samples used for rendering when
        auto_adjust_sample_distances is off, or when this mapper has more
        than 1 second allocated to it for rendering.
        """
    )
    def _sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDistance,
                        self.sample_distance)

    number_of_threads = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of threads to use. This by default is equal to
        the number of available processors detected.
        """
    )
    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

    final_color_window = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the window / level applied to the final color. This
        allows brightness / contrast adjustments on the final image.
        window is the width of the window. level is the center of the
        window. Initial window value is 1.0 Initial level value is 0.5
        window cannot be null but can be negative, this way values will
        be reversed. |window| can be larger than 1.0 level can be any
        real value.
        """
    )
    def _final_color_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFinalColorWindow,
                        self.final_color_window)

    interactive_sample_distance = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the distance between samples when interactive rendering
        is happening. In this case, interactive is defined as this volume
        mapper having less than 1 second allocated for rendering. When
        auto_adjust_sample_distance is On, and the allocated render time is
        less than 1 second, then this interactive_sample_distance will be
        used instead of the sample_distance above.
        """
    )
    def _interactive_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractiveSampleDistance,
                        self.interactive_sample_distance)

    final_color_level = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the window / level applied to the final color. This
        allows brightness / contrast adjustments on the final image.
        window is the width of the window. level is the center of the
        window. Initial window value is 1.0 Initial level value is 0.5
        window cannot be null but can be negative, this way values will
        be reversed. |window| can be larger than 1.0 level can be any
        real value.
        """
    )
    def _final_color_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFinalColorLevel,
                        self.final_color_level)

    minimum_image_sample_distance = traits.Trait(1.0, traits.Range(0.10000000149011612, 100.0, enter_set=True, auto_set=False), help=\
        """
        This is the minimum image sample distance allow when the image
        sample distance is being automatically adjusted.
        """
    )
    def _minimum_image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumImageSampleDistance,
                        self.minimum_image_sample_distance)

    def _get_auto_adjust_sample_distances_max_value(self):
        return self._vtk_obj.GetAutoAdjustSampleDistancesMaxValue()
    auto_adjust_sample_distances_max_value = traits.Property(_get_auto_adjust_sample_distances_max_value, help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        and the sample_distance will be varied to achieve the allocated
        render time of this prop (controlled by the desired update rate
        and any culling in use). If this is an interactive render (more
        than 1 frame per second) the sample_distance will be increased,
        otherwise it will not be altered (a binary decision, as opposed
        to the image_sample_distance which will vary continuously).
        """
    )

    def _get_auto_adjust_sample_distances_min_value(self):
        return self._vtk_obj.GetAutoAdjustSampleDistancesMinValue()
    auto_adjust_sample_distances_min_value = traits.Property(_get_auto_adjust_sample_distances_min_value, help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        and the sample_distance will be varied to achieve the allocated
        render time of this prop (controlled by the desired update rate
        and any culling in use). If this is an interactive render (more
        than 1 frame per second) the sample_distance will be increased,
        otherwise it will not be altered (a binary decision, as opposed
        to the image_sample_distance which will vary continuously).
        """
    )

    def _get_composite_go_helper(self):
        return wrap_vtk(self._vtk_obj.GetCompositeGOHelper())
    composite_go_helper = traits.Property(_get_composite_go_helper, help=\
        """
        
        """
    )

    def _get_composite_go_shade_helper(self):
        return wrap_vtk(self._vtk_obj.GetCompositeGOShadeHelper())
    composite_go_shade_helper = traits.Property(_get_composite_go_shade_helper, help=\
        """
        
        """
    )

    def _get_composite_helper(self):
        return wrap_vtk(self._vtk_obj.GetCompositeHelper())
    composite_helper = traits.Property(_get_composite_helper, help=\
        """
        
        """
    )

    def _get_composite_shade_helper(self):
        return wrap_vtk(self._vtk_obj.GetCompositeShadeHelper())
    composite_shade_helper = traits.Property(_get_composite_shade_helper, help=\
        """
        
        """
    )

    def _get_current_scalars(self):
        return wrap_vtk(self._vtk_obj.GetCurrentScalars())
    current_scalars = traits.Property(_get_current_scalars, help=\
        """
        
        """
    )

    def get_estimated_render_time(self, *args):
        """
        V.get_estimated_render_time(Renderer, Volume) -> float
        C++: float GetEstimatedRenderTime(Renderer *ren,
            Volume *vol)
        V.get_estimated_render_time(Renderer) -> float
        C++: float GetEstimatedRenderTime(Renderer *ren)
        Get an estimate of the rendering time for a given volume /
        renderer. Only valid if this mapper has been used to render that
        volume for that renderer previously. Estimate is good when the
        viewing parameters have not changed much since that last render.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetEstimatedRenderTime, *my_args)
        return ret

    def _get_flip_mip_comparison(self):
        return self._vtk_obj.GetFlipMIPComparison()
    flip_mip_comparison = traits.Property(_get_flip_mip_comparison, help=\
        """
        
        """
    )

    def _get_gradient_opacity_required(self):
        return self._vtk_obj.GetGradientOpacityRequired()
    gradient_opacity_required = traits.Property(_get_gradient_opacity_required, help=\
        """
        
        """
    )

    def _get_intermix_intersecting_geometry_max_value(self):
        return self._vtk_obj.GetIntermixIntersectingGeometryMaxValue()
    intermix_intersecting_geometry_max_value = traits.Property(_get_intermix_intersecting_geometry_max_value, help=\
        """
        If intermix_intersecting_geometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
    )

    def _get_intermix_intersecting_geometry_min_value(self):
        return self._vtk_obj.GetIntermixIntersectingGeometryMinValue()
    intermix_intersecting_geometry_min_value = traits.Property(_get_intermix_intersecting_geometry_min_value, help=\
        """
        If intermix_intersecting_geometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
    )

    def _get_lock_sample_distance_to_input_spacing_max_value(self):
        return self._vtk_obj.GetLockSampleDistanceToInputSpacingMaxValue()
    lock_sample_distance_to_input_spacing_max_value = traits.Property(_get_lock_sample_distance_to_input_spacing_max_value, help=\
        """
        Automatically compute the sample distance from the data spacing. 
        When the number of voxels is 8, the sample distance will be
        roughly 1/200 the average voxel size. The distance will grow
        proportionally to num_voxels^(_1/_3) until it reaches 1/2 average
        voxel size when number of voxels is 1e6. Note that
        scalar_opacity_unit_distance is still taken into account and if
        different than 1, will effect the sample distance.
        """
    )

    def _get_lock_sample_distance_to_input_spacing_min_value(self):
        return self._vtk_obj.GetLockSampleDistanceToInputSpacingMinValue()
    lock_sample_distance_to_input_spacing_min_value = traits.Property(_get_lock_sample_distance_to_input_spacing_min_value, help=\
        """
        Automatically compute the sample distance from the data spacing. 
        When the number of voxels is 8, the sample distance will be
        roughly 1/200 the average voxel size. The distance will grow
        proportionally to num_voxels^(_1/_3) until it reaches 1/2 average
        voxel size when number of voxels is 1e6. Note that
        scalar_opacity_unit_distance is still taken into account and if
        different than 1, will effect the sample distance.
        """
    )

    def _get_mip_helper(self):
        return wrap_vtk(self._vtk_obj.GetMIPHelper())
    mip_helper = traits.Property(_get_mip_helper, help=\
        """
        
        """
    )

    def _get_previous_scalars(self):
        return wrap_vtk(self._vtk_obj.GetPreviousScalars())
    previous_scalars = traits.Property(_get_previous_scalars, help=\
        """
        
        """
    )

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    render_window = traits.Property(_get_render_window, help=\
        """
        
        """
    )

    def _get_shading_required(self):
        return self._vtk_obj.GetShadingRequired()
    shading_required = traits.Property(_get_shading_required, help=\
        """
        
        """
    )

    def _get_table_scale(self):
        return self._vtk_obj.GetTableScale()
    table_scale = traits.Property(_get_table_scale, help=\
        """
        
        """
    )

    def _get_table_shift(self):
        return self._vtk_obj.GetTableShift()
    table_shift = traits.Property(_get_table_shift, help=\
        """
        
        """
    )

    def _get_volume(self):
        return wrap_vtk(self._vtk_obj.GetVolume())
    volume = traits.Property(_get_volume, help=\
        """
        
        """
    )

    def abort_render(self):
        """
        V.abort_render()
        C++: void AbortRender()"""
        ret = self._vtk_obj.AbortRender()
        return ret
        

    def check_if_cropped(self, *args):
        """
        V.check_if_cropped([int, int, int]) -> int
        C++: int CheckIfCropped(unsigned int pos[3])"""
        ret = self._wrap_call(self._vtk_obj.CheckIfCropped, *args)
        return ret

    def check_mip_min_max_volume_flag(self, *args):
        """
        V.check_mip_min_max_volume_flag([int, int, int], int, int, int) -> int
        C++: int CheckMIPMinMaxVolumeFlag(unsigned int pos[3], int c,
            unsigned short maxIdx, int flip)"""
        ret = self._wrap_call(self._vtk_obj.CheckMIPMinMaxVolumeFlag, *args)
        return ret

    def check_min_max_volume_flag(self, *args):
        """
        V.check_min_max_volume_flag([int, int, int], int) -> int
        C++: int CheckMinMaxVolumeFlag(unsigned int pos[3], int c)"""
        ret = self._wrap_call(self._vtk_obj.CheckMinMaxVolumeFlag, *args)
        return ret

    def compute_required_image_sample_distance(self, *args):
        """
        V.compute_required_image_sample_distance(float, Renderer) -> float
        C++: float ComputeRequiredImageSampleDistance(float desiredTime,
            Renderer *ren)
        V.compute_required_image_sample_distance(float, Renderer,
            Volume) -> float
        C++: float ComputeRequiredImageSampleDistance(float desiredTime,
            Renderer *ren, Volume *vol)
        What is the image sample distance required to achieve the desired
        time? A version of this method is provided that does not require
        the volume argument since if you are using an lod_prop3d you may
        not know this information. If you use this version you must be
        certain that the ray cast mapper is only used for one volume (and
        not shared among multiple volumes)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeRequiredImageSampleDistance, *my_args)
        return ret

    def create_canonical_view(self, *args):
        """
        V.create_canonical_view(Volume, ImageData, int, [float, float,
             float], [float, float, float])
        C++: void CreateCanonicalView(Volume *volume,
            ImageData *image, int blend_mode, double viewDirection[3],
            double viewUp[3])"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateCanonicalView, *my_args)
        return ret

    def display_rendered_image(self, *args):
        """
        V.display_rendered_image(Renderer, Volume)
        C++: void DisplayRenderedImage(Renderer *, Volume *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DisplayRenderedImage, *my_args)
        return ret

    def fixed_point_increment(self, *args):
        """
        V.fixed_point_increment([int, int, int], [int, int, int])
        C++: void FixedPointIncrement(unsigned int position[3],
            unsigned int increment[3])"""
        ret = self._wrap_call(self._vtk_obj.FixedPointIncrement, *args)
        return ret

    def initialize_ray_info(self, *args):
        """
        V.initialize_ray_info(Volume)
        C++: void InitializeRayInfo(Volume *vol)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InitializeRayInfo, *my_args)
        return ret

    def per_sub_volume_initialization(self, *args):
        """
        V.per_sub_volume_initialization(Renderer, Volume, int)
        C++: void PerSubVolumeInitialization(Renderer *, Volume *,
            int)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PerSubVolumeInitialization, *my_args)
        return ret

    def per_volume_initialization(self, *args):
        """
        V.per_volume_initialization(Renderer, Volume)
        C++: void PerVolumeInitialization(Renderer *, Volume *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PerVolumeInitialization, *my_args)
        return ret

    def render_sub_volume(self):
        """
        V.render_sub_volume()
        C++: void RenderSubVolume()"""
        ret = self._vtk_obj.RenderSubVolume()
        return ret
        

    def shift_vector_down(self, *args):
        """
        V.shift_vector_down([int, int, int], [int, int, int])
        C++: void ShiftVectorDown(unsigned int in[3], unsigned int out[3])"""
        ret = self._wrap_call(self._vtk_obj.ShiftVectorDown, *args)
        return ret

    def should_use_nearest_neighbor_interpolation(self, *args):
        """
        V.should_use_nearest_neighbor_interpolation(Volume) -> int
        C++: int ShouldUseNearestNeighborInterpolation(Volume *vol)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShouldUseNearestNeighborInterpolation, *my_args)
        return ret

    def to_fixed_point_direction(self, *args):
        """
        V.to_fixed_point_direction(float) -> int
        C++: unsigned int ToFixedPointDirection(float dir)
        V.to_fixed_point_direction([float, float, float], [int, int, int])
        C++: void ToFixedPointDirection(float in[3], unsigned int out[3])"""
        ret = self._wrap_call(self._vtk_obj.ToFixedPointDirection, *args)
        return ret

    def to_fixed_point_position(self, *args):
        """
        V.to_fixed_point_position(float) -> int
        C++: unsigned int ToFixedPointPosition(float val)
        V.to_fixed_point_position([float, float, float], [int, int, int])
        C++: void ToFixedPointPosition(float in[3], unsigned int out[3])"""
        ret = self._wrap_call(self._vtk_obj.ToFixedPointPosition, *args)
        return ret

    _updateable_traits_ = \
    (('release_data_flag', 'GetReleaseDataFlag'),
    ('intermix_intersecting_geometry', 'GetIntermixIntersectingGeometry'),
    ('cropping_region_flags', 'GetCroppingRegionFlags'), ('scalar_mode',
    'GetScalarMode'), ('maximum_image_sample_distance',
    'GetMaximumImageSampleDistance'), ('reference_count',
    'GetReferenceCount'), ('lock_sample_distance_to_input_spacing',
    'GetLockSampleDistanceToInputSpacing'), ('final_color_window',
    'GetFinalColorWindow'), ('minimum_image_sample_distance',
    'GetMinimumImageSampleDistance'), ('blend_mode', 'GetBlendMode'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('auto_adjust_sample_distances', 'GetAutoAdjustSampleDistances'),
    ('progress_text', 'GetProgressText'), ('final_color_level',
    'GetFinalColorLevel'), ('image_sample_distance',
    'GetImageSampleDistance'), ('abort_execute', 'GetAbortExecute'),
    ('cropping_region_planes', 'GetCroppingRegionPlanes'),
    ('number_of_threads', 'GetNumberOfThreads'), ('debug', 'GetDebug'),
    ('progress', 'GetProgress'), ('cropping', 'GetCropping'),
    ('interactive_sample_distance', 'GetInteractiveSampleDistance'),
    ('sample_distance', 'GetSampleDistance'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_adjust_sample_distances', 'cropping',
    'debug', 'global_warning_display', 'intermix_intersecting_geometry',
    'lock_sample_distance_to_input_spacing', 'release_data_flag',
    'blend_mode', 'cropping_region_flags', 'scalar_mode',
    'cropping_region_planes', 'final_color_level', 'final_color_window',
    'image_sample_distance', 'interactive_sample_distance',
    'maximum_image_sample_distance', 'minimum_image_sample_distance',
    'number_of_threads', 'progress_text', 'sample_distance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FixedPointVolumeRayCastMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FixedPointVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_sample_distances', 'cropping',
            'intermix_intersecting_geometry',
            'lock_sample_distance_to_input_spacing'], ['blend_mode',
            'cropping_region_flags', 'scalar_mode'], ['cropping_region_planes',
            'final_color_level', 'final_color_window', 'image_sample_distance',
            'interactive_sample_distance', 'maximum_image_sample_distance',
            'minimum_image_sample_distance', 'number_of_threads',
            'sample_distance']),
            title='Edit FixedPointVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FixedPointVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

