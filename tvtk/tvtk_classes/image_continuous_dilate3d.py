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

from tvtk.tvtk_classes.image_spatial_algorithm import ImageSpatialAlgorithm


class ImageContinuousDilate3D(ImageSpatialAlgorithm):
    """
    ImageContinuousDilate3D - Dilate implemented as a maximum.
    
    Superclass: ImageSpatialAlgorithm
    
    ImageContinuousDilate3D replaces a pixel with the maximum over an
    ellipsoidal neighborhood.  If kernel_size of an axis is 1, no
    processing is done on that axis.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageContinuousDilate3D, obj, update, **traits)
    
    def set_kernel_size(self, *args):
        """
        V.set_kernel_size(int, int, int)
        C++: void SetKernelSize(int size0, int size1, int size2)
        This method sets the size of the neighborhood.  It also sets the
        default middle of the neighborhood and computes the elliptical
        foot print.
        """
        ret = self._wrap_call(self._vtk_obj.SetKernelSize, *args)
        return ret

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
            return super(ImageContinuousDilate3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageContinuousDilate3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_threads']),
            title='Edit ImageContinuousDilate3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageContinuousDilate3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

