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

from tvtk.tvtk_classes.text_actor import TextActor


class ScaledTextActor(TextActor):
    """
    ScaledTextActor - create text that will scale as needed
    
    Superclass: TextActor
    
    ScaledTextActor is deprecated. New code should use TextActor
    with the Scaled = true option.
    
    See Also:
    
    TextActor Actor2D TextMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScaledTextActor, obj, update, **traits)
    
    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('minimum_size',
    'GetMinimumSize'), ('orientation', 'GetOrientation'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_line_height', 'GetMaximumLineHeight'), ('debug',
    'GetDebug'), ('dragable', 'GetDragable'), ('text_scale_mode',
    'GetTextScaleMode'), ('use_border_align', 'GetUseBorderAlign'),
    ('visibility', 'GetVisibility'), ('height', 'GetHeight'), ('width',
    'GetWidth'), ('layer_number', 'GetLayerNumber'), ('position2',
    'GetPosition2'), ('reference_count', 'GetReferenceCount'),
    ('position', 'GetPosition'), ('pickable', 'GetPickable'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('use_bounds',
    'GetUseBounds'), ('alignment_point', 'GetAlignmentPoint'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_border_align', 'use_bounds', 'visibility', 'text_scale_mode',
    'alignment_point', 'allocated_render_time', 'estimated_render_time',
    'height', 'layer_number', 'maximum_line_height', 'minimum_size',
    'orientation', 'position', 'position2', 'render_time_multiplier',
    'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScaledTextActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ScaledTextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_border_align', 'use_bounds', 'visibility'],
            ['text_scale_mode'], ['alignment_point', 'allocated_render_time',
            'estimated_render_time', 'height', 'layer_number',
            'maximum_line_height', 'minimum_size', 'orientation', 'position',
            'position2', 'render_time_multiplier', 'width']),
            title='Edit ScaledTextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScaledTextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

