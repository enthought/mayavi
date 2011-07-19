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


class SphereWidget(ThreeDWidget):
    """
    SphereWidget - 3d widget for manipulating a sphere
    
    Superclass: ThreeDWidget
    
    This 3d widget defines a sphere that can be interactively placed in a
    scene.
    
    To use this object, just invoke set_interactor() with the argument of
    the method a RenderWindowInteractor.  You may also wish to invoke
    "_place_widget()" to initially position the widget. The interactor will
    act normally until the "i" key (for "interactor") is pressed, at
    which point the SphereWidget will appear. (See superclass
    documentation for information about changing this behavior.) Events
    that occur outside of the widget (i.e., no part of the widget is
    picked) are propagated to any other registered obsevers (such as the
    interaction style).  Turn off the widget by pressing the "i" key
    again (or invoke the Off() method).
    
    The SphereWidget has several methods that can be used in
    conjunction with other VTK objects. The set/_get_theta_resolution() and
    set/_get_phi_resolution() methods control the number of subdivisions of
    the sphere in the theta and phi directions; the get_poly_data() method
    can be used to get the polygonal representation and can be used for
    things like seeding streamlines. The get_sphere() method returns a
    sphere implicit function that can be used for cutting and clipping.
    Typical usage of the widget is to make use of the
    start_interaction_event, interaction_event, and end_interaction_event
    events. The interaction_event is called on mouse motion; the other two
    events are called on button down and button up (any mouse button).
    
    Some additional features of this class include the ability to control
    the properties of the widget. You can set the properties of the
    selected and unselected representations of the sphere.
    
    Caveats:
    
    Note that the sphere can be picked even when they are "behind" other
    actors.  This is an intended feature and not a bug.
    
    See Also:
    
    ThreeDWidget LineWidget BoxWidget PlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSphereWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(SphereWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
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

    scale = tvtk_base.true_bool_trait(help=\
        """
        Enable translation and scaling of the widget. By default, the
        widget can be translated and rotated.
        """
    )
    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale_)

    translation = tvtk_base.true_bool_trait(help=\
        """
        Enable translation and scaling of the widget. By default, the
        widget can be translated and rotated.
        """
    )
    def _translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslation,
                        self.translation_)

    representation = traits.Trait('wireframe',
    tvtk_base.TraitRevPrefixMap({'wireframe': 1, 'off': 0, 'surface': 2}), help=\
        """
        Set the representation of the sphere. Different representations
        are useful depending on the application. The default is
        VTK_SPHERE_WIREFRAME.
        """
    )
    def _representation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepresentation,
                        self.representation_)

    phi_resolution = traits.Int(8, enter_set=True, auto_set=False, help=\
        """
        Set/Get the resolution of the sphere in the Phi direction. The
        default is 8.
        """
    )
    def _phi_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiResolution,
                        self.phi_resolution)

    radius = traits.Float(0.25, enter_set=True, auto_set=False, help=\
        """
        Set/Get the radius of sphere. Default is .5.
        """
    )
    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    center = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the center of the sphere.
        """
    )
    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    handle_direction = traits.Array(shape=(3,), value=(1.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _handle_direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleDirection,
                        self.handle_direction)

    theta_resolution = traits.Int(16, enter_set=True, auto_set=False, help=\
        """
        Set/Get the resolution of the sphere in the Theta direction. The
        default is 16.
        """
    )
    def _theta_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaResolution,
                        self.theta_resolution)

    def _get_handle_position(self):
        return self._vtk_obj.GetHandlePosition()
    handle_position = traits.Property(_get_handle_position, help=\
        """
        
        """
    )

    def _get_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetHandleProperty())
    handle_property = traits.Property(_get_handle_property, help=\
        """
        Get the handle properties (the little ball on the sphere is the
        handle). The properties of the handle when selected and
        unselected can be  manipulated.
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

    _updateable_traits_ = \
    (('scale', 'GetScale'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('center', 'GetCenter'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('handle_direction', 'GetHandleDirection'),
    ('phi_resolution', 'GetPhiResolution'), ('priority', 'GetPriority'),
    ('theta_resolution', 'GetThetaResolution'), ('radius', 'GetRadius'),
    ('representation', 'GetRepresentation'), ('reference_count',
    'GetReferenceCount'), ('place_factor', 'GetPlaceFactor'),
    ('translation', 'GetTranslation'), ('handle_visibility',
    'GetHandleVisibility'), ('key_press_activation',
    'GetKeyPressActivation'), ('enabled', 'GetEnabled'), ('handle_size',
    'GetHandleSize'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display', 'handle_visibility',
    'key_press_activation', 'scale', 'translation', 'representation',
    'center', 'handle_direction', 'handle_size',
    'key_press_activation_value', 'phi_resolution', 'place_factor',
    'priority', 'radius', 'theta_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SphereWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SphereWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'handle_visibility',
            'key_press_activation', 'scale', 'translation'], ['representation'],
            ['center', 'handle_direction', 'handle_size',
            'key_press_activation_value', 'phi_resolution', 'place_factor',
            'priority', 'radius', 'theta_resolution']),
            title='Edit SphereWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SphereWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

