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

from tvtk.tvtk_classes.renderer import Renderer


class OpenGLRenderer(Renderer):
    """
    OpenGLRenderer - open_gl renderer
    
    Superclass: Renderer
    
    OpenGLRenderer is a concrete implementation of the abstract class
    Renderer. OpenGLRenderer interfaces to the open_gl graphics
    library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLRenderer, obj, update, **traits)
    
    def _get_shader_program(self):
        return wrap_vtk(self._vtk_obj.GetShaderProgram())
    def _set_shader_program(self, arg):
        old_val = self._get_shader_program()
        self._wrap_call(self._vtk_obj.SetShaderProgram,
                        deref_vtk(arg))
        self.trait_property_changed('shader_program', old_val, arg)
    shader_program = traits.Property(_get_shader_program, _set_shader_program, help=\
        """
        
        """
    )

    def _get_depth_peeling_higher_layer(self):
        return self._vtk_obj.GetDepthPeelingHigherLayer()
    depth_peeling_higher_layer = traits.Property(_get_depth_peeling_higher_layer, help=\
        """
        Is rendering at translucent geometry stage using depth peeling
        and rendering a layer other than the first one? (Boolean value)
        If so, the uniform variables use_texture and Texture can be set.
        (Used by OpenGLProperty or OpenGLTexture)
        """
    )

    def clear_lights(self):
        """
        V.clear_lights()
        C++: void ClearLights(void)
        Internal method temporarily removes lights before reloading them
        into graphics pipeline.
        """
        ret = self._vtk_obj.ClearLights()
        return ret
        

    def update_lights(self):
        """
        V.update_lights() -> int
        C++: int UpdateLights(void)
        Ask lights to load themselves into graphics pipeline.
        """
        ret = self._vtk_obj.UpdateLights()
        return ret
        

    _updateable_traits_ = \
    (('layer', 'GetLayer'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('maximum_number_of_peels',
    'GetMaximumNumberOfPeels'), ('two_sided_lighting',
    'GetTwoSidedLighting'), ('aspect', 'GetAspect'), ('ambient',
    'GetAmbient'), ('draw', 'GetDraw'), ('view_point', 'GetViewPoint'),
    ('background2', 'GetBackground2'), ('automatic_light_creation',
    'GetAutomaticLightCreation'), ('erase', 'GetErase'),
    ('occlusion_ratio', 'GetOcclusionRatio'), ('background',
    'GetBackground'), ('pixel_aspect', 'GetPixelAspect'),
    ('textured_background', 'GetTexturedBackground'), ('viewport',
    'GetViewport'), ('preserve_depth_buffer', 'GetPreserveDepthBuffer'),
    ('display_point', 'GetDisplayPoint'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'),
    ('near_clipping_plane_tolerance', 'GetNearClippingPlaneTolerance'),
    ('backing_store', 'GetBackingStore'), ('use_depth_peeling',
    'GetUseDepthPeeling'), ('world_point', 'GetWorldPoint'),
    ('light_follow_camera', 'GetLightFollowCamera'), ('reference_count',
    'GetReferenceCount'), ('gradient_background',
    'GetGradientBackground'), ('interactive', 'GetInteractive'))
    
    _full_traitnames_list_ = \
    (['automatic_light_creation', 'backing_store', 'debug', 'draw',
    'erase', 'global_warning_display', 'gradient_background',
    'interactive', 'light_follow_camera', 'preserve_depth_buffer',
    'textured_background', 'two_sided_lighting', 'use_depth_peeling',
    'allocated_render_time', 'ambient', 'aspect', 'background',
    'background2', 'display_point', 'layer', 'maximum_number_of_peels',
    'near_clipping_plane_tolerance', 'occlusion_ratio', 'pixel_aspect',
    'view_point', 'viewport', 'world_point'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLRenderer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLRenderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic_light_creation', 'backing_store', 'draw',
            'erase', 'gradient_background', 'interactive', 'light_follow_camera',
            'preserve_depth_buffer', 'textured_background', 'two_sided_lighting',
            'use_depth_peeling'], [], ['allocated_render_time', 'ambient',
            'aspect', 'background', 'background2', 'display_point', 'layer',
            'maximum_number_of_peels', 'near_clipping_plane_tolerance',
            'occlusion_ratio', 'pixel_aspect', 'view_point', 'viewport',
            'world_point']),
            title='Edit OpenGLRenderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLRenderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

