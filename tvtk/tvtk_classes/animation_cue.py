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


class AnimationCue(Object):
    """
    AnimationCue - a seqin an animation.
    
    Superclass: Object
    
    AnimationCue and AnimationScene provide the framework to
    support animations in VTK. AnimationCue represents an entity that
    changes/ animates with time, while AnimationScene represents scene
    or setup for the animation, which consists on individual cues or
    other scenes.
    
    A cue has three states: UNINITIALIZED, ACTIVE and INACTIVE.
    UNINITIALIZED represents an point in time before the start time of
    the cue. The cue is in ACTIVE state at a point in time between start
    time and end time for the cue. While, beyond the end time, it is in
    INACTIVE state. When the cue enters the ACTIVE state,
    start_animation_cue_event is fired. This event may be handled to
    initialize the entity to be animated. When the cue leaves the ACTIVE
    state, end_animation_cue_event is fired, which can be handled to cleanup
    after having run the animation. For every request to render during
    the ACTIVE state, animation_cue_tick_event is fired, which must be
    handled to perform the actual animation.
    
    See Also:
    
    AnimationScene
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAnimationCue, obj, update, **traits)
    
    time_mode = traits.Trait('relative',
    tvtk_base.TraitRevPrefixMap({'relative': 1, 'normalized': 0}), help=\
        """
        Get/Set the time mode. In Normalized mode, the start and end
        times of the cue are normalized [0,1] with respect to the start
        and end times of the container scene. In Relative mode the start
        and end time of the cue are specified in offset seconds relative
        to the start time of the container scene.
        """
    )
    def _time_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeMode,
                        self.time_mode_)

    end_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the End time for this cue. When the current time is >
        end_time, the Cue is in INACTIVE state. Whenever the cue leaves an
        ACTIVE state to enter INACTIVE state, the end_event is triggered.
        The End time is in seconds relative to the start of the container
        Scene (when in Relative time mode) or is normalized over the span
        of the container Scene (when in Normalized time mode).
        """
    )
    def _end_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndTime,
                        self.end_time)

    start_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the Start time for this cue. When the current time is >=
        start_time, the Cue is in ACTIVE state. if Current time i <
        start_time, the Cue is in UNINITIALIZED state. Whenever the cue
        enters the ACTIVE state from an INACTIVE state, it triggers the
        start_event. The Start time is in seconds relative to the start of
        the container Scene (when in Relative time mode) or is normalized
        over the span of the container Scene (when in Normalized time
        mode).
        """
    )
    def _start_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartTime,
                        self.start_time)

    def _get_animation_time(self):
        return self._vtk_obj.GetAnimationTime()
    animation_time = traits.Property(_get_animation_time, help=\
        """
        This is valid only in a animation_cue_tick_event handler. Before
        firing the event the animation cue sets the animation_time to the
        time of the tick.
        """
    )

    def _get_clock_time(self):
        return self._vtk_obj.GetClockTime()
    clock_time = traits.Property(_get_clock_time, help=\
        """
        This is valid only in a animation_cue_tick_event handler. Before
        firing the event the animation cue sets the clock_time to the time
        of the tick. clock_time is directly the time from the animation
        scene neither normalized nor offsetted to the start of the scene.
        """
    )

    def _get_delta_time(self):
        return self._vtk_obj.GetDeltaTime()
    delta_time = traits.Property(_get_delta_time, help=\
        """
        This is valid only in a animation_cue_tick_event handler. Before
        firing the event the animation cue sets the delta_time to the
        difference in time between the current tick and the last tick.
        """
    )

    def finalize(self):
        """
        V.finalize()
        C++: virtual void Finalize()
        Called when the scene reaches the end. If the cue state is ACTIVE
        when this method is called, this will trigger a
        end_animation_cue_event.
        """
        ret = self._vtk_obj.Finalize()
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Called when the playing of the scene begins. This will set the
        Cue to UNINITIALIZED state.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def tick(self, *args):
        """
        V.tick(float, float, float)
        C++: virtual void Tick(double currenttime, double deltatime,
            double clocktime)
        Indicates a tick or point in time in the animation. Triggers a
        Tick event if currenttime >= start_time and currenttime <=
        end_time. Whenever the state of the cue changes, either start_event
        or end_event is triggerred depending upon whether the cue entered
        Active state or quit active state respectively. The current time
        is relative to the start of the container Scene (when in Relative
        time mode) or is normalized over the span of the container Scene
        (when in Normalized time mode). deltatime is the time since last
        call to Tick. deltatime also can be in seconds relative to the
        start of the container Scene or normalized depending upon the
        cue's Time mode. clocktime is the time from the scene i.e. it
        does not depend on the time mode for the cue. For the first call
        to Tick after a call to Initialize(), the deltatime is 0;
        """
        ret = self._wrap_call(self._vtk_obj.Tick, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('end_time', 'GetEndTime'),
    ('reference_count', 'GetReferenceCount'), ('start_time',
    'GetStartTime'), ('time_mode', 'GetTimeMode'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'time_mode', 'end_time',
    'start_time'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AnimationCue, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AnimationCue properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['time_mode'], ['end_time', 'start_time']),
            title='Edit AnimationCue properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AnimationCue properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

