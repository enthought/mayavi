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

from tvtk.tvtk_classes.image_to_image_filter import ImageToImageFilter


class ImageSpatialFilter(ImageToImageFilter):
    """
    ImageSpatialFilter - Filters that operate on pixel neighborhoods.
    
    Superclass: ImageToImageFilter
    
    ImageSpatialFilter is a super class for filters that operate on an
    input neighborhood for each output pixel. It handles even sized
    neighborhoods, but their can be a half pixel shift associated with
    processing.  This superclass has some logic for handling boundaries. 
    It can split regions into boundary and non-boundary pieces and call
    different execute methods.
    
    Warning:
    
    This used to be the parent class for most imaging filter in VTK4.x,
    now this role has been replaced by ImageSpatialAlgorithm. You
    should consider using ImageSpatialAlgorithm instead, when writing
    filter for VTK5 and above. This class was kept to ensure full
    backward compatibility.
    
    See also:
    
    SimpleImageToImageFilter ImageToImageFilter
    ImageSpatialAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSpatialFilter, obj, update, **traits)
    
    def _get_kernel_middle(self):
        return self._vtk_obj.GetKernelMiddle()
    kernel_middle = traits.Property(_get_kernel_middle, help=\
        """
        
        """
    )

    def _get_kernel_size(self):
        return self._vtk_obj.GetKernelSize()
    kernel_size = traits.Property(_get_kernel_size, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('number_of_threads', 'GetNumberOfThreads'), ('bypass', 'GetBypass'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('input_memory_limit',
    'GetInputMemoryLimit'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'bypass', 'debug', 'global_warning_display',
    'release_data_flag', 'input_memory_limit', 'number_of_threads',
    'progress_text', 'release_data_flag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSpatialFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSpatialFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['bypass'], [], ['input_memory_limit',
            'number_of_threads', 'release_data_flag']),
            title='Edit ImageSpatialFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSpatialFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

