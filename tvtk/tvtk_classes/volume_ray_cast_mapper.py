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


class VolumeRayCastMapper(VolumeMapper):
    """
    VolumeRayCastMapper - A slow but accurate mapper for rendering
    volumes
    
    Superclass: VolumeMapper
    
    This is a software ray caster for rendering volumes in ImageData.
    
    See Also:
    
    VolumeMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeRayCastMapper, obj, update, **traits)
    
    intermix_intersecting_geometry = tvtk_base.true_bool_trait(help=\
        """
        If intermix_intersecting_geometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
    )
    def _intermix_intersecting_geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntermixIntersectingGeometry,
                        self.intermix_intersecting_geometry_)

    auto_adjust_sample_distances = tvtk_base.true_bool_trait(help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        will be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
    )
    def _auto_adjust_sample_distances_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdjustSampleDistances,
                        self.auto_adjust_sample_distances_)

    def _get_gradient_estimator(self):
        return wrap_vtk(self._vtk_obj.GetGradientEstimator())
    def _set_gradient_estimator(self, arg):
        old_val = self._get_gradient_estimator()
        self._wrap_call(self._vtk_obj.SetGradientEstimator,
                        deref_vtk(arg))
        self.trait_property_changed('gradient_estimator', old_val, arg)
    gradient_estimator = traits.Property(_get_gradient_estimator, _set_gradient_estimator, help=\
        """
        Set / Get the gradient estimator used to estimate normals
        """
    )

    maximum_image_sample_distance = traits.Trait(10.0, traits.Range(0.10000000000000001, 100.0, enter_set=True, auto_set=False), help=\
        """
        This is the maximum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
    )
    def _maximum_image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumImageSampleDistance,
                        self.maximum_image_sample_distance)

    image_sample_distance = traits.Trait(1.0, traits.Range(0.10000000000000001, 100.0, enter_set=True, auto_set=False), help=\
        """
        Sampling distance in the XY image dimensions. Default value of 1
        meaning 1 ray cast per pixel. If set to 0.5, 4 rays will be cast
        per pixel. If set to 2.0, 1 ray will be cast for every 4 (2 by 2)
        pixels.
        """
    )
    def _image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageSampleDistance,
                        self.image_sample_distance)

    sample_distance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the distance between samples.  This variable is only used
        for sampling ray casting methods.  Methods that compute a ray
        value by stepping cell-by-cell are not affected by this value.
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

    def _get_volume_ray_cast_function(self):
        return wrap_vtk(self._vtk_obj.GetVolumeRayCastFunction())
    def _set_volume_ray_cast_function(self, arg):
        old_val = self._get_volume_ray_cast_function()
        self._wrap_call(self._vtk_obj.SetVolumeRayCastFunction,
                        deref_vtk(arg))
        self.trait_property_changed('volume_ray_cast_function', old_val, arg)
    volume_ray_cast_function = traits.Property(_get_volume_ray_cast_function, _set_volume_ray_cast_function, help=\
        """
        Get / Set the volume ray cast function. This is used to process
        values found along the ray to compute a final pixel value.
        """
    )

    minimum_image_sample_distance = traits.Trait(1.0, traits.Range(0.10000000000000001, 100.0, enter_set=True, auto_set=False), help=\
        """
        This is the minimum image sample distance allow when the image
        sample distance is being automatically adjusted
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
        will be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
    )

    def _get_auto_adjust_sample_distances_min_value(self):
        return self._vtk_obj.GetAutoAdjustSampleDistancesMinValue()
    auto_adjust_sample_distances_min_value = traits.Property(_get_auto_adjust_sample_distances_min_value, help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        will be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
    )

    def _get_gradient_shader(self):
        return wrap_vtk(self._vtk_obj.GetGradientShader())
    gradient_shader = traits.Property(_get_gradient_shader, help=\
        """
        Get the gradient shader.
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

    def get_zero_opacity_threshold(self, *args):
        """
        V.get_zero_opacity_threshold(Volume) -> float
        C++: float GetZeroOpacityThreshold(Volume *vol)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE Return
        the scalar value below which all opacities are zero
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetZeroOpacityThreshold, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('auto_adjust_sample_distances', 'GetAutoAdjustSampleDistances'),
    ('cropping_region_flags', 'GetCroppingRegionFlags'),
    ('maximum_image_sample_distance', 'GetMaximumImageSampleDistance'),
    ('intermix_intersecting_geometry', 'GetIntermixIntersectingGeometry'),
    ('progress_text', 'GetProgressText'), ('image_sample_distance',
    'GetImageSampleDistance'), ('debug', 'GetDebug'),
    ('cropping_region_planes', 'GetCroppingRegionPlanes'), ('scalar_mode',
    'GetScalarMode'), ('number_of_threads', 'GetNumberOfThreads'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('cropping',
    'GetCropping'), ('blend_mode', 'GetBlendMode'), ('abort_execute',
    'GetAbortExecute'), ('minimum_image_sample_distance',
    'GetMinimumImageSampleDistance'), ('sample_distance',
    'GetSampleDistance'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_adjust_sample_distances', 'cropping',
    'debug', 'global_warning_display', 'intermix_intersecting_geometry',
    'release_data_flag', 'blend_mode', 'cropping_region_flags',
    'scalar_mode', 'cropping_region_planes', 'image_sample_distance',
    'maximum_image_sample_distance', 'minimum_image_sample_distance',
    'number_of_threads', 'progress_text', 'sample_distance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeRayCastMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_sample_distances', 'cropping',
            'intermix_intersecting_geometry'], ['blend_mode',
            'cropping_region_flags', 'scalar_mode'], ['cropping_region_planes',
            'image_sample_distance', 'maximum_image_sample_distance',
            'minimum_image_sample_distance', 'number_of_threads',
            'sample_distance']),
            title='Edit VolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

