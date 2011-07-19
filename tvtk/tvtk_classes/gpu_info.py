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


class GPUInfo(Object):
    """
    GPUInfo - Stores GPU VRAM information.
    
    Superclass: Object
    
    GPUInfo stores information about GPU Video RAM. An host can have
    several GPUs. The values are set by GPUInfoList.
    
    See Also:
    
    GPUInfoList DirectXGPUInfoList CoreGraphicsGPUInfoList
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGPUInfo, obj, update, **traits)
    
    dedicated_system_memory = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get dedicated system memory in bytes. Initial value is 0.
        This is slow memory. If it is not null, this value should be
        taken into account only if there is no dedicated_video_memory and
        shared_system_memory should be ignored.
        """
    )
    def _dedicated_system_memory_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDedicatedSystemMemory,
                        self.dedicated_system_memory)

    dedicated_video_memory = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get dedicated video memory in bytes. Initial value is 0.
        Usually the fastest one. If it is not null, it should be take
        into account first and dedicated_system_memory or
        shared_system_memory should be ignored.
        """
    )
    def _dedicated_video_memory_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDedicatedVideoMemory,
                        self.dedicated_video_memory)

    shared_system_memory = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get shared system memory in bytes. Initial value is 0.
        Slowest memory. This value should be taken into account only if
        there is neither dedicated_video_memory nor dedicated_system_memory.
        """
    )
    def _shared_system_memory_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSharedSystemMemory,
                        self.shared_system_memory)

    _updateable_traits_ = \
    (('dedicated_video_memory', 'GetDedicatedVideoMemory'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('dedicated_system_memory', 'GetDedicatedSystemMemory'),
    ('shared_system_memory', 'GetSharedSystemMemory'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'dedicated_system_memory',
    'dedicated_video_memory', 'shared_system_memory'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GPUInfo, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GPUInfo properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['dedicated_system_memory',
            'dedicated_video_memory', 'shared_system_memory']),
            title='Edit GPUInfo properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GPUInfo properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

