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

from tvtk.tvtk_classes.abstract_volume_mapper import AbstractVolumeMapper


class VolumeMapper(AbstractVolumeMapper):
    """
    VolumeMapper - Abstract class for a volume mapper
    
    Superclass: AbstractVolumeMapper
    
    VolumeMapper is the abstract definition of a volume mapper for
    regular rectilinear data (vtk_image_data).  Several  basic types of
    volume mappers are supported.
    
    See Also:
    
    VolumeRayCastMapper VolumeTextureMapper2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeMapper, obj, update, **traits)
    
    cropping = tvtk_base.false_bool_trait(help=\
        """
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
    )
    def _cropping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCropping,
                        self.cropping_)

    cropping_region_flags = traits.Trait('sub_volume',
    tvtk_base.TraitRevPrefixMap({'sub_volume': 8192, 'inverted_fence': 85197125, 'inverted_cross': 129928175, 'cross': 4289552, 'fence': 49020602}), help=\
        """
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
    )
    def _cropping_region_flags_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCroppingRegionFlags,
                        self.cropping_region_flags_)

    blend_mode = traits.Trait('composite',
    tvtk_base.TraitRevPrefixMap({'composite': 0, 'maximum_intensity': 1, 'minimum_intensity': 2, 'additive': 3}), help=\
        """
        Set/Get the blend mode. Currently this is only supported by the
        FixedPointVolumeRayCastMapper - other mappers have different
        ways to set this (supplying a function to a
        VolumeRayCastMapper) or don't have any options
        (vtk_volume_texture_mapper2d supports only compositing). Additive
        blend mode adds scalars along the ray and multiply them by their
        opacity mapping value.
        """
    )
    def _blend_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlendMode,
                        self.blend_mode_)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self):
        """
        V.get_input() -> ImageData
        C++: ImageData *GetInput()
        Set/Get the input data
        """
        ret = wrap_vtk(self._vtk_obj.GetInput())
        return ret
        

    def set_input(self, *args):
        """
        V.set_input(ImageData)
        C++: virtual void SetInput(ImageData *)
        V.set_input(DataSet)
        C++: virtual void SetInput(DataSet *)
        Set/Get the input data
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    cropping_region_planes = traits.Array(shape=(6,), value=(0.0, 1.0, 0.0, 1.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _cropping_region_planes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCroppingRegionPlanes,
                        self.cropping_region_planes)

    def _get_cropping_max_value(self):
        return self._vtk_obj.GetCroppingMaxValue()
    cropping_max_value = traits.Property(_get_cropping_max_value, help=\
        """
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
    )

    def _get_cropping_min_value(self):
        return self._vtk_obj.GetCroppingMinValue()
    cropping_min_value = traits.Property(_get_cropping_min_value, help=\
        """
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
    )

    def _get_voxel_cropping_region_planes(self):
        return self._vtk_obj.GetVoxelCroppingRegionPlanes()
    voxel_cropping_region_planes = traits.Property(_get_voxel_cropping_region_planes, help=\
        """
        Get the cropping region planes in voxels. Only valid during the
        rendering process
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('cropping_region_flags', 'GetCroppingRegionFlags'), ('scalar_mode',
    'GetScalarMode'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('cropping_region_planes', 'GetCroppingRegionPlanes'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('cropping',
    'GetCropping'), ('abort_execute', 'GetAbortExecute'), ('blend_mode',
    'GetBlendMode'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cropping', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'cropping_region_flags',
    'scalar_mode', 'cropping_region_planes', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['cropping'], ['blend_mode', 'cropping_region_flags',
            'scalar_mode'], ['cropping_region_planes']),
            title='Edit VolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

