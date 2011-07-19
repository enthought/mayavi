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

from tvtk.tvtk_classes.graph_algorithm import GraphAlgorithm


class GraphLayout(GraphAlgorithm):
    """
    GraphLayout - layout a graph in 2 or 3 dimensions
    
    Superclass: GraphAlgorithm
    
    This class is a shell for many graph layout strategies which may be
    set using the set_layout_strategy() function.  The layout strategies do
    the actual work.
    
    .SECION Thanks Thanks to Brian Wylie from Sandia National
    Laboratories for adding incremental layout capabilities.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphLayout, obj, update, **traits)
    
    use_transform = tvtk_base.false_bool_trait(help=\
        """
        Whether to use the specified transform after layout.
        """
    )
    def _use_transform_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseTransform,
                        self.use_transform_)

    def _get_layout_strategy(self):
        return wrap_vtk(self._vtk_obj.GetLayoutStrategy())
    def _set_layout_strategy(self, arg):
        old_val = self._get_layout_strategy()
        self._wrap_call(self._vtk_obj.SetLayoutStrategy,
                        deref_vtk(arg))
        self.trait_property_changed('layout_strategy', old_val, arg)
    layout_strategy = traits.Property(_get_layout_strategy, _set_layout_strategy, help=\
        """
        The layout strategy to use during graph layout.
        """
    )

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Transform the graph vertices after the layout.
        """
    )

    z_range = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the ZRange for the output data. If the initial layout is
        planar (i.e. all z coordinates are zero), the coordinates will be
        evenly spaced from 0.0 to ZRange. The default is zero, which has
        no effect.
        """
    )
    def _z_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZRange,
                        self.z_range)

    def is_layout_complete(self):
        """
        V.is_layout_complete() -> int
        C++: virtual int IsLayoutComplete()
        Ask the layout algorithm if the layout is complete
        """
        ret = self._vtk_obj.IsLayoutComplete()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('use_transform',
    'GetUseTransform'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('z_range', 'GetZRange'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_transform', 'progress_text', 'z_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphLayout, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_transform'], [], ['z_range']),
            title='Edit GraphLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

