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


class RendererDelegate(Object):
    """
    RendererDelegate - Render the props of a Renderer
    
    Superclass: Object
    
    RendererDelegate is an abstract class with a pure virtual method
    Render. This method replaces the Render method of Renderer to
    allow custom rendering from an external project. A renderer_delegate
    is connected to a Renderer with method set_delegate(). An external
    project just has to provide a concrete implementation of
    RendererDelegate.
    
    See Also:
    
    Renderer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRendererDelegate, obj, update, **traits)
    
    used = tvtk_base.false_bool_trait(help=\
        """
        Tells if the delegate has to be used by the renderer or not.
        Initial value is off.
        """
    )
    def _used_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUsed,
                        self.used_)

    def render(self, *args):
        """
        V.render(Renderer)
        C++: virtual void Render(Renderer *r)
        Render the props of Renderer if Used is on.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('used', 'GetUsed'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'used'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RendererDelegate, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RendererDelegate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['used'], [], []),
            title='Edit RendererDelegate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RendererDelegate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

