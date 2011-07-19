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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class TemporalStatistics(PassInputTypeAlgorithm):
    """
    TemporalStatistics - Compute statistics of point or cell data as
    it changes over time
    
    Superclass: PassInputTypeAlgorithm
    
    Given an input that changes over time, TemporalStatistics looks at
    the data for each time step and computes some statistical information
    of how a point or cell variable changes over time.  For example,
    TemporalStatistics can compute the average value of "pressure"
    over time of each point.
    
    Note that this filter will require the upstream filter to be run on
    every time step that it reports that it can compute.  This may be a
    time consuming operation.
    
    TemporalStatistics ignores the temporal spacing.  Each timestep
    will be weighted the same regardless of how long of an interval it is
    to the next timestep.  Thus, the average statistic may be quite
    different from an integration of the variable if the time spacing
    varies.
    
    Thanks:
    
    This class was originally written by Kenneth Moreland
    (kmorel@sandia.gov) from Sandia National Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalStatistics, obj, update, **traits)
    
    compute_maximum = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the computation of the maximum values over time.  On
        by default.  The resulting array names have "_maximum" appended
        to them.
        """
    )
    def _compute_maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeMaximum,
                        self.compute_maximum_)

    compute_average = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the computation of the average values over time.  On
        by default.  The resulting array names have "_average" appended
        to them.
        """
    )
    def _compute_average_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeAverage,
                        self.compute_average_)

    compute_standard_deviation = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _compute_standard_deviation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeStandardDeviation,
                        self.compute_standard_deviation_)

    compute_minimum = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the computation of the minimum values over time.  On
        by default.  The resulting array names have "_minimum" appended
        to them.
        """
    )
    def _compute_minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeMinimum,
                        self.compute_minimum_)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('compute_average',
    'GetComputeAverage'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('compute_standard_deviation', 'GetComputeStandardDeviation'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('compute_minimum', 'GetComputeMinimum'), ('compute_maximum',
    'GetComputeMaximum'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_average', 'compute_maximum',
    'compute_minimum', 'compute_standard_deviation', 'debug',
    'global_warning_display', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compute_average', 'compute_maximum',
            'compute_minimum', 'compute_standard_deviation'], [], []),
            title='Edit TemporalStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

