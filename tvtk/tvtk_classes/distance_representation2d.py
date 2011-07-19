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

from tvtk.tvtk_classes.distance_representation import DistanceRepresentation


class DistanceRepresentation2D(DistanceRepresentation):
    """
    DistanceRepresentation2D - represent the DistanceWidget
    
    Superclass: DistanceRepresentation
    
    The DistanceRepresentation2D is a representation for the
    DistanceWidget. This representation consists of a measuring line
    (axis) and two HandleWidgets to place the end points of the line.
    Note that this particular widget draws its representation in the
    overlay plane.
    
    See Also:
    
    DistanceWidget DistanceRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDistanceRepresentation2D, obj, update, **traits)
    
    def get_point2display_position(self, *args):
        """
        V.get_point2display_position([float, float, float])
        C++: void GetPoint2DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.GetPoint2DisplayPosition, *args)
        return ret

    def set_point2display_position(self, *args):
        """
        V.set_point2display_position([float, float, float])
        C++: void SetPoint2DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.SetPoint2DisplayPosition, *args)
        return ret

    def get_point1display_position(self, *args):
        """
        V.get_point1display_position([float, float, float])
        C++: void GetPoint1DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.GetPoint1DisplayPosition, *args)
        return ret

    def set_point1display_position(self, *args):
        """
        V.set_point1display_position([float, float, float])
        C++: void SetPoint1DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.SetPoint1DisplayPosition, *args)
        return ret

    def get_point1_world_position(self, *args):
        """
        V.get_point1_world_position([float, float, float])
        C++: void GetPoint1WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1WorldPosition, *args)
        return ret

    def set_point1_world_position(self, *args):
        """
        V.set_point1_world_position([float, float, float])
        C++: void SetPoint1WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1WorldPosition, *args)
        return ret

    def get_point2_world_position(self, *args):
        """
        V.get_point2_world_position([float, float, float])
        C++: void GetPoint2WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2WorldPosition, *args)
        return ret

    def set_point2_world_position(self, *args):
        """
        V.set_point2_world_position([float, float, float])
        C++: void SetPoint2WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2WorldPosition, *args)
        return ret

    def _get_axis(self):
        return wrap_vtk(self._vtk_obj.GetAxis())
    axis = traits.Property(_get_axis, help=\
        """
        Retrieve the AxisActor2D used to draw the measurement axis.
        With this properties can be set and so on.
        """
    )

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('label_format', 'GetLabelFormat'), ('debug', 'GetDebug'),
    ('dragable', 'GetDragable'), ('visibility', 'GetVisibility'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('need_to_render', 'GetNeedToRender'), ('reference_count',
    'GetReferenceCount'), ('place_factor', 'GetPlaceFactor'), ('pickable',
    'GetPickable'), ('tolerance', 'GetTolerance'), ('use_bounds',
    'GetUseBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'label_format',
    'place_factor', 'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DistanceRepresentation2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DistanceRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'label_format', 'place_factor', 'render_time_multiplier',
            'tolerance']),
            title='Edit DistanceRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DistanceRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

