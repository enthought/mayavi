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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class MultiBlockMergeFilter(MultiBlockDataSetAlgorithm):
    """
    MultiBlockMergeFilter - merges multiblock inputs into a single
    multiblock output
    
    Superclass: MultiBlockDataSetAlgorithm
    
    MultiBlockMergeFilter is an M to 1 filter similar to
    MultiBlockDataGroupFilter. However where as that class creates N
    groups in the output for N inputs, this creates 1 group in the output
    with N datasets inside it. In actuality if the inputs have M blocks,
    this will produce M blocks, each of which has N datasets. Inside the
    merged group, the i'th data set comes from the i'th data set in the
    i'th input.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMultiBlockMergeFilter, obj, update, **traits)
    
    def add_input(self, *args):
        """
        V.add_input(DataObject)
        C++: void AddInput(DataObject *)
        V.add_input(int, DataObject)
        C++: void AddInput(int, DataObject *)
        Add an input of this algorithm.  Note that these methods support
        old-style pipeline connections.  When writing new code you should
        use the more general Algorithm::AddInputConnection().  See
        set_input() for details.
        """
        old_val = self._get_input()
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInput, *my_args)
        self.trait_property_changed('input', old_val, self._get_input())
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MultiBlockMergeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MultiBlockMergeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit MultiBlockMergeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MultiBlockMergeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

