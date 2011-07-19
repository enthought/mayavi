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


class GeoSampleArcs(PolyDataAlgorithm):
    """
    GeoSampleArcs - Samples geospatial lines at regular intervals.
    
    Superclass: PolyDataAlgorithm
    
    GeoSampleArcs refines lines in the input polygonal data so that
    the distance between adjacent points is no more than a threshold
    distance. Points are interpolated along the surface of the globe.
    This is useful in order to keep lines such as political boundaries
    from intersecting the globe and becoming invisible.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoSampleArcs, obj, update, **traits)
    
    output_coordinate_system = traits.Trait('rectangular',
    tvtk_base.TraitRevPrefixMap({'spherical': 1, 'rectangular': 0}), help=\
        """
        The desired output coordinate system. RECTANGULAR is x,y,z meters
        relative the the earth center. SPHERICAL is
        longitude,latitude,altitude.
        """
    )
    def _output_coordinate_system_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputCoordinateSystem,
                        self.output_coordinate_system_)

    input_coordinate_system = traits.Trait('rectangular',
    tvtk_base.TraitRevPrefixMap({'spherical': 1, 'rectangular': 0}), help=\
        """
        The input coordinate system. RECTANGULAR is x,y,z meters relative
        the the earth center. SPHERICAL is longitude,latitude,altitude.
        """
    )
    def _input_coordinate_system_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputCoordinateSystem,
                        self.input_coordinate_system_)

    globe_radius = traits.Float(6356750.0, enter_set=True, auto_set=False, help=\
        """
        The base radius used to determine the earth's surface. Default is
        the earth's radius in meters. TODO: Change this to take in a
        GeoTerrain to get altitude.
        """
    )
    def _globe_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobeRadius,
                        self.globe_radius)

    maximum_distance_meters = traits.Float(100000.0, enter_set=True, auto_set=False, help=\
        """
        The maximum distance, in meters, between adjacent points.
        """
    )
    def _maximum_distance_meters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDistanceMeters,
                        self.maximum_distance_meters)

    _updateable_traits_ = \
    (('globe_radius', 'GetGlobeRadius'), ('input_coordinate_system',
    'GetInputCoordinateSystem'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_coordinate_system',
    'GetOutputCoordinateSystem'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('maximum_distance_meters', 'GetMaximumDistanceMeters'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'input_coordinate_system',
    'output_coordinate_system', 'globe_radius', 'maximum_distance_meters',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoSampleArcs, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoSampleArcs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['input_coordinate_system',
            'output_coordinate_system'], ['globe_radius',
            'maximum_distance_meters']),
            title='Edit GeoSampleArcs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoSampleArcs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

