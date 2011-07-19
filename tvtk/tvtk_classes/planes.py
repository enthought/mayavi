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


class Planes(ImplicitFunction):
    """
    Planes - implicit function for convex set of planes
    
    Superclass: ImplicitFunction
    
    Planes computes the implicit function and function gradient for a
    set of planes. The planes must define a convex space.
    
    The function value is the closest first order distance of a point to
    the convex region defined by the planes. The function gradient is the
    plane normal at the function value.  Note that the normals must point
    outside of the convex region. Thus, a negative function value means
    that a point is inside the convex region.
    
    There are several methods to define the set of planes. The most
    general is to supply an instance of Points and an instance of
    DataArray. (The points define a point on the plane, and the
    normals corresponding plane normals.) Two other specialized ways are
    to 1) supply six planes defining the view frustrum of a camera, and
    2) provide a bounding box.
    
    See Also:
    
    Camera
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlanes, obj, update, **traits)
    
    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    def _set_points(self, arg):
        old_val = self._get_points()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetPoints,
                        my_arg[0])
        self.trait_property_changed('points', old_val, arg)
    points = traits.Property(_get_points, _set_points, help=\
        """
        Specify a list of points defining points through which the planes
        pass.
        """
    )

    def _get_normals(self):
        return wrap_vtk(self._vtk_obj.GetNormals())
    def _set_normals(self, arg):
        old_val = self._get_normals()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetNormals,
                        my_arg[0])
        self.trait_property_changed('normals', old_val, arg)
    normals = traits.Property(_get_normals, _set_normals, help=\
        """
        Specify a list of normal vectors for the planes. There is a
        one-to-one correspondence between plane points and plane normals.
        """
    )

    def _get_number_of_planes(self):
        return self._vtk_obj.GetNumberOfPlanes()
    number_of_planes = traits.Property(_get_number_of_planes, help=\
        """
        Return the number of planes in the set of planes.
        """
    )

    def get_plane(self, *args):
        """
        V.get_plane(int) -> Plane
        C++: Plane *GetPlane(int i)
        V.get_plane(int, Plane)
        C++: void GetPlane(int i, Plane *plane)
        Create and return a pointer to a Plane object at the ith
        position. Asking for a plane outside the allowable range returns
        NULL. This method always returns the same object. Use
        get_plane(int i, Plane *plane) instead
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlane, *my_args)
        return wrap_vtk(ret)

    def set_bounds(self, *args):
        """
        V.set_bounds([float, float, float, float, float, float])
        C++: void SetBounds(double bounds[6])
        V.set_bounds(float, float, float, float, float, float)
        C++: void SetBounds(double xmin, double xmax, double ymin,
            double ymax, double zmin, double zmax)
        An alternative method to specify six planes defined by a bounding
        box. The bounding box is a six-vector defined as
        (xmin,xmax,ymin,ymax,zmin,zmax). It defines six planes orthogonal
        to the x-y-z coordinate axes.
        """
        ret = self._wrap_call(self._vtk_obj.SetBounds, *args)
        return ret

    def set_frustum_planes(self, *args):
        """
        V.set_frustum_planes([float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float])
        C++: void SetFrustumPlanes(double planes[24])
        An alternative method to specify six planes defined by the camera
        view frustrum. See Camera::GetFrustumPlanes() documentation.
        """
        ret = self._wrap_call(self._vtk_obj.SetFrustumPlanes, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Planes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Planes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Planes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Planes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

