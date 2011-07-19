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


class CellArray(Object):
    """
    CellArray - object to represent cell connectivity
    
    Superclass: Object
    
    CellArray is a supporting object that explicitly represents cell
    connectivity. The cell array structure is a raw integer list of the
    form: (n,id1,id2,...,idn, n,id1,id2,...,idn, ...) where n is the
    number of points in the cell, and id is a zero-offset index into an
    associated point list.
    
    Advantages of this data structure are its compactness, simplicity,
    and easy interface to external data.  However, it is totally
    inadequate for random access.  This functionality (when necessary) is
    accomplished by using the CellTypes and CellLinks objects to
    extend the definition of the data structure.
    
    See Also:
    
    CellTypes CellLinks
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellArray, obj, update, **traits)
    
    traversal_location = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the current traversal location.
        """
    )
    def _traversal_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTraversalLocation,
                        self.traversal_location)

    number_of_cells = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of cells in the array. DO NOT do any kind of
        allocation, advanced use only.
        """
    )
    def _number_of_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfCells,
                        self.number_of_cells)

    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the memory in kilobytes consumed by this cell array. Used
        to support streaming and reading/writing data. The value returned
        is guaranteed to be greater than or equal to the memory required
        to actually represent the data represented by this object. The
        information returned is valid only after the pipeline has been
        updated.
        """
    )

    def get_cell(self, *args):
        """
        V.get_cell(int, IdList)
        C++: void GetCell(IdType loc, IdList *pts)
        Internal method used to retrieve a cell given an offset into the
        internal array.
        """
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetCell, *my_args)
        return ret

    def _get_data(self):
        return wrap_vtk(self._vtk_obj.GetData())
    data = traits.Property(_get_data, help=\
        """
        Return the underlying data as a data array.
        """
    )

    def get_insert_location(self, *args):
        """
        V.get_insert_location(int) -> int
        C++: IdType GetInsertLocation(int npts)
        Computes the current insertion location within the internal
        array. Used in conjunction with get_cell(int loc,...).
        """
        ret = self._wrap_call(self._vtk_obj.GetInsertLocation, *args)
        return ret

    def _get_max_cell_size(self):
        return self._vtk_obj.GetMaxCellSize()
    max_cell_size = traits.Property(_get_max_cell_size, help=\
        """
        Returns the size of the largest cell. The size is the number of
        points defining the cell.
        """
    )

    def get_next_cell(self, *args):
        """
        V.get_next_cell(IdList) -> int
        C++: int GetNextCell(IdList *pts)
        A cell traversal methods that is more efficient than DataSet
        traversal methods.  get_next_cell() gets the next cell in the list.
        If end of list is encountered, 0 is returned.
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.GetNextCell, *my_args)
        return ret

    def _get_number_of_connectivity_entries(self):
        return self._vtk_obj.GetNumberOfConnectivityEntries()
    number_of_connectivity_entries = traits.Property(_get_number_of_connectivity_entries, help=\
        """
        Get the total number of entries (i.e., data values) in the
        connectivity array. This may be much less than the allocated size
        (i.e., return value from get_size().)
        """
    )

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        Get the size of the allocated connectivity array.
        """
    )

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: int Allocate(const IdType sz, const int ext=1000)
        Allocate memory and set the size to extend by.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(CellArray)
        C++: void DeepCopy(CellArray *ca)
        Perform a deep copy (no reference counting) of the given cell
        array.
        """
        my_args = deref_array(args, [['vtkCellArray']])
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def estimate_size(self, *args):
        """
        V.estimate_size(int, int) -> int
        C++: IdType EstimateSize(IdType numCells, int maxPtsPerCell)
        Utility routines help manage memory of cell array. estimate_size()
        returns a value used to initialize and allocate memory for array
        based on number of cells and maximum number of points making up
        cell.  If every cell is the same size (in terms of number of
        points), then the memory estimate is guaranteed exact. (If not
        exact, use Squeeze() to reclaim any extra memory.)
        """
        ret = self._wrap_call(self._vtk_obj.EstimateSize, *args)
        return ret

    def init_traversal(self):
        """
        V.init_traversal()
        C++: void InitTraversal()
        A cell traversal methods that is more efficient than DataSet
        traversal methods.  init_traversal() initializes the traversal of
        the list of cells.
        """
        ret = self._vtk_obj.InitTraversal()
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Free any memory and reset to an empty state.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def insert_cell_point(self, *args):
        """
        V.insert_cell_point(int)
        C++: void InsertCellPoint(IdType id)
        Used in conjunction with insert_next_cell(int npts) to add another
        point to the list of cells.
        """
        ret = self._wrap_call(self._vtk_obj.InsertCellPoint, *args)
        return ret

    def insert_next_cell(self, *args):
        """
        V.insert_next_cell(Cell) -> int
        C++: IdType InsertNextCell(Cell *cell)
        V.insert_next_cell(IdList) -> int
        C++: IdType InsertNextCell(IdList *pts)
        V.insert_next_cell(int) -> int
        C++: IdType InsertNextCell(int npts)
        Insert a cell object. Return the cell id of the cell.
        """
        my_args = deref_array(args, [['vtkCell'], ['vtkIdList'], ['int']])
        ret = self._wrap_call(self._vtk_obj.InsertNextCell, *my_args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reuse list. Reset to initial condition.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def reverse_cell(self, *args):
        """
        V.reverse_cell(int)
        C++: void ReverseCell(IdType loc)
        Special method inverts ordering of current cell. Must be called
        carefully or the cell topology may be corrupted.
        """
        ret = self._wrap_call(self._vtk_obj.ReverseCell, *args)
        return ret

    def set_cells(self, *args):
        """
        V.set_cells(int, IdTypeArray)
        C++: void SetCells(IdType ncells, IdTypeArray *cells)
        Define multiple cells by providing a connectivity list. The list
        is in the form (npts,p0,p1,...p(npts-1), repeated for each cell).
        Be careful using this method because it discards the old cells,
        and anything referring these cells becomes invalid (for example,
        if build_cells() has been called see PolyData).  The traversal
        location is reset to the beginning of the list; the insertion
        location is set to the end of the list.
        """
        my_args = deref_array(args, [('int', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.SetCells, *my_args)
        return ret

    def squeeze(self):
        """
        V.squeeze()
        C++: void Squeeze()
        Reclaim any extra memory.
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    def update_cell_count(self, *args):
        """
        V.update_cell_count(int)
        C++: void UpdateCellCount(int npts)
        Used in conjunction with insert_next_cell(int npts) and
        insert_cell_point() to update the number of points defining the
        cell.
        """
        ret = self._wrap_call(self._vtk_obj.UpdateCellCount, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('traversal_location', 'GetTraversalLocation'), ('number_of_cells',
    'GetNumberOfCells'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_cells',
    'traversal_location'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CellArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_cells', 'traversal_location']),
            title='Edit CellArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
    def from_array(self, arr):
        '''Set the value of the data array using the passed
        Numeric array or Python list.  This is implemented
        efficiently.
        '''
        array_handler.array2vtkCellArray(arr, self._vtk_obj)
        self.update_traits()
    
    def to_array(self):
        '''Return the object as a Numeric array.'''
        return array_handler.vtk2array(self._vtk_obj.GetData())

