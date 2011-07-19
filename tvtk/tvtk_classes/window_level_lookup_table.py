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

from tvtk.tvtk_classes.lookup_table import LookupTable


class WindowLevelLookupTable(LookupTable):
    """
    WindowLevelLookupTable - map scalar values into colors or colors
    to scalars; generate color table
    
    Superclass: LookupTable
    
    WindowLevelLookupTable is an object that is used by mapper objects
    to map scalar values into rgba (red-green-blue-alpha transparency)
    color specification, or rgba into scalar values. The color table can
    be created by direct insertion of color values, or by specifying a
    window and level. Window / Level is used in medical imaging to
    specify a linear greyscale ramp. The Level is the center of the ramp.
     The Window is the width of the ramp.
    
    Caveats:
    
    WindowLevelLookupTable is a reference counted object. Therefore,
    you should always use operator "new" to construct new objects. This
    procedure will avoid memory problems (see text).
    
    See Also:
    
    LogLookupTable
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWindowLevelLookupTable, obj, update, **traits)
    
    inverse_video = tvtk_base.false_bool_trait(help=\
        """
        Set inverse video on or off.  You can achieve the same effect by
        switching the minimum_table_value and the maximum_table_value.
        """
    )
    def _inverse_video_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInverseVideo,
                        self.inverse_video_)

    level = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set the Level for the lookup table.  The level is the average of
        table_range[_0] and table_range[_1].
        """
    )
    def _level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevel,
                        self.level)

    window = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the window for the lookup table.  The window is the
        difference between table_range[_0] and table_range[_1].
        """
    )
    def _window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindow,
                        self.window)

    def get_maximum_color(self):
        """
        V.get_maximum_color([, , , ])
        C++: void GetMaximumColor(unsigned char rgba[4])
        @deprecated For backwards compatibility: specify the color using
        integers in the range [0,255].
        """
        ret = self._vtk_obj.GetMaximumColor()
        return ret
        

    def set_maximum_color(self, *args):
        """
        V.set_maximum_color(int, int, int, int)
        C++: void SetMaximumColor(int r, int g, int b, int a)
        V.set_maximum_color((, , , ))
        C++: void SetMaximumColor(const unsigned char rgba[4])
        @deprecated For backwards compatibility: specify the color using
        integers in the range [0,255].
        """
        ret = self._wrap_call(self._vtk_obj.SetMaximumColor, *args)
        return ret

    maximum_table_value = traits.Array(shape=(4,), value=(1.0, 1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _maximum_table_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumTableValue,
                        self.maximum_table_value)

    minimum_table_value = traits.Array(shape=(4,), value=(0.0, 0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _minimum_table_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumTableValue,
                        self.minimum_table_value)

    def get_minimum_color(self):
        """
        V.get_minimum_color([, , , ])
        C++: void GetMinimumColor(unsigned char rgba[4])
        @deprecated For backwards compatibility: specify the color using
        integers in the range [0,255].
        """
        ret = self._vtk_obj.GetMinimumColor()
        return ret
        

    def set_minimum_color(self, *args):
        """
        V.set_minimum_color(int, int, int, int)
        C++: void SetMinimumColor(int r, int g, int b, int a)
        V.set_minimum_color((, , , ))
        C++: void SetMinimumColor(const unsigned char rgba[4])
        @deprecated For backwards compatibility: specify the color using
        integers in the range [0,255].
        """
        ret = self._wrap_call(self._vtk_obj.SetMinimumColor, *args)
        return ret

    _updateable_traits_ = \
    (('saturation_range', 'GetSaturationRange'), ('hue_range',
    'GetHueRange'), ('nan_color', 'GetNanColor'), ('minimum_table_value',
    'GetMinimumTableValue'), ('table_range', 'GetTableRange'),
    ('vector_component', 'GetVectorComponent'), ('alpha_range',
    'GetAlphaRange'), ('alpha', 'GetAlpha'), ('scale', 'GetScale'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_table_value', 'GetMaximumTableValue'), ('level',
    'GetLevel'), ('debug', 'GetDebug'), ('number_of_table_values',
    'GetNumberOfTableValues'), ('ramp', 'GetRamp'), ('window',
    'GetWindow'), ('number_of_colors', 'GetNumberOfColors'), ('range',
    'GetRange'), ('value_range', 'GetValueRange'), ('reference_count',
    'GetReferenceCount'), ('vector_mode', 'GetVectorMode'),
    ('inverse_video', 'GetInverseVideo'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'inverse_video', 'ramp', 'scale',
    'vector_mode', 'alpha', 'alpha_range', 'hue_range', 'level',
    'maximum_table_value', 'minimum_table_value', 'nan_color',
    'number_of_colors', 'number_of_table_values', 'range',
    'saturation_range', 'table_range', 'value_range', 'vector_component',
    'window'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WindowLevelLookupTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WindowLevelLookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['inverse_video'], ['ramp', 'scale', 'vector_mode'],
            ['alpha', 'alpha_range', 'hue_range', 'level', 'maximum_table_value',
            'minimum_table_value', 'nan_color', 'number_of_colors',
            'number_of_table_values', 'range', 'saturation_range', 'table_range',
            'value_range', 'vector_component', 'window']),
            title='Edit WindowLevelLookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WindowLevelLookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

