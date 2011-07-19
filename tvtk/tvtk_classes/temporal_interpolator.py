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

from tvtk.tvtk_classes.temporal_data_set_algorithm import TemporalDataSetAlgorithm


class TemporalInterpolator(TemporalDataSetAlgorithm):
    """
    TemporalInterpolator - interpolate datasets between time steps to
    produce a new dataset
    
    Superclass: TemporalDataSetAlgorithm
    
    TemporalInterpolator interpolates between two time steps to
    produce new data for an arbitrary T. TemporalInterpolator has
    three modes of operation. The default mode is to produce a continuous
    range of time values as output, which enables a filter downstream to
    request any value of T within the range. The second mode of operation
    is enabled by setting discrete_time_step_interval to a non zero value.
    When this mode is activated, the filter will report a finite number
    of Time steps separated by delta_t between the original range of
    values. This mode is useful when a dataset of N time steps has one
    (or more) missing datasets for certain T values and you simply wish
    to smooth over the missing steps but otherwise use the original data.
    The third mode of operation is enabled by setting resample_factor to a
    non zero positive integer value. When this mode is activated, the
    filter will report a finite number of Time steps which contain the
    original steps, plus N new values between each original step
    1/_resample_factor time units apart. Note that if the input time steps
    are irregular, then using resample_factor will produce an irregular
    sequence of regular steps between each of the original irregular
    steps (clear enough, yes?).
    
    @TODO Higher order interpolation schemes will require changes to the
    API as most calls assume only two timesteps are used.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalInterpolator, obj, update, **traits)
    
    resample_factor = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        When resample_factor is a non zero positive integer, each pair of
        input time steps will be interpolated between with the number of
        steps specified. For example an input of 1,2,3,4,5 and a resample
        factor of 10, will produce steps 0f 1.0, 1.1, 1.2.....1.9, 2.0
        etc NB. Irregular input steps will produce irregular output
        steps. Resample factor wuill only be used if
        discrete_time_step_interval is zero otherwise the
        discrete_time_step_interval takes precedence
        """
    )
    def _resample_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResampleFactor,
                        self.resample_factor)

    discrete_time_step_interval = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        If you require a discrete number of outputs steps, to be
        generated from an input source - for example, you required N
        steps separated by T, then set discrete_time_step_interval to T and
        you will get time__range/_discrete_time_step_interval steps This is a
        useful option to use if you have a dataset with one missing time
        step and wish to 'fill-in' the missing data with an interpolated
        value from the steps either side
        """
    )
    def _discrete_time_step_interval_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiscreteTimeStepInterval,
                        self.discrete_time_step_interval)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('resample_factor', 'GetResampleFactor'), ('progress_text',
    'GetProgressText'), ('discrete_time_step_interval',
    'GetDiscreteTimeStepInterval'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'discrete_time_step_interval', 'progress_text',
    'resample_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['discrete_time_step_interval',
            'resample_factor']),
            title='Edit TemporalInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

