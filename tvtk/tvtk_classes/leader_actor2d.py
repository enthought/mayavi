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

from tvtk.tvtk_classes.actor2d import Actor2D


class LeaderActor2D(Actor2D):
    """
    LeaderActor2D - create a leader with optional label and arrows
    
    Superclass: Actor2D
    
    LeaderActor2D creates a leader with an optional label and arrows.
    (A leader is typically used to indicate distance between points.)
    LeaderActor2D is a type of Actor2D; that is, it is drawn on the
    overlay plane and is not occluded by 3d geometry. To use this class,
    you typically specify two points defining the start and end points of
    the line (x-y definition using Coordinate class), whether to place
    arrows on one or both end points, and whether to label the leader.
    Also, this class has a special feature that allows curved leaders to
    be created by specifying a radius.
    
    Use the LeaderActor2D uses its superclass Actor2D instance
    variables Position and Position2 Coordinates to place an instance
    of LeaderActor2D (i.e., these two data members represent the start
    and end points of the leader).  Using these Coordinates you can
    specify the position of the leader in a variety of coordinate
    systems.
    
    To control the appearance of the actor, use the superclasses
    Actor2D::vtkProperty2D and the TextProperty objects associated
    with this actor.
    
    See Also:
    
    AxisActor2D Actor2D Coordinate TextProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLeaderActor2D, obj, update, **traits)
    
    auto_label = tvtk_base.false_bool_trait(help=\
        """
        Enable auto-labelling. In this mode, the label is automatically
        updated based on distance (in world coordinates) between the two
        end points; or if a curved leader is being generated, the angle
        in degrees between the two points.
        """
    )
    def _auto_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoLabel,
                        self.auto_label_)

    arrow_placement = traits.Trait('both',
    tvtk_base.TraitRevPrefixMap({'both': 3, 'none': 0, 'point2': 2, 'point1': 1}), help=\
        """
        Control whether arrow heads are drawn on the leader. Arrows may
        be drawn on one end, both ends, or not at all.
        """
    )
    def _arrow_placement_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrowPlacement,
                        self.arrow_placement_)

    arrow_style = traits.Trait('filled',
    tvtk_base.TraitRevPrefixMap({'open': 1, 'filled': 0, 'hollow': 2}), help=\
        """
        Control the appearance of the arrow heads. A solid arrow head is
        a filled triangle; a open arrow looks like a "V"; and a hollow
        arrow looks like a non-filled triangle.
        """
    )
    def _arrow_style_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrowStyle,
                        self.arrow_style_)

    arrow_length = traits.Trait(0.04, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify the arrow length and base width (in normalized viewport
        coordinates).
        """
    )
    def _arrow_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrowLength,
                        self.arrow_length)

    label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Specify the format to use for auto-labelling.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    maximum_arrow_size = traits.Trait(25.0, traits.Range(1.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Limit the minimum and maximum size of the arrows. These values
        are expressed in pixels and clamp the minimum/maximum possible
        size for the width/length of the arrow head. (When clamped, the
        ratio between length and width is preserved.)
        """
    )
    def _maximum_arrow_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumArrowSize,
                        self.maximum_arrow_size)

    label_factor = traits.Trait(1.0, traits.Range(0.10000000000000001, 2.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the overall size of the fonts
        used to label the leader.
        """
    )
    def _label_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFactor,
                        self.label_factor)

    minimum_arrow_size = traits.Trait(2.0, traits.Range(1.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Limit the minimum and maximum size of the arrows. These values
        are expressed in pixels and clamp the minimum/maximum possible
        size for the width/length of the arrow head. (When clamped, the
        ratio between length and width is preserved.)
        """
    )
    def _minimum_arrow_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumArrowSize,
                        self.minimum_arrow_size)

    label = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the label for the leader. If the label is an empty
        string, then it will not be drawn.
        """
    )
    def _label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabel,
                        self.label)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Set/Get the text property of the label.
        """
    )

    radius = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get a radius which can be used to curve the leader.  If a
        radius is specified whose absolute value is greater than one half
        the distance between the two points defined by the superclasses'
        Position and Position2 ivars, then the leader will be curved. A
        positive radius will produce a curve such that the center is to
        the right of the line from Position and Position2; a negative
        radius will produce a curve in the opposite sense. By default,
        the radius is set to zero and thus there is no curvature. Note
        that the radius is expresses as a multiple of the distance
        between (Position,Position2); this avoids issues relative to
        coordinate system transformations.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    arrow_width = traits.Trait(0.02, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify the arrow length and base width (in normalized viewport
        coordinates).
        """
    )
    def _arrow_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrowWidth,
                        self.arrow_width)

    def _get_angle(self):
        return self._vtk_obj.GetAngle()
    angle = traits.Property(_get_angle, help=\
        """
        Obtain the length of the leader if the leader is not curved,
        otherwise obtain the angle that the leader circumscribes.
        """
    )

    def _get_length(self):
        return self._vtk_obj.GetLength()
    length = traits.Property(_get_length, help=\
        """
        Obtain the length of the leader if the leader is not curved,
        otherwise obtain the angle that the leader circumscribes.
        """
    )

    _updateable_traits_ = \
    (('auto_label', 'GetAutoLabel'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('arrow_placement', 'GetArrowPlacement'),
    ('minimum_arrow_size', 'GetMinimumArrowSize'), ('dragable',
    'GetDragable'), ('arrow_length', 'GetArrowLength'), ('height',
    'GetHeight'), ('label_factor', 'GetLabelFactor'), ('radius',
    'GetRadius'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('use_bounds',
    'GetUseBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('arrow_width', 'GetArrowWidth'),
    ('layer_number', 'GetLayerNumber'), ('maximum_arrow_size',
    'GetMaximumArrowSize'), ('label_format', 'GetLabelFormat'), ('debug',
    'GetDebug'), ('arrow_style', 'GetArrowStyle'), ('label', 'GetLabel'),
    ('width', 'GetWidth'), ('visibility', 'GetVisibility'), ('position2',
    'GetPosition2'), ('reference_count', 'GetReferenceCount'),
    ('position', 'GetPosition'), ('pickable', 'GetPickable'))
    
    _full_traitnames_list_ = \
    (['auto_label', 'debug', 'dragable', 'global_warning_display',
    'pickable', 'use_bounds', 'visibility', 'arrow_placement',
    'arrow_style', 'allocated_render_time', 'arrow_length', 'arrow_width',
    'estimated_render_time', 'height', 'label', 'label_factor',
    'label_format', 'layer_number', 'maximum_arrow_size',
    'minimum_arrow_size', 'position', 'position2', 'radius',
    'render_time_multiplier', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LeaderActor2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LeaderActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_label', 'use_bounds', 'visibility'],
            ['arrow_placement', 'arrow_style'], ['allocated_render_time',
            'arrow_length', 'arrow_width', 'estimated_render_time', 'height',
            'label', 'label_factor', 'label_format', 'layer_number',
            'maximum_arrow_size', 'minimum_arrow_size', 'position', 'position2',
            'radius', 'render_time_multiplier', 'width']),
            title='Edit LeaderActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LeaderActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

