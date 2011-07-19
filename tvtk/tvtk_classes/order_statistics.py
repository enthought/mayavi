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

from tvtk.tvtk_classes.univariate_statistics_algorithm import UnivariateStatisticsAlgorithm


class OrderStatistics(UnivariateStatisticsAlgorithm):
    """
    OrderStatistics - A class for univariate order statistics
    
    Superclass: UnivariateStatisticsAlgorithm
    
    Given a selection of columns of interest in an input data table, this
    class provides the following functionalities, depending on the
    execution mode it is executed in:
    * Learn: calculate arbitrary quantiles. Provide specific names when
      5-point statistics (minimum, 1st quartile, median, third quartile,
      maximum) requested.
    * Assess: given an input data set and a set of q-quantiles, label
      each datum either with the quantile interval to which it belongs,
      or 0 if it is smaller than smaller quantile, or q if it is larger
      than largest quantile.
    
    Thanks:
    
    Thanks to Philippe Pebay and David Thompson from Sandia National
    Laboratories for implementing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOrderStatistics, obj, update, **traits)
    
    numeric_type = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether histograms and assessment data should be treated
        as numeric data. Otherwise, then everything is treated as
        strings, which always works, and is thus the the default. Note
        that if the data is indeed numeric but this is not set, some
        strange results will occur because of the use of the
        lexicographic order instead of the order on reals.
        """
    )
    def _numeric_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumericType,
                        self.numeric_type_)

    quantile_definition = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the quantile definition.
        """
    )
    def _quantile_definition_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuantileDefinition,
                        self.quantile_definition)

    number_of_intervals = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of quantiles (with uniform spacing).
        """
    )
    def _number_of_intervals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfIntervals,
                        self.number_of_intervals)

    _updateable_traits_ = \
    (('numeric_type', 'GetNumericType'), ('quantile_definition',
    'GetQuantileDefinition'), ('assess_option', 'GetAssessOption'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('test_option',
    'GetTestOption'), ('progress_text', 'GetProgressText'),
    ('learn_option', 'GetLearnOption'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('number_of_primary_tables',
    'GetNumberOfPrimaryTables'), ('number_of_intervals',
    'GetNumberOfIntervals'), ('derive_option', 'GetDeriveOption'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'numeric_type',
    'release_data_flag', 'assess_option', 'derive_option', 'learn_option',
    'number_of_intervals', 'number_of_primary_tables', 'progress_text',
    'quantile_definition', 'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OrderStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OrderStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['numeric_type'], [], ['assess_option',
            'derive_option', 'learn_option', 'number_of_intervals',
            'number_of_primary_tables', 'quantile_definition', 'test_option']),
            title='Edit OrderStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OrderStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

