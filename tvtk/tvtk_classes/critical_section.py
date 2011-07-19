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


class CriticalSection(Object):
    """
    CriticalSection - Critical section locking class
    
    Superclass: Object
    
    CriticalSection allows the locking of variables which are accessed
    through different threads.  This header file also defines
    SimpleCriticalSection which is not a subclass of Object. The
    API is identical to that of MutexLock, and the behavior is
    identical as well, except on Windows 9x/NT platforms. The only
    difference on these platforms is that MutexLock is more flexible,
    in that it works across processes as well as across threads, but also
    costs more, in that it evokes a 600-cycle x86 ring transition. The
    CriticalSection provides a higher-performance equivalent (on
    Windows) but won't work across processes. Since it is unclear how, in
    vtk, an object at the vtk level can be shared across processes in the
    first place, one should use CriticalSection unless one has a very
    good reason to use MutexLock. If higher-performance equivalents
    for non-Windows platforms (Irix, sun_os, etc) are discovered, they
    should replace the implementations in this class
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCriticalSection, obj, update, **traits)
    
    def lock(self):
        """
        V.lock()
        C++: void Lock()
        Lock the CriticalSection
        """
        ret = self._vtk_obj.Lock()
        return ret
        

    def unlock(self):
        """
        V.unlock()
        C++: void Unlock()
        Unlock the CriticalSection
        """
        ret = self._vtk_obj.Unlock()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CriticalSection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CriticalSection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit CriticalSection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CriticalSection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

