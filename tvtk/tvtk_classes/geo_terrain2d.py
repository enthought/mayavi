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

from tvtk.tvtk_classes.geo_terrain import GeoTerrain


class GeoTerrain2D(GeoTerrain):
    """
    GeoTerrain2D - A 2d terrain model for the globe.
    
    Superclass: GeoTerrain
    
    GeoTerrain2D contains a multi-resolution tree of geometry
    representing the globe. It uses a GeoSource subclass to generate
    the terrain, such as GeoProjectionSource. This source must be set
    before using the terrain in a GeoView2D. The terrain also contains
    an add_actors() method which updates the set of actors representing
    the globe given the current camera position.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoTerrain2D, obj, update, **traits)
    
    location_tolerance = traits.Float(50.0, enter_set=True, auto_set=False, help=\
        """
        The maximum allowed deviation of geometry in pixels. Geometry
        will be refined if the deviation is larger than the tolerance.
        """
    )
    def _location_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLocationTolerance,
                        self.location_tolerance)

    texture_tolerance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The maximum size of a single texel in pixels. Images will be
        refined if a texel becomes larger than the tolerance.
        """
    )
    def _texture_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureTolerance,
                        self.texture_tolerance)

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    transform = traits.Property(_get_transform, help=\
        """
        Return the projection transformation used by this 2d terrain.
        """
    )

    _updateable_traits_ = \
    (('texture_tolerance', 'GetTextureTolerance'), ('origin',
    'GetOrigin'), ('max_level', 'GetMaxLevel'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'),
    ('debug', 'GetDebug'), ('location_tolerance', 'GetLocationTolerance'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'location_tolerance',
    'max_level', 'origin', 'texture_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoTerrain2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoTerrain2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['location_tolerance', 'max_level', 'origin',
            'texture_tolerance']),
            title='Edit GeoTerrain2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoTerrain2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

