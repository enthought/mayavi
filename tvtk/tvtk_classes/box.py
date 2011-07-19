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

from tvtk.tvtk_classes.implicit_function import ImplicitFunction


class Box(ImplicitFunction):
    """
    Box - implicit function for a bounding box
    
    Superclass: ImplicitFunction
    
    Box computes the implicit function and/or gradient for a
    axis-aligned bounding box. (The superclasses transform can be used to
    modify this orientation.) Each side of the box is orthogonal to all
    other sides meeting along shared edges and all faces are orthogonal
    to the x-y-z coordinate axes.  (If you wish to orient this box
    differently, recall that the superclass ImplicitFunction supports
    a transformation matrix.) Cube is a concrete implementation of
    ImplicitFunction.
    
    See Also:
    
    CubeSource ImplicitFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBox, obj, update, **traits)
    
    def get_x_min(self, *args):
        """
        V.get_x_min([float, float, float])
        C++: void GetXMin(double p[3])
        V.get_x_min(float, float, float)
        C++: void GetXMin(double &x, double &y, double &z)
        Set / get the bounding box using various methods.
        """
        ret = self._wrap_call(self._vtk_obj.GetXMin, *args)
        return ret

    def set_x_min(self, *args):
        """
        V.set_x_min([float, float, float])
        C++: void SetXMin(double p[3])
        V.set_x_min(float, float, float)
        C++: void SetXMin(double x, double y, double z)
        Set / get the bounding box using various methods.
        """
        ret = self._wrap_call(self._vtk_obj.SetXMin, *args)
        return ret

    def get_bounds(self, *args):
        """
        V.get_bounds(float, float, float, float, float, float)
        C++: void GetBounds(double &xMin, double &xMax, double &yMin,
            double &yMax, double &zMin, double &zMax)
        V.get_bounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6])"""
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def set_bounds(self, *args):
        """
        V.set_bounds(float, float, float, float, float, float)
        C++: void SetBounds(double xMin, double xMax, double yMin,
            double yMax, double zMin, double zMax)
        V.set_bounds([float, float, float, float, float, float])
        C++: void SetBounds(double bounds[6])"""
        ret = self._wrap_call(self._vtk_obj.SetBounds, *args)
        return ret

    def get_x_max(self, *args):
        """
        V.get_x_max([float, float, float])
        C++: void GetXMax(double p[3])
        V.get_x_max(float, float, float)
        C++: void GetXMax(double &x, double &y, double &z)"""
        ret = self._wrap_call(self._vtk_obj.GetXMax, *args)
        return ret

    def set_x_max(self, *args):
        """
        V.set_x_max([float, float, float])
        C++: void SetXMax(double p[3])
        V.set_x_max(float, float, float)
        C++: void SetXMax(double x, double y, double z)"""
        ret = self._wrap_call(self._vtk_obj.SetXMax, *args)
        return ret

    def add_bounds(self, *args):
        """
        V.add_bounds([float, float, float, float, float, float])
        C++: void AddBounds(double bounds[6])
        A special method that allows union set operation on bounding
        boxes. Start with a set_bounds(). Subsequent add_bounds() methods
        are union set operations on the original bounds. Retrieve the
        final bounds with a get_bounds() method.
        """
        ret = self._wrap_call(self._vtk_obj.AddBounds, *args)
        return ret

    def intersect_box(self, *args):
        """
        V.intersect_box([float, float, float, float, float, float], [float,
             float, float], [float, float, float], [float, float, float],
            float) -> char
        C++: static char IntersectBox(double bounds[6], double origin[3],
            double dir[3], double coord[3], double &t)
        Bounding box intersection modified from Graphics Gems Vol I. The
        method returns a non-zero value if the bounding box is hit.
        Origin[3] starts the ray, dir[3] is the vector components of the
        ray in the x-y-z directions, coord[3] is the location of hit, and
        t is the parametric coordinate along line. (Notes: the
        intersection ray dir[3] is NOT normalized.  Valid intersections
        will only occur between 0<=t<=1.)
        """
        ret = self._wrap_call(self._vtk_obj.IntersectBox, *args)
        return ret

    def intersect_with_line(self, *args):
        """
        V.intersect_with_line((float, float, float, float, float, float), (
            float, float, float), (float, float, float), float, float,
            [float, float, float], [float, float, float], int, int) -> int
        C++: static int IntersectWithLine(const double bounds[6],
            const double p1[3], const double p2[3], double &t1,
            double &t2, double x1[3], double x2[3], int &plane1,
            int &plane2)
        Intersect a line with the box.  Give the endpoints of the line in
        p1 and p2.  The parameteric distances from p1 to the entry and
        exit points are returned in t1 and t2, where t1 and t2 are
        clamped to the range [0,1].  The entry and exit planes are
        returned in plane1 and plane2 where integers (0, 1, 2, 3, 4, 5)
        stand for the (xmin, xmax, ymin, ymax, zmin, zmax) planes
        respectively, and a value of -1 means that no intersection
        occurred.  The actual intersection coordinates are stored in x1
        and x2, which can be set to NULL of you do not need them to be
        returned.  The function return value will be zero if the line is
        wholly outside of the box.
        """
        ret = self._wrap_call(self._vtk_obj.IntersectWithLine, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Box, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Box properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Box properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Box properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

