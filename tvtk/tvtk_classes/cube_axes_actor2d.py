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


class CubeAxesActor2D(Actor2D):
    """
    CubeAxesActor2D - create a 2d plot of a bounding box edges - used
    for navigation
    
    Superclass: Actor2D
    
    CubeAxesActor2D is a composite actor that draws three axes of the
    bounding box of an input dataset. The axes include labels and titles
    for the x-y-z axes. The algorithm selects the axes that are on the
    "exterior" of the bounding box, exterior as determined from examining
    outer edges of the bounding box in projection (display) space.
    Alternatively, the edges closest to the viewer (i.e., camera
    position) can be drawn.
    
    To use this object you must define a bounding box and the camera used
    to render the CubeAxesActor2D. The camera is used to control the
    scaling and position of the CubeAxesActor2D so that it fits in the
    viewport and always remains visible.)
    
    The font property of the axes titles and labels can be modified
    through the axis_title_text_property and axis_label_text_property
    attributes. You may also use the get_x_axis_actor2d, get_y_axis_actor2d or
    get_z_axis_actor2d methods to access each individual axis actor to
    modify their font properties.
    
    The bounding box to use is defined in one of three ways. First, if
    the Input ivar is defined, then the input dataset's bounds is used.
    If the Input is not defined, and the Prop (superclass of all actors)
    is defined, then the Prop's bounds is used. If neither the Input or
    Prop is defined, then the Bounds instance variable (an array of six
    doubles) is used.
    
    See Also:
    
    Actor2D AxisActor2D XYPlotActor TextProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCubeAxesActor2D, obj, update, **traits)
    
    scaling = tvtk_base.true_bool_trait(help=\
        """
        Set/Get a flag that controls whether the axes are scaled to fit
        in the viewport. If off, the axes size remains constant (i.e.,
        stay the size of the bounding box). By default scaling is on so
        the axes are scaled to fit inside the viewport.
        """
    )
    def _scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaling,
                        self.scaling_)

    z_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of each axis.
        """
    )
    def _z_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisVisibility,
                        self.z_axis_visibility_)

    use_ranges = tvtk_base.false_bool_trait(help=\
        """
        Set/Get a flag that controls whether the axes use the data ranges
        or the ranges set by set_ranges. By default the axes use the data
        ranges.
        """
    )
    def _use_ranges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseRanges,
                        self.use_ranges_)

    x_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of each axis.
        """
    )
    def _x_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisVisibility,
                        self.x_axis_visibility_)

    y_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of each axis.
        """
    )
    def _y_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisVisibility,
                        self.y_axis_visibility_)

    fly_mode = traits.Trait('closest_triad',
    tvtk_base.TraitRevPrefixMap({'outer_edges': 0, 'none': 2, 'closest_triad': 1}), help=\
        """
        Specify a mode to control how the axes are drawn: either outer
        edges or closest triad to the camera position, or you may also
        disable flying of the axes.
        """
    )
    def _fly_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlyMode,
                        self.fly_mode_)

    def _get_axis_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisLabelTextProperty())
    def _set_axis_label_text_property(self, arg):
        old_val = self._get_axis_label_text_property()
        self._wrap_call(self._vtk_obj.SetAxisLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('axis_label_text_property', old_val, arg)
    axis_label_text_property = traits.Property(_get_axis_label_text_property, _set_axis_label_text_property, help=\
        """
        Set/Get the labels text property of all axes. Note that each axis
        can be controlled individually through the get_x/_y/_z_axis_actor2d()
        methods.
        """
    )

    font_factor = traits.Trait(1.0, traits.Range(0.10000000000000001, 2.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the overall size of the fonts
        used to label and title the axes.
        """
    )
    def _font_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontFactor,
                        self.font_factor)

    def _get_axis_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisTitleTextProperty())
    def _set_axis_title_text_property(self, arg):
        old_val = self._get_axis_title_text_property()
        self._wrap_call(self._vtk_obj.SetAxisTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('axis_title_text_property', old_val, arg)
    axis_title_text_property = traits.Property(_get_axis_title_text_property, _set_axis_title_text_property, help=\
        """
        Set/Get the title text property of all axes. Note that each axis
        can be controlled individually through the get_x/_y/_z_axis_actor2d()
        methods.
        """
    )

    label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on each of the
        x-y-z axes.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    show_actual_bounds = traits.Trait(1, traits.Range(0, 1, enter_set=True, auto_set=False), help=\
        """
        Set/Get the variable that controls whether the actual bounds of
        the dataset are always shown. Setting this variable to 1 means
        that clipping is disabled and that the actual value of the bounds
        is displayed even with corner offsets Setting this variable to 0
        means these axis will clip themselves and show variable bounds
        (legacy mode)
        """
    )
    def _show_actual_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowActualBounds,
                        self.show_actual_bounds)

    z_label = traits.String(r"Z", enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use "X",
        "Y" and "Z".
        """
    )
    def _z_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZLabel,
                        self.z_label)

    def _get_view_prop(self):
        return wrap_vtk(self._vtk_obj.GetViewProp())
    def _set_view_prop(self, arg):
        old_val = self._get_view_prop()
        self._wrap_call(self._vtk_obj.SetViewProp,
                        deref_vtk(arg))
        self.trait_property_changed('view_prop', old_val, arg)
    view_prop = traits.Property(_get_view_prop, _set_view_prop, help=\
        """
        Use the bounding box of this prop to draw the cube axes. The
        view_prop is used to determine the bounds only if the Input is not
        defined.
        """
    )

    bounds = traits.Array(shape=(6,), value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    ranges = traits.Array(shape=(6,), value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _ranges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRanges,
                        self.ranges)

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
        CubeAxesActor2D.
        """
    )

    x_label = traits.String(r"X", enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use "X",
        "Y" and "Z".
        """
    )
    def _x_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXLabel,
                        self.x_label)

    y_label = traits.String(r"Y", enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use "X",
        "Y" and "Z".
        """
    )
    def _y_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYLabel,
                        self.y_label)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Use the bounding box of this input dataset to draw the cube axes.
        If this is not specified, then the class will attempt to
        determine the bounds from the defined Prop or Bounds.
        """
    )

    corner_offset = traits.Float(0.05, enter_set=True, auto_set=False, help=\
        """
        Specify an offset value to "pull back" the axes from the corner
        at which they are joined to avoid overlap of axes labels. The
        "_corner_offset" is the fraction of the axis length to pull back.
        """
    )
    def _corner_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCornerOffset,
                        self.corner_offset)

    inertia = traits.Trait(1, traits.Range(1.0, 2147483647.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the inertial factor that controls how often (i.e, how
        many renders) the axes can switch position (jump from one axes to
        another).
        """
    )
    def _inertia_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInertia,
                        self.inertia)

    number_of_labels = traits.Trait(3, traits.Range(0, 50, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of annotation labels to show along the x, y,
        and z axes. This values is a suggestion: the number of labels may
        vary depending on the particulars of the data.
        """
    )
    def _number_of_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLabels,
                        self.number_of_labels)

    def _get_x_axis_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetXAxisActor2D())
    x_axis_actor2d = traits.Property(_get_x_axis_actor2d, help=\
        """
        Retrieve handles to the X, Y and Z axis (so that you can set
        their text properties for example)
        """
    )

    def _get_y_axis_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetYAxisActor2D())
    y_axis_actor2d = traits.Property(_get_y_axis_actor2d, help=\
        """
        Retrieve handles to the X, Y and Z axis (so that you can set
        their text properties for example)
        """
    )

    def _get_z_axis_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetZAxisActor2D())
    z_axis_actor2d = traits.Property(_get_z_axis_actor2d, help=\
        """
        Retrieve handles to the X, Y and Z axis (so that you can set
        their text properties for example)
        """
    )

    def set_x_origin(self, *args):
        """
        V.set_x_origin(float)
        C++: void SetXOrigin(double a)
        Explicitly specify an origin for the axes. These usually
        intersect at one of the corners of the bounding box, however
        users have the option to override this if necessary
        """
        ret = self._wrap_call(self._vtk_obj.SetXOrigin, *args)
        return ret

    def set_y_origin(self, *args):
        """
        V.set_y_origin(float)
        C++: void SetYOrigin(double a)
        Explicitly specify an origin for the axes. These usually
        intersect at one of the corners of the bounding box, however
        users have the option to override this if necessary
        """
        ret = self._wrap_call(self._vtk_obj.SetYOrigin, *args)
        return ret

    def set_z_origin(self, *args):
        """
        V.set_z_origin(float)
        C++: void SetZOrigin(double a)
        Explicitly specify an origin for the axes. These usually
        intersect at one of the corners of the bounding box, however
        users have the option to override this if necessary
        """
        ret = self._wrap_call(self._vtk_obj.SetZOrigin, *args)
        return ret

    _updateable_traits_ = \
    (('font_factor', 'GetFontFactor'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('y_label', 'GetYLabel'), ('dragable',
    'GetDragable'), ('fly_mode', 'GetFlyMode'), ('show_actual_bounds',
    'GetShowActualBounds'), ('height', 'GetHeight'), ('ranges',
    'GetRanges'), ('debug', 'GetDebug'), ('visibility', 'GetVisibility'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('inertia',
    'GetInertia'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('use_ranges', 'GetUseRanges'), ('pickable', 'GetPickable'),
    ('layer_number', 'GetLayerNumber'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('label_format', 'GetLabelFormat'),
    ('number_of_labels', 'GetNumberOfLabels'), ('bounds', 'GetBounds'),
    ('use_bounds', 'GetUseBounds'), ('width', 'GetWidth'),
    ('x_axis_visibility', 'GetXAxisVisibility'), ('y_axis_visibility',
    'GetYAxisVisibility'), ('scaling', 'GetScaling'), ('corner_offset',
    'GetCornerOffset'), ('position2', 'GetPosition2'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'), ('x_label',
    'GetXLabel'), ('z_axis_visibility', 'GetZAxisVisibility'), ('z_label',
    'GetZLabel'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'scaling', 'use_bounds', 'use_ranges', 'visibility',
    'x_axis_visibility', 'y_axis_visibility', 'z_axis_visibility',
    'fly_mode', 'allocated_render_time', 'bounds', 'corner_offset',
    'estimated_render_time', 'font_factor', 'height', 'inertia',
    'label_format', 'layer_number', 'number_of_labels', 'position',
    'position2', 'ranges', 'render_time_multiplier', 'show_actual_bounds',
    'width', 'x_label', 'y_label', 'z_label'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CubeAxesActor2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CubeAxesActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['scaling', 'use_bounds', 'use_ranges', 'visibility',
            'x_axis_visibility', 'y_axis_visibility', 'z_axis_visibility'],
            ['fly_mode'], ['allocated_render_time', 'bounds', 'corner_offset',
            'estimated_render_time', 'font_factor', 'height', 'inertia',
            'label_format', 'layer_number', 'number_of_labels', 'position',
            'position2', 'ranges', 'render_time_multiplier', 'show_actual_bounds',
            'width', 'x_label', 'y_label', 'z_label']),
            title='Edit CubeAxesActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CubeAxesActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

