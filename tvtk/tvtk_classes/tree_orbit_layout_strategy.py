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


class TreeOrbitLayoutStrategy(GraphLayoutStrategy):
    """
    TreeOrbitLayoutStrategy - hierarchical orbital layout
    
    Superclass: GraphLayoutStrategy
    
    Assigns points to the nodes of a tree to an orbital layout. Each
    parent is orbited by its children, recursively.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeOrbitLayoutStrategy, obj, update, **traits)
    
    leaf_spacing = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The spacing of leaves.  Levels near one evenly space leaves with
        no gaps between subtrees.  Levels near zero creates large gaps
        between subtrees.
        """
    )
    def _leaf_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeafSpacing,
                        self.leaf_spacing)

    log_spacing_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The spacing of orbital levels. Levels near zero give more space
        to levels near the root, while levels near one (the default)
        create evenly-spaced levels. Levels above one give more space to
        levels near the leaves.
        """
    )
    def _log_spacing_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLogSpacingValue,
                        self.log_spacing_value)

    child_radius_factor = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        This is a magic number right now. Controls the radius of the
        child layout, all of this should be fixed at some point with a
        more logical layout. Defaults to .5 :)
        """
    )
    def _child_radius_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetChildRadiusFactor,
                        self.child_radius_factor)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('log_spacing_value', 'GetLogSpacingValue'),
    ('child_radius_factor', 'GetChildRadiusFactor'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('edge_weight_field', 'GetEdgeWeightField'), ('reference_count',
    'GetReferenceCount'), ('weight_edges', 'GetWeightEdges'),
    ('leaf_spacing', 'GetLeafSpacing'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'child_radius_factor',
    'edge_weight_field', 'leaf_spacing', 'log_spacing_value',
    'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeOrbitLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeOrbitLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['child_radius_factor', 'edge_weight_field',
            'leaf_spacing', 'log_spacing_value', 'weight_edges']),
            title='Edit TreeOrbitLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeOrbitLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

