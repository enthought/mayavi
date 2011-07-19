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

from tvtk.tvtk_classes.border_representation import BorderRepresentation


class ScalarBarRepresentation(BorderRepresentation):
    """
    ScalarBarRepresentation - represent scalar bar for
    ScalarBarWidget
    
    Superclass: BorderRepresentation
    
    This class represents a scalar bar for a ScalarBarWidget.  This
    class provides support for interactively placing a scalar bar on the
    2d overlay plane.  The scalar bar is defined by an instance of
    ScalarBarActor.
    
    One specialty of this class is that if the scalar bar is moved near
    enough to an edge, it's orientation is flipped to match that edge.
    
    See Also:
    
    ScalarBarWidget WidgetRepresentation ScalarBarActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarBarRepresentation, obj, update, **traits)
    
    def _get_scalar_bar_actor(self):
        return wrap_vtk(self._vtk_obj.GetScalarBarActor())
    def _set_scalar_bar_actor(self, arg):
        old_val = self._get_scalar_bar_actor()
        self._wrap_call(self._vtk_obj.SetScalarBarActor,
                        deref_vtk(arg))
        self.trait_property_changed('scalar_bar_actor', old_val, arg)
    scalar_bar_actor = traits.Property(_get_scalar_bar_actor, _set_scalar_bar_actor, help=\
        """
        The prop that is placed in the renderer.
        """
    )

    orientation = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Get/Set the orientation.
        """
    )
    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('minimum_size',
    'GetMinimumSize'), ('orientation', 'GetOrientation'),
    ('need_to_render', 'GetNeedToRender'), ('dragable', 'GetDragable'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('show_border', 'GetShowBorder'), ('moving', 'GetMoving'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('place_factor', 'GetPlaceFactor'), ('use_bounds', 'GetUseBounds'),
    ('handle_size', 'GetHandleSize'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('position2', 'GetPosition2'),
    ('proportional_resize', 'GetProportionalResize'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'), ('maximum_size',
    'GetMaximumSize'), ('pickable', 'GetPickable'), ('tolerance',
    'GetTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'moving',
    'need_to_render', 'pickable', 'proportional_resize', 'use_bounds',
    'visibility', 'show_border', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'maximum_size',
    'minimum_size', 'orientation', 'place_factor', 'position',
    'position2', 'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarBarRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarBarRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['moving', 'need_to_render', 'proportional_resize',
            'use_bounds', 'visibility'], ['show_border'],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'maximum_size', 'minimum_size', 'orientation', 'place_factor',
            'position', 'position2', 'render_time_multiplier', 'tolerance']),
            title='Edit ScalarBarRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarBarRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

