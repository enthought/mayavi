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


class Event(Object):
    """
    Event - a complete specification of a VTK event including all
    modifiers
    
    Superclass: Object
    
    Event is a class that fully describes a VTK event. It is used by
    the widgets to help specify the mapping between VTK events and widget
    events.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEvent, obj, update, **traits)
    
    event_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the modifier for the event.
        """
    )
    def _event_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEventId,
                        self.event_id)

    repeat_count = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the repease count for the event.
        """
    )
    def _repeat_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepeatCount,
                        self.repeat_count)

    modifier = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the modifier for the event.
        """
    )
    def _modifier_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModifier,
                        self.modifier)

    key_sym = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the complex key symbol (compound key strokes) for the event.
        """
    )
    def _key_sym_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeySym,
                        self.key_sym)

    key_code = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Set the key_code for the event.
        """
    )
    def _key_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyCode,
                        self.key_code)

    _updateable_traits_ = \
    (('event_id', 'GetEventId'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'),
    ('repeat_count', 'GetRepeatCount'), ('key_sym', 'GetKeySym'),
    ('modifier', 'GetModifier'), ('debug', 'GetDebug'), ('key_code',
    'GetKeyCode'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'event_id', 'key_code',
    'key_sym', 'modifier', 'repeat_count'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Event, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Event properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['event_id', 'key_code', 'key_sym', 'modifier',
            'repeat_count']),
            title='Edit Event properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Event properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

