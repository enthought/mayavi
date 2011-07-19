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

from tvtk.tvtk_classes.border_representation import BorderRepresentation


class TextRepresentation(BorderRepresentation):
    """
    TextRepresentation - represent text for TextWidget
    
    Superclass: BorderRepresentation
    
    This class represents text for a TextWidget.  This class provides
    support for interactively placing text on the 2d overlay plane. The
    text is defined by an instance of TextActor.
    
    See Also:
    
    TextRepresentation BorderWidget AbstractWidget
    WidgetRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextRepresentation, obj, update, **traits)
    
    text = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get/Set the text string display by this representation.
        """
    )
    def _text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetText,
                        self.text)

    def _get_text_actor(self):
        return wrap_vtk(self._vtk_obj.GetTextActor())
    def _set_text_actor(self, arg):
        old_val = self._get_text_actor()
        self._wrap_call(self._vtk_obj.SetTextActor,
                        deref_vtk(arg))
        self.trait_property_changed('text_actor', old_val, arg)
    text_actor = traits.Property(_get_text_actor, _set_text_actor, help=\
        """
        Specify the TextActor to manage. If not specified, then one is
        automatically created.
        """
    )

    window_location = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the text position, by enumeration ( any_location = 0,
        lower_left_corner, lower_right_corner, lower_center, upper_left_corner,
        upper_right_corner, upper_center) related to the render window
        """
    )
    def _window_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindowLocation,
                        self.window_location)

    def execute_text_actor_modified_event(self, *args):
        """
        V.execute_text_actor_modified_event(Object, int, )
        C++: void ExecuteTextActorModifiedEvent(Object *obj,
            unsigned long enumEvent, void *p)
        Internal. Excecute events observed by internal observer
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ExecuteTextActorModifiedEvent, *my_args)
        return ret

    def execute_text_property_modified_event(self, *args):
        """
        V.execute_text_property_modified_event(Object, int, )
        C++: void ExecuteTextPropertyModifiedEvent(Object *obj,
            unsigned long enumEvent, void *p)
        Internal. Excecute events observed by internal observer
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ExecuteTextPropertyModifiedEvent, *my_args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('minimum_size',
    'GetMinimumSize'), ('handle_size', 'GetHandleSize'), ('text',
    'GetText'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('show_border',
    'GetShowBorder'), ('moving', 'GetMoving'), ('place_factor',
    'GetPlaceFactor'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('window_location', 'GetWindowLocation'),
    ('use_bounds', 'GetUseBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('position2', 'GetPosition2'),
    ('proportional_resize', 'GetProportionalResize'), ('need_to_render',
    'GetNeedToRender'), ('reference_count', 'GetReferenceCount'),
    ('position', 'GetPosition'), ('maximum_size', 'GetMaximumSize'),
    ('pickable', 'GetPickable'), ('tolerance', 'GetTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'moving',
    'need_to_render', 'pickable', 'proportional_resize', 'use_bounds',
    'visibility', 'show_border', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'maximum_size',
    'minimum_size', 'place_factor', 'position', 'position2',
    'render_time_multiplier', 'text', 'tolerance', 'window_location'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['moving', 'need_to_render', 'proportional_resize',
            'use_bounds', 'visibility'], ['show_border'],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'maximum_size', 'minimum_size', 'place_factor', 'position',
            'position2', 'render_time_multiplier', 'text', 'tolerance',
            'window_location']),
            title='Edit TextRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

