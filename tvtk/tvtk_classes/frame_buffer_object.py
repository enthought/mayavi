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


class FrameBufferObject(Object):
    """
    FrameBufferObject - internal class which encapsulates open_gl
    
    Superclass: Object
    
    Encapsulates an open_gl Frame Buffer Object. For use by
    OpenGLFBORenderWindow, not to be used directly.
    
    Caveats:
    
    DON'T PLAY WITH IT YET.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFrameBufferObject, obj, update, **traits)
    
    number_of_render_targets = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of render targets to render into at once.
        """
    )
    def _number_of_render_targets_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfRenderTargets,
                        self.number_of_render_targets)

    depth_buffer_needed = traits.Bool(True, help=\
        """
        If true, the frame buffer object will be initialized with a depth
        buffer. Initial value is true.
        """
    )
    def _depth_buffer_needed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthBufferNeeded,
                        self.depth_buffer_needed)

    def get_color_buffer(self, *args):
        """
        V.get_color_buffer(int) -> TextureObject
        C++: TextureObject *GetColorBuffer(unsigned int index)"""
        ret = self._wrap_call(self._vtk_obj.GetColorBuffer, *args)
        return wrap_vtk(ret)

    def set_color_buffer(self, *args):
        """
        V.set_color_buffer(int, TextureObject, int)
        C++: void SetColorBuffer(unsigned int index,
            TextureObject *texture, unsigned int zslice=0)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetColorBuffer, *my_args)
        return ret

    def _get_context(self):
        return wrap_vtk(self._vtk_obj.GetContext())
    def _set_context(self, arg):
        old_val = self._get_context()
        self._wrap_call(self._vtk_obj.SetContext,
                        deref_vtk(arg))
        self.trait_property_changed('context', old_val, arg)
    context = traits.Property(_get_context, _set_context, help=\
        """
        Get/Set the context. Context must be a OpenGLRenderWindow.
        This does not increase the reference count of the context to
        avoid reference loops. set_context() may raise an error is the
        open_gl context does not support the required open_gl extensions.
        """
    )

    def _get_last_size(self):
        return self._vtk_obj.GetLastSize()
    last_size = traits.Property(_get_last_size, help=\
        """
        
        """
    )

    def _get_maximum_number_of_active_targets(self):
        return self._vtk_obj.GetMaximumNumberOfActiveTargets()
    maximum_number_of_active_targets = traits.Property(_get_maximum_number_of_active_targets, help=\
        """
        Returns the maximum number of targets that can be rendered to at
        one time. This limits the active targets set by
        set_active_targets(). The return value is valid only if get_context
        is non-null.
        """
    )

    def _get_maximum_number_of_render_targets(self):
        return self._vtk_obj.GetMaximumNumberOfRenderTargets()
    maximum_number_of_render_targets = traits.Property(_get_maximum_number_of_render_targets, help=\
        """
        Returns the maximum number of render targets available. This
        limits the available attachement points for set_color_attachment().
        The return value is valid only if get_context is non-null.
        """
    )

    def bind(self):
        """
        V.bind()
        C++: void Bind()
        Save the current framebuffer and make the frame buffer active.
        Multiple calls to Bind has no effect.
        """
        ret = self._vtk_obj.Bind()
        return ret
        

    def is_supported(self, *args):
        """
        V.is_supported(RenderWindow) -> bool
        C++: static bool IsSupported(RenderWindow *renWin)
        Returns if the context supports the required extensions.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsSupported, *my_args)
        return ret

    def remove_all_color_buffers(self):
        """
        V.remove_all_color_buffers()
        C++: void RemoveAllColorBuffers()"""
        ret = self._vtk_obj.RemoveAllColorBuffers()
        return ret
        

    def remove_color_buffer(self, *args):
        """
        V.remove_color_buffer(int)
        C++: void RemoveColorBuffer(unsigned int index)"""
        ret = self._wrap_call(self._vtk_obj.RemoveColorBuffer, *args)
        return ret

    def remove_depth_buffer(self):
        """
        V.remove_depth_buffer()
        C++: void RemoveDepthBuffer()
        Set the texture to use as depth buffer.
        """
        ret = self._vtk_obj.RemoveDepthBuffer()
        return ret
        

    def render_quad(self, *args):
        """
        V.render_quad(int, int, int, int)
        C++: void RenderQuad(int minX, int maxX, int minY, int maxY)
        Renders a quad at the given location with pixel coordinates. This
        method is provided as a convenience, since we often render quads
        in a FBO.
        \pre positive_min_x: min_x>=_0
        \pre increasing_x: min_x<=max_x
        \pre valid_max_x: max_x<_last_size[_0]
        \pre positive_min_y: min_y>=_0
        \pre increasing_y: min_y<=max_y
        \pre valid_max_y: max_y<_last_size[_1]
        """
        ret = self._wrap_call(self._vtk_obj.RenderQuad, *args)
        return ret

    def set_active_buffer(self, *args):
        """
        V.set_active_buffer(int)
        C++: void SetActiveBuffer(unsigned int index)
        Choose the buffer to render into.
        """
        ret = self._wrap_call(self._vtk_obj.SetActiveBuffer, *args)
        return ret

    def set_depth_buffer(self, *args):
        """
        V.set_depth_buffer(TextureObject)
        C++: void SetDepthBuffer(TextureObject *depthTexture)
        Set the texture to use as depth buffer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDepthBuffer, *my_args)
        return ret

    def start(self, *args):
        """
        V.start(int, int, bool) -> bool
        C++: bool Start(int width, int height,
            bool shaderSupportsTextureInt)
        User must take care that width/height match the dimensions of the
        user defined texture attachments. This method makes the "active
        buffers" the buffers that will get drawn into by subsequent
        drawing calls. Note that this does not clear the render buffers
        i.e. no gl_clear() calls are made by either of these methods. It's
        up to the caller to clear the buffers if needed.
        """
        ret = self._wrap_call(self._vtk_obj.Start, *args)
        return ret

    def start_non_ortho(self, *args):
        """
        V.start_non_ortho(int, int, bool) -> bool
        C++: bool StartNonOrtho(int width, int height,
            bool shaderSupportsTextureInt)
        User must take care that width/height match the dimensions of the
        user defined texture attachments. This method makes the "active
        buffers" the buffers that will get drawn into by subsequent
        drawing calls. Note that this does not clear the render buffers
        i.e. no gl_clear() calls are made by either of these methods. It's
        up to the caller to clear the buffers if needed.
        """
        ret = self._wrap_call(self._vtk_obj.StartNonOrtho, *args)
        return ret

    def un_bind(self):
        """
        V.un_bind()
        C++: void UnBind()
        Restore the framebuffer saved with the call to Bind(). Multiple
        calls to un_bind has no effect.
        """
        ret = self._vtk_obj.UnBind()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('number_of_render_targets', 'GetNumberOfRenderTargets'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('depth_buffer_needed', 'GetDepthBufferNeeded'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'depth_buffer_needed',
    'number_of_render_targets'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FrameBufferObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FrameBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['depth_buffer_needed',
            'number_of_render_targets']),
            title='Edit FrameBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FrameBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

