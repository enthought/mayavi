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


class TemporalPathLineFilter(PolyDataAlgorithm):
    """
    TemporalPathLineFilter - Generate a Polydata Pointset from any
    Dataset.
    
    Superclass: PolyDataAlgorithm
    
    TemporalPathLineFilter takes any dataset as input, it extracts the
    point locations of all cells over time to build up a polyline trail.
    The point number (index) is used as the 'key' if the points are
    randomly changing their respective order in the points list, then you
    should specify a scalar that represents the unique ID. This is
    intended to handle the output of a filter such as the
    temporal_stream_tracer.
    
    See Also:
    
    TemporalStreamTracer
    
    Thanks:
    
    John Bidiscombe of CSCS - Swiss National Supercomputing Centre for
    creating and contributing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalPathLineFilter, obj, update, **traits)
    
    max_track_length = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        If the Particles being traced animate for a long time, the trails
        or traces will become long and stringy. Setting the
        max_trace_time_length will limit how much of the trace is displayed.
        Tracks longer then the Max will disappear and the trace will
        apppear like a snake of fixed length which progresses as the
        particle moves
        """
    )
    def _max_track_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxTrackLength,
                        self.max_track_length)

    mask_points = traits.Int(200, enter_set=True, auto_set=False, help=\
        """
        Set the number of particles to track as a ratio of the input
        example: setting mask_points to 10 will track every 10th point
        """
    )
    def _mask_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaskPoints,
                        self.mask_points)

    scalar_array = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )
    def _scalar_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarArray,
                        self.scalar_array)

    max_step_distance = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _max_step_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxStepDistance,
                        self.max_step_distance)

    id_channel_array = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the name of a scalar array which will be used to fetch
        the index of each point. This is necessary only if the particles
        change position (Id order) on each time step. The Id can be used
        to identify particles at each step and hence track them properly.
        If this array is NULL, the global point ids are used.  If an Id
        array cannot otherwise be found, the point index is used as the
        ID.
        """
    )
    def _id_channel_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIdChannelArray,
                        self.id_channel_array)

    keep_dead_trails = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        When a particle 'disappears', the trail belonging to it is
        removed from the list. When this flag is enabled, dead trails
        will persist until the next time the list is cleared. Use
        carefully as it may cause excessive memory consumption if left on
        by mistake.
        """
    )
    def _keep_dead_trails_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeepDeadTrails,
                        self.keep_dead_trails)

    def flush(self):
        """
        V.flush()
        C++: void Flush()
        Flush will wipe any existing data so that traces can be restarted
        from whatever time step is next supplied.
        """
        ret = self._vtk_obj.Flush()
        return ret
        

    def set_selection(self, *args):
        """
        V.set_selection(DataSet)
        C++: void SetSelection(DataSet *input)
        Set a second input which is a selection. Particles with the same
        Id in the selection as the primary input will be chosen for
        pathlines Note that you must have the same id_channel_array in the
        selection as the input
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSelection, *my_args)
        return ret

    def set_selection_connection(self, *args):
        """
        V.set_selection_connection(AlgorithmOutput)
        C++: void SetSelectionConnection(AlgorithmOutput *algOutput)
        Set a second input which is a selection. Particles with the same
        Id in the selection as the primary input will be chosen for
        pathlines Note that you must have the same id_channel_array in the
        selection as the input
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSelectionConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('mask_points', 'GetMaskPoints'), ('max_step_distance',
    'GetMaxStepDistance'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('keep_dead_trails', 'GetKeepDeadTrails'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('id_channel_array', 'GetIdChannelArray'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('scalar_array', 'GetScalarArray'), ('max_track_length',
    'GetMaxTrackLength'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'id_channel_array', 'keep_dead_trails',
    'mask_points', 'max_step_distance', 'max_track_length',
    'progress_text', 'scalar_array'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalPathLineFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalPathLineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['id_channel_array', 'keep_dead_trails',
            'mask_points', 'max_step_distance', 'max_track_length',
            'scalar_array']),
            title='Edit TemporalPathLineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalPathLineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

