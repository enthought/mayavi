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

from tvtk.tvtk_classes.three_d_widget import ThreeDWidget


class ImageTracerWidget(ThreeDWidget):
    """
    ImageTracerWidget - 3d widget for tracing on planar props.
    
    Superclass: ThreeDWidget
    
    ImageTracerWidget is different from other widgets in three
    distinct ways:
    1) any sub-class of Prop can be input rather than just Prop3D,
       so that ImageActor can be set as the prop and then traced over,
    2) the widget fires pick events at the input prop to decide where to
       move its handles, 3) the widget has 2d glyphs for handles instead
       of 3d spheres as is done in other sub-classes of ThreeDWidget. This
    widget is primarily designed for manually tracing over image data.
       The button actions and key modifiers are as follows for
       controlling the widget:
    1) left button click over the image, hold and drag draws a free hand
       line.
    2) left button click and release erases the widget line, if it
       exists, and repositions the first handle.
    3) middle button click starts a snap drawn line.  The line is
       terminated by clicking the middle button while depressing the ctrl
    key.
    4) when tracing a continuous or snap drawn line, if the last cursor
       position is within a specified tolerance to the first handle, the
       widget line will form a closed loop.
    5) right button clicking and holding on any handle that is part of a
       snap drawn line allows handle dragging: existing line segments are
    updated accordingly.  If the path is open and auto_close is set to On,
    the path can be closed by repositioning the first and last points
       over one another.
    6) ctrl key + right button down on any handle will erase it: existing
       snap drawn line segments are updated accordingly.  If the line was
    formed by continous tracing, the line is deleted leaving one handle.
    7) shift key + right button down on any snap drawn line segment will
       insert a handle at the cursor position.  The line segment is split
    accordingly.
    
    Caveats:
    
    the input DataSet should be ImageData.
    
    See Also:
    
    ThreeDWidget BoxWidget LineWidget PointWidget SphereWidget
    ImagePlaneWidget ImplicitPlaneWidget PlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageTracerWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(ImageTracerWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    interaction = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable mouse interaction when the widget is visible.
        """
    )
    def _interaction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteraction,
                        self.interaction_)

    handle_middle_mouse_button = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable mouse button events
        """
    )
    def _handle_middle_mouse_button_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleMiddleMouseButton,
                        self.handle_middle_mouse_button_)

    handle_left_mouse_button = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable mouse button events
        """
    )
    def _handle_left_mouse_button_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleLeftMouseButton,
                        self.handle_left_mouse_button_)

    project_to_plane = tvtk_base.false_bool_trait(help=\
        """
        Force handles to be on a specific ortho plane. Default is Off.
        """
    )
    def _project_to_plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectToPlane,
                        self.project_to_plane_)

    snap_to_image = tvtk_base.false_bool_trait(help=\
        """
        Force snapping to image data while tracing. Default is Off.
        """
    )
    def _snap_to_image_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSnapToImage,
                        self.snap_to_image_)

    handle_right_mouse_button = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable mouse button events
        """
    )
    def _handle_right_mouse_button_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleRightMouseButton,
                        self.handle_right_mouse_button_)

    auto_close = tvtk_base.false_bool_trait(help=\
        """
        In concert with a capture_radius value, automatically form a
        closed path by connecting first to last path points. Default is
        Off.
        """
    )
    def _auto_close_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoClose,
                        self.auto_close_)

    projection_normal = traits.Trait('z_axes',
    tvtk_base.TraitRevPrefixMap({'z_axes': 2, 'y_axes': 1, 'x_axes': 0}), help=\
        """
        Set the projection normal.  The normal in set_projection_normal is
        0,1,2 for YZ,XZ,XY planes respectively.  Since the handles are 2d
        glyphs, it is necessary to specify a plane on which to generate
        them, even though project_to_plane may be turned off.
        """
    )
    def _projection_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionNormal,
                        self.projection_normal_)

    def get_handle_position(self, *args):
        """
        V.get_handle_position(int, [float, float, float])
        C++: void GetHandlePosition(int handle, double xyz[3])
        V.get_handle_position(int) -> (float, float, float)
        C++: double *GetHandlePosition(int handle)
        Set/Get the handle position in terms of a zero-based array of
        handles.
        """
        ret = self._wrap_call(self._vtk_obj.GetHandlePosition, *args)
        return ret

    def set_handle_position(self, *args):
        """
        V.set_handle_position(int, [float, float, float])
        C++: void SetHandlePosition(int handle, double xyz[3])
        V.set_handle_position(int, float, float, float)
        C++: void SetHandlePosition(int handle, double x, double y,
            double z)
        Set/Get the handle position in terms of a zero-based array of
        handles.
        """
        ret = self._wrap_call(self._vtk_obj.SetHandlePosition, *args)
        return ret

    def _get_selected_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedHandleProperty())
    def _set_selected_handle_property(self, arg):
        old_val = self._get_selected_handle_property()
        self._wrap_call(self._vtk_obj.SetSelectedHandleProperty,
                        deref_vtk(arg))
        self.trait_property_changed('selected_handle_property', old_val, arg)
    selected_handle_property = traits.Property(_get_selected_handle_property, _set_selected_handle_property, help=\
        """
        Set/Get the handle properties (the 2d glyphs are the handles).
        The properties of the handles when selected and normal can be
        manipulated.
        """
    )

    def _get_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetHandleProperty())
    def _set_handle_property(self, arg):
        old_val = self._get_handle_property()
        self._wrap_call(self._vtk_obj.SetHandleProperty,
                        deref_vtk(arg))
        self.trait_property_changed('handle_property', old_val, arg)
    handle_property = traits.Property(_get_handle_property, _set_handle_property, help=\
        """
        Set/Get the handle properties (the 2d glyphs are the handles).
        The properties of the handles when selected and normal can be
        manipulated.
        """
    )

    image_snap_type = traits.Trait(0, traits.Range(0, 1, enter_set=True, auto_set=False), help=\
        """
        Set/Get the type of snapping to image data: center of a
        pixel/voxel or nearest point defining a pixel/voxel.
        """
    )
    def _image_snap_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageSnapType,
                        self.image_snap_type)

    projection_position = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the position of the widgets' handles in terms of a plane's
        position. e.g., if projection_normal is 0, all of the x-coordinate
        values of the handles are set to projection_position.  No attempt
        is made to ensure that the position is within the bounds of
        either the underlying image data or the prop on which tracing is
        performed.
        """
    )
    def _projection_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionPosition,
                        self.projection_position)

    def _get_line_property(self):
        return wrap_vtk(self._vtk_obj.GetLineProperty())
    def _set_line_property(self, arg):
        old_val = self._get_line_property()
        self._wrap_call(self._vtk_obj.SetLineProperty,
                        deref_vtk(arg))
        self.trait_property_changed('line_property', old_val, arg)
    line_property = traits.Property(_get_line_property, _set_line_property, help=\
        """
        Set/Get the line properties. The properties of the line when
        selected and unselected can be manipulated.
        """
    )

    def _get_selected_line_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedLineProperty())
    def _set_selected_line_property(self, arg):
        old_val = self._get_selected_line_property()
        self._wrap_call(self._vtk_obj.SetSelectedLineProperty,
                        deref_vtk(arg))
        self.trait_property_changed('selected_line_property', old_val, arg)
    selected_line_property = traits.Property(_get_selected_line_property, _set_selected_line_property, help=\
        """
        Set/Get the line properties. The properties of the line when
        selected and unselected can be manipulated.
        """
    )

    capture_radius = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the capture radius for automatic path closing.  For image
        data, capture radius should be half the distance between
        voxel/pixel centers. Default is 1.0
        """
    )
    def _capture_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCaptureRadius,
                        self.capture_radius)

    def _get_glyph_source(self):
        return wrap_vtk(self._vtk_obj.GetGlyphSource())
    glyph_source = traits.Property(_get_glyph_source, help=\
        """
        Get the handles' geometric representation via GlyphSource2D.
        """
    )

    def _get_number_of_handles(self):
        return self._vtk_obj.GetNumberOfHandles()
    number_of_handles = traits.Property(_get_number_of_handles, help=\
        """
        Get the number of handles.
        """
    )

    def get_path(self, *args):
        """
        V.get_path(PolyData)
        C++: void GetPath(PolyData *pd)
        Grab the points and lines that define the traced path. These
        point values are guaranteed to be up-to-date when either the
        interaction_event or end_interaction events are invoked. The user
        provides the PolyData and the points and cells representing
        the line are added to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPath, *my_args)
        return ret

    def initialize_handles(self, *args):
        """
        V.initialize_handles(Points)
        C++: void InitializeHandles(Points *)
        Initialize the widget with a set of points and generate lines
        between them.  If auto_close is on it will handle the case wherein
        the first and last points are congruent.
        """
        my_args = deref_array(args, [['vtkPoints']])
        ret = self._wrap_call(self._vtk_obj.InitializeHandles, *my_args)
        return ret

    def is_closed(self):
        """
        V.is_closed() -> int
        C++: int IsClosed()
        Is the path closed or open?
        """
        ret = self._vtk_obj.IsClosed()
        return ret
        

    def set_prop(self, *args):
        """
        V.set_prop(Prop)
        C++: void SetProp(Prop *prop)
        @deprecated Replaced by ImageTracerWidget::SetViewProp() as of
        VTK 5.0.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetProp, *my_args)
        return ret

    def set_view_prop(self, *args):
        """
        V.set_view_prop(Prop)
        C++: void SetViewProp(Prop *prop)
        Set the prop, usually a ImageActor, to trace over.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetViewProp, *my_args)
        return ret

    _updateable_traits_ = \
    (('handle_right_mouse_button', 'GetHandleRightMouseButton'),
    ('interaction', 'GetInteraction'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('handle_size', 'GetHandleSize'),
    ('projection_normal', 'GetProjectionNormal'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('projection_position', 'GetProjectionPosition'), ('image_snap_type',
    'GetImageSnapType'), ('snap_to_image', 'GetSnapToImage'), ('enabled',
    'GetEnabled'), ('auto_close', 'GetAutoClose'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('project_to_plane',
    'GetProjectToPlane'), ('handle_middle_mouse_button',
    'GetHandleMiddleMouseButton'), ('capture_radius', 'GetCaptureRadius'),
    ('reference_count', 'GetReferenceCount'), ('place_factor',
    'GetPlaceFactor'), ('key_press_activation', 'GetKeyPressActivation'),
    ('handle_left_mouse_button', 'GetHandleLeftMouseButton'))
    
    _full_traitnames_list_ = \
    (['auto_close', 'debug', 'enabled', 'global_warning_display',
    'handle_left_mouse_button', 'handle_middle_mouse_button',
    'handle_right_mouse_button', 'interaction', 'key_press_activation',
    'project_to_plane', 'snap_to_image', 'projection_normal',
    'capture_radius', 'handle_size', 'image_snap_type',
    'key_press_activation_value', 'place_factor', 'priority',
    'projection_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageTracerWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageTracerWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_close', 'enabled', 'handle_left_mouse_button',
            'handle_middle_mouse_button', 'handle_right_mouse_button',
            'interaction', 'key_press_activation', 'project_to_plane',
            'snap_to_image'], ['projection_normal'], ['capture_radius',
            'handle_size', 'image_snap_type', 'key_press_activation_value',
            'place_factor', 'priority', 'projection_position']),
            title='Edit ImageTracerWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageTracerWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

