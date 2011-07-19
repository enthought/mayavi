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


class DescriptiveStatistics(UnivariateStatisticsAlgorithm):
    """
    DescriptiveStatistics - A class for univariate descriptive
    statistics
    
    Superclass: UnivariateStatisticsAlgorithm
    
    Given a selection of columns of interest in an input data table, this
    class provides the following functionalities, depending on the chosen
    execution options:
    * Learn: calculate extremal values, sample mean, and M2, M3, and M4
      aggregates (cf. P. Pebay, Formulas for robust, one-pass parallel
      computation of covariances and Arbitrary-Order Statistical Moments,
    Sandia Report SAND2008-6212, Sep 2008,
      http://infoserve.sandia.gov/sand_doc/2008/086212.pdf for details)
    * Derive: calculate unbiased variance estimator, standard deviation
      estimator, two skewness estimators, and two kurtosis excess
      estimators.
    * Assess: given an input data set, a reference value and a
      non-negative deviation, mark each datum with corresponding relative
    deviation (1-dimensional Mahlanobis distance). If the deviation is
      zero, then mark each datum which are equal to the reference value
      with 0, and all others with 1. By default, the reference value and
      the deviation are, respectively, the mean and the standard
      deviation of the input model.
    * Test: calculate Jarque-Bera statistic and, if VTK to R interface is
    available, retrieve corresponding p-value for normality testing.
    
    Thanks:
    
    Thanks to Philippe Pebay and David Thompson from Sandia National
    Laboratories for implementing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDescriptiveStatistics, obj, update, **traits)
    
    signed_deviations = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the deviations returned should be signed, or
        should only have their magnitude reported. The default is that
        signed deviations will be computed.
        """
    )
    def _signed_deviations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSignedDeviations,
                        self.signed_deviations_)

    unbiased_variance = tvtk_base.true_bool_trait(help=\
        """
        Set/get whether the unbiased estimator for the variance should be
        used, or if the population variance will be calculated. The
        default is that the unbiased estimator will be used.
        """
    )
    def _unbiased_variance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnbiasedVariance,
                        self.unbiased_variance_)

    g1_skewness = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the G1 estimator for the skewness should be used,
        or if the g1 skewness will be calculated. The default is that the
        g1 skewness estimator will be used.
        """
    )
    def _g1_skewness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetG1Skewness,
                        self.g1_skewness_)

    g2_kurtosis = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the G2 estimator for the kurtosis should be used,
        or if the g2 kurtosis will be calculated. The default is that the
        g2 kurtosis estimator will be used.
        """
    )
    def _g2_kurtosis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetG2Kurtosis,
                        self.g2_kurtosis_)

    def set_deviation_parameter(self, *args):
        """
        V.set_deviation_parameter(string)
        C++: void SetDeviationParameter(const char *name)
        A convenience method (in particular for UI wrapping) to set the
        name of the column that contains the deviation for the Assess
        option.
        """
        ret = self._wrap_call(self._vtk_obj.SetDeviationParameter, *args)
        return ret

    def set_nominal_parameter(self, *args):
        """
        V.set_nominal_parameter(string)
        C++: void SetNominalParameter(const char *name)
        A convenience method (in particular for UI wrapping) to set the
        name of the column that contains the nominal value for the Assess
        option.
        """
        ret = self._wrap_call(self._vtk_obj.SetNominalParameter, *args)
        return ret

    _updateable_traits_ = \
    (('assess_option', 'GetAssessOption'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('test_option',
    'GetTestOption'), ('progress_text', 'GetProgressText'),
    ('learn_option', 'GetLearnOption'), ('g2_kurtosis', 'GetG2Kurtosis'),
    ('abort_execute', 'GetAbortExecute'), ('signed_deviations',
    'GetSignedDeviations'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('number_of_primary_tables', 'GetNumberOfPrimaryTables'),
    ('unbiased_variance', 'GetUnbiasedVariance'), ('derive_option',
    'GetDeriveOption'), ('g1_skewness', 'GetG1Skewness'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'g1_skewness', 'g2_kurtosis',
    'global_warning_display', 'release_data_flag', 'signed_deviations',
    'unbiased_variance', 'assess_option', 'derive_option', 'learn_option',
    'number_of_primary_tables', 'progress_text', 'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DescriptiveStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DescriptiveStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['g1_skewness', 'g2_kurtosis', 'signed_deviations',
            'unbiased_variance'], [], ['assess_option', 'derive_option',
            'learn_option', 'number_of_primary_tables', 'test_option']),
            title='Edit DescriptiveStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DescriptiveStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

