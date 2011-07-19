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


class IdList(Object):
    """
    IdList - list of point or cell ids
    
    Superclass: Object
    
    IdList is used to represent and pass data id's between objects.
    IdList may represent any type of integer id, but usually
    represents point and cell ids.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIdList, obj, update, **traits)
    
    number_of_ids = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the number of ids for this object to hold. Does an
        allocation as well as setting the number of ids.
        """
    )
    def _number_of_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfIds,
                        self.number_of_ids)

    def get_id(self, *args):
        """
        V.get_id(int) -> int
        C++: IdType GetId(const IdType i)
        Return the id at location i.
        """
        ret = self._wrap_call(self._vtk_obj.GetId, *args)
        return ret

    def set_id(self, *args):
        """
        V.set_id(int, int)
        C++: void SetId(const IdType i, const IdType vtkid)
        Set the id at location i. Doesn't do range checking so it's a bit
        faster than insert_id. Make sure you use set_number_of_ids() to
        allocate memory prior to using set_id().
        """
        ret = self._wrap_call(self._vtk_obj.SetId, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: int Allocate(const IdType sz, const int strategy=0)"""
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(IdList)
        C++: void DeepCopy(IdList *ids)
        Copy an id list by explicitly copying the internal array.
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def delete_id(self, *args):
        """
        V.delete_id(int)
        C++: void DeleteId(IdType vtkid)
        Delete specified id from list. Will remove all occurrences of id
        in list.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteId, *args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()"""
        ret = self._vtk_obj.Initialize()
        return ret
        

    def insert_id(self, *args):
        """
        V.insert_id(int, int)
        C++: void InsertId(const IdType i, const IdType vtkid)
        Set the id at location i. Does range checking and allocates
        memory as necessary.
        """
        ret = self._wrap_call(self._vtk_obj.InsertId, *args)
        return ret

    def insert_next_id(self, *args):
        """
        V.insert_next_id(int) -> int
        C++: IdType InsertNextId(const IdType vtkid)
        Add the id specified to the end of the list. Range checking is
        performed.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextId, *args)
        return ret

    def insert_unique_id(self, *args):
        """
        V.insert_unique_id(int) -> int
        C++: IdType InsertUniqueId(const IdType vtkid)
        If id is not already in list, insert it and return location in
        list. Otherwise return just location in list.
        """
        ret = self._wrap_call(self._vtk_obj.InsertUniqueId, *args)
        return ret

    def intersect_with(self, *args):
        """
        V.intersect_with(IdList)
        C++: void IntersectWith(IdList *otherIds)
        Intersect this list with another IdList. Updates current list
        according to result of intersection operation.
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.IntersectWith, *my_args)
        return ret

    def is_id(self, *args):
        """
        V.is_id(int) -> int
        C++: IdType IsId(IdType vtkid)
        Return -1 if id specified is not contained in the list; otherwise
        return the position in the list.
        """
        ret = self._wrap_call(self._vtk_obj.IsId, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reset to an empty state.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def squeeze(self):
        """
        V.squeeze()
        C++: void Squeeze()
        Free any unused memory.
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_ids', 'GetNumberOfIds'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_ids'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IdList, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit IdList properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['number_of_ids']),
            title='Edit IdList properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IdList properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
    def __len__(self):
        return self._vtk_obj.GetNumberOfIds()
    
    def __iter__(self):
        obj = self._vtk_obj
        n = obj.GetNumberOfIds()
        for i in xrange(n):
            yield obj.GetId(i)
    
    def _check_key(self, key, n):
        if type(key) != type(1):
            raise TypeError, "Only integers are valid keys."
        if key < 0:
            key =  n + key
        if key < 0 or key >= n:
            raise IndexError, "Index out of range."
        return key
    
    def __getitem__(self, key):
        obj = self._vtk_obj
        n = obj.GetNumberOfIds()
        key = self._check_key(key, n)
        return obj.GetId(key)
    
    def __setitem__(self, key, val):
        obj = self._vtk_obj
        n = obj.GetNumberOfIds()
        key = self._check_key(key, n)
        obj.SetId(key, val)
    
    def __repr__(self):
        obj = self._vtk_obj
        n = obj.GetNumberOfIds()
        if n <= 10:
            return repr([x for x in self])
        else:
            meth = obj.GetId
            return '[%s, ..., %s], length = %s'%(meth(0),
                                                 meth(n-1), n)
    
    def append(self, val):
        self._vtk_obj.InsertNextId(val)
        self.update_traits()
    
    def extend(self, arr):
        obj = self._vtk_obj
        for i in arr:
            obj.InsertNextId(i)
        self.update_traits()
    
    def from_array(self, arr):
        '''Set the value of the data array using the passed
        Numeric array or Python list.  This is implemented
        efficiently.
        '''
        array_handler.array2vtkIdList(arr, self._vtk_obj)
        self.update_traits()
    

