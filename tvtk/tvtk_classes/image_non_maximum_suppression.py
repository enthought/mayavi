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


class ImageNonMaximumSuppression(ThreadedImageAlgorithm):
    """
    ImageNonMaximumSuppression - Performs non-maximum suppression
    
    Superclass: ThreadedImageAlgorithm
    
    ImageNonMaximumSuppression Sets to zero any pixel that is not a
    peak. If a pixel has a neighbor along the vector that has larger
    magnitude, the smaller pixel is set to zero.  The filter takes two
    inputs: a magnitude and a vector.  Output is magnitude information
    and is always in doubles. Typically this filter is used with
    ImageGradient and ImageGradientMagnitude as inputs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageNonMaximumSuppression, obj, update, **traits)
    
    handle_boundaries = tvtk_base.true_bool_trait(help=\
        """
        If "_handle_boundaries_on" then boundary pixels are duplicated So
        central differences can get values.
        """
    )
    def _handle_boundaries_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleBoundaries,
                        self.handle_boundaries_)

    dimensionality = traits.Trait(2, traits.Range(2, 3, enter_set=True, auto_set=False), help=\
        """
        Determines how the input is interpreted (set of 2d slices or a 3d
        volume)
        """
    )
    def _dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensionality,
                        self.dimensionality)

    def set_magnitude_input(self, *args):
        """
        V.set_magnitude_input(ImageData)
        C++: void SetMagnitudeInput(ImageData *input)
        Set the magnitude and vector inputs.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMagnitudeInput, *my_args)
        return ret

    def set_vector_input(self, *args):
        """
        V.set_vector_input(ImageData)
        C++: void SetVectorInput(ImageData *input)
        Set the magnitude and vector inputs.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVectorInput, *my_args)
        return ret

    _updateable_traits_ = \
    (('dimensionality', 'GetDimensionality'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('handle_boundaries',
    'GetHandleBoundaries'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'handle_boundaries', 'release_data_flag', 'dimensionality',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageNonMaximumSuppression, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageNonMaximumSuppression properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['handle_boundaries'], [], ['dimensionality',
            'number_of_threads']),
            title='Edit ImageNonMaximumSuppression properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageNonMaximumSuppression properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

