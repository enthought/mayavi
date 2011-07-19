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

from tvtk.tvtk_classes.geo_source import GeoSource


class GeoAlignedImageSource(GeoSource):
    """
    GeoAlignedImageSource - Splits hi-res image into tiles.
    
    Superclass: GeoSource
    
    GeoAlignedImageSource uses a high resolution image to generate
    tiles at multiple resolutions in a hierarchy. It should be used as a
    source in GeoAlignedImageRepresentation.
    
    See Also:
    
    GeoAlignedImageRepresentation GeoView GeoView2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoAlignedImageSource, obj, update, **traits)
    
    power_of_two_size = tvtk_base.true_bool_trait(help=\
        """
        Whether to force image sizes to a power of two.
        """
    )
    def _power_of_two_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPowerOfTwoSize,
                        self.power_of_two_size_)

    longitude_range = traits.Array(shape=(2,), value=(-180.0, 180.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _longitude_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLongitudeRange,
                        self.longitude_range)

    def _get_image(self):
        return wrap_vtk(self._vtk_obj.GetImage())
    def _set_image(self, arg):
        old_val = self._get_image()
        self._wrap_call(self._vtk_obj.SetImage,
                        deref_vtk(arg))
        self.trait_property_changed('image', old_val, arg)
    image = traits.Property(_get_image, _set_image, help=\
        """
        The high-resolution image to be used to cover the globe.
        """
    )

    latitude_range = traits.Array(shape=(2,), value=(-90.0, 90.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _latitude_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatitudeRange,
                        self.latitude_range)

    overlap = traits.Trait(0.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        The overlap of adjacent tiles.
        """
    )
    def _overlap_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOverlap,
                        self.overlap)

    _updateable_traits_ = \
    (('latitude_range', 'GetLatitudeRange'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('longitude_range', 'GetLongitudeRange'), ('power_of_two_size',
    'GetPowerOfTwoSize'), ('reference_count', 'GetReferenceCount'),
    ('overlap', 'GetOverlap'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'power_of_two_size',
    'latitude_range', 'longitude_range', 'overlap'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoAlignedImageSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoAlignedImageSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['power_of_two_size'], [], ['latitude_range',
            'longitude_range', 'overlap']),
            title='Edit GeoAlignedImageSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoAlignedImageSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

