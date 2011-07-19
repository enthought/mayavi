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


class ChartLegend(ContextItem):
    """
    ChartLegend - draw the chart legend
    
    Superclass: ContextItem
    
    The ChartLegend is drawn in screen coordinates. It is usually one
    of the last elements of a chart to be drawn. It renders the the
    mark/line for each plot, and the plot labels.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartLegend, obj, update, **traits)
    
    point = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint,
                        self.point)

    def _get_chart(self):
        return wrap_vtk(self._vtk_obj.GetChart())
    def _set_chart(self, arg):
        old_val = self._get_chart()
        self._wrap_call(self._vtk_obj.SetChart,
                        deref_vtk(arg))
        self.trait_property_changed('chart', old_val, arg)
    chart = traits.Property(_get_chart, _set_chart, help=\
        """
        Get the chart that the legend belongs to and will draw the legend
        for.
        """
    )

    padding = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set the padding between legend marks, default is 5.
        """
    )
    def _padding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPadding,
                        self.padding)

    vertical_alignment = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Set the vertical alignment of the legend to the point specified.
        Valid values are TOP, CENTER and BOTTOM.
        """
    )
    def _vertical_alignment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalAlignment,
                        self.vertical_alignment)

    horizontal_alignment = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set the horizontal alignment of the legend to the point
        specified. Valid values are LEFT, CENTER and RIGHT.
        """
    )
    def _horizontal_alignment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHorizontalAlignment,
                        self.horizontal_alignment)

    inline = traits.Bool(True, help=\
        """
        Get/set if the legend should be drawn inline (inside the chart),
        or not. True would generally request that the chart draws it
        inside the chart, false would adjust the chart axes and make
        space to draw the axes outside.
        """
    )
    def _inline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInline,
                        self.inline)

    symbol_width = traits.Int(25, enter_set=True, auto_set=False, help=\
        """
        Set the symbol width, default is 15.
        """
    )
    def _symbol_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSymbolWidth,
                        self.symbol_width)

    label_size = traits.Int(12, enter_set=True, auto_set=False, help=\
        """
        Set the point size of the label text.
        """
    )
    def _label_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelSize,
                        self.label_size)

    def _get_label_properties(self):
        return wrap_vtk(self._vtk_obj.GetLabelProperties())
    label_properties = traits.Property(_get_label_properties, help=\
        """
        Get the TextProperty for the legend's labels.
        """
    )

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('symbol_width', 'GetSymbolWidth'),
    ('point', 'GetPoint'), ('debug', 'GetDebug'), ('vertical_alignment',
    'GetVerticalAlignment'), ('padding', 'GetPadding'), ('visible',
    'GetVisible'), ('horizontal_alignment', 'GetHorizontalAlignment'),
    ('reference_count', 'GetReferenceCount'), ('inline', 'GetInline'),
    ('label_size', 'GetLabelSize'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'horizontal_alignment', 'inline',
    'label_size', 'opacity', 'padding', 'point', 'symbol_width',
    'vertical_alignment', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartLegend, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['horizontal_alignment', 'inline',
            'label_size', 'opacity', 'padding', 'point', 'symbol_width',
            'vertical_alignment', 'visible']),
            title='Edit ChartLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

