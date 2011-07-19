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


class AngleRepresentation(WidgetRepresentation):
    """
    AngleRepresentation - represent the AngleWidget
    
    Superclass: WidgetRepresentation
    
    The AngleRepresentation is a superclass for classes representing
    the AngleWidget. This representation consists of two rays and
    three HandleRepresentations to place and manipulate the three
    points defining the angle representation. (Note: the three points are
    referred to as Point1, Center, and Point2, at the two end points
    (Point1 and Point2) and Center (around which the angle is measured).
    
    See Also:
    
    AngleWidget HandleRepresentation AngleRepresentation2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAngleRepresentation, obj, update, **traits)
    
    ray2_visibility = tvtk_base.true_bool_trait(help=\
        """
        Special methods for turning off the rays and arc that define the
        cone and arc of the angle.
        """
    )
    def _ray2_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRay2Visibility,
                        self.ray2_visibility_)

    arc_visibility = tvtk_base.true_bool_trait(help=\
        """
        Special methods for turning off the rays and arc that define the
        cone and arc of the angle.
        """
    )
    def _arc_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcVisibility,
                        self.arc_visibility_)

    ray1_visibility = tvtk_base.true_bool_trait(help=\
        """
        Special methods for turning off the rays and arc that define the
        cone and arc of the angle.
        """
    )
    def _ray1_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRay1Visibility,
                        self.ray1_visibility_)

    tolerance = traits.Trait(5, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the representation (in
        pixels) in which the cursor is considered near enough to the end
        points of the representation to be active.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def get_point2display_position(self, *args):
        """
        V.get_point2display_position([float, float, float])
        C++: virtual void GetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the three points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2DisplayPosition, *args)
        return ret

    def set_point2display_position(self, *args):
        """
        V.set_point2display_position([float, float, float])
        C++: virtual void SetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the three points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2DisplayPosition, *args)
        return ret

    def get_point1display_position(self, *args):
        """
        V.get_point1display_position([float, float, float])
        C++: virtual void GetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the three points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1DisplayPosition, *args)
        return ret

    def set_point1display_position(self, *args):
        """
        V.set_point1display_position([float, float, float])
        C++: virtual void SetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the three points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1DisplayPosition, *args)
        return ret

    label_format = traits.String(r"%-#6.3g", enter_set=True, auto_set=False, help=\
        """
        Specify the format to use for labelling the angle. Note that an
        empty string results in no label, or a format string without a
        "%" character will not print the angle value.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    def get_center_display_position(self, *args):
        """
        V.get_center_display_position([float, float, float])
        C++: virtual void GetCenterDisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the three points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetCenterDisplayPosition, *args)
        return ret

    def set_center_display_position(self, *args):
        """
        V.set_center_display_position([float, float, float])
        C++: virtual void SetCenterDisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the three points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetCenterDisplayPosition, *args)
        return ret

    def _get_angle(self):
        return self._vtk_obj.GetAngle()
    angle = traits.Property(_get_angle, help=\
        """
        This representation and all subclasses must keep an angle (in
        degrees) consistent with the state of the widget.
        """
    )

    def _get_center_representation(self):
        return wrap_vtk(self._vtk_obj.GetCenterRepresentation())
    center_representation = traits.Property(_get_center_representation, help=\
        """
        Set/Get the handle representations used for the
        AngleRepresentation.
        """
    )

    def get_center_world_position(self, *args):
        """
        V.get_center_world_position([float, float, float])
        C++: virtual void GetCenterWorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the three points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetCenterWorldPosition, *args)
        return ret

    def _get_point1_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Representation())
    point1_representation = traits.Property(_get_point1_representation, help=\
        """
        Set/Get the handle representations used for the
        AngleRepresentation.
        """
    )

    def get_point1_world_position(self, *args):
        """
        V.get_point1_world_position([float, float, float])
        C++: virtual void GetPoint1WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the three points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1WorldPosition, *args)
        return ret

    def _get_point2_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Representation())
    point2_representation = traits.Property(_get_point2_representation, help=\
        """
        Set/Get the handle representations used for the
        AngleRepresentation.
        """
    )

    def get_point2_world_position(self, *args):
        """
        V.get_point2_world_position([float, float, float])
        C++: virtual void GetPoint2WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the three points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2WorldPosition, *args)
        return ret

    def center_widget_interaction(self, *args):
        """
        V.center_widget_interaction([float, float])
        C++: virtual void CenterWidgetInteraction(double e[2])
        These are methods that satisfy WidgetRepresentation's API.
        """
        ret = self._wrap_call(self._vtk_obj.CenterWidgetInteraction, *args)
        return ret

    def instantiate_handle_representation(self):
        """
        V.instantiate_handle_representation()
        C++: void InstantiateHandleRepresentation()
        This method is used to specify the type of handle representation
        to use for the three internal HandleWidgets within
        AngleRepresentation. To use this method, create a dummy
        HandleRepresentation (or subclass), and then invoke this
        method with this dummy. Then the AngleRepresentation uses this
        dummy to clone three HandleRepresentations of the same type.
        Make sure you set the handle representation before the widget is
        enabled. (The method instantiate_handle_representation() is invoked
        by the Angle widget.)
        """
        ret = self._vtk_obj.InstantiateHandleRepresentation()
        return ret
        

    def set_handle_representation(self, *args):
        """
        V.set_handle_representation(HandleRepresentation)
        C++: void SetHandleRepresentation(HandleRepresentation *handle)
        This method is used to specify the type of handle representation
        to use for the three internal HandleWidgets within
        AngleRepresentation. To use this method, create a dummy
        HandleRepresentation (or subclass), and then invoke this
        method with this dummy. Then the AngleRepresentation uses this
        dummy to clone three HandleRepresentations of the same type.
        Make sure you set the handle representation before the widget is
        enabled. (The method instantiate_handle_representation() is invoked
        by the Angle widget.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetHandleRepresentation, *my_args)
        return ret

    _updateable_traits_ = \
    (('ray1_visibility', 'GetRay1Visibility'), ('allocated_render_time',
    'GetAllocatedRenderTime'), ('handle_size', 'GetHandleSize'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('arc_visibility', 'GetArcVisibility'), ('label_format',
    'GetLabelFormat'), ('need_to_render', 'GetNeedToRender'), ('dragable',
    'GetDragable'), ('visibility', 'GetVisibility'), ('reference_count',
    'GetReferenceCount'), ('ray2_visibility', 'GetRay2Visibility'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('place_factor', 'GetPlaceFactor'), ('pickable', 'GetPickable'),
    ('tolerance', 'GetTolerance'), ('use_bounds', 'GetUseBounds'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['arc_visibility', 'debug', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'ray1_visibility', 'ray2_visibility',
    'use_bounds', 'visibility', 'allocated_render_time',
    'estimated_render_time', 'handle_size', 'label_format',
    'place_factor', 'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AngleRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AngleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['arc_visibility', 'need_to_render', 'ray1_visibility',
            'ray2_visibility', 'use_bounds', 'visibility'], [],
            ['allocated_render_time', 'estimated_render_time', 'handle_size',
            'label_format', 'place_factor', 'render_time_multiplier',
            'tolerance']),
            title='Edit AngleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AngleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

