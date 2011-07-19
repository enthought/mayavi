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


class CellTypes(Object):
    """
    CellTypes - object provides direct access to cells in CellArray
    and type information
    
    Superclass: Object
    
    This class is a supplemental object to CellArray to allow random
    access into cells as well as representing cell type information.  The
    "location" field is the location in the CellArray list in terms of
    an integer offset.  An integer offset was used instead of a pointer
    for easy storage and inter-process communication. The type
    information is defined in the file CellType.h.
    
    Caveats:
    
    Sometimes this class is used to pass type information independent of
    the random access (i.e., location) information. For example, see
    DataSet::GetCellTypes(). If you use the class in this way, you can
    use a location value of -1.
    
    See Also:
    
    CellArray CellLinks
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellTypes, obj, update, **traits)
    
    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the memory in kilobytes consumed by this cell type array.
        Used to support streaming and reading/writing data. The value
        returned is guaranteed to be greater than or equal to the memory
        required to actually represent the data represented by this
        object. The information returned is valid only after the pipeline
        has been updated.
        """
    )

    def get_cell_location(self, *args):
        """
        V.get_cell_location(int) -> int
        C++: int GetCellLocation(int cellId)
        Return the location of the cell in the associated CellArray.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellLocation, *args)
        return ret

    def get_cell_type(self, *args):
        """
        V.get_cell_type(int) ->
        C++: unsigned char GetCellType(int cellId)
        Return the type of cell.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellType, *args)
        return ret

    def get_class_name_from_type_id(self, *args):
        """
        V.get_class_name_from_type_id(int) -> string
        C++: static const char *GetClassNameFromTypeId(int typeId)
        Given an int (as defined in CellType.h) identifier for a class
        return it's classname.
        """
        ret = self._wrap_call(self._vtk_obj.GetClassNameFromTypeId, *args)
        return ret

    def _get_number_of_types(self):
        return self._vtk_obj.GetNumberOfTypes()
    number_of_types = traits.Property(_get_number_of_types, help=\
        """
        Return the number of types in the list.
        """
    )

    def get_type_id_from_class_name(self, *args):
        """
        V.get_type_id_from_class_name(string) -> int
        C++: static int GetTypeIdFromClassName(const char *classname)
        Given a data object classname, return it's int identified (as
        defined in CellType.h)
        """
        ret = self._wrap_call(self._vtk_obj.GetTypeIdFromClassName, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: int Allocate(int sz=512, int ext=1000)
        Allocate memory for this array. Delete old storage only if
        necessary.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(CellTypes)
        C++: void DeepCopy(CellTypes *src)
        Standard deep_copy method.  Since this object contains no
        reference to other objects, there is no shallow_copy.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def delete_cell(self, *args):
        """
        V.delete_cell(int)
        C++: void DeleteCell(IdType cellId)
        Delete cell by setting to NULL cell type.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteCell, *args)
        return ret

    def insert_cell(self, *args):
        """
        V.insert_cell(int, , int)
        C++: void InsertCell(int id, unsigned char type, int loc)
        Add a cell at specified id.
        """
        ret = self._wrap_call(self._vtk_obj.InsertCell, *args)
        return ret

    def insert_next_cell(self, *args):
        """
        V.insert_next_cell(, int) -> int
        C++: int InsertNextCell(unsigned char type, int loc)
        Add a cell to the object in the next available slot.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextCell, *args)
        return ret

    def insert_next_type(self):
        """
        V.insert_next_type() -> int
        C++: int InsertNextType(unsigned char type)
        Add the type specified to the end of the list. Range checking is
        performed.
        """
        ret = self._vtk_obj.InsertNextType()
        return ret
        

    def is_linear(self):
        """
        V.is_linear() -> int
        C++: static int IsLinear(unsigned char type)
        This convenience method is a fast check to determine if a cell
        type represents a linear or nonlinear cell.  This is generally
        much more efficient than getting the appropriate Cell and
        checking its is_linear method.
        """
        ret = self._vtk_obj.IsLinear()
        return ret
        

    def is_type(self):
        """
        V.is_type() -> int
        C++: int IsType(unsigned char type)
        Return 1 if type specified is contained in list; 0 otherwise.
        """
        ret = self._vtk_obj.IsType()
        return ret
        

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Initialize object without releasing memory.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def set_cell_types(self, *args):
        """
        V.set_cell_types(int, UnsignedCharArray, IntArray)
        C++: void SetCellTypes(int ncells,
            UnsignedCharArray *cellTypes, IntArray *cellLocations)
        Specify a group of cell types.
        """
        my_args = deref_array(args, [('int', 'vtkUnsignedCharArray', 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.SetCellTypes, *my_args)
        return ret

    def squeeze(self):
        """
        V.squeeze()
        C++: void Squeeze()
        Reclaim any extra memory.
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
            return super(CellTypes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CellTypes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit CellTypes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellTypes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

