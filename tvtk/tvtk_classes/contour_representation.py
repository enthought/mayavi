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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class ContourRepresentation(WidgetRepresentation):
    """
    ContourRepresentation - represent the ContourWidget
    
    Superclass: WidgetRepresentation
    
    The ContourRepresentation is a superclass for various types of
    representations for the ContourWidget.
    
    Managing contour points:
    
    The classes ContourRepresentationNode,
    ContourRepresentationInternals, ContourRepresentationPoint
    manage the data structure used to represent nodes and points on a
    contour. A contour may contain several nodes and several more points.
    Nodes are usually the result of user clicked points on the contour.
    Additional points are created between nodes to generate a smooth
    curve using some Interpolator. See the method
    set_line_interpolator.\par The data structure stores both the world and
    display positions for every point. (This may seem like a
    duplication.) The default behaviour of this class is to use the
    world_position to do all the math. Typically a point is added at a
    given display position. Its corresponding world position is computed
    using the point placer and stored. Any query of the display position
    of a stored point is done via the Renderer, which computes the
    display position given a world position.
    
    \par So why maintain the display position ? Consider drawing a
    contour on a volume widget. You might want the contour to be located
    at a certain world position in the volume or you might want to be
    overlayed over the window like an actor2d. The default behaviour of
    this class is to provide the former behaviour.
    
    \par To achieve the latter behaviour override the methods that return
    the display position (to return the set display position instead of
    computing it from the world positions) and the method build_lines() to
    interpolate lines using their display positions intead of world
    positions.
    
    See Also:
    
    ContourWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContourRepresentation, obj, update, **traits)
    
    closed_loop = tvtk_base.false_bool_trait(help=\
        """
        Set / Get the closed_loop value. This ivar indicates whether the
        contour forms a closed loop.
        """
    )
    def _closed_loop_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClosedLoop,
                        self.closed_loop_)

    show_selected_nodes = tvtk_base.false_bool_trait(help=\
        """
        A flag to indicate whether to show the Selected nodes Default is
        to set it to false.
        """
    )
    def _show_selected_nodes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowSelectedNodes,
                        self.show_selected_nodes_)

    current_operation = traits.Trait('inactive',
    tvtk_base.TraitRevPrefixMap({'shift': 2, 'inactive': 0, 'translate': 1, 'scale': 3}), help=\
        """
        Set / get the current operation. The widget is either inactive,
        or it is being translated.
        """
    )
    def _current_operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentOperation,
                        self.current_operation_)

    pixel_tolerance = traits.Trait(7, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        The tolerance to use when calculations are performed in display
        coordinates
        """
    )
    def _pixel_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPixelTolerance,
                        self.pixel_tolerance)

    def get_nth_node_world_position(self, *args):
        """
        V.get_nth_node_world_position(int, [float, float, float]) -> int
        C++: virtual int GetNthNodeWorldPosition(int n, double pos[3])
        Get the nth node's world position. Will return 1 on success, or 0
        if there are not at least (n+1) nodes (0 based counting).
        """
        ret = self._wrap_call(self._vtk_obj.GetNthNodeWorldPosition, *args)
        return ret

    def set_nth_node_world_position(self, *args):
        """
        V.set_nth_node_world_position(int, [float, float, float]) -> int
        C++: virtual int SetNthNodeWorldPosition(int n, double pos[3])
        V.set_nth_node_world_position(int, [float, float, float], [float,
            float, float, float, float, float, float, float, float])
            -> int
        C++: virtual int SetNthNodeWorldPosition(int n, double pos[3],
            double orient[9])
        Set the nth node's world position. Will return 1 on success, or 0
        if there are not at least (n+1) nodes (0 based counting) or the
        world position is not valid according to the point placer.
        """
        ret = self._wrap_call(self._vtk_obj.SetNthNodeWorldPosition, *args)
        return ret

    def _get_line_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetLineInterpolator())
    def _set_line_interpolator(self, arg):
        old_val = self._get_line_interpolator()
        self._wrap_call(self._vtk_obj.SetLineInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('line_interpolator', old_val, arg)
    line_interpolator = traits.Property(_get_line_interpolator, _set_line_interpolator, help=\
        """
        Set / Get the Line Interpolator. The line interpolator is
        responsible for generating the line segments connecting nodes.
        """
    )

    world_tolerance = traits.Trait(0.001, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        The tolerance to use when calculations are performed in world
        coordinates
        """
    )
    def _world_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWorldTolerance,
                        self.world_tolerance)

    def get_nth_node_display_position(self, *args):
        """
        V.get_nth_node_display_position(int, [float, float]) -> int
        C++: virtual int GetNthNodeDisplayPosition(int n, double pos[2])
        Get the nth node's display position. Will return 1 on success, or
        0 if there are not at least (n+1) nodes (0 based counting).
        """
        ret = self._wrap_call(self._vtk_obj.GetNthNodeDisplayPosition, *args)
        return ret

    def set_nth_node_display_position(self, *args):
        """
        V.set_nth_node_display_position(int, int, int) -> int
        C++: virtual int SetNthNodeDisplayPosition(int n, int X, int Y)
        V.set_nth_node_display_position(int, [int, int]) -> int
        C++: virtual int SetNthNodeDisplayPosition(int n, int pos[2])
        V.set_nth_node_display_position(int, [float, float]) -> int
        C++: virtual int SetNthNodeDisplayPosition(int n, double pos[2])
        Set the nth node's display position. Display position will be
        converted into world position according to the constraints of the
        point placer. Will return 1 on success, or 0 if there are not at
        least (n+1) nodes (0 based counting) or the world position is not
        valid.
        """
        ret = self._wrap_call(self._vtk_obj.SetNthNodeDisplayPosition, *args)
        return ret

    def _get_point_placer(self):
        return wrap_vtk(self._vtk_obj.GetPointPlacer())
    def _set_point_placer(self, arg):
        old_val = self._get_point_placer()
        self._wrap_call(self._vtk_obj.SetPointPlacer,
                        deref_vtk(arg))
        self.trait_property_changed('point_placer', old_val, arg)
    point_placer = traits.Property(_get_point_placer, _set_point_placer, help=\
        """
        
        """
    )

    def get_nth_node_selected(self, *args):
        """
        V.get_nth_node_selected(int) -> int
        C++: virtual int GetNthNodeSelected(int)
        Set/Get whether the active or nth node is selected.
        """
        ret = self._wrap_call(self._vtk_obj.GetNthNodeSelected, *args)
        return ret

    def set_nth_node_selected(self, *args):
        """
        V.set_nth_node_selected(int) -> int
        C++: virtual int SetNthNodeSelected(int)
        Set/Get whether the active or nth node is selected.
        """
        ret = self._wrap_call(self._vtk_obj.SetNthNodeSelected, *args)
        return ret

    def get_active_node_display_position(self, *args):
        """
        V.get_active_node_display_position([float, float]) -> int
        C++: virtual int GetActiveNodeDisplayPosition(double pos[2])
        Get the display position of the active node. Will return 0 if
        there is no active node, or 1 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.GetActiveNodeDisplayPosition, *args)
        return ret

    def _get_active_node_selected(self):
        return self._vtk_obj.GetActiveNodeSelected()
    active_node_selected = traits.Property(_get_active_node_selected, help=\
        """
        Set/Get whether the active or nth node is selected.
        """
    )

    def get_active_node_world_orientation(self, *args):
        """
        V.get_active_node_world_orientation([float, float, float, float,
            float, float, float, float, float]) -> int
        C++: virtual int GetActiveNodeWorldOrientation(double orient[9])
        Get the world orientation of the active node. Will return 0 if
        there is no active node, or 1 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.GetActiveNodeWorldOrientation, *args)
        return ret

    def get_active_node_world_position(self, *args):
        """
        V.get_active_node_world_position([float, float, float]) -> int
        C++: virtual int GetActiveNodeWorldPosition(double pos[3])
        Get the world position of the active node. Will return 0 if there
        is no active node, or 1 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.GetActiveNodeWorldPosition, *args)
        return ret

    def _get_contour_representation_as_poly_data(self):
        return wrap_vtk(self._vtk_obj.GetContourRepresentationAsPolyData())
    contour_representation_as_poly_data = traits.Property(_get_contour_representation_as_poly_data, help=\
        """
        Get the points in this contour as a PolyData.
        """
    )

    def get_intermediate_point_world_position(self, *args):
        """
        V.get_intermediate_point_world_position(int, int, [float, float,
            float]) -> int
        C++: virtual int GetIntermediatePointWorldPosition(int n, int idx,
             double point[3])
        Get the world position of the intermediate point at index idx
        between nodes n and (n+1) (or n and 0 if n is the last node and
        the loop is closed). Returns 1 on success or 0 if n or idx are
        out of range.
        """
        ret = self._wrap_call(self._vtk_obj.GetIntermediatePointWorldPosition, *args)
        return ret

    def get_node_poly_data(self, *args):
        """
        V.get_node_poly_data(PolyData)
        C++: void GetNodePolyData(PolyData *poly)
        Get the nodes and not the intermediate points in this contour as
        a PolyData.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetNodePolyData, *my_args)
        return ret

    def get_nth_node_slope(self, *args):
        """
        V.get_nth_node_slope(int, [float, float, float]) -> int
        C++: virtual int GetNthNodeSlope(int idx, double slope[3])
        Get the nth node's slope. Will return 1 on success, or 0 if there
        are not at least (n+1) nodes (0 based counting).
        """
        ret = self._wrap_call(self._vtk_obj.GetNthNodeSlope, *args)
        return ret

    def get_nth_node_world_orientation(self, *args):
        """
        V.get_nth_node_world_orientation(int, [float, float, float, float,
            float, float, float, float, float]) -> int
        C++: virtual int GetNthNodeWorldOrientation(int n,
            double orient[9])
        Get the nth node's world orientation. Will return 1 on success,
        or 0 if there are not at least (n+1) nodes (0 based counting).
        """
        ret = self._wrap_call(self._vtk_obj.GetNthNodeWorldOrientation, *args)
        return ret

    def get_number_of_intermediate_points(self, *args):
        """
        V.get_number_of_intermediate_points(int) -> int
        C++: virtual int GetNumberOfIntermediatePoints(int n)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfIntermediatePoints, *args)
        return ret

    def _get_number_of_nodes(self):
        return self._vtk_obj.GetNumberOfNodes()
    number_of_nodes = traits.Property(_get_number_of_nodes, help=\
        """
        Get the number of nodes.
        """
    )

    def activate_node(self, *args):
        """
        V.activate_node([float, float]) -> int
        C++: virtual int ActivateNode(double displayPos[2])
        V.activate_node([int, int]) -> int
        C++: virtual int ActivateNode(int displayPos[2])
        V.activate_node(int, int) -> int
        C++: virtual int ActivateNode(int X, int Y)
        Given a display position, activate a node. The closest node
        within tolerance will be activated. If a node is activated, 1
        will be returned, otherwise 0 will be returned.
        """
        ret = self._wrap_call(self._vtk_obj.ActivateNode, *args)
        return ret

    def add_intermediate_point_world_position(self, *args):
        """
        V.add_intermediate_point_world_position(int, [float, float, float])
            -> int
        C++: virtual int AddIntermediatePointWorldPosition(int n,
            double point[3])
        Add an intermediate point between node n and n+1 (or n and 0 if n
        is the last node and the loop is closed). Returns 1 on success or
        0 if n is out of range.
        """
        ret = self._wrap_call(self._vtk_obj.AddIntermediatePointWorldPosition, *args)
        return ret

    def add_node_at_display_position(self, *args):
        """
        V.add_node_at_display_position([float, float]) -> int
        C++: virtual int AddNodeAtDisplayPosition(double displayPos[2])
        V.add_node_at_display_position([int, int]) -> int
        C++: virtual int AddNodeAtDisplayPosition(int displayPos[2])
        V.add_node_at_display_position(int, int) -> int
        C++: virtual int AddNodeAtDisplayPosition(int X, int Y)
        Add a node at a specific display position. This will be converted
        into a world position according to the current constraints of the
        point placer. Return 0 if a point could not be added, 1
        otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.AddNodeAtDisplayPosition, *args)
        return ret

    def add_node_at_world_position(self, *args):
        """
        V.add_node_at_world_position(float, float, float) -> int
        C++: virtual int AddNodeAtWorldPosition(double x, double y,
            double z)
        V.add_node_at_world_position([float, float, float]) -> int
        C++: virtual int AddNodeAtWorldPosition(double worldPos[3])
        V.add_node_at_world_position([float, float, float], [float, float,
            float, float, float, float, float, float, float]) -> int
        C++: virtual int AddNodeAtWorldPosition(double worldPos[3],
            double worldOrient[9])
        Add a node at a specific world position. Returns 0 if the node
        could not be added, 1 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.AddNodeAtWorldPosition, *args)
        return ret

    def add_node_on_contour(self, *args):
        """
        V.add_node_on_contour(int, int) -> int
        C++: virtual int AddNodeOnContour(int X, int Y)
        Given a specific X, Y pixel location, add a new node on the
        contour at this location.
        """
        ret = self._wrap_call(self._vtk_obj.AddNodeOnContour, *args)
        return ret

    def clear_all_nodes(self):
        """
        V.clear_all_nodes()
        C++: virtual void ClearAllNodes()
        Delete all nodes.
        """
        ret = self._vtk_obj.ClearAllNodes()
        return ret
        

    def delete_active_node(self):
        """
        V.delete_active_node() -> int
        C++: virtual int DeleteActiveNode()
        Delete the active node. Returns 1 on success or 0 if the active
        node did not indicate a valid node.
        """
        ret = self._vtk_obj.DeleteActiveNode()
        return ret
        

    def delete_last_node(self):
        """
        V.delete_last_node() -> int
        C++: virtual int DeleteLastNode()
        Delete the last node. Returns 1 on success or 0 if there were not
        any nodes.
        """
        ret = self._vtk_obj.DeleteLastNode()
        return ret
        

    def delete_nth_node(self, *args):
        """
        V.delete_nth_node(int) -> int
        C++: virtual int DeleteNthNode(int n)
        Delete the nth node. Return 1 on success or 0 if n is out of
        range.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteNthNode, *args)
        return ret

    def set_active_node_to_display_position(self, *args):
        """
        V.set_active_node_to_display_position([float, float]) -> int
        C++: virtual int SetActiveNodeToDisplayPosition(double pos[2])
        V.set_active_node_to_display_position([int, int]) -> int
        C++: virtual int SetActiveNodeToDisplayPosition(int pos[2])
        V.set_active_node_to_display_position(int, int) -> int
        C++: virtual int SetActiveNodeToDisplayPosition(int X, int Y)
        Move the active node based on a specified display position. The
        display position will be converted into a world position. If the
        new position is not valid or there is no active node, a 0 will be
        returned. Otherwise, on success a 1 will be returned.
        """
        ret = self._wrap_call(self._vtk_obj.SetActiveNodeToDisplayPosition, *args)
        return ret

    def set_active_node_to_world_position(self, *args):
        """
        V.set_active_node_to_world_position([float, float, float]) -> int
        C++: virtual int SetActiveNodeToWorldPosition(double pos[3])
        V.set_active_node_to_world_position([float, float, float], [float,
            float, float, float, float, float, float, float, float])
            -> int
        C++: virtual int SetActiveNodeToWorldPosition(double pos[3],
            double orient[9])"""
        ret = self._wrap_call(self._vtk_obj.SetActiveNodeToWorldPosition, *args)
        return ret

    def set_rebuild_locator(self, *args):
        """
        V.set_rebuild_locator(bool)
        C++: void SetRebuildLocator(bool a)"""
        ret = self._wrap_call(self._vtk_obj.SetRebuildLocator, *args)
        return ret

    def toggle_active_node_selected(self):
        """
        V.toggle_active_node_selected() -> int
        C++: virtual int ToggleActiveNodeSelected()
        Set/Get whether the active or nth node is selected.
        """
        ret = self._vtk_obj.ToggleActiveNodeSelected()
        return ret
        

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('need_to_render', 'GetNeedToRender'), ('dragable', 'GetDragable'),
    ('visibility', 'GetVisibility'), ('current_operation',
    'GetCurrentOperation'), ('reference_count', 'GetReferenceCount'),
    ('show_selected_nodes', 'GetShowSelectedNodes'), ('pickable',
    'GetPickable'), ('pixel_tolerance', 'GetPixelTolerance'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('place_factor', 'GetPlaceFactor'), ('closed_loop', 'GetClosedLoop'),
    ('world_tolerance', 'GetWorldTolerance'), ('use_bounds',
    'GetUseBounds'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['closed_loop', 'debug', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'show_selected_nodes', 'use_bounds',
    'visibility', 'current_operation', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'pixel_tolerance',
    'place_factor', 'render_time_multiplier', 'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContourRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ContourRepresentation properties', scrollable=True, resizable=True,
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
            title='Edit ContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

