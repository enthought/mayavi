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

from tvtk.tvtk_classes.object import Object


class MergeCells(Object):
    """
    MergeCells - merges any number of DataSets back into a single
    
    Superclass: Object
    
    Designed to work with distributed DataSets, this class will take
       DataSets and merge them back into a single UnstructuredGrid.
    
    
       The Points object of the unstructured grid will have data type
       VTK_FLOAT, regardless of the data type of the points of the
       input DataSets.  If this is a problem, someone must let me
    know.
    
    
       It is assumed the different data_sets have the same field arrays. 
    If
       the name of a global point ID array is provided, this class will
       refrain from including duplicate points in the merged Ugrid.  This
       class differs from AppendFilter in these ways: (1) it uses less
       memory than that class (which uses memory equal to twice the size
       of the final Ugrid) but requires that you know the size of the
       final Ugrid in advance (2) this class assumes the individual
    data_sets have
       the same field arrays, while AppendFilter intersects the field
       arrays (3) this class knows duplicate points may be appearing in
       the data_sets and can filter those out, (4) this class is not a
    filter.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMergeCells, obj, update, **traits)
    
    merge_duplicate_points = tvtk_base.true_bool_trait(help=\
        """
        MergeCells attempts eliminate duplicate points when merging
          data sets.  If for some reason you don't want it to do this,
          than merge_duplicate_points_off().
        """
    )
    def _merge_duplicate_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMergeDuplicatePoints,
                        self.merge_duplicate_points_)

    def _get_unstructured_grid(self):
        return wrap_vtk(self._vtk_obj.GetUnstructuredGrid())
    def _set_unstructured_grid(self, arg):
        old_val = self._get_unstructured_grid()
        self._wrap_call(self._vtk_obj.SetUnstructuredGrid,
                        deref_vtk(arg))
        self.trait_property_changed('unstructured_grid', old_val, arg)
    unstructured_grid = traits.Property(_get_unstructured_grid, _set_unstructured_grid, help=\
        """
        Set the UnstructuredGrid object that will become the
           union of the data_sets specified in merge_data_set calls.
           MergeCells assumes this grid is empty at first.
        """
    )

    total_number_of_data_sets = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        We need to know the number of different data sets that will
           be merged into one so we can pre-allocate some arrays.
           This can be an upper bound, not necessarily exact.
        """
    )
    def _total_number_of_data_sets_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTotalNumberOfDataSets,
                        self.total_number_of_data_sets)

    total_number_of_cells = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the total number of cells in the final
        UnstructuredGrid.
           Make this call before any call to merge_data_set().
        """
    )
    def _total_number_of_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTotalNumberOfCells,
                        self.total_number_of_cells)

    total_number_of_points = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the total number of points in the final
        UnstructuredGrid
           Make this call before any call to merge_data_set().  This is an
           upper bound, since some points may be duplicates.
        """
    )
    def _total_number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTotalNumberOfPoints,
                        self.total_number_of_points)

    point_merge_tolerance = traits.Trait(0.0010000000475, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        MergeCells attempts eliminate duplicate points when merging
          data sets.  If no global point ID field array name is provided,
          it will use a point locator to find duplicate points.  You can
          set a tolerance for that locator here.  The default tolerance
          is 10e-4.
        """
    )
    def _point_merge_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointMergeTolerance,
                        self.point_merge_tolerance)

    use_global_cell_ids = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        MergeCells will detect and filter out duplicate cells if you
          provide it the name of a global cell ID array.
        """
    )
    def _use_global_cell_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseGlobalCellIds,
                        self.use_global_cell_ids)

    use_global_ids = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        MergeCells attempts eliminate duplicate points when merging
          data sets.  This is done most efficiently if a global point ID
          field array is available.  Set the name of the point array if
        you
          have one.
        """
    )
    def _use_global_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseGlobalIds,
                        self.use_global_ids)

    def finish(self):
        """
        V.finish()
        C++: void Finish()
        Call Finish() after merging last data_set to free unneeded memory
        and to
           make sure the ugrid's get_number_of_points() reflects the actual
           number of points set, not the number allocated.
        """
        ret = self._vtk_obj.Finish()
        return ret
        

    def merge_data_set(self, *args):
        """
        V.merge_data_set(DataSet) -> int
        C++: int MergeDataSet(DataSet *set)
        Provide a data_set to be merged in to the final unstructured_grid.
           This call returns after the merge has completed.  Be sure to
        call
           set_total_number_of_cells, set_total_number_of_points, and
        set_total_number_of_data_sets
           before making this call.  Return 0 if OK, -1 if error.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MergeDataSet, *my_args)
        return ret

    _updateable_traits_ = \
    (('total_number_of_cells', 'GetTotalNumberOfCells'),
    ('use_global_cell_ids', 'GetUseGlobalCellIds'),
    ('total_number_of_points', 'GetTotalNumberOfPoints'),
    ('total_number_of_data_sets', 'GetTotalNumberOfDataSets'),
    ('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('point_merge_tolerance', 'GetPointMergeTolerance'),
    ('use_global_ids', 'GetUseGlobalIds'), ('merge_duplicate_points',
    'GetMergeDuplicatePoints'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'merge_duplicate_points',
    'point_merge_tolerance', 'total_number_of_cells',
    'total_number_of_data_sets', 'total_number_of_points',
    'use_global_cell_ids', 'use_global_ids'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MergeCells, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MergeCells properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['merge_duplicate_points'], [],
            ['point_merge_tolerance', 'total_number_of_cells',
            'total_number_of_data_sets', 'total_number_of_points',
            'use_global_cell_ids', 'use_global_ids']),
            title='Edit MergeCells properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MergeCells properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

