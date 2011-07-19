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


class Heap(Object):
    """
    Heap - replacement for malloc/free and new/delete
    
    Superclass: Object
    
    This class is a replacement for malloc/free and new/delete for
    software that has inherent memory leak or performance problems. For
    example, external software such as the PLY library (vtk_ply) and VRML
    importer (vtk_vrml_importer) are often written with lots of malloc()
    calls but without the corresponding free() invocations. The class
    OrderedTriangulator may create and delete millions of new/delete
    calls. This class allows the overloading of the C++ new operator (or
    other memory allocation requests) by using the method
    allocate_memory(). Memory is deleted with an invocation of clean_all()
    (which deletes ALL memory; any given memory allocation cannot be
    deleted). Note: a block size can be used to control the size of each
    memory allocation. Requests for memory are fulfilled from the block
    until the block runs out, then a new block is created.
    
    Caveats:
    
    Do not use this class as a general replacement for system memory
    allocation.  This class should be used only as a last resort if
    memory leaks cannot be tracked down and eliminated by conventional
    means. Also, deleting memory from Heap is not supported. Only the
    deletion of the entire heap is. (A Reset() method allows you to reuse
    previously allocated memory.)
    
    See Also:
    
    VRMLImporter PLY OrderedTriangulator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHeap, obj, update, **traits)
    
    block_size = traits.Int(256000, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size at which blocks are allocated. If a memory
        request is bigger than the block size, then that size will be
        allocated.
        """
    )
    def _block_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlockSize,
                        self.block_size)

    def _get_number_of_allocations(self):
        return self._vtk_obj.GetNumberOfAllocations()
    number_of_allocations = traits.Property(_get_number_of_allocations, help=\
        """
        Get the number of allocations thus far.
        """
    )

    def _get_number_of_blocks(self):
        return self._vtk_obj.GetNumberOfBlocks()
    number_of_blocks = traits.Property(_get_number_of_blocks, help=\
        """
        Get the number of allocations thus far.
        """
    )

    def allocate_memory(self, *args):
        """
        V.allocate_memory(int) ->
        C++: void *AllocateMemory(size_t n)
        Allocate the memory requested.
        """
        ret = self._wrap_call(self._vtk_obj.AllocateMemory, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        This methods resets the current allocation location back to the
        beginning of the heap. This allows reuse of previously allocated
        memory which may be beneficial to performance in many cases.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def string_dup(self, *args):
        """
        V.string_dup(string) -> string
        C++: char *StringDup(const char *str)
        Convenience method performs string duplication.
        """
        ret = self._wrap_call(self._vtk_obj.StringDup, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('block_size', 'GetBlockSize'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'block_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Heap, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Heap properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['block_size']),
            title='Edit Heap properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Heap properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

