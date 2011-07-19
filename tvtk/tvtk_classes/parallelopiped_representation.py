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


class ParallelopipedRepresentation(WidgetRepresentation):
    """
    ParallelopipedRepresentation - Default representation for
    ParallelopipedWidget
    
    Superclass: WidgetRepresentation
    
    This class provides the default geometrical representation for
    ParallelopipedWidget. As a result of interactions of the widget,
    this representation can take on of the following shapes:
    
    1) A parallelopiped. (8 handles, 6 faces)
    
    2) Paralleopiped with a chair depression on any one handle. (A chair
    is a depression on one of the handles that carves inwards so as to
    allow the user to visualize cuts in the volume). (14 handles, 9
    faces).
    
    See Also:
    
    ParallelopipedWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParallelopipedRepresentation, obj, update, **traits)
    
    def _get_hovered_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetHoveredHandleProperty())
    def _set_hovered_handle_property(self, arg):
        old_val = self._get_hovered_handle_property()
        self._wrap_call(self._vtk_obj.SetHoveredHandleProperty,
                        deref_vtk(arg))
        self.trait_property_changed('hovered_handle_property', old_val, arg)
    hovered_handle_property = traits.Property(_get_hovered_handle_property, _set_hovered_handle_property, help=\
        """
        Set/Get the handle properties.
        """
    )

    minimum_thickness = traits.Float(0.05, enter_set=True, auto_set=False, help=\
        """
        Minimum thickness for the parallelopiped. User interactions
        cannot make any individual axis of the parallopiped thinner than
        this value. Default is 0.05 expressed as a fraction of the
        diagonal of the bounding box used in the place_widget()
        invocation.
        """
    )
    def _minimum_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumThickness,
                        self.minimum_thickness)

    def _get_selected_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedHandleProperty())
    def _set_selected_handle_property(self, arg):
        old_val = self._get_selected_handle_property()
        self._wrap_call(self._vtk_obj.SetSelectedHandleProperty,
                        deref_vtk(arg))
        self.trait_property_changed('selected_handle_property', old_val, arg)
    selected_handle_property = traits.Property(_get_selected_handle_property, _set_selected_handle_property, help=\
        """
        Set/Get the handle properties.
        """
    )

    def get_handle_representation(self, *args):
        """
        V.get_handle_representation(int) -> HandleRepresentation
        C++: HandleRepresentation *GetHandleRepresentation(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetHandleRepresentation, *args)
        return wrap_vtk(ret)

    def set_handle_representation(self, *args):
        """
        V.set_handle_representation(HandleRepresentation)
        C++: void SetHandleRepresentation(HandleRepresentation *handle)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetHandleRepresentation, *my_args)
        return ret

    def _get_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetHandleProperty())
    def _set_handle_property(self, arg):
        old_val = self._get_handle_property()
        self._wrap_call(self._vtk_obj.SetHandleProperty,
                        deref_vtk(arg))
        self.trait_property_changed('handle_property', old_val, arg)
    handle_property = traits.Property(_get_handle_property, _set_handle_property, help=\
        """
        Set/Get the handle properties.
        """
    )

    def get_bounding_planes(self, *args):
        """
        V.get_bounding_planes(PlaneCollection)
        C++: void GetBoundingPlanes(PlaneCollection *pc)
        Get the bounding planes of the object. The first 6 planes will be
        bounding planes of the parallelopiped. If in chair mode, three
        additional planes will be present. The last three planes will be
        those of the chair. The normals of all the planes will point into
        the object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBoundingPlanes, *my_args)
        return ret

    def _get_face_property(self):
        return wrap_vtk(self._vtk_obj.GetFaceProperty())
    face_property = traits.Property(_get_face_property, help=\
        """
        Get the face properties. When a face is being translated, the
        face gets highlighted with the selected_face_property.
        """
    )

    def _get_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetOutlineProperty())
    outline_property = traits.Property(_get_outline_property, help=\
        """
        Get the outline properties. These are the properties with which
        the parallelopiped wireframe is rendered.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        The parallelopiped polydata.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_selected_face_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedFaceProperty())
    selected_face_property = traits.Property(_get_selected_face_property, help=\
        """
        Get the face properties. When a face is being translated, the
        face gets highlighted with the selected_face_property.
        """
    )

    def _get_selected_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedOutlineProperty())
    selected_outline_property = traits.Property(_get_selected_outline_property, help=\
        """
        Get the outline properties. These are the properties with which
        the parallelopiped wireframe is rendered.
        """
    )

    def handles_off(self):
        """
        V.handles_off()
        C++: void HandlesOff()
        Turns the visibility of the handles on/off. Sometimes they may
        get in the way of visualization.
        """
        ret = self._vtk_obj.HandlesOff()
        return ret
        

    def handles_on(self):
        """
        V.handles_on()
        C++: void HandlesOn()
        Turns the visibility of the handles on/off. Sometimes they may
        get in the way of visualization.
        """
        ret = self._vtk_obj.HandlesOn()
        return ret
        

    def place_widget(self, *args):
        """
        V.place_widget([[float, float, float], [float, float, float],
            [float, float, float], [float, float, float], [float, float,
            float], [float, float, float], [float, float, float], [float,
            float, float]])
        C++: virtual void PlaceWidget(double corners[8][3])
        V.place_widget([float, float, float, float, float, float])
        C++: virtual void PlaceWidget(double bounds[6])
        Place the widget in the scene. You can use either of the two APIs
        :
        1) place_widget( double bounds[6] ) Creates a cuboid conforming to
        the said bounds.
        2) place_widget( double corners[8][3] ) Creates a parallelopiped
           with corners specified. The order in which corners are
           specified must obey the following rule: Corner 0 - 1 - 2 - 3 -
        0  forms a face Corner 4 - 5 - 6 - 7 - 4  forms a face Corner 0 -
        4 - 5 - 1 - 0  forms a face Corner 1 - 5 - 6 - 2 - 1  forms a
           face Corner 2 - 6 - 7 - 3 - 2  forms a face Corner 3 - 7 - 4 -
        0 - 3  forms a face
        """
        ret = self._wrap_call(self._vtk_obj.PlaceWidget, *args)
        return ret

    def position_handles(self):
        """
        V.position_handles()
        C++: virtual void PositionHandles()
        Synchronize the parallelopiped handle positions with the
        Polygonal datastructure.
        """
        ret = self._vtk_obj.PositionHandles()
        return ret
        

    def scale(self, *args):
        """
        V.scale(int, int)
        C++: virtual void Scale(int X, int Y)"""
        ret = self._wrap_call(self._vtk_obj.Scale, *args)
        return ret

    def set_interaction_state(self, *args):
        """
        V.set_interaction_state(int)
        C++: void SetInteractionState(int a)
        The interaction state may be set from a widget (e.g.,
        point_widget) or other object. This controls how the interaction
        with the widget proceeds.
        """
        ret = self._wrap_call(self._vtk_obj.SetInteractionState, *args)
        return ret

    def translate(self, *args):
        """
        V.translate([float, float, float])
        C++: virtual void Translate(double translation[3])
        V.translate(int, int)
        C++: virtual void Translate(int X, int Y)"""
        ret = self._wrap_call(self._vtk_obj.Translate, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('debug', 'GetDebug'), ('dragable', 'GetDragable'), ('visibility',
    'GetVisibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('minimum_thickness',
    'GetMinimumThickness'), ('need_to_render', 'GetNeedToRender'),
    ('reference_count', 'GetReferenceCount'), ('place_factor',
    'GetPlaceFactor'), ('pickable', 'GetPickable'), ('use_bounds',
    'GetUseBounds'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'minimum_thickness',
    'place_factor', 'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParallelopipedRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ParallelopipedRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['need_to_render', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'minimum_thickness', 'place_factor', 'render_time_multiplier']),
            title='Edit ParallelopipedRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParallelopipedRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

