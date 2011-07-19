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

from tvtk.tvtk_classes.abstract_point_locator import AbstractPointLocator


class IncrementalPointLocator(AbstractPointLocator):
    """
    IncrementalPointLocator - Abstract class in support of both
    
    Superclass: AbstractPointLocator
    
    Compared to a static point locator for pure location functionalities
     through some search structure established from a fixed set of
    points,
     an incremental point locator allows for, in addition, point
    insertion
     capabilities, with the search structure maintaining a dynamically
     increasing number of points. There are two incremental point
    locators,
     i.e., PointLocator and IncrementalOctreePointLocator. As
    opposed
     to the uniform bin-based search structure (adopted in
    PointLocator)
     with a fixed spatial resolution, an octree mechanism (employed in
     IncrementalOctreePointlocator) resorts to a hierarchy of
    tree-like
     sub-division of the 3d data domain. Thus it enables data-aware
    multi-
     resolution and accordingly accelerated point location as well as
    point
     insertion, particularly when handling a radically imbalanced layout
    of
     points as not uncommon in datasets defined on adaptive meshes. In
    other
     words, IncrementalOctreePointLocator is an octree-based
    accelerated
     implementation of all functionalities of PointLocator.
    
    See Also:
    
    
     Locator, IncrementalOctreePointLocator, PointLocator,
     MergePoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIncrementalPointLocator, obj, update, **traits)
    
    def find_closest_inserted_point(self, *args):
        """
        V.find_closest_inserted_point((float, float, float)) -> int
        C++: virtual IdType FindClosestInsertedPoint(const double x[3])
        Given a point x assumed to be covered by the search structure,
        return the index of the closest point (already inserted to the
        search structure) regardless of the associated minimum squared
        distance relative to the squared insertion-tolerance distance.
        This method is used when performing incremental point insertion.
        Note -1 indicates that no point is found. init_point_insertion()
        should have been called in advance.
        """
        ret = self._wrap_call(self._vtk_obj.FindClosestInsertedPoint, *args)
        return ret

    def init_point_insertion(self, *args):
        """
        V.init_point_insertion(Points, (float, float, float, float,
            float, float)) -> int
        C++: virtual int InitPointInsertion(Points *newPts,
            const double bounds[6])
        V.init_point_insertion(Points, (float, float, float, float,
            float, float), int) -> int
        C++: virtual int InitPointInsertion(Points *newPts,
            const double bounds[6], IdType estSize)
        Initialize the point insertion process. new_pts is an object,
        storing 3d point coordinates, to which incremental point
        insertion puts coordinates. It is created and provided by an
        external VTK class. Argument bounds represents the spatial
        bounding box, into which the points fall.
        """
        my_args = deref_array(args, [('vtkPoints', ('float', 'float', 'float', 'float', 'float', 'float')), ('vtkPoints', ('float', 'float', 'float', 'float', 'float', 'float'), 'int')])
        ret = self._wrap_call(self._vtk_obj.InitPointInsertion, *my_args)
        return ret

    def insert_next_point(self, *args):
        """
        V.insert_next_point((float, float, float)) -> int
        C++: virtual IdType InsertNextPoint(const double x[3])
        Insert a given point and return the point index.
        init_point_insertion() should have been called prior to this
        function. Also, is_inserted_point() should have been called in
        advance to ensure that the given point has not been inserted
        unless point duplication is allowed.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextPoint, *args)
        return ret

    def insert_point(self, *args):
        """
        V.insert_point(int, (float, float, float))
        C++: virtual void InsertPoint(IdType ptId, const double x[3])
        Insert a given point with a specified point index pt_id.
        init_point_insertion() should have been called prior to this
        function. Also, is_inserted_point() should have been called in
        advance to ensure that the given point has not been inserted
        unless point duplication is allowed.
        """
        ret = self._wrap_call(self._vtk_obj.InsertPoint, *args)
        return ret

    def insert_unique_point(self, *args):
        """
        V.insert_unique_point((float, float, float), int) -> int
        C++: virtual int InsertUniquePoint(const double x[3],
            IdType &ptId)
        Insert a point unless there has been a duplciate in the search
        structure. This method is not thread safe.
        """
        ret = self._wrap_call(self._vtk_obj.InsertUniquePoint, *args)
        return ret

    def is_inserted_point(self, *args):
        """
        V.is_inserted_point(float, float, float) -> int
        C++: virtual IdType IsInsertedPoint(double x, double y,
            double z)
        V.is_inserted_point((float, float, float)) -> int
        C++: virtual IdType IsInsertedPoint(const double x[3])
        Determine whether or not a given point has been inserted. Return
        the id of the already inserted point if true, else return -1.
        init_point_insertion() should have been called in advance.
        """
        ret = self._wrap_call(self._vtk_obj.IsInsertedPoint, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('max_level', 'GetMaxLevel'), ('debug',
    'GetDebug'), ('tolerance', 'GetTolerance'), ('automatic',
    'GetAutomatic'))
    
    _full_traitnames_list_ = \
    (['automatic', 'debug', 'global_warning_display', 'max_level',
    'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IncrementalPointLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit IncrementalPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic'], [], ['max_level', 'tolerance']),
            title='Edit IncrementalPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IncrementalPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

