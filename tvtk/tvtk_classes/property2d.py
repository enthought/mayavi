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


class Property2D(Object):
    """
    Property2D - represent surface properties of a 2d image
    
    Superclass: Object
    
    Property2D contains properties used to render two dimensional
    images and annotations.
    
    See Also:
    
    Actor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProperty2D, obj, update, **traits)
    
    display_location = traits.Trait('foreground',
    tvtk_base.TraitRevPrefixMap({'foreground': 1, 'background': 0}), help=\
        """
        The display_location is either background or foreground. If it is
        background, then this 2d actor will be drawn behind all 3d props
        or foreground 2d actors. If it is background, then this 2d actor
        will be drawn in front of all 3d props and background 2d actors.
        Within 2d actors of the same display_location type, order is
        determined by the order in which the 2d actors were added to the
        viewport.
        """
    )
    def _display_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayLocation,
                        self.display_location_)

    opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Opacity of this property.
        """
    )
    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    point_size = traits.Trait(1.0, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set/Get the diameter of a Point. The size is expressed in screen
        units. This is only implemented for open_gl. The default is 1.0.
        """
    )
    def _point_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointSize,
                        self.point_size)

    color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, False)

    line_stipple_repeat_factor = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the stippling repeat factor of a Line, which specifies
        how many times each bit in the pattern is to be repeated. This is
        only implemented for open_gl. The default is 1.
        """
    )
    def _line_stipple_repeat_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineStippleRepeatFactor,
                        self.line_stipple_repeat_factor)

    line_stipple_pattern = traits.Int(65535, enter_set=True, auto_set=False, help=\
        """
        Set/Get the stippling pattern of a Line, as a 16-bit binary
        pattern (1 = pixel on, 0 = pixel off). This is only implemented
        for open_gl. The default is 0x_ffff.
        """
    )
    def _line_stipple_pattern_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineStipplePattern,
                        self.line_stipple_pattern)

    line_width = traits.Trait(1.0, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set/Get the width of a Line. The width is expressed in screen
        units. This is only implemented for open_gl. The default is 1.0.
        """
    )
    def _line_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineWidth,
                        self.line_width)

    def deep_copy(self, *args):
        """
        V.deep_copy(Property2D)
        C++: void DeepCopy(Property2D *p)
        Assign one property to another.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def render(self, *args):
        """
        V.render(Viewport)
        C++: virtual void Render(Viewport *viewport)
        Have the device specific subclass render this property.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('line_width', 'GetLineWidth'),
    ('point_size', 'GetPointSize'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('line_stipple_pattern',
    'GetLineStipplePattern'), ('color', 'GetColor'), ('reference_count',
    'GetReferenceCount'), ('line_stipple_repeat_factor',
    'GetLineStippleRepeatFactor'), ('display_location',
    'GetDisplayLocation'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'display_location', 'color',
    'line_stipple_pattern', 'line_stipple_repeat_factor', 'line_width',
    'opacity', 'point_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Property2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Property2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['display_location'], ['color',
            'line_stipple_pattern', 'line_stipple_repeat_factor', 'line_width',
            'opacity', 'point_size']),
            title='Edit Property2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Property2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

