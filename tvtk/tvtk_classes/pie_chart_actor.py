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


class PieChartActor(Actor2D):
    """
    PieChartActor - create a pie chart from an array
    
    Superclass: Actor2D
    
    PieChartActor generates a pie chart from an array of numbers
    defined in field data (a DataObject). To use this class, you must
    specify an input data object. You'll probably also want to specify
    the position of the plot be setting the Position and Position2
    instance variables, which define a rectangle in which the plot lies. 
    There are also many other instance variables that control the look of
    the plot includes its title, and legend.
    
    Set the text property/attributes of the title and the labels through
    the TextProperty objects associated with these components.
    
    See Also:
    
    ParallelCoordinatesActor XYPlotActor2D SpiderPlotActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPieChartActor, obj, update, **traits)
    
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
        Enable/Disable the display of pie piece labels.
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

    def _get_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTitleTextProperty())
    def _set_title_text_property(self, arg):
        old_val = self._get_title_text_property()
        self._wrap_call(self._vtk_obj.SetTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('title_text_property', old_val, arg)
    title_text_property = traits.Property(_get_title_text_property, _set_title_text_property, help=\
        """
        Set/Get the title text property. The property controls the
        appearance of the plot title.
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

    piece_label = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the names for each piece of pie.  not specified, then an
        integer number is automatically generated.
        """
    )
    def _piece_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPieceLabel,
                        self.piece_label)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the pie chart.
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Set/Get the labels text property. This controls the appearance of
        all pie piece labels.
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

    def set_piece_color(self, *args):
        """
        V.set_piece_color(int, float, float, float)
        C++: void SetPieceColor(int i, double r, double g, double b)
        V.set_piece_color(int, (float, float, float))
        C++: void SetPieceColor(int i, const double color[3])
        Specify colors for each piece of pie. If not specified, they are
        automatically generated.
        """
        ret = self._wrap_call(self._vtk_obj.SetPieceColor, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('layer_number',
    'GetLayerNumber'), ('piece_label', 'GetPieceLabel'), ('title',
    'GetTitle'), ('position2', 'GetPosition2'), ('debug', 'GetDebug'),
    ('dragable', 'GetDragable'), ('legend_visibility',
    'GetLegendVisibility'), ('label_visibility', 'GetLabelVisibility'),
    ('visibility', 'GetVisibility'), ('height', 'GetHeight'), ('width',
    'GetWidth'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('pickable', 'GetPickable'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('use_bounds', 'GetUseBounds'),
    ('title_visibility', 'GetTitleVisibility'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'label_visibility',
    'legend_visibility', 'pickable', 'title_visibility', 'use_bounds',
    'visibility', 'allocated_render_time', 'estimated_render_time',
    'height', 'layer_number', 'piece_label', 'position', 'position2',
    'render_time_multiplier', 'title', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PieChartActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PieChartActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['label_visibility', 'legend_visibility',
            'title_visibility', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'height',
            'layer_number', 'piece_label', 'position', 'position2',
            'render_time_multiplier', 'title', 'width']),
            title='Edit PieChartActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PieChartActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

