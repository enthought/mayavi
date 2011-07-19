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


class ContinuousValueWidget(AbstractWidget):
    """
    ContinuousValueWidget - set a value by manipulating something
    
    Superclass: AbstractWidget
    
    The ContinuousValueWidget is used to adjust a scalar value in an
    application. Note that the actual appearance of the widget depends on
    the specific representation for the widget.
    
    To use this widget, set the widget representation. (the details may
    vary depending on the particulars of the representation).
    
    Event Bindings:
    
    By default, the widget responds to the following VTK events (i.e., it
    watches the RenderWindowInteractor for these events):
    
    If the slider bead is selected:
      left_button_press_event - select slider
      left_button_release_event - release slider
      mouse_move_event - move slider 
    
    Note that the event bindings described above can be changed using
    this class's WidgetEventTranslator. This class translates VTK
    events into the ContinuousValueWidget's widget events:
    
    
      WidgetEvent::Select -- some part of the widget has been selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Move -- a request for slider motion has been
    invoked 
    
    In turn, when these widget events are processed, the
    ContinuousValueWidget invokes the following VTK events on itself
    (which observers can listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContinuousValueWidget, obj, update, **traits)
    
    value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get the value for this widget.
        """
    )
    def _value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValue,
                        self.value)

    def set_representation(self, *args):
        """
        V.set_representation(ContinuousValueWidgetRepresentation)
        C++: void SetRepresentation(
            ContinuousValueWidgetRepresentation *r)
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
    'GetEnabled'), ('value', 'GetValue'), ('manages_cursor',
    'GetManagesCursor'), ('priority', 'GetPriority'), ('debug',
    'GetDebug'), ('reference_count', 'GetReferenceCount'),
    ('key_press_activation', 'GetKeyPressActivation'), ('process_events',
    'GetProcessEvents'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'process_events',
    'key_press_activation_value', 'priority', 'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContinuousValueWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ContinuousValueWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'manages_cursor',
            'process_events'], [], ['key_press_activation_value', 'priority',
            'value']),
            title='Edit ContinuousValueWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContinuousValueWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

