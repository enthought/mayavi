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

from tvtk.tvtk_classes.streaming_demand_driven_pipeline import StreamingDemandDrivenPipeline


class CachedStreamingDemandDrivenPipeline(StreamingDemandDrivenPipeline):
    """
    CachedStreamingDemandDrivenPipeline -
    
    Superclass: StreamingDemandDrivenPipeline
    
    CachedStreamingDemandDrivenPipeline
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCachedStreamingDemandDrivenPipeline, obj, update, **traits)
    
    cache_size = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        This is the maximum number of images that can be retained in
        memory. it defaults to 10.
        """
    )
    def _cache_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCacheSize,
                        self.cache_size)

    _updateable_traits_ = \
    (('cache_size', 'GetCacheSize'), ('reference_count',
    'GetReferenceCount'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'cache_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CachedStreamingDemandDrivenPipeline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CachedStreamingDemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['cache_size']),
            title='Edit CachedStreamingDemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CachedStreamingDemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

