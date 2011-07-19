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


class KdTree(Locator):
    """
    KdTree - a Kd-tree spatial decomposition of a set of points
    
    Superclass: Locator
    
    Given one or more DataSets, create a load balancing
        k-d tree decomposition of the points at the center of the cells.
        Or, create a k-d tree point locator from a list of points.
    
    
        This class can also generate a poly_data representation of
        the boundaries of the spatial regions in the decomposition.
    
    
        It can sort the regions with respect to a viewing direction,
        and it can decompose a list of regions into subsets, each
        of which represent a convex spatial region (since many algorithms
        require a convex region).
    
    
        If the points were derived from cells, KdTree
        can create a list of cell Ids for each region for each data set.
        Two lists are available - all cells with centroid in the region,
        and all cells that intersect the region but whose centroid lies
        in another region.
    
    
        For the purpose of removing duplicate points quickly from large
        data sets, or for finding nearby points, we added another mode
    for
        building the locator.  build_locator_from_points will build a k-d
    tree
        from one or more Points objects.  This can be followed by
        build_map_for_duplicate_points which returns a mapping from the
    original
        ids to a subset of the ids that is unique within a supplied
        tolerance, or you can use find_point and find_closest_point to
        locate points in the original set that the tree was built from.
    
    See Also:
    
    
         Locator CellLocator PKdTree
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkKdTree, obj, update, **traits)
    
    generate_representation_using_data_bounds = tvtk_base.false_bool_trait(help=\
        """
        The polydata representation of the k-d tree shows the boundaries
           of the k-d tree decomposition spatial regions.  The data
        inside
           the regions may not occupy the entire space.  To draw just the
           bounds of the data in the regions, set this variable ON.
        """
    )
    def _generate_representation_using_data_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateRepresentationUsingDataBounds,
                        self.generate_representation_using_data_bounds_)

    timing = tvtk_base.false_bool_trait(help=\
        """
        Turn on timing of the k-d tree build
        """
    )
    def _timing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTiming,
                        self.timing_)

    include_region_boundary_cells = tvtk_base.false_bool_trait(help=\
        """
        If include_region_boundary_cells is ON,
          create_cell_lists() will also create a list of cells which
          intersect a given region, but are not assigned
          to the region.  These lists are obtained with
          get_boundary_cell_list().  Default is OFF.
        """
    )
    def _include_region_boundary_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIncludeRegionBoundaryCells,
                        self.include_region_boundary_cells_)

    def _get_cuts(self):
        return wrap_vtk(self._vtk_obj.GetCuts())
    def _set_cuts(self, arg):
        old_val = self._get_cuts()
        self._wrap_call(self._vtk_obj.SetCuts,
                        deref_vtk(arg))
        self.trait_property_changed('cuts', old_val, arg)
    cuts = traits.Property(_get_cuts, _set_cuts, help=\
        """
        Get a BSPCuts object, a general object representing an axis-
          aligned spatial partitioning.  Used by BSPIntersections.
        """
    )

    min_cells = traits.Int(100, enter_set=True, auto_set=False, help=\
        """
        Minimum number of cells per spatial region.  Default is 100.
        """
    )
    def _min_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinCells,
                        self.min_cells)

    number_of_regions_or_less = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of spatial regions you want to get close
          to without going over.  (The number of spatial regions is
        normally
          a power of two.)  Call this before build_locator().  Default
          is unset (0).
        """
    )
    def _number_of_regions_or_less_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfRegionsOrLess,
                        self.number_of_regions_or_less)

    def get_data_set(self, *args):
        """
        V.get_data_set(int) -> DataSet
        C++: DataSet *GetDataSet(int n)
        V.get_data_set() -> DataSet
        C++: DataSet *GetDataSet()
        Return the n'th data set.
        """
        ret = self._wrap_call(self._vtk_obj.GetDataSet, *args)
        return wrap_vtk(ret)

    def set_data_set(self, *args):
        """
        V.set_data_set(DataSet)
        C++: virtual void SetDataSet(DataSet *set)
        Clear out all data sets and replace with single data set.  For
        backward compatibility with superclass.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataSet, *my_args)
        return ret

    number_of_regions_or_more = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of spatial regions you want to get close
          to while having at least this many regions.  (The number of
          spatial regions is normally a power of two.)   Default
          is unset (0).
        """
    )
    def _number_of_regions_or_more_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfRegionsOrMore,
                        self.number_of_regions_or_more)

    fudge_factor = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Some algorithms on k-d trees require a value that is a very
         small distance relative to the diameter of the entire space
         divided by the k-d tree.  This factor is the maximum
        axis-aligned
         width of the space multipled by 10e-6.
        """
    )
    def _fudge_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFudgeFactor,
                        self.fudge_factor)

    def get_boundary_cell_list(self, *args):
        """
        V.get_boundary_cell_list(int) -> IdList
        C++: IdList *GetBoundaryCellList(int regionID)
        The cell list obtained with get_cell_list is the list
           of all cells such that their centroid is contained in
           the spatial region.  It may also be desirable to get
           a list of all cells intersecting a spatial region,
           but with centroid in some other region.  This is that
           list.  This list is computed in create_cell_lists() if
           and only if include_region_boundary_cells is ON.  This
           returns a pointer to kd_tree's memory, so don't free it.
        """
        ret = self._wrap_call(self._vtk_obj.GetBoundaryCellList, *args)
        return wrap_vtk(ret)

    def get_cell_list(self, *args):
        """
        V.get_cell_list(int) -> IdList
        C++: IdList *GetCellList(int regionID)
        Get the cell list for a region.  This returns a pointer
           to KdTree's memory, so don't free it.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellList, *args)
        return wrap_vtk(ret)

    def get_cell_lists(self, *args):
        """
        V.get_cell_lists(IntArray, int, IdList, IdList) -> int
        C++: IdType GetCellLists(IntArray *regions, int set,
            IdList *inRegionCells, IdList *onBoundaryCells)
        V.get_cell_lists(IntArray, DataSet, IdList, IdList)
            -> int
        C++: IdType GetCellLists(IntArray *regions, DataSet *set,
             IdList *inRegionCells, IdList *onBoundaryCells)
        V.get_cell_lists(IntArray, IdList, IdList) -> int
        C++: IdType GetCellLists(IntArray *regions,
            IdList *inRegionCells, IdList *onBoundaryCells)
        For a list of regions, get two cell lists.  The first lists
          the IDs  all cells whose centroids lie in one of the regions.
          The second lists the IDs of all cells that intersect the
        regions,
          but whose centroid lies in a region not on the list.
        
        
          The total number of cell IDs written to both lists is returned.
          Either list pointer passed in can be NULL, and it will be
        ignored.
          If there are multiple data sets, you must specify which data
        set
          you wish cell IDs for.
        
        
          The caller should delete these two lists when done.  This
        method
          uses the cell lists created in create_cell_lists().
          If the cell list for any of the requested regions does not
          exist, then this method will call create_cell_lists() to create
          cell lists for *every* region of the k-d tree.  You must
        remember
          to delete_cell_lists() when done with all calls to this method,
        as
          cell lists can require a great deal of memory.
        """
        my_args = deref_array(args, [('vtkIntArray', 'int', 'vtkIdList', 'vtkIdList'), ('vtkIntArray', 'vtkDataSet', 'vtkIdList', 'vtkIdList'), ('vtkIntArray', 'vtkIdList', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetCellLists, *my_args)
        return ret

    def get_data_set_index(self, *args):
        """
        V.get_data_set_index(DataSet) -> int
        C++: int GetDataSetIndex(DataSet *set)
        Return the index of the given data set.  Returns -1 if that data
        set does not exist.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDataSetIndex, *my_args)
        return ret

    def _get_data_sets(self):
        return wrap_vtk(self._vtk_obj.GetDataSets())
    data_sets = traits.Property(_get_data_sets, help=\
        """
        Return a collection of all the data sets.
        """
    )

    def _get_number_of_data_sets(self):
        return self._vtk_obj.GetNumberOfDataSets()
    number_of_data_sets = traits.Property(_get_number_of_data_sets, help=\
        """
        Get the number of data sets included in spatial paritioning
        """
    )

    def _get_number_of_regions(self):
        return self._vtk_obj.GetNumberOfRegions()
    number_of_regions = traits.Property(_get_number_of_regions, help=\
        """
        The number of leaf nodes of the tree, the spatial regions
        """
    )

    def get_points_in_region(self, *args):
        """
        V.get_points_in_region(int) -> IdTypeArray
        C++: IdTypeArray *GetPointsInRegion(int regionId)
        Get a list of the original IDs of all points in a region.  You
        must have called build_locator_from_points before calling this.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointsInRegion, *args)
        return wrap_vtk(ret)

    def get_region_bounds(self, *args):
        """
        V.get_region_bounds(int, [float, float, float, float, float, float])
        C++: void GetRegionBounds(int regionID, double bounds[6])
        Get the spatial bounds of k-d tree region
        """
        ret = self._wrap_call(self._vtk_obj.GetRegionBounds, *args)
        return ret

    def get_region_containing_cell(self, *args):
        """
        V.get_region_containing_cell(DataSet, int) -> int
        C++: int GetRegionContainingCell(DataSet *set,
            IdType cellID)
        V.get_region_containing_cell(int, int) -> int
        C++: int GetRegionContainingCell(int set, IdType cellID)
        V.get_region_containing_cell(int) -> int
        C++: int GetRegionContainingCell(IdType cellID)
        Get the id of the region containing the cell centroid.  If
           no data_set is specified, assume data_set 0.  If you need the
           region ID for every cell, use all_get_region_containing_cell
           instead.  It is more efficient.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetRegionContainingCell, *my_args)
        return ret

    def get_region_containing_point(self, *args):
        """
        V.get_region_containing_point(float, float, float) -> int
        C++: int GetRegionContainingPoint(double x, double y, double z)
        Get the id of the region containing the specified location.
        """
        ret = self._wrap_call(self._vtk_obj.GetRegionContainingPoint, *args)
        return ret

    def get_region_data_bounds(self, *args):
        """
        V.get_region_data_bounds(int, [float, float, float, float, float,
            float])
        C++: void GetRegionDataBounds(int regionID, double bounds[6])
        Get the bounds of the data within the k-d tree region
        """
        ret = self._wrap_call(self._vtk_obj.GetRegionDataBounds, *args)
        return ret

    def add_data_set(self, *args):
        """
        V.add_data_set(DataSet)
        C++: virtual void AddDataSet(DataSet *set)
        This class can compute a spatial decomposition based on the cells
        in a list of one or more input data sets.  Add them one at a time
        with this method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddDataSet, *my_args)
        return ret

    def build_locator_from_points(self, *args):
        """
        V.build_locator_from_points(PointSet)
        C++: void BuildLocatorFromPoints(PointSet *pointset)
        V.build_locator_from_points(Points)
        C++: void BuildLocatorFromPoints(Points *ptArray)
        This is a special purpose locator that builds a k-d tree to find
        duplicate and near-by points.  It builds the tree from one or
        more Points objects instead of from the cells of a DataSet.
         This build would normally be followed by
        build_map_for_duplicate_points, find_point, or find_closest_point. Since
        this will build a normal k-d tree, all the region intersection
        queries will still work, as will most other calls except those
        that have "Cell" in the name.
        
        This method works most efficiently when the point arrays are
        float arrays.
        """
        my_args = deref_array(args, [['vtkPointSet'], ['vtkPoints']])
        ret = self._wrap_call(self._vtk_obj.BuildLocatorFromPoints, *my_args)
        return ret

    def build_map_for_duplicate_points(self, *args):
        """
        V.build_map_for_duplicate_points(float) -> IdTypeArray
        C++: IdTypeArray *BuildMapForDuplicatePoints(float tolerance)
        This call returns a mapping from the original point IDs supplied
        to build_locator_from_points to a subset of those IDs that is unique
        within the specified tolerance. If points 2, 5, and 12 are the
        same, then id_map[_2] = id_map[_5] = id_map[_12] = 2 (or 5 or 12).
        
        "original point IDs" - For point IDs we start at 0 for the first
        point in the first Points object, and increase by 1 for
        subsequent points and subsequent Points objects.
        
        You must have called build_locator_from_points() before calling
        this. You are responsible for deleting the returned array.
        """
        ret = self._wrap_call(self._vtk_obj.BuildMapForDuplicatePoints, *args)
        return wrap_vtk(ret)

    def copy_tree(self, *args):
        """
        V.copy_tree(KdNode) -> KdNode
        C++: static KdNode *CopyTree(KdNode *kd)
        Create a copy of the binary tree representation of the
           k-d tree spatial partitioning provided.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyTree, *my_args)
        return wrap_vtk(ret)

    def create_cell_lists(self):
        """
        V.create_cell_lists()
        C++: void CreateCellLists()
        Create a list for each of the requested regions, listing
          the IDs of all cells whose centroid falls in the region.
          These lists are obtained with get_cell_list().
          If no data_set is specified, the cell list is created
          for data_set 0.  If no list of requested regions is provided,
          the cell lists for all regions are created.
        
        
          When create_cell_lists is called again, the lists created
          on the previous call  are deleted.
        """
        ret = self._vtk_obj.CreateCellLists()
        return ret
        

    def delete_cell_lists(self):
        """
        V.delete_cell_lists()
        C++: void DeleteCellLists()
        Free the memory used by the cell lists.
        """
        ret = self._vtk_obj.DeleteCellLists()
        return ret
        

    def find_closest_n_points(self, *args):
        """
        V.find_closest_n_points(int, (float, float, float), IdList)
        C++: void FindClosestNPoints(int N, const double x[3],
            IdList *result)
        Find the closest N points to a position. This returns the closest
        N points to a position. A faster method could be created that
        returned N close points to a position, but necessarily the exact
        N closest. The returned points are sorted from closest to
        farthest. These methods are thread safe if build_locator() is
        directly or indirectly called from a single thread first.
        """
        my_args = deref_array(args, [('int', ('float', 'float', 'float'), 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.FindClosestNPoints, *my_args)
        return ret

    def find_closest_point(self, *args):
        """
        V.find_closest_point(float, float, float, float) -> int
        C++: IdType FindClosestPoint(double x, double y, double z,
            double &dist2)
        Find the Id of the point that was previously supplied to
        build_locator_from_points() which is closest to the given point. Set
        the square of the distance between the two points.
        """
        ret = self._wrap_call(self._vtk_obj.FindClosestPoint, *args)
        return ret

    def find_closest_point_in_region(self, *args):
        """
        V.find_closest_point_in_region(int, float, float, float, float) -> int
        C++: IdType FindClosestPointInRegion(int regionId, double x,
            double y, double z, double &dist2)
        Find the Id of the point in the given region which is closest to
        the given point.  Return the ID of the point, and set the square
        of the distance of between the points.
        """
        ret = self._wrap_call(self._vtk_obj.FindClosestPointInRegion, *args)
        return ret

    def find_closest_point_within_radius(self, *args):
        """
        V.find_closest_point_within_radius(float, (float, float, float),
            float) -> int
        C++: IdType FindClosestPointWithinRadius(double radius,
            const double x[3], double &dist2)
        Given a position x and a radius r, return the id of the point
        closest to the point in that radius. dist2 returns the squared
        distance to the point.
        """
        ret = self._wrap_call(self._vtk_obj.FindClosestPointWithinRadius, *args)
        return ret

    def find_point(self, *args):
        """
        V.find_point(float, float, float) -> int
        C++: IdType FindPoint(double x, double y, double z)
        Find the Id of the point that was previously supplied to
        build_locator_from_points().  Returns -1 if the point was not in the
        original array.
        """
        ret = self._wrap_call(self._vtk_obj.FindPoint, *args)
        return ret

    def find_points_within_radius(self, *args):
        """
        V.find_points_within_radius(float, (float, float, float), IdList)
        C++: void FindPointsWithinRadius(double R, const double x[3],
            IdList *result)
        Find all points within a specified radius R of position x. The
        result is not sorted in any specific manner. These methods are
        thread safe if build_locator() is directly or indirectly called
        from a single thread first.
        """
        my_args = deref_array(args, [('float', ('float', 'float', 'float'), 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.FindPointsWithinRadius, *my_args)
        return ret

    def invalidate_geometry(self):
        """
        V.invalidate_geometry()
        C++: virtual void InvalidateGeometry()
        Forget about the last geometry used.  The next call to
        new_geometry will return 1.  A new k-d tree will be built the next
        time build_locator is called.
        """
        ret = self._vtk_obj.InvalidateGeometry()
        return ret
        

    def new_geometry(self):
        """
        V.new_geometry() -> int
        C++: virtual int NewGeometry()
        Return 1 if the geometry of the input data sets
           has changed since the last time the k-d tree was built.
        """
        ret = self._vtk_obj.NewGeometry()
        return ret
        

    def omit_no_partitioning(self):
        """
        V.omit_no_partitioning()
        C++: void OmitNoPartitioning()
        Partition along all three axes - this is the default
        """
        ret = self._vtk_obj.OmitNoPartitioning()
        return ret
        

    def omit_x_partitioning(self):
        """
        V.omit_x_partitioning()
        C++: void OmitXPartitioning()
        Omit partitions along the X axis, yielding shafts in the X
        direction
        """
        ret = self._vtk_obj.OmitXPartitioning()
        return ret
        

    def omit_xy_partitioning(self):
        """
        V.omit_xy_partitioning()
        C++: void OmitXYPartitioning()
        Omit partitions along the X and Y axes, yielding slabs along Z
        """
        ret = self._vtk_obj.OmitXYPartitioning()
        return ret
        

    def omit_y_partitioning(self):
        """
        V.omit_y_partitioning()
        C++: void OmitYPartitioning()
        Omit partitions along the Y axis, yielding shafts in the Y
        direction
        """
        ret = self._vtk_obj.OmitYPartitioning()
        return ret
        

    def omit_yz_partitioning(self):
        """
        V.omit_yz_partitioning()
        C++: void OmitYZPartitioning()
        Omit partitions along the Y and Z axes, yielding slabs along X
        """
        ret = self._vtk_obj.OmitYZPartitioning()
        return ret
        

    def omit_z_partitioning(self):
        """
        V.omit_z_partitioning()
        C++: void OmitZPartitioning()
        Omit partitions along the Z axis, yielding shafts in the Z
        direction
        """
        ret = self._vtk_obj.OmitZPartitioning()
        return ret
        

    def omit_zx_partitioning(self):
        """
        V.omit_zx_partitioning()
        C++: void OmitZXPartitioning()
        Omit partitions along the Z and X axes, yielding slabs along Y
        """
        ret = self._vtk_obj.OmitZXPartitioning()
        return ret
        

    def print_region(self, *args):
        """
        V.print_region(int)
        C++: void PrintRegion(int id)
        Print out leaf node data for given id
        """
        ret = self._wrap_call(self._vtk_obj.PrintRegion, *args)
        return ret

    def print_tree(self):
        """
        V.print_tree()
        C++: void PrintTree()
        Print out nodes of kd tree
        """
        ret = self._vtk_obj.PrintTree()
        return ret
        

    def print_verbose_tree(self):
        """
        V.print_verbose_tree()
        C++: void PrintVerboseTree()
        Print out nodes of kd tree
        """
        ret = self._vtk_obj.PrintVerboseTree()
        return ret
        

    def remove_all_data_sets(self):
        """
        V.remove_all_data_sets()
        C++: virtual void RemoveAllDataSets()
        Remove the given data set.
        """
        ret = self._vtk_obj.RemoveAllDataSets()
        return ret
        

    def remove_data_set(self, *args):
        """
        V.remove_data_set(int)
        C++: virtual void RemoveDataSet(int index)
        V.remove_data_set(DataSet)
        C++: virtual void RemoveDataSet(DataSet *set)
        Remove the given data set.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveDataSet, *my_args)
        return ret

    def view_order_all_regions_from_position(self, *args):
        """
        V.view_order_all_regions_from_position((float, float, float),
            IntArray) -> int
        C++: int ViewOrderAllRegionsFromPosition(
            const double directionOfProjection[3],
            IntArray *orderedList)
        Given a camera position (typically obtained with
        Camera::GetPosition()), this method, creates a list of the k-d
        tree region IDs in order from front to back with respect to that
        direction.  The number of ordered regions is returned.  Use this
        method to view order regions for cameras that use perspective
        projection.
        """
        my_args = deref_array(args, [(('float', 'float', 'float'), 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.ViewOrderAllRegionsFromPosition, *my_args)
        return ret

    def view_order_all_regions_in_direction(self, *args):
        """
        V.view_order_all_regions_in_direction((float, float, float),
            IntArray) -> int
        C++: int ViewOrderAllRegionsInDirection(
            const double directionOfProjection[3],
            IntArray *orderedList)
        Given a direction of projection (typically obtained with
        Camera::GetDirectionOfProjection()), this method, creates a
        list of the k-d tree region IDs in order from front to back with
        respect to that direction.  The number of ordered regions is
        returned.  Use this method to view order regions for cameras that
        use parallel projection.
        """
        my_args = deref_array(args, [(('float', 'float', 'float'), 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.ViewOrderAllRegionsInDirection, *my_args)
        return ret

    def view_order_regions_from_position(self, *args):
        """
        V.view_order_regions_from_position(IntArray, (float, float, float),
             IntArray) -> int
        C++: int ViewOrderRegionsFromPosition(IntArray *regionIds,
            const double directionOfProjection[3],
            IntArray *orderedList)
        Given a camera position and a list of k-d tree region IDs, this
        method, creates a list of the k-d tree region IDs in order from
        front to back with respect to that direction.  The number of
        ordered regions is returned.  Use this method to view order
        regions for cameras that use perspective projection.
        """
        my_args = deref_array(args, [('vtkIntArray', ('float', 'float', 'float'), 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.ViewOrderRegionsFromPosition, *my_args)
        return ret

    def view_order_regions_in_direction(self, *args):
        """
        V.view_order_regions_in_direction(IntArray, (float, float, float),
            IntArray) -> int
        C++: int ViewOrderRegionsInDirection(IntArray *regionIds,
            const double directionOfProjection[3],
            IntArray *orderedList)
        Given a direction of projection and a list of k-d tree region
        IDs, this method, creates a list of the k-d tree region IDs in
        order from front to back with respect to that direction.  The
        number of ordered regions is returned.  Use this method to view
        order regions for cameras that use parallel projection.
        """
        my_args = deref_array(args, [('vtkIntArray', ('float', 'float', 'float'), 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.ViewOrderRegionsInDirection, *my_args)
        return ret

    _updateable_traits_ = \
    (('fudge_factor', 'GetFudgeFactor'), ('number_of_regions_or_more',
    'GetNumberOfRegionsOrMore'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('max_level', 'GetMaxLevel'),
    ('automatic', 'GetAutomatic'),
    ('generate_representation_using_data_bounds',
    'GetGenerateRepresentationUsingDataBounds'),
    ('include_region_boundary_cells', 'GetIncludeRegionBoundaryCells'),
    ('timing', 'GetTiming'), ('debug', 'GetDebug'), ('reference_count',
    'GetReferenceCount'), ('number_of_regions_or_less',
    'GetNumberOfRegionsOrLess'), ('min_cells', 'GetMinCells'),
    ('tolerance', 'GetTolerance'))
    
    _full_traitnames_list_ = \
    (['automatic', 'debug', 'generate_representation_using_data_bounds',
    'global_warning_display', 'include_region_boundary_cells', 'timing',
    'fudge_factor', 'max_level', 'min_cells', 'number_of_regions_or_less',
    'number_of_regions_or_more', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(KdTree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit KdTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic',
            'generate_representation_using_data_bounds',
            'include_region_boundary_cells', 'timing'], [], ['fudge_factor',
            'max_level', 'min_cells', 'number_of_regions_or_less',
            'number_of_regions_or_more', 'tolerance']),
            title='Edit KdTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit KdTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

