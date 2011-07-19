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


class SortDataArray(Object):
    """
    SortDataArray - Provides several methods for sorting vtk arrays.
    
    Superclass: Object
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSortDataArray, obj, update, **traits)
    
    def sort(self, *args):
        """
        V.sort(IdList)
        C++: static void Sort(IdList *keys)
        V.sort(AbstractArray)
        C++: static void Sort(AbstractArray *keys)
        V.sort(IdList, IdList)
        C++: static void Sort(IdList *keys, IdList *values)
        V.sort(IdList, AbstractArray)
        C++: static void Sort(IdList *keys, AbstractArray *values)
        V.sort(AbstractArray, IdList)
        C++: static void Sort(AbstractArray *keys, IdList *values)
        V.sort(AbstractArray, AbstractArray)
        C++: static void Sort(AbstractArray *keys,
            AbstractArray *values)
        Sorts the given array.
        """
        my_args = deref_array(args, [['vtkIdList'], ['vtkAbstractArray'], ('vtkIdList', 'vtkIdList'), ('vtkIdList', 'vtkAbstractArray'), ('vtkAbstractArray', 'vtkIdList'), ('vtkAbstractArray', 'vtkAbstractArray')])
        ret = self._wrap_call(self._vtk_obj.Sort, *my_args)
        return ret

    def sort_array_by_component(self, *args):
        """
        V.sort_array_by_component(AbstractArray, int)
        C++: static void SortArrayByComponent(AbstractArray *arr,
            int k)
        Sorts the given data array using the specified component as a
        key. Think of the array as a 2-D grid with each tuple
        representing a row. Tuples are swapped until the k-th column of
        the grid is monotonically increasing. Where two tuples have the
        same value for the k-th component, their order in the final
        result is unspecified.
        """
        my_args = deref_array(args, [('vtkAbstractArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.SortArrayByComponent, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SortDataArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SortDataArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit SortDataArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SortDataArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

