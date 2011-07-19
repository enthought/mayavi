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


class HandleWidget(AbstractWidget):
    """
    HandleWidget - a general widget for moving handles
    
    Superclass: AbstractWidget
    
    The HandleWidget is used to position a handle.  A handle is a
    widget with a position (in display and world space). Various
    appearances are available depending on its associated representation.
    The widget provides methods for translation, including constrained
    translation along coordinate axes. To use this widget, create and
    associate a representation with the widget.
    
    Event Bindings:
    
    By default, the widget responds to the following VTK events (i.e., it
    watches the RenderWindowInteractor for these events):
    
    
      left_button_press_event - select focal point of widget
      left_button_release_event - end selection
      middle_button_press_event - translate widget
      middle_button_release_event - end translation
      right_button_press_event - scale widget
      right_button_release_event - end scaling
      mouse_move_event - interactive movement across widget 
    
    Note that the event bindings described above can be changed using
    this class's WidgetEventTranslator. This class translates VTK
    events into the HandleWidget's widget events:
    
    
      WidgetEvent::Select -- focal point is being selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Translate -- translate the widget
      WidgetEvent::EndTranslate -- end widget translation
      WidgetEvent::Scale -- scale the widget
      WidgetEvent::EndScale -- end scaling the widget
      WidgetEvent::Move -- a request for widget motion 
    
    In turn, when these widget events are processed, the HandleWidget
    invokes the following VTK events on itself (which observers can
    listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHandleWidget, obj, update, **traits)
    
    allow_handle_resize = tvtk_base.true_bool_trait(help=\
        """
        Allow resizing of handles ? By default the right mouse button
        scales the handle size.
        """
    )
    def _allow_handle_resize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowHandleResize,
                        self.allow_handle_resize_)

    enable_axis_constraint = tvtk_base.true_bool_trait(help=\
        """
        Enable / disable axis constrained motion of the handles. By
        default the widget responds to the shift modifier to constrain
        the handle along the axis closest aligned with the motion vector.
        """
    )
    def _enable_axis_constraint_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableAxisConstraint,
                        self.enable_axis_constraint_)

    def _get_widget_state(self):
        return self._vtk_obj.GetWidgetState()
    widget_state = traits.Property(_get_widget_state, help=\
        """
        Get the widget state.
        """
    )

    def set_representation(self, *args):
        """
        V.set_representation(HandleRepresentation)
        C++: void SetRepresentation(HandleRepresentation *r)
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
    ('enable_axis_constraint', 'GetEnableAxisConstraint'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('enabled',
    'GetEnabled'), ('manages_cursor', 'GetManagesCursor'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('reference_count',
    'GetReferenceCount'), ('allow_handle_resize', 'GetAllowHandleResize'),
    ('key_press_activation', 'GetKeyPressActivation'), ('process_events',
    'GetProcessEvents'))
    
    _full_traitnames_list_ = \
    (['allow_handle_resize', 'debug', 'enable_axis_constraint', 'enabled',
    'global_warning_display', 'key_press_activation', 'manages_cursor',
    'process_events', 'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HandleWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HandleWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['allow_handle_resize', 'enable_axis_constraint',
            'enabled', 'key_press_activation', 'manages_cursor',
            'process_events'], [], ['key_press_activation_value', 'priority']),
            title='Edit HandleWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HandleWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

