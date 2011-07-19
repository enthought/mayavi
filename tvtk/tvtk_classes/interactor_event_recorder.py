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

from tvtk.tvtk_classes.interactor_observer import InteractorObserver


class InteractorEventRecorder(InteractorObserver):
    """
    InteractorEventRecorder - record and play VTK events passing
    through a RenderWindowInteractor
    
    Superclass: InteractorObserver
    
    InteractorEventRecorder records all VTK events invoked from a
    RenderWindowInteractor. The events are recorded to a file.
    InteractorEventRecorder can also be used to play those events back
    and invoke them on an RenderWindowInteractor. (Note: the events
    can also be played back from a file or string.)
    
    The format of the event file is simple. It is:
     event_name X Y ctrl shift keycode repeat_count key_sym The format also
    allows "#" comments.
    
    See Also:
    
    InteractorObserver Callback
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorEventRecorder, obj, update, **traits)
    
    read_from_input_string = tvtk_base.false_bool_trait(help=\
        """
        Enable reading from an input_string as compared to the default
        behavior, which is to read from a file.
        """
    )
    def _read_from_input_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadFromInputString,
                        self.read_from_input_string_)

    input_string = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the string to read from.
        """
    )
    def _input_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputString,
                        self.input_string)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the name of a file events should be written to/from.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def play(self):
        """
        V.play()
        C++: void Play()
        Invoke this method to begin playing events from the current
        position. The events will be played back from the filename
        indicated.
        """
        ret = self._vtk_obj.Play()
        return ret
        

    def record(self):
        """
        V.record()
        C++: void Record()
        Invoke this method to begin recording events. The events will be
        recorded to the filename indicated.
        """
        ret = self._vtk_obj.Record()
        return ret
        

    def rewind(self):
        """
        V.rewind()
        C++: void Rewind()
        Rewind to the beginning of the file.
        """
        ret = self._vtk_obj.Rewind()
        return ret
        

    def stop(self):
        """
        V.stop()
        C++: void Stop()
        Invoke this method to stop recording/playing events.
        """
        ret = self._vtk_obj.Stop()
        return ret
        

    _updateable_traits_ = \
    (('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('enabled', 'GetEnabled'), ('debug', 'GetDebug'),
    ('read_from_input_string', 'GetReadFromInputString'), ('priority',
    'GetPriority'), ('reference_count', 'GetReferenceCount'),
    ('input_string', 'GetInputString'), ('key_press_activation',
    'GetKeyPressActivation'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'read_from_input_string', 'file_name',
    'input_string', 'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorEventRecorder, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorEventRecorder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation',
            'read_from_input_string'], [], ['file_name', 'input_string',
            'key_press_activation_value', 'priority']),
            title='Edit InteractorEventRecorder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorEventRecorder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
    priority = traits.Trait(1.0, traits.Float, traits.Range(0.0, 1.0))
    def _priority_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPriority,
                        self.priority)
    priority.help =             """
        Set/Get the priority at which events are processed. This is used when
        multiple interactor observers are used simultaneously. The default value
        is 0.0 (lowest priority.) Note that when multiple interactor observer
        have the same priority, then the last observer added will process the
        event first. (Note: once the set_interactor() method has been called,
        changing the priority does not effect event processing. You will have
        to set_interactor(_null), change priority, and then set_interactor(iren)
        to have the priority take effect.)
        """

