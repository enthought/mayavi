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

from tvtk.tvtk_classes.object import Object


class PointPlacer(Object):
    """
    PointPlacer - Abstract interface to translate 2d display positions
    to world coordinates
    
    Superclass: Object
    
    Most widgets in VTK have a need to translate of 2d display
    coordinates (as reported by the render_window_interactor) to 3d world
    coordinates. This class is an abstraction of this functionality. A
    few subclasses are listed below:
    
    1) FocalPlanePointPlacer: This class converts 2d display positions
    to world positions such that they lie on the focal plane.
    
    2) PolygonalSurfacePointPlacer: Converts 2d display positions to
    world positions such that they lie on the surface of one or more
    specified polydatas.
    
    3) ImageActorPointPlacer: Converts 2d display positions to world
    positions such that they lie on an image_actor
    
    4) BoundedPlanePointPlacer: Converts 2d display positions to world
    positions such that they lie within a set of specified bounding
    planes.
    
    5) TerrainDataPointPlacer: Converts 2d display positions to world
    positions such that they lie on a height field.
    
    Point placers provide an extensible framework to specify constraints
    on points. The methods compute_world_position, validate_display_position
    and validate_world_position may be overridden to dictate whether a
    world or display position is allowed. These classes are currently
    used by the handle_widget and the contour_widget to allow various
    constraints to be enforced on the placement of their handles.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointPlacer, obj, update, **traits)
    
    pixel_tolerance = traits.Trait(5, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        Set/get the tolerance used when performing computations in
        display coordinates.
        """
    )
    def _pixel_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPixelTolerance,
                        self.pixel_tolerance)

    world_tolerance = traits.Trait(0.001, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/get the tolerance used when performing computations in world
        coordinates.
        """
    )
    def _world_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWorldTolerance,
                        self.world_tolerance)

    def compute_world_position(self, *args):
        """
        V.compute_world_position(Renderer, [float, float], [float, float,
             float], [float, float, float, float, float, float, float,
            float, float]) -> int
        C++: virtual int ComputeWorldPosition(Renderer *ren,
            double displayPos[2], double worldPos[3],
            double worldOrient[9])
        V.compute_world_position(Renderer, [float, float], [float, float,
             float], [float, float, float], [float, float, float, float,
            float, float, float, float, float]) -> int
        C++: virtual int ComputeWorldPosition(Renderer *ren,
            double displayPos[2], double refWorldPos[3],
            double worldPos[3], double worldOrient[9])
        Given a renderer and a display position in pixel coordinates,
        compute the world position and orientation where this point will
        be placed. This method is typically used by the representation to
        place the point initially. A return value of 1 indicates that
        constraints of the placer are met.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeWorldPosition, *my_args)
        return ret

    def update_internal_state(self):
        """
        V.update_internal_state() -> int
        C++: virtual int UpdateInternalState()
        Called by the representation to give the placer a chance to
        update itself.
        """
        ret = self._vtk_obj.UpdateInternalState()
        return ret
        

    def update_world_position(self, *args):
        """
        V.update_world_position(Renderer, [float, float, float], [float,
            float, float, float, float, float, float, float, float])
            -> int
        C++: virtual int UpdateWorldPosition(Renderer *ren,
            double worldPos[3], double worldOrient[9])
        Given a current renderer, world position and orientation, update
        them according to the constraints of the placer. This method is
        typically used when update_contour is called on the
        representation, which must be called after changes are made to
        the constraints in the placer. A return value of 1 indicates that
        the point has been updated. A return value of 0 indicates that
        the point could not be updated and was left alone. By default
        this is a no-op - leaving the point as is.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateWorldPosition, *my_args)
        return ret

    def validate_display_position(self, *args):
        """
        V.validate_display_position(Renderer, [float, float]) -> int
        C++: virtual int ValidateDisplayPosition(Renderer *,
            double displayPos[2])
        Given a display position, check the validity of this position.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ValidateDisplayPosition, *my_args)
        return ret

    def validate_world_position(self, *args):
        """
        V.validate_world_position([float, float, float]) -> int
        C++: virtual int ValidateWorldPosition(double worldPos[3])
        V.validate_world_position([float, float, float], [float, float,
            float, float, float, float, float, float, float]) -> int
        C++: virtual int ValidateWorldPosition(double worldPos[3],
            double worldOrient[9])
        Given a world position check the validity of this position
        according to the constraints of the placer.
        """
        ret = self._wrap_call(self._vtk_obj.ValidateWorldPosition, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('world_tolerance', 'GetWorldTolerance'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('pixel_tolerance', 'GetPixelTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pixel_tolerance',
    'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointPlacer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['pixel_tolerance', 'world_tolerance']),
            title='Edit PointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

