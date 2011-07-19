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

from tvtk.tvtk_classes.point_placer import PointPlacer


class BoundedPlanePointPlacer(PointPlacer):
    """
    BoundedPlanePointPlacer - a placer that constrains a handle to a
    finite plane
    
    Superclass: PointPlacer
    
    BoundedPlanePointPlacer is a type of point placer that constrains
    its points to a finite (i.e., bounded) plance.
    
    See Also:
    
    PointPlacer HandleWidget HandleRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBoundedPlanePointPlacer, obj, update, **traits)
    
    projection_normal = traits.Trait('z_axis',
    tvtk_base.TraitRevPrefixMap({'y_axis': 1, 'oblique': 3, 'z_axis': 2, 'x_axis': 0}), help=\
        """
        Set the projection normal to lie along the x, y, or z axis, or to
        be oblique. If it is oblique, then the plane is defined in the
        oblique_plane ivar.
        """
    )
    def _projection_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionNormal,
                        self.projection_normal_)

    projection_position = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The position of the bounding plane from the origin along the
        normal. The origin and normal are defined in the oblique plane
        when the projection_normal is oblique. For the X, Y, and Z axes
        projection normals, the normal is the axis direction, and the
        origin is (0,0,0).
        """
    )
    def _projection_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionPosition,
                        self.projection_position)

    def _get_bounding_planes(self):
        return wrap_vtk(self._vtk_obj.GetBoundingPlanes())
    def _set_bounding_planes(self, arg):
        old_val = self._get_bounding_planes()
        self._wrap_call(self._vtk_obj.SetBoundingPlanes,
                        deref_vtk(arg))
        self.trait_property_changed('bounding_planes', old_val, arg)
    bounding_planes = traits.Property(_get_bounding_planes, _set_bounding_planes, help=\
        """
        A collection of plane equations used to bound the position of the
        point. This is in addition to confining the point to a plane -
        these contraints are meant to, for example, keep a point within
        the extent of an image. Using a set of plane equations allows for
        more complex bounds (such as bounding a point to an oblique
        reliced image that has hexagonal shape) than a simple extent.
        """
    )

    def add_bounding_plane(self, *args):
        """
        V.add_bounding_plane(Plane)
        C++: void AddBoundingPlane(Plane *plane)
        A collection of plane equations used to bound the position of the
        point. This is in addition to confining the point to a plane -
        these contraints are meant to, for example, keep a point within
        the extent of an image. Using a set of plane equations allows for
        more complex bounds (such as bounding a point to an oblique
        reliced image that has hexagonal shape) than a simple extent.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddBoundingPlane, *my_args)
        return ret

    def remove_all_bounding_planes(self):
        """
        V.remove_all_bounding_planes()
        C++: void RemoveAllBoundingPlanes()
        A collection of plane equations used to bound the position of the
        point. This is in addition to confining the point to a plane -
        these contraints are meant to, for example, keep a point within
        the extent of an image. Using a set of plane equations allows for
        more complex bounds (such as bounding a point to an oblique
        reliced image that has hexagonal shape) than a simple extent.
        """
        ret = self._vtk_obj.RemoveAllBoundingPlanes()
        return ret
        

    def remove_bounding_plane(self, *args):
        """
        V.remove_bounding_plane(Plane)
        C++: void RemoveBoundingPlane(Plane *plane)
        A collection of plane equations used to bound the position of the
        point. This is in addition to confining the point to a plane -
        these contraints are meant to, for example, keep a point within
        the extent of an image. Using a set of plane equations allows for
        more complex bounds (such as bounding a point to an oblique
        reliced image that has hexagonal shape) than a simple extent.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveBoundingPlane, *my_args)
        return ret

    def set_oblique_plane(self, *args):
        """
        V.set_oblique_plane(Plane)
        C++: void SetObliquePlane(Plane *)
        If the projection_normal is set to Oblique, then this is the
        oblique plane used to constrain the handle position.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetObliquePlane, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('projection_normal',
    'GetProjectionNormal'), ('pixel_tolerance', 'GetPixelTolerance'),
    ('projection_position', 'GetProjectionPosition'), ('debug',
    'GetDebug'), ('world_tolerance', 'GetWorldTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'projection_normal',
    'pixel_tolerance', 'projection_position', 'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BoundedPlanePointPlacer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BoundedPlanePointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['projection_normal'], ['pixel_tolerance',
            'projection_position', 'world_tolerance']),
            title='Edit BoundedPlanePointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BoundedPlanePointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

