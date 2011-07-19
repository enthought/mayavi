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


class BoxWidget(ThreeDWidget):
    """
    BoxWidget - orthogonal hexahedron 3d widget
    
    Superclass: ThreeDWidget
    
    This 3d widget defines a region of interest that is represented by an
    arbitrarily oriented hexahedron with interior face angles of 90
    degrees (orthogonal faces). The object creates 7 handles that can be
    moused on and manipulated. The first six correspond to the six faces,
    the seventh is in the center of the hexahedron. In addition, a
    bounding box outline is shown, the "faces" of which can be selected
    for object rotation or scaling. A nice feature of the object is that
    the BoxWidget, like any 3d widget, will work with the current
    interactor style. That is, if BoxWidget does not handle an event,
    then all other registered observers (including the interactor style)
    have an opportunity to process the event. Otherwise, the BoxWidget
    will terminate the processing of the event that it handles.
    
    To use this object, just invoke set_interactor() with the argument of
    the method a RenderWindowInteractor.  You may also wish to invoke
    "_place_widget()" to initially position the widget. The interactor will
    act normally until the "i" key (for "interactor") is pressed, at
    which point the BoxWidget will appear. (See superclass
    documentation for information about changing this behavior.) By
    grabbing the six face handles (use the left mouse button), faces can
    be moved. By grabbing the center handle (with the left mouse button),
    the entire hexahedron can be translated. (Translation can also be
    employed by using the "shift-left-mouse-button" combination inside of
    the widget.) Scaling is achieved by using the right mouse button "up"
    the render window (makes the widget bigger) or "down" the render
    window (makes the widget smaller). To rotate BoxWidget, pick a
    face (but not a face handle) and move the left mouse. (Note: the
    mouse button must be held down during manipulation.) Events that
    occur outside of the widget (i.e., no part of the widget is picked)
    are propagated to any other registered obsevers (such as the
    interaction style).  Turn off the widget by pressing the "i" key
    again. (See the superclass documentation on key press activiation.)
    
    The BoxWidget is very flexible. It can be used to select, cut,
    clip, or perform any other operation that depends on an implicit
    function (use the get_planes() method); or it can be used to transform
    objects using a linear transformation (use the get_transform()
    method). Typical usage of the widget is to make use of the
    start_interaction_event, interaction_event, and end_interaction_event
    events. The interaction_event is called on mouse motion; the other two
    events are called on button down and button up (either left or right
    button).
    
    Some additional features of this class include the ability to control
    the rendered properties of the widget. You can set the properties of
    the selected and unselected representations of the parts of the
    widget. For example, you can set the property for the handles, faces,
    and outline in their normal and selected states.
    
    Caveats:
    
    Note that handles can be picked even when they are "behind" other
    actors. This is an intended feature and not a bug.
    
    The box widget can be oriented by specifying a transformation matrix.
    This transformation is applied to the initial bounding box as defined
    by the place_widget() method. DO NOT ASSUME that the transformation is
    applied to a unit box centered at the origin; this is wrong!
    
    See Also:
    
    ThreeDWidget PointWidget LineWidget PlaneWidget
    ImplicitPlaneWidget ImagePlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBoxWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(BoxWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    inside_out = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the inside_out flag. When off, the normals point out of
        the box. When on, the normals point into the hexahedron. 
        inside_out is off by default.
        """
    )
    def _inside_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInsideOut,
                        self.inside_out_)

    outline_face_wires = tvtk_base.false_bool_trait(help=\
        """
        Control the representation of the outline. This flag enables face
        wires. By default face wires are off.
        """
    )
    def _outline_face_wires_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutlineFaceWires,
                        self.outline_face_wires_)

    rotation_enabled = tvtk_base.true_bool_trait(help=\
        """
        Control the behavior of the widget. Translation, rotation, and
        scaling can all be enabled and disabled.
        """
    )
    def _rotation_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationEnabled,
                        self.rotation_enabled_)

    scaling_enabled = tvtk_base.true_bool_trait(help=\
        """
        Control the behavior of the widget. Translation, rotation, and
        scaling can all be enabled and disabled.
        """
    )
    def _scaling_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalingEnabled,
                        self.scaling_enabled_)

    outline_cursor_wires = tvtk_base.true_bool_trait(help=\
        """
        Control the representation of the outline. This flag enables the
        cursor lines running between the handles. By default cursor wires
        are on.
        """
    )
    def _outline_cursor_wires_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutlineCursorWires,
                        self.outline_cursor_wires_)

    translation_enabled = tvtk_base.true_bool_trait(help=\
        """
        Control the behavior of the widget. Translation, rotation, and
        scaling can all be enabled and disabled.
        """
    )
    def _translation_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationEnabled,
                        self.translation_enabled_)

    def get_transform(self, *args):
        """
        V.get_transform(Transform)
        C++: virtual void GetTransform(Transform *t)
        Retrieve a linear transform characterizing the transformation of
        the box. Note that the transformation is relative to where
        place_widget was initially called. This method modifies the
        transform provided. The transform can be used to control the
        position of Prop3D's, as well as other transformation
        operations (e.g., TranformPolyData).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetTransform, *my_args)
        return ret

    def set_transform(self, *args):
        """
        V.set_transform(Transform)
        C++: virtual void SetTransform(Transform *t)
        Set the position, scale and orientation of the box widget using
        the transform specified. Note that the transformation is relative
        to where place_widget was initially called (i.e., the original
        bounding box).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTransform, *my_args)
        return ret

    def _get_face_property(self):
        return wrap_vtk(self._vtk_obj.GetFaceProperty())
    face_property = traits.Property(_get_face_property, help=\
        """
        Get the face properties (the faces of the box). The properties of
        the face when selected and normal can be set.
        """
    )

    def _get_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetHandleProperty())
    handle_property = traits.Property(_get_handle_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles when selected and normal can be set.
        """
    )

    def _get_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetOutlineProperty())
    outline_property = traits.Property(_get_outline_property, help=\
        """
        Get the outline properties (the outline of the box). The
        properties of the outline when selected and normal can be set.
        """
    )

    def get_planes(self, *args):
        """
        V.get_planes(Planes)
        C++: void GetPlanes(Planes *planes)
        Get the planes describing the implicit function defined by the
        box widget. The user must provide the instance of the class
        Planes. Note that Planes is a subclass of
        ImplicitFunction, meaning that it can be used by a variety of
        filters to perform clipping, cutting, and selection of data. 
        (The direction of the normals of the planes can be reversed
        enabling the inside_out flag.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlanes, *my_args)
        return ret

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata (including points) that define the box widget.
        The polydata consists of 6 quadrilateral faces and 15 points. The
        first eight points define the eight corner vertices; the next six
        define the
        -x,+x, -y,+y, -z,+z face points; and the final point (the 15th
            out of 15 points) defines the center of the hexahedron. These
        point values are guaranteed to be up-to-date when either the
            interaction_event or end_interaction_event events are invoked.
            The user provides the PolyData and the points and cells
            are added to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_selected_face_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedFaceProperty())
    selected_face_property = traits.Property(_get_selected_face_property, help=\
        """
        Get the face properties (the faces of the box). The properties of
        the face when selected and normal can be set.
        """
    )

    def _get_selected_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedHandleProperty())
    selected_handle_property = traits.Property(_get_selected_handle_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles when selected and normal can be set.
        """
    )

    def _get_selected_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedOutlineProperty())
    selected_outline_property = traits.Property(_get_selected_outline_property, help=\
        """
        Get the outline properties (the outline of the box). The
        properties of the outline when selected and normal can be set.
        """
    )

    def handles_off(self):
        """
        V.handles_off()
        C++: void HandlesOff()
        Switches handles (the spheres) on or off by manipulating the
        actor visibility.
        """
        ret = self._vtk_obj.HandlesOff()
        return ret
        

    def handles_on(self):
        """
        V.handles_on()
        C++: void HandlesOn()
        Switches handles (the spheres) on or off by manipulating the
        actor visibility.
        """
        ret = self._vtk_obj.HandlesOn()
        return ret
        

    _updateable_traits_ = \
    (('rotation_enabled', 'GetRotationEnabled'),
    ('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('handle_size', 'GetHandleSize'), ('outline_cursor_wires',
    'GetOutlineCursorWires'), ('enabled', 'GetEnabled'),
    ('translation_enabled', 'GetTranslationEnabled'), ('priority',
    'GetPriority'), ('debug', 'GetDebug'), ('inside_out', 'GetInsideOut'),
    ('scaling_enabled', 'GetScalingEnabled'), ('reference_count',
    'GetReferenceCount'), ('place_factor', 'GetPlaceFactor'),
    ('outline_face_wires', 'GetOutlineFaceWires'),
    ('key_press_activation', 'GetKeyPressActivation'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display', 'inside_out',
    'key_press_activation', 'outline_cursor_wires', 'outline_face_wires',
    'rotation_enabled', 'scaling_enabled', 'translation_enabled',
    'handle_size', 'key_press_activation_value', 'place_factor',
    'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BoxWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BoxWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['enabled', 'inside_out', 'key_press_activation',
            'outline_cursor_wires', 'outline_face_wires', 'rotation_enabled',
            'scaling_enabled', 'translation_enabled'], [], ['handle_size',
            'key_press_activation_value', 'place_factor', 'priority']),
            title='Edit BoxWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BoxWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

