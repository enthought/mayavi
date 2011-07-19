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


class ImageWeightedSum(ThreadedImageAlgorithm):
    """
    ImageWeightedSum -  adds any number of images, weighting
    
    Superclass: ThreadedImageAlgorithm
    
    All weights are normalized so they will sum to 1. Images must have
    the same extents. Output is
    
    Thanks:
    
    The original author of this class is Lauren O'Donnell (MIT) for
    Slicer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageWeightedSum, obj, update, **traits)
    
    normalize_by_weight = tvtk_base.true_bool_trait(help=\
        """
        Setting normalize_by_weight on will divide the final result by the
        total weight of the component functions. This process does not
        otherwise normalize the weighted sum By default,
        normalize_by_weight is on.
        """
    )
    def _normalize_by_weight_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizeByWeight,
                        self.normalize_by_weight_)

    def _get_weights(self):
        return wrap_vtk(self._vtk_obj.GetWeights())
    def _set_weights(self, arg):
        old_val = self._get_weights()
        my_arg = deref_array([arg], [['vtkDoubleArray']])
        self._wrap_call(self._vtk_obj.SetWeights,
                        my_arg[0])
        self.trait_property_changed('weights', old_val, arg)
    weights = traits.Property(_get_weights, _set_weights, help=\
        """
        The weights control the contribution of each input to the sum.
        They will be normalized to sum to 1 before filter execution.
        """
    )

    def _get_normalize_by_weight_max_value(self):
        return self._vtk_obj.GetNormalizeByWeightMaxValue()
    normalize_by_weight_max_value = traits.Property(_get_normalize_by_weight_max_value, help=\
        """
        Setting normalize_by_weight on will divide the final result by the
        total weight of the component functions. This process does not
        otherwise normalize the weighted sum By default,
        normalize_by_weight is on.
        """
    )

    def _get_normalize_by_weight_min_value(self):
        return self._vtk_obj.GetNormalizeByWeightMinValue()
    normalize_by_weight_min_value = traits.Property(_get_normalize_by_weight_min_value, help=\
        """
        Setting normalize_by_weight on will divide the final result by the
        total weight of the component functions. This process does not
        otherwise normalize the weighted sum By default,
        normalize_by_weight is on.
        """
    )

    def calculate_total_weight(self):
        """
        V.calculate_total_weight() -> float
        C++: double CalculateTotalWeight()
        Compute the total value of all the weight
        """
        ret = self._vtk_obj.CalculateTotalWeight()
        return ret
        

    def set_weight(self, *args):
        """
        V.set_weight(int, float)
        C++: virtual void SetWeight(IdType id, double weight)
        Change a specific weight. Reallocation is done
        """
        ret = self._wrap_call(self._vtk_obj.SetWeight, *args)
        return ret

    _updateable_traits_ = \
    (('release_data_flag', 'GetReleaseDataFlag'), ('progress_text',
    'GetProgressText'), ('normalize_by_weight', 'GetNormalizeByWeight'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_threads', 'GetNumberOfThreads'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'normalize_by_weight', 'release_data_flag', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageWeightedSum, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageWeightedSum properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['normalize_by_weight'], [], ['number_of_threads']),
            title='Edit ImageWeightedSum properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageWeightedSum properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

