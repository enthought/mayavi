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

from tvtk.tvtk_classes.scalars_to_colors import ScalarsToColors


class LookupTable(ScalarsToColors):
    """
    LookupTable - map scalar values into colors via a lookup table
    
    Superclass: ScalarsToColors
    
    LookupTable is an object that is used by mapper objects to map
    scalar values into rgba (red-green-blue-alpha transparency) color
    specification, or rgba into scalar values. The color table can be
    created by direct insertion of color values, or by specifying  hue,
    saturation, value, and alpha range and generating a table.
    
    Caveats:
    
    You need to explicitely call Build() when constructing the LUT by
    hand.
    
    See Also:
    
    LogLookupTable WindowLevelLookupTable
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLookupTable, obj, update, **traits)
    
    scale = traits.Trait('linear',
    tvtk_base.TraitRevPrefixMap({'log10': 1, 'linear': 0}), help=\
        """
        Set the type of scale to use, linear or logarithmic.  The default
        is linear.  If the scale is logarithmic, then the table_range must
        not cross the value zero.
        """
    )
    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale_)

    ramp = traits.Trait('s_curve',
    tvtk_base.TraitRevPrefixMap({'s_curve': 1, 'linear': 0, 'sqrt': 2}), help=\
        """
        Set the shape of the table ramp to either linear or S-curve. The
        default is S-curve, which tails off gradually at either end. The
        equation used for the S-curve is y = (sin((x - 1/2)*pi) + 1)/2,
        while the equation for the linear ramp is simply y = x.  For an
        S-curve greyscale ramp, you should set number_of_table_values to 402
        (which is 256*pi/2) to provide room for the tails of the ramp.
        The equation for the SQRT is y = sqrt(x).
        """
    )
    def _ramp_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRamp,
                        self.ramp_)

    value_range = traits.Array(shape=(2,), value=(1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _value_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValueRange,
                        self.value_range)

    number_of_colors = traits.Trait(256, traits.Range(2, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of colors in the lookup table.  Use
        set_number_of_table_values() instead, it can be used both before and
        after the table has been built whereas set_number_of_colors() has no
        effect after the table has been built.
        """
    )
    def _number_of_colors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfColors,
                        self.number_of_colors)

    nan_color = traits.Array(shape=(4,), value=(0.5, 0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _nan_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNanColor,
                        self.nan_color)

    alpha_range = traits.Array(shape=(2,), value=(1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _alpha_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlphaRange,
                        self.alpha_range)

    saturation_range = traits.Array(shape=(2,), value=(1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _saturation_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSaturationRange,
                        self.saturation_range)

    range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Sets/Gets the range of scalars which will be mapped.  This is a
        duplicate of get/_set_table_range.
        """
    )
    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    def get_table_value(self, *args):
        """
        V.get_table_value(int) -> (float, float, float, float)
        C++: double *GetTableValue(IdType id)
        V.get_table_value(int, [float, float, float, float])
        C++: void GetTableValue(IdType id, double rgba[4])
        Return a rgba color value for the given index into the lookup
        table. Color components are expressed as [0,1] double values.
        """
        ret = self._wrap_call(self._vtk_obj.GetTableValue, *args)
        return ret

    def set_table_value(self, *args):
        """
        V.set_table_value(int, [float, float, float, float])
        C++: void SetTableValue(IdType indx, double rgba[4])
        V.set_table_value(int, float, float, float, float)
        C++: void SetTableValue(IdType indx, double r, double g,
            double b, double a=1.0)
        Directly load color into lookup table. Use [0,1] double values
        for color component specification. Make sure that you've either
        used the Build() method or used set_number_of_table_values() prior to
        using this method.
        """
        ret = self._wrap_call(self._vtk_obj.SetTableValue, *args)
        return ret

    number_of_table_values = traits.Int(256, enter_set=True, auto_set=False, help=\
        """
        Specify the number of values (i.e., colors) in the lookup table.
        """
    )
    def _number_of_table_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTableValues,
                        self.number_of_table_values)

    def _get_table(self):
        return wrap_vtk(self._vtk_obj.GetTable())
    def _set_table(self, arg):
        old_val = self._get_table()
        my_arg = deref_array([arg], [['vtkUnsignedCharArray']])
        self._wrap_call(self._vtk_obj.SetTable,
                        my_arg[0])
        self.trait_property_changed('table', old_val, arg)
    table = traits.Property(_get_table, _set_table, help=\
        """
        Set/Get the internal table array that is used to map the scalars
        to colors.  The table array is an unsigned char array with 4
        components representing RGBA.
        """
    )

    table_range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the minimum/maximum scalar values for scalar mapping.
        Scalar values less than minimum range value are clamped to
        minimum range value. Scalar values greater than maximum range
        value are clamped to maximum range value.
        """
    )
    def _table_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTableRange,
                        self.table_range)

    hue_range = traits.Array(shape=(2,), value=(0.0, 0.66666999999999998), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _hue_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHueRange,
                        self.hue_range)

    def get_index(self, *args):
        """
        V.get_index(float) -> int
        C++: virtual IdType GetIndex(double v)
        Return the table index associated with a particular value.
        """
        ret = self._wrap_call(self._vtk_obj.GetIndex, *args)
        return ret

    def get_log_range(self, *args):
        """
        V.get_log_range((float, float), [float, float])
        C++: static void GetLogRange(const double range[2],
            double log_range[2])
        Returns the log of range in log_range. There is a little more to
        this than simply taking the log10 of the two range values: we do
        conversion of negative ranges to positive ranges, and conversion
        of zero to a 'very small number'.
        """
        ret = self._wrap_call(self._vtk_obj.GetLogRange, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: int Allocate(int sz=256, int ext=256)
        Allocate a color table of specified size.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def apply_log_scale(self, *args):
        """
        V.apply_log_scale(float, (float, float), (float, float)) -> float
        C++: static double ApplyLogScale(double v, const double range[2],
            const double log_range[2])
        Apply log to value, with appropriate constraints.
        """
        ret = self._wrap_call(self._vtk_obj.ApplyLogScale, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(LookupTable)
        C++: void DeepCopy(LookupTable *lut)
        Copy the contents from another lookup_table
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def force_build(self):
        """
        V.force_build()
        C++: virtual void ForceBuild()
        Force the lookup table to regenerate from hue, saturation, value,
        and alpha min/max values.  Table is built from a linear ramp of
        each value.  force_build() is useful if a lookup table has been
        defined manually (using set_table_value) and then an application
        decides to rebuild the lookup table using the implicit process.
        """
        ret = self._vtk_obj.ForceBuild()
        return ret
        

    _updateable_traits_ = \
    (('scale', 'GetScale'), ('value_range', 'GetValueRange'),
    ('saturation_range', 'GetSaturationRange'), ('number_of_table_values',
    'GetNumberOfTableValues'), ('hue_range', 'GetHueRange'), ('nan_color',
    'GetNanColor'), ('ramp', 'GetRamp'), ('debug', 'GetDebug'),
    ('number_of_colors', 'GetNumberOfColors'), ('table_range',
    'GetTableRange'), ('range', 'GetRange'), ('vector_component',
    'GetVectorComponent'), ('alpha_range', 'GetAlphaRange'),
    ('reference_count', 'GetReferenceCount'), ('alpha', 'GetAlpha'),
    ('vector_mode', 'GetVectorMode'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'ramp', 'scale', 'vector_mode',
    'alpha', 'alpha_range', 'hue_range', 'nan_color', 'number_of_colors',
    'number_of_table_values', 'range', 'saturation_range', 'table_range',
    'value_range', 'vector_component'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LookupTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['ramp', 'scale', 'vector_mode'], ['alpha',
            'alpha_range', 'hue_range', 'nan_color', 'number_of_colors',
            'number_of_table_values', 'range', 'saturation_range', 'table_range',
            'value_range', 'vector_component']),
            title='Edit LookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

