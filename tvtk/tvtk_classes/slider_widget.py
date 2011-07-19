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

from tvtk.tvtk_classes.abstract_widget import AbstractWidget


class SliderWidget(AbstractWidget):
    """
    SliderWidget - set a value by manipulating a slider
    
    Superclass: AbstractWidget
    
    The SliderWidget is used to set a scalar value in an application. 
    This class assumes that a slider is moved along a 1d parameter space
    (e.g., a spherical bead that can be moved along a tube).  Moving the
    slider modifies the value of the widget, which can be used to set
    parameters on other objects. Note that the actual appearance of the
    widget depends on the specific representation for the widget.
    
    To use this widget, set the widget representation. The representation
    is assumed to consist of a tube, two end caps, and a slider (the
    details may vary depending on the particulars of the representation).
    Then in the representation you will typically set minimum and maximum
    value, as well as the current value. The position of the slider must
    also be set, as well as various properties.
    
    Event Bindings:
    
    By default, the widget responds to the following VTK events (i.e., it
    watches the RenderWindowInteractor for these events):
    
    If the slider bead is selected:
      left_button_press_event - select slider (if on slider)
      left_button_release_event - release slider (if selected)
      mouse_move_event - move slider If the end caps or slider tube are
    selected:
      left_button_press_event - move (or animate) to cap or point on tube; 
    
    Note that the event bindings described above can be changed using
    this class's WidgetEventTranslator. This class translates VTK
    events into the SliderWidget's widget events:
    
    
      WidgetEvent::Select -- some part of the widget has been selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Move -- a request for slider motion has been
    invoked 
    
    In turn, when these widget events are processed, the SliderWidget
    invokes the following VTK events on itself (which observers can
    listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSliderWidget, obj, update, **traits)
    
    animation_mode = traits.Trait('jump',
    tvtk_base.TraitRevPrefixMap({'jump': 1, 'animate': 2, 'off': 0}), help=\
        """
        Control the behavior of the slider when selecting the tube or
        caps. If Jump, then selecting the tube, left cap, or right cap
        causes the slider to jump to the selection point. If the mode is
        Animate, the slider moves towards the selection point in
        number_of_animation_steps number of steps. If Off, then the slider
        does not move.
        """
    )
    def _animation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAnimationMode,
                        self.animation_mode_)

    number_of_animation_steps = traits.Trait(24, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of animation steps to take if the animation
        mode is set to animate.
        """
    )
    def _number_of_animation_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfAnimationSteps,
                        self.number_of_animation_steps)

    def set_representation(self, *args):
        """
        V.set_representation(SliderRepresentation)
        C++: void SetRepresentation(SliderRepresentation *r)
        Specify an instance of WidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of Prop so it can be added to the renderer
        independent of the widget.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRepresentation, *my_args)
        return ret

    _updateable_traits_ = \
    (('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('enabled',
    'GetEnabled'), ('manages_cursor', 'GetManagesCursor'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('number_of_animation_steps',
    'GetNumberOfAnimationSteps'), ('reference_count',
    'GetReferenceCount'), ('animation_mode', 'GetAnimationMode'),
    ('key_press_activation', 'GetKeyPressActivation'), ('process_events',
    'GetProcessEvents'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'process_events',
    'animation_mode', 'key_press_activation_value',
    'number_of_animation_steps', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SliderWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SliderWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'manages_cursor',
            'process_events'], ['animation_mode'], ['key_press_activation_value',
            'number_of_animation_steps', 'priority']),
            title='Edit SliderWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SliderWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

