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

from tvtk.tvtk_classes.object import Object


class ColorSeries(Object):
    """
    ColorSeries - stores a list of colors.
    
    Superclass: Object
    
    The ColorSeries stores a list of colors. There are several schemes
    available and functions to control several aspects of what colors are
    returned. In essence a color scheme is set and colors are returned
    based on the index requested.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkColorSeries, obj, update, **traits)
    
    color_scheme = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the color scheme that should be used from those in the enum.
        """
    )
    def _color_scheme_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorScheme,
                        self.color_scheme)

    def _get_number_of_colors(self):
        return self._vtk_obj.GetNumberOfColors()
    number_of_colors = traits.Property(_get_number_of_colors, help=\
        """
        Get the number of colors available in the current color scheme.
        """
    )

    def clear_colors(self):
        """
        V.clear_colors()
        C++: void ClearColors()
        Clears the list of colors.
        """
        ret = self._vtk_obj.ClearColors()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(ColorSeries)
        C++: void DeepCopy(ColorSeries *chartColors)
        Make a deep copy of the supplied object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def remove_color(self, *args):
        """
        V.remove_color(int)
        C++: void RemoveColor(int index)
        Removes the color at the specified index in the list.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveColor, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('color_scheme',
    'GetColorScheme'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'color_scheme'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ColorSeries, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ColorSeries properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['color_scheme']),
            title='Edit ColorSeries properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ColorSeries properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

