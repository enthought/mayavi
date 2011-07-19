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


class Plot(ContextItem):
    """
    Plot - Abstract class for 2d plots.
    
    Superclass: ContextItem
    
    The base class for all plot types used in Chart derived charts.
    
    See Also:
    
    PlotPoints PlotLine PlotBar Chart ChartXY
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlot, obj, update, **traits)
    
    use_index_for_x_series = traits.Bool(False, help=\
        """
        Use the Y array index for the X value. If true any X column
        setting will be ignored, and the X values will simply be the
        index of the Y column.
        """
    )
    def _use_index_for_x_series_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseIndexForXSeries,
                        self.use_index_for_x_series)

    def _get_selection(self):
        return wrap_vtk(self._vtk_obj.GetSelection())
    def _set_selection(self, arg):
        old_val = self._get_selection()
        my_arg = deref_array([arg], [['vtkIdTypeArray']])
        self._wrap_call(self._vtk_obj.SetSelection,
                        my_arg[0])
        self.trait_property_changed('selection', old_val, arg)
    selection = traits.Property(_get_selection, _set_selection, help=\
        """
        
        """
    )

    def _get_y_axis(self):
        return wrap_vtk(self._vtk_obj.GetYAxis())
    def _set_y_axis(self, arg):
        old_val = self._get_y_axis()
        self._wrap_call(self._vtk_obj.SetYAxis,
                        deref_vtk(arg))
        self.trait_property_changed('y_axis', old_val, arg)
    y_axis = traits.Property(_get_y_axis, _set_y_axis, help=\
        """
        Get/set the Y axis associated with this plot.
        """
    )

    def get_color(self, *args):
        """
        V.get_color([float, float, float])
        C++: virtual void GetColor(double rgb[3])
        V.get_color([, , ])
        C++: void GetColor(unsigned char rgb[3])
        Set the plot color
        """
        ret = self._wrap_call(self._vtk_obj.GetColor, *args)
        return ret

    def set_color(self, *args):
        """
        V.set_color(, , , )
        C++: virtual void SetColor(unsigned char r, unsigned char g,
            unsigned char b, unsigned char a)
        V.set_color(float, float, float)
        C++: virtual void SetColor(double r, double g, double b)
        Set the plot color
        """
        ret = self._wrap_call(self._vtk_obj.SetColor, *args)
        return ret

    def _get_labels(self):
        return wrap_vtk(self._vtk_obj.GetLabels())
    def _set_labels(self, arg):
        old_val = self._get_labels()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetLabels,
                        my_arg[0])
        self.trait_property_changed('labels', old_val, arg)
    labels = traits.Property(_get_labels, _set_labels, help=\
        """
        Get the plot labels.
        """
    )

    label = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Set a single label on this plot.
        """
    )
    def _label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabel,
                        self.label)

    width = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Set the width of the line.
        """
    )
    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

    def _get_x_axis(self):
        return wrap_vtk(self._vtk_obj.GetXAxis())
    def _set_x_axis(self, arg):
        old_val = self._get_x_axis()
        self._wrap_call(self._vtk_obj.SetXAxis,
                        deref_vtk(arg))
        self.trait_property_changed('x_axis', old_val, arg)
    x_axis = traits.Property(_get_x_axis, _set_x_axis, help=\
        """
        Get/set the X axis associated with this plot.
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self):
        """
        V.get_input() -> Table
        C++: virtual Table *GetInput()
        Get the input table used by the plot.
        """
        ret = wrap_vtk(self._vtk_obj.GetInput())
        return ret
        

    def set_input(self, *args):
        """
        V.set_input(Table)
        C++: virtual void SetInput(Table *table)
        V.set_input(Table, string, string)
        C++: virtual void SetInput(Table *table,
            const StdString &xColumn, const StdString &yColumn)
        V.set_input(Table, int, int)
        C++: void SetInput(Table *table, IdType xColumn,
            IdType yColumn)
        This is a convenience function to set the input table and the x,
        y column for the plot.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def get_property(self, *args):
        """
        V.get_property(string) -> Variant
        C++: virtual Variant GetProperty(const StdString &property)
        A General setter/getter that should be overridden. It can
        silently drop options, case is important
        """
        ret = self._wrap_call(self._vtk_obj.GetProperty, *args)
        return wrap_vtk(ret)

    def set_property(self, *args):
        """
        V.set_property(string, Variant)
        C++: virtual void SetProperty(const StdString &property,
            const Variant &var)
        A General setter/getter that should be overridden. It can
        silently drop options, case is important
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetProperty, *my_args)
        return ret

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float])
        C++: virtual void GetBounds(double bounds[4])
        Get the bounds for this plot as (Xmin, Xmax, Ymin, Ymax).
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def _get_brush(self):
        return wrap_vtk(self._vtk_obj.GetBrush())
    brush = traits.Property(_get_brush, help=\
        """
        Get a pointer to the Brush object that controls the was this
        plot fills shapes.
        """
    )

    def _get_data(self):
        return wrap_vtk(self._vtk_obj.GetData())
    data = traits.Property(_get_data, help=\
        """
        Get the data object that the plot will draw.
        """
    )

    def _get_number_of_labels(self):
        return self._vtk_obj.GetNumberOfLabels()
    number_of_labels = traits.Property(_get_number_of_labels, help=\
        """
        Get the number of labels associated with this plot.
        """
    )

    def _get_pen(self):
        return wrap_vtk(self._vtk_obj.GetPen())
    pen = traits.Property(_get_pen, help=\
        """
        Get a pointer to the Pen object that controls the was this
        plot draws lines.
        """
    )

    def set_input_array(self, *args):
        """
        V.set_input_array(int, string)
        C++: virtual void SetInputArray(int index,
            const StdString &name)
        Convenience function to set the input arrays. For most plots
        index 0 is the x axis, and index 1 is the y axis. The name is the
        name of the column in the Table.
        """
        ret = self._wrap_call(self._vtk_obj.SetInputArray, *args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('width', 'GetWidth'), ('label', 'GetLabel'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'label', 'opacity',
    'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Plot, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Plot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['label', 'opacity', 'use_index_for_x_series',
            'visible', 'width']),
            title='Edit Plot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Plot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

