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


class ConeLayoutStrategy(GraphLayoutStrategy):
    """
    ConeLayoutStrategy - produce a cone-tree layout for a forest
    
    Superclass: GraphLayoutStrategy
    
    ConeLayoutStrategy positions the nodes of a tree(forest) in 3d
    space based on the cone-tree approach first described by Robertson,
    Mackinlay and Card in Proc. CHI'91.  This implementation incorporates
    refinements to the layout developed by Carriere and Kazman, and by
    Auber.
    
    The input graph must be a forest (i.e. a set of trees, or a single
    tree); in the case of a forest, the input will be converted to a
    single tree by introducing a new root node, and connecting each root
    in the input forest to the meta-root. The tree is then laid out,
    after which the meta-root is removed.
    
    The cones are positioned so that children lie in planes parallel to
    the X-Y plane, with the axis of cones parallel to Z, and with Z
    coordinate increasing with distance of nodes from the root.
    
    Thanks:
    
    Thanks to David Duke from the University of Leeds for providing this
    implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkConeLayoutStrategy, obj, update, **traits)
    
    compression = tvtk_base.false_bool_trait(help=\
        """
        Determine if layout should be compressed, i.e. the layout puts
        children closer together, possibly allowing sub-trees to overlap.
         This is useful if the tree is actually the spanning tree of a
        graph.  For "real" trees, non-compressed layout is best, and is
        the default.
        """
    )
    def _compression_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompression,
                        self.compression_)

    spacing = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the spacing parameter that affects space between layers of
        the tree.  If compression is on, Spacing is the actual distance
        between layers.  If compression is off, actual distance also
        includes a factor of the compactness and maximum cone radius.
        """
    )
    def _spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacing,
                        self.spacing)

    compactness = traits.Float(0.75, enter_set=True, auto_set=False, help=\
        """
        Determine the compactness, the ratio between the average width of
        a cone in the tree, and the height of the cone.  The default
        setting is 0.75 which (empirically) seems reasonable, but this
        will need adapting depending on the data.
        """
    )
    def _compactness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompactness,
                        self.compactness)

    _updateable_traits_ = \
    (('compression', 'GetCompression'), ('edge_weight_field',
    'GetEdgeWeightField'), ('spacing', 'GetSpacing'), ('debug',
    'GetDebug'), ('compactness', 'GetCompactness'), ('reference_count',
    'GetReferenceCount'), ('weight_edges', 'GetWeightEdges'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['compression', 'debug', 'global_warning_display', 'compactness',
    'edge_weight_field', 'spacing', 'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ConeLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ConeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['compression'], [], ['compactness',
            'edge_weight_field', 'spacing', 'weight_edges']),
            title='Edit ConeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ConeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

