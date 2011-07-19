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

from tvtk.tvtk_classes.poly_data_source_widget import PolyDataSourceWidget


class ImagePlaneWidget(PolyDataSourceWidget):
    """
    ImagePlaneWidget - 3d widget for reslicing image data
    
    Superclass: PolyDataSourceWidget
    
    This 3d widget defines a plane that can be interactively placed in an
    image volume. A nice feature of the object is that the
    ImagePlaneWidget, like any 3d widget, will work with the current
    interactor style. That is, if ImagePlaneWidget does not handle an
    event, then all other registered observers (including the interactor
    style) have an opportunity to process the event. Otherwise, the
    ImagePlaneWidget will terminate the processing of the event that
    it handles.
    
    The core functionality of the widget is provided by a ImageReslice
    object which passes its output onto a texture mapping pipeline for
    fast slicing through volumetric data. See the key methods:
    generate_texture_plane() and update_plane() for implementation details.
    
    To use this object, just invoke set_interactor() with the argument of
    the method a RenderWindowInteractor.  You may also wish to invoke
    "_place_widget()" to initially position the widget. If the "i" key (for
    "interactor") is pressed, the ImagePlaneWidget will appear. (See
    superclass documentation for information about changing this
    behavior.)
    
    Selecting the widget with the middle mouse button with and without
    holding the shift or control keys enables complex reslicing
    capablilites. To facilitate use, a set of 'margins' (left, right,
    top, bottom) are shown as a set of plane-axes aligned lines, the
    properties of which can be changed as a group. Without keyboard
    modifiers: selecting in the middle of the margins enables translation
    of the plane along its normal. Selecting one of the corners within
    the margins enables spinning around the plane's normal at its center.
     Selecting within a margin allows rotating about the center of the
    plane around an axis aligned with the margin (i.e., selecting left
    margin enables rotating around the plane's local y-prime axis). With
    control key modifier: margin selection enables edge translation
    (i.e., a constrained form of scaling). Selecting within the margins
    enables translation of the entire plane. With shift key modifier:
    uniform plane scaling is enabled.  Moving the mouse up enlarges the
    plane while downward movement shrinks it.
    
    Window-level is achieved by using the right mouse button. 
    Window-level values can be reset by shift + 'r' or control + 'r'
    while regular reset camera is maintained with 'r' or 'R'. The left
    mouse button can be used to query the underlying image data with a
    snap-to cross-hair cursor.  Currently, the nearest point in the input
    image data to the mouse cursor generates the cross-hairs.  With
    oblique slicing, this behaviour may appear unsatisfactory. Text
    display of window-level and image coordinates/data values are
    provided by a text actor/mapper pair.
    
    Events that occur outside of the widget (i.e., no part of the widget
    is picked) are propagated to any other registered obsevers (such as
    the interaction style). Turn off the widget by pressing the "i" key
    again (or invoke the Off() method). To support interactive
    manipulation of objects, this class invokes the events
    start_interaction_event, interaction_event, and end_interaction_event as
    well as start_window_level_event, window_level_event, end_window_level_event
    and reset_window_level_event.
    
    The ImagePlaneWidget has several methods that can be used in
    conjunction with other VTK objects. The get_poly_data() method can be
    used to get the polygonal representation of the plane and can be used
    as input for other VTK objects. Typical usage of the widget is to
    make use of the start_interaction_event, interaction_event, and
    end_interaction_event events. The interaction_event is called on mouse
    motion; the other two events are called on button down and button up
    (either left or right button).
    
    Some additional features of this class include the ability to control
    the properties of the widget. You can set the properties of: the
    selected and unselected representations of the plane's outline; the
    text actor via its TextProperty; the cross-hair cursor. In
    addition there are methods to constrain the plane so that it is
    aligned along the x-y-z axes.  Finally, one can specify the degree of
    interpolation (vtk_image_reslice): nearest neighbour, linear, and
    cubic.
    
    Caveats:
    
    Note that handles and plane can be picked even when they are "behind"
    other actors.  This is an intended feature and not a bug.
    
    See Also:
    
    ThreeDWidget BoxWidget LineWidget  PlaneWidget PointWidget
    PolyDataSourceWidget SphereWidget ImplicitPlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImagePlaneWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(ImagePlaneWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    interaction = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable mouse interaction so the widget remains on
        display.
        """
    )
    def _interaction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteraction,
                        self.interaction_)

    restrict_plane_to_volume = tvtk_base.true_bool_trait(help=\
        """
        Make sure that the plane remains within the volume. Default is
        On.
        """
    )
    def _restrict_plane_to_volume_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRestrictPlaneToVolume,
                        self.restrict_plane_to_volume_)

    texture_interpolate = tvtk_base.true_bool_trait(help=\
        """
        Specify whether to interpolate the texture or not. When off, the
        reslice interpolation is nearest neighbour regardless of how the
        interpolation is set through the API. Set before setting the
        ImageData input. Default is On.
        """
    )
    def _texture_interpolate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureInterpolate,
                        self.texture_interpolate_)

    user_controlled_lookup_table = tvtk_base.false_bool_trait(help=\
        """
        Let the user control the lookup table. NOTE: apply this method
        BEFORE applying the set_lookup_table method. Default is Off.
        """
    )
    def _user_controlled_lookup_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUserControlledLookupTable,
                        self.user_controlled_lookup_table_)

    texture_visibility = tvtk_base.true_bool_trait(help=\
        """
        Control the visibility of the actual texture mapped reformatted
        plane. in some cases you may only want the plane outline for
        example.
        """
    )
    def _texture_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureVisibility,
                        self.texture_visibility_)

    display_text = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable text display of window-level, image coordinates
        and scalar values in a render window.
        """
    )
    def _display_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayText,
                        self.display_text_)

    use_continuous_cursor = tvtk_base.false_bool_trait(help=\
        """
        Choose between voxel centered or continuous cursor probing.  With
        voxel centered probing, the cursor snaps to the nearest voxel and
        the reported cursor coordinates are extent based.  With
        continuous probing, voxel data is interpolated using
        DataSetAttributes' interpolate_point method and the reported
        coordinates are 3d spatial continuous.
        """
    )
    def _use_continuous_cursor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseContinuousCursor,
                        self.use_continuous_cursor_)

    reslice_interpolate = traits.Trait('linear',
    tvtk_base.TraitRevPrefixMap({'nearest_neighbour': 0, 'linear': 1, 'cubic': 2}), help=\
        """
        Set the interpolation to use when texturing the plane.
        """
    )
    def _reslice_interpolate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResliceInterpolate,
                        self.reslice_interpolate_)

    plane_orientation = traits.Trait('x_axes', 3,
    tvtk_base.TraitRevPrefixMap({'z_axes': 2, 'y_axes': 1, 'x_axes': 0}), help=\
        """
        Convenience method sets the plane orientation normal to the x, y,
        or z axes.  Default is XAxes (0).
        """
    )
    def _plane_orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlaneOrientation,
                        self.plane_orientation_)

    def _get_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetPlaneProperty())
    def _set_plane_property(self, arg):
        old_val = self._get_plane_property()
        self._wrap_call(self._vtk_obj.SetPlaneProperty,
                        deref_vtk(arg))
        self.trait_property_changed('plane_property', old_val, arg)
    plane_property = traits.Property(_get_plane_property, _set_plane_property, help=\
        """
        Set/Get the plane's outline properties. The properties of the
        plane's outline when selected and unselected can be manipulated.
        """
    )

    def _get_color_map(self):
        return wrap_vtk(self._vtk_obj.GetColorMap())
    def _set_color_map(self, arg):
        old_val = self._get_color_map()
        self._wrap_call(self._vtk_obj.SetColorMap,
                        deref_vtk(arg))
        self.trait_property_changed('color_map', old_val, arg)
    color_map = traits.Property(_get_color_map, _set_color_map, help=\
        """
        Convenience method to get the ImageMapToColors filter used by
        this widget.  The user can properly render other transparent
        actors in a scene by calling the filter's set_output_format_to_rgb
        and pass_alpha_to_output_off.
        """
    )

    right_button_action = traits.Trait(2, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set action associated to buttons.
        """
    )
    def _right_button_action_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRightButtonAction,
                        self.right_button_action)

    def _get_margin_property(self):
        return wrap_vtk(self._vtk_obj.GetMarginProperty())
    def _set_margin_property(self, arg):
        old_val = self._get_margin_property()
        self._wrap_call(self._vtk_obj.SetMarginProperty,
                        deref_vtk(arg))
        self.trait_property_changed('margin_property', old_val, arg)
    margin_property = traits.Property(_get_margin_property, _set_margin_property, help=\
        """
        Set the properties of the margins.
        """
    )

    point1 = traits.Array(shape=(3,), value=(0.0, 0.5, -0.5), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the position of the point defining the first axis of the
        plane.
        """
    )
    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(shape=(3,), value=(0.0, -0.5, 0.5), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the position of the point defining the second axis of the
        plane.
        """
    )
    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    def _get_texture_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetTexturePlaneProperty())
    def _set_texture_plane_property(self, arg):
        old_val = self._get_texture_plane_property()
        self._wrap_call(self._vtk_obj.SetTexturePlaneProperty,
                        deref_vtk(arg))
        self.trait_property_changed('texture_plane_property', old_val, arg)
    texture_plane_property = traits.Property(_get_texture_plane_property, _set_texture_plane_property, help=\
        """
        Set/Get the property for the resliced image.
        """
    )

    left_button_auto_modifier = traits.Trait(0, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set the auto-modifiers associated to buttons. This allows users
        to bind some buttons to actions that are usually triggered by a
        key modifier. For example, if you do not need cursoring, you can
        bind the left button action to VTK_SLICE_MOTION_ACTION (see
        above) and the left button auto modifier to VTK_CONTROL_MODIFIER:
        you end up with the left button controling panning without
        pressing a key.
        """
    )
    def _left_button_auto_modifier_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeftButtonAutoModifier,
                        self.left_button_auto_modifier)

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    def _set_text_property(self, arg):
        old_val = self._get_text_property()
        self._wrap_call(self._vtk_obj.SetTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('text_property', old_val, arg)
    text_property = traits.Property(_get_text_property, _set_text_property, help=\
        """
        Set/Get the text property for the image data and window-level
        annotation.
        """
    )

    slice_index = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the slice position in terms of the data extent.
        """
    )
    def _slice_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceIndex,
                        self.slice_index)

    def _get_selected_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedPlaneProperty())
    def _set_selected_plane_property(self, arg):
        old_val = self._get_selected_plane_property()
        self._wrap_call(self._vtk_obj.SetSelectedPlaneProperty,
                        deref_vtk(arg))
        self.trait_property_changed('selected_plane_property', old_val, arg)
    selected_plane_property = traits.Property(_get_selected_plane_property, _set_selected_plane_property, help=\
        """
        Set/Get the plane's outline properties. The properties of the
        plane's outline when selected and unselected can be manipulated.
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
        Set/Get the internal lookuptable (lut) to one defined by the
        user, or, alternatively, to the lut of another
        ImgePlaneWidget.  In this way, a set of three orthogonal
        planes can share the same lut so that window-levelling is
        performed uniformly among planes.  The default internal lut can
        be re- set/allocated by setting to 0 (NULL).
        """
    )

    middle_button_action = traits.Trait(1, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set action associated to buttons.
        """
    )
    def _middle_button_action_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMiddleButtonAction,
                        self.middle_button_action)

    slice_position = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the position of the slice along its normal.
        """
    )
    def _slice_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlicePosition,
                        self.slice_position)

    right_button_auto_modifier = traits.Trait(0, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set the auto-modifiers associated to buttons. This allows users
        to bind some buttons to actions that are usually triggered by a
        key modifier. For example, if you do not need cursoring, you can
        bind the left button action to VTK_SLICE_MOTION_ACTION (see
        above) and the left button auto modifier to VTK_CONTROL_MODIFIER:
        you end up with the left button controling panning without
        pressing a key.
        """
    )
    def _right_button_auto_modifier_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRightButtonAutoModifier,
                        self.right_button_auto_modifier)

    origin = traits.Array(shape=(3,), value=(0.0, -0.5, -0.5), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the origin of the plane.
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    def _get_cursor_property(self):
        return wrap_vtk(self._vtk_obj.GetCursorProperty())
    def _set_cursor_property(self, arg):
        old_val = self._get_cursor_property()
        self._wrap_call(self._vtk_obj.SetCursorProperty,
                        deref_vtk(arg))
        self.trait_property_changed('cursor_property', old_val, arg)
    cursor_property = traits.Property(_get_cursor_property, _set_cursor_property, help=\
        """
        Set the properties of the cross-hair cursor.
        """
    )

    middle_button_auto_modifier = traits.Trait(0, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set the auto-modifiers associated to buttons. This allows users
        to bind some buttons to actions that are usually triggered by a
        key modifier. For example, if you do not need cursoring, you can
        bind the left button action to VTK_SLICE_MOTION_ACTION (see
        above) and the left button auto modifier to VTK_CONTROL_MODIFIER:
        you end up with the left button controling panning without
        pressing a key.
        """
    )
    def _middle_button_auto_modifier_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMiddleButtonAutoModifier,
                        self.middle_button_auto_modifier)

    margin_size_y = traits.Trait(0.05, traits.Range(0.0, 0.5, enter_set=True, auto_set=False), help=\
        """
        Set the size of the margins based on a percentage of the plane's
        width and height, limited between 0 and 50%.
        """
    )
    def _margin_size_y_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMarginSizeY,
                        self.margin_size_y)

    left_button_action = traits.Trait(0, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set action associated to buttons.
        """
    )
    def _left_button_action_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeftButtonAction,
                        self.left_button_action)

    margin_size_x = traits.Trait(0.05, traits.Range(0.0, 0.5, enter_set=True, auto_set=False), help=\
        """
        Set the size of the margins based on a percentage of the plane's
        width and height, limited between 0 and 50%.
        """
    )
    def _margin_size_x_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMarginSizeX,
                        self.margin_size_x)

    def get_window_level(self, *args):
        """
        V.get_window_level([float, float])
        C++: void GetWindowLevel(double wl[2])
        Set/Get the current window and level values.  set_window_level
        should only be called after set_input.  If a shared lookup table
        is being used, a callback is required to update the window level
        values without having to update the lookup table again.
        """
        ret = self._wrap_call(self._vtk_obj.GetWindowLevel, *args)
        return ret

    def set_window_level(self, *args):
        """
        V.set_window_level(float, float, int)
        C++: void SetWindowLevel(double window, double level, int copy=0)
        Set/Get the current window and level values.  set_window_level
        should only be called after set_input.  If a shared lookup table
        is being used, a callback is required to update the window level
        values without having to update the lookup table again.
        """
        ret = self._wrap_call(self._vtk_obj.SetWindowLevel, *args)
        return ret

    def _get_center(self):
        return self._vtk_obj.GetCenter()
    center = traits.Property(_get_center, help=\
        """
        Get the center of the plane.
        """
    )

    def _get_current_cursor_position(self):
        return self._vtk_obj.GetCurrentCursorPosition()
    current_cursor_position = traits.Property(_get_current_cursor_position, help=\
        """
        Get the current cursor position.  To be used in conjunction with
        get_cursor_data_status.
        """
    )

    def _get_current_image_value(self):
        return self._vtk_obj.GetCurrentImageValue()
    current_image_value = traits.Property(_get_current_image_value, help=\
        """
        Get the current image value at the current cursor position.  To
        be used in conjunction with get_cursor_data_status.  The value is
        VTK_DOUBLE_MAX when the data is invalid.
        """
    )

    def get_cursor_data(self, *args):
        """
        V.get_cursor_data([float, float, float, float]) -> int
        C++: int GetCursorData(double xyzv[4])
        Get the image coordinate position and voxel value.  Currently
        only supports single component image data.
        """
        ret = self._wrap_call(self._vtk_obj.GetCursorData, *args)
        return ret

    def _get_cursor_data_status(self):
        return self._vtk_obj.GetCursorDataStatus()
    cursor_data_status = traits.Property(_get_cursor_data_status, help=\
        """
        Get the status of the cursor data.  If this returns 1 the
        current_cursor_position and current_image_value will have current
        data.  If it returns 0, these values are invalid.
        """
    )

    def _get_level(self):
        return self._vtk_obj.GetLevel()
    level = traits.Property(_get_level, help=\
        """
        Set/Get the current window and level values.  set_window_level
        should only be called after set_input.  If a shared lookup table
        is being used, a callback is required to update the window level
        values without having to update the lookup table again.
        """
    )

    def _get_normal(self):
        return self._vtk_obj.GetNormal()
    normal = traits.Property(_get_normal, help=\
        """
        Get the normal to the plane.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata (including points) that defines the plane.  The
        polydata consists of (res+1)*(res+1) points, and res*res
        quadrilateral polygons, where res is the resolution of the plane.
        These point values are guaranteed to be up-to-date when either
        the interaction_event or end_interaction events are invoked. The
        user provides the PolyData and the points and polygons are
        added to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_reslice(self):
        return wrap_vtk(self._vtk_obj.GetReslice())
    reslice = traits.Property(_get_reslice, help=\
        """
        Get the current reslice class and reslice axes
        """
    )

    def _get_reslice_axes(self):
        return wrap_vtk(self._vtk_obj.GetResliceAxes())
    reslice_axes = traits.Property(_get_reslice_axes, help=\
        """
        Get the current reslice class and reslice axes
        """
    )

    def _get_reslice_output(self):
        return wrap_vtk(self._vtk_obj.GetResliceOutput())
    reslice_output = traits.Property(_get_reslice_output, help=\
        """
        Convenience method to get the ImageReslice output.
        """
    )

    def _get_texture(self):
        return wrap_vtk(self._vtk_obj.GetTexture())
    texture = traits.Property(_get_texture, help=\
        """
        Convenience method to get the texture used by this widget.  This
        can be used in external slice viewers.
        """
    )

    def get_vector1(self, *args):
        """
        V.get_vector1([float, float, float])
        C++: void GetVector1(double v1[3])
        Get the vector from the plane origin to point1.
        """
        ret = self._wrap_call(self._vtk_obj.GetVector1, *args)
        return ret

    def get_vector2(self, *args):
        """
        V.get_vector2([float, float, float])
        C++: void GetVector2(double v2[3])
        Get the vector from the plane origin to point2.
        """
        ret = self._wrap_call(self._vtk_obj.GetVector2, *args)
        return ret

    def _get_window(self):
        return self._vtk_obj.GetWindow()
    window = traits.Property(_get_window, help=\
        """
        Set/Get the current window and level values.  set_window_level
        should only be called after set_input.  If a shared lookup table
        is being used, a callback is required to update the window level
        values without having to update the lookup table again.
        """
    )

    def set_input(self, *args):
        """
        V.set_input(DataSet)
        C++: void SetInput(DataSet *input)
        Set the ImageData* input for the ImageReslice.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def set_picker(self, *args):
        """
        V.set_picker(AbstractPropPicker)
        C++: void SetPicker(AbstractPropPicker *)
        Set the internal picker to one defined by the user.  In this way,
        a set of three orthogonal planes can share the same picker so
        that picking is performed correctly.  The default internal picker
        can be re-set/allocated by setting to 0 (NULL).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPicker, *my_args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('user_controlled_lookup_table',
    'GetUserControlledLookupTable'), ('slice_index', 'GetSliceIndex'),
    ('handle_size', 'GetHandleSize'), ('restrict_plane_to_volume',
    'GetRestrictPlaneToVolume'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('texture_visibility',
    'GetTextureVisibility'), ('debug', 'GetDebug'), ('margin_size_x',
    'GetMarginSizeX'), ('margin_size_y', 'GetMarginSizeY'),
    ('right_button_action', 'GetRightButtonAction'), ('plane_orientation',
    'GetPlaneOrientation'), ('place_factor', 'GetPlaceFactor'),
    ('texture_interpolate', 'GetTextureInterpolate'),
    ('key_press_activation', 'GetKeyPressActivation'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('display_text', 'GetDisplayText'), ('slice_position',
    'GetSlicePosition'), ('interaction', 'GetInteraction'),
    ('left_button_auto_modifier', 'GetLeftButtonAutoModifier'),
    ('right_button_auto_modifier', 'GetRightButtonAutoModifier'),
    ('middle_button_auto_modifier', 'GetMiddleButtonAutoModifier'),
    ('enabled', 'GetEnabled'), ('middle_button_action',
    'GetMiddleButtonAction'), ('priority', 'GetPriority'), ('point1',
    'GetPoint1'), ('point2', 'GetPoint2'), ('use_continuous_cursor',
    'GetUseContinuousCursor'), ('reslice_interpolate',
    'GetResliceInterpolate'), ('reference_count', 'GetReferenceCount'),
    ('left_button_action', 'GetLeftButtonAction'))
    
    _full_traitnames_list_ = \
    (['debug', 'display_text', 'enabled', 'global_warning_display',
    'interaction', 'key_press_activation', 'restrict_plane_to_volume',
    'texture_interpolate', 'texture_visibility', 'use_continuous_cursor',
    'user_controlled_lookup_table', 'plane_orientation',
    'reslice_interpolate', 'handle_size', 'key_press_activation_value',
    'left_button_action', 'left_button_auto_modifier', 'margin_size_x',
    'margin_size_y', 'middle_button_action',
    'middle_button_auto_modifier', 'origin', 'place_factor', 'point1',
    'point2', 'priority', 'right_button_action',
    'right_button_auto_modifier', 'slice_index', 'slice_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImagePlaneWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImagePlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['display_text', 'enabled', 'interaction',
            'key_press_activation', 'restrict_plane_to_volume',
            'texture_interpolate', 'texture_visibility', 'use_continuous_cursor',
            'user_controlled_lookup_table'], ['plane_orientation',
            'reslice_interpolate'], ['handle_size', 'key_press_activation_value',
            'left_button_action', 'left_button_auto_modifier', 'margin_size_x',
            'margin_size_y', 'middle_button_action',
            'middle_button_auto_modifier', 'origin', 'place_factor', 'point1',
            'point2', 'priority', 'right_button_action',
            'right_button_auto_modifier', 'slice_index', 'slice_position']),
            title='Edit ImagePlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImagePlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

