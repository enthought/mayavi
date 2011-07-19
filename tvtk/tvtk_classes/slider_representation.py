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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class SliderRepresentation(WidgetRepresentation):
    """
    SliderRepresentation - abstract class defines the representation
    for a SliderWidget
    
    Superclass: WidgetRepresentation
    
    This abstract class is used to specify how the SliderWidget should
    interact with representations of the SliderWidget. This class may
    be subclassed so that alternative representations can be created. The
    class defines an API, and a default implementation, that the
    SliderWidget interacts with to render itself in the scene.
    
    See Also:
    
    SliderWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSliderRepresentation, obj, update, **traits)
    
    show_slider_label = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether the slider text label should be displayed. This
        is a number corresponding to the current Value of this widget.
        """
    )
    def _show_slider_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowSliderLabel,
                        self.show_slider_label_)

    tube_width = traits.Trait(0.025, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set the width of the tube (in normalized display coordinates) on
        which the slider moves. By default the width is 0.05.
        """
    )
    def _tube_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTubeWidth,
                        self.tube_width)

    label_format = traits.String(r"%0.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the slider value.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    maximum_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the current maximum value that the slider can take. Setting
        the maximum value less than the minimum value will cause the
        minimum value to change to (maximum value - 1).
        """
    )
    def _maximum_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumValue,
                        self.maximum_value)

    slider_length = traits.Trait(0.05, traits.Range(0.01, 0.5, enter_set=True, auto_set=False), help=\
        """
        Specify the length of the slider shape (in normalized display
        coordinates [0.01,0.5]). The slider length by default is 0.05.
        """
    )
    def _slider_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliderLength,
                        self.slider_length)

    label_height = traits.Trait(0.05, traits.Range(0.0, 2.0, enter_set=True, auto_set=False), help=\
        """
        Specify the relative height of the label as compared to the
        length of the slider.
        """
    )
    def _label_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelHeight,
                        self.label_height)

    end_cap_length = traits.Trait(0.025, traits.Range(0.0, 0.25, enter_set=True, auto_set=False), help=\
        """
        Specify the length of each end cap (in normalized coordinates
        [0.0,0.25]). By default the length is 0.025. If the end cap
        length is set to 0.0, then the end cap will not display at all.
        """
    )
    def _end_cap_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndCapLength,
                        self.end_cap_length)

    title_height = traits.Trait(0.15, traits.Range(0.0, 2.0, enter_set=True, auto_set=False), help=\
        """
        Specify the relative height of the title as compared to the
        length of the slider.
        """
    )
    def _title_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleHeight,
                        self.title_height)

    title_text = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Specify the label text for this widget. If the value is not set,
        or set to the empty string "", then the label text is not
        displayed.
        """
    )
    def _title_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleText,
                        self.title_text)

    end_cap_width = traits.Trait(0.05, traits.Range(0.0, 0.25, enter_set=True, auto_set=False), help=\
        """
        Specify the width of each end cap (in normalized coordinates
        [0.0,0.25]). By default the width is twice the tube width.
        """
    )
    def _end_cap_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndCapWidth,
                        self.end_cap_width)

    value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify the current value for the widget. The value should lie
        between the minimum and maximum values.
        """
    )
    def _value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValue,
                        self.value)

    minimum_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the current minimum value that the slider can take. Setting
        the minimum value greater than the maximum value will cause the
        maximum value to grow to (minimum value + 1).
        """
    )
    def _minimum_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumValue,
                        self.minimum_value)

    slider_width = traits.Trait(0.05, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set the width of the slider in the directions orthogonal to the
        slider axis. Using this it is possible to create ellipsoidal and
        hockey puck sliders (in some subclasses). By default the width is
        0.05.
        """
    )
    def _slider_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliderWidth,
                        self.slider_width)

    def _get_current_t(self):
        return self._vtk_obj.GetCurrentT()
    current_t = traits.Property(_get_current_t, help=\
        """
        Methods to interface with the SliderWidget. Subclasses of this
        class actually do something.
        """
    )

    def _get_picked_t(self):
        return self._vtk_obj.GetPickedT()
    picked_t = traits.Property(_get_picked_t, help=\
        """
        Methods to interface with the SliderWidget. Subclasses of this
        class actually do something.
        """
    )

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('need_to_render', 'GetNeedToRender'), ('dragable',
    'GetDragable'), ('title_text', 'GetTitleText'), ('tube_width',
    'GetTubeWidth'), ('end_cap_width', 'GetEndCapWidth'),
    ('show_slider_label', 'GetShowSliderLabel'), ('visibility',
    'GetVisibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('place_factor', 'GetPlaceFactor'),
    ('use_bounds', 'GetUseBounds'), ('minimum_value', 'GetMinimumValue'),
    ('title_height', 'GetTitleHeight'), ('slider_length',
    'GetSliderLength'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('label_height', 'GetLabelHeight'),
    ('debug', 'GetDebug'), ('maximum_value', 'GetMaximumValue'), ('value',
    'GetValue'), ('label_format', 'GetLabelFormat'), ('pickable',
    'GetPickable'), ('slider_width', 'GetSliderWidth'),
    ('reference_count', 'GetReferenceCount'), ('end_cap_length',
    'GetEndCapLength'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'show_slider_label', 'use_bounds', 'visibility',
    'allocated_render_time', 'end_cap_length', 'end_cap_width',
    'estimated_render_time', 'handle_size', 'label_format',
    'label_height', 'maximum_value', 'minimum_value', 'place_factor',
    'render_time_multiplier', 'slider_length', 'slider_width',
    'title_height', 'title_text', 'tube_width', 'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SliderRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SliderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'show_slider_label', 'use_bounds',
            'visibility'], [], ['allocated_render_time', 'end_cap_length',
            'end_cap_width', 'estimated_render_time', 'handle_size',
            'label_format', 'label_height', 'maximum_value', 'minimum_value',
            'place_factor', 'render_time_multiplier', 'slider_length',
            'slider_width', 'title_height', 'title_text', 'tube_width', 'value']),
            title='Edit SliderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SliderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

