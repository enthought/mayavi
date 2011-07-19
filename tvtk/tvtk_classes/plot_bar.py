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


class PlotBar(Plot):
    """
    PlotBar - Class for drawing an XY plot given two columns from a
    
    Superclass: Plot
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotBar, obj, update, **traits)
    
    def get_color(self, *args):
        """
        V.get_color([float, float, float])
        C++: virtual void GetColor(double rgb[3])
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

    def _get_color_series(self):
        return wrap_vtk(self._vtk_obj.GetColorSeries())
    def _set_color_series(self, arg):
        old_val = self._get_color_series()
        self._wrap_call(self._vtk_obj.SetColorSeries,
                        deref_vtk(arg))
        self.trait_property_changed('color_series', old_val, arg)
    color_series = traits.Property(_get_color_series, _set_color_series, help=\
        """
        Get the color series used if when this is a stacked bar plot.
        """
    )

    offset = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the width of the line.
        """
    )
    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

    group_name = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Set the group name of the bar chart - can be displayed on the X
        axis.
        """
    )
    def _group_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGroupName,
                        self.group_name)

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('width', 'GetWidth'), ('debug',
    'GetDebug'), ('group_name', 'GetGroupName'), ('visible',
    'GetVisible'), ('offset', 'GetOffset'), ('reference_count',
    'GetReferenceCount'), ('label', 'GetLabel'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'group_name', 'label', 'offset',
    'opacity', 'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotBar, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotBar properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['group_name', 'label', 'offset', 'opacity',
            'use_index_for_x_series', 'visible', 'width']),
            title='Edit PlotBar properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotBar properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

