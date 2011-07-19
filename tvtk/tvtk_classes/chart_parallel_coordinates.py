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


class ChartParallelCoordinates(Chart):
    """
    ChartParallelCoordinates - Factory class for drawing 2d charts
    
    Superclass: Chart
    
    This defines the interface for a parallel coordinates chart.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartParallelCoordinates, obj, update, **traits)
    
    def get_plot(self, *args):
        """
        V.get_plot(int) -> Plot
        C++: virtual Plot *GetPlot(IdType index)
        Get the plot at the specified index, returns null if the index is
        invalid.
        """
        ret = self._wrap_call(self._vtk_obj.GetPlot, *args)
        return wrap_vtk(ret)

    def set_plot(self, *args):
        """
        V.set_plot(PlotParallelCoordinates)
        C++: virtual void SetPlot(PlotParallelCoordinates *plot)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlot, *my_args)
        return ret

    def get_column_visibility(self, *args):
        """
        V.get_column_visibility(string) -> bool
        C++: bool GetColumnVisibility(const StdString &name)
        Get the visibility of the specified column.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnVisibility, *args)
        return ret

    def set_column_visibility(self, *args):
        """
        V.set_column_visibility(string, bool)
        C++: void SetColumnVisibility(const StdString &name,
            bool visible)
        Set the visibility of the specified column.
        """
        ret = self._wrap_call(self._vtk_obj.SetColumnVisibility, *args)
        return ret

    def _get_visible_columns(self):
        return wrap_vtk(self._vtk_obj.GetVisibleColumns())
    visible_columns = traits.Property(_get_visible_columns, help=\
        """
        Get a list of the columns, and the order in which they are
        displayed.
        """
    )

    def set_column_visibility_all(self, *args):
        """
        V.set_column_visibility_all(bool)
        C++: void SetColumnVisibilityAll(bool visible)
        Set the visibility of all columns (true will make them all
        visible, false will remove all visible columns).
        """
        ret = self._wrap_call(self._vtk_obj.SetColumnVisibilityAll, *args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('title', 'GetTitle'), ('geometry',
    'GetGeometry'), ('debug', 'GetDebug'), ('visible', 'GetVisible'),
    ('show_legend', 'GetShowLegend'), ('point1', 'GetPoint1'), ('point2',
    'GetPoint2'), ('reference_count', 'GetReferenceCount'), ('auto_size',
    'GetAutoSize'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'auto_size', 'geometry',
    'opacity', 'point1', 'point2', 'show_legend', 'title', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartParallelCoordinates, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartParallelCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['auto_size', 'geometry', 'opacity', 'point1',
            'point2', 'show_legend', 'title', 'visible']),
            title='Edit ChartParallelCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartParallelCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

