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


class BoxRepresentation(WidgetRepresentation):
    """
    BoxRepresentation - a class defining the representation for the
    BoxWidget2
    
    Superclass: WidgetRepresentation
    
    This class is a concrete representation for the BoxWidget2. It
    represents a box with seven handles: one on each of the six faces,
    plus a center handle. Through interaction with the widget, the box
    representation can be arbitrarily positioned in the 3d space.
    
    To use this representation, you normally use the place_widget() method
    to position the widget at a specified region in space.
    
    Caveats:
    
    This class, and BoxWidget2, are second generation VTK widgets. An
    earlier version of this functionality was defined in the class
    BoxWidget.
    
    See Also:
    
    BoxWidget2 BoxWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBoxRepresentation, obj, update, **traits)
    
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

    inside_out = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the inside_out flag. This data memeber is used in
        conjunction with the get_planes() method. When off, the normals
        point out of the box. When on, the normals point into the
        hexahedron.  inside_out is off by default.
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

    def get_transform(self, *args):
        """
        V.get_transform(Transform)
        C++: virtual void GetTransform(Transform *t)
        Retrieve a linear transform characterizing the transformation of
        the box. Note that the transformation is relative to where
        place_widget() was initially called. This method modifies the
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
        to where place_widget() was initially called (i.e., the original
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
        properties of the handles, when selected or normal, can be
        specified.
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
            out of 15 points) defines the center of the box. These point
            values are guaranteed to be up-to-date when either the
            widget's corresponding interaction_event or
            end_interaction_event events are invoked. The user provides the
            PolyData and the points and cells are added to it.
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
        properties of the handles, when selected or normal, can be
        specified.
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
        C++: virtual void HandlesOff()
        Switches handles (the spheres) on or off by manipulating the
        underlying actor visibility.
        """
        ret = self._vtk_obj.HandlesOff()
        return ret
        

    def handles_on(self):
        """
        V.handles_on()
        C++: virtual void HandlesOn()
        Switches handles (the spheres) on or off by manipulating the
        underlying actor visibility.
        """
        ret = self._vtk_obj.HandlesOn()
        return ret
        

    def place_widget(self, *args):
        """
        V.place_widget([float, float, float, float, float, float])
        C++: virtual void PlaceWidget(double bounds[6])
        These are methods that satisfy WidgetRepresentation's API.
        """
        ret = self._wrap_call(self._vtk_obj.PlaceWidget, *args)
        return ret

    def set_interaction_state(self, *args):
        """
        V.set_interaction_state(int)
        C++: void SetInteractionState(int state)
        The interaction state may be set from a widget (e.g.,
        BoxWidget2) or other object. This controls how the interaction
        with the widget proceeds. Normally this method is used as part of
        a handshaking process with the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
        ret = self._wrap_call(self._vtk_obj.SetInteractionState, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('need_to_render', 'GetNeedToRender'), ('dragable',
    'GetDragable'), ('visibility', 'GetVisibility'), ('debug',
    'GetDebug'), ('inside_out', 'GetInsideOut'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('place_factor', 'GetPlaceFactor'), ('outline_face_wires',
    'GetOutlineFaceWires'), ('use_bounds', 'GetUseBounds'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('outline_cursor_wires', 'GetOutlineCursorWires'), ('reference_count',
    'GetReferenceCount'), ('pickable', 'GetPickable'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'inside_out',
    'need_to_render', 'outline_cursor_wires', 'outline_face_wires',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'place_factor',
    'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BoxRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BoxRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['inside_out', 'need_to_render',
            'outline_cursor_wires', 'outline_face_wires', 'use_bounds',
            'visibility'], [], ['allocated_render_time', 'estimated_render_time',
            'handle_size', 'place_factor', 'render_time_multiplier']),
            title='Edit BoxRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BoxRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

