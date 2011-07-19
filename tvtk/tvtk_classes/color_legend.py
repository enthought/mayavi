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

from tvtk.tvtk_classes.chart_legend import ChartLegend


class ColorLegend(ChartLegend):
    """
    ColorLegend - Legend item to display ScalarsToColors.
    
    Superclass: ChartLegend
    
    ColorLegend is an item that will display the ScalarsToColors
    using a 1d texture, and a Axis to show both the color and
    numerical range.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkColorLegend, obj, update, **traits)
    
    def _get_transfer_function(self):
        return wrap_vtk(self._vtk_obj.GetTransferFunction())
    def _set_transfer_function(self, arg):
        old_val = self._get_transfer_function()
        self._wrap_call(self._vtk_obj.SetTransferFunction,
                        deref_vtk(arg))
        self.trait_property_changed('transfer_function', old_val, arg)
    transfer_function = traits.Property(_get_transfer_function, _set_transfer_function, help=\
        """
        
        """
    )

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float])
        C++: virtual void GetBounds(double bounds[4])"""
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

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
            return super(ColorLegend, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ColorLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['horizontal_alignment', 'inline',
            'label_size', 'opacity', 'padding', 'point', 'symbol_width',
            'vertical_alignment', 'visible']),
            title='Edit ColorLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ColorLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

