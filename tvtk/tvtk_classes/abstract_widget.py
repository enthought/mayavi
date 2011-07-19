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

from tvtk.tvtk_classes.interactor_observer import InteractorObserver


class AbstractWidget(InteractorObserver):
    """
    AbstractWidget - define the API for widget / widget representation
    
    Superclass: InteractorObserver
    
    The AbstractWidget defines an API and implements methods common to
    all widgets using the interaction/representation design. In this
    design, the term interaction means that part of the widget that
    performs event handling, while the representation corresponds to a
    Prop (or the subclass WidgetRepresentation) used to represent
    the widget. AbstractWidget also implements some methods common to
    all subclasses.
    
    Note that AbstractWidget provides access to the
    WidgetEventTranslator.  This class is responsible for translating
    VTK events (defined in Command.h) into widget events (defined in
    WidgetEvent.h).  This class can be manipulated so that different
    VTK events can be mapped into widget events, thereby allowing the
    modification of event bindings. Each subclass of AbstractWidget
    defines the events to which it responds.
    
    Caveats:
    
    Note that the pair (vtk_abstract_widget/vtk_widget_representation) are an
    implementation of the second generation VTK Widgets design. In the
    first generation design, widgets were implemented in a single
    monotonic class. This design was problematic because in client-server
    applications it was difficult to manage widgets properly. Also, new
    "representations" or look-and-feel, for a widget required a whole new
    class, with a lot of redundant code. The separation of the widget
    event handling and representation enables users and developers to
    create new appearances for the widget. It also facilitates parallel
    processing, where the client application handles events, and remote
    representations of the widget are slaves to the client (and do not
    handle events).
    
    See Also:
    
    WidgetRepresentation WidgetEventTranslator
    WidgetCallbackMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractWidget, obj, update, **traits)
    
    process_events = tvtk_base.true_bool_trait(help=\
        """
        Methods to change the whether the widget responds to interaction.
        Set this to Off to disable interaction. On by default. Subclasses
        must overide set_process_events() to make sure that they pass on
        the flag to all component widgets.
        """
    )
    def _process_events_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProcessEvents,
                        self.process_events_)

    manages_cursor = tvtk_base.true_bool_trait(help=\
        """
        Turn on or off the management of the cursor. Cursor management is
        typically disabled for subclasses when composite widgets are
        created. For example, HandleWidgets are often used to create
        composite widgets, and the parent widget takes over the cursor
        management.
        """
    )
    def _manages_cursor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetManagesCursor,
                        self.manages_cursor_)

    def _get_parent(self):
        return wrap_vtk(self._vtk_obj.GetParent())
    def _set_parent(self, arg):
        old_val = self._get_parent()
        self._wrap_call(self._vtk_obj.SetParent,
                        deref_vtk(arg))
        self.trait_property_changed('parent', old_val, arg)
    parent = traits.Property(_get_parent, _set_parent, help=\
        """
        Specifying a parent to this widget is used when creating
        composite widgets. It is an internal method not meant to be used
        by the public. When a widget has a parent, it defers the
        rendering to the parent. It may also defer managing the cursor
        (see manages_cursor ivar).
        """
    )

    def _get_event_translator(self):
        return wrap_vtk(self._vtk_obj.GetEventTranslator())
    event_translator = traits.Property(_get_event_translator, help=\
        """
        Get the event translator. Careful manipulation of this class
        enables the user to override the default event bindings.
        """
    )

    def _get_process_events_max_value(self):
        return self._vtk_obj.GetProcessEventsMaxValue()
    process_events_max_value = traits.Property(_get_process_events_max_value, help=\
        """
        Methods to change the whether the widget responds to interaction.
        Set this to Off to disable interaction. On by default. Subclasses
        must overide set_process_events() to make sure that they pass on
        the flag to all component widgets.
        """
    )

    def _get_process_events_min_value(self):
        return self._vtk_obj.GetProcessEventsMinValue()
    process_events_min_value = traits.Property(_get_process_events_min_value, help=\
        """
        Methods to change the whether the widget responds to interaction.
        Set this to Off to disable interaction. On by default. Subclasses
        must overide set_process_events() to make sure that they pass on
        the flag to all component widgets.
        """
    )

    def _get_representation(self):
        return wrap_vtk(self._vtk_obj.GetRepresentation())
    representation = traits.Property(_get_representation, help=\
        """
        Return an instance of WidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of Prop (typically a subclass of
        WidgetRepresenation) so it can be added to the renderer
        independent of the widget.
        """
    )

    def create_default_representation(self):
        """
        V.create_default_representation()
        C++: virtual void CreateDefaultRepresentation()
        Create the default widget representation if one is not set. The
        representation defines the geometry of the widget (i.e., how it
        appears) as well as providing special methods for manipulting the
        state and appearance of the widget.
        """
        ret = self._vtk_obj.CreateDefaultRepresentation()
        return ret
        

    def render(self):
        """
        V.render()
        C++: void Render()
        This method is called by subclasses when a render method is to be
        invoked on the RenderWindowInteractor. This method should be
        called (instead of RenderWindow::Render() because it has built
        into it optimizations for minimizing renders and/or speeding
        renders.
        """
        ret = self._vtk_obj.Render()
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
            return super(AbstractWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'manages_cursor',
            'process_events'], [], ['key_press_activation_value', 'priority']),
            title='Edit AbstractWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

