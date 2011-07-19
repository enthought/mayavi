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


class Plane(ImplicitFunction):
    """
    Plane - perform various plane computations
    
    Superclass: ImplicitFunction
    
    Plane provides methods for various plane computations. These
    include projecting points onto a plane, evaluating the plane
    equation, and returning plane normal. Plane is a concrete
    implementation of the abstract class ImplicitFunction.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlane, obj, update, **traits)
    
    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    normal = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    def distance_to_plane(self, *args):
        """
        V.distance_to_plane([float, float, float], [float, float, float],
            [float, float, float]) -> float
        C++: static double DistanceToPlane(double x[3], double n[3],
            double p0[3])
        V.distance_to_plane([float, float, float]) -> float
        C++: double DistanceToPlane(double x[3])
        Return the distance of a point x to a plane defined by n(x-p0) =
        0. The normal n[3] must be magnitude=1.
        """
        ret = self._wrap_call(self._vtk_obj.DistanceToPlane, *args)
        return ret

    def evaluate(self, *args):
        """
        V.evaluate([float, float, float], [float, float, float], [float,
            float, float]) -> float
        C++: static double Evaluate(double normal[3], double origin[3],
            double x[3])
        Quick evaluation of plane equation n(x-origin)=0.
        """
        ret = self._wrap_call(self._vtk_obj.Evaluate, *args)
        return ret

    def generalized_project_point(self, *args):
        """
        V.generalized_project_point([float, float, float], [float, float,
            float], [float, float, float], [float, float, float])
        C++: static void GeneralizedProjectPoint(double x[3],
            double origin[3], double normal[3], double xproj[3])
        V.generalized_project_point([float, float, float], [float, float,
            float])
        C++: void GeneralizedProjectPoint(double x[3], double xproj[3])"""
        ret = self._wrap_call(self._vtk_obj.GeneralizedProjectPoint, *args)
        return ret

    def intersect_with_line(self, *args):
        """
        V.intersect_with_line([float, float, float], [float, float, float],
            [float, float, float], [float, float, float], float, [float,
            float, float]) -> int
        C++: static int IntersectWithLine(double p1[3], double p2[3],
            double n[3], double p0[3], double &t, double x[3])
        V.intersect_with_line([float, float, float], [float, float, float],
            float, [float, float, float]) -> int
        C++: int IntersectWithLine(double p1[3], double p2[3], double &t,
            double x[3])
        Given a line defined by the two points p1,p2; and a plane defined
        by the normal n and point p0, compute an intersection. The
        parametric coordinate along the line is returned in t, and the
        coordinates of intersection are returned in x. A zero is returned
        if the plane and line do not intersect between (0<=t<=1). If the
        plane and line are parallel, zero is returned and t is set to
        VTK_LARGE_DOUBLE.
        """
        ret = self._wrap_call(self._vtk_obj.IntersectWithLine, *args)
        return ret

    def project_point(self, *args):
        """
        V.project_point([float, float, float], [float, float, float],
            [float, float, float], [float, float, float])
        C++: static void ProjectPoint(double x[3], double origin[3],
            double normal[3], double xproj[3])
        V.project_point([float, float, float], [float, float, float])
        C++: void ProjectPoint(double x[3], double xproj[3])"""
        ret = self._wrap_call(self._vtk_obj.ProjectPoint, *args)
        return ret

    def push(self, *args):
        """
        V.push(float)
        C++: void Push(double distance)
        Translate the plane in the direction of the normal by the
        distance specified.  Negative values move the plane in the
        opposite direction.
        """
        ret = self._wrap_call(self._vtk_obj.Push, *args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('reference_count', 'GetReferenceCount'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('normal', 'GetNormal'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'normal', 'origin'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Plane, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Plane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['normal', 'origin']),
            title='Edit Plane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Plane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

