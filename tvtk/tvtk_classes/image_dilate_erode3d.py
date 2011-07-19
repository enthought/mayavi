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


class ImageDilateErode3D(ImageSpatialAlgorithm):
    """
    ImageDilateErode3D - Dilates one value and erodes another.
    
    Superclass: ImageSpatialAlgorithm
    
    ImageDilateErode3D will dilate one value and erode another. It
    uses an elliptical foot print, and only erodes/dilates on the
    boundary of the two values.  The filter is restricted to the X, Y,
    and Z axes for now.  It can degenerate to a 2 or 1 dimensional filter
    by setting the kernel size to 1 for a specific axis.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageDilateErode3D, obj, update, **traits)
    
    erode_value = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Dilate and Erode values to be used by this filter.
        """
    )
    def _erode_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetErodeValue,
                        self.erode_value)

    dilate_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Dilate and Erode values to be used by this filter.
        """
    )
    def _dilate_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDilateValue,
                        self.dilate_value)

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
    (('debug', 'GetDebug'), ('dilate_value', 'GetDilateValue'),
    ('erode_value', 'GetErodeValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_threads',
    'GetNumberOfThreads'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('abort_execute',
    'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'dilate_value', 'erode_value',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageDilateErode3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageDilateErode3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['dilate_value', 'erode_value',
            'number_of_threads']),
            title='Edit ImageDilateErode3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageDilateErode3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

