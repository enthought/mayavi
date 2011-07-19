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

from tvtk.tvtk_classes.prop import Prop


class LegendScaleActor(Prop):
    """
    LegendScaleActor - annotate the render window with scale and
    distance information
    
    Superclass: Prop
    
    This class is used to annotate the render window. Its basic goal is
    to provide an indication of the scale of the scene. Four axes
    surrounding the render window indicate (in a variety of ways) the
    scale of what the camera is viewing. An option also exists for
    displaying a scale legend.
    
    The axes can be programmed either to display distance scales or x-y
    coordinate values. By default, the scales display a distance.
    However, if you know that the view is down the z-axis, the scales can
    be programmed to display x-y coordinate values.
    
    Caveats:
    
    Please be aware that the axes and scale values are subject to
    perspective effects. The distances are computed in the focal plane of
    the camera. When there are large view angles (i.e., perspective
    projection), the computed distances may provide users the wrong sense
    of scale. These effects are not present when parallel projection is
    enabled.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLegendScaleActor, obj, update, **traits)
    
    top_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flags that control which of the four axes to display
        (top, bottom, left and right). By default, all the axes are
        displayed.
        """
    )
    def _top_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTopAxisVisibility,
                        self.top_axis_visibility_)

    right_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flags that control which of the four axes to display
        (top, bottom, left and right). By default, all the axes are
        displayed.
        """
    )
    def _right_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRightAxisVisibility,
                        self.right_axis_visibility_)

    legend_visibility = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether the legend scale should be displayed or not. The
        default is On.
        """
    )
    def _legend_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLegendVisibility,
                        self.legend_visibility_)

    left_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flags that control which of the four axes to display
        (top, bottom, left and right). By default, all the axes are
        displayed.
        """
    )
    def _left_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeftAxisVisibility,
                        self.left_axis_visibility_)

    bottom_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flags that control which of the four axes to display
        (top, bottom, left and right). By default, all the axes are
        displayed.
        """
    )
    def _bottom_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBottomAxisVisibility,
                        self.bottom_axis_visibility_)

    label_mode = traits.Trait('distance',
    tvtk_base.TraitRevPrefixMap({'distance': 0, 'xy_coordinates': 1}), help=\
        """
        Specify the mode for labeling the scale axes. By default, the
        axes are labeled with the distance between points (centered at a
        distance of 0.0). Alternatively if you know that the view is down
        the z-axis; the axes can be labeled with x-y coordinate values.
        """
    )
    def _label_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelMode,
                        self.label_mode_)

    left_border_offset = traits.Trait(50, traits.Range(5, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the offset of the left axis from the border. This number
        is expressed in pixels, and represents the approximate distance
        of the axes from the sides of the renderer. The default is 50.
        """
    )
    def _left_border_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeftBorderOffset,
                        self.left_border_offset)

    right_border_offset = traits.Trait(50, traits.Range(5, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the offset of the right axis from the border. This number
        is expressed in pixels, and represents the approximate distance
        of the axes from the sides of the renderer. The default is 50.
        """
    )
    def _right_border_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRightBorderOffset,
                        self.right_border_offset)

    bottom_border_offset = traits.Trait(30, traits.Range(5, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the offset of the bottom axis from the border. This
        number is expressed in pixels, and represents the approximate
        distance of the axes from the sides of the renderer. The default
        is 30.
        """
    )
    def _bottom_border_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBottomBorderOffset,
                        self.bottom_border_offset)

    corner_offset_factor = traits.Trait(2.0, traits.Range(1.0, 10.0, enter_set=True, auto_set=False), help=\
        """
        Get/Set the corner offset. This is the offset factor used to
        offset the axes at the corners. Default value is 2.0.
        """
    )
    def _corner_offset_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCornerOffsetFactor,
                        self.corner_offset_factor)

    top_border_offset = traits.Trait(30, traits.Range(5, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the offset of the top axis from the border. This number
        is expressed in pixels, and represents the approximate distance
        of the axes from the sides of the renderer. The default is 30.
        """
    )
    def _top_border_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTopBorderOffset,
                        self.top_border_offset)

    def _get_bottom_axis(self):
        return wrap_vtk(self._vtk_obj.GetBottomAxis())
    bottom_axis = traits.Property(_get_bottom_axis, help=\
        """
        These are methods to retrieve the AxisActors used to represent
        the four axes that form this representation. Users may retrieve
        and then modify these axes to control their appearance.
        """
    )

    def _get_left_axis(self):
        return wrap_vtk(self._vtk_obj.GetLeftAxis())
    left_axis = traits.Property(_get_left_axis, help=\
        """
        These are methods to retrieve the AxisActors used to represent
        the four axes that form this representation. Users may retrieve
        and then modify these axes to control their appearance.
        """
    )

    def _get_legend_label_property(self):
        return wrap_vtk(self._vtk_obj.GetLegendLabelProperty())
    legend_label_property = traits.Property(_get_legend_label_property, help=\
        """
        Set/Get the labels text properties for the legend title and
        labels.
        """
    )

    def _get_legend_title_property(self):
        return wrap_vtk(self._vtk_obj.GetLegendTitleProperty())
    legend_title_property = traits.Property(_get_legend_title_property, help=\
        """
        Set/Get the labels text properties for the legend title and
        labels.
        """
    )

    def _get_right_axis(self):
        return wrap_vtk(self._vtk_obj.GetRightAxis())
    right_axis = traits.Property(_get_right_axis, help=\
        """
        These are methods to retrieve the AxisActors used to represent
        the four axes that form this representation. Users may retrieve
        and then modify these axes to control their appearance.
        """
    )

    def _get_top_axis(self):
        return wrap_vtk(self._vtk_obj.GetTopAxis())
    top_axis = traits.Property(_get_top_axis, help=\
        """
        These are methods to retrieve the AxisActors used to represent
        the four axes that form this representation. Users may retrieve
        and then modify these axes to control their appearance.
        """
    )

    def all_annotations_off(self):
        """
        V.all_annotations_off()
        C++: void AllAnnotationsOff()
        Convenience method that turns all the axes and the legend scale.
        """
        ret = self._vtk_obj.AllAnnotationsOff()
        return ret
        

    def all_annotations_on(self):
        """
        V.all_annotations_on()
        C++: void AllAnnotationsOn()
        Convenience method that turns all the axes and the legend scale.
        """
        ret = self._vtk_obj.AllAnnotationsOn()
        return ret
        

    def all_axes_off(self):
        """
        V.all_axes_off()
        C++: void AllAxesOff()
        Convenience method that turns all the axes either on or off.
        """
        ret = self._vtk_obj.AllAxesOff()
        return ret
        

    def all_axes_on(self):
        """
        V.all_axes_on()
        C++: void AllAxesOn()
        Convenience method that turns all the axes either on or off.
        """
        ret = self._vtk_obj.AllAxesOn()
        return ret
        

    def build_representation(self, *args):
        """
        V.build_representation(Viewport)
        C++: virtual void BuildRepresentation(Viewport *viewport)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BuildRepresentation, *my_args)
        return ret

    _updateable_traits_ = \
    (('top_axis_visibility', 'GetTopAxisVisibility'),
    ('allocated_render_time', 'GetAllocatedRenderTime'),
    ('left_border_offset', 'GetLeftBorderOffset'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('legend_visibility', 'GetLegendVisibility'), ('bottom_border_offset',
    'GetBottomBorderOffset'), ('debug', 'GetDebug'), ('dragable',
    'GetDragable'), ('right_border_offset', 'GetRightBorderOffset'),
    ('visibility', 'GetVisibility'), ('left_axis_visibility',
    'GetLeftAxisVisibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('right_axis_visibility',
    'GetRightAxisVisibility'), ('top_border_offset',
    'GetTopBorderOffset'), ('label_mode', 'GetLabelMode'),
    ('reference_count', 'GetReferenceCount'), ('corner_offset_factor',
    'GetCornerOffsetFactor'), ('bottom_axis_visibility',
    'GetBottomAxisVisibility'), ('use_bounds', 'GetUseBounds'),
    ('pickable', 'GetPickable'))
    
    _full_traitnames_list_ = \
    (['bottom_axis_visibility', 'debug', 'dragable',
    'global_warning_display', 'left_axis_visibility', 'legend_visibility',
    'pickable', 'right_axis_visibility', 'top_axis_visibility',
    'use_bounds', 'visibility', 'label_mode', 'allocated_render_time',
    'bottom_border_offset', 'corner_offset_factor',
    'estimated_render_time', 'left_border_offset',
    'render_time_multiplier', 'right_border_offset', 'top_border_offset'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LegendScaleActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LegendScaleActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['bottom_axis_visibility', 'left_axis_visibility',
            'legend_visibility', 'right_axis_visibility', 'top_axis_visibility',
            'use_bounds', 'visibility'], ['label_mode'], ['allocated_render_time',
            'bottom_border_offset', 'corner_offset_factor',
            'estimated_render_time', 'left_border_offset',
            'render_time_multiplier', 'right_border_offset',
            'top_border_offset']),
            title='Edit LegendScaleActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LegendScaleActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

