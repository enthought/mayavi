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


class AngleWidget(AbstractWidget):
    """
    AngleWidget - measure the angle between two rays (defined by three
    points)
    
    Superclass: AbstractWidget
    
    The AngleWidget is used to measure the angle between two rays
    (defined by three points). The three points (two end points and a
    center) can be positioned independently, and when they are released,
    a special place_point_event is invoked so that special operations may
    be take to reposition the point (snap to grid, etc.) The widget has
    two different modes of interaction: when initially defined (i.e.,
    placing the three points) and then a manipulate mode (adjusting the
    position of the three points).
    
    To use this widget, specify an instance of AngleWidget and a
    representation (a subclass of AngleRepresentation). The widget is
    implemented using three instances of HandleWidget which are used
    to position the three points. The representations for these handle
    widgets are provided by the AngleRepresentation.
    
    Event Bindings:
    
    By default, the widget responds to the following VTK events (i.e., it
    watches the RenderWindowInteractor for these events):
    
    
      left_button_press_event - add a point or select a handle
      mouse_move_event - position the second or third point, or move a
    handle
      left_button_release_event - release the selected handle 
    
    Note that the event bindings described above can be changed using
    this class's WidgetEventTranslator. This class translates VTK
    events into the AngleWidget's widget events:
    
    
      WidgetEvent::AddPoint -- add one point; depending on the state
                                  it may the first, second or third point
                                  added. Or, if near a handle, select the
    handle.
      WidgetEvent::Move -- position the second or third point, or move
    the
                              handle depending on the state.
      WidgetEvent::EndSelect -- the handle manipulation process has
    completed. 
    
    This widget invokes the following VTK events on itself (which
    observers can listen for):
    
    
      Command::StartInteractionEvent (beginning to interact)
      Command::EndInteractionEvent (completing interaction)
      Command::InteractionEvent (moving a handle)
      Command::PlacePointEvent (after a point is positioned;
                                   call data includes handle id (0,1,2)) 
    
    See Also:
    
    HandleWidget DistanceWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAngleWidget, obj, update, **traits)
    
    def is_angle_valid(self):
        """
        V.is_angle_valid() -> int
        C++: int IsAngleValid()
        A flag indicates whether the angle is valid. The angle value only
        becomes valid after two of the three points are placed.
        """
        ret = self._vtk_obj.IsAngleValid()
        return ret
        

    def is_widget_defined(self):
        """
        V.is_widget_defined() -> int
        C++: virtual int IsWidgetDefined()
        Has the widget been defined completely yet ? ie. Have the end
        points been laid and is it in Manipulate mode ?
        """
        ret = self._vtk_obj.IsWidgetDefined()
        return ret
        

    def set_representation(self, *args):
        """
        V.set_representation(AngleRepresentation)
        C++: void SetRepresentation(AngleRepresentation *r)
        Specify an instance of WidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of Prop so it can be added to the renderer
        independent of the widget.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRepresentation, *my_args)
        return ret

    def widget_is_defined(self):
        """
        V.widget_is_defined()
        C++: virtual void WidgetIsDefined()
        Set the state of the widget to "defined" (in case its widget and
        its representation were initialized programmatically). This must
        generally be followed by a Render() for things to visually take
        effect.
        """
        ret = self._vtk_obj.WidgetIsDefined()
        return ret
        

    _updateable_traits_ = \
    (('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('enabled',
    'GetEnabled'), ('manages_cursor', 'GetManagesCursor'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('reference_count',
    'GetReferenceCount'), ('key_press_activation',
    'GetKeyPressActivation'), ('process_events', 'GetProcessEvents'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'process_events',
    'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AngleWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AngleWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'manages_cursor',
            'process_events'], [], ['key_press_activation_value', 'priority']),
            title='Edit AngleWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AngleWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

