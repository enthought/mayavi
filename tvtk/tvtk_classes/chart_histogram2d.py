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

from tvtk.tvtk_classes.chart_xy import ChartXY


class ChartHistogram2D(ChartXY):
    """
    Chart2DHistogram - Chart for 2d histograms.
    
    Superclass: ChartXY
    
    This defines the interface for a 2d histogram chart.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartHistogram2D, obj, update, **traits)
    
    def set_input(self, *args):
        """
        V.set_input(ImageData, int)
        C++: virtual void SetInput(ImageData *data, IdType z=0)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def set_transfer_function(self, *args):
        """
        V.set_transfer_function(ScalarsToColors)
        C++: virtual void SetTransferFunction(
            ScalarsToColors *function)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTransferFunction, *my_args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('point1', 'GetPoint1'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('hidden_axis_border', 'GetHiddenAxisBorder'), ('geometry',
    'GetGeometry'), ('debug', 'GetDebug'), ('title', 'GetTitle'),
    ('draw_axes_at_origin', 'GetDrawAxesAtOrigin'), ('point2',
    'GetPoint2'), ('bar_width_fraction', 'GetBarWidthFraction'),
    ('visible', 'GetVisible'), ('show_legend', 'GetShowLegend'),
    ('reference_count', 'GetReferenceCount'), ('auto_size',
    'GetAutoSize'), ('auto_axes', 'GetAutoAxes'))
    
    _full_traitnames_list_ = \
    (['auto_axes', 'debug', 'draw_axes_at_origin',
    'global_warning_display', 'auto_size', 'bar_width_fraction',
    'geometry', 'hidden_axis_border', 'opacity', 'point1', 'point2',
    'show_legend', 'title', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartHistogram2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_axes', 'draw_axes_at_origin'], [], ['auto_size',
            'bar_width_fraction', 'geometry', 'hidden_axis_border', 'opacity',
            'point1', 'point2', 'show_legend', 'title', 'visible']),
            title='Edit ChartHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

