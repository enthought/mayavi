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


class PlaneWidget(PolyDataSourceWidget):
    """
    PlaneWidget - 3d widget for manipulating a finite plane
    
    Superclass: PolyDataSourceWidget
    
    This 3d widget defines a finite (bounded) plane that can be
    interactively placed in a scene. The plane has four handles (at its
    corner vertices), a normal vector, and the plane itself. The handles
    are used to resize the plane; the normal vector to rotate it, and the
    plane can be picked and translated. Selecting the plane while
    pressing CTRL makes it spin around the normal. A nice feature of the
    object is that the PlaneWidget, like any 3d widget, will work with
    the current interactor style. That is, if PlaneWidget does not
    handle an event, then all other registered observers (including the
    interactor style) have an opportunity to process the event.
    Otherwise, the PlaneWidget will terminate the processing of the
    event that it handles.
    
    To use this object, just invoke set_interactor() with the argument of
    the method a RenderWindowInteractor.  You may also wish to invoke
    "_place_widget()" to initially position the widget. If the "i" key (for
    "interactor") is pressed, the PlaneWidget will appear. (See
    superclass documentation for information about changing this
    behavior.) By grabbing the one of the four handles (use the left
    mouse button), the plane can be resized.  By grabbing the plane
    itself, the entire plane can be arbitrarily translated. Pressing CTRL
    while grabbing the plane will spin the plane around the normal. If
    you select the normal vector, the plane can be arbitrarily rotated.
    Selecting any part of the widget with the middle mouse button enables
    translation of the plane along its normal. (Once selected using
    middle mouse, moving the mouse in the direction of the normal
    translates the plane in the direction of the normal; moving in the
    direction opposite the normal translates the plane in the direction
    opposite the normal.) Scaling (about the center of the plane) is
    achieved by using the right mouse button. By moving the mouse "up"
    the render window the plane will be made bigger; by moving "down" the
    render window the widget will be made smaller. Events that occur
    outside of the widget (i.e., no part of the widget is picked) are
    propagated to any other registered obsevers (such as the interaction
    style).  Turn off the widget by pressing the "i" key again (or invoke
    the Off() method).
    
    The PlaneWidget has several methods that can be used in
    conjunction with other VTK objects. The set/_get_resolution() methods
    control the number of subdivisions of the plane; the get_poly_data()
    method can be used to get the polygonal representation and can be
    used for things like seeding stream lines. get_plane() can be used to
    update a Plane implicit function. Typical usage of the widget is
    to make use of the start_interaction_event, interaction_event, and
    end_interaction_event events. The interaction_event is called on mouse
    motion; the other two events are called on button down and button up
    (either left or right button).
    
    Some additional features of this class include the ability to control
    the properties of the widget. You can set the properties of the
    selected and unselected representations of the plane. For example,
    you can set the property for the handles and plane. In addition there
    are methods to constrain the plane so that it is perpendicular to the
    x-y-z axes.
    
    Caveats:
    
    Note that handles and plane can be picked even when they are "behind"
    other actors.  This is an intended feature and not a bug.
    
    See Also:
    
    ThreeDWidget BoxWidget LineWidget SphereWidget
    ImplicitPlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlaneWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(PlaneWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    normal_to_x_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        Remember that when the state changes, a modified_event is invoked.
        This can be used to snap the plane to the axes if it is orginally
        not aligned.
        """
    )
    def _normal_to_x_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToXAxis,
                        self.normal_to_x_axis_)

    normal_to_y_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        Remember that when the state changes, a modified_event is invoked.
        This can be used to snap the plane to the axes if it is orginally
        not aligned.
        """
    )
    def _normal_to_y_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToYAxis,
                        self.normal_to_y_axis_)

    normal_to_z_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        Remember that when the state changes, a modified_event is invoked.
        This can be used to snap the plane to the axes if it is orginally
        not aligned.
        """
    )
    def _normal_to_z_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToZAxis,
                        self.normal_to_z_axis_)

    representation = traits.Trait('wireframe',
    tvtk_base.TraitRevPrefixMap({'wireframe': 2, 'off': 0, 'outline': 1, 'surface': 3}), help=\
        """
        Control how the plane appears when get_poly_data() is invoked. If
        the mode is "outline", then just the outline of the plane is
        shown. If the mode is "wireframe" then the plane is drawn with
        the outline plus the interior mesh (corresponding to the
        resolution specified). If the mode is "surface" then the plane is
        drawn as a surface.
        """
    )
    def _representation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepresentation,
                        self.representation_)

    origin = traits.Array(shape=(3,), value=(-0.5, -0.5, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the origin of the plane.
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    def _get_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetPlaneProperty())
    def _set_plane_property(self, arg):
        old_val = self._get_plane_property()
        self._wrap_call(self._vtk_obj.SetPlaneProperty,
                        deref_vtk(arg))
        self.trait_property_changed('plane_property', old_val, arg)
    plane_property = traits.Property(_get_plane_property, _set_plane_property, help=\
        """
        Get the plane properties. The properties of the plane when
        selected and unselected can be manipulated.
        """
    )

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Get the center of the plane.
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    normal = traits.Array(shape=(3,), value=(0.0, 0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Get the normal to the plane.
        """
    )
    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    point1 = traits.Array(shape=(3,), value=(0.5, -0.5, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the position of the point defining the first axis of the
        plane.
        """
    )
    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(shape=(3,), value=(-0.5, 0.5, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the position of the point defining the second axis of the
        plane.
        """
    )
    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    resolution = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Set/Get the resolution (number of subdivisions) of the plane.
        """
    )
    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    def _get_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetHandleProperty())
    handle_property = traits.Property(_get_handle_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles when selected and normal can be
        manipulated.
        """
    )

    def get_plane(self, *args):
        """
        V.get_plane(Plane)
        C++: void GetPlane(Plane *plane)
        Get the planes describing the implicit function defined by the
        plane widget. The user must provide the instance of the class
        Plane. Note that Plane is a subclass of
        ImplicitFunction, meaning that it can be used by a variety of
        filters to perform clipping, cutting, and selection of data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlane, *my_args)
        return ret

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata (including points) that defines the plane.  The
        polydata consists of (res+1)*(res+1) points, and res*res
        quadrilateral polygons, where res is the resolution of the plane.
        These point values are guaranteed to be up-to-date when either
        the interaction_event or end_interaction events are invoked. The
        user provides the PolyData and the points and polyplane are
        added to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_selected_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedHandleProperty())
    selected_handle_property = traits.Property(_get_selected_handle_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles when selected and normal can be
        manipulated.
        """
    )

    def _get_selected_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedPlaneProperty())
    selected_plane_property = traits.Property(_get_selected_plane_property, help=\
        """
        Get the plane properties. The properties of the plane when
        selected and unselected can be manipulated.
        """
    )

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('normal_to_z_axis', 'GetNormalToZAxis'),
    ('representation', 'GetRepresentation'),
    ('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('center', 'GetCenter'), ('normal', 'GetNormal'),
    ('key_press_activation', 'GetKeyPressActivation'), ('enabled',
    'GetEnabled'), ('debug', 'GetDebug'), ('priority', 'GetPriority'),
    ('point1', 'GetPoint1'), ('point2', 'GetPoint2'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('normal_to_x_axis', 'GetNormalToXAxis'), ('normal_to_y_axis',
    'GetNormalToYAxis'), ('reference_count', 'GetReferenceCount'),
    ('place_factor', 'GetPlaceFactor'), ('resolution', 'GetResolution'),
    ('handle_size', 'GetHandleSize'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'normal_to_x_axis', 'normal_to_y_axis',
    'normal_to_z_axis', 'representation', 'center', 'handle_size',
    'key_press_activation_value', 'normal', 'origin', 'place_factor',
    'point1', 'point2', 'priority', 'resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlaneWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'normal_to_x_axis',
            'normal_to_y_axis', 'normal_to_z_axis'], ['representation'],
            ['center', 'handle_size', 'key_press_activation_value', 'normal',
            'origin', 'place_factor', 'point1', 'point2', 'priority',
            'resolution']),
            title='Edit PlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

