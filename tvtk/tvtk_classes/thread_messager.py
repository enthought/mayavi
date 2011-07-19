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


class ThreadMessager(Object):
    """
    ThreadMessager - A class for performing inter-thread messaging
    
    Superclass: Object
    
    Multithreader is a class that provides support for messaging
    between threads multithreaded using pthreads or Windows messaging.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThreadMessager, obj, update, **traits)
    
    def disable_wait_for_receiver(self):
        """
        V.disable_wait_for_receiver()
        C++: void DisableWaitForReceiver()
        pthreads only. If the wait is enabled, the thread who is to call
        wait_for_message() will block until a receiver thread is ready to
        receive.
        """
        ret = self._vtk_obj.DisableWaitForReceiver()
        return ret
        

    def enable_wait_for_receiver(self):
        """
        V.enable_wait_for_receiver()
        C++: void EnableWaitForReceiver()
        pthreads only. If the wait is enabled, the thread who is to call
        wait_for_message() will block until a receiver thread is ready to
        receive.
        """
        ret = self._vtk_obj.EnableWaitForReceiver()
        return ret
        

    def send_message(self):
        """
        V.send_message()
        C++: void SendMessage()
        @deprecated Replaced by ThreadMessager::SendWakeMessage() as
        of VTK 5.0.
        """
        ret = self._vtk_obj.SendMessage()
        return ret
        

    def send_wake_message(self):
        """
        V.send_wake_message()
        C++: void SendWakeMessage()
        Send a message to all threads who are waiting via
        wait_for_message().
        """
        ret = self._vtk_obj.SendWakeMessage()
        return ret
        

    def wait_for_message(self):
        """
        V.wait_for_message()
        C++: void WaitForMessage()
        Wait (block, non-busy) until another thread sends a message.
        """
        ret = self._vtk_obj.WaitForMessage()
        return ret
        

    def wait_for_receiver(self):
        """
        V.wait_for_receiver()
        C++: void WaitForReceiver()
        pthreads only. If wait is enable, this will block until one
        thread is ready to receive a message.
        """
        ret = self._vtk_obj.WaitForReceiver()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThreadMessager, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ThreadMessager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ThreadMessager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThreadMessager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

