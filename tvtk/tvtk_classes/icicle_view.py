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

from tvtk.tvtk_classes.tree_area_view import TreeAreaView


class IcicleView(TreeAreaView):
    """
    IcicleView - Displays a tree in a stacked "icicle" view
    
    Superclass: TreeAreaView
    
    IcicleView shows a Tree in horizontal layers where each vertex
    in the tree is represented by a bar. Child sectors are below (or
    above) parent sectors, and may be colored and sized by various
    parameters.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIcicleView, obj, update, **traits)
    
    top_to_bottom = tvtk_base.true_bool_trait(help=\
        """
        Sets whether the stacks go from top to bottom or bottom to top.
        """
    )
    def _top_to_bottom_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTopToBottom,
                        self.top_to_bottom_)

    use_gradient_coloring = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off gradient coloring.
        """
    )
    def _use_gradient_coloring_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseGradientColoring,
                        self.use_gradient_coloring_)

    layer_thickness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the thickness of each layer
        """
    )
    def _layer_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLayerThickness,
                        self.layer_thickness)

    root_width = traits.Float(15.0, enter_set=True, auto_set=False, help=\
        """
        Set the width of the root node
        """
    )
    def _root_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRootWidth,
                        self.root_width)

    _updateable_traits_ = \
    (('edge_label_array_name', 'GetEdgeLabelArrayName'),
    ('render_on_mouse_move', 'GetRenderOnMouseMove'), ('interaction_mode',
    'GetInteractionMode'), ('use_gradient_coloring',
    'GetUseGradientColoring'), ('label_render_mode',
    'GetLabelRenderMode'), ('edge_scalar_bar_visibility',
    'GetEdgeScalarBarVisibility'), ('selection_mode', 'GetSelectionMode'),
    ('bundling_strength', 'GetBundlingStrength'),
    ('edge_color_array_name', 'GetEdgeColorArrayName'),
    ('display_hover_text', 'GetDisplayHoverText'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('edge_label_visibility', 'GetEdgeLabelVisibility'),
    ('area_label_font_size', 'GetAreaLabelFontSize'),
    ('label_placement_mode', 'GetLabelPlacementMode'),
    ('shrink_percentage', 'GetShrinkPercentage'),
    ('area_hover_array_name', 'GetAreaHoverArrayName'),
    ('area_label_visibility', 'GetAreaLabelVisibility'),
    ('reference_count', 'GetReferenceCount'), ('area_label_array_name',
    'GetAreaLabelArrayName'), ('layer_thickness', 'GetLayerThickness'),
    ('debug', 'GetDebug'), ('edge_label_font_size',
    'GetEdgeLabelFontSize'), ('area_size_array_name',
    'GetAreaSizeArrayName'), ('label_priority_array_name',
    'GetLabelPriorityArrayName'), ('use_rectangular_coordinates',
    'GetUseRectangularCoordinates'), ('color_edges', 'GetColorEdges'),
    ('color_areas', 'GetColorAreas'), ('icon_size', 'GetIconSize'),
    ('top_to_bottom', 'GetTopToBottom'), ('area_color_array_name',
    'GetAreaColorArrayName'), ('root_width', 'GetRootWidth'))
    
    _full_traitnames_list_ = \
    (['area_label_visibility', 'color_areas', 'color_edges', 'debug',
    'display_hover_text', 'edge_label_visibility',
    'global_warning_display', 'render_on_mouse_move', 'top_to_bottom',
    'use_gradient_coloring', 'use_rectangular_coordinates',
    'interaction_mode', 'label_placement_mode', 'label_render_mode',
    'selection_mode', 'area_color_array_name', 'area_hover_array_name',
    'area_label_array_name', 'area_label_font_size',
    'area_size_array_name', 'bundling_strength', 'edge_color_array_name',
    'edge_label_array_name', 'edge_label_font_size',
    'edge_scalar_bar_visibility', 'icon_size',
    'label_priority_array_name', 'layer_thickness', 'root_width',
    'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IcicleView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit IcicleView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['area_label_visibility', 'color_areas', 'color_edges',
            'display_hover_text', 'edge_label_visibility', 'render_on_mouse_move',
            'top_to_bottom', 'use_gradient_coloring',
            'use_rectangular_coordinates'], ['interaction_mode',
            'label_placement_mode', 'label_render_mode', 'selection_mode'],
            ['area_color_array_name', 'area_hover_array_name',
            'area_label_array_name', 'area_label_font_size',
            'area_size_array_name', 'bundling_strength', 'edge_color_array_name',
            'edge_label_array_name', 'edge_label_font_size',
            'edge_scalar_bar_visibility', 'icon_size',
            'label_priority_array_name', 'layer_thickness', 'root_width',
            'shrink_percentage']),
            title='Edit IcicleView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IcicleView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

