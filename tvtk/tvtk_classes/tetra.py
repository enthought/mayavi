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

from tvtk.tvtk_classes.cell3d import Cell3D


class Tetra(Cell3D):
    """
    Tetra - a 3d cell that represents a tetrahedron
    
    Superclass: Cell3D
    
    Tetra is a concrete implementation of Cell to represent a 3d
    tetrahedron. Tetra uses the standard isoparametric shape functions
    for a linear tetrahedron. The tetrahedron is defined by the four
    points (0-3); where (0,1,2) is the base of the tetrahedron which,
    using the right hand rule, forms a triangle whose normal points in
    the direction of the fourth point.
    
    See Also:
    
    ConvexPointSet Hexahedron Pyramid Voxel Wedge
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTetra, obj, update, **traits)
    
    def get_edge_array(self, *args):
        """
        V.get_edge_array(int) -> (int, int)
        C++: static int *GetEdgeArray(int edgeId)
        Return the ids of the vertices defining edge/face
        (`edge_id`/`face_id'). Ids are related to the cell, not to the
        dataset.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdgeArray, *args)
        return ret

    def get_face_array(self, *args):
        """
        V.get_face_array(int) -> (int, int, int)
        C++: static int *GetFaceArray(int faceId)
        Return the ids of the vertices defining edge/face
        (`edge_id`/`face_id'). Ids are related to the cell, not to the
        dataset.
        """
        ret = self._wrap_call(self._vtk_obj.GetFaceArray, *args)
        return ret

    def barycentric_coords(self, *args):
        """
        V.barycentric_coords([float, float, float], [float, float, float],
            [float, float, float], [float, float, float], [float, float,
            float], [float, float, float, float]) -> int
        C++: static int BarycentricCoords(double x[3], double x1[3],
            double x2[3], double x3[3], double x4[3], double bcoords[4])
        Given a 3d point x[3], determine the barycentric coordinates of
        the point. Barycentric coordinates are a natural coordinate
        system for simplices that express a position as a linear
        combination of the vertices. For a tetrahedron, there are four
        barycentric coordinates (because there are four vertices), and
        the sum of the coordinates must equal 1. If a point x is inside a
        simplex, then all four coordinates will be strictly positive.  If
        three coordinates are zero (so the fourth =1), then the point x
        is on a vertex. If two coordinates are zero, the point x is on an
        edge (and so on). In this method, you must specify the vertex
        coordinates x1->x4. Returns 0 if tetrahedron is degenerate.
        """
        ret = self._wrap_call(self._vtk_obj.BarycentricCoords, *args)
        return ret

    def circumsphere(self, *args):
        """
        V.circumsphere([float, float, float], [float, float, float],
            [float, float, float], [float, float, float], [float, float,
            float]) -> float
        C++: static double Circumsphere(double p1[3], double p2[3],
            double p3[3], double p4[3], double center[3])
        Compute the circumcenter (center[3]) and radius squared (method
        return value) of a tetrahedron defined by the four points x1, x2,
        x3, and x4.
        """
        ret = self._wrap_call(self._vtk_obj.Circumsphere, *args)
        return ret

    def compute_volume(self, *args):
        """
        V.compute_volume([float, float, float], [float, float, float],
            [float, float, float], [float, float, float]) -> float
        C++: static double ComputeVolume(double p1[3], double p2[3],
            double p3[3], double p4[3])
        Compute the volume of a tetrahedron defined by the four points
        p1, p2, p3, and p4.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeVolume, *args)
        return ret

    def insphere(self, *args):
        """
        V.insphere([float, float, float], [float, float, float], [float,
            float, float], [float, float, float], [float, float, float])
            -> float
        C++: static double Insphere(double p1[3], double p2[3],
            double p3[3], double p4[3], double center[3])
        Compute the center (center[3]) and radius (method return value)
        of a sphere that just fits inside the faces of a tetrahedron
        defined by the four points x1, x2, x3, and x4.
        """
        ret = self._wrap_call(self._vtk_obj.Insphere, *args)
        return ret

    def interpolation_derivs(self, *args):
        """
        V.interpolation_derivs([float, float, float], [float, float, float,
             float, float, float, float, float, float, float, float,
            float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[12])
        @deprecated Replaced by Tetra::InterpolateDerivs as of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[4])
        @deprecated Replaced by Tetra::InterpolateFunctions as of VTK
        5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationFunctions, *args)
        return ret

    def tetra_center(self, *args):
        """
        V.tetra_center([float, float, float], [float, float, float],
            [float, float, float], [float, float, float], [float, float,
            float])
        C++: static void TetraCenter(double p1[3], double p2[3],
            double p3[3], double p4[3], double center[3])
        Compute the center of the tetrahedron,
        """
        ret = self._wrap_call(self._vtk_obj.TetraCenter, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('merge_tolerance', 'GetMergeTolerance'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'merge_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Tetra, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Tetra properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['merge_tolerance']),
            title='Edit Tetra properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Tetra properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

