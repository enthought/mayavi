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

from tvtk.tvtk_classes.streamer import Streamer


class StreamPoints(Streamer):
    """
    StreamPoints - generate points along streamer separated by
    constant time increment
    
    Superclass: Streamer
    
    StreamPoints is a filter that generates points along a streamer.
    The points are separated by a constant time increment. The resulting
    visual effect (especially when coupled with Glyph3D) is an
    indication of particle speed.
    
    See Also:
    
    Streamer StreamLine DashedStreamLine
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStreamPoints, obj, update, **traits)
    
    time_increment = traits.Trait(1.0, traits.Range(9.9999999999999995e-07, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the separation of points in terms of absolute time.
        """
    )
    def _time_increment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeIncrement,
                        self.time_increment)

    _updateable_traits_ = \
    (('time_increment', 'GetTimeIncrement'), ('vorticity',
    'GetVorticity'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('release_data_flag',
    'GetReleaseDataFlag'), ('integration_step_length',
    'GetIntegrationStepLength'), ('save_point_interval',
    'GetSavePointInterval'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('orientation_scalars',
    'GetOrientationScalars'), ('start_position', 'GetStartPosition'),
    ('speed_scalars', 'GetSpeedScalars'), ('number_of_threads',
    'GetNumberOfThreads'), ('epsilon', 'GetEpsilon'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('maximum_propagation_time', 'GetMaximumPropagationTime'),
    ('abort_execute', 'GetAbortExecute'), ('terminal_speed',
    'GetTerminalSpeed'), ('integration_direction',
    'GetIntegrationDirection'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'orientation_scalars', 'release_data_flag', 'speed_scalars',
    'vorticity', 'integration_direction', 'epsilon',
    'integration_step_length', 'maximum_propagation_time',
    'number_of_threads', 'progress_text', 'save_point_interval',
    'start_position', 'terminal_speed', 'time_increment'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StreamPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit StreamPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['orientation_scalars', 'speed_scalars', 'vorticity'],
            ['integration_direction'], ['epsilon', 'integration_step_length',
            'maximum_propagation_time', 'number_of_threads',
            'save_point_interval', 'start_position', 'terminal_speed',
            'time_increment']),
            title='Edit StreamPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StreamPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

