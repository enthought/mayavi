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


class TDxInteractorStyle(Object):
    """
    TDxInteractorStyle - provide 3d_connexion device event-driven
    interface to the rendering window
    
    Superclass: Object
    
    TDxInteractorStyle is an abstract class defining an event-driven
    interface to support 3d_connexion device events send by
    RenderWindowInteractor. RenderWindowInteractor forwards events
    in a platform independent form to InteractorStyle which can then
    delegate some processing to TDxInteractorStyle.
    
    See Also:
    
    InteractorStyle RenderWindowInteractor
    TDxInteractorStyleCamera
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTDxInteractorStyle, obj, update, **traits)
    
    def _get_settings(self):
        return wrap_vtk(self._vtk_obj.GetSettings())
    def _set_settings(self, arg):
        old_val = self._get_settings()
        self._wrap_call(self._vtk_obj.SetSettings,
                        deref_vtk(arg))
        self.trait_property_changed('settings', old_val, arg)
    settings = traits.Property(_get_settings, _set_settings, help=\
        """
        3dconnexion device settings. (sensitivity, individual axis
        filters). Initial object is not null.
        """
    )

    def on_button_pressed_event(self, *args):
        """
        V.on_button_pressed_event(int)
        C++: virtual void OnButtonPressedEvent(int button)
        Action on button pressed event. Default implementation is empty.
        """
        ret = self._wrap_call(self._vtk_obj.OnButtonPressedEvent, *args)
        return ret

    def on_button_released_event(self, *args):
        """
        V.on_button_released_event(int)
        C++: virtual void OnButtonReleasedEvent(int button)
        Action on button released event. Default implementation is empty.
        """
        ret = self._wrap_call(self._vtk_obj.OnButtonReleasedEvent, *args)
        return ret

    def on_motion_event(self, *args):
        """
        V.on_motion_event(TDxMotionEventInfo)
        C++: virtual void OnMotionEvent(TDxMotionEventInfo *motionInfo)
        Action on motion event. Default implementation is empty.
        \pre: motion_info_exist: motion_info!=_0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.OnMotionEvent, *my_args)
        return ret

    def process_event(self, *args):
        """
        V.process_event(Renderer, int, )
        C++: virtual void ProcessEvent(Renderer *renderer,
            unsigned long event, void *calldata)
        Dispatch the events t_dx_motion_event, t_dx_button_press_event and
        t_dx_button_release_event to on_motion_event(), on_button_pressed_event()
        and on_button_released_event() respectively. It is called by the
        InteractorStyle. This method is virtual for convenient but you
        should really override the On*Event() methods only.
        \pre renderer can be null.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ProcessEvent, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TDxInteractorStyle, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TDxInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit TDxInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TDxInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

