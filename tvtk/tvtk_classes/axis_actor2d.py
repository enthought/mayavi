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


class AxisActor2D(Actor2D):
    """
    AxisActor2D - Create an axis with tick marks and labels
    
    Superclass: Actor2D
    
    AxisActor2D creates an axis with tick marks, labels, and/or a
    title, depending on the particular instance variable settings.
    AxisActor2D is a 2d actor; that is, it is drawn on the overlay
    plane and is not occluded by 3d geometry. To use this class, you
    typically specify two points defining the start and end points of the
    line (x-y definition using Coordinate class), the number of
    labels, and the data range (min,max). You can also control what parts
    of the axis are visible including the line, the tick marks, the
    labels, and the title.  You can also specify the label format (a
    printf style format).
    
    This class decides what font size to use and how to locate the
    labels. It also decides how to create reasonable tick marks and
    labels. The number of labels and the range of values may not match
    the number specified, but should be close.
    
    Labels are drawn on the "right" side of the axis. The "right" side is
    the side of the axis on the right as you move from Position to
    Position2. The way the labels and title line up with the axis and
    tick marks depends on whether the line is considered horizontal or
    vertical.
    
    The Actor2D instance variables Position and Position2 are
    instances of Coordinate. Note that the Position2 is an absolute
    position in that class (it was by default relative to Position in
    Actor2D).
    
    What this means is that you can specify the axis in a variety of
    coordinate systems. Also, the axis does not have to be either
    horizontal or vertical. The tick marks are created so that they are
    perpendicular to the axis.
    
    Set the text property/attributes of the title and the labels through
    the TextProperty objects associated to this actor.
    
    See Also:
    
    CubeAxesActor2D can be used to create axes in world coordinate
    space.
    
    Actor2D TextMapper PolyDataMapper2D ScalarBarActor
    Coordinate TextProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxisActor2D, obj, update, **traits)
    
    tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis tick marks.
        """
    )
    def _tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickVisibility,
                        self.tick_visibility_)

    label_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis labels.
        """
    )
    def _label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelVisibility,
                        self.label_visibility_)

    adjust_labels = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag that controls whether the labels and ticks are
        adjusted for "nice" numerical values to make it easier to read
        the labels. The adjustment is based in the Range instance
        variable. Call get_adjusted_range and get_adjusted_number_of_labels to
        get the adjusted range and number of labels.
        """
    )
    def _adjust_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustLabels,
                        self.adjust_labels_)

    title_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis title.
        """
    )
    def _title_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleVisibility,
                        self.title_visibility_)

    axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis line.
        """
    )
    def _axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisVisibility,
                        self.axis_visibility_)

    size_font_relative_to_axis = tvtk_base.false_bool_trait(help=\
        """
        Specify whether to size the fonts relative to the viewport or
        relative to length of the axis. By default, fonts are resized
        relative to the axis.
        """
    )
    def _size_font_relative_to_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSizeFontRelativeToAxis,
                        self.size_font_relative_to_axis_)

    font_factor = traits.Trait(1.0, traits.Range(0.10000000000000001, 2.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the overall size of the fonts
        used to label and title the axes. This ivar used in conjunction
        with the label_factor can be used to control font sizes.
        """
    )
    def _font_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontFactor,
                        self.font_factor)

    label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on the scalar
        bar.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    title_position = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get position of the axis title. 0 is at the start of the axis
        whereas 1 is at the end.
        """
    )
    def _title_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitlePosition,
                        self.title_position)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the scalar bar actor,
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    label_factor = traits.Trait(0.75, traits.Range(0.10000000000000001, 2.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the relative size of the axis
        labels to the axis title.
        """
    )
    def _label_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFactor,
                        self.label_factor)

    tick_length = traits.Trait(5, traits.Range(0, 100, enter_set=True, auto_set=False), help=\
        """
        Set/Get the length of the tick marks (expressed in pixels or
        display coordinates).
        """
    )
    def _tick_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickLength,
                        self.tick_length)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Set/Get the labels text property.
        """
    )

    range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    minor_tick_length = traits.Trait(3, traits.Range(0, 100, enter_set=True, auto_set=False), help=\
        """
        Set/Get the length of the minor tick marks (expressed in pixels
        or display coordinates).
        """
    )
    def _minor_tick_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorTickLength,
                        self.minor_tick_length)

    number_of_minor_ticks = traits.Trait(0, traits.Range(0, 20, enter_set=True, auto_set=False), help=\
        """
        Number of minor ticks to be displayed between each tick. Default
        is 0.
        """
    )
    def _number_of_minor_ticks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfMinorTicks,
                        self.number_of_minor_ticks)

    def _get_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTitleTextProperty())
    def _set_title_text_property(self, arg):
        old_val = self._get_title_text_property()
        self._wrap_call(self._vtk_obj.SetTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('title_text_property', old_val, arg)
    title_text_property = traits.Property(_get_title_text_property, _set_title_text_property, help=\
        """
        Set/Get the title text property.
        """
    )

    tick_offset = traits.Trait(2, traits.Range(0, 100, enter_set=True, auto_set=False), help=\
        """
        Set/Get the offset of the labels (expressed in pixels or display
        coordinates). The offset is the distance of labels from tick
        marks or other objects.
        """
    )
    def _tick_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickOffset,
                        self.tick_offset)

    number_of_labels = traits.Trait(5, traits.Range(2, 25, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of annotation labels to show.
        """
    )
    def _number_of_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLabels,
                        self.number_of_labels)

    def _get_adjusted_number_of_labels(self):
        return self._vtk_obj.GetAdjustedNumberOfLabels()
    adjusted_number_of_labels = traits.Property(_get_adjusted_number_of_labels, help=\
        """
        Set/Get the flag that controls whether the labels and ticks are
        adjusted for "nice" numerical values to make it easier to read
        the labels. The adjustment is based in the Range instance
        variable. Call get_adjusted_range and get_adjusted_number_of_labels to
        get the adjusted range and number of labels.
        """
    )

    def get_adjusted_range(self, *args):
        """
        V.get_adjusted_range(float, float)
        C++: virtual void GetAdjustedRange(double &_arg1, double &_arg2)
        V.get_adjusted_range([float, float])
        C++: virtual void GetAdjustedRange(double _arg[2])
        Set/Get the flag that controls whether the labels and ticks are
        adjusted for "nice" numerical values to make it easier to read
        the labels. The adjustment is based in the Range instance
        variable. Call get_adjusted_range and get_adjusted_number_of_labels to
        get the adjusted range and number of labels.
        """
        ret = self._wrap_call(self._vtk_obj.GetAdjustedRange, *args)
        return ret

    def _get_point1_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Coordinate())
    point1_coordinate = traits.Property(_get_point1_coordinate, help=\
        """
        Specify the position of the first point defining the axis. Note:
        backward compatibility only, use Actor2D's Position instead.
        """
    )

    def _get_point2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Coordinate())
    point2_coordinate = traits.Property(_get_point2_coordinate, help=\
        """
        Specify the position of the second point defining the axis. Note
        that the order from Point1 to Point2 controls which side the tick
        marks are drawn on (ticks are drawn on the right, if visible).
        Note: backward compatibility only, use Actor2D's Position2
        instead.
        """
    )

    def compute_range(self, *args):
        """
        V.compute_range([float, float], [float, float], int, int, float)
        C++: static void ComputeRange(double inRange[2],
            double outRange[2], int inNumTicks, int &outNumTicks,
            double &interval)
        This method computes the range of the axis given an input range.
        It also computes the number of tick marks given a suggested
        number. (The number of tick marks includes end ticks as well.)
        The number of tick marks computed (in conjunction with the output
        range) will yield "nice" tick values. For example, if the input
        range is (0.25,96.7) and the number of ticks requested is 10, the
        output range will be (0,100) with the number of computed ticks to
        11 to yield tick values of (0,10,20,...,100).
        """
        ret = self._wrap_call(self._vtk_obj.ComputeRange, *args)
        return ret

    def set_point1(self, *args):
        """
        V.set_point1([float, float])
        C++: virtual void SetPoint1(double x[2])
        V.set_point1(float, float)
        C++: virtual void SetPoint1(double x, double y)
        Specify the position of the first point defining the axis. Note:
        backward compatibility only, use Actor2D's Position instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1, *args)
        return ret

    def set_point2(self, *args):
        """
        V.set_point2([float, float])
        C++: virtual void SetPoint2(double x[2])
        V.set_point2(float, float)
        C++: virtual void SetPoint2(double x, double y)
        Specify the position of the second point defining the axis. Note
        that the order from Point1 to Point2 controls which side the tick
        marks are drawn on (ticks are drawn on the right, if visible).
        Note: backward compatibility only, use Actor2D's Position2
        instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2, *args)
        return ret

    _updateable_traits_ = \
    (('font_factor', 'GetFontFactor'), ('adjust_labels',
    'GetAdjustLabels'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('title_visibility', 'GetTitleVisibility'),
    ('size_font_relative_to_axis', 'GetSizeFontRelativeToAxis'),
    ('tick_visibility', 'GetTickVisibility'), ('dragable', 'GetDragable'),
    ('tick_length', 'GetTickLength'), ('visibility', 'GetVisibility'),
    ('height', 'GetHeight'), ('label_factor', 'GetLabelFactor'),
    ('minor_tick_length', 'GetMinorTickLength'), ('axis_visibility',
    'GetAxisVisibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('layer_number', 'GetLayerNumber'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('title_position', 'GetTitlePosition'),
    ('label_format', 'GetLabelFormat'), ('number_of_labels',
    'GetNumberOfLabels'), ('title', 'GetTitle'), ('label_visibility',
    'GetLabelVisibility'), ('debug', 'GetDebug'), ('tick_offset',
    'GetTickOffset'), ('position2', 'GetPosition2'), ('range',
    'GetRange'), ('number_of_minor_ticks', 'GetNumberOfMinorTicks'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('pickable', 'GetPickable'), ('width', 'GetWidth'))
    
    _full_traitnames_list_ = \
    (['adjust_labels', 'axis_visibility', 'debug', 'dragable',
    'global_warning_display', 'label_visibility', 'pickable',
    'size_font_relative_to_axis', 'tick_visibility', 'title_visibility',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'font_factor', 'height', 'label_factor',
    'label_format', 'layer_number', 'minor_tick_length',
    'number_of_labels', 'number_of_minor_ticks', 'position', 'position2',
    'range', 'render_time_multiplier', 'tick_length', 'tick_offset',
    'title', 'title_position', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AxisActor2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AxisActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['adjust_labels', 'axis_visibility',
            'label_visibility', 'size_font_relative_to_axis', 'tick_visibility',
            'title_visibility', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'font_factor',
            'height', 'label_factor', 'label_format', 'layer_number',
            'minor_tick_length', 'number_of_labels', 'number_of_minor_ticks',
            'position', 'position2', 'range', 'render_time_multiplier',
            'tick_length', 'tick_offset', 'title', 'title_position', 'width']),
            title='Edit AxisActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AxisActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

