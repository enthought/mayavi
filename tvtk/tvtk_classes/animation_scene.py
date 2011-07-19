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

from tvtk.tvtk_classes.animation_cue import AnimationCue


class AnimationScene(AnimationCue):
    """
    AnimationScene - the animation scene manager.
    
    Superclass: AnimationCue
    
    AnimationCue and AnimationScene provide the framework to
    support animations in VTK. AnimationCue represents an entity that
    changes/ animates with time, while AnimationScene represents scene
    or setup for the animation, which consists of individual cues or
    other scenes.
    
    A scene can be played in real time mode, or as a seqence of frames
    1/frame rate apart in time.
    
    See Also:
    
    AnimationCue
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAnimationScene, obj, update, **traits)
    
    animation_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Makes the state of the scene same as the given time.
        """
    )
    def _animation_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAnimationTime,
                        self.animation_time)

    play_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the play_mode for running/playing the animation scene. In
        the Sequence mode, all the frames are generated one after the
        other. The time reported to each Tick of the constituent cues
        (during Play) is incremented by 1/frame rate, irrespective of the
        current time. In the real_time mode, time indicates the instance
        in time.
        """
    )
    def _play_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlayMode,
                        self.play_mode)

    frame_rate = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the frame rate (in frames per second). This parameter
        affects only in the Sequence mode. The time interval indicated to
        each cue on every tick is progressed by 1/frame-rate seconds.
        """
    )
    def _frame_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrameRate,
                        self.frame_rate)

    loop = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Enable/Disable animation loop.
        """
    )
    def _loop_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLoop,
                        self.loop)

    def _get_number_of_cues(self):
        return self._vtk_obj.GetNumberOfCues()
    number_of_cues = traits.Property(_get_number_of_cues, help=\
        """
        Add/Remove an animation_cue to/from the Scene. It's an error to
        add a cue twice to the Scene.
        """
    )

    def add_cue(self, *args):
        """
        V.add_cue(AnimationCue)
        C++: void AddCue(AnimationCue *cue)
        Add/Remove an animation_cue to/from the Scene. It's an error to
        add a cue twice to the Scene.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddCue, *my_args)
        return ret

    def is_in_play(self):
        """
        V.is_in_play() -> int
        C++: int IsInPlay()
        Returns if the animation is being played.
        """
        ret = self._vtk_obj.IsInPlay()
        return ret
        

    def play(self):
        """
        V.play()
        C++: virtual void Play()
        Starts playing the animation scene. Fires a
        Command::StartEvent before play beings and
        Command::EndEvent after play ends.
        """
        ret = self._vtk_obj.Play()
        return ret
        

    def remove_all_cues(self):
        """
        V.remove_all_cues()
        C++: void RemoveAllCues()
        Add/Remove an animation_cue to/from the Scene. It's an error to
        add a cue twice to the Scene.
        """
        ret = self._vtk_obj.RemoveAllCues()
        return ret
        

    def remove_cue(self, *args):
        """
        V.remove_cue(AnimationCue)
        C++: void RemoveCue(AnimationCue *cue)
        Add/Remove an animation_cue to/from the Scene. It's an error to
        add a cue twice to the Scene.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveCue, *my_args)
        return ret

    def set_mode_to_real_time(self):
        """
        V.set_mode_to_real_time()
        C++: void SetModeToRealTime()
        Get/Set the play_mode for running/playing the animation scene. In
        the Sequence mode, all the frames are generated one after the
        other. The time reported to each Tick of the constituent cues
        (during Play) is incremented by 1/frame rate, irrespective of the
        current time. In the real_time mode, time indicates the instance
        in time.
        """
        ret = self._vtk_obj.SetModeToRealTime()
        return ret
        

    def set_mode_to_sequence(self):
        """
        V.set_mode_to_sequence()
        C++: void SetModeToSequence()
        Get/Set the play_mode for running/playing the animation scene. In
        the Sequence mode, all the frames are generated one after the
        other. The time reported to each Tick of the constituent cues
        (during Play) is incremented by 1/frame rate, irrespective of the
        current time. In the real_time mode, time indicates the instance
        in time.
        """
        ret = self._vtk_obj.SetModeToSequence()
        return ret
        

    def stop(self):
        """
        V.stop()
        C++: void Stop()
        Stops the animation scene that is running.
        """
        ret = self._vtk_obj.Stop()
        return ret
        

    _updateable_traits_ = \
    (('animation_time', 'GetAnimationTime'), ('debug', 'GetDebug'),
    ('end_time', 'GetEndTime'), ('frame_rate', 'GetFrameRate'),
    ('reference_count', 'GetReferenceCount'), ('play_mode',
    'GetPlayMode'), ('start_time', 'GetStartTime'), ('time_mode',
    'GetTimeMode'), ('loop', 'GetLoop'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'time_mode', 'animation_time',
    'end_time', 'frame_rate', 'loop', 'play_mode', 'start_time'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AnimationScene, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AnimationScene properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['time_mode'], ['animation_time', 'end_time',
            'frame_rate', 'loop', 'play_mode', 'start_time']),
            title='Edit AnimationScene properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AnimationScene properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

