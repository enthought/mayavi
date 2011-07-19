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


class PointWidget(ThreeDWidget):
    """
    PointWidget - position a point in 3d space
    
    Superclass: ThreeDWidget
    
    This 3d widget allows the user to position a point in 3d space using
    a 3d cursor. The cursor has an outline bounding box, axes-aligned
    cross-hairs, and axes shadows. (The outline and shadows can be turned
    off.) Any of these can be turned off. A nice feature of the object is
    that the PointWidget, like any 3d widget, will work with the
    current interactor style. That is, if PointWidget does not handle
    an event, then all other registered observers (including the
    interactor style) have an opportunity to process the event.
    Otherwise, the PointWidget will terminate the processing of the
    event that it handles.
    
    To use this object, just invoke set_interactor() with the argument of
    the method a RenderWindowInteractor.  You may also wish to invoke
    "_place_widget()" to initially position the widget. The interactor will
    act normally until the "i" key (for "interactor") is pressed, at
    which point the PointWidget will appear. (See superclass
    documentation for information about changing this behavior.) To move
    the point, the user can grab (left mouse) on any widget line and
    "slide" the point into position. Scaling is achieved by using the
    right mouse button "up" the render window (makes the widget bigger)
    or "down" the render window (makes the widget smaller). To translate
    the widget use the middle mouse button. (Note: all of the translation
    interactions can be constrained to one of the x-y-z axes by using the
    "shift" key.) The PointWidget produces as output a polydata with a
    single point and a vertex cell.
    
    Some additional features of this class include the ability to control
    the rendered properties of the widget. You can set the properties of
    the selected and unselected representations of the parts of the
    widget. For example, you can set the property of the 3d cursor in its
    normal and selected states.
    
    Caveats:
    
    Note that widget can be picked even when it is "behind" other actors.
    This is an intended feature and not a bug.
    
    The constrained translation/sliding action (i.e., when the "shift"
    key is depressed) along the axes is based on a combination of a "hot"
    spot around the cursor focus plus the initial mouse motion after
    selection. That is, if the user selects an axis outside of the hot
    spot, then the motion is constrained along that axis. If the user
    selects the point widget near the focus (within the hot spot), the
    initial motion defines a vector which is compared to the x-y-z axes.
    The motion is constrained to the axis that is most parallel to the
    initial motion vector.
    
    See Also:
    
    ThreeDWidget LineWidget BoxWidget PlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(PointWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    y_shadows = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe y-shadows.
        """
    )
    def _y_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYShadows,
                        self.y_shadows_)

    translation_mode = tvtk_base.false_bool_trait(help=\
        """
        If translation mode is on, as the widget is moved the bounding
        box, shadows, and cursor are all translated simultaneously as the
        point moves.
        """
    )
    def _translation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationMode,
                        self.translation_mode_)

    z_shadows = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe z-shadows.
        """
    )
    def _z_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZShadows,
                        self.z_shadows_)

    outline = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe bounding box.
        """
    )
    def _outline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutline,
                        self.outline_)

    x_shadows = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe x-shadows.
        """
    )
    def _x_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXShadows,
                        self.x_shadows_)

    position = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the position of the point. Note that if the position is
        set outside of the bounding box, it will be clamped to the
        boundary of the bounding box.
        """
    )
    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    hot_spot_size = traits.Trait(0.05, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set the "hot spot" size; i.e., the region around the focus, in
        which the motion vector is used to control the constrained
        sliding action. Note the size is specified as a fraction of the
        length of the diagonal of the point widget's bounding box.
        """
    )
    def _hot_spot_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHotSpotSize,
                        self.hot_spot_size)

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata (including points) that defines the point. A
        single point and a vertex compose the PolyData.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    property = traits.Property(_get_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles when selected and normal can be set.
        """
    )

    def _get_selected_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedProperty())
    selected_property = traits.Property(_get_selected_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles when selected and normal can be set.
        """
    )

    def all_off(self):
        """
        V.all_off()
        C++: void AllOff()
        Convenience methods to turn outline and shadows on and off.
        """
        ret = self._vtk_obj.AllOff()
        return ret
        

    def all_on(self):
        """
        V.all_on()
        C++: void AllOn()
        Convenience methods to turn outline and shadows on and off.
        """
        ret = self._vtk_obj.AllOn()
        return ret
        

    _updateable_traits_ = \
    (('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('handle_size', 'GetHandleSize'), ('x_shadows', 'GetXShadows'),
    ('debug', 'GetDebug'), ('y_shadows', 'GetYShadows'), ('hot_spot_size',
    'GetHotSpotSize'), ('place_factor', 'GetPlaceFactor'),
    ('key_press_activation', 'GetKeyPressActivation'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('outline',
    'GetOutline'), ('z_shadows', 'GetZShadows'), ('enabled',
    'GetEnabled'), ('priority', 'GetPriority'), ('reference_count',
    'GetReferenceCount'), ('position', 'GetPosition'),
    ('translation_mode', 'GetTranslationMode'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'outline', 'translation_mode', 'x_shadows',
    'y_shadows', 'z_shadows', 'handle_size', 'hot_spot_size',
    'key_press_activation_value', 'place_factor', 'position', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PointWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'key_press_activation', 'outline',
            'translation_mode', 'x_shadows', 'y_shadows', 'z_shadows'], [],
            ['handle_size', 'hot_spot_size', 'key_press_activation_value',
            'place_factor', 'position', 'priority']),
            title='Edit PointWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

