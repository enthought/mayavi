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

from tvtk.tvtk_classes.border_widget import BorderWidget


class TextWidget(BorderWidget):
    """
    TextWidget - widget for placing text on overlay plane
    
    Superclass: BorderWidget
    
    This class provides support for interactively placing text on the 2d
    overlay plane. The text is defined by an instance of TextActor. It
    uses the event bindings of its superclass (vtk_border_widget). In
    addition, when the text is selected, the widget emits a
    widget_activate_event that observers can watch for. This is useful for
    opening GUI dialogues to adjust font characteristics, etc. (Please
    see the superclass for a description of event bindings.)
    
    See Also:
    
    BorderWidget CaptionWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextWidget, obj, update, **traits)
    
    def _get_text_actor(self):
        return wrap_vtk(self._vtk_obj.GetTextActor())
    def _set_text_actor(self, arg):
        old_val = self._get_text_actor()
        self._wrap_call(self._vtk_obj.SetTextActor,
                        deref_vtk(arg))
        self.trait_property_changed('text_actor', old_val, arg)
    text_actor = traits.Property(_get_text_actor, _set_text_actor, help=\
        """
        Specify a TextActor to manage. This is a convenient,
        alternative method to specify the representation for the widget
        (i.e., used instead of set_representation()). It internally
        creates a TextRepresentation and then invokes
        TextRepresentation::SetTextActor().
        """
    )

    _updateable_traits_ = \
    (('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('resizable',
    'GetResizable'), ('enabled', 'GetEnabled'), ('manages_cursor',
    'GetManagesCursor'), ('priority', 'GetPriority'), ('debug',
    'GetDebug'), ('reference_count', 'GetReferenceCount'), ('selectable',
    'GetSelectable'), ('key_press_activation', 'GetKeyPressActivation'),
    ('process_events', 'GetProcessEvents'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'process_events',
    'resizable', 'selectable', 'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'manages_cursor',
            'process_events', 'resizable', 'selectable'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit TextWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

