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

from tvtk.tvtk_classes.angle_representation import AngleRepresentation


class AngleRepresentation3D(AngleRepresentation):
    """
    AngleRepresentation3D - represent the AngleWidget
    
    Superclass: AngleRepresentation
    
    The AngleRepresentation3D is a representation for the
    AngleWidget. This representation consists of two rays and three
    HandleRepresentations to place and manipulate the three points
    defining the angle representation. (Note: the three points are
    referred to as Point1, Center, and Point2, at the two end points
    (Point1 and Point2) and Center (around which the angle is measured).
    This particular implementation is a 3d representation, meaning that
    it draws in the overlay plane.
    
    See Also:
    
    AngleWidget HandleRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAngleRepresentation3D, obj, update, **traits)
    
    def get_point1_world_position(self, *args):
        """
        V.get_point1_world_position([float, float, float])
        C++: virtual void GetPoint1WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1WorldPosition, *args)
        return ret

    def set_point1_world_position(self, *args):
        """
        V.set_point1_world_position([float, float, float])
        C++: virtual void SetPoint1WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1WorldPosition, *args)
        return ret

    def get_center_world_position(self, *args):
        """
        V.get_center_world_position([float, float, float])
        C++: virtual void GetCenterWorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetCenterWorldPosition, *args)
        return ret

    def set_center_world_position(self, *args):
        """
        V.set_center_world_position([float, float, float])
        C++: virtual void SetCenterWorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetCenterWorldPosition, *args)
        return ret

    def get_point1display_position(self, *args):
        """
        V.get_point1display_position([float, float, float])
        C++: virtual void GetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1DisplayPosition, *args)
        return ret

    def set_point1display_position(self, *args):
        """
        V.set_point1display_position([float, float, float])
        C++: virtual void SetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1DisplayPosition, *args)
        return ret

    def get_center_display_position(self, *args):
        """
        V.get_center_display_position([float, float, float])
        C++: virtual void GetCenterDisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetCenterDisplayPosition, *args)
        return ret

    def set_center_display_position(self, *args):
        """
        V.set_center_display_position([float, float, float])
        C++: virtual void SetCenterDisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetCenterDisplayPosition, *args)
        return ret

    def get_point2display_position(self, *args):
        """
        V.get_point2display_position([float, float, float])
        C++: virtual void GetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2DisplayPosition, *args)
        return ret

    def set_point2display_position(self, *args):
        """
        V.set_point2display_position([float, float, float])
        C++: virtual void SetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2DisplayPosition, *args)
        return ret

    def get_point2_world_position(self, *args):
        """
        V.get_point2_world_position([float, float, float])
        C++: virtual void GetPoint2WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2WorldPosition, *args)
        return ret

    def set_point2_world_position(self, *args):
        """
        V.set_point2_world_position([float, float, float])
        C++: virtual void SetPoint2WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2WorldPosition, *args)
        return ret

    def _get_arc(self):
        return wrap_vtk(self._vtk_obj.GetArc())
    arc = traits.Property(_get_arc, help=\
        """
        Set/Get the three leaders used to create this representation. By
        obtaining these leaders the user can set the appropriate
        properties, etc.
        """
    )

    def _get_ray1(self):
        return wrap_vtk(self._vtk_obj.GetRay1())
    ray1 = traits.Property(_get_ray1, help=\
        """
        Set/Get the three leaders used to create this representation. By
        obtaining these leaders the user can set the appropriate
        properties, etc.
        """
    )

    def _get_ray2(self):
        return wrap_vtk(self._vtk_obj.GetRay2())
    ray2 = traits.Property(_get_ray2, help=\
        """
        Set/Get the three leaders used to create this representation. By
        obtaining these leaders the user can set the appropriate
        properties, etc.
        """
    )

    def _get_text_actor(self):
        return wrap_vtk(self._vtk_obj.GetTextActor())
    text_actor = traits.Property(_get_text_actor, help=\
        """
        Set/Get the three leaders used to create this representation. By
        obtaining these leaders the user can set the appropriate
        properties, etc.
        """
    )

    def set_text_actor_scale(self, *args):
        """
        V.set_text_actor_scale([float, float, float])
        C++: virtual void SetTextActorScale(double scale[3])
        Scale text.
        """
        ret = self._wrap_call(self._vtk_obj.SetTextActorScale, *args)
        return ret

    _updateable_traits_ = \
    (('ray2_visibility', 'GetRay2Visibility'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('handle_size', 'GetHandleSize'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('arc_visibility', 'GetArcVisibility'), ('label_format',
    'GetLabelFormat'), ('need_to_render', 'GetNeedToRender'), ('dragable',
    'GetDragable'), ('visibility', 'GetVisibility'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('pickable',
    'GetPickable'), ('reference_count', 'GetReferenceCount'),
    ('place_factor', 'GetPlaceFactor'), ('ray1_visibility',
    'GetRay1Visibility'), ('tolerance', 'GetTolerance'), ('use_bounds',
    'GetUseBounds'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['arc_visibility', 'debug', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'ray1_visibility', 'ray2_visibility',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'label_format',
    'place_factor', 'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AngleRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AngleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['arc_visibility', 'need_to_render', 'ray1_visibility',
            'ray2_visibility', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'label_format', 'place_factor', 'render_time_multiplier',
            'tolerance']),
            title='Edit AngleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AngleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

