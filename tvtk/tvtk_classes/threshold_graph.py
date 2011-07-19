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

from tvtk.tvtk_classes.graph_algorithm import GraphAlgorithm


class ThresholdGraph(GraphAlgorithm):
    """
    ThresholdGraph - Returns a subgraph of a Graph.
    
    Superclass: GraphAlgorithm
    
    Requires input array, lower and upper threshold. This filter than
    extracts the subgraph based on these three parameters.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThresholdGraph, obj, update, **traits)
    
    upper_threshold = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set upper threshold. This would be the value against which
        edge or vertex data array value will be compared.
        """
    )
    def _upper_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpperThreshold,
                        self.upper_threshold)

    lower_threshold = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set lower threshold. This would be the value against which
        edge or vertex data array value will be compared.
        """
    )
    def _lower_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLowerThreshold,
                        self.lower_threshold)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('upper_threshold',
    'GetUpperThreshold'), ('lower_threshold', 'GetLowerThreshold'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'lower_threshold', 'progress_text',
    'upper_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThresholdGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ThresholdGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['lower_threshold', 'upper_threshold']),
            title='Edit ThresholdGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThresholdGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

