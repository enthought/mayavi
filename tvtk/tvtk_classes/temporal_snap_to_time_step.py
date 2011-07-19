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

from tvtk.tvtk_classes.temporal_data_set_algorithm import TemporalDataSetAlgorithm


class TemporalSnapToTimeStep(TemporalDataSetAlgorithm):
    """
    TemporalSnapToTimeStep - modify the time range/steps of temporal
    data
    
    Superclass: TemporalDataSetAlgorithm
    
    TemporalSnapToTimeStep  modify the time range or time steps of the
    data without changing the data itself. The data is not resampled by
    this filter, only the information accompanying the data is modified.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalSnapToTimeStep, obj, update, **traits)
    
    snap_mode = traits.Trait('nearest',
    tvtk_base.TraitRevPrefixMap({'nearest': 0, 'next_below_or_equal': 1, 'next_above_or_equal': 2}), help=\
        """
        
        """
    )
    def _snap_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSnapMode,
                        self.snap_mode_)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('snap_mode', 'GetSnapMode'),
    ('abort_execute', 'GetAbortExecute'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'snap_mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalSnapToTimeStep, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalSnapToTimeStep properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['snap_mode'], []),
            title='Edit TemporalSnapToTimeStep properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalSnapToTimeStep properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

