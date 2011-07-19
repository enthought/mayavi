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

from tvtk.tvtk_classes.cell import Cell


class Polygon(Cell):
    """
    Polygon - a cell that represents an n-sided polygon
    
    Superclass: Cell
    
    Polygon is a concrete implementation of Cell to represent a 2d
    n-sided polygon. The polygons cannot have any internal holes, and
    cannot self-intersect. Define the polygon with n-points ordered in
    the counter- clockwise direction; do not repeat the last point.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolygon, obj, update, **traits)
    
    use_mvc_interpolation = traits.Bool(False, help=\
        """
        Set/Get the flag indicating whether to use Mean Value Coordinate
        for the interpolation. If true, interpolate_functions() uses the
        Mean Value Coordinate to compute weights. Otherwise, the
        conventional 1/r^2 method is used. The use_mvc_interpolation
        parameter is set to false by default.
        """
    )
    def _use_mvc_interpolation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseMVCInterpolation,
                        self.use_mvc_interpolation)

    def compute_area(self):
        """
        V.compute_area() -> float
        C++: double ComputeArea()
        Compute the area of a polygon. This is a convenience function
        which simply calls static double compute_area(vtk_points *p,
        IdType num_pts, IdType *pts, double normal[3]); with the
        appropriate parameters from the instantiated Polygon.
        """
        ret = self._vtk_obj.ComputeArea()
        return ret
        

    def compute_centroid(self, *args):
        """
        V.compute_centroid(IdTypeArray, Points, [float, float,
            float])
        C++: static void ComputeCentroid(IdTypeArray *ids,
            Points *pts, double centroid[3])
        Compute the centroid of a set of points.
        """
        my_args = deref_array(args, [('vtkIdTypeArray', 'vtkPoints', ['float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.ComputeCentroid, *my_args)
        return ret

    def compute_normal(self, *args):
        """
        V.compute_normal(Points, [float, float, float])
        C++: static void ComputeNormal(Points *p, double n[3])
        V.compute_normal(IdTypeArray, Points, [float, float, float])
        C++: static void ComputeNormal(IdTypeArray *ids,
            Points *pts, double n[3])
        Polygon specific methods.
        """
        my_args = deref_array(args, [('vtkPoints', ['float', 'float', 'float']), ('vtkIdTypeArray', 'vtkPoints', ['float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.ComputeNormal, *my_args)
        return ret

    def intersect_convex2d_cells(self, *args):
        """
        V.intersect_convex2d_cells(Cell, Cell, float, [float, float,
            float], [float, float, float]) -> int
        C++: static int IntersectConvex2DCells(Cell *cell1,
            Cell *cell2, double tol, double p0[3], double p1[3])
        Intersect two convex 2d polygons to produce a line segment as
        output. The return status of the methods indicated no
        intersection (returns 0); a single point of intersection (returns
        1); or a line segment (i.e., two points of intersection, returns
        2). The points of intersection are returned in the arrays p0 and
        p1.  If less than two points of intersection are generated then
        p1 and/or p0 may be indeterminiate. Finally, if the two convex
        polygons are parallel, then "0" is returned (i.e., no
        intersection) even if the triangles lie on one another.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IntersectConvex2DCells, *my_args)
        return ret

    def non_degenerate_triangulate(self, *args):
        """
        V.non_degenerate_triangulate(IdList) -> int
        C++: int NonDegenerateTriangulate(IdList *outTris)
        Same as triangulate(vtk_id_list *out_tris) but with a first pass to
        split the polygon into non-degenerate polygons.
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.NonDegenerateTriangulate, *my_args)
        return ret

    def parameterize_polygon(self, *args):
        """
        V.parameterize_polygon([float, float, float], [float, float,
            float], float, [float, float, float], float, [float, float,
            float]) -> int
        C++: int ParameterizePolygon(double p0[3], double p10[3],
            double &l10, double p20[3], double &l20, double n[3])
        Create a local s-t coordinate system for a polygon. The point p0
        is the origin of the local system, p10 is s-axis vector, and p20
        is the t-axis vector. (These are expressed in the modeling
        coordinate system and are vectors of dimension [3].) The values
        l20 and l20 are the lengths of the vectors p10 and p20, and n is
        the polygon normal.
        """
        ret = self._wrap_call(self._vtk_obj.ParameterizePolygon, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('use_mvc_interpolation', 'GetUseMVCInterpolation'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'use_mvc_interpolation'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Polygon, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Polygon properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['use_mvc_interpolation']),
            title='Edit Polygon properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Polygon properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

