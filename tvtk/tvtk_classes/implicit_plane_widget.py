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


class ImplicitPlaneWidget(PolyDataSourceWidget):
    """
    ImplicitPlaneWidget - 3d widget for manipulating an infinite plane
    
    Superclass: PolyDataSourceWidget
    
    This 3d widget defines an infinite plane that can be interactively
    placed in a scene. The widget is represented by a plane with a normal
    vector; the plane is contained by a bounding box, and where the plane
    intersects the bounding box the edges are shown (possibly tubed). The
    normal can be selected and moved to rotate the plane; the plane
    itself can be selected and translated in various directions. As the
    plane is moved, the implicit plane function and polygon (representing
    the plane cut against the bounding box) is updated.
    
    To use this object, just invoke set_interactor() with the argument of
    the method a RenderWindowInteractor.  You may also wish to invoke
    "_place_widget()" to initially position the widget. If the "i" key (for
    "interactor") is pressed, the ImplicitPlaneWidget will appear.
    (See superclass documentation for information about changing this
    behavior.) If you select the normal vector, the plane can be
    arbitrarily rotated. The plane can be translated along the normal by
    selecting the plane and moving it. The plane (the plane origin) can
    also be arbitrary moved by selecting the plane with the middle mouse
    button. The right mouse button can be used to uniformly scale the
    bounding box (moving "up" the box scales larger; moving "down" the
    box scales smaller). Events that occur outside of the widget (i.e.,
    no part of the widget is picked) are propagated to any other
    registered obsevers (such as the interaction style).  Turn off the
    widget by pressing the "i" key again (or invoke the Off() method).
    
    The ImplicitPlaneWidget has several methods that can be used in
    conjunction with other VTK objects.  The get_poly_data() method can be
    used to get a polygonal representation (the single polygon clipped by
    the bounding box).  Typical usage of the widget is to make use of the
    start_interaction_event, interaction_event, and end_interaction_event
    events. The interaction_event is called on mouse motion; the other two
    events are called on button down and button up (either left or right
    button). (Note: there is also a place_widget_event that is invoked when
    the widget is placed with place_widget().)
    
    Some additional features of this class include the ability to control
    the properties of the widget. You do this by setting property values
    on the normal vector (selected and unselected properties); the plane
    (selected and unselected properties); the outline (selected and
    unselected properties); and the edges. The edges may also be tubed or
    not.
    
    Caveats:
    
    Note that the widget can be picked even when it is "behind" other
    actors.  This is an intended feature and not a bug.
    
    See Also:
    
    ThreeDWidget BoxWidget PlaneWidget LineWidget PointWidget
    SphereWidget ImagePlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitPlaneWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(ImplicitPlaneWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    normal_to_x_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a modified_event is invoked. This can
        be used to snap the plane to the axes if it is orginally not
        aligned.
        """
    )
    def _normal_to_x_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToXAxis,
                        self.normal_to_x_axis_)

    normal_to_z_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a modified_event is invoked. This can
        be used to snap the plane to the axes if it is orginally not
        aligned.
        """
    )
    def _normal_to_z_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToZAxis,
                        self.normal_to_z_axis_)

    outline_translation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to translate the bounding box by grabbing
        it with the left mouse button.
        """
    )
    def _outline_translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutlineTranslation,
                        self.outline_translation_)

    origin_translation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to translate the origin (sphere) with the
        left mouse button.
        """
    )
    def _origin_translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginTranslation,
                        self.origin_translation_)

    normal_to_y_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a modified_event is invoked. This can
        be used to snap the plane to the axes if it is orginally not
        aligned.
        """
    )
    def _normal_to_y_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToYAxis,
                        self.normal_to_y_axis_)

    outside_bounds = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to move the widget outside of the input's
        bound
        """
    )
    def _outside_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutsideBounds,
                        self.outside_bounds_)

    draw_plane = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
    )
    def _draw_plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawPlane,
                        self.draw_plane_)

    tubing = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a TubeFilter.
        """
    )
    def _tubing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTubing,
                        self.tubing_)

    scale_enabled = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to scale with the mouse
        """
    )
    def _scale_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleEnabled,
                        self.scale_enabled_)

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Get the origin of the plane.
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    diagonal_ratio = traits.Trait(0.3, traits.Range(0.0, 2.0, enter_set=True, auto_set=False), help=\
        """
        By default the arrow is 30% of the diagonal length. diagonal_ratio
        control this ratio in the interval [0-2]
        """
    )
    def _diagonal_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiagonalRatio,
                        self.diagonal_ratio)

    normal = traits.Array(shape=(3,), value=(1.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Get the normal to the plane.
        """
    )
    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    def _get_edges_property(self):
        return wrap_vtk(self._vtk_obj.GetEdgesProperty())
    edges_property = traits.Property(_get_edges_property, help=\
        """
        Get the property of the intersection edges. (This property also
        applies to the edges when tubed.)
        """
    )

    def _get_normal_property(self):
        return wrap_vtk(self._vtk_obj.GetNormalProperty())
    normal_property = traits.Property(_get_normal_property, help=\
        """
        Get the properties on the normal (line and cone).
        """
    )

    def _get_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetOutlineProperty())
    outline_property = traits.Property(_get_outline_property, help=\
        """
        Get the property of the outline.
        """
    )

    def get_plane(self, *args):
        """
        V.get_plane(Plane)
        C++: void GetPlane(Plane *plane)
        Get the implicit function for the plane. The user must provide
        the instance of the class Plane. Note that Plane is a
        subclass of ImplicitFunction, meaning that it can be used by a
        variety of filters to perform clipping, cutting, and selection of
        data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlane, *my_args)
        return ret

    def _get_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetPlaneProperty())
    plane_property = traits.Property(_get_plane_property, help=\
        """
        Get the plane properties. The properties of the plane when
        selected and unselected can be manipulated.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata that defines the plane. The polydata contains a
        single polygon that is clipped by the bounding box.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_selected_normal_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedNormalProperty())
    selected_normal_property = traits.Property(_get_selected_normal_property, help=\
        """
        Get the properties on the normal (line and cone).
        """
    )

    def _get_selected_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedOutlineProperty())
    selected_outline_property = traits.Property(_get_selected_outline_property, help=\
        """
        Get the property of the outline.
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

    def size_handles(self):
        """
        V.size_handles()
        C++: virtual void SizeHandles()
        Control widget appearance
        """
        ret = self._vtk_obj.SizeHandles()
        return ret
        

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('normal_to_z_axis', 'GetNormalToZAxis'),
    ('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('handle_size', 'GetHandleSize'), ('normal', 'GetNormal'),
    ('origin_translation', 'GetOriginTranslation'), ('scale_enabled',
    'GetScaleEnabled'), ('enabled', 'GetEnabled'), ('outline_translation',
    'GetOutlineTranslation'), ('normal_to_x_axis', 'GetNormalToXAxis'),
    ('draw_plane', 'GetDrawPlane'), ('priority', 'GetPriority'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('outside_bounds', 'GetOutsideBounds'), ('reference_count',
    'GetReferenceCount'), ('place_factor', 'GetPlaceFactor'), ('tubing',
    'GetTubing'), ('key_press_activation', 'GetKeyPressActivation'),
    ('normal_to_y_axis', 'GetNormalToYAxis'), ('diagonal_ratio',
    'GetDiagonalRatio'))
    
    _full_traitnames_list_ = \
    (['debug', 'draw_plane', 'enabled', 'global_warning_display',
    'key_press_activation', 'normal_to_x_axis', 'normal_to_y_axis',
    'normal_to_z_axis', 'origin_translation', 'outline_translation',
    'outside_bounds', 'scale_enabled', 'tubing', 'diagonal_ratio',
    'handle_size', 'key_press_activation_value', 'normal', 'origin',
    'place_factor', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitPlaneWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitPlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['draw_plane', 'enabled', 'key_press_activation',
            'normal_to_x_axis', 'normal_to_y_axis', 'normal_to_z_axis',
            'origin_translation', 'outline_translation', 'outside_bounds',
            'scale_enabled', 'tubing'], [], ['diagonal_ratio', 'handle_size',
            'key_press_activation_value', 'normal', 'origin', 'place_factor',
            'priority']),
            title='Edit ImplicitPlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitPlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

