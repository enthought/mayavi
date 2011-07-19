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

from tvtk.tvtk_classes.actor import Actor


class CubeAxesActor(Actor):
    """
    CubeAxesActor - create a  plot of a bounding box edges -
    
    Superclass: Actor
    
    CubeAxesActor is a composite actor that draws axes of the bounding
    box of an input dataset. The axes include labels and titles for the
    x-y-z axes. The algorithm selects which axes to draw based on the
    user-defined 'fly' mode.  (STATIC is default). 'STATIC' constructs
    axes from all edges of the bounding box. 'CLOSEST_TRIAD' consists of
    the three axes x-y-z forming a triad that lies closest to the
    specified camera. 'FURTHEST_TRIAD' consists of the three axes x-y-z
    forming a triad that lies furthest from the specified camera.
    'OUTER_EDGES' is constructed from edges that are on the "exterior" of
    the bounding box, exterior as determined from examining outer edges
    of the bounding box in projection (display) space.
    
    To use this object you must define a bounding box and the camera used
    to render the CubeAxesActor. You can optionally turn on/off
    labels, ticks, gridlines, and set tick location, number of labels,
    and text to use for axis-titles.  A 'corner offset' can also be set. 
    This allows the axes to be set partially away from the actual
    bounding box to perhaps prevent overlap of labels between the various
    axes.
    
    The Bounds instance variable (an array of six doubles) is used to
    determine the bounding box.
    
    See Also:
    
    Actor AxisActor CubeAxesActor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCubeAxesActor, obj, update, **traits)
    
    z_axis_label_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _z_axis_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisLabelVisibility,
                        self.z_axis_label_visibility_)

    y_axis_minor_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _y_axis_minor_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisMinorTickVisibility,
                        self.y_axis_minor_tick_visibility_)

    z_axis_minor_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _z_axis_minor_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisMinorTickVisibility,
                        self.z_axis_minor_tick_visibility_)

    y_axis_label_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _y_axis_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisLabelVisibility,
                        self.y_axis_label_visibility_)

    z_axis_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _z_axis_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisTickVisibility,
                        self.z_axis_tick_visibility_)

    x_axis_label_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of labels for each axis.
        """
    )
    def _x_axis_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisLabelVisibility,
                        self.x_axis_label_visibility_)

    x_axis_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of ticks for each axis.
        """
    )
    def _x_axis_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisTickVisibility,
                        self.x_axis_tick_visibility_)

    y_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of each axis.
        """
    )
    def _y_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisVisibility,
                        self.y_axis_visibility_)

    draw_x_gridlines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _draw_x_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawXGridlines,
                        self.draw_x_gridlines_)

    draw_y_gridlines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _draw_y_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawYGridlines,
                        self.draw_y_gridlines_)

    x_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of each axis.
        """
    )
    def _x_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisVisibility,
                        self.x_axis_visibility_)

    x_axis_minor_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of minor ticks for each axis.
        """
    )
    def _x_axis_minor_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisMinorTickVisibility,
                        self.x_axis_minor_tick_visibility_)

    z_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of each axis.
        """
    )
    def _z_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisVisibility,
                        self.z_axis_visibility_)

    y_axis_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )
    def _y_axis_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisTickVisibility,
                        self.y_axis_tick_visibility_)

    draw_z_gridlines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _draw_z_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawZGridlines,
                        self.draw_z_gridlines_)

    fly_mode = traits.Trait('closest_triad',
    tvtk_base.TraitRevPrefixMap({'outer_edges': 0, 'static_triad': 3, 'closest_triad': 1, 'furthest_triad': 2, 'static_edges': 4}), help=\
        """
        Specify a mode to control how the axes are drawn: either static,
        closest triad, furthest triad or outer edges in relation to the
        camera position.
        """
    )
    def _fly_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlyMode,
                        self.fly_mode_)

    tick_location = traits.Trait('inside',
    tvtk_base.TraitRevPrefixMap({'both': 2, 'inside': 0, 'outside': 1}), help=\
        """
        Set/Get the location of ticks marks.
        """
    )
    def _tick_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickLocation,
                        self.tick_location_)

    x_units = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )
    def _x_units_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXUnits,
                        self.x_units)

    x_axis_range = traits.Array(shape=(2,), value=(1.0000000000000001e+299, 1.0000000000000001e+299), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _x_axis_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisRange,
                        self.x_axis_range)

    y_axis_range = traits.Array(shape=(2,), value=(1.0000000000000001e+299, 1.0000000000000001e+299), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _y_axis_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisRange,
                        self.y_axis_range)

    x_title = traits.String(r"X-Axis", enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )
    def _x_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXTitle,
                        self.x_title)

    bounds = traits.Array(shape=(6,), value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    z_title = traits.String(r"Z-Axis", enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )
    def _z_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZTitle,
                        self.z_title)

    z_units = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )
    def _z_units_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZUnits,
                        self.z_units)

    z_label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on each of the
        x-y-z axes.
        """
    )
    def _z_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZLabelFormat,
                        self.z_label_format)

    z_axis_range = traits.Array(shape=(2,), value=(1.0000000000000001e+299, 1.0000000000000001e+299), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _z_axis_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisRange,
                        self.z_axis_range)

    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Set/Get the camera to perform scaling and translation of the
        CubeAxesActor.
        """
    )

    y_units = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )
    def _y_units_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYUnits,
                        self.y_units)

    y_label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on each of the
        x-y-z axes.
        """
    )
    def _y_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYLabelFormat,
                        self.y_label_format)

    corner_offset = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify an offset value to "pull back" the axes from the corner
        at which they are joined to avoid overlap of axes labels. The
        "_corner_offset" is the fraction of the axis length to pull back.
        """
    )
    def _corner_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCornerOffset,
                        self.corner_offset)

    x_label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on each of the
        x-y-z axes.
        """
    )
    def _x_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXLabelFormat,
                        self.x_label_format)

    inertia = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the inertial factor that controls how often (i.e, how
        many renders) the axes can switch position (jump from one axes to
        another).
        """
    )
    def _inertia_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInertia,
                        self.inertia)

    y_title = traits.String(r"Y-Axis", enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )
    def _y_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYTitle,
                        self.y_title)

    def render_translucent_geometry(self, *args):
        """
        V.render_translucent_geometry(Viewport) -> int
        C++: virtual int RenderTranslucentGeometry(Viewport *)
        Draw the axes as per the Prop superclass' API.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderTranslucentGeometry, *my_args)
        return ret

    def set_label_scaling(self, *args):
        """
        V.set_label_scaling(bool, int, int, int)
        C++: void SetLabelScaling(bool, int, int, int)"""
        ret = self._wrap_call(self._vtk_obj.SetLabelScaling, *args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('y_units', 'GetYUnits'), ('z_title',
    'GetZTitle'), ('y_title', 'GetYTitle'), ('dragable', 'GetDragable'),
    ('fly_mode', 'GetFlyMode'), ('y_axis_range', 'GetYAxisRange'),
    ('y_axis_tick_visibility', 'GetYAxisTickVisibility'), ('z_axis_range',
    'GetZAxisRange'), ('y_label_format', 'GetYLabelFormat'),
    ('draw_x_gridlines', 'GetDrawXGridlines'), ('orientation',
    'GetOrientation'), ('draw_z_gridlines', 'GetDrawZGridlines'),
    ('scale', 'GetScale'), ('x_title', 'GetXTitle'),
    ('x_axis_label_visibility', 'GetXAxisLabelVisibility'),
    ('y_axis_label_visibility', 'GetYAxisLabelVisibility'),
    ('tick_location', 'GetTickLocation'), ('debug', 'GetDebug'),
    ('z_axis_tick_visibility', 'GetZAxisTickVisibility'),
    ('x_axis_visibility', 'GetXAxisVisibility'), ('y_axis_visibility',
    'GetYAxisVisibility'), ('corner_offset', 'GetCornerOffset'),
    ('z_axis_label_visibility', 'GetZAxisLabelVisibility'), ('pickable',
    'GetPickable'), ('z_units', 'GetZUnits'),
    ('y_axis_minor_tick_visibility', 'GetYAxisMinorTickVisibility'),
    ('x_axis_minor_tick_visibility', 'GetXAxisMinorTickVisibility'),
    ('allocated_render_time', 'GetAllocatedRenderTime'),
    ('draw_y_gridlines', 'GetDrawYGridlines'), ('visibility',
    'GetVisibility'), ('x_axis_tick_visibility',
    'GetXAxisTickVisibility'), ('position', 'GetPosition'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('z_axis_minor_tick_visibility', 'GetZAxisMinorTickVisibility'),
    ('inertia', 'GetInertia'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('x_axis_range', 'GetXAxisRange'),
    ('z_label_format', 'GetZLabelFormat'), ('bounds', 'GetBounds'),
    ('use_bounds', 'GetUseBounds'), ('x_units', 'GetXUnits'),
    ('reference_count', 'GetReferenceCount'), ('x_label_format',
    'GetXLabelFormat'), ('z_axis_visibility', 'GetZAxisVisibility'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'draw_x_gridlines', 'draw_y_gridlines',
    'draw_z_gridlines', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'x_axis_label_visibility',
    'x_axis_minor_tick_visibility', 'x_axis_tick_visibility',
    'x_axis_visibility', 'y_axis_label_visibility',
    'y_axis_minor_tick_visibility', 'y_axis_tick_visibility',
    'y_axis_visibility', 'z_axis_label_visibility',
    'z_axis_minor_tick_visibility', 'z_axis_tick_visibility',
    'z_axis_visibility', 'fly_mode', 'tick_location',
    'allocated_render_time', 'bounds', 'corner_offset',
    'estimated_render_time', 'inertia', 'orientation', 'origin',
    'position', 'render_time_multiplier', 'scale', 'x_axis_range',
    'x_label_format', 'x_title', 'x_units', 'y_axis_range',
    'y_label_format', 'y_title', 'y_units', 'z_axis_range',
    'z_label_format', 'z_title', 'z_units'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CubeAxesActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CubeAxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['draw_x_gridlines', 'draw_y_gridlines',
            'draw_z_gridlines', 'use_bounds', 'visibility',
            'x_axis_label_visibility', 'x_axis_minor_tick_visibility',
            'x_axis_tick_visibility', 'x_axis_visibility',
            'y_axis_label_visibility', 'y_axis_minor_tick_visibility',
            'y_axis_tick_visibility', 'y_axis_visibility',
            'z_axis_label_visibility', 'z_axis_minor_tick_visibility',
            'z_axis_tick_visibility', 'z_axis_visibility'], ['fly_mode',
            'tick_location'], ['allocated_render_time', 'bounds', 'corner_offset',
            'estimated_render_time', 'inertia', 'orientation', 'origin',
            'position', 'render_time_multiplier', 'scale', 'x_axis_range',
            'x_label_format', 'x_title', 'x_units', 'y_axis_range',
            'y_label_format', 'y_title', 'y_units', 'z_axis_range',
            'z_label_format', 'z_title', 'z_units']),
            title='Edit CubeAxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CubeAxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

