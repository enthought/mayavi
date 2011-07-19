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


class Collection(Object):
    """
    Collection - create and manipulate unsorted lists of objects
    
    Superclass: Object
    
    Collection is a general object for creating and manipulating lists
    of objects. The lists are unsorted and allow duplicate entries.
    Collection also serves as a base class for lists of specific types
    of objects.
    
    See Also:
    
    ActorCollection AssemblyPaths DataSetCollection
    ImplicitFunctionCollection LightCollection
    PolyDataCollection RenderWindowCollection RendererCollection
    StructuredPointsCollection TransformCollection
    VolumeCollection
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCollection, obj, update, **traits)
    
    def get_item_as_object(self, *args):
        """
        V.get_item_as_object(int) -> Object
        C++: Object *GetItemAsObject(int i)
        Get the i'th item in the collection. NULL is returned if i is out
        of range
        """
        ret = self._wrap_call(self._vtk_obj.GetItemAsObject, *args)
        return wrap_vtk(ret)

    def _get_next_item_as_object(self):
        return wrap_vtk(self._vtk_obj.GetNextItemAsObject())
    next_item_as_object = traits.Property(_get_next_item_as_object, help=\
        """
        Get the next item in the collection. NULL is returned if the
        collection is exhausted.
        """
    )

    def _get_number_of_items(self):
        return self._vtk_obj.GetNumberOfItems()
    number_of_items = traits.Property(_get_number_of_items, help=\
        """
        Return the number of objects in the list.
        """
    )

    def add_item(self, *args):
        """
        V.add_item(Object)
        C++: void AddItem(Object *)
        Add an object to the list. Does not prevent duplicate entries.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddItem, *my_args)
        return ret

    def init_traversal(self, *args):
        """
        V.init_traversal()
        C++: void InitTraversal()
        V.init_traversal()
        C++: void InitTraversal(CollectionSimpleIterator &cookie)
        Initialize the traversal of the collection. This means the data
        pointer is set at the beginning of the list.
        """
        ret = self._wrap_call(self._vtk_obj.InitTraversal, *args)
        return ret

    def insert_item(self, *args):
        """
        V.insert_item(int, Object)
        C++: void InsertItem(int i, Object *)
        Insert item into the list after the i'th item. Does not prevent
        duplicate entries. If i < 0 the item is placed at the top of the
        list.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertItem, *my_args)
        return ret

    def is_item_present(self, *args):
        """
        V.is_item_present(Object) -> int
        C++: int IsItemPresent(Object *a)
        Search for an object and return location in list. If the return
        value is 0, the object was not found. If the object was found,
        the location is the return value-1.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsItemPresent, *my_args)
        return ret

    def new_iterator(self):
        """
        V.new_iterator() -> CollectionIterator
        C++: CollectionIterator *NewIterator()
        Get an iterator to traverse the objects in this collection.
        """
        ret = wrap_vtk(self._vtk_obj.NewIterator())
        return ret
        

    def remove_all_items(self):
        """
        V.remove_all_items()
        C++: void RemoveAllItems()
        Remove all objects from the list.
        """
        ret = self._vtk_obj.RemoveAllItems()
        return ret
        

    def remove_item(self, *args):
        """
        V.remove_item(int)
        C++: void RemoveItem(int i)
        V.remove_item(Object)
        C++: void RemoveItem(Object *)
        Remove the i'th item in the list. Be careful if using this
        function during traversal of the list using get_next_item_as_object
        (or get_next_item in derived class).  The list WILL be shortened if
        a valid index is given!  If this->Current is equal to the element
        being removed, have it point to then next element in the list.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveItem, *my_args)
        return ret

    def replace_item(self, *args):
        """
        V.replace_item(int, Object)
        C++: void ReplaceItem(int i, Object *)
        Replace the i'th item in the collection with a
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReplaceItem, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Collection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Collection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Collection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Collection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
    def __len__(self):
        return self._vtk_obj.GetNumberOfItems()
    
    def __iter__(self):
        self._vtk_obj.InitTraversal()
        return self
    
    def next(self):
        try:
            val = self._vtk_obj.GetNextItem()
        except AttributeError:
            val = self._vtk_obj.GetNextProp()
        if val is None:
            raise StopIteration
        return wrap_vtk(val)
    
    def __getitem__(self, key):
        obj = self._vtk_obj
        if type(key) != type(1):
            raise TypeError, "Only integers are valid keys."
        ni = obj.GetNumberOfItems()
        if key < 0:
            key =  ni + key
        ret = obj.GetItemAsObject(key)
        if ret is None:
            raise IndexError, "Index out of range."
        return wrap_vtk(ret)
    
    def __setitem__(self, key, val):
        obj = self._vtk_obj
        if type(key) != type(1):
            raise TypeError, "Only integers are valid key."
        ni = obj.GetNumberOfItems()
        if key < 0:
            key =  ni + key
        if key < 0 or key >= ni:
            raise IndexError, "Index out of range."
        obj.ReplaceItem(key, deref_vtk(val))
    
    def __delitem__(self, key):
        obj = self._vtk_obj
        if type(key) != type(1):
            raise TypeError, "Only integers are valid keys."
        ni = obj.GetNumberOfItems()
        if key < 0:
            key =  ni + key
        if key < 0 or key >= ni:
            raise IndexError, "Index out of range."
        obj.RemoveItem(key)
    
    def __repr__(self):
        return repr([repr(x) for x in self])
    
    def append(self, val):
        self._vtk_obj.AddItem(deref_vtk(val))
    
    def extend(self, arr):
        obj = self._vtk_obj
        for i in arr:
            obj.AddItem(deref_vtk(i))

