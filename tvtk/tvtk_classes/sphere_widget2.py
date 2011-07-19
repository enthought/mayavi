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


class SphereWidget2(AbstractWidget):
    """
    SphereWidget2 - 3d widget for manipulating a point on a sphere
    
    Superclass: AbstractWidget
    
    This 3d widget interacts with a SphereRepresentation class (i.e.,
    it handles the events that drive its corresponding representation).
    It can be used to position a point on a sphere (for example, to place
    a light or camera), or to position a sphere in a scene, including
    translating and scaling the sphere.
    
    A nice feature of SphereWidget2, like any 3d widget, is that it
    will work in combination with the current interactor style (or any
    other interactor observer). That is, if SphereWidget2 does not
    handle an event, then all other registered observers (including the
    interactor style) have an opportunity to process the event.
    Otherwise, the SphereWidget2 will terminate the processing of the
    event that it handles.
    
    To use this widget, you generally pair it with a
    SphereRepresentation (or a subclass). Variuos options are
    available in the representation for controlling how the widget
    appears, and how the widget functions.
    
    Event Bindings:
    
    By default, the widget responds to the following VTK events (i.e., it
    watches the RenderWindowInteractor for these events):
    
    If the handle or sphere are selected:
      left_button_press_event - select the handle or sphere
      left_button_release_event - release the handle ot sphere
      mouse_move_event - move the handle or translate the sphere In all the
    cases, independent of what is picked, the widget responds to the
    following VTK events:
      middle_button_press_event - translate the representation
      middle_button_release_event - stop translating the representation
      right_button_press_event - scale the widget's representation
      right_button_release_event - stop scaling the representation
      mouse_move_event - scale (if right button) or move (if middle button)
    the widget 
    
    Note that the event bindings described above can be changed using
    this class's WidgetEventTranslator. This class translates VTK
    events into the SphereWidget2's widget events:
    
    
      WidgetEvent::Select -- some part of the widget has been selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Scale -- some part of the widget has been selected
      WidgetEvent::EndScale -- the selection process has completed
      WidgetEvent::Translate -- some part of the widget has been
    selected
      WidgetEvent::EndTranslate -- the selection process has completed
      WidgetEvent::Move -- a request for motion has been invoked 
    
    In turn, when these widget events are processed, the SphereWidget2
    invokes the following VTK events on itself (which observers can
    listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    
    Caveats:
    
    Note that in some cases the widget can be picked even when it is
    "behind" other actors.  This is an intended feature and not a bug.
    
    This class, and the affiliated SphereRepresentation, are second
    generation VTK widgets. An earlier version of this functionality was
    defined in the class SphereWidget.
    
    See Also:
    
    SphereRepresentation SphereWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSphereWidget2, obj, update, **traits)
    
    translation_enabled = tvtk_base.true_bool_trait(help=\
        """
        Control the behavior of the widget (i.e., how it processes
        events). Translation, and scaling can all be enabled and
        disabled.
        """
    )
    def _translation_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationEnabled,
                        self.translation_enabled_)

    scaling_enabled = tvtk_base.true_bool_trait(help=\
        """
        Control the behavior of the widget (i.e., how it processes
        events). Translation, and scaling can all be enabled and
        disabled.
        """
    )
    def _scaling_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalingEnabled,
                        self.scaling_enabled_)

    def set_representation(self, *args):
        """
        V.set_representation(SphereRepresentation)
        C++: void SetRepresentation(SphereRepresentation *r)
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
    'GetPriority'), ('debug', 'GetDebug'), ('scaling_enabled',
    'GetScalingEnabled'), ('reference_count', 'GetReferenceCount'),
    ('translation_enabled', 'GetTranslationEnabled'),
    ('key_press_activation', 'GetKeyPressActivation'), ('process_events',
    'GetProcessEvents'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'process_events',
    'scaling_enabled', 'translation_enabled',
    'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SphereWidget2, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SphereWidget2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'manages_cursor',
            'process_events', 'scaling_enabled', 'translation_enabled'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit SphereWidget2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SphereWidget2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

