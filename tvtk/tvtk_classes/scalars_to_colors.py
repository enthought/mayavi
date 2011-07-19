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


class ScalarsToColors(Object):
    """
    ScalarsToColors - Superclass for mapping scalar values into 
    
    Superclass: Object
    
    ScalarsToColors is a general purpose superclass for objects that
    convert scalars to colors. This include LookupTable classes and
    color transfer functions.
    
    The scalars to color mapping can be augmented with an additional
    uniform alpha blend. This is used, for example, to blend a Actor's
    opacity with the lookup table values.
    
    See Also:
    
    LookupTable ColorTransferFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarsToColors, obj, update, **traits)
    
    vector_mode = traits.Trait('component',
    tvtk_base.TraitRevPrefixMap({'magnitude': 0, 'component': 1}), help=\
        """
        Change mode that maps vectors by magnitude vs. component.
        """
    )
    def _vector_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorMode,
                        self.vector_mode_)

    alpha = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify an additional opacity (alpha) value to blend with. Values
        != 1 modify the resulting color consistent with the requested
        form of the output. This is typically used by an actor in order
        to blend its opacity.
        """
    )
    def _alpha_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlpha,
                        self.alpha)

    range = traits.Array(shape=(2,), value=(0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Sets/Gets the range of scalars which will be mapped.
        """
    )
    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    vector_component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        If the mapper does not select which component of a vector to map
        to colors, you can specify it here.
        """
    )
    def _vector_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorComponent,
                        self.vector_component)

    def get_color(self, *args):
        """
        V.get_color(float, [float, float, float])
        C++: virtual void GetColor(double v, double rgb[3])
        V.get_color(float) -> (float, float, float)
        C++: double *GetColor(double v)
        Map one value through the lookup table and return the color as an
        RGB array of doubles between 0 and 1.
        """
        ret = self._wrap_call(self._vtk_obj.GetColor, *args)
        return ret

    def get_luminance(self, *args):
        """
        V.get_luminance(float) -> float
        C++: double GetLuminance(double x)
        Map one value through the lookup table and return the luminance
        0.3*red + 0.59*green + 0.11*blue as a double between 0 and 1.
        Returns the luminance value for the specified scalar value.
        """
        ret = self._wrap_call(self._vtk_obj.GetLuminance, *args)
        return ret

    def _get_number_of_available_colors(self):
        return self._vtk_obj.GetNumberOfAvailableColors()
    number_of_available_colors = traits.Property(_get_number_of_available_colors, help=\
        """
        Get the number of available colors for mapping to.
        """
    )

    def get_opacity(self, *args):
        """
        V.get_opacity(float) -> float
        C++: virtual double GetOpacity(double v)
        Map one value through the lookup table and return the alpha value
        (the opacity) as a double between 0 and 1.
        """
        ret = self._wrap_call(self._vtk_obj.GetOpacity, *args)
        return ret

    def build(self):
        """
        V.build()
        C++: virtual void Build()
        Perform any processing required (if any) before processing
        scalars.
        """
        ret = self._vtk_obj.Build()
        return ret
        

    def convert_unsigned_char_to_rgba(self, *args):
        """
        V.convert_unsigned_char_to_rgba(UnsignedCharArray, int, int)
            -> UnsignedCharArray
        C++: virtual UnsignedCharArray *ConvertUnsignedCharToRGBA(
            UnsignedCharArray *colors, int numComp, int numTuples)
        An internal method used to convert a color array to RGBA. The
        method instantiates a UnsignedCharArray and returns it. The
        user is responsible for managing the memory.
        """
        my_args = deref_array(args, [('vtkUnsignedCharArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.ConvertUnsignedCharToRGBA, *my_args)
        return wrap_vtk(ret)

    def is_opaque(self):
        """
        V.is_opaque() -> int
        C++: virtual int IsOpaque()
        Return true if all of the values defining the mapping have an
        opacity equal to 1. Default implementation return true.
        """
        ret = self._vtk_obj.IsOpaque()
        return ret
        

    def map_scalars(self, *args):
        """
        V.map_scalars(DataArray, int, int) -> UnsignedCharArray
        C++: virtual UnsignedCharArray *MapScalars(
            DataArray *scalars, int colorMode, int component)
        An internal method maps a data array into a 4-component, unsigned
        char RGBA array. The color mode determines the behavior of
        mapping. If VTK_COLOR_MODE_DEFAULT is set, then unsigned char
        data arrays are treated as colors (and converted to RGBA if
        necessary); otherwise, the data is mapped through this instance
        of scalars_to_colors. The offset is used for data arrays with more
        than one component; it indicates which component to use to do the
        blending. When the component argument is -1, then the this object
        uses its own selected technique to change a vector into a scalar
        to map.
        """
        my_args = deref_array(args, [('vtkDataArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.MapScalars, *my_args)
        return wrap_vtk(ret)

    def using_log_scale(self):
        """
        V.using_log_scale() -> int
        C++: virtual int UsingLogScale()
        This should return 1 is the subclass is using log scale for
        mapping scalars to colors. Default implementation returns 0.
        """
        ret = self._vtk_obj.UsingLogScale()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('range', 'GetRange'), ('vector_component',
    'GetVectorComponent'), ('reference_count', 'GetReferenceCount'),
    ('alpha', 'GetAlpha'), ('vector_mode', 'GetVectorMode'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'vector_mode', 'alpha', 'range',
    'vector_component'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarsToColors, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarsToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['vector_mode'], ['alpha', 'range',
            'vector_component']),
            title='Edit ScalarsToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarsToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

