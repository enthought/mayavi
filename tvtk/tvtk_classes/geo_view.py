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


class GeoView(RenderView):
    """
    GeoView - A 3d geospatial view.
    
    Superclass: RenderView
    
    GeoView is a 3d globe view. The globe may contain a
    multi-resolution geometry source (vtk_geo_terrain), multiple
    multi-resolution image sources (vtk_geo_aligned_image_representation), as
    well as other representations such as RenderedGraphRepresentation.
    At a minimum, the view must have a terrain and one image
    representation. The view uses GeoInteractorStyle to orbit, zoom,
    and tilt the view, and contains a CompassWidget for manipulating
    the camera.
    
    Each terrain or image representation contains a GeoSource subclass
    which generates geometry or imagery at multiple resolutions. As the
    camera position changes, the terrain and/or image representations may
    ask its GeoSource to refine the geometry. This refinement is
    performed on a separate thread, and the data is added to the view
    when it becomes available.
    
    See Also:
    
    GeoTerrain GeoAlignedImageRepresentation GeoSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoView, obj, update, **traits)
    
    lock_heading = tvtk_base.false_bool_trait(help=\
        """
        Whether the view locks the heading when panning. Default is off.
        """
    )
    def _lock_heading_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLockHeading,
                        self.lock_heading_)

    def _get_geo_interactor_style(self):
        return wrap_vtk(self._vtk_obj.GetGeoInteractorStyle())
    def _set_geo_interactor_style(self, arg):
        old_val = self._get_geo_interactor_style()
        self._wrap_call(self._vtk_obj.SetGeoInteractorStyle,
                        deref_vtk(arg))
        self.trait_property_changed('geo_interactor_style', old_val, arg)
    geo_interactor_style = traits.Property(_get_geo_interactor_style, _set_geo_interactor_style, help=\
        """
        Convenience method for obtaining the internal interactor style.
        """
    )

    def _get_terrain(self):
        return wrap_vtk(self._vtk_obj.GetTerrain())
    def _set_terrain(self, arg):
        old_val = self._get_terrain()
        self._wrap_call(self._vtk_obj.SetTerrain,
                        deref_vtk(arg))
        self.trait_property_changed('terrain', old_val, arg)
    terrain = traits.Property(_get_terrain, _set_terrain, help=\
        """
        The terrain (geometry) model for this earth view.
        """
    )

    def add_default_image_representation(self, *args):
        """
        V.add_default_image_representation(ImageData)
            -> GeoAlignedImageRepresentation
        C++: GeoAlignedImageRepresentation *AddDefaultImageRepresentation(
            ImageData *image)
        Adds an image representation with a simple terrain model using
        the image in the specified file as the globe terrain.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddDefaultImageRepresentation, *my_args)
        return wrap_vtk(ret)

    def build_low_res_earth(self, *args):
        """
        V.build_low_res_earth([float, float, float])
        C++: void BuildLowResEarth(double origin[3])
        Rebuild low-res earth source; call after (re)setting origin.
        """
        ret = self._wrap_call(self._vtk_obj.BuildLowResEarth, *args)
        return ret

    def prepare_for_rendering(self):
        """
        V.prepare_for_rendering()
        C++: virtual void PrepareForRendering()"""
        ret = self._vtk_obj.PrepareForRendering()
        return ret
        

    _updateable_traits_ = \
    (('render_on_mouse_move', 'GetRenderOnMouseMove'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('interaction_mode', 'GetInteractionMode'), ('label_render_mode',
    'GetLabelRenderMode'), ('debug', 'GetDebug'), ('selection_mode',
    'GetSelectionMode'), ('icon_size', 'GetIconSize'),
    ('display_hover_text', 'GetDisplayHoverText'), ('reference_count',
    'GetReferenceCount'), ('label_placement_mode',
    'GetLabelPlacementMode'), ('lock_heading', 'GetLockHeading'))
    
    _full_traitnames_list_ = \
    (['debug', 'display_hover_text', 'global_warning_display',
    'lock_heading', 'render_on_mouse_move', 'interaction_mode',
    'label_placement_mode', 'label_render_mode', 'selection_mode',
    'icon_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['display_hover_text', 'lock_heading',
            'render_on_mouse_move'], ['interaction_mode', 'label_placement_mode',
            'label_render_mode', 'selection_mode'], ['icon_size']),
            title='Edit GeoView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

