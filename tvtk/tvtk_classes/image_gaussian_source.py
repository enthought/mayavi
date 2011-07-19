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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageGaussianSource(ImageAlgorithm):
    """
    ImageGaussianSource - Create an image with Gaussian pixel values.
    
    Superclass: ImageAlgorithm
    
    ImageGaussianSource just produces images with pixel values
    determined by a Gaussian.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageGaussianSource, obj, update, **traits)
    
    standard_deviation = traits.Float(100.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the standard deviation of the gaussian
        """
    )
    def _standard_deviation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStandardDeviation,
                        self.standard_deviation)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    maximum = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Maximum value of the gaussian
        """
    )
    def _maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximum,
                        self.maximum)

    def set_whole_extent(self, *args):
        """
        V.set_whole_extent(int, int, int, int, int, int)
        C++: void SetWholeExtent(int xMinx, int xMax, int yMin, int yMax,
            int zMin, int zMax)
        Set/Get the extent of the whole output image.
        """
        ret = self._wrap_call(self._vtk_obj.SetWholeExtent, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('center', 'GetCenter'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('standard_deviation', 'GetStandardDeviation'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('maximum', 'GetMaximum'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'maximum', 'progress_text',
    'standard_deviation'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageGaussianSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageGaussianSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['center', 'maximum', 'standard_deviation']),
            title='Edit ImageGaussianSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageGaussianSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

