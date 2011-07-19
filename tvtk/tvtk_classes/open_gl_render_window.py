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

from tvtk.tvtk_classes.render_window import RenderWindow


class OpenGLRenderWindow(RenderWindow):
    """
    OpenGLRenderWindow - open_gl rendering window
    
    Superclass: RenderWindow
    
    OpenGLRenderWindow is a concrete implementation of the abstract
    class RenderWindow. OpenGLRenderer interfaces to the open_gl
    graphics library. Application programmers should normally use
    RenderWindow instead of the open_gl specific version.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLRenderWindow, obj, update, **traits)
    
    global_maximum_number_of_multi_samples = traits.Int(8, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum number of multisamples
        """
    )
    def _global_maximum_number_of_multi_samples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalMaximumNumberOfMultiSamples,
                        self.global_maximum_number_of_multi_samples)

    def get_pixel_data(self, *args):
        """
        V.get_pixel_data(int, int, int, int, int, UnsignedCharArray)
            -> int
        C++: virtual int GetPixelData(int x, int y, int x2, int y2,
            int front, UnsignedCharArray *data)
        Set/Get the pixel data of an image, transmitted as RGBRGB...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'int', 'vtkUnsignedCharArray')])
        ret = self._wrap_call(self._vtk_obj.GetPixelData, *my_args)
        return ret

    def set_pixel_data(self, *args):
        """
        V.set_pixel_data(int, int, int, int, UnsignedCharArray, int)
            -> int
        C++: virtual int SetPixelData(int x, int y, int x2, int y2,
            UnsignedCharArray *data, int front)
        Set/Get the pixel data of an image, transmitted as RGBRGB...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'vtkUnsignedCharArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.SetPixelData, *my_args)
        return ret

    def get_rgba_char_pixel_data(self, *args):
        """
        V.get_rgba_char_pixel_data(int, int, int, int, int,
            UnsignedCharArray) -> int
        C++: virtual int GetRGBACharPixelData(int x, int y, int x2,
            int y2, int front, UnsignedCharArray *data)
        Set/Get the pixel data of an image, transmitted as RGBARGBA...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'int', 'vtkUnsignedCharArray')])
        ret = self._wrap_call(self._vtk_obj.GetRGBACharPixelData, *my_args)
        return ret

    def set_rgba_char_pixel_data(self, *args):
        """
        V.set_rgba_char_pixel_data(int, int, int, int, UnsignedCharArray,
            int, int) -> int
        C++: virtual int SetRGBACharPixelData(int x, int y, int x2,
            int y2, UnsignedCharArray *data, int front, int blend=0)
        Set/Get the pixel data of an image, transmitted as RGBARGBA...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'vtkUnsignedCharArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.SetRGBACharPixelData, *my_args)
        return ret

    def get_zbuffer_data(self, *args):
        """
        V.get_zbuffer_data(int, int, int, int, FloatArray) -> int
        C++: virtual int GetZbufferData(int x1, int y1, int x2, int y2,
            FloatArray *z)
        Set/Get the zbuffer data from an image
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.GetZbufferData, *my_args)
        return ret

    def set_zbuffer_data(self, *args):
        """
        V.set_zbuffer_data(int, int, int, int, FloatArray) -> int
        C++: virtual int SetZbufferData(int x1, int y1, int x2, int y2,
            FloatArray *buffer)
        Set/Get the zbuffer data from an image
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.SetZbufferData, *my_args)
        return ret

    def get_rgba_pixel_data(self, *args):
        """
        V.get_rgba_pixel_data(int, int, int, int, int, FloatArray) -> int
        C++: virtual int GetRGBAPixelData(int x, int y, int x2, int y2,
            int front, FloatArray *data)
        Set/Get the pixel data of an image, transmitted as RGBARGBA...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.GetRGBAPixelData, *my_args)
        return ret

    def set_rgba_pixel_data(self, *args):
        """
        V.set_rgba_pixel_data(int, int, int, int, FloatArray, int, int)
            -> int
        C++: virtual int SetRGBAPixelData(int x, int y, int x2, int y2,
            FloatArray *data, int front, int blend=0)
        Set/Get the pixel data of an image, transmitted as RGBARGBA...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'vtkFloatArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.SetRGBAPixelData, *my_args)
        return ret

    def _get_back_buffer(self):
        return self._vtk_obj.GetBackBuffer()
    back_buffer = traits.Property(_get_back_buffer, help=\
        """
        Return the open_gl name of the back left buffer. It is GL_BACK if
        GL is bound to the window-system-provided framebuffer. It is
        vtkgl::COLOR_ATTACHMENT0_EXT if GL is bound to an
        application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_back_left_buffer(self):
        return self._vtk_obj.GetBackLeftBuffer()
    back_left_buffer = traits.Property(_get_back_left_buffer, help=\
        """
        Return the open_gl name of the back left buffer. It is
        GL_BACK_LEFT if GL is bound to the window-system-provided
        framebuffer. It is vtkgl::COLOR_ATTACHMENT0_EXT if GL is bound to
        an application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_back_right_buffer(self):
        return self._vtk_obj.GetBackRightBuffer()
    back_right_buffer = traits.Property(_get_back_right_buffer, help=\
        """
        Return the open_gl name of the back right buffer. It is
        GL_BACK_RIGHT if GL is bound to the window-system-provided
        framebuffer. It is vtkgl::COLOR_ATTACHMENT0_EXT+1 if GL is bound
        to an application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_context_creation_time(self):
        return wrap_vtk(self._vtk_obj.GetContextCreationTime())
    context_creation_time = traits.Property(_get_context_creation_time, help=\
        """
        Get the time when the open_gl context was created.
        """
    )

    def _get_extension_manager(self):
        return wrap_vtk(self._vtk_obj.GetExtensionManager())
    extension_manager = traits.Property(_get_extension_manager, help=\
        """
        Returns the extension manager. A new one will be created if one
        hasn't already been set up.
        """
    )

    def _get_front_buffer(self):
        return self._vtk_obj.GetFrontBuffer()
    front_buffer = traits.Property(_get_front_buffer, help=\
        """
        Return the open_gl name of the front left buffer. It is GL_FRONT
        if GL is bound to the window-system-provided framebuffer. It is
        vtkgl::COLOR_ATTACHMENT0_EXT if GL is bound to an
        application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_front_left_buffer(self):
        return self._vtk_obj.GetFrontLeftBuffer()
    front_left_buffer = traits.Property(_get_front_left_buffer, help=\
        """
        Return the open_gl name of the front left buffer. It is
        GL_FRONT_LEFT if GL is bound to the window-system-provided
        framebuffer. It is vtkgl::COLOR_ATTACHMENT0_EXT if GL is bound to
        an application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_front_right_buffer(self):
        return self._vtk_obj.GetFrontRightBuffer()
    front_right_buffer = traits.Property(_get_front_right_buffer, help=\
        """
        Return the open_gl name of the front right buffer. It is
        GL_FRONT_RIGHT if GL is bound to the window-system-provided
        framebuffer. It is vtkgl::COLOR_ATTACHMENT0_EXT+1 if GL is bound
        to an application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_hardware_support(self):
        return wrap_vtk(self._vtk_obj.GetHardwareSupport())
    hardware_support = traits.Property(_get_hardware_support, help=\
        """
        Returns an Hardware Support object. A new one will be created if
        one hasn't already been set up.
        """
    )

    def _get_texture_unit_manager(self):
        return wrap_vtk(self._vtk_obj.GetTextureUnitManager())
    texture_unit_manager = traits.Property(_get_texture_unit_manager, help=\
        """
        Returns its texture unit manager object. A new one will be
        created if one hasn't already been set up.
        """
    )

    def open_gl_init(self):
        """
        V.open_gl_init()
        C++: virtual void OpenGLInit()
        Initialize open_gl for this window.
        """
        ret = self._vtk_obj.OpenGLInit()
        return ret
        

    _updateable_traits_ = \
    (('tile_viewport', 'GetTileViewport'), ('full_screen',
    'GetFullScreen'), ('stereo_render', 'GetStereoRender'),
    ('desired_update_rate', 'GetDesiredUpdateRate'), ('current_cursor',
    'GetCurrentCursor'), ('double_buffer', 'GetDoubleBuffer'),
    ('stereo_capable_window', 'GetStereoCapableWindow'), ('debug',
    'GetDebug'), ('erase', 'GetErase'), ('abort_render',
    'GetAbortRender'), ('fd_frames', 'GetFDFrames'), ('aa_frames',
    'GetAAFrames'), ('off_screen_rendering', 'GetOffScreenRendering'),
    ('polygon_smoothing', 'GetPolygonSmoothing'), ('in_abort_check',
    'GetInAbortCheck'), ('size', 'GetSize'), ('anaglyph_color_mask',
    'GetAnaglyphColorMask'), ('stereo_type', 'GetStereoType'),
    ('point_smoothing', 'GetPointSmoothing'), ('sub_frames',
    'GetSubFrames'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_layers', 'GetNumberOfLayers'),
    ('tile_scale', 'GetTileScale'), ('stencil_capable',
    'GetStencilCapable'), ('window_name', 'GetWindowName'),
    ('alpha_bit_planes', 'GetAlphaBitPlanes'), ('swap_buffers',
    'GetSwapBuffers'), ('multi_samples', 'GetMultiSamples'),
    ('is_picking', 'GetIsPicking'), ('report_graphic_errors',
    'GetReportGraphicErrors'), ('mapped', 'GetMapped'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('global_maximum_number_of_multi_samples',
    'GetGlobalMaximumNumberOfMultiSamples'), ('borders', 'GetBorders'),
    ('anaglyph_color_saturation', 'GetAnaglyphColorSaturation'), ('dpi',
    'GetDPI'), ('line_smoothing', 'GetLineSmoothing'))
    
    _full_traitnames_list_ = \
    (['alpha_bit_planes', 'borders', 'debug', 'double_buffer', 'erase',
    'full_screen', 'global_warning_display', 'is_picking',
    'line_smoothing', 'mapped', 'off_screen_rendering', 'point_smoothing',
    'polygon_smoothing', 'report_graphic_errors', 'stencil_capable',
    'stereo_capable_window', 'stereo_render', 'swap_buffers',
    'stereo_type', 'aa_frames', 'abort_render', 'anaglyph_color_mask',
    'anaglyph_color_saturation', 'current_cursor', 'desired_update_rate',
    'dpi', 'fd_frames', 'global_maximum_number_of_multi_samples',
    'in_abort_check', 'multi_samples', 'number_of_layers', 'position',
    'size', 'sub_frames', 'tile_scale', 'tile_viewport', 'window_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLRenderWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['alpha_bit_planes', 'borders', 'double_buffer',
            'erase', 'full_screen', 'is_picking', 'line_smoothing', 'mapped',
            'off_screen_rendering', 'point_smoothing', 'polygon_smoothing',
            'report_graphic_errors', 'stencil_capable', 'stereo_capable_window',
            'stereo_render', 'swap_buffers'], ['stereo_type'], ['aa_frames',
            'abort_render', 'anaglyph_color_mask', 'anaglyph_color_saturation',
            'current_cursor', 'desired_update_rate', 'dpi', 'fd_frames',
            'global_maximum_number_of_multi_samples', 'in_abort_check',
            'multi_samples', 'number_of_layers', 'position', 'size', 'sub_frames',
            'tile_scale', 'tile_viewport', 'window_name']),
            title='Edit OpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

