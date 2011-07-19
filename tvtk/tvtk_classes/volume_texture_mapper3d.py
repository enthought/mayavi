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


class VolumeTextureMapper3D(VolumeMapper):
    """
    VolumeTextureMapper3D - volume render with 3d texture mapping
    
    Superclass: VolumeMapper
    
    VolumeTextureMapper3D renders a volume using 3d texture mapping.
    This class is actually an abstract superclass - with all the actual
    work done by OpenGLVolumeTextureMapper3D.
    
    This mappers currently supports:
    
    - any data type as input
    - one component, or two or four non-independent components
    - composite blending
    - intermixed opaque geometry
    - multiple volumes can be rendered if they can be sorted into
      back-to-front order (use the FrustumCoverageCuller)
    
    This mapper does not support:
    - more than one independent component
    - maximum intensity projection
    
    Internally, this mapper will potentially change the resolution of the
    input data. The data will be resampled to be a power of two in each
    direction, and also no greater than 128*256*256 voxels (any aspect)
    for one or two component data, or 128*128*256 voxels (any aspect) for
    four component data. The limits are currently hardcoded after a check
    using the gl__proxy__texture3d because some graphics drivers were
    always responding "yes" to the proxy call despite not being able to
    allocate that much texture memory.
    
    Currently, calculations are computed using 8 bits per RGBA channel.
    In the future this should be expanded to handle newer boards that can
    support 15 bit float compositing.
    
    This mapper supports two main families of graphics hardware: nvidia
    and ATI. There are two different implementations of 3d texture
    mapping used - one based on nvidia's GL_NV_texture_shader2 and
    GL_NV_register_combiners2 extension, and one based on ATI's
    GL_ATI_fragment_shader (supported also by some nvidia boards) To use
    this class in an application that will run on various hardware
    configurations, you should have a back-up volume rendering method.
    You should create a VolumeTextureMapper3D, assign its input, make
    sure you have a current open_gl context (you've rendered at least
    once), then call is_render_supported with a VolumeProperty as an
    argument. This method will return 0 if the input has more than one
    independent component, or if the graphics hardware does not support
    the set of required extensions for using at least one of the two
    implemented methods (nvidia or ati)
    
    Thanks:
    
    Thanks to Alexandre Gouaillard at the Megason Lab, Department of
    Systems Biology, Harvard Medical School
    https://wiki.med.harvard.edu/_sys_bio/_megason/ for the idea and initial
    patch to speed-up rendering with compressed textures.
    
    See Also:
    
    VolumeMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeTextureMapper3D, obj, update, **traits)
    
    use_compressed_texture = traits.Bool(False, help=\
        """
        Set/Get if the mapper use compressed textures (if supported by
        the hardware). Initial value is false. There are two reasons to
        use compressed textures: 1. rendering can be 4 times faster. 2.
        It saves some VRAM. There is one reason to not use compressed
        textures: quality may be lower than with uncompressed textures.
        """
    )
    def _use_compressed_texture_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseCompressedTexture,
                        self.use_compressed_texture)

    preferred_render_method = traits.Trait(0, traits.Range(0, 1, enter_set=True, auto_set=False), help=\
        """
        Set the preferred render method. If it is supported, this one
        will be used. Don't allow ATI_METHOD - it is not actually
        supported.
        """
    )
    def _preferred_render_method_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreferredRenderMethod,
                        self.preferred_render_method)

    sample_distance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The distance at which to space sampling planes. This may not be
        honored for interactive renders. An interactive render is defined
        as one that has less than 1 second of allocated render time.
        """
    )
    def _sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDistance,
                        self.sample_distance)

    def _get_actual_sample_distance(self):
        return self._vtk_obj.GetActualSampleDistance()
    actual_sample_distance = traits.Property(_get_actual_sample_distance, help=\
        """
        Allow access to the actual sample distance used to render the
        image.
        """
    )

    def _get_number_of_polygons(self):
        return self._vtk_obj.GetNumberOfPolygons()
    number_of_polygons = traits.Property(_get_number_of_polygons, help=\
        """
        Allow access to the number of polygons used for the rendering.
        """
    )

    def _get_volume_dimensions(self):
        return self._vtk_obj.GetVolumeDimensions()
    volume_dimensions = traits.Property(_get_volume_dimensions, help=\
        """
        These are the dimensions of the 3d texture
        """
    )

    def _get_volume_spacing(self):
        return self._vtk_obj.GetVolumeSpacing()
    volume_spacing = traits.Property(_get_volume_spacing, help=\
        """
        This is the spacing of the 3d texture
        """
    )

    def is_render_supported(self, *args):
        """
        V.is_render_supported(VolumeProperty, Renderer) -> int
        C++: virtual int IsRenderSupported(VolumeProperty *,
            Renderer *r)
        Based on hardware and properties, we may or may not be able to
        render using 3d texture mapping. This indicates if 3d texture
        mapping is supported by the hardware, and if the other extensions
        necessary to support the specific properties are available.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsRenderSupported, *my_args)
        return ret

    def set_preferred_method_to_fragment_program(self):
        """
        V.set_preferred_method_to_fragment_program()
        C++: void SetPreferredMethodToFragmentProgram()
        Set the preferred render method. If it is supported, this one
        will be used. Don't allow ATI_METHOD - it is not actually
        supported.
        """
        ret = self._vtk_obj.SetPreferredMethodToFragmentProgram()
        return ret
        

    def set_preferred_method_to_n_vidia(self):
        """
        V.set_preferred_method_to_n_vidia()
        C++: void SetPreferredMethodToNVidia()
        Set the preferred render method. If it is supported, this one
        will be used. Don't allow ATI_METHOD - it is not actually
        supported.
        """
        ret = self._vtk_obj.SetPreferredMethodToNVidia()
        return ret
        

    _updateable_traits_ = \
    (('use_compressed_texture', 'GetUseCompressedTexture'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('cropping_region_flags', 'GetCroppingRegionFlags'), ('scalar_mode',
    'GetScalarMode'), ('progress_text', 'GetProgressText'),
    ('preferred_render_method', 'GetPreferredRenderMethod'), ('debug',
    'GetDebug'), ('cropping_region_planes', 'GetCroppingRegionPlanes'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('cropping',
    'GetCropping'), ('blend_mode', 'GetBlendMode'), ('abort_execute',
    'GetAbortExecute'), ('sample_distance', 'GetSampleDistance'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cropping', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'cropping_region_flags',
    'scalar_mode', 'cropping_region_planes', 'preferred_render_method',
    'progress_text', 'sample_distance', 'use_compressed_texture'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeTextureMapper3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeTextureMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['cropping'], ['blend_mode', 'cropping_region_flags',
            'scalar_mode'], ['cropping_region_planes', 'preferred_render_method',
            'sample_distance', 'use_compressed_texture']),
            title='Edit VolumeTextureMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeTextureMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

