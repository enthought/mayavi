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

from tvtk.tvtk_classes.handle_representation import HandleRepresentation


class ConstrainedPointHandleRepresentation(HandleRepresentation):
    """
    ConstrainedPointHandleRepresentation - point representation
    constrained to a 2d plane
    
    Superclass: HandleRepresentation
    
    This class is used to represent a HandleWidget. It represents a
    position in 3d world coordinates that is constrained to a specified
    plane. The default look is to draw a white point when this widget is
    not selected or active, a thin green circle when it is highlighted,
    and a thicker cyan circle when it is active (being positioned).
    Defaults can be adjusted - but take care to define cursor geometry
    that makes sense for this widget. The geometry will be aligned on the
    constraining plane, with the plane normal aligned with the X axis of
    the geometry (similar behavior to Glyph3D).
    
    TODO: still need to work on
    1) translation when mouse is outside bounding planes
    2) size of the widget
    
    See Also:
    
    HandleRepresentation HandleWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkConstrainedPointHandleRepresentation, obj, update, **traits)
    
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

    def _get_oblique_plane(self):
        return wrap_vtk(self._vtk_obj.GetObliquePlane())
    def _set_oblique_plane(self, arg):
        old_val = self._get_oblique_plane()
        self._wrap_call(self._vtk_obj.SetObliquePlane,
                        deref_vtk(arg))
        self.trait_property_changed('oblique_plane', old_val, arg)
    oblique_plane = traits.Property(_get_oblique_plane, _set_oblique_plane, help=\
        """
        If the projection_normal is set to Oblique, then this is the
        oblique plane used to constrain the handle position
        """
    )

    def _get_cursor_shape(self):
        return wrap_vtk(self._vtk_obj.GetCursorShape())
    def _set_cursor_shape(self, arg):
        old_val = self._get_cursor_shape()
        self._wrap_call(self._vtk_obj.SetCursorShape,
                        deref_vtk(arg))
        self.trait_property_changed('cursor_shape', old_val, arg)
    cursor_shape = traits.Property(_get_cursor_shape, _set_cursor_shape, help=\
        """
        Specify the cursor shape. Keep in mind that the shape will be
        aligned with the  constraining plane by orienting it such that
        the x axis of the geometry lies along the normal of the plane.
        """
    )

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

    projection_position = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The position of the bounding plane from the origin along the
        normal. The origin and normal are defined in the oblique plane
        when the projection_normal is Oblique. For the X, Y, and Z axes
        projection normals, the normal is the axis direction, and the
        origin is (0,0,0).
        """
    )
    def _projection_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionPosition,
                        self.projection_position)

    def get_position(self, *args):
        """
        V.get_position([float, float, float])
        C++: void GetPosition(double xyz[3])
        Set/Get the position of the point in display coordinates.  These
        are convenience methods that extend the superclasses'
        get_handle_position() method. Note that only the x-y coordinate
        values are used
        """
        ret = self._wrap_call(self._vtk_obj.GetPosition, *args)
        return ret

    def set_position(self, *args):
        """
        V.set_position(float, float, float)
        C++: void SetPosition(double x, double y, double z)
        V.set_position([float, float, float])
        C++: void SetPosition(double xyz[3])
        Set/Get the position of the point in display coordinates.  These
        are convenience methods that extend the superclasses'
        get_handle_position() method. Note that only the x-y coordinate
        values are used
        """
        ret = self._wrap_call(self._vtk_obj.SetPosition, *args)
        return ret

    def _get_active_cursor_shape(self):
        return wrap_vtk(self._vtk_obj.GetActiveCursorShape())
    def _set_active_cursor_shape(self, arg):
        old_val = self._get_active_cursor_shape()
        self._wrap_call(self._vtk_obj.SetActiveCursorShape,
                        deref_vtk(arg))
        self.trait_property_changed('active_cursor_shape', old_val, arg)
    active_cursor_shape = traits.Property(_get_active_cursor_shape, _set_active_cursor_shape, help=\
        """
        Specify the shape of the cursor (handle) when it is active. This
        is the geometry that will be used when the mouse is close to the
        handle or if the user is manipulating the handle.
        """
    )

    def _get_active_property(self):
        return wrap_vtk(self._vtk_obj.GetActiveProperty())
    active_property = traits.Property(_get_active_property, help=\
        """
        This is the property used when the user is interacting with the
        handle.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    property = traits.Property(_get_property, help=\
        """
        This is the property used when the handle is not active (the
        mouse is not near the handle)
        """
    )

    def _get_selected_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedProperty())
    selected_property = traits.Property(_get_selected_property, help=\
        """
        This is the property used when the mouse is near the handle (but
        the user is not yet interacting with it)
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
    (('display_position', 'GetDisplayPosition'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('handle_size', 'GetHandleSize'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('projection_position', 'GetProjectionPosition'), ('tolerance',
    'GetTolerance'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('projection_normal',
    'GetProjectionNormal'), ('active_representation',
    'GetActiveRepresentation'), ('pickable', 'GetPickable'),
    ('need_to_render', 'GetNeedToRender'), ('reference_count',
    'GetReferenceCount'), ('place_factor', 'GetPlaceFactor'),
    ('constrained', 'GetConstrained'), ('world_position',
    'GetWorldPosition'), ('use_bounds', 'GetUseBounds'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'pickable', 'use_bounds',
    'visibility', 'projection_normal', 'allocated_render_time',
    'display_position', 'estimated_render_time', 'handle_size',
    'place_factor', 'projection_position', 'render_time_multiplier',
    'tolerance', 'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ConstrainedPointHandleRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ConstrainedPointHandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['active_representation', 'constrained',
            'need_to_render', 'use_bounds', 'visibility'], ['projection_normal'],
            ['allocated_render_time', 'display_position', 'estimated_render_time',
            'handle_size', 'place_factor', 'projection_position',
            'render_time_multiplier', 'tolerance', 'world_position']),
            title='Edit ConstrainedPointHandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ConstrainedPointHandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

