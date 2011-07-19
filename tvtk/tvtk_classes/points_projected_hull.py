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

from tvtk.tvtk_classes.points import Points


class PointsProjectedHull(Points):
    """
    PointsProjectedHull - the convex hull of the orthogonal 
    
    Superclass: Points
    
    a subclass of Points, it maintains the counter clockwise
       convex hull of the points (projected orthogonally in the
       three coordinate directions) and has a method to
       test for intersection of that hull with an axis aligned
       rectangle.  This is used for intersection tests of 3d volumes.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointsProjectedHull, obj, update, **traits)
    
    def _get_size_ccw_hull_x(self):
        return self._vtk_obj.GetSizeCCWHullX()
    size_ccw_hull_x = traits.Property(_get_size_ccw_hull_x, help=\
        """
        Returns the number of points in the convex hull of the projection
         of the points down the positive x-axis
        """
    )

    def _get_size_ccw_hull_y(self):
        return self._vtk_obj.GetSizeCCWHullY()
    size_ccw_hull_y = traits.Property(_get_size_ccw_hull_y, help=\
        """
        Returns the number of points in the convex hull of the projection
         of the points down the positive y-axis
        """
    )

    def _get_size_ccw_hull_z(self):
        return self._vtk_obj.GetSizeCCWHullZ()
    size_ccw_hull_z = traits.Property(_get_size_ccw_hull_z, help=\
        """
        Returns the number of points in the convex hull of the projection
         of the points down the positive z-axis
        """
    )

    def rectangle_intersection_x(self, *args):
        """
        V.rectangle_intersection_x(Points) -> int
        C++: int RectangleIntersectionX(Points *R)
        V.rectangle_intersection_x(float, float, float, float) -> int
        C++: int RectangleIntersectionX(double ymin, double ymax,
            double zmin, double zmax)
        determine whether the resulting rectangle intersects the
          convex hull of the projection of the points along that axis.
        """
        my_args = deref_array(args, [['vtkPoints'], ('float', 'float', 'float', 'float')])
        ret = self._wrap_call(self._vtk_obj.RectangleIntersectionX, *my_args)
        return ret

    def rectangle_intersection_y(self, *args):
        """
        V.rectangle_intersection_y(Points) -> int
        C++: int RectangleIntersectionY(Points *R)
        V.rectangle_intersection_y(float, float, float, float) -> int
        C++: int RectangleIntersectionY(double zmin, double zmax,
            double xmin, double xmax)
        of the parallel projection along the Y axis of the points
        """
        my_args = deref_array(args, [['vtkPoints'], ('float', 'float', 'float', 'float')])
        ret = self._wrap_call(self._vtk_obj.RectangleIntersectionY, *my_args)
        return ret

    def rectangle_intersection_z(self, *args):
        """
        V.rectangle_intersection_z(Points) -> int
        C++: int RectangleIntersectionZ(Points *R)
        V.rectangle_intersection_z(float, float, float, float) -> int
        C++: int RectangleIntersectionZ(double xmin, double xmax,
            double ymin, double ymax)
        of the parallel projection along the Z axis of the points
        """
        my_args = deref_array(args, [['vtkPoints'], ('float', 'float', 'float', 'float')])
        ret = self._wrap_call(self._vtk_obj.RectangleIntersectionZ, *my_args)
        return ret

    def update(self):
        """
        V.update()
        C++: void Update()
        Forces recalculation of convex hulls, use this if
          you delete/add points
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('number_of_points',
    'GetNumberOfPoints'), ('data_type', 'GetDataType'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'data_type', 'number_of_points'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointsProjectedHull, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PointsProjectedHull properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['data_type'], ['number_of_points']),
            title='Edit PointsProjectedHull properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointsProjectedHull properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

