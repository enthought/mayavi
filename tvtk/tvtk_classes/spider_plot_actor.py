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


class SpiderPlotActor(Actor2D):
    """
    SpiderPlotActor - create a spider plot from input field
    
    Superclass: Actor2D
    
    SpiderPlotActor generates a spider plot from an input field (i.e.,
    DataObject). A spider plot represents N-dimensional data by using
    a set of N axes that originate from the center of a circle, and form
    the spokes of a wheel (like a spider web).  Each N-dimensional point
    is plotted as a polyline that forms a closed polygon; the vertices of
    the polygon are plotted against the radial axes.
    
    To use this class, you must specify an input data object. You'll
    probably also want to specify the position of the plot be setting the
    Position and Position2 instance variables, which define a rectangle
    in which the plot lies. Another important parameter is the
    independent_variables ivar, which tells the instance how to interpret
    the field data (independent variables as the rows or columns of the
    field). There are also many other instance variables that control the
    look of the plot includes its title and legend.
    
    Set the text property/attributes of the title and the labels through
    the TextProperty objects associated with these components.
    
    Caveats:
    
    Field data is not necessarily "rectangular" in shape. In these cases,
    some of the data may not be plotted.
    
    Field data can contain non-numeric arrays (i.e. arrays not subclasses
    of DataArray). Such arrays are skipped.
    
    See Also:
    
    ParallelCoordinatesActor XYPlotActor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSpiderPlotActor, obj, update, **traits)
    
    legend_visibility = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable the creation of a legend. If on, the legend labels
        will be created automatically unless the per plot legend symbol
        has been set.
        """
    )
    def _legend_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLegendVisibility,
                        self.legend_visibility_)

    label_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelVisibility,
                        self.label_visibility_)

    title_visibility = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable the display of a plot title.
        """
    )
    def _title_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleVisibility,
                        self.title_visibility_)

    independent_variables = traits.Trait('columns',
    tvtk_base.TraitRevPrefixMap({'rows': 1, 'columns': 0}), help=\
        """
        Specify whether to use the rows or columns as independent
        variables. If columns, then each row represents a separate point.
        If rows, then each column represents a separate point.
        """
    )
    def _independent_variables_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIndependentVariables,
                        self.independent_variables_)

    number_of_rings = traits.Trait(2, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of circumferential rings. If set to zero, then
        none will be shown; othewise the specified number will be shown.
        """
    )
    def _number_of_rings_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfRings,
                        self.number_of_rings)

    def get_axis_range(self, *args):
        """
        V.get_axis_range(int, [float, float])
        C++: void GetAxisRange(int i, double range[2])
        Specify the range of data on each radial axis. If not specified,
        then the range is computed automatically.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxisRange, *args)
        return ret

    def set_axis_range(self, *args):
        """
        V.set_axis_range(int, float, float)
        C++: void SetAxisRange(int i, double min, double max)
        V.set_axis_range(int, [float, float])
        C++: void SetAxisRange(int i, double range[2])
        Specify the range of data on each radial axis. If not specified,
        then the range is computed automatically.
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisRange, *args)
        return ret

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the spider plot.
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    axis_label = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the names of the radial spokes (i.e., the radial axes).
        If not specified, then an integer number is automatically
        generated.
        """
    )
    def _axis_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisLabel,
                        self.axis_label)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Enable/Disable the creation of a legend. If on, the legend labels
        will be created automatically unless the per plot legend symbol
        has been set.
        """
    )

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

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Get the input data object to this actor.
        """
    )

    def _get_legend_actor(self):
        return wrap_vtk(self._vtk_obj.GetLegendActor())
    legend_actor = traits.Property(_get_legend_actor, help=\
        """
        Retrieve handles to the legend box. This is useful if you would
        like to manually control the legend appearance.
        """
    )

    def set_plot_color(self, *args):
        """
        V.set_plot_color(int, float, float, float)
        C++: void SetPlotColor(int i, double r, double g, double b)
        V.set_plot_color(int, (float, float, float))
        C++: void SetPlotColor(int i, const double color[3])
        Specify colors for each plot. If not specified, they are
        automatically generated.
        """
        ret = self._wrap_call(self._vtk_obj.SetPlotColor, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'),
    ('title_visibility', 'GetTitleVisibility'), ('number_of_rings',
    'GetNumberOfRings'), ('visibility', 'GetVisibility'), ('height',
    'GetHeight'), ('reference_count', 'GetReferenceCount'),
    ('independent_variables', 'GetIndependentVariables'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('axis_label',
    'GetAxisLabel'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('layer_number', 'GetLayerNumber'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('title', 'GetTitle'), ('position2',
    'GetPosition2'), ('legend_visibility', 'GetLegendVisibility'),
    ('label_visibility', 'GetLabelVisibility'), ('width', 'GetWidth'),
    ('debug', 'GetDebug'), ('position', 'GetPosition'), ('pickable',
    'GetPickable'), ('dragable', 'GetDragable'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'label_visibility',
    'legend_visibility', 'pickable', 'title_visibility', 'use_bounds',
    'visibility', 'independent_variables', 'allocated_render_time',
    'axis_label', 'estimated_render_time', 'height', 'layer_number',
    'number_of_rings', 'position', 'position2', 'render_time_multiplier',
    'title', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SpiderPlotActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SpiderPlotActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['label_visibility', 'legend_visibility',
            'title_visibility', 'use_bounds', 'visibility'],
            ['independent_variables'], ['allocated_render_time', 'axis_label',
            'estimated_render_time', 'height', 'layer_number', 'number_of_rings',
            'position', 'position2', 'render_time_multiplier', 'title', 'width']),
            title='Edit SpiderPlotActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SpiderPlotActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

