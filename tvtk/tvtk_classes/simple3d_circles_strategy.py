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


class Simple3DCirclesStrategy(GraphLayoutStrategy):
    """
    Simple3DCirclesStrategy - places vertices on circles in 3d
    
    Superclass: GraphLayoutStrategy
    
    Places vertices on circles depending on the graph vertices hierarchy
    level. The source graph could be DirectedAcyclicGraph or
    DirectedGraph if marked_start_points array was added. The algorithm
    collects the standalone points, too and take them to a separated
    circle. If method is fixed_radius_method, the radius of the circles
    will be equal. If method is fixed_distance_method, the distance beetwen
    the points on circles will be equal.
    
    In first step initial points are searched. A point is initial, if its
    in degree equal zero and out degree is greater than zero (or marked
    by marked_start_vertices and out degree is greater than zero).
    Independent vertices (in and out degree equal zero) are collected
    separatelly. In second step the hierarchical level is generated for
    every vertex. In third step the hierarchical order is generated. If a
    vertex has no hierarchical level and it is not independent, the graph
    has loop so the algorithm exit with error message. Finally the
    vertices positions are calculated by the hierarchical order and by
    the vertices hierarchy levels.
    
    Thanks:
    
    Ferenc Nasztanovics, naszta
    
    aszta.hu, Budapest University of Technology and Economics, Department
    of Structural Mechanics
    
    References:
    
    in 3d rotation was used:
    http://en.citizendium.org/wiki/Rotation_matrix
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSimple3DCirclesStrategy, obj, update, **traits)
    
    auto_height = tvtk_base.false_bool_trait(help=\
        """
        Set or get auto height (Default: false). If auto_height is true,
        (r(i+1) - r(i-1))/Height will be smaller than tan(_minimum_radian).
        If you want equal distances and parallel circles, you should turn
        off auto_height.
        """
    )
    def _auto_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoHeight,
                        self.auto_height_)

    force_to_use_universal_start_points_finder = tvtk_base.false_bool_trait(help=\
        """
        Set or get force_to_use_universal_start_points_finder. If
        force_to_use_universal_start_points_finder is true, marked_start_vertices
        won't be used. In this case the input graph must be
        DirectedAcyclicGraph (Defualt: false).
        """
    )
    def _force_to_use_universal_start_points_finder_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceToUseUniversalStartPointsFinder,
                        self.force_to_use_universal_start_points_finder_)

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    direction = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set or get the normal vector of the circles plain. The height is
        growing in this direction. The direction must not be zero vector.
        The default vector is (0.0,0.0,1.0)
        """
    )
    def _direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirection,
                        self.direction)

    height = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set or get the vertical (local z) distance between the circles.
        If auto_height is on, this is the minimal height between the
        circle layers
        """
    )
    def _height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeight,
                        self.height)

    minimum_degree = traits.Float(30.0, enter_set=True, auto_set=False, help=\
        """
        Set or get minimum degree (used by auto height). There is no
        separated minimum degree, so minimum radian will be changed.
        """
    )
    def _minimum_degree_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumDegree,
                        self.minimum_degree)

    def _get_marked_start_vertices(self):
        return wrap_vtk(self._vtk_obj.GetMarkedStartVertices())
    def _set_marked_start_vertices(self, arg):
        old_val = self._get_marked_start_vertices()
        my_arg = deref_array([arg], [['vtkAbstractArray']])
        self._wrap_call(self._vtk_obj.SetMarkedStartVertices,
                        my_arg[0])
        self.trait_property_changed('marked_start_vertices', old_val, arg)
    marked_start_vertices = traits.Property(_get_marked_start_vertices, _set_marked_start_vertices, help=\
        """
        Set or get initial vertices. If marked_start_vertices is added,
        loop is accepted in the graph. (If all of the loop start vertices
        are marked in marked_start_vertices array.) marked_start_vertices
        size must be equal with the number of the vertices in the graph.
        Start vertices must be marked by marked_value. (E.g.: if
        marked_value=_3 and marked_start_points is { 0, 3, 5, 3 }, the start
        points ids will be {1,3}.) )
        """
    )

    def _get_hierarchical_order(self):
        return wrap_vtk(self._vtk_obj.GetHierarchicalOrder())
    def _set_hierarchical_order(self, arg):
        old_val = self._get_hierarchical_order()
        my_arg = deref_array([arg], [['vtkIdTypeArray']])
        self._wrap_call(self._vtk_obj.SetHierarchicalOrder,
                        my_arg[0])
        self.trait_property_changed('hierarchical_order', old_val, arg)
    hierarchical_order = traits.Property(_get_hierarchical_order, _set_hierarchical_order, help=\
        """
        Set or get hierarchical ordering of vertices (The array starts
        from the first vertex's id. All id must be greater or equal to
        zero!) If no hierarchical_order is defined,
        Simple3DCirclesStrategy will generate it automatically
        (default).
        """
    )

    radius = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        If Method is fixed_radius_method: Set or get the radius of the
        circles. If Method is fixed_distance_method: Set or get the
        distance of the points in the circle.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    minimum_radian = traits.Float(0.523598775598, enter_set=True, auto_set=False, help=\
        """
        Set or get minimum radian (used by auto height).
        """
    )
    def _minimum_radian_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumRadian,
                        self.minimum_radian)

    method = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set or get cicrle generating method
        (_fixed_radius_method/_fixed_distance_method). Default is
        fixed_radius_method.
        """
    )
    def _method_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMethod,
                        self.method)

    def _get_hierarchical_layers(self):
        return wrap_vtk(self._vtk_obj.GetHierarchicalLayers())
    def _set_hierarchical_layers(self, arg):
        old_val = self._get_hierarchical_layers()
        my_arg = deref_array([arg], [['vtkIntArray']])
        self._wrap_call(self._vtk_obj.SetHierarchicalLayers,
                        my_arg[0])
        self.trait_property_changed('hierarchical_layers', old_val, arg)
    hierarchical_layers = traits.Property(_get_hierarchical_layers, _set_hierarchical_layers, help=\
        """
        Set or get hierarchical layers id by vertices (An usual vertex's
        layer id is greater or equal to zero. If a vertex is standalone,
        its layer id is -2.) If no hierarchical_layers array is defined,
        Simple3DCirclesStrategy will generate it automatically
        (default).
        """
    )

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('direction', 'GetDirection'),
    ('force_to_use_universal_start_points_finder',
    'GetForceToUseUniversalStartPointsFinder'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('edge_weight_field',
    'GetEdgeWeightField'), ('minimum_degree', 'GetMinimumDegree'),
    ('height', 'GetHeight'), ('debug', 'GetDebug'), ('radius',
    'GetRadius'), ('reference_count', 'GetReferenceCount'),
    ('minimum_radian', 'GetMinimumRadian'), ('weight_edges',
    'GetWeightEdges'), ('auto_height', 'GetAutoHeight'), ('method',
    'GetMethod'))
    
    _full_traitnames_list_ = \
    (['auto_height', 'debug',
    'force_to_use_universal_start_points_finder',
    'global_warning_display', 'direction', 'edge_weight_field', 'height',
    'method', 'minimum_degree', 'minimum_radian', 'origin', 'radius',
    'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Simple3DCirclesStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Simple3DCirclesStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_height',
            'force_to_use_universal_start_points_finder'], [], ['direction',
            'edge_weight_field', 'height', 'method', 'minimum_degree',
            'minimum_radian', 'origin', 'radius', 'weight_edges']),
            title='Edit Simple3DCirclesStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Simple3DCirclesStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

