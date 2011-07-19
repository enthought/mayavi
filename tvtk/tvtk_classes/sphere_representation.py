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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class SphereRepresentation(WidgetRepresentation):
    """
    SphereRepresentation - a class defining the representation for the
    SphereWidget2
    
    Superclass: WidgetRepresentation
    
    This class is a concrete representation for the SphereWidget2. It
    represents a sphere with an optional handle.  Through interaction
    with the widget, the sphere can be arbitrarily positioned and scaled
    in 3d space; and the handle can be moved on the surface of the
    sphere. Typically the SphereWidget2/vtkSphereRepresentation are
    used to position a sphere for the purpose of extracting, cutting or
    clipping data; or the handle is moved on the sphere to position a
    light or camera.
    
    To use this representation, you normally use the place_widget() method
    to position the widget at a specified region in space. It is also
    possible to set the center of the sphere, a radius, and/or a handle
    position.
    
    Caveats:
    
    Note that the representation is overconstrained in that the center
    and radius of the sphere can be defined, this information plus the
    handle direction defines the geometry of the representation.
    Alternatively, the user may specify the center of the sphere plus the
    handle position.
    
    This class, and SphereWidget2, are second generation VTK widgets.
    An earlier version of this functionality was defined in the class
    SphereWidget.
    
    See Also:
    
    SphereWidget2 SphereWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSphereRepresentation, obj, update, **traits)
    
    radial_line = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable a radial line segment that joins the center of the
        outer sphere and the handle.
        """
    )
    def _radial_line_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialLine,
                        self.radial_line_)

    handle_visibility = tvtk_base.false_bool_trait(help=\
        """
        The handle sits on the surface of the sphere and may be moved
        around the surface by picking (left mouse) and then moving. The
        position of the handle can be retrieved, this is useful for
        positioning cameras and lights. By default, the handle is turned
        off.
        """
    )
    def _handle_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleVisibility,
                        self.handle_visibility_)

    handle_text = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable a label that displays the location of the handle
        in spherical coordinates (radius,theta,phi). The two angles,
        theta and phi, are displayed in degrees. Note that phi is
        measured from the north pole down towards the equator; and theta
        is the angle around the north/south axis.
        """
    )
    def _handle_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleText,
                        self.handle_text_)

    representation = traits.Trait('wireframe',
    tvtk_base.TraitRevPrefixMap({'wireframe': 1, 'off': 0, 'surface': 2}), help=\
        """
        Set the representation (i.e., appearance) of the sphere.
        Different representations are useful depending on the
        application.
        """
    )
    def _representation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepresentation,
                        self.representation_)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the center position of the sphere. Note that this may
        adjust the direction from the handle to the center, as well as
        the radius of the sphere.
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    handle_direction = traits.Array(shape=(3,), value=(1.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the direction vector of the handle relative to the center
        of the sphere. This may affect the position of the handle and the
        radius of the sphere.
        """
    )
    def _handle_direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleDirection,
                        self.handle_direction)

    phi_resolution = traits.Int(8, enter_set=True, auto_set=False, help=\
        """
        Set/Get the resolution of the sphere in the phi direction.
        """
    )
    def _phi_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiResolution,
                        self.phi_resolution)

    radius = traits.Float(0.25, enter_set=True, auto_set=False, help=\
        """
        Set/Get the radius of sphere. Default is 0.5. Note that this may
        modify the position of the handle based on the handle direction.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    theta_resolution = traits.Int(16, enter_set=True, auto_set=False, help=\
        """
        Set/Get the resolution of the sphere in the theta direction.
        """
    )
    def _theta_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaResolution,
                        self.theta_resolution)

    handle_position = traits.Array(shape=(3,), value=(0.25, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the position of the handle. Note that this may adjust the
        radius of the sphere and the handle direction.
        """
    )
    def _handle_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandlePosition,
                        self.handle_position)

    def _get_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetHandleProperty())
    handle_property = traits.Property(_get_handle_property, help=\
        """
        Get the handle properties (the little ball on the sphere is the
        handle). The properties of the handle when selected and
        unselected can be  manipulated.
        """
    )

    def _get_handle_text_property(self):
        return wrap_vtk(self._vtk_obj.GetHandleTextProperty())
    handle_text_property = traits.Property(_get_handle_text_property, help=\
        """
        Get the handle text property. This can be used to control the
        appearance of the handle text.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata (including points) that defines the sphere. 
        The polydata consists of n+1 points, where n is the resolution of
        the sphere. These point values are guaranteed to be up-to-date
        when either the interaction_event or end_interaction events are
        invoked. The user provides the PolyData and the points and
        polysphere are added to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_radial_line_property(self):
        return wrap_vtk(self._vtk_obj.GetRadialLineProperty())
    radial_line_property = traits.Property(_get_radial_line_property, help=\
        """
        Get the property of the radial line. This can be used to control
        the appearance of the optional line connecting the center to the
        handle.
        """
    )

    def _get_selected_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedHandleProperty())
    selected_handle_property = traits.Property(_get_selected_handle_property, help=\
        """
        Get the handle properties (the little ball on the sphere is the
        handle). The properties of the handle when selected and
        unselected can be  manipulated.
        """
    )

    def _get_selected_sphere_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedSphereProperty())
    selected_sphere_property = traits.Property(_get_selected_sphere_property, help=\
        """
        Get the sphere properties. The properties of the sphere when
        selected and unselected can be manipulated.
        """
    )

    def get_sphere(self, *args):
        """
        V.get_sphere(Sphere)
        C++: void GetSphere(Sphere *sphere)
        Get the spherical implicit function defined by this widget.  Note
        that Sphere is a subclass of ImplicitFunction, meaning that
        it can be used by a variety of filters to perform clipping,
        cutting, and selection of data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetSphere, *my_args)
        return ret

    def _get_sphere_property(self):
        return wrap_vtk(self._vtk_obj.GetSphereProperty())
    sphere_property = traits.Property(_get_sphere_property, help=\
        """
        Get the sphere properties. The properties of the sphere when
        selected and unselected can be manipulated.
        """
    )

    def place_widget(self, *args):
        """
        V.place_widget([float, float, float, float, float, float])
        C++: virtual void PlaceWidget(double bounds[6])
        V.place_widget([float, float, float], [float, float, float])
        C++: virtual void PlaceWidget(double center[3],
            double handlePosition[3])
        These are methods that satisfy WidgetRepresentation's API.
        Note that a version of place widget is available where the center
        and handle position are specified.
        """
        ret = self._wrap_call(self._vtk_obj.PlaceWidget, *args)
        return ret

    def set_interaction_state(self, *args):
        """
        V.set_interaction_state(int)
        C++: void SetInteractionState(int state)
        The interaction state may be set from a widget (e.g.,
        SphereWidget2) or other object. This controls how the
        interaction with the widget proceeds. Normally this method is
        used as part of a handshaking process with the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
        ret = self._wrap_call(self._vtk_obj.SetInteractionState, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('handle_position', 'GetHandlePosition'),
    ('need_to_render', 'GetNeedToRender'), ('dragable', 'GetDragable'),
    ('visibility', 'GetVisibility'), ('theta_resolution',
    'GetThetaResolution'), ('radius', 'GetRadius'), ('radial_line',
    'GetRadialLine'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('place_factor', 'GetPlaceFactor'),
    ('use_bounds', 'GetUseBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('handle_visibility',
    'GetHandleVisibility'), ('center', 'GetCenter'),
    ('estimated_render_time', 'GetEstimatedRenderTime'), ('debug',
    'GetDebug'), ('representation', 'GetRepresentation'),
    ('handle_direction', 'GetHandleDirection'), ('handle_text',
    'GetHandleText'), ('reference_count', 'GetReferenceCount'),
    ('phi_resolution', 'GetPhiResolution'), ('pickable', 'GetPickable'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'handle_text',
    'handle_visibility', 'need_to_render', 'pickable', 'radial_line',
    'use_bounds', 'visibility', 'representation', 'allocated_render_time',
    'center', 'estimated_render_time', 'handle_direction',
    'handle_position', 'handle_size', 'phi_resolution', 'place_factor',
    'radius', 'render_time_multiplier', 'theta_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SphereRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SphereRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['handle_text', 'handle_visibility', 'need_to_render',
            'radial_line', 'use_bounds', 'visibility'], ['representation'],
            ['allocated_render_time', 'center', 'estimated_render_time',
            'handle_direction', 'handle_position', 'handle_size',
            'phi_resolution', 'place_factor', 'radius', 'render_time_multiplier',
            'theta_resolution']),
            title='Edit SphereRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SphereRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

