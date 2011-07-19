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


class GPUInfoList(Object):
    """
    GPUInfoList - Stores the list of GPUs VRAM information.
    
    Superclass: Object
    
    GPUInfoList stores a list of GPUInfo. An host can have several
    GPUs. It creates and sets the list by probing the host with system
    calls. This an abstract class. Concrete classes are OS specific.
    
    See Also:
    
    GPUInfo DirectXGPUInfoList CoreGraphicsGPUInfoList
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGPUInfoList, obj, update, **traits)
    
    def get_gpu_info(self, *args):
        """
        V.get_gpu_info(int) -> GPUInfo
        C++: virtual GPUInfo *GetGPUInfo(int i)
        Return information about GPU i.
        \pre probed: is_probed()
        \pre valid_index: i>=0 && i<_get_number_of_gp_us()
        \post result_exists: result!=0
        """
        ret = self._wrap_call(self._vtk_obj.GetGPUInfo, *args)
        return wrap_vtk(ret)

    def _get_number_of_gp_us(self):
        return self._vtk_obj.GetNumberOfGPUs()
    number_of_gp_us = traits.Property(_get_number_of_gp_us, help=\
        """
        Return the number of GPUs.
        \pre probed: is_probed()
        """
    )

    def is_probed(self):
        """
        V.is_probed() -> bool
        C++: virtual bool IsProbed()
        Tells if the operating system has been probed. Initial value is
        false.
        """
        ret = self._vtk_obj.IsProbed()
        return ret
        

    def probe(self):
        """
        V.probe()
        C++: virtual void Probe()
        Build the list of InfoGPU if not done yet. Default
        implementation created an empty list. Useful if there is no
        implementation available for a given architecture yet.
        \post probed: is_probed()
        """
        ret = self._vtk_obj.Probe()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GPUInfoList, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GPUInfoList properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GPUInfoList properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GPUInfoList properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

