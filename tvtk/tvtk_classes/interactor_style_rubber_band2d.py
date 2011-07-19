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

from tvtk.tvtk_classes.interactor_style import InteractorStyle


class InteractorStyleRubberBand2D(InteractorStyle):
    """
    InteractorStyleRubberBand2D - A rubber band interactor for a 2d
    view
    
    Superclass: InteractorStyle
    
    InteractorStyleRubberBand2D manages interaction in a 2d view.
    Camera rotation is not allowed with this interactor style. Zooming
    affects the camera's parallel scale only, and assumes that the camera
    is in parallel projection mode. The style also allows draws a rubber
    band using the left button. All camera changes invoke
    interaction_begin_event when the button is pressed, interaction_event
    when the mouse (or wheel) is moved, and interaction_end_event when the
    button is released.  The bindings are as follows: Left mouse - Select
    (invokes a selection_changed_event). Right mouse - Zoom. Middle mouse -
    Pan. Scroll wheel - Zoom.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleRubberBand2D, obj, update, **traits)
    
    render_on_mouse_move = tvtk_base.false_bool_trait(help=\
        """
        Whether to invoke a render when the mouse moves.
        """
    )
    def _render_on_mouse_move_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderOnMouseMove,
                        self.render_on_mouse_move_)

    def _get_end_position(self):
        return self._vtk_obj.GetEndPosition()
    end_position = traits.Property(_get_end_position, help=\
        """
        
        """
    )

    def _get_interaction(self):
        return self._vtk_obj.GetInteraction()
    interaction = traits.Property(_get_interaction, help=\
        """
        Current interaction state
        """
    )

    def _get_start_position(self):
        return self._vtk_obj.GetStartPosition()
    start_position = traits.Property(_get_start_position, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('enabled', 'GetEnabled'), ('use_timers',
    'GetUseTimers'), ('pick_color', 'GetPickColor'), ('handle_observers',
    'GetHandleObservers'), ('priority', 'GetPriority'), ('debug',
    'GetDebug'), ('key_press_activation', 'GetKeyPressActivation'),
    ('reference_count', 'GetReferenceCount'), ('render_on_mouse_move',
    'GetRenderOnMouseMove'), ('timer_duration', 'GetTimerDuration'),
    ('mouse_wheel_motion_factor', 'GetMouseWheelMotionFactor'))
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'render_on_mouse_move', 'use_timers', 'key_press_activation_value',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleRubberBand2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleRubberBand2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'render_on_mouse_move',
            'use_timers'], [], ['key_press_activation_value',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration']),
            title='Edit InteractorStyleRubberBand2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleRubberBand2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

