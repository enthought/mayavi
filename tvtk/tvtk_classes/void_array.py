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


class VoidArray(Object):
    """
    VoidArray - dynamic, self-adjusting array of void* pointers
    
    Superclass: Object
    
    VoidArray is an array of pointers to void. It provides methods for
    insertion and retrieval of these pointers values, and will
    automatically resize itself to hold new data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVoidArray, obj, update, **traits)
    
    def get_void_pointer(self, *args):
        """
        V.get_void_pointer(int) ->
        C++: void *GetVoidPointer(IdType id)
        Get the void* pointer at the ith location.
        """
        ret = self._wrap_call(self._vtk_obj.GetVoidPointer, *args)
        return ret

    def set_void_pointer(self, *args):
        """
        V.set_void_pointer(int, )
        C++: void SetVoidPointer(IdType id, void *ptr)
        Set the void* pointer value at the ith location in the array.
        """
        ret = self._wrap_call(self._vtk_obj.SetVoidPointer, *args)
        return ret

    number_of_pointers = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of void* pointers held in the array.
        """
    )
    def _number_of_pointers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPointers,
                        self.number_of_pointers)

    def _get_data_type(self):
        return self._vtk_obj.GetDataType()
    data_type = traits.Property(_get_data_type, help=\
        """
        Return the type of data.
        """
    )

    def _get_data_type_size(self):
        return self._vtk_obj.GetDataTypeSize()
    data_type_size = traits.Property(_get_data_type_size, help=\
        """
        Return the size of the data contained in the array.
        """
    )

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: int Allocate(IdType sz, IdType ext=1000)
        Allocate memory for this array. Delete old storage only if
        necessary. Note that the parameter ext is no longer used.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(VoidArray)
        C++: void DeepCopy(VoidArray *va)
        Deep copy of another void array.
        """
        my_args = deref_array(args, [['vtkVoidArray']])
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Release storage and reset array to initial state.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def insert_next_void_pointer(self):
        """
        V.insert_next_void_pointer() -> int
        C++: IdType InsertNextVoidPointer(void *tuple)
        Insert (memory allocation performed) the void* pointer at the end
        of the array.
        """
        ret = self._vtk_obj.InsertNextVoidPointer()
        return ret
        

    def insert_void_pointer(self, *args):
        """
        V.insert_void_pointer(int, )
        C++: void InsertVoidPointer(IdType i, void *ptr)
        Insert (memory allocation performed) the void* into the ith
        location in the array.
        """
        ret = self._wrap_call(self._vtk_obj.InsertVoidPointer, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reuse already allocated data; make the container look like it is
        empty.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def squeeze(self):
        """
        V.squeeze()
        C++: void Squeeze()
        Resize the array to just fit the inserted memory. Reclaims extra
        memory.
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('number_of_pointers', 'GetNumberOfPointers'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_pointers'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VoidArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit VoidArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_pointers']),
            title='Edit VoidArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VoidArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

