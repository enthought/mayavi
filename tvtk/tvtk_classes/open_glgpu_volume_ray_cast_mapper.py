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

from tvtk.tvtk_classes.gpu_volume_ray_cast_mapper import GPUVolumeRayCastMapper


class OpenGLGPUVolumeRayCastMapper(GPUVolumeRayCastMapper):
    """
    OpenGLGPUVolumeRayCastMapper - open_gl subclass that draws the
    
    Superclass: GPUVolumeRayCastMapper
    
    This is the concrete implementation of a ray cast image display
    helper - a helper class responsible for drawing the image to the
    screen.
    
    See Also:
    
    GPUVolumeRayCastMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLGPUVolumeRayCastMapper, obj, update, **traits)
    
    def open_gl_error_message(self, *args):
        """
        V.open_gl_error_message(int) -> string
        C++: static const char *OpenGLErrorMessage(unsigned int errorCode)
        Return a string matching the open_gl error_code.
        \post result_exists: result!=0
        """
        ret = self._wrap_call(self._vtk_obj.OpenGLErrorMessage, *args)
        return ret

    def print_error(self, *args):
        """
        V.print_error(string)
        C++: static void PrintError(const char *headerMessage)
        Display header_message on the standard output and the last open_gl
        error message if any.
        \pre header_message_exists: header_message!=_0
        """
        ret = self._wrap_call(self._vtk_obj.PrintError, *args)
        return ret

    _updateable_traits_ = \
    (('mask_type', 'GetMaskType'), ('cropping_region_flags',
    'GetCroppingRegionFlags'), ('scalar_mode', 'GetScalarMode'),
    ('maximum_image_sample_distance', 'GetMaximumImageSampleDistance'),
    ('reference_count', 'GetReferenceCount'), ('max_memory_fraction',
    'GetMaxMemoryFraction'), ('report_progress', 'GetReportProgress'),
    ('final_color_window', 'GetFinalColorWindow'),
    ('minimum_image_sample_distance', 'GetMinimumImageSampleDistance'),
    ('blend_mode', 'GetBlendMode'), ('mask_blend_factor',
    'GetMaskBlendFactor'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('auto_adjust_sample_distances',
    'GetAutoAdjustSampleDistances'), ('progress_text', 'GetProgressText'),
    ('max_memory_in_bytes', 'GetMaxMemoryInBytes'), ('final_color_level',
    'GetFinalColorLevel'), ('image_sample_distance',
    'GetImageSampleDistance'), ('abort_execute', 'GetAbortExecute'),
    ('cropping_region_planes', 'GetCroppingRegionPlanes'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('progress', 'GetProgress'), ('cropping', 'GetCropping'),
    ('sample_distance', 'GetSampleDistance'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_adjust_sample_distances', 'cropping',
    'debug', 'global_warning_display', 'release_data_flag', 'blend_mode',
    'cropping_region_flags', 'mask_type', 'scalar_mode',
    'cropping_region_planes', 'final_color_level', 'final_color_window',
    'image_sample_distance', 'mask_blend_factor', 'max_memory_fraction',
    'max_memory_in_bytes', 'maximum_image_sample_distance',
    'minimum_image_sample_distance', 'progress_text', 'report_progress',
    'sample_distance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLGPUVolumeRayCastMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLGPUVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_sample_distances', 'cropping'],
            ['blend_mode', 'cropping_region_flags', 'mask_type', 'scalar_mode'],
            ['cropping_region_planes', 'final_color_level', 'final_color_window',
            'image_sample_distance', 'mask_blend_factor', 'max_memory_fraction',
            'max_memory_in_bytes', 'maximum_image_sample_distance',
            'minimum_image_sample_distance', 'report_progress',
            'sample_distance']),
            title='Edit OpenGLGPUVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLGPUVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

