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

from tvtk.tvtk_classes.open_gl_render_window import OpenGLRenderWindow


class GenericOpenGLRenderWindow(OpenGLRenderWindow):
    """
    GenericOpenGLRenderWindow - platform independent render window
    
    Superclass: OpenGLRenderWindow
    
    GenericOpenGLRenderWindow provides a skeleton for implementing a
    render window using one's own open_gl context and drawable. To be
    effective, one must register an observer for window_make_current_event,
    window_is_current_event and window_frame_event.  When this class sends a
    window_is_current_event, the call data is an bool* which one can use to
    return whether the context is current.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericOpenGLRenderWindow, obj, update, **traits)
    
    def create_a_window(self):
        """
        V.create_a_window()
        C++: void CreateAWindow()"""
        ret = self._vtk_obj.CreateAWindow()
        return ret
        

    def destroy_window(self):
        """
        V.destroy_window()
        C++: void DestroyWindow()"""
        ret = self._vtk_obj.DestroyWindow()
        return ret
        

    def pop_state(self):
        """
        V.pop_state()
        C++: void PopState()"""
        ret = self._vtk_obj.PopState()
        return ret
        

    def push_state(self):
        """
        V.push_state()
        C++: void PushState()"""
        ret = self._vtk_obj.PushState()
        return ret
        

    def set_back_buffer(self, *args):
        """
        V.set_back_buffer(int)
        C++: void SetBackBuffer(unsigned int)"""
        ret = self._wrap_call(self._vtk_obj.SetBackBuffer, *args)
        return ret

    def set_back_left_buffer(self, *args):
        """
        V.set_back_left_buffer(int)
        C++: void SetBackLeftBuffer(unsigned int)"""
        ret = self._wrap_call(self._vtk_obj.SetBackLeftBuffer, *args)
        return ret

    def set_back_right_buffer(self, *args):
        """
        V.set_back_right_buffer(int)
        C++: void SetBackRightBuffer(unsigned int)"""
        ret = self._wrap_call(self._vtk_obj.SetBackRightBuffer, *args)
        return ret

    def set_front_buffer(self, *args):
        """
        V.set_front_buffer(int)
        C++: void SetFrontBuffer(unsigned int)"""
        ret = self._wrap_call(self._vtk_obj.SetFrontBuffer, *args)
        return ret

    def set_front_left_buffer(self, *args):
        """
        V.set_front_left_buffer(int)
        C++: void SetFrontLeftBuffer(unsigned int)"""
        ret = self._wrap_call(self._vtk_obj.SetFrontLeftBuffer, *args)
        return ret

    def set_front_right_buffer(self, *args):
        """
        V.set_front_right_buffer(int)
        C++: void SetFrontRightBuffer(unsigned int)"""
        ret = self._wrap_call(self._vtk_obj.SetFrontRightBuffer, *args)
        return ret

    _updateable_traits_ = \
    (('anaglyph_color_mask', 'GetAnaglyphColorMask'),
    ('report_graphic_errors', 'GetReportGraphicErrors'),
    ('desired_update_rate', 'GetDesiredUpdateRate'), ('current_cursor',
    'GetCurrentCursor'), ('double_buffer', 'GetDoubleBuffer'),
    ('full_screen', 'GetFullScreen'), ('debug', 'GetDebug'), ('erase',
    'GetErase'), ('abort_render', 'GetAbortRender'), ('fd_frames',
    'GetFDFrames'), ('aa_frames', 'GetAAFrames'), ('off_screen_rendering',
    'GetOffScreenRendering'), ('polygon_smoothing',
    'GetPolygonSmoothing'), ('in_abort_check', 'GetInAbortCheck'),
    ('size', 'GetSize'), ('tile_viewport', 'GetTileViewport'),
    ('stereo_type', 'GetStereoType'), ('point_smoothing',
    'GetPointSmoothing'), ('sub_frames', 'GetSubFrames'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_layers', 'GetNumberOfLayers'), ('tile_scale',
    'GetTileScale'), ('stencil_capable', 'GetStencilCapable'),
    ('window_name', 'GetWindowName'), ('alpha_bit_planes',
    'GetAlphaBitPlanes'), ('swap_buffers', 'GetSwapBuffers'),
    ('multi_samples', 'GetMultiSamples'), ('is_picking', 'GetIsPicking'),
    ('stereo_capable_window', 'GetStereoCapableWindow'), ('stereo_render',
    'GetStereoRender'), ('mapped', 'GetMapped'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'),
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
            return super(GenericOpenGLRenderWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericOpenGLRenderWindow properties', scrollable=True, resizable=True,
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
            title='Edit GenericOpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericOpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

