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

from tvtk.tvtk_classes.composite_data_iterator import CompositeDataIterator


class HierarchicalBoxDataIterator(CompositeDataIterator):
    """
    HierarchicalBoxDataIterator - subclass of CompositeDataIterator
    
    Superclass: CompositeDataIterator
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHierarchicalBoxDataIterator, obj, update, **traits)
    
    def _get_current_index(self):
        return self._vtk_obj.GetCurrentIndex()
    current_index = traits.Property(_get_current_index, help=\
        """
        Returns the dataset index for the current data object. Valid only
        if the current data is a leaf node i.e. no a composite dataset.
        """
    )

    def _get_current_level(self):
        return self._vtk_obj.GetCurrentLevel()
    current_level = traits.Property(_get_current_level, help=\
        """
        Returns the level for the current dataset.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('traverse_sub_tree',
    'GetTraverseSubTree'), ('reference_count', 'GetReferenceCount'),
    ('visit_only_leaves', 'GetVisitOnlyLeaves'), ('skip_empty_nodes',
    'GetSkipEmptyNodes'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'skip_empty_nodes',
    'traverse_sub_tree', 'visit_only_leaves'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HierarchicalBoxDataIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HierarchicalBoxDataIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['skip_empty_nodes', 'traverse_sub_tree',
            'visit_only_leaves'], [], []),
            title='Edit HierarchicalBoxDataIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HierarchicalBoxDataIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

