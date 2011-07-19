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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class ThresholdPoints(PolyDataAlgorithm):
    """
    ThresholdPoints - extracts points whose scalar value satisfies
    threshold criterion
    
    Superclass: PolyDataAlgorithm
    
    ThresholdPoints is a filter that extracts points from a dataset
    that satisfy a threshold criterion. The criterion can take three
    forms:
    1) greater than a particular value; 2) less than a particular value;
       or
    3) between a particular value. The output of the filter is polygonal
       data.
    
    See Also:
    
    Threshold
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThresholdPoints, obj, update, **traits)
    
    upper_threshold = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the upper threshold.
        """
    )
    def _upper_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpperThreshold,
                        self.upper_threshold)

    lower_threshold = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the lower threshold.
        """
    )
    def _lower_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLowerThreshold,
                        self.lower_threshold)

    def threshold_between(self, *args):
        """
        V.threshold_between(float, float)
        C++: void ThresholdBetween(double lower, double upper)
        Criterion is cells whose scalars are between lower and upper
        thresholds (inclusive of the end values).
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdBetween, *args)
        return ret

    def threshold_by_lower(self, *args):
        """
        V.threshold_by_lower(float)
        C++: void ThresholdByLower(double lower)
        Criterion is cells whose scalars are less or equal to lower
        threshold.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByLower, *args)
        return ret

    def threshold_by_upper(self, *args):
        """
        V.threshold_by_upper(float)
        C++: void ThresholdByUpper(double upper)
        Criterion is cells whose scalars are greater or equal to upper
        threshold.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByUpper, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('upper_threshold',
    'GetUpperThreshold'), ('lower_threshold', 'GetLowerThreshold'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'lower_threshold', 'progress_text',
    'upper_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThresholdPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ThresholdPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['lower_threshold', 'upper_threshold']),
            title='Edit ThresholdPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThresholdPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

