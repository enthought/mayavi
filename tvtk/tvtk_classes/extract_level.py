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

from tvtk.tvtk_classes.hierarchical_box_data_set_algorithm import HierarchicalBoxDataSetAlgorithm


class ExtractLevel(HierarchicalBoxDataSetAlgorithm):
    """
    ExtractLevel - extract levels between min and max from a
    
    Superclass: HierarchicalBoxDataSetAlgorithm
    
    ExtractLevel filter extracts the levels between (and including)
    the user specified min and max levels.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractLevel, obj, update, **traits)
    
    def add_level(self, *args):
        """
        V.add_level(int)
        C++: void AddLevel(unsigned int level)
        Select the levels that should be extracted. All other levels will
        have no datasets in them.
        """
        ret = self._wrap_call(self._vtk_obj.AddLevel, *args)
        return ret

    def remove_all_levels(self):
        """
        V.remove_all_levels()
        C++: void RemoveAllLevels()
        Select the levels that should be extracted. All other levels will
        have no datasets in them.
        """
        ret = self._vtk_obj.RemoveAllLevels()
        return ret
        

    def remove_level(self, *args):
        """
        V.remove_level(int)
        C++: void RemoveLevel(unsigned int level)
        Select the levels that should be extracted. All other levels will
        have no datasets in them.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveLevel, *args)
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
            return super(ExtractLevel, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractLevel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ExtractLevel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractLevel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

