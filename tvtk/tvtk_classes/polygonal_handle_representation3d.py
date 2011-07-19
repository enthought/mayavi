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

from tvtk.tvtk_classes.abstract_polygonal_handle_representation3d import AbstractPolygonalHandleRepresentation3D


class PolygonalHandleRepresentation3D(AbstractPolygonalHandleRepresentation3D):
    """
    PolygonalHandleRepresentation3D - represent a user defined handle
    geometry in 3d space
    
    Superclass: AbstractPolygonalHandleRepresentation3D
    
    This class serves as the geometrical representation of a
    HandleWidget. The handle can be represented by an arbitrary
    polygonal data (vtk_poly_data), set via set_handle(vtk_poly_data *). The
    actual position of the handle will be initially assumed to be
    (0,0,0). You can specify an offset from this position if desired.
    
    See Also:
    
    PointHandleRepresentation3D HandleRepresentation
    HandleWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolygonalHandleRepresentation3D, obj, update, **traits)
    
    offset = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    _updateable_traits_ = \
    (('display_position', 'GetDisplayPosition'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('handle_size', 'GetHandleSize'),
    ('need_to_render', 'GetNeedToRender'), ('dragable', 'GetDragable'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('active_representation', 'GetActiveRepresentation'), ('offset',
    'GetOffset'), ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('place_factor', 'GetPlaceFactor'), ('constrained', 'GetConstrained'),
    ('use_bounds', 'GetUseBounds'), ('handle_visibility',
    'GetHandleVisibility'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('tolerance', 'GetTolerance'),
    ('label_visibility', 'GetLabelVisibility'), ('label_text',
    'GetLabelText'), ('reference_count', 'GetReferenceCount'),
    ('pickable', 'GetPickable'), ('world_position', 'GetWorldPosition'))
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'handle_visibility', 'label_visibility',
    'need_to_render', 'pickable', 'use_bounds', 'visibility',
    'allocated_render_time', 'display_position', 'estimated_render_time',
    'handle_size', 'label_text', 'offset', 'place_factor',
    'render_time_multiplier', 'tolerance', 'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolygonalHandleRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PolygonalHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['active_representation', 'constrained',
            'handle_visibility', 'label_visibility', 'need_to_render',
            'use_bounds', 'visibility'], [], ['allocated_render_time',
            'display_position', 'estimated_render_time', 'handle_size',
            'label_text', 'offset', 'place_factor', 'render_time_multiplier',
            'tolerance', 'world_position']),
            title='Edit PolygonalHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolygonalHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

