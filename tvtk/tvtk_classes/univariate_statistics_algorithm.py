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


class UnivariateStatisticsAlgorithm(StatisticsAlgorithm):
    """
    UnivariateStatistics - Base class for univariate statistics 
    
    Superclass: StatisticsAlgorithm
    
    This class specializes statistics algorithms to the univariate case,
    where a number of columns of interest can be selected in the input
    data set. This is done by the means of the following functions:
    
    reset_columns() - reset the list of columns of interest.
    add/_remove_colum( nam_col ) - try to add/remove column with name nam_col
    to/from the list. set_column_status ( nam_col, status ) - mostly for UI
    wrapping purposes, try to add/remove (depending on status) nam_col
    from the list of columns of interest. The verb "try" is used in the
    sense that neither attempting to repeat an existing entry nor to
    remove a non-existent entry will work.
    
    Thanks:
    
    Thanks to Philippe Pebay and David Thompson from Sandia National
    Laboratories for implementing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnivariateStatisticsAlgorithm, obj, update, **traits)
    
    def add_column(self, *args):
        """
        V.add_column(string)
        C++: void AddColumn(const char *namCol)
        Convenience method to create a request with a single column name
        nam_col in a single call; this is the preferred method to select
        columns, ensuring selection consistency (a single column per
        request). Warning: no name checking is performed on nam_col; it is
        the user's responsibility to use valid column names.
        """
        ret = self._wrap_call(self._vtk_obj.AddColumn, *args)
        return ret

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
            return super(UnivariateStatisticsAlgorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit UnivariateStatisticsAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['assess_option', 'derive_option',
            'learn_option', 'number_of_primary_tables', 'test_option']),
            title='Edit UnivariateStatisticsAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnivariateStatisticsAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

