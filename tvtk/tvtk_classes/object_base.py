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

class ObjectBase(tvtk_base.TVTKBase):
    """
    ObjectBase - abstract base class for most VTK objects
    
    ObjectBase is the base class for all reference counted classes in
    the VTK. These classes include Command classes, InformationKey
    classes, and Object classes.
    
    ObjectBase performs reference counting: objects that are reference
    counted exist as long as another object uses them. Once the last
    reference to a reference counted object is removed, the object will
    spontaneously destruct.
    
    Constructor and destructor of the subclasses of ObjectBase should
    be protected, so that only New() and un_register() actually call them.
    Debug leaks can be used to see if there are any objects left with
    nonzero reference count.
    
    Caveats:
    
    Note: Objects of subclasses of ObjectBase should always be created
    with the New() method and deleted with the Delete() method. They
    cannot be allocated off the stack (i.e., automatic objects) because
    the constructor is a protected method.
    
    See also:
    
    Object Command InformationKey
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkObjectBase, obj, update, **traits)
    
    reference_count = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Sets the reference count. (This is very dangerous, use with
        care.)
        """
    )
    def _reference_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReferenceCount,
                        self.reference_count)

    def get_address_as_string(self, *args):
        """
        V.get_address_as_string(string) -> string
        C++: const char *GetAddressAsString()
        Get address of C++ object in format 'Addr=%p' after casting to
        the specified type.  You can get the same information from o.__this__."""
        ret = self._wrap_call(self._vtk_obj.GetAddressAsString, *args)
        return ret

    def _get_class_name(self):
        return self._vtk_obj.GetClassName()
    class_name = traits.Property(_get_class_name, help=\
        """
        Return the class name as a string. This method is defined in all
        subclasses of ObjectBase with the TypeMacro found in
        SetGet.h.
        """
    )

    def fast_delete(self):
        """
        V.fast_delete()
        C++: virtual void FastDelete()
        Delete a reference to this object.  This version will not invoke
        garbage collection and can potentially leak the object if it is
        part of a reference loop.  Use this method only when it is known
        that the object has another reference and would not be collected
        if a full garbage collection check were done.
        """
        ret = self._vtk_obj.FastDelete()
        return ret
        

    def is_a(self, *args):
        """
        V.is_a(string) -> int
        C++: virtual int IsA(const char *name)
        Return 1 if this class is the same type of (or a subclass of) the
        named class. Returns 0 otherwise. This method works in
        combination with TypeMacro found in SetGet.h.
        """
        ret = self._wrap_call(self._vtk_obj.IsA, *args)
        return ret

    def is_type_of(self, *args):
        """
        V.is_type_of(string) -> int
        C++: static int IsTypeOf(const char *name)
        Return 1 if this class type is the same type of (or a subclass
        of) the named class. Returns 0 otherwise. This method works in
        combination with TypeMacro found in SetGet.h.
        """
        ret = self._wrap_call(self._vtk_obj.IsTypeOf, *args)
        return ret

    def print_revisions(self):
        """
        V.print_revisions() -> string
        C++: const char *PrintRevisions()
        Prints the .cxx file CVS revisions of the classes in the
        object's inheritance chain."""
        ret = self._vtk_obj.PrintRevisions()
        return ret
        

    def register(self, *args):
        """
        V.register(ObjectBase)
        C++: virtual void Register(ObjectBase *o)
        Increase the reference count (mark as used by another object).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Register, *my_args)
        return ret

    def un_register(self, *args):
        """
        V.un_register(ObjectBase)
        C++: virtual void UnRegister(ObjectBase *o)
        Decrease the reference count (release by another object). This
        has the same effect as invoking Delete() (i.e., it reduces the
        reference count by 1).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UnRegister, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'),)
    
    _full_traitnames_list_ = \
    ([])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ObjectBase, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ObjectBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ObjectBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ObjectBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

