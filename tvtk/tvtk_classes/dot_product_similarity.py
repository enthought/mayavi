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


class DotProductSimilarity(TableAlgorithm):
    """
    DotProductSimilarity - compute dot-product similarity metrics.
    
    Superclass: TableAlgorithm
    
    Treats matrices as collections of vectors and computes dot-product
    similarity metrics between vectors.
    
    The results are returned as an edge-table that lists the index of
    each vector and their computed similarity.  The output edge-table is
    typically used with TableToGraph to create a similarity graph.
    
    This filter can be used with one or two input matrices.  If you
    provide a single matrix as input, every vector in the matrix is
    compared with every other vector. If you provide two matrices, every
    vector in the first matrix is compared with every vector in the
    second matrix.
    
    Note that this filter *only* computes the dot-product between each
    pair of vectors; if you want to compute the cosine of the angles
    between vectors, you will need to normalize the inputs yourself.
    
    Inputs:
      Input port 0: (required) A DenseArraywith two dimensions (a
    matrix).
      Input port 1: (optional) A DenseArraywith two dimensions (a
    matrix).
    
    Outputs:
      Output port 0: A Table containing "source", "target", and
    "similarity" columns.
    
    Caveats:
    
    Note that the complexity of this filter is quadratic!  It also
    requires dense arrays as input, in the future it should be
    generalized to accept sparse arrays.
    
    Thanks:
    
    Developed by Timothy M. Shead (tshead@sandia.gov) at Sandia National
    Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDotProductSimilarity, obj, update, **traits)
    
    lower_diagonal = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        When computing similarities for a single input matrix, controls
        whether the results will include the lower diagonal of the
        similarity matrix.  Default: false.
        """
    )
    def _lower_diagonal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLowerDiagonal,
                        self.lower_diagonal)

    minimum_threshold = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specifies a minimum threshold that a similarity must exceed to be
        included in the output.
        """
    )
    def _minimum_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumThreshold,
                        self.minimum_threshold)

    vector_dimension = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Controls whether to compute similarities for row-vectors or
        column-vectors. 0 = rows, 1 = columns.
        """
    )
    def _vector_dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorDimension,
                        self.vector_dimension)

    upper_diagonal = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        When computing similarities for a single input matrix, controls
        whether the results will include the upper diagonal of the
        similarity matrix.  Default: true.
        """
    )
    def _upper_diagonal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpperDiagonal,
                        self.upper_diagonal)

    minimum_count = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specifies a minimum number of edges to include for each vector.
        """
    )
    def _minimum_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumCount,
                        self.minimum_count)

    second_first = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        When computing similarities for two input matrices, controls
        whether the results will include comparisons from the second
        matrix to the first matrix.
        """
    )
    def _second_first_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSecondFirst,
                        self.second_first)

    diagonal = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        When computing similarities for a single input matrix, controls
        whether the results will include the diagonal of the similarity
        matrix.  Default: false.
        """
    )
    def _diagonal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiagonal,
                        self.diagonal)

    maximum_count = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        Specifies a maximum number of edges to include for each vector.
        """
    )
    def _maximum_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumCount,
                        self.maximum_count)

    first_second = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        When computing similarities for two input matrices, controls
        whether the results will include comparisons from the first
        matrix to the second matrix.
        """
    )
    def _first_second_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFirstSecond,
                        self.first_second)

    _updateable_traits_ = \
    (('second_first', 'GetSecondFirst'), ('vector_dimension',
    'GetVectorDimension'), ('minimum_threshold', 'GetMinimumThreshold'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('upper_diagonal', 'GetUpperDiagonal'), ('maximum_count',
    'GetMaximumCount'), ('progress_text', 'GetProgressText'),
    ('minimum_count', 'GetMinimumCount'), ('diagonal', 'GetDiagonal'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('lower_diagonal', 'GetLowerDiagonal'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('first_second', 'GetFirstSecond'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'diagonal', 'first_second', 'lower_diagonal',
    'maximum_count', 'minimum_count', 'minimum_threshold',
    'progress_text', 'second_first', 'upper_diagonal',
    'vector_dimension'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DotProductSimilarity, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DotProductSimilarity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['diagonal', 'first_second', 'lower_diagonal',
            'maximum_count', 'minimum_count', 'minimum_threshold', 'second_first',
            'upper_diagonal', 'vector_dimension']),
            title='Edit DotProductSimilarity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DotProductSimilarity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

