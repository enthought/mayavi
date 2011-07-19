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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class DEMReader(ImageAlgorithm):
    """
    DEMReader - read a digital elevation model (DEM) file
    
    Superclass: ImageAlgorithm
    
    DEMReader reads digital elevation files and creates image data.
    Digital elevation files are produced by the <A
    HREF="http://www.usgs.gov">US Geological Survey</A>. A complete
    description of the DEM file is located at the USGS site. The reader
    reads the entire dem file and create a ImageData that contains a
    single scalar component that is the elevation in meters. The spacing
    is also expressed in meters. A number of get methods provide access
    to fields on the header.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDEMReader, obj, update, **traits)
    
    elevation_reference = traits.Trait('elevation_bounds',
    tvtk_base.TraitRevPrefixMap({'elevation_bounds': 1, 'sea_level': 0}), help=\
        """
        Specify the elevation origin to use. By default, the elevation
        origin is equal to elevation_bounds[_0]. A more convenient origin
        is to use sea level (i.e., a value of 0.0).
        """
    )
    def _elevation_reference_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetElevationReference,
                        self.elevation_reference_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of Digital Elevation Model (DEM) file
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_accuracy_code(self):
        return self._vtk_obj.GetAccuracyCode()
    accuracy_code = traits.Property(_get_accuracy_code, help=\
        """
        Accuracy code for elevations. 0=unknown accuracy
        """
    )

    def _get_dem_level(self):
        return self._vtk_obj.GetDEMLevel()
    dem_level = traits.Property(_get_dem_level, help=\
        """
        Code 1=DEM-1, 2=DEM_2, ...
        """
    )

    def _get_elevation_bounds(self):
        return self._vtk_obj.GetElevationBounds()
    elevation_bounds = traits.Property(_get_elevation_bounds, help=\
        """
        Minimum and maximum elevation for the DEM. The units in the file
        are in elevation_unit_of_measure. This class converts them to
        meters.
        """
    )

    def _get_elevation_pattern(self):
        return self._vtk_obj.GetElevationPattern()
    elevation_pattern = traits.Property(_get_elevation_pattern, help=\
        """
        Code 1=regular, 2=random, reserved for future use
        """
    )

    def _get_elevation_unit_of_measure(self):
        return self._vtk_obj.GetElevationUnitOfMeasure()
    elevation_unit_of_measure = traits.Property(_get_elevation_unit_of_measure, help=\
        """
        Defining unit of measure for elevation coordinates throughout the
        file. 1 = feet, 2 = meters
        """
    )

    def _get_ground_system(self):
        return self._vtk_obj.GetGroundSystem()
    ground_system = traits.Property(_get_ground_system, help=\
        """
        Ground planimetric reference system
        """
    )

    def _get_ground_zone(self):
        return self._vtk_obj.GetGroundZone()
    ground_zone = traits.Property(_get_ground_zone, help=\
        """
        Zone in ground planimetric reference system
        """
    )

    def _get_local_rotation(self):
        return self._vtk_obj.GetLocalRotation()
    local_rotation = traits.Property(_get_local_rotation, help=\
        """
        Counterclockwise angle (in radians) from the primary axis of the
        planimetric reference to the primary axis of the DEM local
        reference system. IGNORED BY THIS IMPLEMENTATION.
        """
    )

    def _get_map_label(self):
        return self._vtk_obj.GetMapLabel()
    map_label = traits.Property(_get_map_label, help=\
        """
        An ASCII description of the map
        """
    )

    def _get_plane_unit_of_measure(self):
        return self._vtk_obj.GetPlaneUnitOfMeasure()
    plane_unit_of_measure = traits.Property(_get_plane_unit_of_measure, help=\
        """
        Defining unit of measure for ground planimetric coordinates
        throughout the file. 0 = radians, 1 = feet, 2 = meters, 3 =
        arc-seconds.
        """
    )

    def _get_polygon_size(self):
        return self._vtk_obj.GetPolygonSize()
    polygon_size = traits.Property(_get_polygon_size, help=\
        """
        Number of sides in the polygon which defines the coverage of the
        DEM file. Set to 4.
        """
    )

    def _get_profile_dimension(self):
        return self._vtk_obj.GetProfileDimension()
    profile_dimension = traits.Property(_get_profile_dimension, help=\
        """
        The number of rows and columns in the DEM.
        """
    )

    def _get_projection_parameters(self):
        return self._vtk_obj.GetProjectionParameters()
    projection_parameters = traits.Property(_get_projection_parameters, help=\
        """
        Map Projection parameters. All are zero.
        """
    )

    def _get_spatial_resolution(self):
        return self._vtk_obj.GetSpatialResolution()
    spatial_resolution = traits.Property(_get_spatial_resolution, help=\
        """
        DEM spatial resolution for x,y,z. Values are expressed in units
        of resolution. Since elevations are read as integers, this
        permits fractional elevations.
        """
    )

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('elevation_reference', 'GetElevationReference'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'elevation_reference', 'file_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DEMReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DEMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['elevation_reference'], ['file_name']),
            title='Edit DEMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DEMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

