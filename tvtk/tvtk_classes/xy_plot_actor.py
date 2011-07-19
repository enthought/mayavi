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


class XYPlotActor(Actor2D):
    """
    XYPlotActor - generate an x-y plot from input dataset(s) or field
    data
    
    Superclass: Actor2D
    
    XYPlotActor creates an x-y plot of data from one or more input
    data sets or field data. The class plots dataset scalar values
    (y-axis) against the points (x-axis). The x-axis values are generated
    by taking the point ids, computing a cumulative arc length, or a
    normalized arc length. More than one input data set can be specified
    to generate multiple plots. Alternatively, if field data is supplied
    as input, the class plots one component against another. (The user
    must specify which component to use as the x-axis and which for the
    y-axis.)
    
    To use this class to plot dataset(s), you must specify one or more
    input datasets containing scalar and point data.  You'll probably
    also want to invoke a method to control how the point coordinates are
    converted into x values (by default point ids are used).
    
    To use this class to plot field data, you must specify one or more
    input data objects with its associated field data. You'll also want
    to specify which component to use as the x-axis and which to use as
    the y-axis. Note that when plotting field data, the x and y values
    are used directly (i.e., there are no options to normalize the
    components).
    
    Once you've set up the plot, you'll want to position it.  The
    position_coordinate defines the lower-left location of the x-y plot
    (specified in normalized viewport coordinates) and the
    position2_coordinate define the upper-right corner. (Note: the
    position2_coordinate is relative to position_coordinate, so you can
    move the XYPlotActor around the viewport by setting just the
    position_coordinate.) The combination of the two position coordinates
    specifies a rectangle in which the plot will lie.
    
    Optional features include the ability to specify axes labels, label
    format and plot title. You can also manually specify the x and y plot
    ranges (by default they are computed automatically). The Border
    instance variable is used to create space between the boundary of the
    plot window (specified by position_coordinate and position2_coordinate)
    and the plot itself.
    
    The font property of the plot title can be modified through the
    title_text_property attribute. The font property of the axes titles and
    labels can be modified through the axis_title_text_property and
    axis_label_text_property attributes. You may also use the
    get_x_axis_actor2d or get_y_axis_actor2d methods to access each individual
    axis actor to modify their font properties. In the same way, the
    get_legend_box_actor method can be used to access the legend box actor
    to modify its font properties.
    
    There are several advanced features as well. You can assign per curve
    properties (such as color and a plot symbol). (Note that each input
    dataset and/or data object creates a single curve.) Another option is
    to add a plot legend that graphically indicates the correspondance
    between the curve, curve symbols, and the data source. You can also
    exchange the x and y axes if you prefer you plot orientation that
    way.
    
    Caveats:
    
    If you are interested in plotting something other than scalar data,
    you can use the vtk data shuffling filters (e.g.,
    AttributeDataToFieldDataFilter and
    FieldDataToAttributeDataFilter) to convert the data into scalar
    data and/or points.
    
    See Also:
    
    Actor2D TextMapper ScalarBarActor AxisActor2D
    CubeAxesActor2D AttributeDataToFieldDataFilter
    FieldDataToAttributeDataFilter TextProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXYPlotActor, obj, update, **traits)
    
    plot_curve_points = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _plot_curve_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlotCurvePoints,
                        self.plot_curve_points_)

    reverse_x_axis = tvtk_base.false_bool_trait(help=\
        """
        Normally the x-axis is plotted from minimum to maximum. Setting
        this instance variable causes the x-axis to be plotted from
        maximum to minimum. Note that boolean always applies to the
        x-axis even if exchange_axes is set.
        """
    )
    def _reverse_x_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseXAxis,
                        self.reverse_x_axis_)

    plot_lines = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _plot_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlotLines,
                        self.plot_lines_)

    exchange_axes = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable exchange of the x-y axes (i.e., what was x becomes
        y, and vice-versa). Exchanging axes affects the labeling as well.
        """
    )
    def _exchange_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExchangeAxes,
                        self.exchange_axes_)

    logx = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable plotting of Log of x-values.
        """
    )
    def _logx_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLogx,
                        self.logx_)

    adjust_title_position = tvtk_base.true_bool_trait(help=\
        """
        If true, the xyplot actor will adjust the position of the title
        automatically to be upper-middle. Default is true.
        """
    )
    def _adjust_title_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustTitlePosition,
                        self.adjust_title_position_)

    chart_box = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag that controls whether a box will be drawn/filled
        corresponding to the chart box.
        """
    )
    def _chart_box_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetChartBox,
                        self.chart_box_)

    show_reference_y_line = tvtk_base.false_bool_trait(help=\
        """
        Set/Get if the Y reference line is visible. hidden by default
        """
    )
    def _show_reference_y_line_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowReferenceYLine,
                        self.show_reference_y_line_)

    plot_curve_lines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _plot_curve_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlotCurveLines,
                        self.plot_curve_lines_)

    reverse_y_axis = tvtk_base.false_bool_trait(help=\
        """
        Normally the y-axis is plotted from minimum to maximum. Setting
        this instance variable causes the y-axis to be plotted from
        maximum to minimum. Note that boolean always applies to the
        y-axis even if exchange_axes is set.
        """
    )
    def _reverse_y_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseYAxis,
                        self.reverse_y_axis_)

    chart_border = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag that controls whether a box will be drawn/filled
        corresponding to the legend box.
        """
    )
    def _chart_border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetChartBorder,
                        self.chart_border_)

    show_reference_x_line = tvtk_base.false_bool_trait(help=\
        """
        Set/Get if the X reference line is visible. hidden by default
        """
    )
    def _show_reference_x_line_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowReferenceXLine,
                        self.show_reference_x_line_)

    legend = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable the creation of a legend. If on, the legend labels
        will be created automatically unless the per plot legend symbol
        has been set.
        """
    )
    def _legend_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLegend,
                        self.legend_)

    plot_points = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _plot_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlotPoints,
                        self.plot_points_)

    data_object_plot_mode = traits.Trait('columns',
    tvtk_base.TraitRevPrefixMap({'rows': 0, 'columns': 1}), help=\
        """
        Indicate whether to plot rows or columns. If plotting rows, then
        the dependent variables is taken from a specified row, versus
        rows (y).
        """
    )
    def _data_object_plot_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataObjectPlotMode,
                        self.data_object_plot_mode_)

    x_values = traits.Trait('index',
    tvtk_base.TraitRevPrefixMap({'normalized_arc_length': 2, 'index': 0, 'arc_length': 1, 'value': 3}), help=\
        """
        Specify how the independent (x) variable is computed from the
        points. The independent variable can be the scalar/point index
        (i.e., point id), the accumulated arc length along the points,
        the normalized arc length, or by component value. If plotting
        datasets (e.g., points), the value that is used is specified by
        the point_component ivar.  (Note: these methods also control how
        field data is plotted. Field data is usually plotted by value or
        index, if plotting length 1-dimensional length measures are
        used.)
        """
    )
    def _x_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXValues,
                        self.x_values_)

    number_of_x_minor_ticks = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of minor ticks in X or Y.
        """
    )
    def _number_of_x_minor_ticks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfXMinorTicks,
                        self.number_of_x_minor_ticks)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the x-y plot, and the title along the x and
        y axes.
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    glyph_size = traits.Trait(0.02, traits.Range(0.0, 0.20000000000000001, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls how big glyphs are in the plot.
        The number is expressed as a fraction of the length of the
        diagonal of the plot bounding box.
        """
    )
    def _glyph_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlyphSize,
                        self.glyph_size)

    y_label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the Y label.
        """
    )
    def _y_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYLabelFormat,
                        self.y_label_format)

    reference_x_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _reference_x_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReferenceXValue,
                        self.reference_x_value)

    def get_plot_symbol(self, *args):
        """
        V.get_plot_symbol(int) -> PolyData
        C++: PolyData *GetPlotSymbol(int i)"""
        ret = self._wrap_call(self._vtk_obj.GetPlotSymbol, *args)
        return wrap_vtk(ret)

    def set_plot_symbol(self, *args):
        """
        V.set_plot_symbol(int, PolyData)
        C++: void SetPlotSymbol(int i, PolyData *input)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlotSymbol, *my_args)
        return ret

    def get_data_object_x_component(self, *args):
        """
        V.get_data_object_x_component(int) -> int
        C++: int GetDataObjectXComponent(int i)
        Specify which component of the input data object to use as the
        independent variable for the ith input data object. (This ivar is
        ignored if plotting the index.) Note that the value is
        interpreted differently depending on data_object_plot_mode. If the
        mode is Rows, then the value of data_object_x_component is the row
        number; otherwise it's the column number.
        """
        ret = self._wrap_call(self._vtk_obj.GetDataObjectXComponent, *args)
        return ret

    def set_data_object_x_component(self, *args):
        """
        V.set_data_object_x_component(int, int)
        C++: void SetDataObjectXComponent(int i, int comp)
        Specify which component of the input data object to use as the
        independent variable for the ith input data object. (This ivar is
        ignored if plotting the index.) Note that the value is
        interpreted differently depending on data_object_plot_mode. If the
        mode is Rows, then the value of data_object_x_component is the row
        number; otherwise it's the column number.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataObjectXComponent, *args)
        return ret

    viewport_coordinate = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _viewport_coordinate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewportCoordinate,
                        self.viewport_coordinate)

    def get_plot_color(self, *args):
        """
        V.get_plot_color(int) -> (float, float, float)
        C++: double *GetPlotColor(int i)"""
        ret = self._wrap_call(self._vtk_obj.GetPlotColor, *args)
        return ret

    def set_plot_color(self, *args):
        """
        V.set_plot_color(int, float, float, float)
        C++: void SetPlotColor(int i, double r, double g, double b)
        V.set_plot_color(int, (float, float, float))
        C++: void SetPlotColor(int i, const double color[3])"""
        ret = self._wrap_call(self._vtk_obj.SetPlotColor, *args)
        return ret

    plot_label = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _plot_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlotLabel,
                        self.plot_label)

    y_title_position = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the position of the title of X or Y axis.
        """
    )
    def _y_title_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYTitlePosition,
                        self.y_title_position)

    legend_position = traits.Array(shape=(2,), value=(0.84999999999999998, 0.75), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _legend_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLegendPosition,
                        self.legend_position)

    x_title_position = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the position of the title of X or Y axis.
        """
    )
    def _x_title_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXTitlePosition,
                        self.x_title_position)

    adjust_y_labels = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the flag that controls whether the labels and ticks are
        adjusted for "nice" numerical values to make it easier to read
        the labels. The adjustment is based in the Range instance
        variable. Call get_adjusted_range and get_adjusted_number_of_labels to
        get the adjusted range and number of labels.
        """
    )
    def _adjust_y_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustYLabels,
                        self.adjust_y_labels)

    number_of_y_labels = traits.Trait(5, traits.Range(0, 50, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of annotation labels to show along the x and y
        axes. This values is a suggestion: the number of labels may vary
        depending on the particulars of the data. The convenience method
        set_number_of_lables() sets the number of x and y labels to the same
        value.
        """
    )
    def _number_of_y_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfYLabels,
                        self.number_of_y_labels)

    def _get_axis_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisTitleTextProperty())
    def _set_axis_title_text_property(self, arg):
        old_val = self._get_axis_title_text_property()
        self._wrap_call(self._vtk_obj.SetAxisTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('axis_title_text_property', old_val, arg)
    axis_title_text_property = traits.Property(_get_axis_title_text_property, _set_axis_title_text_property, help=\
        """
        Set/Get the title text property of all axes. Note that each axis
        can be controlled individually through the get_x/_y_axis_actor2d()
        methods.
        """
    )

    plot_coordinate = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _plot_coordinate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlotCoordinate,
                        self.plot_coordinate)

    x_range = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _x_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXRange,
                        self.x_range)

    adjust_title_position_mode = traits.Int(17428, enter_set=True, auto_set=False, help=\
        """
        If adjust_title_position is truem, the xyplot actor will adjust the
        position of the title automatically depending on the given mode,
        the mode is a combination of the Alignment flags. by default:
        XYPlotActor::AlignHCenter | XYPlotActor::Top |
        XYPlotActor::AlignAxisVCenter
        """
    )
    def _adjust_title_position_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustTitlePositionMode,
                        self.adjust_title_position_mode)

    x_title = traits.String(r"X Axis", enter_set=True, auto_set=False, help=\
        """
        Set/Get the title of the x-y plot, and the title along the x and
        y axes.
        """
    )
    def _x_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXTitle,
                        self.x_title)

    reference_y_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _reference_y_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReferenceYValue,
                        self.reference_y_value)

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

    legend_position2 = traits.Array(shape=(2,), value=(0.14999999999999999, 0.20000000000000001), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _legend_position2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLegendPosition2,
                        self.legend_position2)

    y_title = traits.String(r"Y Axis", enter_set=True, auto_set=False, help=\
        """
        Set/Get the title of the x-y plot, and the title along the x and
        y axes.
        """
    )
    def _y_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYTitle,
                        self.y_title)

    def _get_axis_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisLabelTextProperty())
    def _set_axis_label_text_property(self, arg):
        old_val = self._get_axis_label_text_property()
        self._wrap_call(self._vtk_obj.SetAxisLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('axis_label_text_property', old_val, arg)
    axis_label_text_property = traits.Property(_get_axis_label_text_property, _set_axis_label_text_property, help=\
        """
        Set/Get the labels text property of all axes. Note that each axis
        can be controlled individually through the get_x/_y_axis_actor2d()
        methods.
        """
    )

    adjust_x_labels = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the flag that controls whether the labels and ticks are
        adjusted for "nice" numerical values to make it easier to read
        the labels. The adjustment is based in the Range instance
        variable. Call get_adjusted_range and get_adjusted_number_of_labels to
        get the adjusted range and number of labels.
        """
    )
    def _adjust_x_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustXLabels,
                        self.adjust_x_labels)

    label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels . This sets
        both X and Y label formats. get_label_format() returns X label
        format.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    y_range = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _y_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYRange,
                        self.y_range)

    title_position = traits.Array(shape=(2,), value=(0.5, 0.90000000000000002), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _title_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitlePosition,
                        self.title_position)

    def get_point_component(self, *args):
        """
        V.get_point_component(int) -> int
        C++: int GetPointComponent(int i)
        If plotting points by value, which component to use to determine
        the value. This sets a value per each input dataset (i.e., the
        ith dataset).
        """
        ret = self._wrap_call(self._vtk_obj.GetPointComponent, *args)
        return ret

    def set_point_component(self, *args):
        """
        V.set_point_component(int, int)
        C++: void SetPointComponent(int i, int comp)
        If plotting points by value, which component to use to determine
        the value. This sets a value per each input dataset (i.e., the
        ith dataset).
        """
        ret = self._wrap_call(self._vtk_obj.SetPointComponent, *args)
        return ret

    number_of_x_labels = traits.Trait(5, traits.Range(0, 50, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of annotation labels to show along the x and y
        axes. This values is a suggestion: the number of labels may vary
        depending on the particulars of the data. The convenience method
        set_number_of_lables() sets the number of x and y labels to the same
        value.
        """
    )
    def _number_of_x_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfXLabels,
                        self.number_of_x_labels)

    number_of_y_minor_ticks = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of minor ticks in X or Y.
        """
    )
    def _number_of_y_minor_ticks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfYMinorTicks,
                        self.number_of_y_minor_ticks)

    x_label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the X label.
        """
    )
    def _x_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXLabelFormat,
                        self.x_label_format)

    border = traits.Trait(5, traits.Range(0, 50, enter_set=True, auto_set=False), help=\
        """
        Set/Get the spacing between the plot window and the plot. The
        value is specified in pixels.
        """
    )
    def _border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorder,
                        self.border)

    def get_data_object_y_component(self, *args):
        """
        V.get_data_object_y_component(int) -> int
        C++: int GetDataObjectYComponent(int i)
        Specify which component of the input data object to use as the
        dependent variable for the ith input data object. (This ivar is
        ignored if plotting the index.) Note that the value is
        interpreted differently depending on data_object_plot_mode. If the
        mode is Rows, then the value of data_object_y_component is the row
        number; otherwise it's the column number.
        """
        ret = self._wrap_call(self._vtk_obj.GetDataObjectYComponent, *args)
        return ret

    def set_data_object_y_component(self, *args):
        """
        V.set_data_object_y_component(int, int)
        C++: void SetDataObjectYComponent(int i, int comp)
        Specify which component of the input data object to use as the
        dependent variable for the ith input data object. (This ivar is
        ignored if plotting the index.) Note that the value is
        interpreted differently depending on data_object_plot_mode. If the
        mode is Rows, then the value of data_object_y_component is the row
        number; otherwise it's the column number.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataObjectYComponent, *args)
        return ret

    def _get_chart_box_property(self):
        return wrap_vtk(self._vtk_obj.GetChartBoxProperty())
    chart_box_property = traits.Property(_get_chart_box_property, help=\
        """
        Get the box Property2D.
        """
    )

    def _get_data_object_input_list(self):
        return wrap_vtk(self._vtk_obj.GetDataObjectInputList())
    data_object_input_list = traits.Property(_get_data_object_input_list, help=\
        """
        Return the list of inputs to this filter.
        """
    )

    def _get_glyph_source(self):
        return wrap_vtk(self._vtk_obj.GetGlyphSource())
    glyph_source = traits.Property(_get_glyph_source, help=\
        """
        Retrieve handles to the legend box and glyph source. This is
        useful if you would like to change the default behavior of the
        legend box or glyph source. For example, the default glyph can be
        changed from a line to a vertex plus line, etc.)
        """
    )

    def _get_input_list(self):
        return wrap_vtk(self._vtk_obj.GetInputList())
    input_list = traits.Property(_get_input_list, help=\
        """
        Return the list of inputs to this filter.
        """
    )

    def _get_legend_actor(self):
        return wrap_vtk(self._vtk_obj.GetLegendActor())
    legend_actor = traits.Property(_get_legend_actor, help=\
        """
        Retrieve handles to the legend box and glyph source. This is
        useful if you would like to change the default behavior of the
        legend box or glyph source. For example, the default glyph can be
        changed from a line to a vertex plus line, etc.)
        """
    )

    def _get_x_axis_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetXAxisActor2D())
    x_axis_actor2d = traits.Property(_get_x_axis_actor2d, help=\
        """
        Retrieve handles to the X and Y axis (so that you can set their
        text properties for example)
        """
    )

    def _get_y_axis_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetYAxisActor2D())
    y_axis_actor2d = traits.Property(_get_y_axis_actor2d, help=\
        """
        Retrieve handles to the X and Y axis (so that you can set their
        text properties for example)
        """
    )

    def add_data_object_input(self, *args):
        """
        V.add_data_object_input(DataObject)
        C++: void AddDataObjectInput(DataObject *in)
        Add a dataset to the list of data to append.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddDataObjectInput, *my_args)
        return ret

    def add_input(self, *args):
        """
        V.add_input(DataSet, string, int)
        C++: void AddInput(DataSet *in, const char *arrayName,
            int component)
        V.add_input(DataSet)
        C++: void AddInput(DataSet *in)
        Add a dataset to the list of data to append. The array name
        specifies which point array to plot. The array must be a
        DataArray subclass, i.e. a numeric array. If the array name is
        NULL, then the default scalars are used.  The array can have
        multiple components, but only the first component is ploted.
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    def is_in_plot(self, *args):
        """
        V.is_in_plot(Viewport, float, float) -> int
        C++: int IsInPlot(Viewport *viewport, double u, double v)
        Is the specified viewport position within the plot area (as
        opposed to the region used by the plot plus the labels)?
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsInPlot, *my_args)
        return ret

    def plot_to_viewport_coordinate(self, *args):
        """
        V.plot_to_viewport_coordinate(Viewport, float, float)
        C++: void PlotToViewportCoordinate(Viewport *viewport,
            double &u, double &v)
        V.plot_to_viewport_coordinate(Viewport)
        C++: void PlotToViewportCoordinate(Viewport *viewport)
        Given a plot coordinate, return the viewpoint position
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PlotToViewportCoordinate, *my_args)
        return ret

    def remove_all_inputs(self):
        """
        V.remove_all_inputs()
        C++: void RemoveAllInputs()
        This removes all of the data set inputs, but does not change the
        data object inputs.
        """
        old_val = self._get_input()
        ret = self._vtk_obj.RemoveAllInputs()
        self.trait_property_changed('input', old_val, self._get_input())
        return ret
        

    def remove_data_object_input(self, *args):
        """
        V.remove_data_object_input(DataObject)
        C++: void RemoveDataObjectInput(DataObject *in)
        Remove a dataset from the list of data to append.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveDataObjectInput, *my_args)
        return ret

    def remove_input(self, *args):
        """
        V.remove_input(DataSet, string, int)
        C++: void RemoveInput(DataSet *in, const char *arrayName,
            int component)
        V.remove_input(DataSet)
        C++: void RemoveInput(DataSet *in)
        Remove a dataset from the list of data to append.
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    def set_number_of_labels(self, *args):
        """
        V.set_number_of_labels(int)
        C++: void SetNumberOfLabels(int num)
        Set/Get the number of annotation labels to show along the x and y
        axes. This values is a suggestion: the number of labels may vary
        depending on the particulars of the data. The convenience method
        set_number_of_lables() sets the number of x and y labels to the same
        value.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfLabels, *args)
        return ret

    def set_plot_range(self, *args):
        """
        V.set_plot_range(float, float, float, float)
        C++: void SetPlotRange(double xmin, double ymin, double xmax,
            double ymax)
        Set the plot range (range of independent and dependent variables)
        to plot. Data outside of the range will be clipped. If the plot
        range of either the x or y variables is set to (v1,v2), where v1
        == v2, then the range will be computed automatically. Note that
        the x-range values should be consistent with the way the
        independent variable is created (via INDEX, DISTANCE, or
        ARC_LENGTH).
        """
        ret = self._wrap_call(self._vtk_obj.SetPlotRange, *args)
        return ret

    def viewport_to_plot_coordinate(self, *args):
        """
        V.viewport_to_plot_coordinate(Viewport, float, float)
        C++: void ViewportToPlotCoordinate(Viewport *viewport,
            double &u, double &v)
        V.viewport_to_plot_coordinate(Viewport)
        C++: void ViewportToPlotCoordinate(Viewport *viewport)
        Given a position within the viewport used by the plot, return the
        the plot coordinates (XAxis value, YAxis value)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ViewportToPlotCoordinate, *my_args)
        return ret

    _updateable_traits_ = \
    (('show_reference_x_line', 'GetShowReferenceXLine'),
    ('data_object_plot_mode', 'GetDataObjectPlotMode'),
    ('adjust_y_labels', 'GetAdjustYLabels'), ('y_title', 'GetYTitle'),
    ('dragable', 'GetDragable'), ('logx', 'GetLogx'), ('height',
    'GetHeight'), ('legend_position', 'GetLegendPosition'),
    ('reverse_x_axis', 'GetReverseXAxis'), ('y_label_format',
    'GetYLabelFormat'), ('x_values', 'GetXValues'), ('chart_box',
    'GetChartBox'), ('border', 'GetBorder'), ('x_title_position',
    'GetXTitlePosition'), ('plot_curve_points', 'GetPlotCurvePoints'),
    ('x_title', 'GetXTitle'), ('layer_number', 'GetLayerNumber'),
    ('title_position', 'GetTitlePosition'), ('title', 'GetTitle'),
    ('label_format', 'GetLabelFormat'), ('reverse_y_axis',
    'GetReverseYAxis'), ('glyph_size', 'GetGlyphSize'),
    ('plot_coordinate', 'GetPlotCoordinate'), ('legend', 'GetLegend'),
    ('viewport_coordinate', 'GetViewportCoordinate'), ('width',
    'GetWidth'), ('chart_border', 'GetChartBorder'), ('reference_x_value',
    'GetReferenceXValue'), ('reference_y_value', 'GetReferenceYValue'),
    ('number_of_x_labels', 'GetNumberOfXLabels'), ('x_range',
    'GetXRange'), ('allocated_render_time', 'GetAllocatedRenderTime'),
    ('show_reference_y_line', 'GetShowReferenceYLine'),
    ('adjust_title_position_mode', 'GetAdjustTitlePositionMode'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'), ('plot_lines',
    'GetPlotLines'), ('y_title_position', 'GetYTitlePosition'),
    ('plot_points', 'GetPlotPoints'), ('x_label_format',
    'GetXLabelFormat'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('number_of_y_minor_ticks',
    'GetNumberOfYMinorTicks'), ('y_range', 'GetYRange'), ('use_bounds',
    'GetUseBounds'), ('pickable', 'GetPickable'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('legend_position2', 'GetLegendPosition2'), ('exchange_axes',
    'GetExchangeAxes'), ('number_of_y_labels', 'GetNumberOfYLabels'),
    ('plot_label', 'GetPlotLabel'), ('adjust_x_labels',
    'GetAdjustXLabels'), ('number_of_x_minor_ticks',
    'GetNumberOfXMinorTicks'), ('position2', 'GetPosition2'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('adjust_title_position', 'GetAdjustTitlePosition'),
    ('plot_curve_lines', 'GetPlotCurveLines'))
    
    _full_traitnames_list_ = \
    (['adjust_title_position', 'chart_border', 'chart_box', 'debug',
    'dragable', 'exchange_axes', 'global_warning_display', 'legend',
    'logx', 'pickable', 'plot_curve_lines', 'plot_curve_points',
    'plot_lines', 'plot_points', 'reverse_x_axis', 'reverse_y_axis',
    'show_reference_x_line', 'show_reference_y_line', 'use_bounds',
    'visibility', 'data_object_plot_mode', 'x_values',
    'adjust_title_position_mode', 'adjust_x_labels', 'adjust_y_labels',
    'allocated_render_time', 'border', 'estimated_render_time',
    'glyph_size', 'height', 'label_format', 'layer_number',
    'legend_position', 'legend_position2', 'number_of_x_labels',
    'number_of_x_minor_ticks', 'number_of_y_labels',
    'number_of_y_minor_ticks', 'plot_coordinate', 'plot_label',
    'position', 'position2', 'reference_x_value', 'reference_y_value',
    'render_time_multiplier', 'title', 'title_position',
    'viewport_coordinate', 'width', 'x_label_format', 'x_range',
    'x_title', 'x_title_position', 'y_label_format', 'y_range', 'y_title',
    'y_title_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XYPlotActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XYPlotActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['adjust_title_position', 'chart_border', 'chart_box',
            'exchange_axes', 'legend', 'logx', 'plot_curve_lines',
            'plot_curve_points', 'plot_lines', 'plot_points', 'reverse_x_axis',
            'reverse_y_axis', 'show_reference_x_line', 'show_reference_y_line',
            'use_bounds', 'visibility'], ['data_object_plot_mode', 'x_values'],
            ['adjust_title_position_mode', 'adjust_x_labels', 'adjust_y_labels',
            'allocated_render_time', 'border', 'estimated_render_time',
            'glyph_size', 'height', 'label_format', 'layer_number',
            'legend_position', 'legend_position2', 'number_of_x_labels',
            'number_of_x_minor_ticks', 'number_of_y_labels',
            'number_of_y_minor_ticks', 'plot_coordinate', 'plot_label',
            'position', 'position2', 'reference_x_value', 'reference_y_value',
            'render_time_multiplier', 'title', 'title_position',
            'viewport_coordinate', 'width', 'x_label_format', 'x_range',
            'x_title', 'x_title_position', 'y_label_format', 'y_range', 'y_title',
            'y_title_position']),
            title='Edit XYPlotActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XYPlotActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

