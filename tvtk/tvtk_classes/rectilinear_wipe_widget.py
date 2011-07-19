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


class RectilinearWipeWidget(AbstractWidget):
    """
    RectilinearWipeWidget - interactively control an instance of
    ImageRectilinearWipe filter
    
    Superclass: AbstractWidget
    
    The RectilinearWipeWidget is used to interactively control an
    instance of ImageRectilinearWipe (and an associated ImageActor
    used to display the rectilinear wipe). A rectilinear wipe is a 2x2
    checkerboard pattern created by combining two separate images, where
    various combinations of the checker squares are possible. Using this
    widget, the user can adjust the layout of the checker pattern, such
    as moving the center point, moving the horizontal separator, or
    moving the vertical separator. These capabilities are particularly
    useful for comparing two images.
    
    To use this widget, specify its representation (by default the
    representation is an instance of RectilinearWipeProp). The
    representation generally requires that you specify an instance of
    ImageRectilinearWipe and an instance of ImageActor. Other
    instance variables may also be required to be set -- see the
    documentation for RectilinearWipeProp (or appropriate subclass).
    
    By default, the widget responds to the following events:
    
    Selecting the center point, horizontal separator, and verticel
    separator:
      left_button_press_event - move the separators
      left_button_release_event - release the separators
      mouse_move_event - move the separators  Selecting the center point
    allows you to move the horizontal and vertical separators
    simultaneously. Otherwise only horizontal or vertical motion is
    possible/
    
    Note that the event bindings described above can be changed using
    this class's WidgetEventTranslator. This class translates VTK
    events into the RectilinearWipeWidget's widget events:
    
    
      WidgetEvent::Select -- some part of the widget has been selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Move -- a request for motion has been invoked 
    
    In turn, when these widget events are processed, the
    RectilinearWipeWidget invokes the following VTK events (which
    observers can listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    
    Caveats:
    
    The appearance of this widget is defined by its representation,
    including any properties associated with the representation.  The
    widget representation is a type of Prop that defines a particular
    API that works with this widget. If desired, the Prop may be
    subclassed to create new looks for the widget.
    
    See Also:
    
    RectilinearWipeProp ImageRectilinearWipe ImageActor
    CheckerboardWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRectilinearWipeWidget, obj, update, **traits)
    
    def set_representation(self, *args):
        """
        V.set_representation(RectilinearWipeRepresentation)
        C++: void SetRepresentation(RectilinearWipeRepresentation *r)
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
    'GetPriority'), ('debug', 'GetDebug'), ('reference_count',
    'GetReferenceCount'), ('key_press_activation',
    'GetKeyPressActivation'), ('process_events', 'GetProcessEvents'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'process_events',
    'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RectilinearWipeWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RectilinearWipeWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'manages_cursor',
            'process_events'], [], ['key_press_activation_value', 'priority']),
            title='Edit RectilinearWipeWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RectilinearWipeWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

