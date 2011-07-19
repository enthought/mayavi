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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class GraphLayoutFilter(PolyDataAlgorithm):
    """
    GraphLayoutFilter - nice layout of undirected graphs in 3d
    
    Superclass: PolyDataAlgorithm
    
    GraphLayoutFilter will reposition a network of nodes, connected by
    lines or polylines, into a more pleasing arrangement. The class
    implements a simple force-directed placement algorithm (Fruchterman &
    Reingold "Graph Drawing by Force-directed Placement"
    Software-Practice and Experience 21(11) 1991).
    
    The input to the filter is a PolyData representing the undirected
    graphs. A graph is represented by a set of polylines and/or lines.
    The output is also a PolyData, where the point positions have been
    modified. To use the filter, specify whether you wish the layout to
    occur in 2d or 3d; the bounds in which the graph should lie (note
    that you can just use automatic bounds computation); and modify the
    cool down rate (controls the final process of simulated annealing).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphLayoutFilter, obj, update, **traits)
    
    automatic_bounds_computation = tvtk_base.true_bool_trait(help=\
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
        
        """
    )
    def _three_dimensional_layout_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreeDimensionalLayout,
                        self.three_dimensional_layout_)

    max_number_of_iterations = traits.Trait(50, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the maximum number of iterations to be used. The higher
        this number, the more iterations through the algorithm is
        possible, and thus, the more the graph gets modified.
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

    _updateable_traits_ = \
    (('cool_down_rate', 'GetCoolDownRate'),
    ('automatic_bounds_computation', 'GetAutomaticBoundsComputation'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('progress_text', 'GetProgressText'), ('graph_bounds',
    'GetGraphBounds'), ('debug', 'GetDebug'), ('abort_execute',
    'GetAbortExecute'), ('max_number_of_iterations',
    'GetMaxNumberOfIterations'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('three_dimensional_layout',
    'GetThreeDimensionalLayout'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'automatic_bounds_computation', 'debug',
    'global_warning_display', 'release_data_flag',
    'three_dimensional_layout', 'cool_down_rate', 'graph_bounds',
    'max_number_of_iterations', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphLayoutFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphLayoutFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic_bounds_computation',
            'three_dimensional_layout'], [], ['cool_down_rate', 'graph_bounds',
            'max_number_of_iterations']),
            title='Edit GraphLayoutFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphLayoutFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

