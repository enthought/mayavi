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

from tvtk.tvtk_classes.piecewise_function_algorithm import PiecewiseFunctionAlgorithm


class PiecewiseFunctionShiftScale(PiecewiseFunctionAlgorithm):
    """
    PiecewiseFunctionShiftScale -
    
    Superclass: PiecewiseFunctionAlgorithm
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPiecewiseFunctionShiftScale, obj, update, **traits)
    
    value_shift = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _value_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValueShift,
                        self.value_shift)

    position_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _position_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPositionScale,
                        self.position_scale)

    value_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _value_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValueScale,
                        self.value_scale)

    position_shift = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _position_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPositionShift,
                        self.position_shift)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('value_scale', 'GetValueScale'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('position_scale', 'GetPositionScale'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('value_shift',
    'GetValueShift'), ('position_shift', 'GetPositionShift'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'position_scale', 'position_shift',
    'progress_text', 'value_scale', 'value_shift'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PiecewiseFunctionShiftScale, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PiecewiseFunctionShiftScale properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['position_scale', 'position_shift',
            'value_scale', 'value_shift']),
            title='Edit PiecewiseFunctionShiftScale properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PiecewiseFunctionShiftScale properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

