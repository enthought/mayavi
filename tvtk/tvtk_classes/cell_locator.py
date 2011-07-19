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

from tvtk.tvtk_classes.abstract_cell_locator import AbstractCellLocator


class CellLocator(AbstractCellLocator):
    """
    CellLocator - octree-based spatial search object to quickly locate
    cells
    
    Superclass: AbstractCellLocator
    
    CellLocator is a spatial search object to quickly locate cells in
    3d. CellLocator uses a uniform-level octree subdivision, where
    each octant (an octant is also referred to as a bucket) carries an
    indication of whether it is empty or not, and each leaf octant
    carries a list of the cells inside of it. (An octant is not empty if
    it has one or more cells inside of it.)  Typical operations are
    intersection with a line to return candidate cells, or intersection
    with another CellLocator to return candidate cells.
    
    Caveats:
    
    Many other types of spatial locators have been developed, such as
    variable depth octrees and kd-trees. These are often more efficient
    for the operations described here. CellLocator has been designed
    for subclassing; so these locators can be derived if necessary.
    
    See Also:
    
    Locator PointLocator OBBTree
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellLocator, obj, update, **traits)
    
    number_of_cells_per_bucket = traits.Int(25, enter_set=True, auto_set=False, help=\
        """
        Specify the average number of cells in each octant.
        """
    )
    def _number_of_cells_per_bucket_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfCellsPerBucket,
                        self.number_of_cells_per_bucket)

    def get_cells(self, *args):
        """
        V.get_cells(int) -> IdList
        C++: virtual IdList *GetCells(int bucket)
        Get the cells in a particular bucket.
        """
        ret = self._wrap_call(self._vtk_obj.GetCells, *args)
        return wrap_vtk(ret)

    def _get_number_of_buckets(self):
        return self._vtk_obj.GetNumberOfBuckets()
    number_of_buckets = traits.Property(_get_number_of_buckets, help=\
        """
        Return number of buckets available. Insure that the locator has
        been built before attempting to access buckets (octants).
        """
    )

    def build_locator_if_needed(self):
        """
        V.build_locator_if_needed()
        C++: virtual void BuildLocatorIfNeeded()
        Satisfy Locator abstract interface.
        """
        ret = self._vtk_obj.BuildLocatorIfNeeded()
        return ret
        

    def build_locator_internal(self):
        """
        V.build_locator_internal()
        C++: virtual void BuildLocatorInternal()
        Satisfy Locator abstract interface.
        """
        ret = self._vtk_obj.BuildLocatorInternal()
        return ret
        

    def force_build_locator(self):
        """
        V.force_build_locator()
        C++: virtual void ForceBuildLocator()
        Satisfy Locator abstract interface.
        """
        ret = self._vtk_obj.ForceBuildLocator()
        return ret
        

    _updateable_traits_ = \
    (('use_existing_search_structure', 'GetUseExistingSearchStructure'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('max_level',
    'GetMaxLevel'), ('retain_cell_lists', 'GetRetainCellLists'), ('debug',
    'GetDebug'), ('automatic', 'GetAutomatic'), ('lazy_evaluation',
    'GetLazyEvaluation'), ('cache_cell_bounds', 'GetCacheCellBounds'),
    ('reference_count', 'GetReferenceCount'), ('number_of_cells_per_node',
    'GetNumberOfCellsPerNode'), ('tolerance', 'GetTolerance'),
    ('number_of_cells_per_bucket', 'GetNumberOfCellsPerBucket'))
    
    _full_traitnames_list_ = \
    (['automatic', 'cache_cell_bounds', 'debug', 'global_warning_display',
    'lazy_evaluation', 'retain_cell_lists',
    'use_existing_search_structure', 'max_level',
    'number_of_cells_per_bucket', 'number_of_cells_per_node',
    'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CellLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic', 'cache_cell_bounds', 'lazy_evaluation',
            'retain_cell_lists', 'use_existing_search_structure'], [],
            ['max_level', 'number_of_cells_per_bucket',
            'number_of_cells_per_node', 'tolerance']),
            title='Edit CellLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

