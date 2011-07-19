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


class CosmicTreeLayoutStrategy(GraphLayoutStrategy):
    """
    CosmicTreeLayoutStrategy - tree layout strategy reminiscent of
    astronomical systems
    
    Superclass: GraphLayoutStrategy
    
    This layout strategy takes an input tree and places all the children
    of a node into a containing circle. The placement is such that each
    child placed can be represented with a circle tangent to the
    containing circle and (usually) 2 other children. The interior of the
    circle is left empty so that graph edges drawn on top of the tree
    will not obfuscate the tree. However, when one child is much larger
    than all the others, it may encroach on the center of the containing
    circle; that's OK, because it's large enough not to be obscured by
    edges drawn atop it.
    
    Thanks:
    
    Thanks to the galaxy and David Thompson hierarchically nested inside
    it for inspiring this layout strategy.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCosmicTreeLayoutStrategy, obj, update, **traits)
    
    size_leaf_nodes_only = tvtk_base.true_bool_trait(help=\
        """
        Should node size specifications be obeyed at leaf nodes only or
        (with scaling as required to meet constraints) at every node in
        the tree? This defaults to true, so that leaf nodes are scaled
        according to the size specification provided, and the parent node
        sizes are calculated by the algorithm.
        """
    )
    def _size_leaf_nodes_only_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSizeLeafNodesOnly,
                        self.size_leaf_nodes_only_)

    layout_root = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        What is the top-most tree node to lay out? This node will become
        the largest containing circle in the layout. Use this in
        combination with set_layout_depth to retrieve the layout of a
        subtree of interest for rendering. Setting layout_root to a
        negative number signals that the root node of the tree should be
        used as the root node of the layout. This defaults to -1.
        """
    )
    def _layout_root_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLayoutRoot,
                        self.layout_root)

    node_size_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the array to be used for sizing nodes. If this is set to an
        empty string or NULL (the default), then all leaf nodes (or all
        nodes, when size_leaf_nodes_only is false) will be assigned a unit
        size.
        """
    )
    def _node_size_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNodeSizeArrayName,
                        self.node_size_array_name)

    layout_depth = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        How many levels of the tree should be laid out? For large trees,
        you may wish to set the root and maximum depth in order to
        retrieve the layout for the visible portion of the tree. When
        this value is zero or negative, all nodes below and including the
        layout_root will be presented. This defaults to 0.
        """
    )
    def _layout_depth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLayoutDepth,
                        self.layout_depth)

    _updateable_traits_ = \
    (('layout_depth', 'GetLayoutDepth'), ('debug', 'GetDebug'),
    ('node_size_array_name', 'GetNodeSizeArrayName'), ('layout_root',
    'GetLayoutRoot'), ('edge_weight_field', 'GetEdgeWeightField'),
    ('size_leaf_nodes_only', 'GetSizeLeafNodesOnly'), ('reference_count',
    'GetReferenceCount'), ('weight_edges', 'GetWeightEdges'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'size_leaf_nodes_only',
    'edge_weight_field', 'layout_depth', 'layout_root',
    'node_size_array_name', 'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CosmicTreeLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CosmicTreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['size_leaf_nodes_only'], [], ['edge_weight_field',
            'layout_depth', 'layout_root', 'node_size_array_name',
            'weight_edges']),
            title='Edit CosmicTreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CosmicTreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

