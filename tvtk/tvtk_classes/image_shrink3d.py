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


class ImageShrink3D(ThreadedImageAlgorithm):
    """
    ImageShrink3D - Subsamples an image.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageShrink3D shrinks an image by sub sampling on a uniform grid
    (integer multiples).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageShrink3D, obj, update, **traits)
    
    averaging = tvtk_base.true_bool_trait(help=\
        """
        Choose Mean, Minimum, Maximum, Median or sub sampling. The
        neighborhood operations are not centered on the sampled pixel.
        This may cause a half pixel shift in your output image. You can
        changed "Shift" to get around this. ImageGaussianSmooth or
        ImageMean with strides.
        """
    )
    def _averaging_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAveraging,
                        self.averaging_)

    minimum = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimum,
                        self.minimum_)

    median = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _median_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMedian,
                        self.median_)

    maximum = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximum,
                        self.maximum_)

    mean = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _mean_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMean,
                        self.mean_)

    shift = traits.Array(shape=(3,), value=(0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShift,
                        self.shift)

    shrink_factors = traits.Array(shape=(3,), value=(1, 1, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _shrink_factors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShrinkFactors,
                        self.shrink_factors)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('shift', 'GetShift'),
    ('progress_text', 'GetProgressText'), ('maximum', 'GetMaximum'),
    ('debug', 'GetDebug'), ('shrink_factors', 'GetShrinkFactors'),
    ('median', 'GetMedian'), ('minimum', 'GetMinimum'),
    ('number_of_threads', 'GetNumberOfThreads'), ('averaging',
    'GetAveraging'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'),
    ('mean', 'GetMean'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'averaging', 'debug', 'global_warning_display',
    'maximum', 'mean', 'median', 'minimum', 'release_data_flag',
    'number_of_threads', 'progress_text', 'shift', 'shrink_factors'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageShrink3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageShrink3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['averaging', 'maximum', 'mean', 'median', 'minimum'],
            [], ['number_of_threads', 'shift', 'shrink_factors']),
            title='Edit ImageShrink3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageShrink3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

