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

from tvtk.tvtk_classes.actor import Actor


class AxisActor(Actor):
    """
    AxisActor - Create an axis with tick marks and labels
    
    Superclass: Actor
    
    AxisActor creates an axis with tick marks, labels, and/or a title,
    depending on the particular instance variable settings. It is assumed
    that the axes is part of a bounding box and is orthoganal to one of
    the coordinate axes.  To use this class, you typically specify two
    points defining the start and end points of the line (xyz definition
    using Coordinate class), the axis type (X, Y or Z), the axis
    location in relation to the bounding box, the bounding box, the
    number of labels, and the data range (min,max). You can also control
    what parts of the axis are visible including the line, the tick
    marks, the labels, and the title. It is also possible to control
    gridlines, and specifiy on which 'side' the tickmarks are drawn
    (again with respect to the underlying assumed bounding box). You can
    also specify the label format (a printf style format).
    
    This class decides how to locate the labels, and how to create
    reasonable tick marks and labels.
    
    Labels follow the camera so as to be legible from any viewpoint.
    
    The instance variables Point1 and Point2 are instances of
    Coordinate. All calculations and references are in World
    Coordinates.
    
    Notes:
    
    This class was adapted from a 2d version created by Hank Childs
    called HankAxisActor2D.
    
    See Also:
    
    Actor VectorText PolyDataMapper AxisActor2D Coordinate
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxisActor, obj, update, **traits)
    
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

    draw_gridlines = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether gridlines should be drawn.
        """
    )
    def _draw_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawGridlines,
                        self.draw_gridlines_)

    minor_ticks_visible = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag that controls whether the minor ticks are
        visible.
        """
    )
    def _minor_ticks_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorTicksVisible,
                        self.minor_ticks_visible_)

    axis_type = traits.Trait('x',
    tvtk_base.TraitRevPrefixMap({'y': 1, 'x': 0, 'z': 2}), help=\
        """
        Set/Get the type of this axis.
        """
    )
    def _axis_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisType,
                        self.axis_type_)

    tick_location = traits.Trait('inside',
    tvtk_base.TraitRevPrefixMap({'both': 2, 'inside': 0, 'outside': 1}), help=\
        """
        Set/Get the location of the ticks.
        """
    )
    def _tick_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickLocation,
                        self.tick_location_)

    axis_position = traits.Trait('min_min',
    tvtk_base.TraitRevPrefixMap({'max_min': 3, 'min_max': 1, 'max_max': 2, 'min_min': 0}), help=\
        """
        Set/Get the position of this axis (in relation to an an assumed
        bounding box).  For an x-type axis, MINMIN corresponds to the
        x-edge in the bounding box where Y values are minimum and Z
        values are minimum. For a y-type axis, MAXMIN corresponds to the
        y-edge where X values are maximum and Z values are minimum.
        """
    )
    def _axis_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisPosition,
                        self.axis_position_)

    major_tick_size = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the major tick marks
        """
    )
    def _major_tick_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMajorTickSize,
                        self.major_tick_size)

    delta_range_minor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points on
        the range and the delta values that determine their spacing. The
        range and the position need not be identical. ie the displayed
        values need not match the actual positions in 3d space.
        """
    )
    def _delta_range_minor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaRangeMinor,
                        self.delta_range_minor)

    gridline_y_length = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the length to use when drawing gridlines.
        """
    )
    def _gridline_y_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridlineYLength,
                        self.gridline_y_length)

    label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on the axis.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    delta_range_major = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points on
        the range and the delta values that determine their spacing. The
        range and the position need not be identical. ie the displayed
        values need not match the actual positions in 3d space.
        """
    )
    def _delta_range_major_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaRangeMajor,
                        self.delta_range_major)

    minor_start = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points,
        and the delta values that determine their spacing.
        """
    )
    def _minor_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorStart,
                        self.minor_start)

    gridline_z_length = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the length to use when drawing gridlines.
        """
    )
    def _gridline_z_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridlineZLength,
                        self.gridline_z_length)

    bounds = traits.Array(shape=(6,), value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set or get the bounds for this Actor as
        (Xmin,Xmax,Ymin,Ymax,Zmin,Zmax).
        """
    )
    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    delta_minor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points,
        and the delta values that determine their spacing.
        """
    )
    def _delta_minor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaMinor,
                        self.delta_minor)

    major_range_start = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points on
        the range and the delta values that determine their spacing. The
        range and the position need not be identical. ie the displayed
        values need not match the actual positions in 3d space.
        """
    )
    def _major_range_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMajorRangeStart,
                        self.major_range_start)

    range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Set/Get the camera for this axis.  The camera is used by the
        labels to 'follow' the camera and be legible from any viewpoint.
        """
    )

    minor_range_start = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points on
        the range and the delta values that determine their spacing. The
        range and the position need not be identical. ie the displayed
        values need not match the actual positions in 3d space.
        """
    )
    def _minor_range_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorRangeStart,
                        self.minor_range_start)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the axis actor,
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    gridline_x_length = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the length to use when drawing gridlines.
        """
    )
    def _gridline_x_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridlineXLength,
                        self.gridline_x_length)

    delta_major = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points,
        and the delta values that determine their spacing.
        """
    )
    def _delta_major_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaMajor,
                        self.delta_major)

    minor_tick_size = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the major tick marks
        """
    )
    def _minor_tick_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorTickSize,
                        self.minor_tick_size)

    major_start = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points,
        and the delta values that determine their spacing.
        """
    )
    def _major_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMajorStart,
                        self.major_start)

    def _get_point1_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Coordinate())
    point1_coordinate = traits.Property(_get_point1_coordinate, help=\
        """
        Specify the position of the first point defining the axis.
        """
    )

    def _get_point2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Coordinate())
    point2_coordinate = traits.Property(_get_point2_coordinate, help=\
        """
        Specify the position of the second point defining the axis.
        """
    )

    def build_axis(self, *args):
        """
        V.build_axis(Viewport, bool)
        C++: void BuildAxis(Viewport *viewport, bool)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BuildAxis, *my_args)
        return ret

    def compute_max_label_length(self, *args):
        """
        V.compute_max_label_length((float, float, float)) -> float
        C++: double ComputeMaxLabelLength(const double[3])"""
        ret = self._wrap_call(self._vtk_obj.ComputeMaxLabelLength, *args)
        return ret

    def compute_title_length(self, *args):
        """
        V.compute_title_length((float, float, float)) -> float
        C++: double ComputeTitleLength(const double[3])"""
        ret = self._wrap_call(self._vtk_obj.ComputeTitleLength, *args)
        return ret

    def render_translucent_geometry(self, *args):
        """
        V.render_translucent_geometry(Viewport) -> int
        C++: virtual int RenderTranslucentGeometry(Viewport *)
        Draw the axis.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderTranslucentGeometry, *my_args)
        return ret

    def set_label_scale(self, *args):
        """
        V.set_label_scale(float)
        C++: void SetLabelScale(const double)"""
        ret = self._wrap_call(self._vtk_obj.SetLabelScale, *args)
        return ret

    def set_labels(self, *args):
        """
        V.set_labels(StringArray)
        C++: void SetLabels(StringArray *labels)"""
        my_args = deref_array(args, [['vtkStringArray']])
        ret = self._wrap_call(self._vtk_obj.SetLabels, *my_args)
        return ret

    def set_point1(self, *args):
        """
        V.set_point1([float, float, float])
        C++: virtual void SetPoint1(double x[3])
        V.set_point1(float, float, float)
        C++: virtual void SetPoint1(double x, double y, double z)
        Specify the position of the first point defining the axis.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1, *args)
        return ret

    def set_point2(self, *args):
        """
        V.set_point2([float, float, float])
        C++: virtual void SetPoint2(double x[3])
        V.set_point2(float, float, float)
        C++: virtual void SetPoint2(double x, double y, double z)
        Specify the position of the second point defining the axis.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2, *args)
        return ret

    def set_title_scale(self, *args):
        """
        V.set_title_scale(float)
        C++: void SetTitleScale(const double)"""
        ret = self._wrap_call(self._vtk_obj.SetTitleScale, *args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('axis_visibility', 'GetAxisVisibility'),
    ('tick_location', 'GetTickLocation'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('minor_tick_size', 'GetMinorTickSize'),
    ('orientation', 'GetOrientation'), ('major_tick_size',
    'GetMajorTickSize'), ('dragable', 'GetDragable'), ('delta_major',
    'GetDeltaMajor'), ('minor_ticks_visible', 'GetMinorTicksVisible'),
    ('tick_visibility', 'GetTickVisibility'), ('visibility',
    'GetVisibility'), ('minor_start', 'GetMinorStart'), ('debug',
    'GetDebug'), ('minor_range_start', 'GetMinorRangeStart'),
    ('label_visibility', 'GetLabelVisibility'), ('major_range_start',
    'GetMajorRangeStart'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('axis_position', 'GetAxisPosition'),
    ('gridline_y_length', 'GetGridlineYLength'), ('use_bounds',
    'GetUseBounds'), ('delta_minor', 'GetDeltaMinor'), ('scale',
    'GetScale'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('title',
    'GetTitle'), ('label_format', 'GetLabelFormat'), ('draw_gridlines',
    'GetDrawGridlines'), ('axis_type', 'GetAxisType'), ('bounds',
    'GetBounds'), ('gridline_x_length', 'GetGridlineXLength'),
    ('major_start', 'GetMajorStart'), ('range', 'GetRange'),
    ('delta_range_minor', 'GetDeltaRangeMinor'), ('gridline_z_length',
    'GetGridlineZLength'), ('title_visibility', 'GetTitleVisibility'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('delta_range_major', 'GetDeltaRangeMajor'), ('pickable',
    'GetPickable'))
    
    _full_traitnames_list_ = \
    (['axis_visibility', 'debug', 'dragable', 'draw_gridlines',
    'global_warning_display', 'label_visibility', 'minor_ticks_visible',
    'pickable', 'tick_visibility', 'title_visibility', 'use_bounds',
    'visibility', 'axis_position', 'axis_type', 'tick_location',
    'allocated_render_time', 'bounds', 'delta_major', 'delta_minor',
    'delta_range_major', 'delta_range_minor', 'estimated_render_time',
    'gridline_x_length', 'gridline_y_length', 'gridline_z_length',
    'label_format', 'major_range_start', 'major_start', 'major_tick_size',
    'minor_range_start', 'minor_start', 'minor_tick_size', 'orientation',
    'origin', 'position', 'range', 'render_time_multiplier', 'scale',
    'title'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AxisActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AxisActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['axis_visibility', 'draw_gridlines',
            'label_visibility', 'minor_ticks_visible', 'tick_visibility',
            'title_visibility', 'use_bounds', 'visibility'], ['axis_position',
            'axis_type', 'tick_location'], ['allocated_render_time', 'bounds',
            'delta_major', 'delta_minor', 'delta_range_major',
            'delta_range_minor', 'estimated_render_time', 'gridline_x_length',
            'gridline_y_length', 'gridline_z_length', 'label_format',
            'major_range_start', 'major_start', 'major_tick_size',
            'minor_range_start', 'minor_start', 'minor_tick_size', 'orientation',
            'origin', 'position', 'range', 'render_time_multiplier', 'scale',
            'title']),
            title='Edit AxisActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AxisActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

