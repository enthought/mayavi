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


class CornerAnnotation(Actor2D):
    """
    CornerAnnotation - text annotation in four corners
    
    Superclass: Actor2D
    
    This is an annotation object that manages four text actors / mappers
    to provide annotation in the four corners of a viewport
    
    See Also:
    
    Actor2D TextMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCornerAnnotation, obj, update, **traits)
    
    show_slice_and_image = tvtk_base.true_bool_trait(help=\
        """
        Even if there is an image actor, should `slice' and `image' be
        displayed?
        """
    )
    def _show_slice_and_image_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowSliceAndImage,
                        self.show_slice_and_image_)

    linear_font_scale_factor = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get font scaling factors The font size, f, is calculated as
        the largest possible value such that the annotations for the
        given viewport do not overlap. This font size is scaled
        non-linearly with the viewport size, to maintain an acceptable
        readable size at larger viewport sizes, without being too big. f'
        = linear_scale * pow(f,nonlinear_scale)
        """
    )
    def _linear_font_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLinearFontScaleFactor,
                        self.linear_font_scale_factor)

    nonlinear_font_scale_factor = traits.Float(0.35, enter_set=True, auto_set=False, help=\
        """
        Set/Get font scaling factors The font size, f, is calculated as
        the largest possible value such that the annotations for the
        given viewport do not overlap. This font size is scaled
        non-linearly with the viewport size, to maintain an acceptable
        readable size at larger viewport sizes, without being too big. f'
        = linear_scale * pow(f,nonlinear_scale)
        """
    )
    def _nonlinear_font_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNonlinearFontScaleFactor,
                        self.nonlinear_font_scale_factor)

    def _get_image_actor(self):
        return wrap_vtk(self._vtk_obj.GetImageActor())
    def _set_image_actor(self, arg):
        old_val = self._get_image_actor()
        self._wrap_call(self._vtk_obj.SetImageActor,
                        deref_vtk(arg))
        self.trait_property_changed('image_actor', old_val, arg)
    image_actor = traits.Property(_get_image_actor, _set_image_actor, help=\
        """
        Set an image actor to look at for slice information
        """
    )

    maximum_font_size = traits.Int(200, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum/maximum size font that will be shown. If the
        font drops below the minimum size it will not be rendered.
        """
    )
    def _maximum_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumFontSize,
                        self.maximum_font_size)

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    def _set_text_property(self, arg):
        old_val = self._get_text_property()
        self._wrap_call(self._vtk_obj.SetTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('text_property', old_val, arg)
    text_property = traits.Property(_get_text_property, _set_text_property, help=\
        """
        Set/Get the text property of all corners.
        """
    )

    level_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the value to scale the level by.
        """
    )
    def _level_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevelScale,
                        self.level_scale)

    minimum_font_size = traits.Int(6, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum/maximum size font that will be shown. If the
        font drops below the minimum size it will not be rendered.
        """
    )
    def _minimum_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumFontSize,
                        self.minimum_font_size)

    level_shift = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the value to shift the level by.
        """
    )
    def _level_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevelShift,
                        self.level_shift)

    maximum_line_height = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum height of a line of text as a percentage of
        the vertical area allocated to this scaled text actor. Defaults
        to 1.0
        """
    )
    def _maximum_line_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLineHeight,
                        self.maximum_line_height)

    def _get_window_level(self):
        return wrap_vtk(self._vtk_obj.GetWindowLevel())
    def _set_window_level(self, arg):
        old_val = self._get_window_level()
        self._wrap_call(self._vtk_obj.SetWindowLevel,
                        deref_vtk(arg))
        self.trait_property_changed('window_level', old_val, arg)
    window_level = traits.Property(_get_window_level, _set_window_level, help=\
        """
        Set an instance of ImageMapToWindowLevelColors to use for
        looking at window level changes
        """
    )

    text = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the text to be displayed for each corner
        """
    )
    def _text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetText,
                        self.text)

    def clear_all_texts(self):
        """
        V.clear_all_texts()
        C++: void ClearAllTexts()
        Set/Get the text to be displayed for each corner
        """
        ret = self._vtk_obj.ClearAllTexts()
        return ret
        

    def copy_all_texts_from(self, *args):
        """
        V.copy_all_texts_from(CornerAnnotation)
        C++: void CopyAllTextsFrom(CornerAnnotation *ca)
        Set/Get the text to be displayed for each corner
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyAllTextsFrom, *my_args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'),
    ('show_slice_and_image', 'GetShowSliceAndImage'), ('level_shift',
    'GetLevelShift'), ('text', 'GetText'), ('level_scale',
    'GetLevelScale'), ('visibility', 'GetVisibility'), ('height',
    'GetHeight'), ('minimum_font_size', 'GetMinimumFontSize'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('use_bounds',
    'GetUseBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('layer_number', 'GetLayerNumber'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('maximum_line_height', 'GetMaximumLineHeight'), ('debug',
    'GetDebug'), ('linear_font_scale_factor', 'GetLinearFontScaleFactor'),
    ('width', 'GetWidth'), ('maximum_font_size', 'GetMaximumFontSize'),
    ('position2', 'GetPosition2'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'),
    ('nonlinear_font_scale_factor', 'GetNonlinearFontScaleFactor'),
    ('pickable', 'GetPickable'), ('dragable', 'GetDragable'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'show_slice_and_image', 'use_bounds', 'visibility',
    'allocated_render_time', 'estimated_render_time', 'height',
    'layer_number', 'level_scale', 'level_shift',
    'linear_font_scale_factor', 'maximum_font_size',
    'maximum_line_height', 'minimum_font_size',
    'nonlinear_font_scale_factor', 'position', 'position2',
    'render_time_multiplier', 'text', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CornerAnnotation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CornerAnnotation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['show_slice_and_image', 'use_bounds', 'visibility'],
            [], ['allocated_render_time', 'estimated_render_time', 'height',
            'layer_number', 'level_scale', 'level_shift',
            'linear_font_scale_factor', 'maximum_font_size',
            'maximum_line_height', 'minimum_font_size',
            'nonlinear_font_scale_factor', 'position', 'position2',
            'render_time_multiplier', 'text', 'width']),
            title='Edit CornerAnnotation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CornerAnnotation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

