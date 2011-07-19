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

from tvtk.tvtk_classes.graph_layout_strategy import GraphLayoutStrategy


class RandomLayoutStrategy(GraphLayoutStrategy):
    """
    RandomLayoutStrategy - randomly places vertices in 2 or 3
    dimensions
    
    Superclass: GraphLayoutStrategy
    
    Assigns points to the vertices of a graph randomly within a bounded
    range.
    
    .SECION Thanks Thanks to Brian Wylie from Sandia National
    Laboratories for adding incremental layout capabilities.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRandomLayoutStrategy, obj, update, **traits)
    
    automatic_bounds_computation = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off automatic graph bounds calculation. If this boolean
        is off, then the manually specified graph_bounds is used. If on,
        then the input's bounds us used as the graph bounds.
        """
    )
    def _automatic_bounds_computation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticBoundsComputation,
                        self.automatic_bounds_computation_)

    three_dimensional_layout = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off layout of graph in three dimensions. If off, graph
        layout occurs in two dimensions. By default, three dimensional
        layout is on.
        """
    )
    def _three_dimensional_layout_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreeDimensionalLayout,
                        self.three_dimensional_layout_)

    random_seed = traits.Trait(123, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Seed the random number generator used to compute point positions.
        This has a significant effect on their final positions when the
        layout is complete.
        """
    )
    def _random_seed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomSeed,
                        self.random_seed)

    graph_bounds = traits.Array(shape=(6,), value=(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _graph_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphBounds,
                        self.graph_bounds)

    _updateable_traits_ = \
    (('automatic_bounds_computation', 'GetAutomaticBoundsComputation'),
    ('random_seed', 'GetRandomSeed'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('edge_weight_field',
    'GetEdgeWeightField'), ('graph_bounds', 'GetGraphBounds'), ('debug',
    'GetDebug'), ('reference_count', 'GetReferenceCount'),
    ('weight_edges', 'GetWeightEdges'), ('three_dimensional_layout',
    'GetThreeDimensionalLayout'))
    
    _full_traitnames_list_ = \
    (['automatic_bounds_computation', 'debug', 'global_warning_display',
    'three_dimensional_layout', 'edge_weight_field', 'graph_bounds',
    'random_seed', 'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RandomLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RandomLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic_bounds_computation',
            'three_dimensional_layout'], [], ['edge_weight_field', 'graph_bounds',
            'random_seed', 'weight_edges']),
            title='Edit RandomLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RandomLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

