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


class WidgetCallbackMapper(Object):
    """
    WidgetCallbackMapper - map widget events into callbacks
    
    Superclass: Object
    
    WidgetCallbackMapper maps widget events (defined in
    WidgetEvent.h) into static class methods, and provides facilities
    to invoke the methods. This class is templated and meant to be used
    as an internal helper class by the widget classes. The class works in
    combination with the class WidgetEventTranslator, which translates
    VTK events into widget events.
    
    See Also:
    
    WidgetEvent WidgetEventTranslator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWidgetCallbackMapper, obj, update, **traits)
    
    def _get_event_translator(self):
        return wrap_vtk(self._vtk_obj.GetEventTranslator())
    def _set_event_translator(self, arg):
        old_val = self._get_event_translator()
        self._wrap_call(self._vtk_obj.SetEventTranslator,
                        deref_vtk(arg))
        self.trait_property_changed('event_translator', old_val, arg)
    event_translator = traits.Property(_get_event_translator, _set_event_translator, help=\
        """
        Specify the WidgetEventTranslator to coordinate with.
        """
    )

    def invoke_callback(self, *args):
        """
        V.invoke_callback(int)
        C++: void InvokeCallback(unsigned long widgetEvent)
        This method invokes the callback given a widget event. A non-zero
        value is returned if the listed event is registered.
        """
        ret = self._wrap_call(self._vtk_obj.InvokeCallback, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WidgetCallbackMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WidgetCallbackMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit WidgetCallbackMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WidgetCallbackMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

