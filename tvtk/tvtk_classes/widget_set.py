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


class WidgetSet(Object):
    """
    WidgetSet - Synchronize a collection on Widgets drawn on
    different renderwindows using the Callback - Dispatch Action
    mechanism.
    
    Superclass: Object
    
    The class synchronizes a set of AbstractWidget(s). Widgets
    typically invoke "Actions" that drive the geometry/behaviour of their
    representations in response to interactor events. Interactor
    interactions on a render window are mapped into "Callbacks" by the
    widget, from which "Actions" are dispatched to the entire set. This
    architecture allows us to tie widgets existing in different render
    windows together. For instance a handle_widget might exist on the
    sagittal view. Moving it around should update the representations of
    the corresponding handle widget that lies on the axial and coronal
    and volume views as well.
    
    User API:
    
    A user would use this class as follows.vtk_widget_set *set =
    WidgetSet::New();
    ParallelopipedWidget *w1 = ParallelopipedWidget::New();
    set->_add_widget(w_1);
    w_1->_set_interactor(axial_render_window->_get_interactor());
    ParallelopipedWidget *w2 = ParallelopipedWidget::New();
    set->_add_widget(w_2);
    w_2->_set_interactor(coronal_render_window->_get_interactor());
    ParallelopipedWidget *w3 = ParallelopipedWidget::New();
    set->_add_widget(w_3);
    w_3->_set_interactor(sagittal_render_window->_get_interactor());
    set->_set_enabled(_1);
    
    Motivation:
    
    The motivation for this class is really to provide a usable API to
    tie together multiple widgets of the same kind. To enable this,
    subclasses of AbstractWidget, must be written as follows:
      They will generally have callback methods mapped to some user
    interaction such
    as:this->_callback_mapper->_set_callback_method(vtk_command::_left_button_press
    Event,
                            Event::NoModifier, 0, 0, NULL,
                            PaintbrushWidget::BeginDrawStrokeEvent,
                            this,
    PaintbrushWidget::BeginDrawCallback);
    
      The callback invoked when the left button is pressed looks
    like:void PaintbrushWidget::BeginDrawCallback(vtkAbstractWidget
    *w)
    {
      PaintbrushWidget *self = PaintbrushWidget::SafeDownCast(w);
      self->_widget_set->_dispatch_action(self,
    &vtk_paintbrush_widget::_begin_draw_action);
    }
    
      The actual code for handling the drawing is written in the
    begin_draw_action method.void PaintbrushWidget::BeginDrawAction(
    PaintbrushWidget *dispatcher)
    {
    // Do stuff to draw...
    // Here dispatcher is the widget that was interacted with, the one
    that
    // dispatched an action to all the other widgets in its group. You
    may, if
    // necessary find it helpful to get parameters from it.
    //   For instance for a resize_action:
    //     if (this != dispatcher)
    //       {
    //       double *newsize =
    dispatcher->_get_representation()->_get_size();
    //       this->_widget_rep->_set_size(newsize);
    //       }
    //     else
    //       {
    //       this->_widget_rep->_increment_size_by_delta();
    //       }
    }
    
    Caveats:
    
    Actions are always dispatched first to the active_widget, the one
    calling the set, and then to the other widgets in the set.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWidgetSet, obj, update, **traits)
    
    def get_nth_widget(self, *args):
        """
        V.get_nth_widget(int) -> AbstractWidget
        C++: AbstractWidget *GetNthWidget(unsigned int)
        Get the Nth widget in the set.
        """
        ret = self._wrap_call(self._vtk_obj.GetNthWidget, *args)
        return wrap_vtk(ret)

    def _get_number_of_widgets(self):
        return self._vtk_obj.GetNumberOfWidgets()
    number_of_widgets = traits.Property(_get_number_of_widgets, help=\
        """
        Get number of widgets in the set.
        """
    )

    def add_widget(self, *args):
        """
        V.add_widget(AbstractWidget)
        C++: void AddWidget(AbstractWidget *)
        Add a widget to the set.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddWidget, *my_args)
        return ret

    def enabled_off(self):
        """
        V.enabled_off()
        C++: void EnabledOff()
        Method for activiating and deactiviating all widgets in the
        group.
        """
        ret = self._vtk_obj.EnabledOff()
        return ret
        

    def enabled_on(self):
        """
        V.enabled_on()
        C++: void EnabledOn()
        Method for activiating and deactiviating all widgets in the
        group.
        """
        ret = self._vtk_obj.EnabledOn()
        return ret
        

    def remove_widget(self, *args):
        """
        V.remove_widget(AbstractWidget)
        C++: void RemoveWidget(AbstractWidget *)
        Remove a widget from the set
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveWidget, *my_args)
        return ret

    def set_enabled(self, *args):
        """
        V.set_enabled(int)
        C++: virtual void SetEnabled(int)
        Method for activiating and deactiviating all widgets in the
        group.
        """
        ret = self._wrap_call(self._vtk_obj.SetEnabled, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WidgetSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WidgetSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit WidgetSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WidgetSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

