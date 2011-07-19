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

from tvtk.tvtk_classes.bivariate_statistics_algorithm import BivariateStatisticsAlgorithm


class CorrelativeStatistics(BivariateStatisticsAlgorithm):
    """
    CorrelativeStatistics - A class for linear correlation
    
    Superclass: BivariateStatisticsAlgorithm
    
    Given a selection of pairs of columns of interest, this class
    provides the following functionalities, depending on the chosen
    execution options:
    * Learn: calculate extremal values, sample mean, and M2 aggregates
      (cf. P. Pebay, Formulas for robust, one-pass parallel computation
      of covariances and Arbitrary-Order Statistical Moments, Sandia
      Report SAND2008-6212, Sep 2008,
      http://infoserve.sandia.gov/sand_doc/2008/086212.pdf for details)
    * Derive: calculate unbiased variance and covariance estimators,
      estimator of standard deviations, linear regressions, and Pearson
      correlation coefficient.
    * Assess: given an input data set, two means and a 2x2 covariance
      matrix, mark each datum with corresponding relative deviation
      (2-dimensional Mahlanobis distance).
    * Test: no statistical tests available yet.
    
    Thanks:
    
    Thanks to Philippe Pebay and David Thompson from Sandia National
    Laboratories for implementing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCorrelativeStatistics, obj, update, **traits)
    
    _updateable_traits_ = \
    (('assess_option', 'GetAssessOption'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('test_option', 'GetTestOption'),
    ('progress_text', 'GetProgressText'), ('learn_option',
    'GetLearnOption'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('number_of_primary_tables', 'GetNumberOfPrimaryTables'),
    ('derive_option', 'GetDeriveOption'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'assess_option', 'derive_option', 'learn_option',
    'number_of_primary_tables', 'progress_text', 'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CorrelativeStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['assess_option', 'derive_option',
            'learn_option', 'number_of_primary_tables', 'test_option']),
            title='Edit CorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

