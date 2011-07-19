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

from tvtk.tvtk_classes.interactor_style_rubber_band2d import InteractorStyleRubberBand2D


class InteractorStyleAreaSelectHover(InteractorStyleRubberBand2D):
    """
    InteractorStyleAreaSelectHover - An interactor style for an area
    tree view
    
    Superclass: InteractorStyleRubberBand2D
    
    The InteractorStyleAreaSelectHover specifically works with
    pipelines that create a hierarchical tree.  Such pipelines will have
    a AreaLayout filter which must be passed to this interactor style
    for it to function correctly. This interactor style allows only 2d
    panning and zooming, rubber band selection and provides a balloon
    containing the name of the vertex hovered over.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleAreaSelectHover, obj, update, **traits)
    
    use_rectangular_coordinates = tvtk_base.false_bool_trait(help=\
        """
        Determine whether or not to use rectangular coordinates instead
        of polar coordinates.
        """
    )
    def _use_rectangular_coordinates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseRectangularCoordinates,
                        self.use_rectangular_coordinates_)

    def _get_layout(self):
        return wrap_vtk(self._vtk_obj.GetLayout())
    def _set_layout(self, arg):
        old_val = self._get_layout()
        self._wrap_call(self._vtk_obj.SetLayout,
                        deref_vtk(arg))
        self.trait_property_changed('layout', old_val, arg)
    layout = traits.Property(_get_layout, _set_layout, help=\
        """
        Must be set to the AreaLayout used to compute the bounds of
        each vertex.
        """
    )

    high_light_width = traits.Float(4.0, enter_set=True, auto_set=False, help=\
        """
        The width of the line around the hovered vertex.
        """
    )
    def _high_light_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHighLightWidth,
                        self.high_light_width)

    label_field = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the field to use when displaying text in the hover
        balloon.
        """
    )
    def _label_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelField,
                        self.label_field)

    def get_id_at_pos(self, *args):
        """
        V.get_id_at_pos(int, int) -> int
        C++: IdType GetIdAtPos(int x, int y)
        Obtain the tree vertex id at the position specified.
        """
        ret = self._wrap_call(self._vtk_obj.GetIdAtPos, *args)
        return ret

    def set_high_light_color(self, *args):
        """
        V.set_high_light_color(float, float, float)
        C++: void SetHighLightColor(double r, double g, double b)
        Set the color used to highlight the hovered vertex.
        """
        ret = self._wrap_call(self._vtk_obj.SetHighLightColor, *args)
        return ret

    _updateable_traits_ = \
    (('high_light_width', 'GetHighLightWidth'),
    ('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('use_timers', 'GetUseTimers'),
    ('enabled', 'GetEnabled'), ('pick_color', 'GetPickColor'),
    ('handle_observers', 'GetHandleObservers'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('use_rectangular_coordinates',
    'GetUseRectangularCoordinates'), ('label_field', 'GetLabelField'),
    ('key_press_activation', 'GetKeyPressActivation'), ('reference_count',
    'GetReferenceCount'), ('render_on_mouse_move',
    'GetRenderOnMouseMove'), ('timer_duration', 'GetTimerDuration'),
    ('mouse_wheel_motion_factor', 'GetMouseWheelMotionFactor'))
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'render_on_mouse_move', 'use_rectangular_coordinates', 'use_timers',
    'high_light_width', 'key_press_activation_value', 'label_field',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleAreaSelectHover, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleAreaSelectHover properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'render_on_mouse_move',
            'use_rectangular_coordinates', 'use_timers'], [], ['high_light_width',
            'key_press_activation_value', 'label_field',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration']),
            title='Edit InteractorStyleAreaSelectHover properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleAreaSelectHover properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

