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


class CellLinks(Object):
    """
    CellLinks - object represents upward pointers from points to list
    of cells using each point
    
    Superclass: Object
    
    CellLinks is a supplemental object to CellArray and
    CellTypes, enabling access from points to the cells using the
    points. CellLinks is a list of Links, each link represents a
    dynamic list of cell id's using the point. The information provided
    by this object can be used to determine neighbors and construct other
    local topological information.
    
    See Also:
    
    CellArray CellTypes
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellLinks, obj, update, **traits)
    
    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the memory in kilobytes consumed by this cell links array.
        Used to support streaming and reading/writing data. The value
        returned is guaranteed to be greater than or equal to the memory
        required to actually represent the data represented by this
        object. The information returned is valid only after the pipeline
        has been updated.
        """
    )

    def get_ncells(self, *args):
        """
        V.get_ncells(int) -> int
        C++: unsigned short GetNcells(IdType ptId)
        Get the number of cells using the point specified by pt_id.
        """
        ret = self._wrap_call(self._vtk_obj.GetNcells, *args)
        return ret

    def add_cell_reference(self, *args):
        """
        V.add_cell_reference(int, int)
        C++: void AddCellReference(IdType cellId, IdType ptId)
        Add the reference to the cell (cell_id) from the point (pt_id).
        This adds a reference to the cell_id from the cell list, but does
        not resize the list (extend memory with resize_cell_list(), if
        necessary).
        """
        ret = self._wrap_call(self._vtk_obj.AddCellReference, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int)
        C++: void Allocate(IdType numLinks, IdType ext=1000)
        Allocate the specified number of links (i.e., number of points)
        that will be built.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def build_links(self, *args):
        """
        V.build_links(DataSet)
        C++: void BuildLinks(DataSet *data)
        V.build_links(DataSet, CellArray)
        C++: void BuildLinks(DataSet *data, CellArray *Connectivity)
        Build the link list array.
        """
        my_args = deref_array(args, [['vtkDataSet'], ('vtkDataSet', 'vtkCellArray')])
        ret = self._wrap_call(self._vtk_obj.BuildLinks, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(CellLinks)
        C++: void DeepCopy(CellLinks *src)
        Standard deep_copy method.  Since this object contains no
        reference to other objects, there is no shallow_copy.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def delete_point(self, *args):
        """
        V.delete_point(int)
        C++: void DeletePoint(IdType ptId)
        Delete point (and storage) by destroying links to using cells.
        """
        ret = self._wrap_call(self._vtk_obj.DeletePoint, *args)
        return ret

    def insert_next_cell_reference(self, *args):
        """
        V.insert_next_cell_reference(int, int)
        C++: void InsertNextCellReference(IdType ptId,
            IdType cellId)
        Insert a cell id into the list of cells (at the end) using the
        cell id provided. (Make sure to extend the link list (if
        necessary) using the method resize_cell_list().)
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextCellReference, *args)
        return ret

    def insert_next_point(self, *args):
        """
        V.insert_next_point(int) -> int
        C++: IdType InsertNextPoint(int numLinks)
        Insert a new point into the cell-links data structure. The size
        parameter is the initial size of the list.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextPoint, *args)
        return ret

    def remove_cell_reference(self, *args):
        """
        V.remove_cell_reference(int, int)
        C++: void RemoveCellReference(IdType cellId, IdType ptId)
        Delete the reference to the cell (cell_id) from the point (pt_id).
        This removes the reference to the cell_id from the cell list, but
        does not resize the list (recover memory with resize_cell_list(),
        if necessary).
        """
        ret = self._wrap_call(self._vtk_obj.RemoveCellReference, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reset to a state of no entries without freeing the memory.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def resize_cell_list(self, *args):
        """
        V.resize_cell_list(int, int)
        C++: void ResizeCellList(IdType ptId, int size)
        Change the length of a point's link list (i.e., list of cells
        using a point) by the size specified.
        """
        ret = self._wrap_call(self._vtk_obj.ResizeCellList, *args)
        return ret

    def squeeze(self):
        """
        V.squeeze()
        C++: void Squeeze()
        Reclaim any unused memory.
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellLinks, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CellLinks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit CellLinks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellLinks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

