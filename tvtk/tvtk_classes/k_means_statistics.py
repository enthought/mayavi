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


class KMeansStatistics(StatisticsAlgorithm):
    """
    KMeansStatistics - A class for KMeans clustering
    
    Superclass: StatisticsAlgorithm
    
    This class takes as input an optional Table on port
    LEARN_PARAMETERS specifying initial  set(s) of cluster values of the
    following form:
    
    
              K     | Col1            |  ...    | col_n
    -----------+-----------------+---------+--------------- M    
        |clust_coord(_1, 1) |  ...    | clust_coord(_1, N) M    
        |clust_coord(_2, 1) |  ...    | clust_coord(_2, N) .     |       .   
         |   .     |        . .     |       .         |   .     |       
        . .     |       .         |   .     |        . M    
        |clust_coord(_m, 1) |  ...    | clust_coord(_m, N) L    
        |clust_coord(_1, 1) |  ...    | clust_coord(_1, N) L    
        |clust_coord(_2, 1) |  ...    | clust_coord(_2, N) .     |       .   
         |   .     |        . .     |       .         |   .     |       
        . .     |       .         |   .     |        . L    
        |clust_coord(_l, 1) |  ...    | clust_coord(_l, N) 
    
    Because the desired value of K is often not known in advance and the
    results of the algorithm are dependent on the initial cluster
    centers, we provide a mechanism for the user to test multiple runs or
    sets of cluster centers within a single call to the Learn phase.  The
    first column of the table identifies the number of clusters K in the
    particular run (the entries in this column should be of type
    IdType), while the remaining columns are a subset of the columns
    contained in the table on port INPUT_DATA.  We require that all user
    specified clusters be of the same dimension N and consequently, that
    the LEARN_PARAMETERS table have N+1 columns. Due to this restriction,
    only one request can be processed for each call to the Learn phase
    and subsequent requests are silently ignored. Note that, if the first
    column of the LEARN_PARAMETERS table is not of type IdType, then
    the table will be ignored and a single run will be performed using
    the first default_number_of_clusters input data observations as initial
    cluster centers.
    
    When the user does not supply an initial set of clusters, then the
    first default_number_of_clusters input data observations are used as
    initial cluster centers and a single run is performed.
    
    This class provides the following functionalities, depending on the
    mode it is executed in:
    * Learn: calculates new cluster centers for each run.  The output
      metadata on port OUTPUT_MODEL is a multiblock dataset containing at
    a minimum one Table with columns specifying the following for each
    run: the run ID, number of clusters, number of iterations required
      for convergence, total error associated with the cluster (sum of
      squared Euclidean distance from each observation to its nearest
      cluster center), the cardinality of the cluster, and the new
      cluster coordinates.
    
    *Derive:  An additional Table is stored in the multiblock dataset
        output on port OUTPUT_MODEL. This table contains columns that
        store for each run: the run_id, number of clusters, total error
        for all clusters in the run, local rank, and global rank. The
        local rank is computed by comparing squared Euclidean errors of
        all runs with the same number of clusters.  The global rank is
        computed analagously across all runs.
    
    * Assess: This requires a multiblock dataset (as computed from Learn
      and Derive) on input port INPUT_MODEL and tabular data on input
      port INPUT_DATA that contains column names matching those of the
      tables on input port INPUT_MODEL. The assess mode reports the
      closest cluster center and associated squared Euclidean distance of
    each observation in port INPUT_DATA's table to the cluster centers
      for each run in the multiblock dataset provided on port
      INPUT_MODEL.
    
    The code can handle a wide variety of data types as it operates on
    AbstractArrays and is not limited to DataArrays.  A default
    distance functor that computes the sum of the squares of the
    Euclidean distance between two objects is provided
    (vtk_k_means_distance_functor). The default distance functor can be
    overridden to use alternative distance metrics.
    
    Thanks:
    
    Thanks to Janine Bennett, David Thompson, and Philippe Pebay of
    Sandia National Laboratories for implementing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkKMeansStatistics, obj, update, **traits)
    
    k_values_array_name = traits.String(r"K", enter_set=True, auto_set=False, help=\
        """
        Set/get the k_values_array_name.
        """
    )
    def _k_values_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKValuesArrayName,
                        self.k_values_array_name)

    tolerance = traits.Float(0.01, enter_set=True, auto_set=False, help=\
        """
        Set/get the relative Tolerance used to terminate iterations on
        cluster center coordinates.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    default_number_of_clusters = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Set/get the default_number_of_clusters, used when no initial cluster
        coordinates are specified.
        """
    )
    def _default_number_of_clusters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultNumberOfClusters,
                        self.default_number_of_clusters)

    max_num_iterations = traits.Int(50, enter_set=True, auto_set=False, help=\
        """
        Set/get the max_num_iterations used to terminate iterations on
        cluster center coordinates when the relative tolerance can not be
        met.
        """
    )
    def _max_num_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxNumIterations,
                        self.max_num_iterations)

    def _get_distance_functor(self):
        return wrap_vtk(self._vtk_obj.GetDistanceFunctor())
    def _set_distance_functor(self, arg):
        old_val = self._get_distance_functor()
        self._wrap_call(self._vtk_obj.SetDistanceFunctor,
                        deref_vtk(arg))
        self.trait_property_changed('distance_functor', old_val, arg)
    distance_functor = traits.Property(_get_distance_functor, _set_distance_functor, help=\
        """
        Set the distance_functor.
        """
    )

    _updateable_traits_ = \
    (('test_option', 'GetTestOption'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('assess_option',
    'GetAssessOption'), ('progress_text', 'GetProgressText'),
    ('learn_option', 'GetLearnOption'), ('default_number_of_clusters',
    'GetDefaultNumberOfClusters'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('number_of_primary_tables', 'GetNumberOfPrimaryTables'),
    ('k_values_array_name', 'GetKValuesArrayName'), ('tolerance',
    'GetTolerance'), ('max_num_iterations', 'GetMaxNumIterations'),
    ('derive_option', 'GetDeriveOption'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'assess_option', 'default_number_of_clusters',
    'derive_option', 'k_values_array_name', 'learn_option',
    'max_num_iterations', 'number_of_primary_tables', 'progress_text',
    'test_option', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(KMeansStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit KMeansStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['assess_option', 'default_number_of_clusters',
            'derive_option', 'k_values_array_name', 'learn_option',
            'max_num_iterations', 'number_of_primary_tables', 'test_option',
            'tolerance']),
            title='Edit KMeansStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit KMeansStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

