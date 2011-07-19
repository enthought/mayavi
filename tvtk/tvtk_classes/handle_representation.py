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


class HandleRepresentation(WidgetRepresentation):
    """
    HandleRepresentation - abstract class for representing widget
    handles
    
    Superclass: WidgetRepresentation
    
    This class defines an API for widget handle representations. These
    representations interact with HandleWidget. Various
    representations can be used depending on the nature of the handle.
    The basic functionality of the handle representation is to maintain a
    position. The position is represented via a Coordinate, meaning
    that the position can be easily obtained in a variety of coordinate
    systems.
    
    Optional features for this representation include an active mode (the
    widget appears only when the mouse pointer is close to it). The
    active distance is expressed in pixels and represents a circle in
    display space.
    
    The class may be subclassed so that alternative representations can
    be created.  The class defines an API and a default implementation
    that the HandleWidget interacts with to render itself in the
    scene.
    
    Caveats:
    
    The separation of the widget event handling and representation
    enables users and developers to create new appearances for the
    widget. It also facilitates parallel processing, where the client
    application handles events, and remote representations of the widget
    are slaves to the client (and do not handle events).
    
    See Also:
    
    RectilinearWipeWidget WidgetRepresentation AbstractWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHandleRepresentation, obj, update, **traits)
    
    active_representation = tvtk_base.false_bool_trait(help=\
        """
        Flag controls whether the widget becomes visible when the mouse
        pointer moves close to it (i.e., the widget becomes active). By
        default, active_representation is off and the representation is
        always visible.
        """
    )
    def _active_representation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveRepresentation,
                        self.active_representation_)

    constrained = tvtk_base.false_bool_trait(help=\
        """
        Specify whether any motions (such as scale, translate, etc.) are
        constrained in some way (along an axis, etc.) Widgets can use
        this to control the resulting motion.
        """
    )
    def _constrained_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstrained,
                        self.constrained_)

    def _get_point_placer(self):
        return wrap_vtk(self._vtk_obj.GetPointPlacer())
    def _set_point_placer(self, arg):
        old_val = self._get_point_placer()
        self._wrap_call(self._vtk_obj.SetPointPlacer,
                        deref_vtk(arg))
        self.trait_property_changed('point_placer', old_val, arg)
    point_placer = traits.Property(_get_point_placer, _set_point_placer, help=\
        """
        Set/Get the point placer. Point placers can be used to dictate
        constraints on the placement of handles. As an example, see
        BoundedPlanePointPlacer (constrains the placement of handles
        to a set of bounded planes) FocalPlanePointPlacer (constrains
        placement on the focal plane) etc. The default point placer is
        PointPlacer (which does not apply any constraints, so the
        handles are free to move anywhere).
        """
    )

    tolerance = traits.Trait(15, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the widget to be
        active.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    display_position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Handles usually have their coordinates set in display coordinates
        (generally by an associated widget) and internally maintain the
        position in world coordinates. (Using world coordinates insures
        that handles are rendered in the right position when the camera
        view changes.) These methods are often subclassed because special
        constraint operations can be used to control the actual
        positioning.
        """
    )
    def _display_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayPosition,
                        self.display_position)

    world_position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Handles usually have their coordinates set in display coordinates
        (generally by an associated widget) and internally maintain the
        position in world coordinates. (Using world coordinates insures
        that handles are rendered in the right position when the camera
        view changes.) These methods are often subclassed because special
        constraint operations can be used to control the actual
        positioning.
        """
    )
    def _world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWorldPosition,
                        self.world_position)

    def _get_interaction_state_max_value(self):
        return self._vtk_obj.GetInteractionStateMaxValue()
    interaction_state_max_value = traits.Property(_get_interaction_state_max_value, help=\
        """
        The interaction state may be set from a widget (e.g.,
        handle_widget) or other object. This controls how the interaction
        with the widget proceeds. Normally this method is used as part of
        a handshaking processwith the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
    )

    def _get_interaction_state_min_value(self):
        return self._vtk_obj.GetInteractionStateMinValue()
    interaction_state_min_value = traits.Property(_get_interaction_state_min_value, help=\
        """
        The interaction state may be set from a widget (e.g.,
        handle_widget) or other object. This controls how the interaction
        with the widget proceeds. Normally this method is used as part of
        a handshaking processwith the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
    )

    def check_constraint(self, *args):
        """
        V.check_constraint(Renderer, [float, float]) -> int
        C++: virtual int CheckConstraint(Renderer *renderer,
            double pos[2])
        Method has to be overridden in the subclasses which has
        constraints on placing the handle (Ex.
        ConstrainedPointHandleRepresentation). It should return 1 if
        the position is within the constraint, else it should return
        0. By default it returns 1.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CheckConstraint, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(Prop)
        C++: virtual void DeepCopy(Prop *prop)
        Methods to make this class properly act like a
        WidgetRepresentation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def set_interaction_state(self, *args):
        """
        V.set_interaction_state(int)
        C++: void SetInteractionState(int)
        The interaction state may be set from a widget (e.g.,
        handle_widget) or other object. This controls how the interaction
        with the widget proceeds. Normally this method is used as part of
        a handshaking processwith the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
        ret = self._wrap_call(self._vtk_obj.SetInteractionState, *args)
        return ret

    _updateable_traits_ = \
    (('display_position', 'GetDisplayPosition'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('handle_size', 'GetHandleSize'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('world_position', 'GetWorldPosition'), ('dragable', 'GetDragable'),
    ('constrained', 'GetConstrained'), ('visibility', 'GetVisibility'),
    ('reference_count', 'GetReferenceCount'), ('active_representation',
    'GetActiveRepresentation'), ('need_to_render', 'GetNeedToRender'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('place_factor', 'GetPlaceFactor'), ('pickable', 'GetPickable'),
    ('tolerance', 'GetTolerance'), ('use_bounds', 'GetUseBounds'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'pickable', 'use_bounds',
    'visibility', 'allocated_render_time', 'display_position',
    'estimated_render_time', 'handle_size', 'place_factor',
    'render_time_multiplier', 'tolerance', 'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HandleRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['active_representation', 'constrained',
            'need_to_render', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'display_position', 'estimated_render_time',
            'handle_size', 'place_factor', 'render_time_multiplier', 'tolerance',
            'world_position']),
            title='Edit HandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

