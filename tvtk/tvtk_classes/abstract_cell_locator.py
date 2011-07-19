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

from tvtk.tvtk_classes.locator import Locator


class AbstractCellLocator(Locator):
    """
    AbstractCellLocator - an abstract base class for locators which
    find cells
    
    Superclass: Locator
    
    AbstractCellLocator is a spatial search object to quickly locate
    cells in 3d. AbstractCellLocator supplies a basic interface which
    concrete subclasses should implement.
    
    Warning:
    
    When deriving a class from AbstractCellLocator, one should include
    the 'hidden' member functions by the following construct in the
    derived class
     //BTX
      using AbstractCellLocator::IntersectWithLine;
      using AbstractCellLocator::FindClosestPoint;
      using AbstractCellLocator::FindClosestPointWithinRadius;
     //ETX
     
    
    See Also:
    
    Locator PointLocator OBBTree CellLocator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractCellLocator, obj, update, **traits)
    
    use_existing_search_structure = tvtk_base.false_bool_trait(help=\
        """
        Some locators support querying a new dataset without rebuilding
        the search structure (typically this may occur when a dataset
        changes due to a time update, but is actually the same topology)
        Turning on this flag enables some locators to skip the rebuilding
        phase
        """
    )
    def _use_existing_search_structure_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseExistingSearchStructure,
                        self.use_existing_search_structure_)

    lazy_evaluation = tvtk_base.false_bool_trait(help=\
        """
        Most Locators build their search structures during build_locator
        but some may delay construction until it is actually needed. If
        lazy_evaluation is supported, this turns on/off the feature. if
        not supported, it is ignored.
        """
    )
    def _lazy_evaluation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLazyEvaluation,
                        self.lazy_evaluation_)

    cache_cell_bounds = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether the bounds of each cell are computed
        only once and then saved.  Should be 10 to 20% faster if
        repeatedly calling any of the Intersect/Find routines and the
        extra memory won't cause disk caching (24 extra bytes per cell
        are required to save the bounds).
        """
    )
    def _cache_cell_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCacheCellBounds,
                        self.cache_cell_bounds_)

    retain_cell_lists = tvtk_base.true_bool_trait(help=\
        """
        Boolean controls whether to maintain list of cells in each node.
        not applicable to all implementations, but if the locator is
        being used as a geometry simplification technique, there is no
        need to keep them.
        """
    )
    def _retain_cell_lists_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRetainCellLists,
                        self.retain_cell_lists_)

    number_of_cells_per_node = traits.Trait(25, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the preferred/maximum number of cells in each
        node/bucket. Default 32. Locators generally operate by
        subdividing space into smaller regions until the number of cells
        in each region (or node) reaches the desired level.
        """
    )
    def _number_of_cells_per_node_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfCellsPerNode,
                        self.number_of_cells_per_node)

    def find_cell(self, *args):
        """
        V.find_cell([float, float, float]) -> int
        C++: virtual IdType FindCell(double x[3])
        Returns the Id of the cell containing the point, returns -1 if no
        cell found. This interface uses a tolerance of zero
        """
        ret = self._wrap_call(self._vtk_obj.FindCell, *args)
        return ret

    def find_cells_along_line(self, *args):
        """
        V.find_cells_along_line([float, float, float], [float, float, float],
             float, IdList)
        C++: virtual void FindCellsAlongLine(double p1[3], double p2[3],
            double tolerance, IdList *cells)
        Given a finite line defined by the two points (p1,p2), return the
        list of unique cell ids in the buckets containing the line. It is
        possible that an empty cell list is returned. The user must
        provide the IdList to populate. This method returns data only
        after the locator has been built.
        """
        my_args = deref_array(args, [(['float', 'float', 'float'], ['float', 'float', 'float'], 'float', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.FindCellsAlongLine, *my_args)
        return ret

    def find_closest_point(self, *args):
        """
        V.find_closest_point([float, float, float], [float, float, float],
            int, int, float)
        C++: virtual void FindClosestPoint(double x[3],
            double closestPoint[3], IdType &cellId, int &subId,
            double &dist2)
        V.find_closest_point([float, float, float], [float, float, float],
            GenericCell, int, int, float)
        C++: virtual void FindClosestPoint(double x[3],
            double closestPoint[3], GenericCell *cell,
            IdType &cellId, int &subId, double &dist2)
        Return the closest point and the cell which is closest to the
        point x. The closest point is somewhere on a cell, it need not be
        one of the vertices of the cell.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FindClosestPoint, *my_args)
        return ret

    def find_closest_point_within_radius(self, *args):
        """
        V.find_closest_point_within_radius([float, float, float], float,
            [float, float, float], int, int, float) -> int
        C++: virtual IdType FindClosestPointWithinRadius(double x[3],
            double radius, double closestPoint[3], IdType &cellId,
            int &subId, double &dist2)
        V.find_closest_point_within_radius([float, float, float], float,
            [float, float, float], GenericCell, int, int, float) -> int
        C++: virtual IdType FindClosestPointWithinRadius(double x[3],
            double radius, double closestPoint[3], GenericCell *cell,
            IdType &cellId, int &subId, double &dist2)
        V.find_closest_point_within_radius([float, float, float], float,
            [float, float, float], GenericCell, int, int, float, int)
            -> int
        C++: virtual IdType FindClosestPointWithinRadius(double x[3],
            double radius, double closestPoint[3], GenericCell *cell,
            IdType &cellId, int &subId, double &dist2, int &inside)
        Return the closest point within a specified radius and the cell
        which is closest to the point x. The closest point is somewhere
        on a cell, it need not be one of the vertices of the cell. This
        method returns 1 if a point is found within the specified radius.
        If there are no cells within the specified radius, the method
        returns 0 and the values of closest_point, cell_id, sub_id, and
        dist2 are undefined.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FindClosestPointWithinRadius, *my_args)
        return ret

    def inside_cell_bounds(self, *args):
        """
        V.inside_cell_bounds([float, float, float], int) -> bool
        C++: virtual bool InsideCellBounds(double x[3], IdType cell_ID)
        Quickly test if a point is inside the bounds of a particular
        cell. Some locators cache cell bounds and this function can make
        use of fast access to the data.
        """
        ret = self._wrap_call(self._vtk_obj.InsideCellBounds, *args)
        return ret

    def intersect_with_line(self, *args):
        """
        V.intersect_with_line([float, float, float], [float, float, float],
            float, float, [float, float, float], [float, float, float],
            int) -> int
        C++: virtual int IntersectWithLine(double p1[3], double p2[3],
            double tol, double &t, double x[3], double pcoords[3],
            int &subId)
        V.intersect_with_line([float, float, float], [float, float, float],
            float, float, [float, float, float], [float, float, float],
            int, int) -> int
        C++: virtual int IntersectWithLine(double p1[3], double p2[3],
            double tol, double &t, double x[3], double pcoords[3],
            int &subId, IdType &cellId)
        V.intersect_with_line([float, float, float], [float, float, float],
            float, float, [float, float, float], [float, float, float],
            int, int, GenericCell) -> int
        C++: virtual int IntersectWithLine(double p1[3], double p2[3],
            double tol, double &t, double x[3], double pcoords[3],
            int &subId, IdType &cellId, GenericCell *cell)
        V.intersect_with_line((float, float, float), (float, float, float),
            Points, IdList) -> int
        C++: virtual int IntersectWithLine(const double p1[3],
            const double p2[3], Points *points, IdList *cellIds)
        Return intersection point (if any) of finite line with cells
        contained in cell locator.
        """
        my_args = deref_array(args, [(['float', 'float', 'float'], ['float', 'float', 'float'], 'float', 'float', ['float', 'float', 'float'], ['float', 'float', 'float'], 'int'), (['float', 'float', 'float'], ['float', 'float', 'float'], 'float', 'float', ['float', 'float', 'float'], ['float', 'float', 'float'], 'int', 'int'), (['float', 'float', 'float'], ['float', 'float', 'float'], 'float', 'float', ['float', 'float', 'float'], ['float', 'float', 'float'], 'int', 'int', 'vtkGenericCell'), (('float', 'float', 'float'), ('float', 'float', 'float'), 'vtkPoints', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.IntersectWithLine, *my_args)
        return ret

    _updateable_traits_ = \
    (('use_existing_search_structure', 'GetUseExistingSearchStructure'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('max_level',
    'GetMaxLevel'), ('retain_cell_lists', 'GetRetainCellLists'), ('debug',
    'GetDebug'), ('automatic', 'GetAutomatic'), ('lazy_evaluation',
    'GetLazyEvaluation'), ('cache_cell_bounds', 'GetCacheCellBounds'),
    ('reference_count', 'GetReferenceCount'), ('number_of_cells_per_node',
    'GetNumberOfCellsPerNode'), ('tolerance', 'GetTolerance'))
    
    _full_traitnames_list_ = \
    (['automatic', 'cache_cell_bounds', 'debug', 'global_warning_display',
    'lazy_evaluation', 'retain_cell_lists',
    'use_existing_search_structure', 'max_level',
    'number_of_cells_per_node', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractCellLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractCellLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic', 'cache_cell_bounds', 'lazy_evaluation',
            'retain_cell_lists', 'use_existing_search_structure'], [],
            ['max_level', 'number_of_cells_per_node', 'tolerance']),
            title='Edit AbstractCellLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractCellLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

