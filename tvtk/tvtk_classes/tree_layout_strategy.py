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


class TreeLayoutStrategy(GraphLayoutStrategy):
    """
    TreeLayoutStrategy - hierarchical layout
    
    Superclass: GraphLayoutStrategy
    
    Assigns points to the nodes of a tree in either a standard or radial
    layout. The standard layout places each level on a horizontal line,
    while the radial layout places each level on a concentric circle. You
    may specify the sweep angle of the tree which constrains the tree to
    be contained within a wedge. Also, you may indicate the log scale of
    the tree, which diminishes the length of arcs at lower levels of the
    tree. Values near zero give a large proportion of the space to the
    tree levels near the root, while values near one give nearly equal
    proportions of space to all tree levels.
    
    The user may also specify an array to use to indicate the distance
    from the root, either vertically (for standard layout) or radially
    (for radial layout).  You specify this with set_distance_array_name().
    
    If the input is not a tree but a general graph, this strategy first
    extracts a tree from the graph using a breadth-first search starting
    at vertex ID 0.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeLayoutStrategy, obj, update, **traits)
    
    reverse_edges = tvtk_base.false_bool_trait(help=\
        """
        If set and the input is not a tree but a general graph, the
        filter will reverse the edges on the graph before extracting a
        tree using breadth first search.
        """
    )
    def _reverse_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseEdges,
                        self.reverse_edges_)

    radial = tvtk_base.false_bool_trait(help=\
        """
        If set, the tree is laid out with levels on concentric circles
        around the root. If unset (default), the tree is laid out with
        levels on horizontal lines.
        """
    )
    def _radial_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadial,
                        self.radial_)

    distance_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get/Set the array to use to determine the distance from the root.
        """
    )
    def _distance_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceArrayName,
                        self.distance_array_name)

    leaf_spacing = traits.Trait(0.9, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The spacing of leaves.  Levels near one evenly space leaves with
        no gaps between subtrees.  Levels near zero creates large gaps
        between subtrees.
        """
    )
    def _leaf_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeafSpacing,
                        self.leaf_spacing)

    rotation = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The amount of counter-clockwise rotation to apply after the
        layout.
        """
    )
    def _rotation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotation,
                        self.rotation)

    log_spacing_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The spacing of tree levels. Levels near zero give more space to
        levels near the root, while levels near one (the default) create
        evenly-spaced levels. Levels above one give more space to levels
        near the leaves.
        """
    )
    def _log_spacing_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLogSpacingValue,
                        self.log_spacing_value)

    angle = traits.Trait(90.0, traits.Range(0.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        The sweep angle of the tree. For a standard tree layout, this
        should be between 0 and 180. For a radial tree layout, this can
        be between 0 and 360.
        """
    )
    def _angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngle,
                        self.angle)

    _updateable_traits_ = \
    (('angle', 'GetAngle'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('edge_weight_field',
    'GetEdgeWeightField'), ('debug', 'GetDebug'), ('log_spacing_value',
    'GetLogSpacingValue'), ('distance_array_name',
    'GetDistanceArrayName'), ('radial', 'GetRadial'), ('reference_count',
    'GetReferenceCount'), ('rotation', 'GetRotation'), ('weight_edges',
    'GetWeightEdges'), ('leaf_spacing', 'GetLeafSpacing'),
    ('reverse_edges', 'GetReverseEdges'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'radial', 'reverse_edges',
    'angle', 'distance_array_name', 'edge_weight_field', 'leaf_spacing',
    'log_spacing_value', 'rotation', 'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['radial', 'reverse_edges'], [], ['angle',
            'distance_array_name', 'edge_weight_field', 'leaf_spacing',
            'log_spacing_value', 'rotation', 'weight_edges']),
            title='Edit TreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

