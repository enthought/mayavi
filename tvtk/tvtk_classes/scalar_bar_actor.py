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

from tvtk.tvtk_classes.actor2d import Actor2D


class ScalarBarActor(Actor2D):
    """
    ScalarBarActor - Create a scalar bar with labels
    
    Superclass: Actor2D
    
    ScalarBarActor creates a scalar bar with annotation text. A scalar
    bar is a legend that indicates to the viewer the correspondence
    between color value and data value. The legend consists of a
    rectangular bar made of rectangular pieces each colored a constant
    value. Since ScalarBarActor is a subclass of Actor2D, it is
    drawn in the image plane (i.e., in the renderer's viewport) on top of
    the 3d graphics window.
    
    To use ScalarBarActor you must associate a ScalarsToColors (or
    subclass) with it. The lookup table defines the colors and the range
    of scalar values used to map scalar data.  Typically, the number of
    colors shown in the scalar bar is not equal to the number of colors
    in the lookup table, in which case sampling of the lookup table is
    performed.
    
    Other optional capabilities include specifying the fraction of the
    viewport size (both x and y directions) which will control the size
    of the scalar bar and the number of annotation labels. The actual
    position of the scalar bar on the screen is controlled by using the
    Actor2D::SetPosition() method (by default the scalar bar is
    centered in the viewport).  Other features include the ability to
    orient the scalar bar horizontally of vertically and controlling the
    format (printf style) with which to print the labels on the scalar
    bar. Also, the ScalarBarActor's property is applied to the scalar
    bar and annotation (including layer, and compositing operator).
    
    Set the text property/attributes of the title and the labels through
    the TextProperty objects associated to this actor.
    
    Caveats:
    
    If a LogLookupTable is specified as the lookup table to use, then
    the labels are created using a logarithmic scale.
    
    See Also:
    
    Actor2D TextProperty TextMapper PolyDataMapper2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarBarActor, obj, update, **traits)
    
    use_opacity = tvtk_base.false_bool_trait(help=\
        """
        Should be display the opacity as well. This is displayed by
        changing the opacity of the scalar bar in accordance with the
        opacity of the given color. For clarity, a texture grid is placed
        in the background if Opacity is ON. You might also want to play
        with set_texture_grid_with in that case. [Default: off]
        """
    )
    def _use_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseOpacity,
                        self.use_opacity_)

    text_position = traits.Trait('succeed_scalar_bar',
    tvtk_base.TraitRevPrefixMap({'succeed_scalar_bar': 1, 'precede_scalar_bar': 0}), help=\
        """
        Have the text preceding the scalar bar or suceeding it ? Succeed
        implies the that the text is Above scalar bar if orientation is
        horizontal or Right of scalar bar if orientation is vertical.
        Precede is the opposite
        """
    )
    def _text_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextPosition,
                        self.text_position_)

    orientation = traits.Trait('vertical',
    tvtk_base.TraitRevPrefixMap({'horizontal': 0, 'vertical': 1}), help=\
        """
        Control the orientation of the scalar bar.
        """
    )
    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation_)

    component_title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title for the component that is selected,
        """
    )
    def _component_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentTitle,
                        self.component_title)

    label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on the scalar
        bar.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    maximum_number_of_colors = traits.Trait(64, traits.Range(2, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the maximum number of scalar bar segments to show. This
        may differ from the number of colors in the lookup table, in
        which case the colors are samples from the lookup table.
        """
    )
    def _maximum_number_of_colors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfColors,
                        self.maximum_number_of_colors)

    texture_grid_width = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set the width of the texture grid. Used only if use_opacity is ON.
        """
    )
    def _texture_grid_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureGridWidth,
                        self.texture_grid_width)

    maximum_width_in_pixels = traits.Int(2147483647, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum width and height in pixels. Specifying the
        size as a relative fraction of the viewport can sometimes
        undersirably strech the size of the actor too much. These methods
        allow the user to set bounds on the maximum size of the scalar
        bar in pixels along any direction. Defaults to unbounded.
        """
    )
    def _maximum_width_in_pixels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumWidthInPixels,
                        self.maximum_width_in_pixels)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Set/Get the labels text property.
        """
    )

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set/Get the LookupTable to use. The lookup table specifies the
        number of colors to use in the table (if not overridden), as well
        as the scalar range.
        """
    )

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the scalar bar actor,
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    def _get_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTitleTextProperty())
    def _set_title_text_property(self, arg):
        old_val = self._get_title_text_property()
        self._wrap_call(self._vtk_obj.SetTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('title_text_property', old_val, arg)
    title_text_property = traits.Property(_get_title_text_property, _set_title_text_property, help=\
        """
        Set/Get the title text property.
        """
    )

    maximum_height_in_pixels = traits.Int(2147483647, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum width and height in pixels. Specifying the
        size as a relative fraction of the viewport can sometimes
        undersirably strech the size of the actor too much. These methods
        allow the user to set bounds on the maximum size of the scalar
        bar in pixels along any direction. Defaults to unbounded.
        """
    )
    def _maximum_height_in_pixels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumHeightInPixels,
                        self.maximum_height_in_pixels)

    number_of_labels = traits.Trait(5, traits.Range(0, 64, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of annotation labels to show.
        """
    )
    def _number_of_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLabels,
                        self.number_of_labels)

    def _get_texture_actor(self):
        return wrap_vtk(self._vtk_obj.GetTextureActor())
    texture_actor = traits.Property(_get_texture_actor, help=\
        """
        Get the texture actor.. you may want to change some properties on
        it
        """
    )

    _updateable_traits_ = \
    (('use_opacity', 'GetUseOpacity'), ('text_position',
    'GetTextPosition'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('orientation', 'GetOrientation'),
    ('maximum_width_in_pixels', 'GetMaximumWidthInPixels'),
    ('maximum_height_in_pixels', 'GetMaximumHeightInPixels'), ('height',
    'GetHeight'), ('debug', 'GetDebug'), ('maximum_number_of_colors',
    'GetMaximumNumberOfColors'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('component_title', 'GetComponentTitle'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('layer_number', 'GetLayerNumber'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('title', 'GetTitle'), ('label_format',
    'GetLabelFormat'), ('number_of_labels', 'GetNumberOfLabels'),
    ('use_bounds', 'GetUseBounds'), ('width', 'GetWidth'),
    ('texture_grid_width', 'GetTextureGridWidth'), ('visibility',
    'GetVisibility'), ('position2', 'GetPosition2'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'), ('pickable',
    'GetPickable'), ('dragable', 'GetDragable'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'use_opacity', 'visibility', 'orientation',
    'text_position', 'allocated_render_time', 'component_title',
    'estimated_render_time', 'height', 'label_format', 'layer_number',
    'maximum_height_in_pixels', 'maximum_number_of_colors',
    'maximum_width_in_pixels', 'number_of_labels', 'position',
    'position2', 'render_time_multiplier', 'texture_grid_width', 'title',
    'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarBarActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarBarActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['use_bounds', 'use_opacity', 'visibility'],
            ['orientation', 'text_position'], ['allocated_render_time',
            'component_title', 'estimated_render_time', 'height', 'label_format',
            'layer_number', 'maximum_height_in_pixels',
            'maximum_number_of_colors', 'maximum_width_in_pixels',
            'number_of_labels', 'position', 'position2', 'render_time_multiplier',
            'texture_grid_width', 'title', 'width']),
            title='Edit ScalarBarActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarBarActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

