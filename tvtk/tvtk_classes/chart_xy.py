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

from tvtk.tvtk_classes.chart import Chart


class ChartXY(Chart):
    """
    ChartXY - Factory class for drawing XY charts
    
    Superclass: Chart
    
    This class implements an XY chart.
    
    See Also:
    
    BarChartActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartXY, obj, update, **traits)
    
    draw_axes_at_origin = tvtk_base.false_bool_trait(help=\
        """
        If true then the axes will be drawn at the origin (scientific
        style).
        """
    )
    def _draw_axes_at_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawAxesAtOrigin,
                        self.draw_axes_at_origin_)

    auto_axes = tvtk_base.true_bool_trait(help=\
        """
        If true then the axes will be turned on and off depending upon
        whether any plots are in that corner. Defaults to true.
        """
    )
    def _auto_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAxes,
                        self.auto_axes_)

    def get_plot_corner(self, *args):
        """
        V.get_plot_corner(Plot) -> int
        C++: int GetPlotCorner(Plot *plot)
        Figure out which quadrant the plot is in.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlotCorner, *my_args)
        return ret

    def set_plot_corner(self, *args):
        """
        V.set_plot_corner(Plot, int)
        C++: void SetPlotCorner(Plot *plot, int corner)
        Figure out which quadrant the plot is in.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlotCorner, *my_args)
        return ret

    bar_width_fraction = traits.Float(0.800000011921, enter_set=True, auto_set=False, help=\
        """
        Set the width fraction for any bar charts drawn in this chart. It
        is assumed that all bar plots will use the same array for the X
        axis, and that this array is regularly spaced. The delta between
        the first two x values is used to calculated the width of the
        bars, and subdivided between each bar. The default value is 0.8,
        1.0 would lead to bars that touch.
        """
    )
    def _bar_width_fraction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBarWidthFraction,
                        self.bar_width_fraction)

    hidden_axis_border = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        Border size of the axes that are hidden (vtk_axis::_get_visible())
        """
    )
    def _hidden_axis_border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHiddenAxisBorder,
                        self.hidden_axis_border)

    def _get_legend(self):
        return wrap_vtk(self._vtk_obj.GetLegend())
    legend = traits.Property(_get_legend, help=\
        """
        Get the ChartLegend object that will be displayed by the
        chart.
        """
    )

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('hidden_axis_border',
    'GetHiddenAxisBorder'), ('geometry', 'GetGeometry'), ('debug',
    'GetDebug'), ('title', 'GetTitle'), ('visible', 'GetVisible'),
    ('show_legend', 'GetShowLegend'), ('bar_width_fraction',
    'GetBarWidthFraction'), ('point1', 'GetPoint1'), ('point2',
    'GetPoint2'), ('draw_axes_at_origin', 'GetDrawAxesAtOrigin'),
    ('reference_count', 'GetReferenceCount'), ('auto_size',
    'GetAutoSize'), ('auto_axes', 'GetAutoAxes'))
    
    _full_traitnames_list_ = \
    (['auto_axes', 'debug', 'draw_axes_at_origin',
    'global_warning_display', 'auto_size', 'bar_width_fraction',
    'geometry', 'hidden_axis_border', 'opacity', 'point1', 'point2',
    'show_legend', 'title', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartXY, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartXY properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_axes', 'draw_axes_at_origin'], [], ['auto_size',
            'bar_width_fraction', 'geometry', 'hidden_axis_border', 'opacity',
            'point1', 'point2', 'show_legend', 'title', 'visible']),
            title='Edit ChartXY properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartXY properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

