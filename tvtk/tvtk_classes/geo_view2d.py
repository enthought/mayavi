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

from tvtk.tvtk_classes.render_view import RenderView


class GeoView2D(RenderView):
    """
    GeoView2D - A 2d geospatial view.
    
    Superclass: RenderView
    
    GeoView is a 2d globe view. The globe may contain a
    multi-resolution geometry source (vtk_geo_terrain2d), multiple
    multi-resolution image sources (vtk_geo_aligned_image_representation), as
    well as other representations such as GeoGraphRepresentation2D. At
    a minimum, the view must have a terrain and one image representation.
    By default, you may select in the view with the left mouse button,
    pan with the middle button, and zoom with the right mouse button or
    scroll wheel.
    
    Each terrain or image representation contains a GeoSource subclass
    which generates geometry or imagery at multiple resolutions. As the
    camera position changes, the terrain and/or image representations may
    ask its GeoSource to refine the geometry. This refinement is
    performed on a separate thread, and the data is added to the view
    when it becomes available.
    
    See Also:
    
    GeoTerrain2D GeoAlignedImageRepresentation GeoSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoView2D, obj, update, **traits)
    
    def _get_surface(self):
        return wrap_vtk(self._vtk_obj.GetSurface())
    def _set_surface(self, arg):
        old_val = self._get_surface()
        self._wrap_call(self._vtk_obj.SetSurface,
                        deref_vtk(arg))
        self.trait_property_changed('surface', old_val, arg)
    surface = traits.Property(_get_surface, _set_surface, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('display_hover_text',
    'GetDisplayHoverText'), ('render_on_mouse_move',
    'GetRenderOnMouseMove'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interaction_mode',
    'GetInteractionMode'), ('icon_size', 'GetIconSize'), ('debug',
    'GetDebug'), ('selection_mode', 'GetSelectionMode'),
    ('label_placement_mode', 'GetLabelPlacementMode'),
    ('label_render_mode', 'GetLabelRenderMode'))
    
    _full_traitnames_list_ = \
    (['debug', 'display_hover_text', 'global_warning_display',
    'render_on_mouse_move', 'interaction_mode', 'label_placement_mode',
    'label_render_mode', 'selection_mode', 'icon_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoView2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoView2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['display_hover_text', 'render_on_mouse_move'],
            ['interaction_mode', 'label_placement_mode', 'label_render_mode',
            'selection_mode'], ['icon_size']),
            title='Edit GeoView2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoView2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

