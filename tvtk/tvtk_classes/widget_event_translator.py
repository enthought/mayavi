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

from tvtk.tvtk_classes.object import Object


class WidgetEventTranslator(Object):
    """
    WidgetEventTranslator - map VTK events into widget events
    
    Superclass: Object
    
    WidgetEventTranslator maps VTK events (defined on Command) into
    widget events (defined in WidgetEvent.h). This class is typically
    used in combination with WidgetCallbackMapper, which is
    responsible for translating widget events into method callbacks, and
    then invoking the callbacks.
    
    This class can be used to define different mappings of VTK events
    into the widget events. Thus widgets can be reconfigured to use
    different event bindings.
    
    See Also:
    
    WidgetEvent Command InteractorObserver
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWidgetEventTranslator, obj, update, **traits)
    
    def get_translation(self, *args):
        """
        V.get_translation(int) -> int
        C++: unsigned long GetTranslation(unsigned long VTKEvent)
        V.get_translation(string) -> string
        C++: const char *GetTranslation(const char *VTKEvent)
        V.get_translation(int, int, char, int, string) -> int
        C++: unsigned long GetTranslation(unsigned long VTKEvent,
            int modifier, char keyCode, int repeatCount, char *keySym)
        V.get_translation(Event) -> int
        C++: unsigned long GetTranslation(Event *VTKEvent)
        Translate a VTK event into a widget event. If no event mapping is
        found, then the methods return WidgetEvent::NoEvent or a NULL
        string.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetTranslation, *my_args)
        return ret

    def set_translation(self, *args):
        """
        V.set_translation(int, int)
        C++: void SetTranslation(unsigned long VTKEvent,
            unsigned long widgetEvent)
        V.set_translation(string, string)
        C++: void SetTranslation(const char *VTKEvent,
            const char *widgetEvent)
        V.set_translation(int, int, char, int, string, int)
        C++: void SetTranslation(unsigned long VTKEvent, int modifier,
            char keyCode, int repeatCount, const char *keySym,
            unsigned long widgetEvent)
        V.set_translation(Event, int)
        C++: void SetTranslation(Event *VTKevent,
            unsigned long widgetEvent)
        Use these methods to create the translation from a VTK event to a
        widget event. Specifying WidgetEvent::NoEvent or an empty
        string for the (to_event) erases the mapping for the event.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTranslation, *my_args)
        return ret

    def add_events_to_interactor(self, *args):
        """
        V.add_events_to_interactor(RenderWindowInteractor,
            CallbackCommand, float)
        C++: void AddEventsToInteractor(RenderWindowInteractor *,
            CallbackCommand *, float priority)
        Add the events in the current translation table to the
        interactor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddEventsToInteractor, *my_args)
        return ret

    def add_events_to_parent(self, *args):
        """
        V.add_events_to_parent(AbstractWidget, CallbackCommand, float)
        C++: void AddEventsToParent(AbstractWidget *,
            CallbackCommand *, float priority)
        Add the events in the current translation table to the
        interactor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddEventsToParent, *my_args)
        return ret

    def clear_events(self):
        """
        V.clear_events()
        C++: void ClearEvents()
        Clear all events from the translator (i.e., no events will be
        translated).
        """
        ret = self._vtk_obj.ClearEvents()
        return ret
        

    def remove_translation(self, *args):
        """
        V.remove_translation(int, int, char, int, string) -> int
        C++: int RemoveTranslation(unsigned long VTKEvent, int modifier,
            char keyCode, int repeatCount, char *keySym)
        V.remove_translation(Event) -> int
        C++: int RemoveTranslation(Event *e)
        V.remove_translation(int) -> int
        C++: int RemoveTranslation(unsigned long VTKEvent)
        Remove translations for a binding. Returns the number of
        translations removed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveTranslation, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WidgetEventTranslator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WidgetEventTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit WidgetEventTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WidgetEventTranslator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

