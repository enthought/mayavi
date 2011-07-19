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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageConvolve(ThreadedImageAlgorithm):
    """
    ImageConvolve - Convolution of an image with a kernel.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageConvolve convolves the image with a 3d nx_nx_n kernel or a 2d
    nx_n kernal.  The output image is cropped to the same size as the
    input.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageConvolve, obj, update, **traits)
    
    def _get_kernel7x7x7(self):
        return self._vtk_obj.GetKernel7x7x7()
    def _set_kernel7x7x7(self, arg):
        old_val = self._get_kernel7x7x7()
        self._wrap_call(self._vtk_obj.SetKernel7x7x7,
                        arg)
        self.trait_property_changed('kernel7x7x7', old_val, arg)
    kernel7x7x7 = traits.Property(_get_kernel7x7x7, _set_kernel7x7x7, help=\
        """
        Return an array that contains the kernel
        """
    )

    def get_kernel3x3(self, *args):
        """
        V.get_kernel3x3([float, float, float, float, float, float, float,
            float, float])
        C++: void GetKernel3x3(double kernel[9])
        Return an array that contains the kernel.
        """
        ret = self._wrap_call(self._vtk_obj.GetKernel3x3, *args)
        return ret

    def set_kernel3x3(self, *args):
        """
        V.set_kernel3x3((float, float, float, float, float, float, float,
            float, float))
        C++: void SetKernel3x3(const double kernel[9])
        Set the kernel to be a given 3x3 or 5x5 or 7x7 kernel.
        """
        ret = self._wrap_call(self._vtk_obj.SetKernel3x3, *args)
        return ret

    def get_kernel3x3x3(self, *args):
        """
        V.get_kernel3x3x3([float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float])
        C++: void GetKernel3x3x3(double kernel[27])
        Return an array that contains the kernel
        """
        ret = self._wrap_call(self._vtk_obj.GetKernel3x3x3, *args)
        return ret

    def set_kernel3x3x3(self, *args):
        """
        V.set_kernel3x3x3((float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float))
        C++: void SetKernel3x3x3(const double kernel[27])
        Set the kernel to be a 3x3x3 or 5x5x5 or 7x7x7 kernel.
        """
        ret = self._wrap_call(self._vtk_obj.SetKernel3x3x3, *args)
        return ret

    def get_kernel5x5x5(self, *args):
        """
        V.get_kernel5x5x5([float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: void GetKernel5x5x5(double kernel[125])
        Return an array that contains the kernel
        """
        ret = self._wrap_call(self._vtk_obj.GetKernel5x5x5, *args)
        return ret

    def set_kernel5x5x5(self, *args):
        """
        V.set_kernel5x5x5([float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: void SetKernel5x5x5(double kernel[125])
        Set the kernel to be a 3x3x3 or 5x5x5 or 7x7x7 kernel.
        """
        ret = self._wrap_call(self._vtk_obj.SetKernel5x5x5, *args)
        return ret

    def get_kernel5x5(self, *args):
        """
        V.get_kernel5x5([float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float])
        C++: void GetKernel5x5(double kernel[25])
        Return an array that contains the kernel.
        """
        ret = self._wrap_call(self._vtk_obj.GetKernel5x5, *args)
        return ret

    def set_kernel5x5(self, *args):
        """
        V.set_kernel5x5((float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float))
        C++: void SetKernel5x5(const double kernel[25])
        Set the kernel to be a given 3x3 or 5x5 or 7x7 kernel.
        """
        ret = self._wrap_call(self._vtk_obj.SetKernel5x5, *args)
        return ret

    def get_kernel7x7(self, *args):
        """
        V.get_kernel7x7([float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: void GetKernel7x7(double kernel[49])
        Return an array that contains the kernel.
        """
        ret = self._wrap_call(self._vtk_obj.GetKernel7x7, *args)
        return ret

    def set_kernel7x7(self, *args):
        """
        V.set_kernel7x7([float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: void SetKernel7x7(double kernel[49])
        Set the kernel to be a given 3x3 or 5x5 or 7x7 kernel.
        """
        ret = self._wrap_call(self._vtk_obj.SetKernel7x7, *args)
        return ret

    def _get_kernel_size(self):
        return self._vtk_obj.GetKernelSize()
    kernel_size = traits.Property(_get_kernel_size, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('number_of_threads',
    'GetNumberOfThreads'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageConvolve, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageConvolve properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_threads']),
            title='Edit ImageConvolve properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageConvolve properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

