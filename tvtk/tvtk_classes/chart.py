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

from tvtk.tvtk_classes.context_item import ContextItem


class Chart(ContextItem):
    """
    Chart - Factory class for drawing 2d charts
    
    Superclass: ContextItem
    
    This defines the interface for a chart.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChart, obj, update, **traits)
    
    auto_size = traits.Bool(True, help=\
        """
        Set/get whether the chart should automatically resize to fill the
        current render window. Default is true.
        """
    )
    def _auto_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoSize,
                        self.auto_size)

    title = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Get/set the title text of the chart.
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    geometry = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometry,
                        self.geometry)

    def get_action_to_button(self, *args):
        """
        V.get_action_to_button(int) -> int
        C++: virtual int GetActionToButton(int action)
        Get the mouse button associated with the supplied action. The
        mouse button enum is from ContextMouseEvent, and the action
        enum is from Chart.
        """
        ret = self._wrap_call(self._vtk_obj.GetActionToButton, *args)
        return ret

    def set_action_to_button(self, *args):
        """
        V.set_action_to_button(int, int)
        C++: virtual void SetActionToButton(int action, int button)
        Assign action types to mouse buttons. Available action types are
        PAN, ZOOM and SELECT in the chart enum, the default assigns the
        LEFT_BUTTON to PAN, MIDDLE_BUTTON to ZOOM and RIGHT_BUTTON to
        SELECT. Valid mouse enums are in the ContextMouseEvent class.
        
        Note that only one mouse button can be assigned to each action,
        an action will have -1 (invalid button) assigned if it had the
        same button as the one assigned to a different action.
        """
        ret = self._wrap_call(self._vtk_obj.SetActionToButton, *args)
        return ret

    def _get_annotation_link(self):
        return wrap_vtk(self._vtk_obj.GetAnnotationLink())
    def _set_annotation_link(self, arg):
        old_val = self._get_annotation_link()
        self._wrap_call(self._vtk_obj.SetAnnotationLink,
                        deref_vtk(arg))
        self.trait_property_changed('annotation_link', old_val, arg)
    annotation_link = traits.Property(_get_annotation_link, _set_annotation_link, help=\
        """
        Get the AnnotationLink for the chart.
        """
    )

    show_legend = traits.Bool(False, help=\
        """
        Set/get whether the chart should draw a legend.
        """
    )
    def _show_legend_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowLegend,
                        self.show_legend)

    point1 = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    def get_axis(self, *args):
        """
        V.get_axis(int) -> Axis
        C++: virtual Axis *GetAxis(int axisIndex)
        Get the axis specified by axis_index. 0 is x, 1 is y. This should
        probably be improved either using a string or enum to select the
        axis.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxis, *args)
        return wrap_vtk(ret)

    def _get_number_of_axes(self):
        return self._vtk_obj.GetNumberOfAxes()
    number_of_axes = traits.Property(_get_number_of_axes, help=\
        """
        Get the number of axes in the current chart.
        """
    )

    def _get_number_of_plots(self):
        return self._vtk_obj.GetNumberOfPlots()
    number_of_plots = traits.Property(_get_number_of_plots, help=\
        """
        Get the number of plots the chart contains.
        """
    )

    def get_plot(self, *args):
        """
        V.get_plot(int) -> Plot
        C++: virtual Plot *GetPlot(IdType index)
        Get the plot at the specified index, returns null if the index is
        invalid.
        """
        ret = self._wrap_call(self._vtk_obj.GetPlot, *args)
        return wrap_vtk(ret)

    def _get_title_properties(self):
        return wrap_vtk(self._vtk_obj.GetTitleProperties())
    title_properties = traits.Property(_get_title_properties, help=\
        """
        Get the TextProperty that governs how the chart title is
        displayed.
        """
    )

    def add_plot(self, *args):
        """
        V.add_plot(int) -> Plot
        C++: virtual Plot *AddPlot(int type)
        V.add_plot(Plot) -> int
        C++: virtual IdType AddPlot(Plot *plot)
        Add a plot to the chart, defaults to using the name of the y
        column
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddPlot, *my_args)
        return wrap_vtk(ret)

    def clear_plots(self):
        """
        V.clear_plots()
        C++: virtual void ClearPlots()
        Remove all plots from the chart.
        """
        ret = self._vtk_obj.ClearPlots()
        return ret
        

    def recalculate_bounds(self):
        """
        V.recalculate_bounds()
        C++: virtual void RecalculateBounds()
        Request that the chart recalculates the range of its axes.
        Especially useful in applications after the parameters of plots
        have been modified.
        """
        ret = self._vtk_obj.RecalculateBounds()
        return ret
        

    def remove_plot(self, *args):
        """
        V.remove_plot(int) -> bool
        C++: virtual bool RemovePlot(IdType index)
        Remove the plot at the specified index, returns true if
        successful, false if the index was invalid.
        """
        ret = self._wrap_call(self._vtk_obj.RemovePlot, *args)
        return ret

    def remove_plot_instance(self, *args):
        """
        V.remove_plot_instance(Plot) -> bool
        C++: virtual bool RemovePlotInstance(Plot *plot)
        Remove the given plot.  Returns true if successful, false if the
        plot was not contained in this chart.  Note, the base
        implementation of this method performs a linear search to locate
        the plot.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemovePlotInstance, *my_args)
        return ret

    def set_borders(self, *args):
        """
        V.set_borders(int, int, int, int)
        C++: void SetBorders(int left, int bottom, int right, int top)
        Set/get the borders of the chart (space in pixels around the
        chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetBorders, *args)
        return ret

    def set_bottom_border(self, *args):
        """
        V.set_bottom_border(int)
        C++: void SetBottomBorder(int border)
        Set/get the borders of the chart (space in pixels around the
        chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetBottomBorder, *args)
        return ret

    def set_left_border(self, *args):
        """
        V.set_left_border(int)
        C++: void SetLeftBorder(int border)
        Set/get the borders of the chart (space in pixels around the
        chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetLeftBorder, *args)
        return ret

    def set_right_border(self, *args):
        """
        V.set_right_border(int)
        C++: void SetRightBorder(int border)
        Set/get the borders of the chart (space in pixels around the
        chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetRightBorder, *args)
        return ret

    def set_top_border(self, *args):
        """
        V.set_top_border(int)
        C++: void SetTopBorder(int border)
        Set/get the borders of the chart (space in pixels around the
        chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetTopBorder, *args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('point1', 'GetPoint1'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('title',
    'GetTitle'), ('geometry', 'GetGeometry'), ('debug', 'GetDebug'),
    ('point2', 'GetPoint2'), ('visible', 'GetVisible'), ('show_legend',
    'GetShowLegend'), ('reference_count', 'GetReferenceCount'),
    ('auto_size', 'GetAutoSize'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'auto_size', 'geometry',
    'opacity', 'point1', 'point2', 'show_legend', 'title', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Chart, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Chart properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['auto_size', 'geometry', 'opacity', 'point1',
            'point2', 'show_legend', 'title', 'visible']),
            title='Edit Chart properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Chart properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

