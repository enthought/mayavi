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

from tvtk.tvtk_classes.volume_texture_mapper3d import VolumeTextureMapper3D


class OpenGLVolumeTextureMapper3D(VolumeTextureMapper3D):
    """
    OpenGLVolumeTextureMapper3D - concrete implementation of 3d volume
    texture mapping
    
    Superclass: VolumeTextureMapper3D
    
    OpenGLVolumeTextureMapper3D renders a volume using 3d texture
    mapping. See VolumeTextureMapper3D for full description.
    
    See Also:
    
    VolumeTextureMapper3D VolumeMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLVolumeTextureMapper3D, obj, update, **traits)
    
    def _get_initialized(self):
        return self._vtk_obj.GetInitialized()
    initialized = traits.Property(_get_initialized, help=\
        """
        
        """
    )

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
            return super(OpenGLVolumeTextureMapper3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLVolumeTextureMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['cropping'], ['blend_mode', 'cropping_region_flags',
            'scalar_mode'], ['cropping_region_planes', 'preferred_render_method',
            'sample_distance', 'use_compressed_texture']),
            title='Edit OpenGLVolumeTextureMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLVolumeTextureMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

