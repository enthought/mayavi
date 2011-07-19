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

from tvtk.tvtk_classes.incremental_point_locator import IncrementalPointLocator


class IncrementalOctreePointLocator(IncrementalPointLocator):
    """
    IncrementalOctreePointLocator - Incremental octree in support
    
    Superclass: IncrementalPointLocator
    
    As opposed to the uniform bin-based search structure (adopted in
    class
     PointLocator) with a fixed spatial resolution, an octree
    mechanism
     employs a hierarchy of tree-like sub-division of the 3d data domain.
    Thus
     it enables data-aware multi-resolution and accordingly accelerated
    point
     location as well as insertion, particularly when handling a
    radically
     imbalanced layout of points as not uncommon in datasets defined on
     adaptive meshes. Compared to a static point locator supporting pure
     location functionalities through some search structure established
    from
     a fixed set of points, an incremental point locator allows for, in
    addition,
     point insertion capabilities, with the search structure maintaining
    a
     dynamically increasing number of points.
     Class IncrementalOctreePointLocator is an octree-based
    accelerated
     implementation of the functionalities of the uniform bin-based
    incremental
     point locator PointLocator. For point location, an octree is
    built by
     accessing a DataSet, specifically a PointSet. For point
    insertion,
     an empty octree is inited and then incrementally populated as points
    are
     inserted. Three increasingly complex point insertion modes, i.e.,
    direct
     check-free insertion, zero tolerance insertion, and non-zero
    tolerance
     insertion, are supported. In fact, the octree used in the point
    location
     mode is actually constructed via direct check-free point insertion.
    This
     class also provides a polygonal representation of the octree
    boundary.
    
    See Also:
    
    
     AbstractPointLocator, IncrementalPointLocator,
    PointLocator,
     MergePoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIncrementalOctreePointLocator, obj, update, **traits)
    
    build_cubic_octree = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether the search octree is built as a cubic shape or
        not.
        """
    )
    def _build_cubic_octree_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBuildCubicOctree,
                        self.build_cubic_octree_)

    max_points_per_leaf = traits.Trait(128, traits.Range(16, 256, enter_set=True, auto_set=False), help=\
        """
        Set/Get the maximum number of points that a leaf node may
        maintain. Note that the actual number of points maintained by a
        leaf node might exceed this threshold if there is a large number
        (equal to or greater than the threshold) of exactly duplicate
        points (with zero distance) to be inserted (e.g., to construct an
        octree for subsequent point location) in extreme cases.
        Respecting this threshold in such scenarios would cause endless
        node sub-division. Thus this threshold is broken, but only in
        case of such situations.
        """
    )
    def _max_points_per_leaf_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxPointsPerLeaf,
                        self.max_points_per_leaf)

    def _get_locator_points(self):
        return wrap_vtk(self._vtk_obj.GetLocatorPoints())
    locator_points = traits.Property(_get_locator_points, help=\
        """
        Get access to the Points object in which point coordinates are
        stored for either point location or point insertion.
        """
    )

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Get the number of points maintained by the octree.
        """
    )

    def find_closest_point_within_squared_radius(self, *args):
        """
        V.find_closest_point_within_squared_radius(float, (float, float, float)
            , float) -> int
        C++: IdType FindClosestPointWithinSquaredRadius(double radius2,
             const double x[3], double &dist2)
        Given a point x and a squared radius radius2, return the id of
        the closest point within the radius and the associated minimum
        squared distance (via dist2, note this returned distance is valid
        only if the point id is not
        -1). build_locator() should have been called prior to this
            function.This method is thread safe if build_locator() is
            directly or indirectly called from a single thread first.
        """
        ret = self._wrap_call(self._vtk_obj.FindClosestPointWithinSquaredRadius, *args)
        return ret

    def find_points_within_squared_radius(self, *args):
        """
        V.find_points_within_squared_radius(float, (float, float, float),
            IdList)
        C++: void FindPointsWithinSquaredRadius(double R2,
            const double x[3], IdList *result)
        Find all points within a squared radius R2 relative to a given
        point x. The returned point ids (stored in result) are not sorted
        in any way. build_locator() should have been called prior to this
        function. This method is thread safe if build_locator() is
        directly or indirectly called from a single thread first.
        """
        my_args = deref_array(args, [('float', ('float', 'float', 'float'), 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.FindPointsWithinSquaredRadius, *my_args)
        return ret

    def insert_point_without_checking(self, *args):
        """
        V.insert_point_without_checking((float, float, float), int, int)
        C++: void InsertPointWithoutChecking(const double point[3],
            IdType &pntId, int insert)
        "Insert" a point to the octree without any checking. Argument
        insert means whether Points::InsertNextPoint() upon 1 is
        called or the point itself is not inserted to the Points at
        all but instead only the point index is inserted to a IdList
        upon 0. For case 0, the point index needs to be specified via
        pnt_id. For case 1, the actual point index is returned via pnt_id.
        init_point_insertion() should have been called.
        """
        ret = self._wrap_call(self._vtk_obj.InsertPointWithoutChecking, *args)
        return ret

    _updateable_traits_ = \
    (('max_points_per_leaf', 'GetMaxPointsPerLeaf'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('max_level',
    'GetMaxLevel'), ('automatic', 'GetAutomatic'), ('debug', 'GetDebug'),
    ('build_cubic_octree', 'GetBuildCubicOctree'), ('reference_count',
    'GetReferenceCount'), ('tolerance', 'GetTolerance'))
    
    _full_traitnames_list_ = \
    (['automatic', 'build_cubic_octree', 'debug',
    'global_warning_display', 'max_level', 'max_points_per_leaf',
    'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IncrementalOctreePointLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit IncrementalOctreePointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic', 'build_cubic_octree'], [], ['max_level',
            'max_points_per_leaf', 'tolerance']),
            title='Edit IncrementalOctreePointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IncrementalOctreePointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

