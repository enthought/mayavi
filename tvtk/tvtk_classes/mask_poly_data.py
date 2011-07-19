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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class MaskPolyData(PolyDataAlgorithm):
    """
    MaskPolyData - sample subset of input polygonal data cells
    
    Superclass: PolyDataAlgorithm
    
    MaskPolyData is a filter that sub-samples the cells of input
    polygonal data. The user specifies every nth item, with an initial
    offset to begin sampling.
    
    See Also:
    
    MaskPoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMaskPolyData, obj, update, **traits)
    
    on_ratio = traits.Trait(11, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Turn on every nth entity (cell).
        """
    )
    def _on_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnRatio,
                        self.on_ratio)

    offset = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Start with this entity (cell).
        """
    )
    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('on_ratio', 'GetOnRatio'), ('release_data_flag',
    'GetReleaseDataFlag'), ('offset', 'GetOffset'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('abort_execute',
    'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'offset', 'on_ratio', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MaskPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MaskPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['offset', 'on_ratio']),
            title='Edit MaskPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MaskPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

