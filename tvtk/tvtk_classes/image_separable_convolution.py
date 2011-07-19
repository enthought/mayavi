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

from tvtk.tvtk_classes.image_decompose_filter import ImageDecomposeFilter


class ImageSeparableConvolution(ImageDecomposeFilter):
    """
    ImageSeparableConvolution -  3 1d convolutions on an image
    
    Superclass: ImageDecomposeFilter
    
    ImageSeparableConvolution performs a convolution along the X, Y,
    and Z axes of an image, based on the three different 1d convolution
    kernels.  The kernels must be of odd size, and are considered to be
    centered at (int)((kernelsize - 1) / 2.0 ).  If a kernel is NULL,
    that dimension is skipped.  This filter is designed to efficiently
    convolve separable filters that can be decomposed into 1 or more 1d
    convolutions.  It also handles arbitrarly large kernel sizes, and
    uses edge replication to handle boundaries.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSeparableConvolution, obj, update, **traits)
    
    def _get_x_kernel(self):
        return wrap_vtk(self._vtk_obj.GetXKernel())
    def _set_x_kernel(self, arg):
        old_val = self._get_x_kernel()
        my_arg = deref_array([arg], [['vtkFloatArray']])
        self._wrap_call(self._vtk_obj.SetXKernel,
                        my_arg[0])
        self.trait_property_changed('x_kernel', old_val, arg)
    x_kernel = traits.Property(_get_x_kernel, _set_x_kernel, help=\
        """
        
        """
    )

    def _get_y_kernel(self):
        return wrap_vtk(self._vtk_obj.GetYKernel())
    def _set_y_kernel(self, arg):
        old_val = self._get_y_kernel()
        my_arg = deref_array([arg], [['vtkFloatArray']])
        self._wrap_call(self._vtk_obj.SetYKernel,
                        my_arg[0])
        self.trait_property_changed('y_kernel', old_val, arg)
    y_kernel = traits.Property(_get_y_kernel, _set_y_kernel, help=\
        """
        
        """
    )

    def _get_z_kernel(self):
        return wrap_vtk(self._vtk_obj.GetZKernel())
    def _set_z_kernel(self, arg):
        old_val = self._get_z_kernel()
        my_arg = deref_array([arg], [['vtkFloatArray']])
        self._wrap_call(self._vtk_obj.SetZKernel,
                        my_arg[0])
        self.trait_property_changed('z_kernel', old_val, arg)
    z_kernel = traits.Property(_get_z_kernel, _set_z_kernel, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('dimensionality', 'GetDimensionality'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'dimensionality', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSeparableConvolution, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSeparableConvolution properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['dimensionality', 'number_of_threads']),
            title='Edit ImageSeparableConvolution properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSeparableConvolution properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

