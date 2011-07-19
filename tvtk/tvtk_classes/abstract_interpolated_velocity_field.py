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

from tvtk.tvtk_classes.function_set import FunctionSet


class AbstractInterpolatedVelocityField(FunctionSet):
    """
    AbstractInterpolatedVelocityField - An abstract class for 
    
    Superclass: FunctionSet
    
    AbstractInterpolatedVelocityField acts as a continuous velocity
    field
     by performing cell interpolation on the underlying DataSet. This
    is an
     abstract sub-class of FunctionSet, number_of_independent_variables =
    4
     (x,y,z,t) and number_of_functions = 3 (u,v,w). With a brute-force
    scheme,
     every time an evaluation is performed, the target cell containing
    point
     (x,y,z) needs to be found by calling find_cell(), via either
    DataSet or
     AbstractCelllocator's sub-classes (vtk_cell_locator &
    ModifiedBSPTree).
     As it incurs a large cost, one (for
    CellLocatorInterpolatedVelocityField
     via AbstractCellLocator) or two (for InterpolatedVelocityField
    via
     DataSet that involves PointLocator in addressing PointSet)
    levels
     of cell caching may be exploited to increase the performance.
    
    
     For InterpolatedVelocityField, level #0 begins with intra-cell
    caching.
     Specifically if the previous cell is valid and the next point is
    still in
     it ( i.e., Cell::EvaluatePosition() returns 1, coupled with newly
    created
     parametric coordinates & weights ), the function values can be
    interpolated
     and only Cell::EvaluatePosition() is invoked. If this fails, then
    level #1
     follows by inter-cell search for the target cell that contains the
    next point.
     By an inter-cell search, the previous cell provides an important
    clue or serves
     as an immediate neighbor to aid in locating the target cell via
    PointSet::
     find_cell(). If this still fails, a global cell location / search is
    invoked via
     PointSet::FindCell(). Here regardless of either inter-cell or
    global search,
     PointLocator is in fact employed (for datasets of type
    PointSet only, note
     ImageData and RectilinearGrid are able to provide rapid and
    robust cell
     location due to the simple mesh topology) as a crucial tool
    underlying the cell
     locator. However, the use of PointLocator makes
    InterpolatedVelocityField
     non-robust in cell location for PointSet.
    
    
     For CellLocatorInterpolatedVelocityField, the only caching (level
    #0) works
     by intra-cell trial. In case of failure, a global search for the
    target cell is
     invoked via AbstractCellLocator::FindCell() and the actual work
    is done by
     either CellLocator or ModifiedBSPTree (for datasets of type
    PointSet
     only, while ImageData and RectilinearGrid themselves are able
    to provide
     fast robust cell location). Without the involvement of
    PointLocator, robust
     cell location is achieved for PointSet.
    
    Caveats:
    
    
     AbstractInterpolatedVelocityField is not thread safe. A new
    instance
     should be created by each thread.
    
    See Also:
    
    
     InterpolatedVelocityField CellLocatorInterpolatedVelocityField
     GenericInterpolatedVelocityField
    CachingInterpolatedVelocityField
     TemporalInterpolatedVelocityField FunctionSet Streamer
    StreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractInterpolatedVelocityField, obj, update, **traits)
    
    caching = traits.Bool(True, help=\
        """
        Set/Get the caching flag. If this flag is turned ON, there are
        two levels of caching for derived concrete class
        InterpolatedVelocityField and one level of caching for derived
        concrete class CellLocatorInterpolatedVelocityField. Otherwise
        a global cell location is always invoked for evaluating the
        function values at any point.
        """
    )
    def _caching_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCaching,
                        self.caching)

    last_cell_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Get/Set the id of the cell cached from last evaluation.
        """
    )
    def _last_cell_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLastCellId,
                        self.last_cell_id)

    normalize_vector = traits.Bool(False, help=\
        """
        Set/Get the flag indicating vector post-normalization (following
        vector interpolation). Vector post-normalization is required to
        avoid the 'curve-overshooting' problem (caused by high velocity
        magnitude) that occurs when Cell-Length is used as the step size
        unit (particularly the Minimum step size unit). Furthermore, it
        is required by RK45 to achieve, as expected, high numerical
        accuracy (or high smoothness of flow lines) through adaptive step
        sizing. Note this operation is performed (when normalize_vector
        TRUE) right after vector interpolation such that the differing
        amount of contribution of each node (of a cell) to the resulting
        direction of the interpolated vector, due to the possibly
        significantly-differing velocity magnitude values at the nodes
        (which is the case with large cells), can be reflected as is.
        Also note that this flag needs to be turned to FALSE after
        InitialValueProblemSolver:: compute_next_step() as subsequent
        operations, e.g., vorticity computation, may need non-normalized
        vectors.
        """
    )
    def _normalize_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizeVector,
                        self.normalize_vector)

    def _get_cache_hit(self):
        return self._vtk_obj.GetCacheHit()
    cache_hit = traits.Property(_get_cache_hit, help=\
        """
        Get the caching statistics. cache_hit refers to the number of
        level #0 cache hits while cache_miss is the number of level #0
        cache misses.
        """
    )

    def _get_cache_miss(self):
        return self._vtk_obj.GetCacheMiss()
    cache_miss = traits.Property(_get_cache_miss, help=\
        """
        Get the caching statistics. cache_hit refers to the number of
        level #0 cache hits while cache_miss is the number of level #0
        cache misses.
        """
    )

    def _get_last_data_set(self):
        return wrap_vtk(self._vtk_obj.GetLastDataSet())
    last_data_set = traits.Property(_get_last_data_set, help=\
        """
        Get the most recently visited dataset and it id. The dataset is
        used for a guess regarding where the next point will be, without
        searching through all datasets. When setting the last dataset,
        care is needed as no reference counting or checks are performed.
        This feature is intended for custom interpolators only that cache
        datasets independently.
        """
    )

    def _get_last_data_set_index(self):
        return self._vtk_obj.GetLastDataSetIndex()
    last_data_set_index = traits.Property(_get_last_data_set_index, help=\
        """
        Get the most recently visited dataset and it id. The dataset is
        used for a guess regarding where the next point will be, without
        searching through all datasets. When setting the last dataset,
        care is needed as no reference counting or checks are performed.
        This feature is intended for custom interpolators only that cache
        datasets independently.
        """
    )

    def get_last_local_coordinates(self, *args):
        """
        V.get_last_local_coordinates([float, float, float]) -> int
        C++: int GetLastLocalCoordinates(double pcoords[3])
        Get the interpolation weights cached from last evaluation. Return
        1 if the cached cell is valid and 0 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.GetLastLocalCoordinates, *args)
        return ret

    def _get_vectors_selection(self):
        return self._vtk_obj.GetVectorsSelection()
    vectors_selection = traits.Property(_get_vectors_selection, help=\
        """
        Get/Set the name of a spcified vector array. By default it is
        NULL, with the active vector array for use.
        """
    )

    def add_data_set(self, *args):
        """
        V.add_data_set(DataSet)
        C++: virtual void AddDataSet(DataSet *dataset)
        Add a dataset for implicit velocity function evaluation. If more
        than one dataset is added, the evaluation point is searched in
        all until a match is found. THIS FUNCTION DOES NOT CHANGE THE
        REFERENCE COUNT OF dataset FOR THREAD SAFETY REASONS.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddDataSet, *my_args)
        return ret

    def clear_last_cell_id(self):
        """
        V.clear_last_cell_id()
        C++: void ClearLastCellId()
        Set the last cell id to -1 to incur a global cell search for the
        next point.
        """
        ret = self._vtk_obj.ClearLastCellId()
        return ret
        

    def copy_parameters(self, *args):
        """
        V.copy_parameters(AbstractInterpolatedVelocityField)
        C++: virtual void CopyParameters(
            AbstractInterpolatedVelocityField *from)
        Import parameters. Sub-classes can add more after chaining.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyParameters, *my_args)
        return ret

    def select_vectors(self, *args):
        """
        V.select_vectors(string)
        C++: void SelectVectors(const char *fieldName)
        Get/Set the name of a spcified vector array. By default it is
        NULL, with the active vector array for use.
        """
        ret = self._wrap_call(self._vtk_obj.SelectVectors, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('last_cell_id',
    'GetLastCellId'), ('caching', 'GetCaching'), ('normalize_vector',
    'GetNormalizeVector'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'caching', 'last_cell_id',
    'normalize_vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractInterpolatedVelocityField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['caching', 'last_cell_id',
            'normalize_vector']),
            title='Edit AbstractInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

