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

from tvtk.tvtk_classes.actor2d import Actor2D


class TexturedActor2D(Actor2D):
    """
    TexturedActor2D - actor that draws 2d data with texture support
    
    Superclass: Actor2D
    
    TexturedActor2D is an actor2d which has additional support for
    textures, just like Actor. To use textures, the geometry must have
    texture coordinates, and the texture must be set with set_texture().
    
    See Also:
    
    Actor2D Prop Mapper2D Property2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTexturedActor2D, obj, update, **traits)
    
    def _get_texture(self):
        return wrap_vtk(self._vtk_obj.GetTexture())
    def _set_texture(self, arg):
        old_val = self._get_texture()
        self._wrap_call(self._vtk_obj.SetTexture,
                        deref_vtk(arg))
        self.trait_property_changed('texture', old_val, arg)
    texture = traits.Property(_get_texture, _set_texture, help=\
        """
        Set/Get the texture object to control rendering texture maps. 
        This will be a Texture object. An actor does not need to have
        an associated texture map and multiple actors can share one
        texture.
        """
    )

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('layer_number',
    'GetLayerNumber'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('position2', 'GetPosition2'), ('debug',
    'GetDebug'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('height', 'GetHeight'), ('width', 'GetWidth'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('pickable', 'GetPickable'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'height', 'layer_number', 'position',
    'position2', 'render_time_multiplier', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TexturedActor2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TexturedActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'height',
            'layer_number', 'position', 'position2', 'render_time_multiplier',
            'width']),
            title='Edit TexturedActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TexturedActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

