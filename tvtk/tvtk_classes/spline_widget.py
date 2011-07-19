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


class SplineWidget(ThreeDWidget):
    """
    SplineWidget - 3d widget for manipulating a spline
    
    Superclass: ThreeDWidget
    
    This 3d widget defines a spline that can be interactively placed in a
    scene. The spline has handles, the number of which can be changed,
    plus it can be picked on the spline itself to translate or rotate it
    in the scene. A nice feature of the object is that the
    SplineWidget, like any 3d widget, will work with the current
    interactor style. That is, if SplineWidget does not handle an
    event, then all other registered observers (including the interactor
    style) have an opportunity to process the event. Otherwise, the
    SplineWidget will terminate the processing of the event that it
    handles.
    
    To use this object, just invoke set_interactor() with the argument of
    the method a RenderWindowInteractor.  You may also wish to invoke
    "_place_widget()" to initially position the widget. The interactor will
    act normally until the "i" key (for "interactor") is pressed, at
    which point the SplineWidget will appear. (See superclass
    documentation for information about changing this behavior.) Events
    that occur outside of the widget (i.e., no part of the widget is
    picked) are propagated to any other registered obsevers (such as the
    interaction style).  Turn off the widget by pressing the "i" key
    again (or invoke the Off() method).
    
    The button actions and key modifiers are as follows for controlling
    the widget:
    1) left button down on and drag one of the spherical handles to
       change the shape of the spline: the handles act as "control
       points".
    2) left button or middle button down on a line segment forming the
       spline allows uniform translation of the widget.
    3) ctrl + middle button down on the widget enables spinning of the
       widget about its center.
    4) right button down on the widget enables scaling of the widget. By
       moving the mouse "up" the render window the spline will be made
       bigger; by moving "down" the render window the widget will be made
    smaller.
    5) ctrl key + right button down on any handle will erase it providing
    there will be two or more points remaining to form a spline.
    6) shift key + right button down on any line segment will insert a
       handle onto the spline at the cursor position.
    
    The SplineWidget has several methods that can be used in
    conjunction with other VTK objects. The set/_get_resolution() methods
    control the number of subdivisions of the spline; the get_poly_data()
    method can be used to get the polygonal representation and can be
    used for things like seeding streamlines or probing other data sets.
    Typical usage of the widget is to make use of the
    start_interaction_event, interaction_event, and end_interaction_event
    events. The interaction_event is called on mouse motion; the other two
    events are called on button down and button up (either left or right
    button).
    
    Some additional features of this class include the ability to control
    the properties of the widget. You can set the properties of the
    selected and unselected representations of the spline. For example,
    you can set the property for the handles and spline. In addition
    there are methods to constrain the spline so that it is aligned with
    a plane.  Note that a simple ruler widget can be derived by setting
    the resolution to 1, the number of handles to 2, and calling the
    get_summed_length method!
    
    Caveats:
    
    Note that handles and line can be picked even when they are "behind"
    other actors.  This is an intended feature and not a bug.
    
    See Also:
    
    ThreeDWidget BoxWidget LineWidget PointWidget SphereWidget
    ImagePlaneWidget ImplicitPlaneWidget PlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSplineWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(SplineWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    process_events = tvtk_base.true_bool_trait(help=\
        """
        Turn on / off event processing for this widget. If off, the
        widget will not respond to user interaction
        """
    )
    def _process_events_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProcessEvents,
                        self.process_events_)

    project_to_plane = tvtk_base.false_bool_trait(help=\
        """
        Force the spline widget to be projected onto one of the
        orthogonal planes. Remember that when the state changes, a
        modified_event is invoked. This can be used to snap the spline to
        the plane if it is orginally not aligned.  The normal in
        set_projection_normal is 0,1,2 for YZ,XZ,XY planes respectively and
        3 for arbitrary oblique planes when the widget is tied to a
        PlaneSource.
        """
    )
    def _project_to_plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectToPlane,
                        self.project_to_plane_)

    closed = tvtk_base.false_bool_trait(help=\
        """
        Control whether the spline is open or closed. A closed spline
        forms a continuous loop: the first and last points are the same,
        and derivatives are continuous.  A minimum of 3 handles are
        required to form a closed loop.  This method enforces consistency
        with user supplied subclasses of Spline.
        """
    )
    def _closed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClosed,
                        self.closed_)

    projection_normal = traits.Trait('x_axes',
    tvtk_base.TraitRevPrefixMap({'z_axes': 2, 'oblique': 3, 'y_axes': 1, 'x_axes': 0}), help=\
        """
        
        """
    )
    def _projection_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionNormal,
                        self.projection_normal_)

    def _get_parametric_spline(self):
        return wrap_vtk(self._vtk_obj.GetParametricSpline())
    def _set_parametric_spline(self, arg):
        old_val = self._get_parametric_spline()
        self._wrap_call(self._vtk_obj.SetParametricSpline,
                        deref_vtk(arg))
        self.trait_property_changed('parametric_spline', old_val, arg)
    parametric_spline = traits.Property(_get_parametric_spline, _set_parametric_spline, help=\
        """
        Set the parametric spline object. Through ParametricSpline's
        API, the user can supply and configure one of currently two types
        of spline: CardinalSpline, KochanekSpline. The widget
        controls the open or closed configuration of the spline. WARNING:
        The widget does not enforce internal consistency so that all
        three are of the same type.
        """
    )

    def get_handle_position(self, *args):
        """
        V.get_handle_position(int, [float, float, float])
        C++: void GetHandlePosition(int handle, double xyz[3])
        V.get_handle_position(int) -> (float, float, float)
        C++: double *GetHandlePosition(int handle)
        Set/Get the position of the spline handles. Call
        get_number_of_handles to determine the valid range of handle
        indices.
        """
        ret = self._wrap_call(self._vtk_obj.GetHandlePosition, *args)
        return ret

    def set_handle_position(self, *args):
        """
        V.set_handle_position(int, float, float, float)
        C++: void SetHandlePosition(int handle, double x, double y,
            double z)
        V.set_handle_position(int, [float, float, float])
        C++: void SetHandlePosition(int handle, double xyz[3])
        Set/Get the position of the spline handles. Call
        get_number_of_handles to determine the valid range of handle
        indices.
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
        Set/Get the handle properties (the spheres are the handles). The
        properties of the handles when selected and unselected can be
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
        Set/Get the handle properties (the spheres are the handles). The
        properties of the handles when selected and unselected can be
        manipulated.
        """
    )

    projection_position = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the position of spline handles and points in terms of a
        plane's position. i.e., if projection_normal is 0, all of the
        x-coordinate values of the points are set to position. Any value
        can be passed (and is ignored) to update the spline points when
        Projection normal is set to 3 for arbritrary plane orientations.
        """
    )
    def _projection_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionPosition,
                        self.projection_position)

    number_of_handles = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of handles for this widget.
        """
    )
    def _number_of_handles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfHandles,
                        self.number_of_handles)

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

    resolution = traits.Int(499, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of line segments representing the spline for
        this widget.
        """
    )
    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata (including points) that defines the spline. 
        The polydata consists of points and line segments numbering
        Resolution + 1 and Resoltuion, respectively. Points are
        guaranteed to be up-to-date when either the interaction_event or 
        end_interaction events are invoked. The user provides the
        PolyData and the points and polyline are added to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_process_events_max_value(self):
        return self._vtk_obj.GetProcessEventsMaxValue()
    process_events_max_value = traits.Property(_get_process_events_max_value, help=\
        """
        Turn on / off event processing for this widget. If off, the
        widget will not respond to user interaction
        """
    )

    def _get_process_events_min_value(self):
        return self._vtk_obj.GetProcessEventsMinValue()
    process_events_min_value = traits.Property(_get_process_events_min_value, help=\
        """
        Turn on / off event processing for this widget. If off, the
        widget will not respond to user interaction
        """
    )

    def _get_summed_length(self):
        return self._vtk_obj.GetSummedLength()
    summed_length = traits.Property(_get_summed_length, help=\
        """
        Get the approximate vs. the true arc length of the spline.
        Calculated as the summed lengths of the individual straight line
        segments. Use set_resolution to control the accuracy.
        """
    )

    def initialize_handles(self, *args):
        """
        V.initialize_handles(Points)
        C++: void InitializeHandles(Points *points)
        Convenience method to allocate and set the handles from a
        Points instance.  If the first and last points are the same,
        the spline sets Closed to the on state and disregards the last
        point, otherwise Closed remains unchanged.
        """
        my_args = deref_array(args, [['vtkPoints']])
        ret = self._wrap_call(self._vtk_obj.InitializeHandles, *my_args)
        return ret

    def is_closed(self):
        """
        V.is_closed() -> int
        C++: int IsClosed()
        Convenience method to determine whether the spline is closed in a
        geometric sense.  The widget may be set "closed" but still be
        geometrically open (e.g., a straight line).
        """
        ret = self._vtk_obj.IsClosed()
        return ret
        

    def set_plane_source(self, *args):
        """
        V.set_plane_source(PlaneSource)
        C++: void SetPlaneSource(PlaneSource *plane)
        Set up a reference to a PlaneSource that could be from another
        widget object, e.g. a PolyDataSourceWidget.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlaneSource, *my_args)
        return ret

    _updateable_traits_ = \
    (('priority', 'GetPriority'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('handle_size', 'GetHandleSize'),
    ('projection_normal', 'GetProjectionNormal'), ('projection_position',
    'GetProjectionPosition'), ('key_press_activation',
    'GetKeyPressActivation'), ('enabled', 'GetEnabled'),
    ('number_of_handles', 'GetNumberOfHandles'), ('debug', 'GetDebug'),
    ('project_to_plane', 'GetProjectToPlane'), ('closed', 'GetClosed'),
    ('reference_count', 'GetReferenceCount'), ('place_factor',
    'GetPlaceFactor'), ('process_events', 'GetProcessEvents'),
    ('resolution', 'GetResolution'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['closed', 'debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'process_events', 'project_to_plane',
    'projection_normal', 'handle_size', 'key_press_activation_value',
    'number_of_handles', 'place_factor', 'priority',
    'projection_position', 'resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SplineWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SplineWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['closed', 'enabled', 'key_press_activation',
            'process_events', 'project_to_plane'], ['projection_normal'],
            ['handle_size', 'key_press_activation_value', 'number_of_handles',
            'place_factor', 'priority', 'projection_position', 'resolution']),
            title='Edit SplineWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SplineWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

