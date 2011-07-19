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

from tvtk.tvtk_classes.view import View


class RenderViewBase(View):
    """
    RenderViewBase - A base view containing a renderer.
    
    Superclass: View
    
    RenderViewBase is a view which contains a Renderer.  You may
    add Actors directly to the renderer.
    
    This class is also the parent class for any more specialized view
    which uses a renderer.
    
    In order to use the view with a QVTKWidget the following code is
    required to ensure the interactor and render window are initialized
    properly.QVTKWidget *widget = new QVTKWidget;
    ContextView *view = ContextView::New();
    view->_set_interactor(widget->_get_interactor());
    widget->_set_render_window(view->_get_render_window());
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderViewBase, obj, update, **traits)
    
    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        Get a handle to the render window.
        """
    )

    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    def _set_interactor(self, arg):
        old_val = self._get_interactor()
        self._wrap_call(self._vtk_obj.SetInteractor,
                        deref_vtk(arg))
        self.trait_property_changed('interactor', old_val, arg)
    interactor = traits.Property(_get_interactor, _set_interactor, help=\
        """
        The render window interactor. Note that this requires special
        handling in order to do correctly - see the notes in the detailed
        description of RenderViewBase.
        """
    )

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Gets the renderer for this view.
        """
    )

    def render(self):
        """
        V.render()
        C++: virtual void Render()
        Updates the representations, then calls Render() on the render
        window associated with this view.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    def reset_camera(self):
        """
        V.reset_camera()
        C++: virtual void ResetCamera()
        Updates the representations, then calls reset_camera() on the
        renderer associated with this view.
        """
        ret = self._vtk_obj.ResetCamera()
        return ret
        

    def reset_camera_clipping_range(self):
        """
        V.reset_camera_clipping_range()
        C++: virtual void ResetCameraClippingRange()
        Updates the representations, then calls
        reset_camera_clipping_range() on the renderer associated with this
        view.
        """
        ret = self._vtk_obj.ResetCameraClippingRange()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderViewBase, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderViewBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit RenderViewBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderViewBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

