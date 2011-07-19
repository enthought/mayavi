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


class GenericAttributeCollection(Object):
    """
    GenericAttributeCollection - a collection of attributes
    
    Superclass: Object
    
    GenericAttributeCollection is a class that collects attributes
    (represented by GenericAttribute).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericAttributeCollection, obj, update, **traits)
    
    active_attribute = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the scalar attribute to be processed. -1 means module.
        \pre not_empty: !_is_empty()
        \pre valid_attribute: attribute>=0 &&
            attribute<_get_number_of_attributes()
        \pre valid_component: component>=-1 &&
                    
        component<_get_attribute(attribute)->_get_number_of_components()
        \post is_set: get_active_attribute()==attribute &&
                      get_active_component()==component
        """
    )
    def _active_attribute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveAttribute,
                        self.active_attribute)

    def _get_active_component(self):
        return self._vtk_obj.GetActiveComponent()
    active_component = traits.Property(_get_active_component, help=\
        """
        Component of the active attribute to be processed. -1 means
        module.
        \pre not_empty: get_number_of_attributes()>_0
        \post valid_result: result>=-1 &&
             
        result<_get_attribute(_get_active_attribute())->_get_number_of_components()
        """
    )

    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Actual size of the data in kilobytes; only valid after the
        pipeline has updated. It is guaranteed to be greater than or
        equal to the memory required to represent the data.
        """
    )

    def get_attribute(self, *args):
        """
        V.get_attribute(int) -> GenericAttribute
        C++: GenericAttribute *GetAttribute(int i)
        Return a pointer to the ith instance of GenericAttribute.
        \pre not_empty: !_is_empty()
        \pre valid_i: i>=0 && i<_get_number_of_attributes()
        \post result_exists: result!=0
        """
        ret = self._wrap_call(self._vtk_obj.GetAttribute, *args)
        return wrap_vtk(ret)

    def get_attribute_index(self, *args):
        """
        V.get_attribute_index(int) -> int
        C++: int GetAttributeIndex(int i)
        Return the index of the first component of attribute `i' in an
        array of format attrib0comp0 attrib0comp1 ... attrib4comp0 ...
        \pre valid_i: i>=0 && i<_get_number_of_attributes()
        \pre is_point_centered:
            get_attribute(i)->_get_centering()==vtk_point_centered
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributeIndex, *args)
        return ret

    def _get_max_number_of_components(self):
        return self._vtk_obj.GetMaxNumberOfComponents()
    max_number_of_components = traits.Property(_get_max_number_of_components, help=\
        """
        Maximum number of components encountered among all attributes.
        \post positive_result: result>=0
        \post valid_result: result<=_get_number_of_components()
        """
    )

    def _get_number_of_attributes(self):
        return self._vtk_obj.GetNumberOfAttributes()
    number_of_attributes = traits.Property(_get_number_of_attributes, help=\
        """
        Return the number of attributes (e.g., instances of
        GenericAttribute) in the collection.
        \post positive_result: result>=0
        """
    )

    def _get_number_of_attributes_to_interpolate(self):
        return self._vtk_obj.GetNumberOfAttributesToInterpolate()
    number_of_attributes_to_interpolate = traits.Property(_get_number_of_attributes_to_interpolate, help=\
        """
        Number of attributes to interpolate.
        \pre not_empty: !_is_empty()
        \post positive_result: result>=0
        """
    )

    def _get_number_of_components(self):
        return self._vtk_obj.GetNumberOfComponents()
    number_of_components = traits.Property(_get_number_of_components, help=\
        """
        Return the number of components. This is the sum of all
        components found in all attributes.
        \post positive_result: result>=0
        """
    )

    def _get_number_of_point_centered_components(self):
        return self._vtk_obj.GetNumberOfPointCenteredComponents()
    number_of_point_centered_components = traits.Property(_get_number_of_point_centered_components, help=\
        """
        Return the number of components. This is the sum of all
        components found in all point centered attributes.
        \post positive_result: result>=0
        """
    )

    def deep_copy(self, *args):
        """
        V.deep_copy(GenericAttributeCollection)
        C++: void DeepCopy(GenericAttributeCollection *other)
        Copy, without reference counting, the other attribute array.
        \pre other_exists: other!=0
        \pre not_self: other!=this
        \post same_size:
            get_number_of_attributes()==other->_get_number_of_attributes()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def find_attribute(self, *args):
        """
        V.find_attribute(string) -> int
        C++: int FindAttribute(const char *name)
        Return the index of the attribute named `name'. Return the
        non-negative index if found. Return -1 otherwise.
        \pre name_exists: name!=0
        \post valid_result: (result==-1) || (result>=0) &&
            (result<=_get_number_of_attributes())
        """
        ret = self._wrap_call(self._vtk_obj.FindAttribute, *args)
        return ret

    def insert_attribute(self, *args):
        """
        V.insert_attribute(int, GenericAttribute)
        C++: void InsertAttribute(int i, GenericAttribute *a)
        Replace the attribute at index `i' by `a'.
        \pre not_empty: !_is_empty()
        \pre a_exists: a!=0
        \pre valid_i: i>=0 && i<_get_number_of_attributes()
        \post same_size: get_number_of_attributes()==old
            get_number_of_attributes()
        \post item_is_set: get_attribute(i)==a
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertAttribute, *my_args)
        return ret

    def insert_next_attribute(self, *args):
        """
        V.insert_next_attribute(GenericAttribute)
        C++: void InsertNextAttribute(GenericAttribute *a)
        Add the attribute `a' to the end of the collection.
        \pre a_exists: a!=0
        \post more_items: get_number_of_attributes()==old
            get_number_of_attributes()+_1
        \post a_is_set: get_attribute(_get_number_of_attributes()-_1)==a
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertNextAttribute, *my_args)
        return ret

    def is_empty(self):
        """
        V.is_empty() -> int
        C++: int IsEmpty()
        Indicate whether the collection contains any attributes.
        \post definition: result==(_get_number_of_attributes()==_0)
        """
        ret = self._vtk_obj.IsEmpty()
        return ret
        

    def remove_attribute(self, *args):
        """
        V.remove_attribute(int)
        C++: void RemoveAttribute(int i)
        Remove the attribute at `i'.
        \pre not_empty: !_is_empty()
        \pre valid_i: i>=0 && i<_get_number_of_attributes()
        \post fewer_items: get_number_of_attributes()==old
            get_number_of_attributes()-_1
        """
        ret = self._wrap_call(self._vtk_obj.RemoveAttribute, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Remove all attributes.
        \post is_empty: get_number_of_attributes()==_0
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def set_attributes_to_interpolate_to_all(self):
        """
        V.set_attributes_to_interpolate_to_all()
        C++: void SetAttributesToInterpolateToAll()
        Set the attributes to interpolate.
        \pre not_empty: !_is_empty()
        \pre positive_size: size>=0
        \pre valid_attributes: size>0 implies attributes!=0
        \pre valid_attributes_contents: attributes!=0 implies
                           
        !_has_attributes(size,attributes,_get_active_attribute())
        \post is_set: (_get_number_of_attributes_to_interpolate()==size)&&
                      (_get_attributes_to_interpolate()==attributes)
        """
        ret = self._vtk_obj.SetAttributesToInterpolateToAll()
        return ret
        

    def shallow_copy(self, *args):
        """
        V.shallow_copy(GenericAttributeCollection)
        C++: void ShallowCopy(GenericAttributeCollection *other)
        Copy, via reference counting, the other attribute array.
        \pre other_exists: other!=0
        \pre not_self: other!=this
        \post same_size:
            get_number_of_attributes()==other->_get_number_of_attributes()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('active_attribute', 'GetActiveAttribute'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'active_attribute'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericAttributeCollection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericAttributeCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['active_attribute']),
            title='Edit GenericAttributeCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericAttributeCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

