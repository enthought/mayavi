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

from tvtk.tvtk_classes.label_hierarchy_iterator import LabelHierarchyIterator


class LabelHierarchyCompositeIterator(LabelHierarchyIterator):
    """
    LabelHierarchyCompositeIterator - Iterator over sub-iterators
    
    Superclass: LabelHierarchyIterator
    
    Iterates over child iterators in a round-robin order. Each iterator
    may have its own count, which is the number of times it is repeated
    until moving to the next iterator.
    
    For example, if you initialize the iterator with
    
    it->_add_iterator(_a, 1); it->_add_iterator(_b, 3);  The order of iterators
    will be A,B,B,B,A,B,B,B,...
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabelHierarchyCompositeIterator, obj, update, **traits)
    
    def add_iterator(self, *args):
        """
        V.add_iterator(LabelHierarchyIterator)
        C++: virtual void AddIterator(LabelHierarchyIterator *it)
        V.add_iterator(LabelHierarchyIterator, int)
        C++: virtual void AddIterator(LabelHierarchyIterator *it,
            int count)
        Adds a label iterator to this composite iterator. The second
        optional argument is the number of times to repeat the iterator
        before moving to the next one round-robin style. Default is 1.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddIterator, *my_args)
        return ret

    def clear_iterators(self):
        """
        V.clear_iterators()
        C++: virtual void ClearIterators()
        Remove all iterators from this composite iterator.
        """
        ret = self._vtk_obj.ClearIterators()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('all_bounds', 'GetAllBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'all_bounds'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabelHierarchyCompositeIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LabelHierarchyCompositeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['all_bounds']),
            title='Edit LabelHierarchyCompositeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabelHierarchyCompositeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

