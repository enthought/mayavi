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


class SmartVolumeMapper(VolumeMapper):
    """
    SmartVolumeMapper - Adaptive volume mapper
    
    Superclass: VolumeMapper
    
    SmartVolumeMapper is a volume mapper that will delegate to a
    specific volume mapper based on rendering parameters and available
    hardware. Use the set_requested_render_mode() method to control the
    behavior of the selection. The following options are available:
    
    
     SmartVolumeMapper::DefaultRenderMode:
             Allow the SmartVolumeMapper to select the best mapper
    based on
             rendering parameters and hardware support. If GPU ray
    casting is
             supported, this mapper will be used for all rendering. If
    not,
             then if 3d texture mapping is supported, it will be used for
             interactive rendering and the FixedPointRayCastMapper
    will be
             used for still rendering. If 3d texture mapping is not
    supported,
             then the FixedPointRayCastMapper will be used
    exclusively.
             This is the default requested render mode, and is generally
    the
             best option. When you use this option, your volume will
    always
             be rendered, but the method used to render it may vary based
             on parameters and platform.
    
    
     SmartVolumeMapper::RayCastAndTextureRenderMode:
             Use the VolumeTextureMapper3D for interactive rendering,
             and the FixedPointVolumeRayCastMapper for still renders.
             If 3d texture mapping is not supported, then the ray
             caster will be used exclusively. When you use this option
    your
             volume will always be rendered, but the method used for
             interactive rendering will vary based on parameters and
             platform. The decision on whether a particular render is
             interactive or still is based on the adjustable parameter
             interactive_update_rate. If the desired_update_rate found in the
             RenderWindow that initiated the Render is at or above
             the interactive_update_rate value, then the render is
    considered
             interactive, otherwise it is considered a still render.
    
    
     SmartVolumeMapper::RayCastRenderMode:
             Use the FixedPointVolumeRayCastMapper for both
    interactive and
             still rendering. When you use this option your volume will
    always
             be rendered with the FixedPointVolumeRayCastMapper.
    
    
     SmartVolumeMapper::TextureRenderMode:
             Use the VolumeTextureMapper3D, if supported, for both
             interactive and still rendering. If 3d texture mapping is
    not
             supported (either by the hardware, or due to the rendering
             parameters) then no image will be rendered. Use this option
    only
             if you have already checked for support based on the current
             hardware, number of scalar components, and rendering
    parameters
             in the VolumeProperty. Also note that the
             VolumeTextureMapper3D does not support window / level
             operations on the final image, so final_color_window must be
    at
             the default value of 1.0 and final_color_level must be at the
             default value of 0.5.
    
    
     SmartVolumeMapper::GPURenderMode:
             Use the GPUVolumeRayCastMapper, if supported, for both
             interactive and still rendering. If the GPU ray caster is
    not
             supported (due to hardware limitations or rendering
    parameters)
             then no image will be rendered. Use this option only if you
    have
             already checked for supported based on the current hardware,
             number of scalar components, and rendering parameters in the
             VolumeProperty.
    
    
     You can adjust the contrast and brightness in the rendered image
    using the
     final_color_window and final_color_level ivars. By default the
     final_color_window is set to 1.0, and the final_color_level is set to
    0.5,
     which applies no correction to the computed image. To apply the
    window /
     level operation to the computer image color, first a Scale and Bias
     value are computed:
    
    
     scale = 1.0 / this->_final_color_window
     bias  = 0.5 - this->_final_color_level / this->_final_color_window
    
    
     To compute a new color (R', G', B', A') from an existing color
    (R,G,B,A)
     for a pixel, the following equation is used:
    
    
     R' = R*scale + bias*A
     G' = G*scale + bias*A
     B' = B*scale + bias*A
     A' = A
    
    Note that bias is multiplied by the alpha component before adding
    because the red, green, and blue component of the color are already
    pre-multiplied by alpha. Also note that the window / level operation
    leaves the alpha component unchanged - it only adjusts the RGB
    values.
    
    ----------------------------------------------------------------------
        -------
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSmartVolumeMapper, obj, update, **traits)
    
    requested_render_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'ray_cast_and_texture': 1, 'ray_cast': 2}), help=\
        """
        Set the requested render mode. The default is
        SmartVolumeMapper::DefaultRenderMode.
        """
    )
    def _requested_render_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRequestedRenderMode,
                        self.requested_render_mode_)

    interpolation_mode = traits.Trait('cubic',
    tvtk_base.TraitRevPrefixMap({'nearest_neighbor': 0, 'linear': 1, 'cubic': 3}), help=\
        """
        Set interpolation mode for downsampling (lowres GPU) (initial
        value: cubic).
        """
    )
    def _interpolation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationMode,
                        self.interpolation_mode_)

    interactive_update_rate = traits.Trait(1e-05, traits.Range(1e-10, 10000000000.0, enter_set=True, auto_set=False), help=\
        """
        Set the rate at or above this render will be considered
        interactive. If the desired_update_rate of the RenderWindow that
        caused the Render falls at or above this rate, the render is
        considered interactive and the mapper may be adjusted (depending
        on the render mode). Initial value is 1.0e-5.
        """
    )
    def _interactive_update_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractiveUpdateRate,
                        self.interactive_update_rate)

    final_color_level = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set the final color level. The level controls the brightness of
        the image. The final color window will be centered at the final
        color level, and together represent a linear remapping of color
        values. The default value for the level is 0.5.
        """
    )
    def _final_color_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFinalColorLevel,
                        self.final_color_level)

    max_memory_in_bytes = traits.Int(134217728, enter_set=True, auto_set=False, help=\
        """
        Value passed to the GPU mapper. Ignored by other mappers. Maximum
        size of the 3d texture in GPU memory. Will default to the size
        computed from the graphics card. Can be adjusted by the user.
        Useful if the automatic detection is defective or missing.
        """
    )
    def _max_memory_in_bytes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxMemoryInBytes,
                        self.max_memory_in_bytes)

    max_memory_fraction = traits.Trait(0.75, traits.Range(0.10000000149011612, 1.0, enter_set=True, auto_set=False), help=\
        """
        Value passed to the GPU mapper. Ignored by other mappers. Maximum
        fraction of the max_memory_in_bytes that should be used to hold the
        texture. Valid values are 0.1 to 1.0.
        """
    )
    def _max_memory_fraction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxMemoryFraction,
                        self.max_memory_fraction)

    final_color_window = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the final color window. This controls the contrast of the
        image. The default value is 1.0. The Window can be negative (this
        causes a "negative" effect on the image) Although Window can be
        set to 0.0, any value less than 0.00001 and greater than or equal
        to 0.0 will be set to 0.00001, and any value greater than
        -0.00001 but less than or equal to 0.0 will be set to -0.00001.
        Initial value is 1.0.
        """
    )
    def _final_color_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFinalColorWindow,
                        self.final_color_window)

    def _get_last_used_render_mode(self):
        return self._vtk_obj.GetLastUsedRenderMode()
    last_used_render_mode = traits.Property(_get_last_used_render_mode, help=\
        """
        This will return the render mode used during the previous call to
        Render().
        """
    )

    def create_canonical_view(self, *args):
        """
        V.create_canonical_view(Renderer, Volume, Volume,
            ImageData, int, [float, float, float], [float, float,
            float])
        C++: void CreateCanonicalView(Renderer *ren, Volume *volume,
             Volume *volume2, ImageData *image, int blend_mode,
            double viewDirection[3], double viewUp[3])
        This method can be used to render a representative view of the
        input data into the supplied image given the supplied blending
        mode, view direction, and view up vector.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateCanonicalView, *my_args)
        return ret

    _updateable_traits_ = \
    (('cropping', 'GetCropping'), ('cropping_region_flags',
    'GetCroppingRegionFlags'), ('scalar_mode', 'GetScalarMode'),
    ('requested_render_mode', 'GetRequestedRenderMode'), ('abort_execute',
    'GetAbortExecute'), ('progress_text', 'GetProgressText'),
    ('max_memory_in_bytes', 'GetMaxMemoryInBytes'),
    ('max_memory_fraction', 'GetMaxMemoryFraction'), ('debug',
    'GetDebug'), ('cropping_region_planes', 'GetCroppingRegionPlanes'),
    ('final_color_level', 'GetFinalColorLevel'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('interactive_update_rate',
    'GetInteractiveUpdateRate'), ('blend_mode', 'GetBlendMode'),
    ('final_color_window', 'GetFinalColorWindow'), ('interpolation_mode',
    'GetInterpolationMode'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cropping', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'cropping_region_flags',
    'interpolation_mode', 'requested_render_mode', 'scalar_mode',
    'cropping_region_planes', 'final_color_level', 'final_color_window',
    'interactive_update_rate', 'max_memory_fraction',
    'max_memory_in_bytes', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SmartVolumeMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SmartVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['cropping'], ['blend_mode', 'cropping_region_flags',
            'interpolation_mode', 'requested_render_mode', 'scalar_mode'],
            ['cropping_region_planes', 'final_color_level', 'final_color_window',
            'interactive_update_rate', 'max_memory_fraction',
            'max_memory_in_bytes']),
            title='Edit SmartVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SmartVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

