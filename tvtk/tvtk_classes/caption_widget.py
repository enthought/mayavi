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


class CaptionWidget(BorderWidget):
    """
    CaptionWidget - widget for placing a caption (text plus leader)
    
    Superclass: BorderWidget
    
    This class provides support for interactively placing a caption on
    the 2d overlay plane. A caption is defined by some text with a leader
    (e.g., arrow) that points from the text to a point in the scene. The
    caption is represented by a CaptionRepresentation. It uses the
    event bindings of its superclass (vtk_border_widget) to control the
    placement of the text, and adds the ability to move the attachment
    point around. In addition, when the caption text is selected, the
    widget emits a activate_event that observers can watch for. This is
    useful for opening GUI dialogoues to adjust font characteristics,
    etc. (Please see the superclass for a description of event bindings.)
    
    Note that this widget extends the behavior of its superclass
    BorderWidget. The end point of the leader can be selected and
    moved around with an internal HandleWidget.
    
    See Also:
    
    BorderWidget TextWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCaptionWidget, obj, update, **traits)
    
    def _get_caption_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetCaptionActor2D())
    def _set_caption_actor2d(self, arg):
        old_val = self._get_caption_actor2d()
        self._wrap_call(self._vtk_obj.SetCaptionActor2D,
                        deref_vtk(arg))
        self.trait_property_changed('caption_actor2d', old_val, arg)
    caption_actor2d = traits.Property(_get_caption_actor2d, _set_caption_actor2d, help=\
        """
        Specify a CaptionActor2D to manage. This is convenient,
        alternative method to set_representation(). It internally create a
        CaptionRepresentation and then invokes
        CaptionRepresentation::SetCaptionActor2D().
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
            return super(CaptionWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CaptionWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'manages_cursor',
            'process_events', 'resizable', 'selectable'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit CaptionWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CaptionWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

