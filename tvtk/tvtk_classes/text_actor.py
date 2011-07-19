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

from tvtk.tvtk_classes.actor2d import Actor2D


class TextActor(Actor2D):
    """
    TextActor - An actor that displays text. Scaled or unscaled
    
    Superclass: Actor2D
    
    TextActor can be used to place text annotation into a window. When
    text_scale_mode is NONE, the text is fixed font and operation is the
    same as a PolyDataMapper2D/vtkActor2D pair. When text_scale_mode is
    VIEWPORT, the font resizes such that it maintains a consistent size
    relative to the viewport in which it is rendered. When text_scale_mode
    is PROP, the font resizes such that the text fits inside the box
    defined by the position 1 & 2 coordinates. This class replaces the
    deprecated ScaledTextActor and acts as a convenient wrapper for a
    TextMapper/vtkActor2D pair. Set the text property/attributes
    through the TextProperty associated to this actor.
    
    See Also:
    
    Actor2D PolyDataMapper TextProperty FreeTypeUtilities
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextActor, obj, update, **traits)
    
    use_border_align = tvtk_base.false_bool_trait(help=\
        """
        Turn on or off the use_border_align option. When use_border_align is
        on, the bounding rectangle is used to align the text, which is
        the proper behavior when using TextRepresentation
        """
    )
    def _use_border_align_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseBorderAlign,
                        self.use_border_align_)

    text_scale_mode = traits.Trait('none',
    tvtk_base.TraitRevPrefixMap({'none': 0, 'viewport': 2, 'prop': 1}), help=\
        """
        Set how text should be scaled.  If set to
        TextActor::TEXT_SCALE_MODE_NONE, the the font size will be
        fixed by the size given in text_property.  If set to
        TextActor::TEXT_SCALE_MODE_PROP, the text will be scaled to
        fit exactly in the prop as specified by the position 1 & 2
        coordinates.  If set to TextActor::TEXT_SCALE_MODE_VIEWPORT,
        the text will be scaled based on the size of the viewport it is
        displayed in.
        """
    )
    def _text_scale_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextScaleMode,
                        self.text_scale_mode_)

    orientation = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Counterclockwise rotation around the Alignment point. Units are
        in degrees and defaults to 0. The orientation in the text
        property rotates the text in the texture map.  It will proba ly
        not give you the effect you desire.
        """
    )
    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    minimum_size = traits.Array(shape=(2,), value=(10, 10), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _minimum_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumSize,
                        self.minimum_size)

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    def _set_text_property(self, arg):
        old_val = self._get_text_property()
        self._wrap_call(self._vtk_obj.SetTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('text_property', old_val, arg)
    text_property = traits.Property(_get_text_property, _set_text_property, help=\
        """
        Set/Get the text property.
        """
    )

    alignment_point = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This method is being depricated.  Use set_justification and
        set_vertical_justification in text property instead. Set/Get the
        Alignment point if zero (default), the text aligns itself to the
        bottom left corner (which is defined by the position_coordinate)
        otherwise the text aligns itself to corner/midpoint or centre
              6   7   8
              3   4   5
              0   1   2
          This is the same as setting the text_property's justification.
        Currently text_actor is not oriented around its alignment_point.
        """
    )
    def _alignment_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlignmentPoint,
                        self.alignment_point)

    def _get_input(self):
        return self._vtk_obj.GetInput()
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        arg)
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the text string to be displayed. "\n" is recognized as a
        carriage return/linefeed (line separator). The characters must be
        in the ISO-8859-1 encoding. Convenience method to the underlying
        mapper
        """
    )

    maximum_line_height = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum height of a line of text as a percentage of
        the vertical area allocated to this scaled text actor. Defaults
        to 1.0. Only valid when text_scale_mode is PROP.
        """
    )
    def _maximum_line_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLineHeight,
                        self.maximum_line_height)

    def get_font_scale(self, *args):
        """
        V.get_font_scale(Viewport) -> float
        C++: static float GetFontScale(Viewport *viewport)
        Provide a font scaling based on a viewport.  This is the scaling
        factor used when the text_scale_mode is set to VIEWPORT and has
        been made public for other components to use.  This scaling
        assumes that the long dimension of the viewport is meant to be 6
        inches (a typical width of text in a paper) and then resizes
        based on if that long dimension was 72 DPI.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetFontScale, *my_args)
        return ret

    def _get_scaled_text_property(self):
        return wrap_vtk(self._vtk_obj.GetScaledTextProperty())
    scaled_text_property = traits.Property(_get_scaled_text_property, help=\
        """
        Get the scaled font.  Use compute_scaled_font to set the scale for
        a given viewport.
        """
    )

    def compute_scaled_font(self, *args):
        """
        V.compute_scaled_font(Viewport)
        C++: virtual void ComputeScaledFont(Viewport *viewport)
        Compute the scale the font should be given the viewport.  The
        result is placed in the scaled_text_property ivar.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeScaledFont, *my_args)
        return ret

    def set_non_linear_font_scale(self, *args):
        """
        V.set_non_linear_font_scale(float, int)
        C++: virtual void SetNonLinearFontScale(double exponent,
            int target)
        Enable non-linear scaling of font sizes. This is useful in
        combination with scaled text. With small windows you want to use
        the entire scaled text area. With larger windows you want to
        reduce the font size some so that the entire area is not used.
        These values modify the computed font size as follows:
          new_font_size = pow(_font_size,exponent)*pow(target,_1._0 - exponent)
        typically exponent should be around 0.7 and target should be
        around 10
        """
        ret = self._wrap_call(self._vtk_obj.SetNonLinearFontScale, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('minimum_size',
    'GetMinimumSize'), ('orientation', 'GetOrientation'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_line_height', 'GetMaximumLineHeight'), ('debug',
    'GetDebug'), ('dragable', 'GetDragable'), ('text_scale_mode',
    'GetTextScaleMode'), ('use_border_align', 'GetUseBorderAlign'),
    ('visibility', 'GetVisibility'), ('height', 'GetHeight'), ('width',
    'GetWidth'), ('pickable', 'GetPickable'), ('position2',
    'GetPosition2'), ('reference_count', 'GetReferenceCount'),
    ('position', 'GetPosition'), ('alignment_point', 'GetAlignmentPoint'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('use_bounds',
    'GetUseBounds'), ('layer_number', 'GetLayerNumber'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_border_align', 'use_bounds', 'visibility', 'text_scale_mode',
    'alignment_point', 'allocated_render_time', 'estimated_render_time',
    'height', 'layer_number', 'maximum_line_height', 'minimum_size',
    'orientation', 'position', 'position2', 'render_time_multiplier',
    'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_border_align', 'use_bounds', 'visibility'],
            ['text_scale_mode'], ['alignment_point', 'allocated_render_time',
            'estimated_render_time', 'height', 'layer_number',
            'maximum_line_height', 'minimum_size', 'orientation', 'position',
            'position2', 'render_time_multiplier', 'width']),
            title='Edit TextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

