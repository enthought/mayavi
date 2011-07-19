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


class EdgeLayoutStrategy(Object):
    """
    EdgeLayoutStrategy - abstract superclass for all edge layout
    strategies
    
    Superclass: Object
    
    All edge layouts should subclass from this class. 
    EdgeLayoutStrategy works as a plug-in to the EdgeLayout
    algorithm.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEdgeLayoutStrategy, obj, update, **traits)
    
    edge_weight_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the field to use for the edge weights.
        """
    )
    def _edge_weight_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeWeightArrayName,
                        self.edge_weight_array_name)

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        This method allows the layout strategy to do initialization of
        data structures or whatever else it might want to do.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def layout(self):
        """
        V.layout()
        C++: virtual void Layout()
        This is the layout method where the graph that was set in
        set_graph() is laid out.
        """
        ret = self._vtk_obj.Layout()
        return ret
        

    def set_graph(self, *args):
        """
        V.set_graph(Graph)
        C++: virtual void SetGraph(Graph *graph)
        Setting the graph for the layout strategy
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGraph, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('edge_weight_array_name', 'GetEdgeWeightArrayName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'edge_weight_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EdgeLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit EdgeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['edge_weight_array_name']),
            title='Edit EdgeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EdgeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

