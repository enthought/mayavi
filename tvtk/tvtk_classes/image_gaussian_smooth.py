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


class ImageGaussianSmooth(ThreadedImageAlgorithm):
    """
    ImageGaussianSmooth - Performs a gaussian convolution.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageGaussianSmooth implements a convolution of the input image
    with a gaussian. Supports from one to three dimensional convolutions.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageGaussianSmooth, obj, update, **traits)
    
    dimensionality = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Set/Get the dimensionality of this filter. This determines
        whether a one, two, or three dimensional gaussian is performed.
        """
    )
    def _dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensionality,
                        self.dimensionality)

    standard_deviations = traits.Array(shape=(3,), value=(2.0, 2.0, 2.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _standard_deviations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStandardDeviations,
                        self.standard_deviations)

    radius_factors = traits.Array(shape=(3,), value=(1.5, 1.5, 1.5), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _radius_factors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadiusFactors,
                        self.radius_factors)

    def set_radius_factor(self, *args):
        """
        V.set_radius_factor(float)
        C++: void SetRadiusFactor(double f)
        Sets/Gets the Radius Factors of the gaussian (no unit). The
        radius factors determine how far out the gaussian kernel will go
        before being clamped to zero.
        """
        ret = self._wrap_call(self._vtk_obj.SetRadiusFactor, *args)
        return ret

    def set_standard_deviation(self, *args):
        """
        V.set_standard_deviation(float)
        C++: void SetStandardDeviation(double std)
        V.set_standard_deviation(float, float)
        C++: void SetStandardDeviation(double a, double b)
        V.set_standard_deviation(float, float, float)
        C++: void SetStandardDeviation(double a, double b, double c)
        Sets/Gets the Standard deviation of the gaussian in pixel units.
        """
        ret = self._wrap_call(self._vtk_obj.SetStandardDeviation, *args)
        return ret

    _updateable_traits_ = \
    (('dimensionality', 'GetDimensionality'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('standard_deviations', 'GetStandardDeviations'),
    ('abort_execute', 'GetAbortExecute'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'),
    ('reference_count', 'GetReferenceCount'), ('radius_factors',
    'GetRadiusFactors'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'dimensionality', 'number_of_threads',
    'progress_text', 'radius_factors', 'standard_deviations'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageGaussianSmooth, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageGaussianSmooth properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['dimensionality', 'number_of_threads',
            'radius_factors', 'standard_deviations']),
            title='Edit ImageGaussianSmooth properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageGaussianSmooth properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

