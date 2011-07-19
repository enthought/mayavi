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


class InformationIterator(Object):
    """
    InformationIterator - Iterates over keys of an information object
    
    Superclass: Object
    
    InformationIterator can be used to iterate over the keys of an
    information object. The corresponding values can then be directly
    obtained from the information object using the keys.
    
    See Also:
    
    Information InformationKey
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInformationIterator, obj, update, **traits)
    
    def _get_information(self):
        return wrap_vtk(self._vtk_obj.GetInformation())
    def _set_information(self, arg):
        old_val = self._get_information()
        self._wrap_call(self._vtk_obj.SetInformation,
                        deref_vtk(arg))
        self.trait_property_changed('information', old_val, arg)
    information = traits.Property(_get_information, _set_information, help=\
        """
        Set/Get the information to iterator over.
        """
    )

    def _get_current_key(self):
        return wrap_vtk(self._vtk_obj.GetCurrentKey())
    current_key = traits.Property(_get_current_key, help=\
        """
        Get the current item. Valid only when is_done_with_traversal()
        returns 1.
        """
    )

    def go_to_first_item(self):
        """
        V.go_to_first_item()
        C++: virtual void GoToFirstItem()
        Move the iterator to the beginning of the collection.
        """
        ret = self._vtk_obj.GoToFirstItem()
        return ret
        

    def go_to_next_item(self):
        """
        V.go_to_next_item()
        C++: virtual void GoToNextItem()
        Move the iterator to the next item in the collection.
        """
        ret = self._vtk_obj.GoToNextItem()
        return ret
        

    def init_traversal(self):
        """
        V.init_traversal()
        C++: void InitTraversal()
        Move the iterator to the beginning of the collection.
        """
        ret = self._vtk_obj.InitTraversal()
        return ret
        

    def is_done_with_traversal(self):
        """
        V.is_done_with_traversal() -> int
        C++: virtual int IsDoneWithTraversal()
        Test whether the iterator is currently pointing to a valid item.
        Returns 1 for yes, 0 for no.
        """
        ret = self._vtk_obj.IsDoneWithTraversal()
        return ret
        

    def set_information_weak(self, *args):
        """
        V.set_information_weak(Information)
        C++: void SetInformationWeak(Information *)
        Set the function to iterate over. The iterator will not hold a
        reference to the information object. Can be used to optimize
        certain places by avoiding garbage collection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInformationWeak, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InformationIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InformationIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit InformationIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InformationIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

