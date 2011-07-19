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

from tvtk.tvtk_classes.multi_correlative_statistics import MultiCorrelativeStatistics


class PCAStatistics(MultiCorrelativeStatistics):
    """
    PCAStatistics - A class for principal component analysis
    
    Superclass: MultiCorrelativeStatistics
    
    This class derives from the multi-correlative statistics algorithm
    and uses the covariance matrix and Cholesky decomposition computed by
    it. However, when it finalizes the statistics in Learn mode, the PCA
    class computes the SVD of the covariance matrix in order to obtain
    its eigenvectors.
    
    In the assess mode, the input data are
    - projected into the basis defined by the eigenvectors,
    - the energy associated with each datum is computed,
    - or some combination thereof. Additionally, the user may specify
      some threshold energy or eigenvector entry below which the basis is
    truncated. This allows projection into a lower-dimensional state
      while minimizing (in a least squares sense) the projection error.
    
    Thanks:
    
    Thanks to David Thompson, Philippe Pebay and Jackson Mayo from Sandia
    National Laboratories for implementing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPCAStatistics, obj, update, **traits)
    
    fixed_basis_energy = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The minimum energy the new basis should use, as a fraction. See
        set_basis_scheme() for more information. When fixed_basis_energy >= 1
        (the default), the fixed basis energy scheme is equivalent to the
        full basis scheme.
        """
    )
    def _fixed_basis_energy_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFixedBasisEnergy,
                        self.fixed_basis_energy)

    def _get_specified_normalization(self):
        return wrap_vtk(self._vtk_obj.GetSpecifiedNormalization())
    def _set_specified_normalization(self, arg):
        old_val = self._get_specified_normalization()
        self._wrap_call(self._vtk_obj.SetSpecifiedNormalization,
                        deref_vtk(arg))
        self.trait_property_changed('specified_normalization', old_val, arg)
    specified_normalization = traits.Property(_get_specified_normalization, _set_specified_normalization, help=\
        """
        These methods allow you to set/get values used to normalize the
        covariance matrix before PCA. The normalization values apply to
        all requests, so you do not specify a single vector but a
        3-column table.
        
        The first two columns contain the names of columns from input 0
        and the third column contains the value to normalize the
        corresponding entry in the covariance matrix. The table must
        always have 3 columns even when the normalization_scheme is
        DIAGONAL_SPECIFIED. When only diagonal entries are to be used,
        only table rows where the first two columns are identical to one
        another will be employed. If there are multiple rows specifying
        different values for the same pair of columns, the entry nearest
        the bottom of the table takes precedence.
        
        These functions are actually convenience methods that set/get the
        third input of the filter. Because the table is the third input,
        you may use other filters to produce a table of normalizations
        and have the pipeline take care of updates.
        
        Any missing entries will be set to 1.0 and a warning issued. An
        error will occur if the third input to the filter is not set and
        the normalization_scheme is DIAGONAL_SPECIFIED or
        TRIANGLE_SPECIFIED.
        """
    )

    basis_scheme = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This variable controls the dimensionality of output tuples in
        Assess mode. Consider the case where you have requested a PCA on
        D columns.
        
        When set to PCAStatistics::FULL_BASIS, the entire set of basis
        vectors is used to derive new coordinates for each tuple being
        assessed. In this mode, you are guaranteed to have output tuples
        of the same dimension as the input tuples. (That dimension is D,
        so there will be D additional columns added to the table for the
        request.)
        
        When set to PCAStatistics::FIXED_BASIS_SIZE, only the first N
        basis vectors are used to derive new coordinates for each tuple
        being assessed. In this mode, you are guaranteed to have output
        tuples of dimension min(N,D). You must set N prior to assessing
        data using the set_fixed_basis_size() method. When N < D, this turns
        the PCA into a projection (instead of change of basis).
        
        When set to PCAStatistics::FIXED_BASIS_ENERGY, the number of
        basis vectors used to derive new coordinates for each tuple will
        be the minimum number of columns N that satisfy\[ 
        \frac{\sum_{i=1}^{N} \lambda_i}{\sum_{i=1}^{D} \lambda_i} < T\]
        You must set T prior to assessing data using the
        set_fixed_basis_energy() method. When T < 1, this turns the PCA into
        a projection (instead of change of basis).
        
        By default basis_scheme is set to PCAStatistics::FULL_BASIS.
        """
    )
    def _basis_scheme_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBasisScheme,
                        self.basis_scheme)

    fixed_basis_size = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        The number of basis vectors to use. See set_basis_scheme() for more
        information. When fixed_basis_size <= 0 (the default), the fixed
        basis size scheme is equivalent to the full basis scheme.
        """
    )
    def _fixed_basis_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFixedBasisSize,
                        self.fixed_basis_size)

    normalization_scheme = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This determines how (or if) the covariance matrix cov is
        normalized before PCA.
        
        When set to NONE, no normalization is performed. This is the
        default.
        
        When set to TRIANGLE_SPECIFIED, each entry cov(i,j) is divided by
        V(i,j). The list V of normalization factors must be set using the
        set_normalization method before the filter is executed.
        
        When set to DIAGONAL_SPECIFIED, each entry cov(i,j) is divided by
        sqrt(V(i)*V(j)). The list V of normalization factors must be set
        using the set_normalization method before the filter is executed.
        
        When set to DIAGONAL_VARIANCE, each entry cov(i,j) is divided by
        sqrt(cov(i,i)*cov(j,j)). Warning: Although this is accepted
        practice in some fields, some people think you should not turn
        this option on unless there is a good physically-based reason for
        doing so. Much better instead to determine how component
        magnitudes should be compared using physical reasoning and use
        DIAGONAL_SPECIFIED, TRIANGLE_SPECIFIED, or perform some
        pre-processing to shift and scale input data columns
        appropriately than to expect magical results from a shady
        normalization hack.
        """
    )
    def _normalization_scheme_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizationScheme,
                        self.normalization_scheme)

    def get_basis_scheme_name(self, *args):
        """
        V.get_basis_scheme_name(int) -> string
        C++: virtual const char *GetBasisSchemeName(int schemeIndex)
        This variable controls the dimensionality of output tuples in
        Assess mode. Consider the case where you have requested a PCA on
        D columns.
        
        When set to PCAStatistics::FULL_BASIS, the entire set of basis
        vectors is used to derive new coordinates for each tuple being
        assessed. In this mode, you are guaranteed to have output tuples
        of the same dimension as the input tuples. (That dimension is D,
        so there will be D additional columns added to the table for the
        request.)
        
        When set to PCAStatistics::FIXED_BASIS_SIZE, only the first N
        basis vectors are used to derive new coordinates for each tuple
        being assessed. In this mode, you are guaranteed to have output
        tuples of dimension min(N,D). You must set N prior to assessing
        data using the set_fixed_basis_size() method. When N < D, this turns
        the PCA into a projection (instead of change of basis).
        
        When set to PCAStatistics::FIXED_BASIS_ENERGY, the number of
        basis vectors used to derive new coordinates for each tuple will
        be the minimum number of columns N that satisfy\[ 
        \frac{\sum_{i=1}^{N} \lambda_i}{\sum_{i=1}^{D} \lambda_i} < T\]
        You must set T prior to assessing data using the
        set_fixed_basis_energy() method. When T < 1, this turns the PCA into
        a projection (instead of change of basis).
        
        By default basis_scheme is set to PCAStatistics::FULL_BASIS.
        """
        ret = self._wrap_call(self._vtk_obj.GetBasisSchemeName, *args)
        return ret

    def get_eigenvalue(self, *args):
        """
        V.get_eigenvalue(int, int) -> float
        C++: double GetEigenvalue(int request, int i)
        V.get_eigenvalue(int) -> float
        C++: double GetEigenvalue(int i)
        Get the eigenvalues. This function: void get_eigenvalues(int
        request, int i, DoubleArray*); does all of the work. The other
        functions simply call this function with the appropriate
        paramters. These functions are not valid unless Update() has been
        called and the Derive option is turned on.
        """
        ret = self._wrap_call(self._vtk_obj.GetEigenvalue, *args)
        return ret

    def get_eigenvalues(self, *args):
        """
        V.get_eigenvalues(int, DoubleArray)
        C++: void GetEigenvalues(int request, DoubleArray *)
        V.get_eigenvalues(DoubleArray)
        C++: void GetEigenvalues(DoubleArray *)
        Get the eigenvalues. This function: void get_eigenvalues(int
        request, int i, DoubleArray*); does all of the work. The other
        functions simply call this function with the appropriate
        paramters. These functions are not valid unless Update() has been
        called and the Derive option is turned on.
        """
        my_args = deref_array(args, [('int', 'vtkDoubleArray'), ['vtkDoubleArray']])
        ret = self._wrap_call(self._vtk_obj.GetEigenvalues, *my_args)
        return ret

    def get_eigenvector(self, *args):
        """
        V.get_eigenvector(int, DoubleArray)
        C++: void GetEigenvector(int i, DoubleArray *eigenvector)
        V.get_eigenvector(int, int, DoubleArray)
        C++: void GetEigenvector(int request, int i,
            DoubleArray *eigenvector)
        Get the eigenvectors. This function: void get_eigenvectors(int
        request, DoubleArray* eigenvectors) does all of the work. The
        other functions are convenience functions that call this function
        with default arguments. These functions are not valid unless
        Update() has been called and the Derive option is turned on.
        """
        my_args = deref_array(args, [('int', 'vtkDoubleArray'), ('int', 'int', 'vtkDoubleArray')])
        ret = self._wrap_call(self._vtk_obj.GetEigenvector, *my_args)
        return ret

    def get_eigenvectors(self, *args):
        """
        V.get_eigenvectors(int, DoubleArray)
        C++: void GetEigenvectors(int request,
            DoubleArray *eigenvectors)
        V.get_eigenvectors(DoubleArray)
        C++: void GetEigenvectors(DoubleArray *eigenvectors)
        Get the eigenvectors. This function: void get_eigenvectors(int
        request, DoubleArray* eigenvectors) does all of the work. The
        other functions are convenience functions that call this function
        with default arguments. These functions are not valid unless
        Update() has been called and the Derive option is turned on.
        """
        my_args = deref_array(args, [('int', 'vtkDoubleArray'), ['vtkDoubleArray']])
        ret = self._wrap_call(self._vtk_obj.GetEigenvectors, *my_args)
        return ret

    def get_normalization_scheme_name(self, *args):
        """
        V.get_normalization_scheme_name(int) -> string
        C++: virtual const char *GetNormalizationSchemeName(int scheme)
        This determines how (or if) the covariance matrix cov is
        normalized before PCA.
        
        When set to NONE, no normalization is performed. This is the
        default.
        
        When set to TRIANGLE_SPECIFIED, each entry cov(i,j) is divided by
        V(i,j). The list V of normalization factors must be set using the
        set_normalization method before the filter is executed.
        
        When set to DIAGONAL_SPECIFIED, each entry cov(i,j) is divided by
        sqrt(V(i)*V(j)). The list V of normalization factors must be set
        using the set_normalization method before the filter is executed.
        
        When set to DIAGONAL_VARIANCE, each entry cov(i,j) is divided by
        sqrt(cov(i,i)*cov(j,j)). Warning: Although this is accepted
        practice in some fields, some people think you should not turn
        this option on unless there is a good physically-based reason for
        doing so. Much better instead to determine how component
        magnitudes should be compared using physical reasoning and use
        DIAGONAL_SPECIFIED, TRIANGLE_SPECIFIED, or perform some
        pre-processing to shift and scale input data columns
        appropriately than to expect magical results from a shady
        normalization hack.
        """
        ret = self._wrap_call(self._vtk_obj.GetNormalizationSchemeName, *args)
        return ret

    def set_basis_scheme_by_name(self, *args):
        """
        V.set_basis_scheme_by_name(string)
        C++: virtual void SetBasisSchemeByName(const char *schemeName)
        This variable controls the dimensionality of output tuples in
        Assess mode. Consider the case where you have requested a PCA on
        D columns.
        
        When set to PCAStatistics::FULL_BASIS, the entire set of basis
        vectors is used to derive new coordinates for each tuple being
        assessed. In this mode, you are guaranteed to have output tuples
        of the same dimension as the input tuples. (That dimension is D,
        so there will be D additional columns added to the table for the
        request.)
        
        When set to PCAStatistics::FIXED_BASIS_SIZE, only the first N
        basis vectors are used to derive new coordinates for each tuple
        being assessed. In this mode, you are guaranteed to have output
        tuples of dimension min(N,D). You must set N prior to assessing
        data using the set_fixed_basis_size() method. When N < D, this turns
        the PCA into a projection (instead of change of basis).
        
        When set to PCAStatistics::FIXED_BASIS_ENERGY, the number of
        basis vectors used to derive new coordinates for each tuple will
        be the minimum number of columns N that satisfy\[ 
        \frac{\sum_{i=1}^{N} \lambda_i}{\sum_{i=1}^{D} \lambda_i} < T\]
        You must set T prior to assessing data using the
        set_fixed_basis_energy() method. When T < 1, this turns the PCA into
        a projection (instead of change of basis).
        
        By default basis_scheme is set to PCAStatistics::FULL_BASIS.
        """
        ret = self._wrap_call(self._vtk_obj.SetBasisSchemeByName, *args)
        return ret

    def set_normalization_scheme_by_name(self, *args):
        """
        V.set_normalization_scheme_by_name(string)
        C++: virtual void SetNormalizationSchemeByName(const char *sname)
        This determines how (or if) the covariance matrix cov is
        normalized before PCA.
        
        When set to NONE, no normalization is performed. This is the
        default.
        
        When set to TRIANGLE_SPECIFIED, each entry cov(i,j) is divided by
        V(i,j). The list V of normalization factors must be set using the
        set_normalization method before the filter is executed.
        
        When set to DIAGONAL_SPECIFIED, each entry cov(i,j) is divided by
        sqrt(V(i)*V(j)). The list V of normalization factors must be set
        using the set_normalization method before the filter is executed.
        
        When set to DIAGONAL_VARIANCE, each entry cov(i,j) is divided by
        sqrt(cov(i,i)*cov(j,j)). Warning: Although this is accepted
        practice in some fields, some people think you should not turn
        this option on unless there is a good physically-based reason for
        doing so. Much better instead to determine how component
        magnitudes should be compared using physical reasoning and use
        DIAGONAL_SPECIFIED, TRIANGLE_SPECIFIED, or perform some
        pre-processing to shift and scale input data columns
        appropriately than to expect magical results from a shady
        normalization hack.
        """
        ret = self._wrap_call(self._vtk_obj.SetNormalizationSchemeByName, *args)
        return ret

    _updateable_traits_ = \
    (('test_option', 'GetTestOption'), ('fixed_basis_size',
    'GetFixedBasisSize'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('basis_scheme', 'GetBasisScheme'),
    ('assess_option', 'GetAssessOption'), ('progress_text',
    'GetProgressText'), ('learn_option', 'GetLearnOption'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('fixed_basis_energy', 'GetFixedBasisEnergy'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('number_of_primary_tables',
    'GetNumberOfPrimaryTables'), ('derive_option', 'GetDeriveOption'),
    ('normalization_scheme', 'GetNormalizationScheme'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'assess_option', 'basis_scheme', 'derive_option',
    'fixed_basis_energy', 'fixed_basis_size', 'learn_option',
    'normalization_scheme', 'number_of_primary_tables', 'progress_text',
    'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PCAStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PCAStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['assess_option', 'basis_scheme',
            'derive_option', 'fixed_basis_energy', 'fixed_basis_size',
            'learn_option', 'normalization_scheme', 'number_of_primary_tables',
            'test_option']),
            title='Edit PCAStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PCAStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

