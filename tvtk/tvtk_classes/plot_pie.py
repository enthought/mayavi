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

from tvtk.tvtk_classes.plot import Plot


class PlotPie(Plot):
    """
    PlotPie - Class for drawing a Pie diagram.
    
    Superclass: Plot
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotPie, obj, update, **traits)
    
    def _get_color_series(self):
        return wrap_vtk(self._vtk_obj.GetColorSeries())
    def _set_color_series(self, arg):
        old_val = self._get_color_series()
        self._wrap_call(self._vtk_obj.SetColorSeries,
                        deref_vtk(arg))
        self.trait_property_changed('color_series', old_val, arg)
    color_series = traits.Property(_get_color_series, _set_color_series, help=\
        """
        Get the color series used.
        """
    )

    dimensions = traits.Array(shape=(4,), value=(0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set the dimensions of the pie, arguments 1 and 2 are the x and y
        coordinate of the bottom corner. Arguments 3 and 4 are the width
        and height.
        """
    )
    def _dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensions,
                        self.dimensions)

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('dimensions', 'GetDimensions'),
    ('visible', 'GetVisible'), ('reference_count', 'GetReferenceCount'),
    ('debug', 'GetDebug'), ('width', 'GetWidth'), ('label', 'GetLabel'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'dimensions', 'label', 'opacity',
    'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotPie, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotPie properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['dimensions', 'label', 'opacity',
            'use_index_for_x_series', 'visible', 'width']),
            title='Edit PlotPie properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotPie properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

