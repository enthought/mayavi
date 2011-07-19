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


class RenderPass(Object):
    """
    RenderPass - Perform part of the rendering of a Renderer.
    
    Superclass: Object
    
    RenderPass is a deferred class with a simple deferred method
    Render. This method performs a rendering pass of the scene described
    in RenderState. Subclasses define what really happens during
    rendering.
    
    Directions to write a subclass of RenderPass: It is up to the
    subclass to decide if it needs to delegate part of its job to some
    other RenderPass objects ("delegates").
    - The subclass has to define ivar to set/get its delegates.
    - The documentation of the subclass has to describe:
    - what each delegate is supposed to perform
    - if a delegate is supposed to be used once or multiple times
    - what it expects to have in the framebuffer before starting (status
      of colorbuffers, depth buffer, stencil buffer)
    - what it will change in the framebuffer.
    - A pass cannot modify the RenderState where it will perform but
      it can build a new RenderState (it can change the frame_buffer,
      change the prop array, changed the required prop properties keys
      (usually adding some to a copy of the existing list) but it has to
      keep the same Renderer object), make it current and pass it to
      its delegate.
    - at the end of the execution of Render, the pass has to ensure the
      current RenderState is the one it has in argument.
    
    See Also:
    
    RenderState Renderer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderPass, obj, update, **traits)
    
    def _get_number_of_rendered_props(self):
        return self._vtk_obj.GetNumberOfRenderedProps()
    number_of_rendered_props = traits.Property(_get_number_of_rendered_props, help=\
        """
        Number of props rendered at the last Render call.
        """
    )

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *w)
        Release graphics resources and ask components to release their
        own resources. Default implementation is empty.
        \pre w_exists: w!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit RenderPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

