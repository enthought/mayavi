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


class FocalPlaneContourRepresentation(ContourRepresentation):
    """
    FocalPlaneContourRepresentation - represent a contour drawn on the
    
    Superclass: ContourRepresentation
    
    The contour will stay on the focal plane irrespective of camera
    position/orientation changes. The class was written in order to be
    able to draw contours on a volume widget and have the contours
    overlayed on the focal plane in order to do contour segmentation. The
    superclass, ContourRepresentation handles contours that are drawn
    in actual world position co-ordinates, so they would rotate with the
    camera position/ orientation changes
    
    See Also:
    
    ContourWidget HandleRepresentation ContourRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFocalPlaneContourRepresentation, obj, update, **traits)
    
    def get_intermediate_point_display_position(self, *args):
        """
        V.get_intermediate_point_display_position(int, int, [float, float,
            float]) -> int
        C++: virtual int GetIntermediatePointDisplayPosition(int n,
            int idx, double point[3])
        Get the world position of the intermediate point at index idx
        between nodes n and (n+1) (or n and 0 if n is the last node and
        the loop is closed). Returns 1 on success or 0 if n or idx are
        out of range.
        """
        ret = self._wrap_call(self._vtk_obj.GetIntermediatePointDisplayPosition, *args)
        return ret

    def update_contour(self):
        """
        V.update_contour() -> int
        C++: virtual int UpdateContour()
        The method must be called whenever the contour needs to be
        updated, usually from render_opaque_geometry()
        """
        ret = self._vtk_obj.UpdateContour()
        return ret
        

    def update_contour_world_positions_based_on_display_positions(self):
        """
        V.update_contour_world_positions_based_on_display_positions()
        C++: virtual void UpdateContourWorldPositionsBasedOnDisplayPositions(
            )
        The class maintains its true contour locations based on display
        co-ords This method syncs the world co-ords data structure with
        the display co-ords.
        """
        ret = self._vtk_obj.UpdateContourWorldPositionsBasedOnDisplayPositions()
        return ret
        

    def update_lines(self, *args):
        """
        V.update_lines(int)
        C++: virtual void UpdateLines(int index)"""
        ret = self._wrap_call(self._vtk_obj.UpdateLines, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('need_to_render', 'GetNeedToRender'), ('dragable', 'GetDragable'),
    ('visibility', 'GetVisibility'), ('current_operation',
    'GetCurrentOperation'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('show_selected_nodes',
    'GetShowSelectedNodes'), ('pickable', 'GetPickable'),
    ('pixel_tolerance', 'GetPixelTolerance'), ('reference_count',
    'GetReferenceCount'), ('place_factor', 'GetPlaceFactor'),
    ('closed_loop', 'GetClosedLoop'), ('world_tolerance',
    'GetWorldTolerance'), ('use_bounds', 'GetUseBounds'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['closed_loop', 'debug', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'show_selected_nodes', 'use_bounds',
    'visibility', 'current_operation', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'pixel_tolerance',
    'place_factor', 'render_time_multiplier', 'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FocalPlaneContourRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FocalPlaneContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['closed_loop', 'need_to_render',
            'show_selected_nodes', 'use_bounds', 'visibility'],
            ['current_operation'], ['allocated_render_time',
            'estimated_render_time', 'handle_size', 'pixel_tolerance',
            'place_factor', 'render_time_multiplier', 'world_tolerance']),
            title='Edit FocalPlaneContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FocalPlaneContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

