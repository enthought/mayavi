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

from tvtk.tvtk_classes.contour_representation import ContourRepresentation


class OrientedGlyphContourRepresentation(ContourRepresentation):
    """
    OrientedGlyphContourRepresentation - Default representation for
    the contour widget
    
    Superclass: ContourRepresentation
    
    This class provides the default concrete representation for the
    ContourWidget. It works in conjunction with the
    ContourLineInterpolator and PointPlacer. See ContourWidget
    for details.
    
    See Also:
    
    ContourRepresentation ContourWidget PointPlacer
    ContourLineInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOrientedGlyphContourRepresentation, obj, update, **traits)
    
    always_on_top = tvtk_base.false_bool_trait(help=\
        """
        Controls whether the contour widget should always appear on top
        of other actors in the scene. (In effect, this will disable
        open_gl Depth buffer tests while rendering the contour). Default
        is to set it to false.
        """
    )
    def _always_on_top_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlwaysOnTop,
                        self.always_on_top_)

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

    def _get_lines_property(self):
        return wrap_vtk(self._vtk_obj.GetLinesProperty())
    lines_property = traits.Property(_get_lines_property, help=\
        """
        This is the property used by the lines.
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

    def set_line_color(self, *args):
        """
        V.set_line_color(float, float, float)
        C++: void SetLineColor(double r, double g, double b)
        Convenience method to set the line color. Ideally one should use
        get_lines_property()->_set_color().
        """
        ret = self._wrap_call(self._vtk_obj.SetLineColor, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('need_to_render', 'GetNeedToRender'), ('dragable', 'GetDragable'),
    ('visibility', 'GetVisibility'), ('current_operation',
    'GetCurrentOperation'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('show_selected_nodes',
    'GetShowSelectedNodes'), ('always_on_top', 'GetAlwaysOnTop'),
    ('pickable', 'GetPickable'), ('pixel_tolerance', 'GetPixelTolerance'),
    ('reference_count', 'GetReferenceCount'), ('place_factor',
    'GetPlaceFactor'), ('closed_loop', 'GetClosedLoop'),
    ('world_tolerance', 'GetWorldTolerance'), ('use_bounds',
    'GetUseBounds'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['always_on_top', 'closed_loop', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'pickable',
    'show_selected_nodes', 'use_bounds', 'visibility',
    'current_operation', 'allocated_render_time', 'estimated_render_time',
    'handle_size', 'pixel_tolerance', 'place_factor',
    'render_time_multiplier', 'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OrientedGlyphContourRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OrientedGlyphContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['always_on_top', 'closed_loop', 'need_to_render',
            'show_selected_nodes', 'use_bounds', 'visibility'],
            ['current_operation'], ['allocated_render_time',
            'estimated_render_time', 'handle_size', 'pixel_tolerance',
            'place_factor', 'render_time_multiplier', 'world_tolerance']),
            title='Edit OrientedGlyphContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OrientedGlyphContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

