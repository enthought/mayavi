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


class ClosedSurfacePointPlacer(PointPlacer):
    """
    ClosedSurfacePointPlacer - point_placer to constrain validity
    within a set of convex planes
    
    Superclass: PointPlacer
    
    This placer takes a set of boudning planes and constraints the
    validity within the supplied convex planes. It is used by the
    parallelop_piped_representation to place constraints on the motion the
    handles within the parallelopiped.
    
    See Also:
    
    ParallelopipedRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkClosedSurfacePointPlacer, obj, update, **traits)
    
    minimum_distance = traits.Trait(0.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _minimum_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumDistance,
                        self.minimum_distance)

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

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('minimum_distance', 'GetMinimumDistance'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pixel_tolerance', 'GetPixelTolerance'), ('reference_count',
    'GetReferenceCount'), ('world_tolerance', 'GetWorldTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'minimum_distance',
    'pixel_tolerance', 'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ClosedSurfacePointPlacer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ClosedSurfacePointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['minimum_distance', 'pixel_tolerance',
            'world_tolerance']),
            title='Edit ClosedSurfacePointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ClosedSurfacePointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

