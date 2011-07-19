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

from tvtk.tvtk_classes.tensor_probe_representation import TensorProbeRepresentation


class EllipsoidTensorProbeRepresentation(TensorProbeRepresentation):
    """
    EllipsoidTensorProbeRepresentation - A concrete implementation of
    TensorProbeRepresentation that renders tensors as ellipoids.
    
    Superclass: TensorProbeRepresentation
    
    EllipsoidTensorProbeRepresentation is a concrete implementation of
    TensorProbeRepresentation. It renders tensors as ellipsoids.
    Locations between two points when probed have the tensors linearly
    interpolated from the neighboring locations on the polyline.
    
    See Also:
    
    TensorProbeWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEllipsoidTensorProbeRepresentation, obj, update, **traits)
    
    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('debug', 'GetDebug'), ('probe_position', 'GetProbePosition'),
    ('probe_cell_id', 'GetProbeCellId'), ('use_bounds', 'GetUseBounds'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('visibility',
    'GetVisibility'), ('need_to_render', 'GetNeedToRender'),
    ('reference_count', 'GetReferenceCount'), ('place_factor',
    'GetPlaceFactor'), ('pickable', 'GetPickable'), ('dragable',
    'GetDragable'), ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'place_factor',
    'probe_cell_id', 'probe_position', 'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EllipsoidTensorProbeRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit EllipsoidTensorProbeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'place_factor', 'probe_cell_id', 'probe_position',
            'render_time_multiplier']),
            title='Edit EllipsoidTensorProbeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EllipsoidTensorProbeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

