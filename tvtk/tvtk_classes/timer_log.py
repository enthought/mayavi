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


class TimerLog(Object):
    """
    TimerLog - Timer support and logging
    
    Superclass: Object
    
    TimerLog contains walltime and cputime measurements associated
    with a given event.  These results can be later analyzed when "dumping
    out" the table.
    
    In addition, TimerLog allows the user to simply get the current
    time, and to start/stop a simple timer separate from the timing table
    logging.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTimerLog, obj, update, **traits)
    
    logging = tvtk_base.true_bool_trait(help=\
        """
        This flag will turn loging of events off or on. By default,
        logging is on.
        """
    )
    def _logging_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLogging,
                        self.logging_)

    max_entries = traits.Int(100, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum number of entries allowed in the timer log
        """
    )
    def _max_entries_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxEntries,
                        self.max_entries)

    def _get_cpu_time(self):
        return self._vtk_obj.GetCPUTime()
    cpu_time = traits.Property(_get_cpu_time, help=\
        """
        Returns the CPU time for this process On Win32 platforms this
        actually returns wall time.
        """
    )

    def _get_current_time(self):
        return self._vtk_obj.GetCurrentTime()
    current_time = traits.Property(_get_current_time, help=\
        """
        @deprecated Replaced by TimerLog::GetUniversalTime() as of VTK
        5.0.
        """
    )

    def _get_elapsed_time(self):
        return self._vtk_obj.GetElapsedTime()
    elapsed_time = traits.Property(_get_elapsed_time, help=\
        """
        Returns the difference between start_time and end_time as a
        doubleing point value indicating the elapsed time in seconds.
        """
    )

    def get_event_indent(self, *args):
        """
        V.get_event_indent(int) -> int
        C++: static int GetEventIndent(int i)
        Programatic access to events.  Indexed from 0 to num-1.
        """
        ret = self._wrap_call(self._vtk_obj.GetEventIndent, *args)
        return ret

    def get_event_string(self, *args):
        """
        V.get_event_string(int) -> string
        C++: static const char *GetEventString(int i)
        Programatic access to events.  Indexed from 0 to num-1.
        """
        ret = self._wrap_call(self._vtk_obj.GetEventString, *args)
        return ret

    def get_event_wall_time(self, *args):
        """
        V.get_event_wall_time(int) -> float
        C++: static double GetEventWallTime(int i)
        Programatic access to events.  Indexed from 0 to num-1.
        """
        ret = self._wrap_call(self._vtk_obj.GetEventWallTime, *args)
        return ret

    def _get_number_of_events(self):
        return self._vtk_obj.GetNumberOfEvents()
    number_of_events = traits.Property(_get_number_of_events, help=\
        """
        Programatic access to events.  Indexed from 0 to num-1.
        """
    )

    def _get_universal_time(self):
        return self._vtk_obj.GetUniversalTime()
    universal_time = traits.Property(_get_universal_time, help=\
        """
        Returns the elapsed number of seconds since January 1, 1970. This
        is also called Universal Coordinated Time.
        """
    )

    def allocate_log(self):
        """
        V.allocate_log()
        C++: static void AllocateLog()
        Allocate timing table with max_entries elements.
        """
        ret = self._vtk_obj.AllocateLog()
        return ret
        

    def cleanup_log(self):
        """
        V.cleanup_log()
        C++: static void CleanupLog()
        Remove timer log.
        """
        ret = self._vtk_obj.CleanupLog()
        return ret
        

    def dump_log(self, *args):
        """
        V.dump_log(string)
        C++: static void DumpLog(const char *filename)
        Write the timing table out to a file.  Calculate some helpful
        statistics (deltas and  percentages) in the process.
        """
        ret = self._wrap_call(self._vtk_obj.DumpLog, *args)
        return ret

    def format_and_mark_event(self, *args):
        """
        V.format_and_mark_event(string)
        C++: static void FormatAndMarkEvent(const char *EventString, ...)
        Record a timing event.  The event is represented by a formatted
        string.
        """
        ret = self._wrap_call(self._vtk_obj.FormatAndMarkEvent, *args)
        return ret

    def mark_end_event(self, *args):
        """
        V.mark_end_event(string)
        C++: static void MarkEndEvent(const char *EventString)
        I want to time events, so I am creating this interface to mark
        events that have a start and an end.  These events can be,
        nested. The standard Dumplog ignores the indents.
        """
        ret = self._wrap_call(self._vtk_obj.MarkEndEvent, *args)
        return ret

    def mark_event(self, *args):
        """
        V.mark_event(string)
        C++: static void MarkEvent(const char *EventString)
        Record a timing event and capture wall time and cpu ticks.
        """
        ret = self._wrap_call(self._vtk_obj.MarkEvent, *args)
        return ret

    def mark_start_event(self, *args):
        """
        V.mark_start_event(string)
        C++: static void MarkStartEvent(const char *EventString)
        I want to time events, so I am creating this interface to mark
        events that have a start and an end.  These events can be,
        nested. The standard Dumplog ignores the indents.
        """
        ret = self._wrap_call(self._vtk_obj.MarkStartEvent, *args)
        return ret

    def reset_log(self):
        """
        V.reset_log()
        C++: static void ResetLog()
        Clear the timing table.  walltime and cputime will also be set to
        zero when the first new event is recorded.
        """
        ret = self._vtk_obj.ResetLog()
        return ret
        

    def start_timer(self):
        """
        V.start_timer()
        C++: void StartTimer()
        Set the start_time to the current time. Used with
        get_elapsed_time().
        """
        ret = self._vtk_obj.StartTimer()
        return ret
        

    def stop_timer(self):
        """
        V.stop_timer()
        C++: void StopTimer()
        Sets end_time to the current time. Used with get_elapsed_time().
        """
        ret = self._vtk_obj.StopTimer()
        return ret
        

    _updateable_traits_ = \
    (('max_entries', 'GetMaxEntries'), ('reference_count',
    'GetReferenceCount'), ('logging', 'GetLogging'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'logging', 'max_entries'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TimerLog, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TimerLog properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['logging'], [], ['max_entries']),
            title='Edit TimerLog properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TimerLog properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

