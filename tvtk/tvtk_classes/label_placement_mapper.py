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

from tvtk.tvtk_classes.mapper2d import Mapper2D


class LabelPlacementMapper(Mapper2D):
    """
    LabelPlacementMapper - Places and renders non-overlapping labels.
    
    Superclass: Mapper2D
    
    To use this mapper, first send your data through
    PointSetToLabelHierarchy, which takes a set of points, associates
    special arrays to the points (label, priority, etc.), and produces a
    prioritized spatial tree of labels.
    
    This mapper then takes that hierarchy (or hierarchies) as input, and
    every frame will decide which labels and/or icons to place in order
    of priority, and will render only those labels/icons. A label render
    strategy is used to render the labels, and can use e.g. free_type or
    Qt for rendering.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabelPlacementMapper, obj, update, **traits)
    
    use_depth_buffer = tvtk_base.false_bool_trait(help=\
        """
        Use the depth buffer to test each label to see if it should not
        be displayed if it would be occluded by other objects in the
        scene. Off by default.
        """
    )
    def _use_depth_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDepthBuffer,
                        self.use_depth_buffer_)

    place_all_labels = tvtk_base.false_bool_trait(help=\
        """
        Tells the placer to place every label regardless of overlap. Off
        by default.
        """
    )
    def _place_all_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlaceAllLabels,
                        self.place_all_labels_)

    positions_as_normals = tvtk_base.false_bool_trait(help=\
        """
        Use label anchor point coordinates as normal vectors and
        eliminate those pointing away from the camera. Valid only when
        points are on a sphere centered at the origin (such as a 3d
        geographic view). Off by default.
        """
    )
    def _positions_as_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPositionsAsNormals,
                        self.positions_as_normals_)

    use_unicode_strings = tvtk_base.false_bool_trait(help=\
        """
        Set whether, or not, to use unicode strings.
        """
    )
    def _use_unicode_strings_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseUnicodeStrings,
                        self.use_unicode_strings_)

    generate_perturbed_label_spokes = tvtk_base.false_bool_trait(help=\
        """
        Enable drawing spokes (lines) to anchor point coordinates that
        were perturbed for being coincident with other anchor point
        coordinates.
        """
    )
    def _generate_perturbed_label_spokes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePerturbedLabelSpokes,
                        self.generate_perturbed_label_spokes_)

    output_traversed_bounds = tvtk_base.false_bool_trait(help=\
        """
        Whether to render traversed bounds. Off by default.
        """
    )
    def _output_traversed_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputTraversedBounds,
                        self.output_traversed_bounds_)

    shape = traits.Trait('none',
    tvtk_base.TraitRevPrefixMap({'none': 0, 'rounded_rect': 2, 'rect': 1}), help=\
        """
        The shape of the label background, should be one of the values in
        the label_shape enumeration.
        """
    )
    def _shape_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShape,
                        self.shape_)

    style = traits.Trait('filled',
    tvtk_base.TraitRevPrefixMap({'outline': 1, 'filled': 0}), help=\
        """
        The style of the label background shape, should be one of the
        values in the label_style enumeration.
        """
    )
    def _style_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStyle,
                        self.style_)

    iterator_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        The type of iterator used when traversing the labels. May be
        LabelHierarchy::FRUSTUM or LabelHierarchy::FULL_SORT
        """
    )
    def _iterator_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIteratorType,
                        self.iterator_type)

    def _get_render_strategy(self):
        return wrap_vtk(self._vtk_obj.GetRenderStrategy())
    def _set_render_strategy(self, arg):
        old_val = self._get_render_strategy()
        self._wrap_call(self._vtk_obj.SetRenderStrategy,
                        deref_vtk(arg))
        self.trait_property_changed('render_strategy', old_val, arg)
    render_strategy = traits.Property(_get_render_strategy, _set_render_strategy, help=\
        """
        Set the label rendering strategy.
        """
    )

    background_color = tvtk_base.vtk_color_trait((0.5, 0.5, 0.5), help=\
        """
        
        """
    )
    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color, False)

    background_opacity = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The opacity of the background shape.
        """
    )
    def _background_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundOpacity,
                        self.background_opacity)

    margin = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        The size of the margin on the label background shape. Default is
        5.
        """
    )
    def _margin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMargin,
                        self.margin)

    maximum_label_fraction = traits.Trait(0.05, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The maximum fraction of the screen that the labels may cover.
        Label placement stops when this fraction is reached.
        """
    )
    def _maximum_label_fraction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLabelFraction,
                        self.maximum_label_fraction)

    def _get_anchor_transform(self):
        return wrap_vtk(self._vtk_obj.GetAnchorTransform())
    anchor_transform = traits.Property(_get_anchor_transform, help=\
        """
        Get the transform for the anchor points.
        """
    )

    _updateable_traits_ = \
    (('iterator_type', 'GetIteratorType'), ('style', 'GetStyle'),
    ('use_depth_buffer', 'GetUseDepthBuffer'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('use_unicode_strings',
    'GetUseUnicodeStrings'), ('margin', 'GetMargin'),
    ('positions_as_normals', 'GetPositionsAsNormals'), ('progress_text',
    'GetProgressText'), ('place_all_labels', 'GetPlaceAllLabels'),
    ('debug', 'GetDebug'), ('background_opacity', 'GetBackgroundOpacity'),
    ('shape', 'GetShape'), ('abort_execute', 'GetAbortExecute'),
    ('maximum_label_fraction', 'GetMaximumLabelFraction'),
    ('release_data_flag', 'GetReleaseDataFlag'),
    ('output_traversed_bounds', 'GetOutputTraversedBounds'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('generate_perturbed_label_spokes',
    'GetGeneratePerturbedLabelSpokes'), ('background_color',
    'GetBackgroundColor'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_perturbed_label_spokes',
    'global_warning_display', 'output_traversed_bounds',
    'place_all_labels', 'positions_as_normals', 'release_data_flag',
    'use_depth_buffer', 'use_unicode_strings', 'shape', 'style',
    'background_color', 'background_opacity', 'iterator_type', 'margin',
    'maximum_label_fraction', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabelPlacementMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LabelPlacementMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_perturbed_label_spokes',
            'output_traversed_bounds', 'place_all_labels', 'positions_as_normals',
            'use_depth_buffer', 'use_unicode_strings'], ['shape', 'style'],
            ['background_color', 'background_opacity', 'iterator_type', 'margin',
            'maximum_label_fraction']),
            title='Edit LabelPlacementMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabelPlacementMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

