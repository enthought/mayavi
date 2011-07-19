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


class ColorTransferFunction(ScalarsToColors):
    """
    ColorTransferFunction - Defines a transfer function for mapping a
    property to an RGB color value.
    
    Superclass: ScalarsToColors
    
    ColorTransferFunction is a color mapping in RGB or HSV space that
    uses piecewise hermite functions to allow interpolation that can be
    piecewise constant, piecewise linear, or somewhere in-between (a
    modified piecewise hermite function that squishes the function
    according to a sharpness parameter). The function also allows for the
    specification of the midpoint (the place where the function reaches
    the average of the two bounding nodes) as a normalize distance
    between nodes. See the description of class PiecewiseFunction for
    an explanation of midpoint and sharpness.
    
    See Also:
    
    PiecewiseFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkColorTransferFunction, obj, update, **traits)
    
    hsv_wrap = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        or Diverging.  In HSV mode, if HSVWrap is on, it will take the
        shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of LookupTable).  Diverging is a special mode
        where colors will pass through white when interpolating between
        two saturated colors.
        """
    )
    def _hsv_wrap_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHSVWrap,
                        self.hsv_wrap_)

    clamping = tvtk_base.true_bool_trait(help=\
        """
        Sets and gets the clamping value for this transfer function.
        """
    )
    def _clamping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClamping,
                        self.clamping_)

    allow_duplicate_scalars = tvtk_base.false_bool_trait(help=\
        """
        Toggle whether to allow duplicate scalar values in the color
        transfer function (off by default).
        """
    )
    def _allow_duplicate_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowDuplicateScalars,
                        self.allow_duplicate_scalars_)

    color_space = traits.Trait('rgb',
    tvtk_base.TraitRevPrefixMap({'diverging': 3, 'rgb': 0, 'hsv': 1, 'lab': 2}), help=\
        """
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        or Diverging.  In HSV mode, if HSVWrap is on, it will take the
        shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of LookupTable).  Diverging is a special mode
        where colors will pass through white when interpolating between
        two saturated colors.
        """
    )
    def _color_space_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorSpace,
                        self.color_space_)

    scale = traits.Trait('linear',
    tvtk_base.TraitRevPrefixMap({'log10': 1, 'linear': 0}), help=\
        """
        Set the type of scale to use, linear or logarithmic.  The default
        is linear.  If the scale is logarithmic, and the range contains
        zero, the color mapping will be linear.
        """
    )
    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale_)

    nan_color = tvtk_base.vtk_color_trait((0.5, 0.0, 0.0), help=\
        """
        
        """
    )
    def _nan_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNanColor,
                        self.nan_color, False)

    def get_node_value(self, *args):
        """
        V.get_node_value(int, [float, float, float, float, float, float])
            -> int
        C++: int GetNodeValue(int index, double val[6])
        For the node specified by index, set/get the location (X), R, G,
        and B values, midpoint, and sharpness values at the node.
        """
        ret = self._wrap_call(self._vtk_obj.GetNodeValue, *args)
        return ret

    def set_node_value(self, *args):
        """
        V.set_node_value(int, [float, float, float, float, float, float])
            -> int
        C++: int SetNodeValue(int index, double val[6])
        For the node specified by index, set/get the location (X), R, G,
        and B values, midpoint, and sharpness values at the node.
        """
        ret = self._wrap_call(self._vtk_obj.SetNodeValue, *args)
        return ret

    def get_blue_value(self, *args):
        """
        V.get_blue_value(float) -> float
        C++: double GetBlueValue(double x)
        Get the color components individually.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlueValue, *args)
        return ret

    def _get_clamping_max_value(self):
        return self._vtk_obj.GetClampingMaxValue()
    clamping_max_value = traits.Property(_get_clamping_max_value, help=\
        """
        Sets and gets the clamping value for this transfer function.
        """
    )

    def _get_clamping_min_value(self):
        return self._vtk_obj.GetClampingMinValue()
    clamping_min_value = traits.Property(_get_clamping_min_value, help=\
        """
        Sets and gets the clamping value for this transfer function.
        """
    )

    def get_green_value(self, *args):
        """
        V.get_green_value(float) -> float
        C++: double GetGreenValue(double x)
        Get the color components individually.
        """
        ret = self._wrap_call(self._vtk_obj.GetGreenValue, *args)
        return ret

    def get_red_value(self, *args):
        """
        V.get_red_value(float) -> float
        C++: double GetRedValue(double x)
        Get the color components individually.
        """
        ret = self._wrap_call(self._vtk_obj.GetRedValue, *args)
        return ret

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        How many points are there defining this function?
        """
    )

    def add_hsv_point(self, *args):
        """
        V.add_hsv_point(float, float, float, float) -> int
        C++: int AddHSVPoint(double x, double h, double s, double v)
        V.add_hsv_point(float, float, float, float, float, float) -> int
        C++: int AddHSVPoint(double x, double h, double s, double v,
            double midpoint, double sharpness)
        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error. See the
        description of class PiecewiseFunction for an explanation of
        midpoint and sharpness.
        """
        ret = self._wrap_call(self._vtk_obj.AddHSVPoint, *args)
        return ret

    def add_hsv_segment(self, *args):
        """
        V.add_hsv_segment(float, float, float, float, float, float, float,
            float)
        C++: void AddHSVSegment(double x1, double h1, double s1,
            double v1, double x2, double h2, double s2, double v2)
        Add two points to the function and remove all the points between
        them
        """
        ret = self._wrap_call(self._vtk_obj.AddHSVSegment, *args)
        return ret

    def add_rgb_point(self, *args):
        """
        V.add_rgb_point(float, float, float, float) -> int
        C++: int AddRGBPoint(double x, double r, double g, double b)
        V.add_rgb_point(float, float, float, float, float, float) -> int
        C++: int AddRGBPoint(double x, double r, double g, double b,
            double midpoint, double sharpness)
        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error. See the
        description of class PiecewiseFunction for an explanation of
        midpoint and sharpness.
        """
        ret = self._wrap_call(self._vtk_obj.AddRGBPoint, *args)
        return ret

    def add_rgb_segment(self, *args):
        """
        V.add_rgb_segment(float, float, float, float, float, float, float,
            float)
        C++: void AddRGBSegment(double x1, double r1, double g1,
            double b1, double x2, double r2, double g2, double b2)
        Add two points to the function and remove all the points between
        them
        """
        ret = self._wrap_call(self._vtk_obj.AddRGBSegment, *args)
        return ret

    def adjust_range(self, *args):
        """
        V.adjust_range([float, float]) -> int
        C++: int AdjustRange(double range[2])
        Remove all points out of the new range, and make sure there is a
        point at each end of that range. Return 1 on success, 0
        otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.AdjustRange, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(ColorTransferFunction)
        C++: void DeepCopy(ColorTransferFunction *f)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def remove_all_points(self):
        """
        V.remove_all_points()
        C++: void RemoveAllPoints()
        Remove all points
        """
        ret = self._vtk_obj.RemoveAllPoints()
        return ret
        

    def remove_point(self, *args):
        """
        V.remove_point(float) -> int
        C++: int RemovePoint(double x)
        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error. See the
        description of class PiecewiseFunction for an explanation of
        midpoint and sharpness.
        """
        ret = self._wrap_call(self._vtk_obj.RemovePoint, *args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(ColorTransferFunction)
        C++: void ShallowCopy(ColorTransferFunction *f)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('color_space', 'GetColorSpace'), ('scale', 'GetScale'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('hsv_wrap',
    'GetHSVWrap'), ('nan_color', 'GetNanColor'), ('debug', 'GetDebug'),
    ('range', 'GetRange'), ('vector_component', 'GetVectorComponent'),
    ('reference_count', 'GetReferenceCount'), ('alpha', 'GetAlpha'),
    ('vector_mode', 'GetVectorMode'), ('clamping', 'GetClamping'),
    ('allow_duplicate_scalars', 'GetAllowDuplicateScalars'))
    
    _full_traitnames_list_ = \
    (['allow_duplicate_scalars', 'clamping', 'debug',
    'global_warning_display', 'hsv_wrap', 'color_space', 'scale',
    'vector_mode', 'alpha', 'nan_color', 'range', 'vector_component'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ColorTransferFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['allow_duplicate_scalars', 'clamping', 'hsv_wrap'],
            ['color_space', 'scale', 'vector_mode'], ['alpha', 'nan_color',
            'range', 'vector_component']),
            title='Edit ColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

