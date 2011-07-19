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

from tvtk.tvtk_classes.render_view import RenderView


class TreeAreaView(RenderView):
    """
    TreeAreaView - Accepts a graph and a hierarchy - currently
    
    Superclass: RenderView
    
    Takes a graph and a hierarchy (currently a tree) and lays out the
    graph vertices based on their categorization within the hierarchy.
    
    .SEE ALSO GraphLayoutView
    
    Thanks:
    
    Thanks to Jason Shepherd for implementing this class
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeAreaView, obj, update, **traits)
    
    area_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether to show area labels.  Default is off.
        """
    )
    def _area_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaLabelVisibility,
                        self.area_label_visibility_)

    color_edges = tvtk_base.false_bool_trait(help=\
        """
        Whether to color edges.  Default is off.
        """
    )
    def _color_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorEdges,
                        self.color_edges_)

    color_areas = tvtk_base.true_bool_trait(help=\
        """
        Whether to color vertices.  Default is off.
        """
    )
    def _color_areas_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorAreas,
                        self.color_areas_)

    edge_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether to show edge labels.  Default is off.
        """
    )
    def _edge_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLabelVisibility,
                        self.edge_label_visibility_)

    use_rectangular_coordinates = tvtk_base.false_bool_trait(help=\
        """
        Whether the area represents radial or rectangular coordinates.
        """
    )
    def _use_rectangular_coordinates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseRectangularCoordinates,
                        self.use_rectangular_coordinates_)

    edge_color_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for coloring edges.  Default is "color".
        """
    )
    def _edge_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeColorArrayName,
                        self.edge_color_array_name)

    edge_label_font_size = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The size of the font used for edge labeling
        """
    )
    def _edge_label_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLabelFontSize,
                        self.edge_label_font_size)

    area_size_array_name = traits.String(r"size", enter_set=True, auto_set=False, help=\
        """
        The array to use for area sizes. Default is "size".
        """
    )
    def _area_size_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaSizeArrayName,
                        self.area_size_array_name)

    area_label_font_size = traits.Int(12, enter_set=True, auto_set=False, help=\
        """
        The size of the font used for area labeling
        """
    )
    def _area_label_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaLabelFontSize,
                        self.area_label_font_size)

    area_label_array_name = traits.Trait('id', None, traits.String('id', enter_set=True, auto_set=False), help=\
        """
        The array to use for area labeling.  Default is "label".
        """
    )
    def _area_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaLabelArrayName,
                        self.area_label_array_name)

    def _get_layout_strategy(self):
        return wrap_vtk(self._vtk_obj.GetLayoutStrategy())
    def _set_layout_strategy(self, arg):
        old_val = self._get_layout_strategy()
        self._wrap_call(self._vtk_obj.SetLayoutStrategy,
                        deref_vtk(arg))
        self.trait_property_changed('layout_strategy', old_val, arg)
    layout_strategy = traits.Property(_get_layout_strategy, _set_layout_strategy, help=\
        """
        The layout strategy for producing spatial regions for the tree.
        """
    )

    area_color_array_name = traits.String(r"level", enter_set=True, auto_set=False, help=\
        """
        The array to use for coloring vertices.  Default is "color".
        """
    )
    def _area_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaColorArrayName,
                        self.area_color_array_name)

    edge_label_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for edge labeling.  Default is "label".
        """
    )
    def _edge_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLabelArrayName,
                        self.edge_label_array_name)

    bundling_strength = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the bundling strength.
        """
    )
    def _bundling_strength_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBundlingStrength,
                        self.bundling_strength)

    edge_scalar_bar_visibility = traits.Bool(False, help=\
        """
        Visibility of scalar bar actor for edges.
        """
    )
    def _edge_scalar_bar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeScalarBarVisibility,
                        self.edge_scalar_bar_visibility)

    area_hover_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the array whose value appears when the mouse hovers
        over a rectangle in the treemap. This must be a string array.
        """
    )
    def _area_hover_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaHoverArrayName,
                        self.area_hover_array_name)

    shrink_percentage = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set the region shrink percentage between 0.0 and 1.0.
        """
    )
    def _shrink_percentage_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShrinkPercentage,
                        self.shrink_percentage)

    label_priority_array_name = traits.String(r"Priority", enter_set=True, auto_set=False, help=\
        """
        The array to use for area labeling priority. Default is
        "_graph_vertex_degree".
        """
    )
    def _label_priority_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelPriorityArrayName,
                        self.label_priority_array_name)

    def set_edge_color_to_spline_fraction(self):
        """
        V.set_edge_color_to_spline_fraction()
        C++: void SetEdgeColorToSplineFraction()
        Set the color to be the spline fraction
        """
        ret = self._vtk_obj.SetEdgeColorToSplineFraction()
        return ret
        

    def set_graph_from_input(self, *args):
        """
        V.set_graph_from_input(Graph) -> DataRepresentation
        C++: DataRepresentation *SetGraphFromInput(Graph *input)
        Set the tree and graph representations to the appropriate input
        ports.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGraphFromInput, *my_args)
        return wrap_vtk(ret)

    def set_graph_from_input_connection(self, *args):
        """
        V.set_graph_from_input_connection(AlgorithmOutput)
            -> DataRepresentation
        C++: DataRepresentation *SetGraphFromInputConnection(
            AlgorithmOutput *conn)
        Set the tree and graph representations to the appropriate input
        ports.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGraphFromInputConnection, *my_args)
        return wrap_vtk(ret)

    def set_tree_from_input(self, *args):
        """
        V.set_tree_from_input(Tree) -> DataRepresentation
        C++: DataRepresentation *SetTreeFromInput(Tree *input)
        Set the tree and graph representations to the appropriate input
        ports.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTreeFromInput, *my_args)
        return wrap_vtk(ret)

    def set_tree_from_input_connection(self, *args):
        """
        V.set_tree_from_input_connection(AlgorithmOutput)
            -> DataRepresentation
        C++: DataRepresentation *SetTreeFromInputConnection(
            AlgorithmOutput *conn)
        Set the tree and graph representations to the appropriate input
        ports.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTreeFromInputConnection, *my_args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('edge_label_array_name', 'GetEdgeLabelArrayName'),
    ('render_on_mouse_move', 'GetRenderOnMouseMove'), ('interaction_mode',
    'GetInteractionMode'), ('label_render_mode', 'GetLabelRenderMode'),
    ('edge_scalar_bar_visibility', 'GetEdgeScalarBarVisibility'),
    ('selection_mode', 'GetSelectionMode'), ('bundling_strength',
    'GetBundlingStrength'), ('area_label_font_size',
    'GetAreaLabelFontSize'), ('display_hover_text',
    'GetDisplayHoverText'), ('edge_label_visibility',
    'GetEdgeLabelVisibility'), ('edge_color_array_name',
    'GetEdgeColorArrayName'), ('label_placement_mode',
    'GetLabelPlacementMode'), ('shrink_percentage',
    'GetShrinkPercentage'), ('area_hover_array_name',
    'GetAreaHoverArrayName'), ('area_label_visibility',
    'GetAreaLabelVisibility'), ('reference_count', 'GetReferenceCount'),
    ('area_label_array_name', 'GetAreaLabelArrayName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('edge_label_font_size', 'GetEdgeLabelFontSize'),
    ('area_size_array_name', 'GetAreaSizeArrayName'),
    ('label_priority_array_name', 'GetLabelPriorityArrayName'),
    ('use_rectangular_coordinates', 'GetUseRectangularCoordinates'),
    ('color_edges', 'GetColorEdges'), ('color_areas', 'GetColorAreas'),
    ('icon_size', 'GetIconSize'), ('area_color_array_name',
    'GetAreaColorArrayName'))
    
    _full_traitnames_list_ = \
    (['area_label_visibility', 'color_areas', 'color_edges', 'debug',
    'display_hover_text', 'edge_label_visibility',
    'global_warning_display', 'render_on_mouse_move',
    'use_rectangular_coordinates', 'interaction_mode',
    'label_placement_mode', 'label_render_mode', 'selection_mode',
    'area_color_array_name', 'area_hover_array_name',
    'area_label_array_name', 'area_label_font_size',
    'area_size_array_name', 'bundling_strength', 'edge_color_array_name',
    'edge_label_array_name', 'edge_label_font_size',
    'edge_scalar_bar_visibility', 'icon_size',
    'label_priority_array_name', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeAreaView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeAreaView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['area_label_visibility', 'color_areas', 'color_edges',
            'display_hover_text', 'edge_label_visibility', 'render_on_mouse_move',
            'use_rectangular_coordinates'], ['interaction_mode',
            'label_placement_mode', 'label_render_mode', 'selection_mode'],
            ['area_color_array_name', 'area_hover_array_name',
            'area_label_array_name', 'area_label_font_size',
            'area_size_array_name', 'bundling_strength', 'edge_color_array_name',
            'edge_label_array_name', 'edge_label_font_size',
            'edge_scalar_bar_visibility', 'icon_size',
            'label_priority_array_name', 'shrink_percentage']),
            title='Edit TreeAreaView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeAreaView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

