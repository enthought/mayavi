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


class PriorityQueue(Object):
    """
    PriorityQueue - an list of ids arranged in priority order
    
    Superclass: Object
    
    PriorityQueue is a general object for creating and manipulating
    lists of object ids (e.g., point or cell ids). Object ids are sorted
    according to a user-specified priority, where entries at the top of
    the queue have the smallest values.
    
    This implementation provides a feature beyond the usual ability to
    insert and retrieve (or pop) values from the queue. It is also
    possible to pop any item in the queue given its id number. This
    allows you to delete entries in the queue which can useful for
    reinserting an item into the queue.
    
    Caveats:
    
    This implementation is a variation of the priority queue described in "Data Structures &
    Algorithms" by Aho, Hopcroft, Ullman. It creates a balanced,
    partially ordered binary tree implemented as an ordered array. This
    avoids the overhead associated with parent/child pointers, and
    frequent memory allocation and deallocation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPriorityQueue, obj, update, **traits)
    
    def _get_number_of_items(self):
        return self._vtk_obj.GetNumberOfItems()
    number_of_items = traits.Property(_get_number_of_items, help=\
        """
        Return the number of items in this queue.
        """
    )

    def get_priority(self, *args):
        """
        V.get_priority(int) -> float
        C++: double GetPriority(IdType id)
        Get the priority of an entry in the queue with specified id.
        Returns priority value of that id or VTK_DOUBLE_MAX if not in
        queue.
        """
        ret = self._wrap_call(self._vtk_obj.GetPriority, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int)
        C++: void Allocate(const IdType sz, const IdType ext=1000)
        Allocate initial space for priority queue.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def delete_id(self, *args):
        """
        V.delete_id(int) -> float
        C++: double DeleteId(IdType id)
        Delete entry in queue with specified id. Returns priority value
        associated with that id; or VTK_DOUBLE_MAX if not in queue.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteId, *args)
        return ret

    def insert(self, *args):
        """
        V.insert(float, int)
        C++: void Insert(double priority, IdType id)
        Insert id with priority specified. The id is generally an index
        like a point id or cell id.
        """
        ret = self._wrap_call(self._vtk_obj.Insert, *args)
        return ret

    def peek(self, *args):
        """
        V.peek(int, float) -> int
        C++: IdType Peek(IdType location, double &priority)
        V.peek(int) -> int
        C++: IdType Peek(IdType location=0)
        Peek into the queue without actually removing anything. Returns
        the id and the priority.
        """
        ret = self._wrap_call(self._vtk_obj.Peek, *args)
        return ret

    def pop(self, *args):
        """
        V.pop(int, float) -> int
        C++: IdType Pop(IdType location, double &priority)
        V.pop(int) -> int
        C++: IdType Pop(IdType location=0)
        Removes item at specified location from tree; then reorders and
        balances tree. The location == 0 is the root of the tree. If
        queue is exhausted, then a value < 0 is returned. (Note: the
        location is not the same as deleting an id; id is mapped to
        location.)
        """
        ret = self._wrap_call(self._vtk_obj.Pop, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Empty the queue but without releasing memory. This avoids the
        overhead of memory allocation/deletion.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PriorityQueue, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PriorityQueue properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit PriorityQueue properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PriorityQueue properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

