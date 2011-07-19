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

from tvtk.tvtk_classes.table_algorithm import TableAlgorithm


class ThresholdTable(TableAlgorithm):
    """
    ThresholdTable - Thresholds table rows.
    
    Superclass: TableAlgorithm
    
    ThresholdTable uses minimum and/or maximum values to threshold
    table rows based on the values in a particular column. The column to
    threshold is specified using set_input_array_to_process(_0, ...).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThresholdTable, obj, update, **traits)
    
    mode = traits.Trait(0, traits.Range(0, 3, enter_set=True, auto_set=False), help=\
        """
        The mode of the threshold filter.  Options are: ACCEPT_LESS_THAN
        (0) accepts rows with values < max_value; ACCEPT_GREATER_THAN (1)
        accepts rows with values > min_value; ACCEPT_BETWEEN (2) accepts
        rows with values > min_value and < max_value; ACCEPT_OUTSIDE (3)
        accepts rows with values < min_value or > max_value.
        """
    )
    def _mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMode,
                        self.mode)

    def threshold_between(self, *args):
        """
        V.threshold_between(Variant, Variant)
        C++: void ThresholdBetween(Variant lower, Variant upper)
        V.threshold_between(float, float)
        C++: void ThresholdBetween(double lower, double upper)
        Criterion is rows whose scalars are between lower and upper
        thresholds (inclusive of the end values).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ThresholdBetween, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('mode', 'GetMode'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThresholdTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ThresholdTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['mode']),
            title='Edit ThresholdTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThresholdTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

