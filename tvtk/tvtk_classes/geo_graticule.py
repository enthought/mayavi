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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class GeoGraticule(PolyDataAlgorithm):
    """
    GeoGraticule - Create a polygonal lat-long grid
    
    Superclass: PolyDataAlgorithm
    
    This filter generates polydata to illustrate the distortions
    introduced by a map projection. The level parameter specifies the
    number of lines to be drawn. Poles are treated differently than other
    regions; hence the use of a Level parameter instead of a
    number_of_lines parameter. The latitude and longitude are specified as
    half-open intervals with units of degrees. By default the latitude
    bounds are [-90,90[ and the longitude bounds are [0,180[.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoGraticule, obj, update, **traits)
    
    longitude_level = traits.Trait(1, traits.Range(0, 11, enter_set=True, auto_set=False), help=\
        """
        The frequency level of longitude lines.
        """
    )
    def _longitude_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLongitudeLevel,
                        self.longitude_level)

    longitude_bounds = traits.Array(shape=(2,), value=(0.0, 180.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _longitude_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLongitudeBounds,
                        self.longitude_bounds)

    geometry_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set//get the type(s) of cells that will be output by the filter.
        By default, polylines are output. You may also request
        quadrilaterals. This is a bit vector of geometry_type enums.
        """
    )
    def _geometry_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometryType,
                        self.geometry_type)

    latitude_bounds = traits.Array(shape=(2,), value=(-90.0, 90.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _latitude_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatitudeBounds,
                        self.latitude_bounds)

    latitude_level = traits.Trait(2, traits.Range(0, 11, enter_set=True, auto_set=False), help=\
        """
        The frequency level of latitude lines.
        """
    )
    def _latitude_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatitudeLevel,
                        self.latitude_level)

    def get_latitude_delta(self, *args):
        """
        V.get_latitude_delta(int) -> float
        C++: static double GetLatitudeDelta(int level)
        The latitude delta at a certain frequency level.
        """
        ret = self._wrap_call(self._vtk_obj.GetLatitudeDelta, *args)
        return ret

    def get_longitude_delta(self, *args):
        """
        V.get_longitude_delta(int) -> float
        C++: static double GetLongitudeDelta(int level)
        The longitude delta at a certain frequency level.
        """
        ret = self._wrap_call(self._vtk_obj.GetLongitudeDelta, *args)
        return ret

    _updateable_traits_ = \
    (('longitude_bounds', 'GetLongitudeBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('geometry_type', 'GetGeometryType'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('latitude_level', 'GetLatitudeLevel'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('longitude_level',
    'GetLongitudeLevel'), ('latitude_bounds', 'GetLatitudeBounds'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'geometry_type', 'latitude_bounds',
    'latitude_level', 'longitude_bounds', 'longitude_level',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoGraticule, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoGraticule properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['geometry_type', 'latitude_bounds',
            'latitude_level', 'longitude_bounds', 'longitude_level']),
            title='Edit GeoGraticule properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoGraticule properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

