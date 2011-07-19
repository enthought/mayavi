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


class XOpenGLRenderWindow(OpenGLRenderWindow):
    """
    XOpenGLRenderWindow - open_gl rendering window
    
    Superclass: OpenGLRenderWindow
    
    XOpenGLRenderWindow is a concrete implementation of the abstract
    class RenderWindow. OpenGLRenderer interfaces to the open_gl
    graphics library. Application programmers should normally use
    RenderWindow instead of the open_gl specific version.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXOpenGLRenderWindow, obj, update, **traits)
    
    def _get_desired_depth(self):
        return self._vtk_obj.GetDesiredDepth()
    desired_depth = traits.Property(_get_desired_depth, help=\
        """
        Get the X properties of an ideal rendering window.
        """
    )

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize(void)
        Initialize the rendering window.  This will setup all
        system-specific resources.  This method and Finalize() must be
        symmetric and it should be possible to call them multiple times,
        even changing window_id in-between.  This is what window_remap
        does.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def pref_full_screen(self):
        """
        V.pref_full_screen()
        C++: virtual void PrefFullScreen(void)
        Set the preferred window size to full screen.
        """
        ret = self._vtk_obj.PrefFullScreen()
        return ret
        

    def window_initialize(self):
        """
        V.window_initialize()
        C++: virtual void WindowInitialize(void)
        Initialize the window for rendering.
        """
        ret = self._vtk_obj.WindowInitialize()
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
            return super(XOpenGLRenderWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XOpenGLRenderWindow properties', scrollable=True, resizable=True,
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
            title='Edit XOpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XOpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

