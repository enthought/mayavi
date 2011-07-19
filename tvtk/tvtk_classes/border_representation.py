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


class BorderRepresentation(WidgetRepresentation):
    """
    BorderRepresentation - represent a BorderWidget
    
    Superclass: WidgetRepresentation
    
    This class is used to represent and render a vt_border_widget. To use
    this class, you need to specify the two corners of a rectangular
    region.
    
    The class is typically subclassed so that specialized representations
    can be created.  The class defines an API and a default
    implementation that the BorderRepresentation interacts with to
    render itself in the scene.
    
    Caveats:
    
    The separation of the widget event handling (e.g., BorderWidget)
    from the representation (vtk_border_representation) enables users and
    developers to create new appearances for the widget. It also
    facilitates parallel processing, where the client application handles
    events, and remote representations of the widget are slaves to the
    client (and do not handle events).
    
    See Also:
    
    BorderWidget TextWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBorderRepresentation, obj, update, **traits)
    
    moving = tvtk_base.false_bool_trait(help=\
        """
        This is a modifier of the interaction state. When set, widget
        interaction allows the border (and stuff inside of it) to be
        translated with mouse motion.
        """
    )
    def _moving_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMoving,
                        self.moving_)

    proportional_resize = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether resizing operations should keep the x-y
        directions proportional to one another. Also, if
        proportional_resize is on, then the rectangle (Position,Position2)
        is a bounding rectangle, and the representation will be placed in
        the rectangle in such a way as to preserve the aspect ratio of
        the representation.
        """
    )
    def _proportional_resize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProportionalResize,
                        self.proportional_resize_)

    show_border = traits.Trait('on',
    tvtk_base.TraitRevPrefixMap({'active': 2, 'on': 1, 'off': 0}), help=\
        """
        Specify when and if the border should appear. If show_border is
        "on", then the border will always appear. If show_border is "off"
        then the border will never appear.  If show_border is "active"
        then the border will appear when the mouse pointer enters the
        region bounded by the border widget.
        """
    )
    def _show_border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowBorder,
                        self.show_border_)

    position2 = traits.Array(shape=(2,), value=(0.10000000000000001, 0.10000000000000001), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the proportional_resize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., proportional_resize is on), then the rectangle
        (Position,Position2) is a bounding rectangle. Also,
        """
    )
    def _position2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition2,
                        self.position2)

    position = traits.Array(shape=(2,), value=(0.050000000000000003, 0.050000000000000003), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the proportional_resize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., proportional_resize is on), then the rectangle
        (Position,Position2) is a bounding rectangle. Also,
        """
    )
    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    tolerance = traits.Trait(3, traits.Range(1, 10, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    minimum_size = traits.Array(shape=(2,), value=(1, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _minimum_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumSize,
                        self.minimum_size)

    maximum_size = traits.Array(shape=(2,), value=(100000, 100000), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _maximum_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumSize,
                        self.maximum_size)

    def _get_border_property(self):
        return wrap_vtk(self._vtk_obj.GetBorderProperty())
    border_property = traits.Property(_get_border_property, help=\
        """
        Specify the properties of the border.
        """
    )

    def _get_position2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPosition2Coordinate())
    position2_coordinate = traits.Property(_get_position2_coordinate, help=\
        """
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the proportional_resize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., proportional_resize is on), then the rectangle
        (Position,Position2) is a bounding rectangle. Also,
        """
    )

    def _get_position_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPositionCoordinate())
    position_coordinate = traits.Property(_get_position_coordinate, help=\
        """
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the proportional_resize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., proportional_resize is on), then the rectangle
        (Position,Position2) is a bounding rectangle. Also,
        """
    )

    def _get_selection_point(self):
        return self._vtk_obj.GetSelectionPoint()
    selection_point = traits.Property(_get_selection_point, help=\
        """
        After a selection event within the region interior to the border;
        the normalized selection coordinates may be obtained.
        """
    )

    def get_size(self, *args):
        """
        V.get_size([float, float])
        C++: virtual void GetSize(double size[2])
        Subclasses should implement these methods. See the superclasses'
        documentation for more information.
        """
        ret = self._wrap_call(self._vtk_obj.GetSize, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('minimum_size',
    'GetMinimumSize'), ('handle_size', 'GetHandleSize'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('position2',
    'GetPosition2'), ('need_to_render', 'GetNeedToRender'), ('dragable',
    'GetDragable'), ('proportional_resize', 'GetProportionalResize'),
    ('visibility', 'GetVisibility'), ('reference_count',
    'GetReferenceCount'), ('show_border', 'GetShowBorder'), ('moving',
    'GetMoving'), ('position', 'GetPosition'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('place_factor', 'GetPlaceFactor'),
    ('maximum_size', 'GetMaximumSize'), ('pickable', 'GetPickable'),
    ('tolerance', 'GetTolerance'), ('use_bounds', 'GetUseBounds'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'moving',
    'need_to_render', 'pickable', 'proportional_resize', 'use_bounds',
    'visibility', 'show_border', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'maximum_size',
    'minimum_size', 'place_factor', 'position', 'position2',
    'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BorderRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BorderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['moving', 'need_to_render', 'proportional_resize',
            'use_bounds', 'visibility'], ['show_border'],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'maximum_size', 'minimum_size', 'place_factor', 'position',
            'position2', 'render_time_multiplier', 'tolerance']),
            title='Edit BorderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BorderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

