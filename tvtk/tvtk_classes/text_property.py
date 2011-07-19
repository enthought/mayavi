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


class TextProperty(Object):
    """
    TextProperty - represent text properties.
    
    Superclass: Object
    
    TextProperty is an object that represents text properties. The
    primary properties that can be set are color, opacity, font size,
    font family horizontal and vertical justification, bold/italic/shadow
    styles.
    
    See Also:
    
    TextMapper TextActor LegendBoxActor CaptionActor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextProperty, obj, update, **traits)
    
    shadow = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable text shadow.
        """
    )
    def _shadow_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShadow,
                        self.shadow_)

    bold = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable text bolding.
        """
    )
    def _bold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBold,
                        self.bold_)

    italic = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable text italic.
        """
    )
    def _italic_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetItalic,
                        self.italic_)

    font_family = traits.Trait('arial',
    tvtk_base.TraitRevPrefixMap({'arial': 0, 'courier': 1, 'times': 2}), help=\
        """
        Set/Get the font family. Supports legacy three font family
        system.
        """
    )
    def _font_family_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontFamily,
                        self.font_family_)

    justification = traits.Trait('left',
    tvtk_base.TraitRevPrefixMap({'centered': 1, 'right': 2, 'left': 0}), help=\
        """
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
    )
    def _justification_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetJustification,
                        self.justification_)

    vertical_justification = traits.Trait('bottom',
    tvtk_base.TraitRevPrefixMap({'centered': 1, 'top': 2, 'bottom': 0}), help=\
        """
        Set/Get the vertical justification to bottom (default), middle,
        or top.
        """
    )
    def _vertical_justification_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalJustification,
                        self.vertical_justification_)

    opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the text's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
    )
    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    orientation = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the text's orientation (in degrees).
        """
    )
    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    line_spacing = traits.Float(1.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the (extra) spacing between lines, expressed as a text
        height multiplication factor.
        """
    )
    def _line_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineSpacing,
                        self.line_spacing)

    color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, False)

    font_size = traits.Trait(12, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the font size (in points).
        """
    )
    def _font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontSize,
                        self.font_size)

    line_offset = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the vertical offset (measured in pixels).
        """
    )
    def _line_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineOffset,
                        self.line_offset)

    shadow_offset = traits.Array(shape=(2,), value=(1, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _shadow_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShadowOffset,
                        self.shadow_offset)

    def get_font_family_from_string(self, *args):
        """
        V.get_font_family_from_string(string) -> int
        C++: static int GetFontFamilyFromString(const char *f)
        Set/Get the font family. Supports legacy three font family
        system.
        """
        ret = self._wrap_call(self._vtk_obj.GetFontFamilyFromString, *args)
        return ret

    def _get_font_family_min_value(self):
        return self._vtk_obj.GetFontFamilyMinValue()
    font_family_min_value = traits.Property(_get_font_family_min_value, help=\
        """
        Set/Get the font family. Supports legacy three font family
        system.
        """
    )

    def get_shadow_color(self, *args):
        """
        V.get_shadow_color([float, float, float])
        C++: void GetShadowColor(double color[3])
        Get the shadow color. It is computed from the Color ivar
        """
        ret = self._wrap_call(self._vtk_obj.GetShadowColor, *args)
        return ret

    def set_font_family_as_string(self, *args):
        """
        V.set_font_family_as_string(string)
        C++: void SetFontFamilyAsString(char *)
        Set/Get the font family. Supports legacy three font family
        system.
        """
        ret = self._wrap_call(self._vtk_obj.SetFontFamilyAsString, *args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(TextProperty)
        C++: void ShallowCopy(TextProperty *tprop)
        Shallow copy of a text property.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('justification', 'GetJustification'),
    ('font_size', 'GetFontSize'), ('orientation', 'GetOrientation'),
    ('line_offset', 'GetLineOffset'), ('line_spacing', 'GetLineSpacing'),
    ('debug', 'GetDebug'), ('vertical_justification',
    'GetVerticalJustification'), ('color', 'GetColor'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('italic',
    'GetItalic'), ('shadow_offset', 'GetShadowOffset'),
    ('reference_count', 'GetReferenceCount'), ('shadow', 'GetShadow'),
    ('font_family', 'GetFontFamily'), ('bold', 'GetBold'))
    
    _full_traitnames_list_ = \
    (['bold', 'debug', 'global_warning_display', 'italic', 'shadow',
    'font_family', 'justification', 'vertical_justification', 'color',
    'font_size', 'line_offset', 'line_spacing', 'opacity', 'orientation',
    'shadow_offset'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextProperty, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['bold', 'italic', 'shadow'], ['font_family',
            'justification', 'vertical_justification'], ['color', 'font_size',
            'line_offset', 'line_spacing', 'opacity', 'orientation',
            'shadow_offset']),
            title='Edit TextProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

