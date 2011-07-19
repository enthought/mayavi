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

from tvtk.tvtk_classes.texture import Texture


class OpenGLTexture(Texture):
    """
    OpenGLTexture - open_gl texture map
    
    Superclass: Texture
    
    OpenGLTexture is a concrete implementation of the abstract class
    Texture. OpenGLTexture interfaces to the open_gl rendering
    library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLTexture, obj, update, **traits)
    
    def _get_index(self):
        return self._vtk_obj.GetIndex()
    index = traits.Property(_get_index, help=\
        """
        Get the open_gl texture name to which this texture is bound. This
        is available only if GL version >= 1.1
        """
    )

    _updateable_traits_ = \
    (('blending_mode', 'GetBlendingMode'), ('repeat', 'GetRepeat'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('map_color_scalars_through_lookup_table',
    'GetMapColorScalarsThroughLookupTable'), ('progress_text',
    'GetProgressText'), ('interpolate', 'GetInterpolate'),
    ('restrict_power_of2_image_smaller',
    'GetRestrictPowerOf2ImageSmaller'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('premultiplied_alpha',
    'GetPremultipliedAlpha'), ('quality', 'GetQuality'), ('edge_clamp',
    'GetEdgeClamp'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'edge_clamp', 'global_warning_display',
    'interpolate', 'map_color_scalars_through_lookup_table',
    'premultiplied_alpha', 'release_data_flag', 'repeat',
    'restrict_power_of2_image_smaller', 'quality', 'blending_mode',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLTexture, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['edge_clamp', 'interpolate',
            'map_color_scalars_through_lookup_table', 'premultiplied_alpha',
            'repeat', 'restrict_power_of2_image_smaller'], ['quality'],
            ['blending_mode']),
            title='Edit OpenGLTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

