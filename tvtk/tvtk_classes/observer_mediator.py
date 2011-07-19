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


class ObserverMediator(Object):
    """
    ObserverMediator - manage contention for cursors and other
    resources
    
    Superclass: Object
    
    The ObserverMediator is a helper class that manages requests for
    cursor changes from multiple interactor observers (e.g. widgets). It
    keeps a list of widgets (and their priorities) and their current
    requests for cursor shape. It then satisfies requests based on widget
    priority and the relative importance of the request (e.g., a lower
    priority widget requesting a particular cursor shape will overrule a
    higher priority widget requesting a default shape).
    
    See Also:
    
    AbstractWidget WidgetRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkObserverMediator, obj, update, **traits)
    
    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    def _set_interactor(self, arg):
        old_val = self._get_interactor()
        self._wrap_call(self._vtk_obj.SetInteractor,
                        deref_vtk(arg))
        self.trait_property_changed('interactor', old_val, arg)
    interactor = traits.Property(_get_interactor, _set_interactor, help=\
        """
        Specify the instance of RenderWindow whose cursor shape is to
        be managed.
        """
    )

    def remove_all_cursor_shape_requests(self, *args):
        """
        V.remove_all_cursor_shape_requests(InteractorObserver)
        C++: void RemoveAllCursorShapeRequests(InteractorObserver *)
        Remove all requests for cursor shape from a given interactor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveAllCursorShapeRequests, *my_args)
        return ret

    def request_cursor_shape(self, *args):
        """
        V.request_cursor_shape(InteractorObserver, int) -> int
        C++: int RequestCursorShape(InteractorObserver *,
            int cursorShape)
        Method used to request a cursor shape. Note that the shape is
        specified using one of the integral values determined in
        RenderWindow.h. The method returns a non-zero value if the
        shape was successfully changed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RequestCursorShape, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ObserverMediator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ObserverMediator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ObserverMediator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ObserverMediator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

