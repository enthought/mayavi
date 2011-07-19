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

from tvtk.tvtk_classes.statistics_algorithm import StatisticsAlgorithm


class MultiCorrelativeStatistics(StatisticsAlgorithm):
    """
    MultiCorrelativeStatistics - A class for linear correlation
    
    Superclass: StatisticsAlgorithm
    
    Given a selection of sets of columns of interest, this class provides
    the following functionalities, depending on the execution mode it is
    executed in:
    * Learn: calculates means, unbiased variance and covariance
      estimators of column pairs coefficient. More precisely, Learn
      calculates the averages and centered variance/covariance sums; if
      finalize is set to true (default), the final statistics are
      calculated. The output metadata on port OUTPUT_MODEL is a
      multiblock dataset containing at a minimum one Table holding the
    raw sums in a sparse matrix style. If finalize is true, then one
      additional Table will be present for each requested set of
      column correlations. These additional tables contain column
      averages, the upper triangular portion of the covariance matrix (in
    the upper right hand portion of the table) and the Cholesky
      decomposition of the covariance matrix (in the lower portion of the
    table beneath the covariance triangle). The leftmost column will be a
    vector of column averages. The last entry in the column averages
      vector is the number of samples. As an example, consider a request
      for a 3-column correlation with columns named col_a, col_b, and col_c.
      The resulting table will look like this:
    
    
         Column  |Mean     |_col_a     |_col_b     |_col_c
    --------+---------+---------+---------+--------- col_a    |avg(A)  
        |cov(A,A) |cov(A,B) |cov(A,C) col_b    |avg(B)  
        |chol(1,1)|cov(B,B) |cov(B,C) col_c    |avg(C)  
        |chol(2,1)|chol(2,2)|cov(C,C)
        Cholesky|length(A)|chol(3,1)|chol(3,2)|chol(3,3) 
    * Assess: given a set of results matrices as specified above in input
    port INPUT_MODEL and tabular data on input port INPUT_DATA that
      contains column names matching those of the tables on input port
      INPUT_MODEL, the assess mode computes the relative deviation of
      each observation in port INPUT_DATA's table according to the linear
      correlations implied by each table in port INPUT_MODEL.
    
    Thanks:
    
    Thanks to Philippe Pebay, Jackson Mayo, and David Thompson of Sandia
    National Laboratories for implementing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMultiCorrelativeStatistics, obj, update, **traits)
    
    _updateable_traits_ = \
    (('test_option', 'GetTestOption'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('assess_option', 'GetAssessOption'),
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
            return super(MultiCorrelativeStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MultiCorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['assess_option', 'derive_option',
            'learn_option', 'number_of_primary_tables', 'test_option']),
            title='Edit MultiCorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MultiCorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

