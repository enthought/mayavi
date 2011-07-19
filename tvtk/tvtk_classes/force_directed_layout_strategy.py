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


class ForceDirectedLayoutStrategy(GraphLayoutStrategy):
    """
    ForceDirectedLayoutStrategy - a force directed graph layout
    algorithm
    
    Superclass: GraphLayoutStrategy
    
    Lays out a graph in 2d or 3d using a force-directed algorithm. The
    user may specify whether to layout the graph randomly initially, the
    bounds, the number of dimensions (2 or 3), and the cool-down rate.
    
    Thanks:
    
    Thanks to Brian Wylie for adding functionality for allowing this
    layout to be incremental.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkForceDirectedLayoutStrategy, obj, update, **traits)
    
    random_initial_points = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off use of random positions within the graph bounds as
        initial points.
        """
    )
    def _random_initial_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomInitialPoints,
                        self.random_initial_points_)

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

    three_dimensional_layout = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off layout of graph in three dimensions. If off, graph
        layout occurs in two dimensions. By default, three dimensional
        layout is off.
        """
    )
    def _three_dimensional_layout_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreeDimensionalLayout,
                        self.three_dimensional_layout_)

    random_seed = traits.Trait(123, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Seed the random number generator used to jitter point positions.
        This has a significant effect on their final positions when the
        layout is complete.
        """
    )
    def _random_seed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomSeed,
                        self.random_seed)

    iterations_per_layout = traits.Trait(50, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of iterations per layout. The only use for
        this ivar is for the application to do visualizations of the
        layout before it's complete. The default is '50' to match the
        default '_max_number_of_iterations'
        """
    )
    def _iterations_per_layout_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIterationsPerLayout,
                        self.iterations_per_layout)

    max_number_of_iterations = traits.Trait(50, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the maximum number of iterations to be used. The higher
        this number, the more iterations through the algorithm is
        possible, and thus, the more the graph gets modified. The default
        is '50' for no particular reason
        """
    )
    def _max_number_of_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxNumberOfIterations,
                        self.max_number_of_iterations)

    graph_bounds = traits.Array(shape=(6,), value=(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _graph_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphBounds,
                        self.graph_bounds)

    cool_down_rate = traits.Trait(10.0, traits.Range(0.01, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the Cool-down rate. The higher this number is, the longer
        it will take to "cool-down", and thus, the more the graph will be
        modified.
        """
    )
    def _cool_down_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoolDownRate,
                        self.cool_down_rate)

    initial_temperature = traits.Trait(10.0, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set the initial temperature.  If zero (the default) , the initial
        temperature will be computed automatically.
        """
    )
    def _initial_temperature_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInitialTemperature,
                        self.initial_temperature)

    _updateable_traits_ = \
    (('cool_down_rate', 'GetCoolDownRate'), ('three_dimensional_layout',
    'GetThreeDimensionalLayout'), ('random_seed', 'GetRandomSeed'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('edge_weight_field', 'GetEdgeWeightField'), ('iterations_per_layout',
    'GetIterationsPerLayout'), ('debug', 'GetDebug'), ('graph_bounds',
    'GetGraphBounds'), ('initial_temperature', 'GetInitialTemperature'),
    ('random_initial_points', 'GetRandomInitialPoints'),
    ('max_number_of_iterations', 'GetMaxNumberOfIterations'),
    ('reference_count', 'GetReferenceCount'),
    ('automatic_bounds_computation', 'GetAutomaticBoundsComputation'),
    ('weight_edges', 'GetWeightEdges'))
    
    _full_traitnames_list_ = \
    (['automatic_bounds_computation', 'debug', 'global_warning_display',
    'random_initial_points', 'three_dimensional_layout', 'cool_down_rate',
    'edge_weight_field', 'graph_bounds', 'initial_temperature',
    'iterations_per_layout', 'max_number_of_iterations', 'random_seed',
    'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ForceDirectedLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ForceDirectedLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic_bounds_computation',
            'random_initial_points', 'three_dimensional_layout'], [],
            ['cool_down_rate', 'edge_weight_field', 'graph_bounds',
            'initial_temperature', 'iterations_per_layout',
            'max_number_of_iterations', 'random_seed', 'weight_edges']),
            title='Edit ForceDirectedLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ForceDirectedLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

