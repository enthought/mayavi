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


class LogoRepresentation(BorderRepresentation):
    """
    LogoRepresentation - represent the LogoWidget
    
    Superclass: BorderRepresentation
    
    See Also:
    
    LogoWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLogoRepresentation, obj, update, **traits)
    
    def _get_image(self):
        return wrap_vtk(self._vtk_obj.GetImage())
    def _set_image(self, arg):
        old_val = self._get_image()
        self._wrap_call(self._vtk_obj.SetImage,
                        deref_vtk(arg))
        self.trait_property_changed('image', old_val, arg)
    image = traits.Property(_get_image, _set_image, help=\
        """
        Specify/retrieve the image to display in the balloon.
        """
    )

    def _get_image_property(self):
        return wrap_vtk(self._vtk_obj.GetImageProperty())
    def _set_image_property(self, arg):
        old_val = self._get_image_property()
        self._wrap_call(self._vtk_obj.SetImageProperty,
                        deref_vtk(arg))
        self.trait_property_changed('image_property', old_val, arg)
    image_property = traits.Property(_get_image_property, _set_image_property, help=\
        """
        Set/get the image property (relevant only if an image is shown).
        """
    )

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('minimum_size',
    'GetMinimumSize'), ('handle_size', 'GetHandleSize'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('position2',
    'GetPosition2'), ('need_to_render', 'GetNeedToRender'), ('dragable',
    'GetDragable'), ('proportional_resize', 'GetProportionalResize'),
    ('visibility', 'GetVisibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('show_border', 'GetShowBorder'),
    ('moving', 'GetMoving'), ('place_factor', 'GetPlaceFactor'),
    ('reference_count', 'GetReferenceCount'), ('position', 'GetPosition'),
    ('maximum_size', 'GetMaximumSize'), ('pickable', 'GetPickable'),
    ('tolerance', 'GetTolerance'), ('use_bounds', 'GetUseBounds'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'moving',
    'need_to_render', 'pickable', 'proportional_resize', 'use_bounds',
    'visibility', 'show_border', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'maximum_size',
    'minimum_size', 'place_factor', 'position', 'position2',
    'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LogoRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LogoRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['moving', 'need_to_render', 'proportional_resize',
            'use_bounds', 'visibility'], ['show_border'],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'maximum_size', 'minimum_size', 'place_factor', 'position',
            'position2', 'render_time_multiplier', 'tolerance']),
            title='Edit LogoRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LogoRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

