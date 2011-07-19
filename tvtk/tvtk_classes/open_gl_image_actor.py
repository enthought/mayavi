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

from tvtk.tvtk_classes.image_actor import ImageActor


class OpenGLImageActor(ImageActor):
    """
    OpenGLImageActor - open_gl texture map
    
    Superclass: ImageActor
    
    OpenGLImageActor is a concrete implementation of the abstract
    class ImageActor. OpenGLImageActor interfaces to the open_gl
    rendering library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLImageActor, obj, update, **traits)
    
    def load(self, *args):
        """
        V.load(Renderer)
        C++: void Load(Renderer *ren)
        Implement base class method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Load, *my_args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('origin', 'GetOrigin'), ('scale',
    'GetScale'), ('orientation', 'GetOrientation'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('debug',
    'GetDebug'), ('dragable', 'GetDragable'), ('z_slice', 'GetZSlice'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('allocated_render_time', 'GetAllocatedRenderTime'), ('visibility',
    'GetVisibility'), ('interpolate', 'GetInterpolate'),
    ('display_extent', 'GetDisplayExtent'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'interpolate',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'display_extent', 'estimated_render_time', 'opacity', 'orientation',
    'origin', 'position', 'render_time_multiplier', 'scale', 'z_slice'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLImageActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLImageActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['interpolate', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'display_extent', 'estimated_render_time',
            'opacity', 'orientation', 'origin', 'position',
            'render_time_multiplier', 'scale', 'z_slice']),
            title='Edit OpenGLImageActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLImageActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

