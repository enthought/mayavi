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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class ConnectivityFilter(UnstructuredGridAlgorithm):
    """
    ConnectivityFilter - extract data based on geometric connectivity
    
    Superclass: UnstructuredGridAlgorithm
    
    ConnectivityFilter is a filter that extracts cells that share
    common points and/or meet other connectivity criterion. (Cells that
    share vertices and meet other connectivity criterion such as scalar
    range are known as a region.)  The filter works in one of six ways:
    1) extract the largest connected region in the dataset; 2) extract
    specified region numbers; 3) extract all regions sharing specified
    point ids; 4) extract all regions sharing specified cell ids; 5)
    extract the region closest to the specified point; or 6) extract all
    regions (used to color the data by region).
    
    ConnectivityFilter is generalized to handle any type of input
    dataset. It generates output data of type UnstructuredGrid. If you
    know that your input type is PolyData, you may wish to use
    PolyDataConnectivityFilter.
    
    The behavior of ConnectivityFilter can be modified by turning on
    the boolean ivar scalar_connectivity. If this flag is on, the
    connectivity algorithm is modified so that cells are considered
    connected only if 1) they are geometrically connected (share a point)
    and 2) the scalar values of one of the cell's points falls in the
    scalar range specified. This use of scalar_connectivity is
    particularly useful for volume datasets: it can be used as a simple "connected
    segmentation" algorithm. For example, by using a seed voxel (i.e.,
    cell) on a known anatomical structure, connectivity will pull out all
    voxels "containing" the anatomical structure. These voxels can then
    be contoured or processed by other visualization filters.
    
    See Also:
    
    PolyDataConnectivityFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkConnectivityFilter, obj, update, **traits)
    
    color_regions = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the coloring of connected regions.
        """
    )
    def _color_regions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorRegions,
                        self.color_regions_)

    scalar_connectivity = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off connectivity based on scalar value. If on, cells are
        connected only if they share points AND one of the cells scalar
        values falls in the scalar range specified.
        """
    )
    def _scalar_connectivity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarConnectivity,
                        self.scalar_connectivity_)

    extraction_mode = traits.Trait('largest_region',
    tvtk_base.TraitRevPrefixMap({'all_regions': 5, 'specified_regions': 3, 'largest_region': 4, 'cell_seeded_regions': 2, 'closest_point_region': 6, 'point_seeded_regions': 1}), help=\
        """
        Control the extraction of connected surfaces.
        """
    )
    def _extraction_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractionMode,
                        self.extraction_mode_)

    scalar_range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarRange,
                        self.scalar_range)

    closest_point = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _closest_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClosestPoint,
                        self.closest_point)

    def _get_number_of_extracted_regions(self):
        return self._vtk_obj.GetNumberOfExtractedRegions()
    number_of_extracted_regions = traits.Property(_get_number_of_extracted_regions, help=\
        """
        Obtain the number of connected regions.
        """
    )

    def add_seed(self, *args):
        """
        V.add_seed(int)
        C++: void AddSeed(IdType id)
        Add a seed id (point or cell id). Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.AddSeed, *args)
        return ret

    def add_specified_region(self, *args):
        """
        V.add_specified_region(int)
        C++: void AddSpecifiedRegion(int id)
        Add a region id to extract. Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.AddSpecifiedRegion, *args)
        return ret

    def delete_seed(self, *args):
        """
        V.delete_seed(int)
        C++: void DeleteSeed(IdType id)
        Delete a seed id (point or cell id). Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteSeed, *args)
        return ret

    def delete_specified_region(self, *args):
        """
        V.delete_specified_region(int)
        C++: void DeleteSpecifiedRegion(int id)
        Delete a region id to extract. Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteSpecifiedRegion, *args)
        return ret

    def initialize_seed_list(self):
        """
        V.initialize_seed_list()
        C++: void InitializeSeedList()
        Initialize list of point ids/cell ids used to seed regions.
        """
        ret = self._vtk_obj.InitializeSeedList()
        return ret
        

    def initialize_specified_region_list(self):
        """
        V.initialize_specified_region_list()
        C++: void InitializeSpecifiedRegionList()
        Initialize list of region ids to extract.
        """
        ret = self._vtk_obj.InitializeSpecifiedRegionList()
        return ret
        

    _updateable_traits_ = \
    (('color_regions', 'GetColorRegions'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('scalar_connectivity',
    'GetScalarConnectivity'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('closest_point', 'GetClosestPoint'),
    ('extraction_mode', 'GetExtractionMode'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'),
    ('scalar_range', 'GetScalarRange'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'color_regions', 'debug', 'global_warning_display',
    'release_data_flag', 'scalar_connectivity', 'extraction_mode',
    'closest_point', 'progress_text', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ConnectivityFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ConnectivityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['color_regions', 'scalar_connectivity'],
            ['extraction_mode'], ['closest_point', 'scalar_range']),
            title='Edit ConnectivityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ConnectivityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

