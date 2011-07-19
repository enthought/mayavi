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

from tvtk.tvtk_classes.object import Object


class EncodedGradientEstimator(Object):
    """
    EncodedGradientEstimator - Superclass for gradient estimation
    
    Superclass: Object
    
    EncodedGradientEstimator is an abstract superclass for gradient
    estimation. It takes a scalar input of ImageData, computes a
    gradient value for every point, and encodes this value into a three
    byte value (2 for direction, 1 for magnitude) using the
    DirectionEncoder. The direction encoder is defaulted to a
    RecursiveSphereDirectionEncoder, but can be overridden with the
    set_direction_encoder method. The scale and the bias values for the
    gradient magnitude are used to convert it into a one byte value
    according to v = m*scale + bias where m is the magnitude and v is the
    resulting one byte value.
    
    See Also:
    
    FiniteDifferenceGradientEstimator DirectionEncoder
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEncodedGradientEstimator, obj, update, **traits)
    
    compute_gradient_magnitudes = tvtk_base.true_bool_trait(help=\
        """
        If you don't want to compute gradient magnitudes (but you do want
        normals for shading) this can be used. Be careful - if if you a
        non-constant gradient magnitude transfer function and you turn
        this on, it may crash
        """
    )
    def _compute_gradient_magnitudes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeGradientMagnitudes,
                        self.compute_gradient_magnitudes_)

    cylinder_clip = tvtk_base.false_bool_trait(help=\
        """
        If the data in each slice is only contained within a circle
        circumscribed within the slice, and the slice is square, then
        don't compute anything outside the circle. This circle through
        the slices forms a cylinder.
        """
    )
    def _cylinder_clip_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCylinderClip,
                        self.cylinder_clip_)

    zero_pad = tvtk_base.true_bool_trait(help=\
        """
        Assume that the data value outside the volume is zero when
        computing normals.
        """
    )
    def _zero_pad_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZeroPad,
                        self.zero_pad_)

    bounds_clip = tvtk_base.false_bool_trait(help=\
        """
        Turn on / off the bounding of the normal computation by the
        this->Bounds bounding box
        """
    )
    def _bounds_clip_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundsClip,
                        self.bounds_clip_)

    gradient_magnitude_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scale and bias for the gradient magnitude
        """
    )
    def _gradient_magnitude_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGradientMagnitudeScale,
                        self.gradient_magnitude_scale)

    bounds = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    zero_normal_threshold = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set / Get the zero_normal_threshold - this defines the minimum
        magnitude of a gradient that is considered sufficient to define a
        direction. Gradients with magnitudes at or less than this value
        are given a "zero normal" index. These are handled specially in
        the shader, and you can set the intensity of light for these zero
        normals in the gradient shader.
        """
    )
    def _zero_normal_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZeroNormalThreshold,
                        self.zero_normal_threshold)

    number_of_threads = traits.Trait(2, traits.Range(1, 32, enter_set=True, auto_set=False), help=\
        """
        Get/Set the number of threads to create when encoding normals
        This defaults to the number of available processors on the
        machine
        """
    )
    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

    gradient_magnitude_bias = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scale and bias for the gradient magnitude
        """
    )
    def _gradient_magnitude_bias_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGradientMagnitudeBias,
                        self.gradient_magnitude_bias)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set/Get the scalar input for which the normals will be calculated
        """
    )

    def _get_direction_encoder(self):
        return wrap_vtk(self._vtk_obj.GetDirectionEncoder())
    def _set_direction_encoder(self, arg):
        old_val = self._get_direction_encoder()
        self._wrap_call(self._vtk_obj.SetDirectionEncoder,
                        deref_vtk(arg))
        self.trait_property_changed('direction_encoder', old_val, arg)
    direction_encoder = traits.Property(_get_direction_encoder, _set_direction_encoder, help=\
        """
        Set / Get the direction encoder used to encode normal directions
        to fit within two bytes
        """
    )

    def _get_bounds_clip_max_value(self):
        return self._vtk_obj.GetBoundsClipMaxValue()
    bounds_clip_max_value = traits.Property(_get_bounds_clip_max_value, help=\
        """
        Turn on / off the bounding of the normal computation by the
        this->Bounds bounding box
        """
    )

    def _get_bounds_clip_min_value(self):
        return self._vtk_obj.GetBoundsClipMinValue()
    bounds_clip_min_value = traits.Property(_get_bounds_clip_min_value, help=\
        """
        Turn on / off the bounding of the normal computation by the
        this->Bounds bounding box
        """
    )

    def get_encoded_normal_index(self, *args):
        """
        V.get_encoded_normal_index(int) -> int
        C++: int GetEncodedNormalIndex(int xyz_index)
        V.get_encoded_normal_index(int, int, int) -> int
        C++: int GetEncodedNormalIndex(int x_index, int y_index,
            int z_index)
        Get the encoded normal at an x,y,z location in the volume
        """
        ret = self._wrap_call(self._vtk_obj.GetEncodedNormalIndex, *args)
        return ret

    def _get_input_aspect(self):
        return self._vtk_obj.GetInputAspect()
    input_aspect = traits.Property(_get_input_aspect, help=\
        """
        
        """
    )

    def _get_input_size(self):
        return self._vtk_obj.GetInputSize()
    input_size = traits.Property(_get_input_size, help=\
        """
        
        """
    )

    def _get_last_update_time_in_cpu_seconds(self):
        return self._vtk_obj.GetLastUpdateTimeInCPUSeconds()
    last_update_time_in_cpu_seconds = traits.Property(_get_last_update_time_in_cpu_seconds, help=\
        """
        Get the time required for the last update in seconds or cpu
        seconds
        """
    )

    def _get_last_update_time_in_seconds(self):
        return self._vtk_obj.GetLastUpdateTimeInSeconds()
    last_update_time_in_seconds = traits.Property(_get_last_update_time_in_seconds, help=\
        """
        Get the time required for the last update in seconds or cpu
        seconds
        """
    )

    def _get_use_cylinder_clip(self):
        return self._vtk_obj.GetUseCylinderClip()
    use_cylinder_clip = traits.Property(_get_use_cylinder_clip, help=\
        """
        
        """
    )

    def _get_zero_pad_max_value(self):
        return self._vtk_obj.GetZeroPadMaxValue()
    zero_pad_max_value = traits.Property(_get_zero_pad_max_value, help=\
        """
        Assume that the data value outside the volume is zero when
        computing normals.
        """
    )

    def _get_zero_pad_min_value(self):
        return self._vtk_obj.GetZeroPadMinValue()
    zero_pad_min_value = traits.Property(_get_zero_pad_min_value, help=\
        """
        Assume that the data value outside the volume is zero when
        computing normals.
        """
    )

    def update(self):
        """
        V.update()
        C++: void Update(void)
        Recompute the encoded normals and gradient magnitudes.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('zero_normal_threshold', 'GetZeroNormalThreshold'), ('bounds',
    'GetBounds'), ('compute_gradient_magnitudes',
    'GetComputeGradientMagnitudes'), ('zero_pad', 'GetZeroPad'), ('debug',
    'GetDebug'), ('gradient_magnitude_scale',
    'GetGradientMagnitudeScale'), ('number_of_threads',
    'GetNumberOfThreads'), ('reference_count', 'GetReferenceCount'),
    ('cylinder_clip', 'GetCylinderClip'), ('bounds_clip',
    'GetBoundsClip'), ('gradient_magnitude_bias',
    'GetGradientMagnitudeBias'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['bounds_clip', 'compute_gradient_magnitudes', 'cylinder_clip',
    'debug', 'global_warning_display', 'zero_pad', 'bounds',
    'gradient_magnitude_bias', 'gradient_magnitude_scale',
    'number_of_threads', 'zero_normal_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EncodedGradientEstimator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit EncodedGradientEstimator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['bounds_clip', 'compute_gradient_magnitudes',
            'cylinder_clip', 'zero_pad'], [], ['bounds',
            'gradient_magnitude_bias', 'gradient_magnitude_scale',
            'number_of_threads', 'zero_normal_threshold']),
            title='Edit EncodedGradientEstimator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EncodedGradientEstimator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

