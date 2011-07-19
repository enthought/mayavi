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


class LineIntegralConvolution2D(Object):
    """
    LineIntegralConvolution2D - GPU-based implementation of Line 
    
    Superclass: Object
    
    This class resorts to GLSL to implement GPU-based Line Integral
    Convolution
     (LIC) for visualizing a 2d vector field that may be obtained by
    projecting
     an original 3d vector field onto a surface (such that the resulting
    2d
     vector at each grid point on the surface is tangential to the local
    normal,
     as done in SurfaceLICPainter).
    
    
     As an image-based technique, 2d LIC works by (1) integrating a
    bidirectional
     streamline from the center of each pixel (of the LIC output image),
    (2)
     locating the pixels along / hit by this streamline as the correlated
    pixels
     of the starting pixel (seed point / pixel), (3) indexing a (usually
    white)
     noise texture (another input to LIC, in addition to the 2d vector
    field,
     usually with the same size as that of the 2d vetor field) to
    determine the
     values (colors) of these pixels (the starting and the correlated
    pixels),
     typically through bi-linear interpolation, and (4) performing
    convolution
     (weighted averaging) on these values, by adopting a low-pass filter
    (such
     as box, ramp, and Hanning kernels), to obtain the result value
    (color) that
     is then assigned to the seed pixel.
    
    
     The GLSL-based GPU implementation herein maps the aforementioned
    pipeline to
     fragment shaders and a box kernel is employed. Both the white noise
    and the
     vector field are provided to the GPU as texture objects (supported
    by the
     multi-texturing capability). In addition, there are four texture
    objects
     (color buffers) allocated to constitute two pairs that work in a
    ping-pong
     fashion, with one as the read buffers and the other as the write /
    render
     targets. Maintained by a frame buffer object
    (GL_EXT_framebuffer_object),
     each pair employs one buffer to store the current (dynamically
    updated)
     position (by means of the texture coordinate that keeps being warped
    by the
     underlying vector) of the (virtual) particle initially released from
    each
     fragment while using the bother buffer to store the current
    (dynamically
     updated too) accumulated texture value that each seed fragment
    (before the
     'mesh' is warped) collects. Given number_of_steps integration steps in
    each
     direction, there are a total of (2 * number_of_steps + 1) fragments
    (including
     the seed fragment) are convolved and each contributes 1 / (2 *
    number_of_steps
     + 1) of the associated texture value to fulfill the box filter.
    
    
     One pass of LIC (basic LIC) tends to produce low-contrast / blurred
    images and
     LineIntegralConvolution2D provides an option for creating
    enhanced LIC
     images. Enhanced LIC improves image quality by increasing
    inter-streamline
     contrast while suppressing artifacts. It performs two passes of LIC,
    with a
     3x3 Laplacian high-pass filter in between that processes the output
    of pass
    #1 LIC and forwards the result as the input 'noise' to pass #2 LIC.
       Enhanced LIC automatically degenerates to basic LIC during user
       interaction.
    
    
     LineIntegralConvolution2D applies masking to zero-vector
    fragments so
     that un-filtered white noise areas are made totally transparent by
    class
     SurfaceLICPainter to show the underlying geometry surface.
    
    Required open_gl Extensins:
    
    
     GL_ARB_texture_non_power_of_two
     GL_VERSION_2_0
     GL_ARB_texture_float
     GL_ARB_draw_buffers
     GL_EXT_framebuffer_object
    
    See Also:
    
    
     SurfaceLICPainter ImageDataLIC2D StructuredGridLIC2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLineIntegralConvolution2D, obj, update, **traits)
    
    transform_vectors = tvtk_base.true_bool_trait(help=\
        """
        This class performs LIC in the normalized image space. Hence, by
        default it transforms the input vectors to the normalized image
        space (using the grid_spacings and input vector field dimensions).
        Set this to 0 to disable tranformation if the vectors are already
        tranformed.
        """
    )
    def _transform_vectors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransformVectors,
                        self.transform_vectors_)

    enhanced_lic = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable enhanced LIC that improves image quality by
        increasing inter-streamline contrast while suppressing artifacts.
        Enhanced LIC performs two passes of LIC, with a 3x3 Laplacian
        high-pass filter in between that processes the output of pass #1
        LIC and forwards the result as the input 'noise' to pass #2 LIC.
        This flag is automatically turned off during user interaction.
        """
    )
    def _enhanced_lic_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnhancedLIC,
                        self.enhanced_lic_)

    lic_for_surface = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _lic_for_surface_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLICForSurface,
                        self.lic_for_surface_)

    def _get_vector_field(self):
        return wrap_vtk(self._vtk_obj.GetVectorField())
    def _set_vector_field(self, arg):
        old_val = self._get_vector_field()
        self._wrap_call(self._vtk_obj.SetVectorField,
                        deref_vtk(arg))
        self.trait_property_changed('vector_field', old_val, arg)
    vector_field = traits.Property(_get_vector_field, _set_vector_field, help=\
        """
        Set/Get the vector field (initial value is NULL).
        """
    )

    def _get_noise(self):
        return wrap_vtk(self._vtk_obj.GetNoise())
    def _set_noise(self, arg):
        old_val = self._get_noise()
        self._wrap_call(self._vtk_obj.SetNoise,
                        deref_vtk(arg))
        self.trait_property_changed('noise', old_val, arg)
    noise = traits.Property(_get_noise, _set_noise, help=\
        """
        Set/Get the input white noise texture (initial value is NULL).
        """
    )

    def _get_lic(self):
        return wrap_vtk(self._vtk_obj.GetLIC())
    def _set_lic(self, arg):
        old_val = self._get_lic()
        self._wrap_call(self._vtk_obj.SetLIC,
                        deref_vtk(arg))
        self.trait_property_changed('lic', old_val, arg)
    lic = traits.Property(_get_lic, _set_lic, help=\
        """
        LIC texture (initial value is NULL) set by Execute().
        """
    )

    number_of_steps = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Number of streamline integration steps (initial value is 1). In
        term of visual quality, the greater (within some range) the
        better.
        """
    )
    def _number_of_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSteps,
                        self.number_of_steps)

    grid_spacings = traits.Array(shape=(2,), value=(1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _grid_spacings_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridSpacings,
                        self.grid_spacings)

    magnification = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        The the magnification factor (default is 1.0).
        """
    )
    def _magnification_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMagnification,
                        self.magnification)

    component_ids = traits.Array(shape=(2,), value=(0, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _component_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentIds,
                        self.component_ids)

    lic_step_size = traits.Trait(0.01, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Get/Set the streamline integration step size (0.01 by default).
        This is the length of each step in normalized image space i.e. in
        range [0, 1]. In term of visual quality, the smaller the better.
        The type for the interface is double as VTK interface is, but GPU
        only supports float. Thus it will be converted to float in the
        execution of the algorithm.
        """
    )
    def _lic_step_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLICStepSize,
                        self.lic_step_size)

    def _get_transform_vectors_max_value(self):
        return self._vtk_obj.GetTransformVectorsMaxValue()
    transform_vectors_max_value = traits.Property(_get_transform_vectors_max_value, help=\
        """
        This class performs LIC in the normalized image space. Hence, by
        default it transforms the input vectors to the normalized image
        space (using the grid_spacings and input vector field dimensions).
        Set this to 0 to disable tranformation if the vectors are already
        tranformed.
        """
    )

    def _get_transform_vectors_min_value(self):
        return self._vtk_obj.GetTransformVectorsMinValue()
    transform_vectors_min_value = traits.Property(_get_transform_vectors_min_value, help=\
        """
        This class performs LIC in the normalized image space. Hence, by
        default it transforms the input vectors to the normalized image
        space (using the grid_spacings and input vector field dimensions).
        Set this to 0 to disable tranformation if the vectors are already
        tranformed.
        """
    )

    def execute(self, *args):
        """
        V.execute() -> int
        C++: int Execute()
        V.execute([int, int, int, int]) -> int
        C++: int Execute(int extent[4])
        Perform the LIC and obtain the LIC texture. Return 1 if no error.
        """
        ret = self._wrap_call(self._vtk_obj.Execute, *args)
        return ret

    def is_supported(self, *args):
        """
        V.is_supported(RenderWindow) -> bool
        C++: static bool IsSupported(RenderWindow *renWin)
        Returns if the context supports the required extensions.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsSupported, *my_args)
        return ret

    def set_vector_shift_scale(self, *args):
        """
        V.set_vector_shift_scale(float, float)
        C++: void SetVectorShiftScale(double shift, double scale)
        On machines where the vector field texture is clamped between
        [0,1], one can specify the shift/scale factor used to convert the
        original vector field to lie in the clamped range. Default is
        (0.0, 1.0);
        """
        ret = self._wrap_call(self._vtk_obj.SetVectorShiftScale, *args)
        return ret

    _updateable_traits_ = \
    (('lic_step_size', 'GetLICStepSize'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('number_of_steps',
    'GetNumberOfSteps'), ('lic_for_surface', 'GetLICForSurface'),
    ('reference_count', 'GetReferenceCount'), ('magnification',
    'GetMagnification'), ('component_ids', 'GetComponentIds'),
    ('transform_vectors', 'GetTransformVectors'), ('grid_spacings',
    'GetGridSpacings'), ('enhanced_lic', 'GetEnhancedLIC'))
    
    _full_traitnames_list_ = \
    (['debug', 'enhanced_lic', 'global_warning_display',
    'lic_for_surface', 'transform_vectors', 'component_ids',
    'grid_spacings', 'lic_step_size', 'magnification', 'number_of_steps'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LineIntegralConvolution2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LineIntegralConvolution2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enhanced_lic', 'lic_for_surface',
            'transform_vectors'], [], ['component_ids', 'grid_spacings',
            'lic_step_size', 'magnification', 'number_of_steps']),
            title='Edit LineIntegralConvolution2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LineIntegralConvolution2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

