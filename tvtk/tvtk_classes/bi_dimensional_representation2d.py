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


class BiDimensionalRepresentation2D(WidgetRepresentation):
    """
    BiDimensionalRepresentation2D - represent the
    BiDimensionalWidget
    
    Superclass: WidgetRepresentation
    
    The BiDimensionalRepresentation2D is used to represent the
    bi-dimensional measure in a 2d (overlay) context. This representation
    consists of two perpendicular lines defined by four
    HandleRepresentations. The four handles can be independently
    manipulated consistent with the orthogonal constraint on the lines.
    (Note: the four points are referred to as Point1, Point2, Point3 and
    Point4. Point1 and Point2 define the first line; and Point3 and
    Point4 define the second orthogonal line.)
    
    To create this widget, you click to place the first two points. The
    third point is mirrored with the fourth point; when you place the
    third point (which is orthogonal to the lined defined by the first
    two points), the fourth point is dropped as well. After definition,
    the four points can be moved (in constrained fashion, preserving
    orthogonality). Further, the entire widget can be translated by
    grabbing the center point of the widget; each line can be moved along
    the other line; and the entire widget can be rotated around its
    center point.
    
    See Also:
    
    AngleWidget HandleRepresentation
    BiDimensionalRepresentation2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBiDimensionalRepresentation2D, obj, update, **traits)
    
    show_label_above_widget = tvtk_base.true_bool_trait(help=\
        """
        Toggle whether to display the label above or below the widget.
        Defaults to 1.
        """
    )
    def _show_label_above_widget_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowLabelAboveWidget,
                        self.show_label_above_widget_)

    line2_visibility = tvtk_base.true_bool_trait(help=\
        """
        Special methods for turning off the lines that define the
        bi-dimensional measure. Generally these methods are used by the
        BiDimensionalWidget to control the appearance of the widget.
        Note: turning off Line1 actually turns off Line1 and Line2.
        """
    )
    def _line2_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLine2Visibility,
                        self.line2_visibility_)

    line1_visibility = tvtk_base.true_bool_trait(help=\
        """
        Special methods for turning off the lines that define the
        bi-dimensional measure. Generally these methods are used by the
        BiDimensionalWidget to control the appearance of the widget.
        Note: turning off Line1 actually turns off Line1 and Line2.
        """
    )
    def _line1_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLine1Visibility,
                        self.line1_visibility_)

    def get_point1_world_position(self, *args):
        """
        V.get_point1_world_position([float, float, float])
        C++: virtual void GetPoint1WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1WorldPosition, *args)
        return ret

    def set_point1_world_position(self, *args):
        """
        V.set_point1_world_position([float, float, float])
        C++: virtual void SetPoint1WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1WorldPosition, *args)
        return ret

    label_format = traits.String(r"%0.3g", enter_set=True, auto_set=False, help=\
        """
        Specify the format to use for labelling the distance. Note that
        an empty string results in no label, or a format string without a
        "%" character will not print the distance value.
        """
    )
    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    def get_point3_world_position(self, *args):
        """
        V.get_point3_world_position([float, float, float])
        C++: virtual void GetPoint3WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint3WorldPosition, *args)
        return ret

    def set_point3_world_position(self, *args):
        """
        V.set_point3_world_position([float, float, float])
        C++: virtual void SetPoint3WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint3WorldPosition, *args)
        return ret

    def get_point3display_position(self, *args):
        """
        V.get_point3display_position([float, float, float])
        C++: virtual void GetPoint3DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint3DisplayPosition, *args)
        return ret

    def set_point3display_position(self, *args):
        """
        V.set_point3display_position([float, float, float])
        C++: virtual void SetPoint3DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint3DisplayPosition, *args)
        return ret

    def get_point1display_position(self, *args):
        """
        V.get_point1display_position([float, float, float])
        C++: virtual void GetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1DisplayPosition, *args)
        return ret

    def set_point1display_position(self, *args):
        """
        V.set_point1display_position([float, float, float])
        C++: virtual void SetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1DisplayPosition, *args)
        return ret

    def get_point2_world_position(self, *args):
        """
        V.get_point2_world_position([float, float, float])
        C++: virtual void GetPoint2WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2WorldPosition, *args)
        return ret

    def set_point2_world_position(self, *args):
        """
        V.set_point2_world_position([float, float, float])
        C++: virtual void SetPoint2WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2WorldPosition, *args)
        return ret

    def get_point4_display_position(self, *args):
        """
        V.get_point4_display_position([float, float, float])
        C++: virtual void GetPoint4DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint4DisplayPosition, *args)
        return ret

    def set_point4_display_position(self, *args):
        """
        V.set_point4_display_position([float, float, float])
        C++: virtual void SetPoint4DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint4DisplayPosition, *args)
        return ret

    def get_point4_world_position(self, *args):
        """
        V.get_point4_world_position([float, float, float])
        C++: virtual void GetPoint4WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint4WorldPosition, *args)
        return ret

    def set_point4_world_position(self, *args):
        """
        V.set_point4_world_position([float, float, float])
        C++: virtual void SetPoint4WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint4WorldPosition, *args)
        return ret

    def get_point2display_position(self, *args):
        """
        V.get_point2display_position([float, float, float])
        C++: virtual void GetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2DisplayPosition, *args)
        return ret

    def set_point2display_position(self, *args):
        """
        V.set_point2display_position([float, float, float])
        C++: virtual void SetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the four points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2DisplayPosition, *args)
        return ret

    tolerance = traits.Trait(5, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the representation (in
        pixels) in which the cursor is considered near enough to the
        representation to be active.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    id = traits.Long(4294967295, enter_set=True, auto_set=False, help=\
        """
        Set/get the id to display in the label.
        """
    )
    def _id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetID,
                        self.id)

    def get_label_position(self, *args):
        """
        V.get_label_position([float, float, float])
        C++: void GetLabelPosition(double pos[3])
        Get the position of the widget's label in display coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetLabelPosition, *args)
        return ret

    def _get_label_text(self):
        return self._vtk_obj.GetLabelText()
    label_text = traits.Property(_get_label_text, help=\
        """
        Get the text shown in the widget's label.
        """
    )

    def _get_length1(self):
        return self._vtk_obj.GetLength1()
    length1 = traits.Property(_get_length1, help=\
        """
        Return the length of the line defined by (Point1,Point2). This is
        the distance in the world coordinate system.
        """
    )

    def _get_length2(self):
        return self._vtk_obj.GetLength2()
    length2 = traits.Property(_get_length2, help=\
        """
        Return the length of the line defined by (Point3,Point4). This is
        the distance in the world coordinate system.
        """
    )

    def _get_line_property(self):
        return wrap_vtk(self._vtk_obj.GetLineProperty())
    line_property = traits.Property(_get_line_property, help=\
        """
        Retrieve the property used to control the appearance of the two
        orthogonal lines.
        """
    )

    def _get_point1_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Representation())
    point1_representation = traits.Property(_get_point1_representation, help=\
        """
        Set/Get the handle representations used within the
        BiDimensionalRepresentation2D. (Note: properties can be set by
        grabbing these representations and setting the properties
        appropriately.)
        """
    )

    def _get_point2_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Representation())
    point2_representation = traits.Property(_get_point2_representation, help=\
        """
        Set/Get the handle representations used within the
        BiDimensionalRepresentation2D. (Note: properties can be set by
        grabbing these representations and setting the properties
        appropriately.)
        """
    )

    def _get_point3_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint3Representation())
    point3_representation = traits.Property(_get_point3_representation, help=\
        """
        Set/Get the handle representations used within the
        BiDimensionalRepresentation2D. (Note: properties can be set by
        grabbing these representations and setting the properties
        appropriately.)
        """
    )

    def _get_point4_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint4Representation())
    point4_representation = traits.Property(_get_point4_representation, help=\
        """
        Set/Get the handle representations used within the
        BiDimensionalRepresentation2D. (Note: properties can be set by
        grabbing these representations and setting the properties
        appropriately.)
        """
    )

    def _get_selected_line_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedLineProperty())
    selected_line_property = traits.Property(_get_selected_line_property, help=\
        """
        Retrieve the property used to control the appearance of the two
        orthogonal lines.
        """
    )

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    text_property = traits.Property(_get_text_property, help=\
        """
        Retrieve the property used to control the appearance of the text
        labels.
        """
    )

    def get_world_label_position(self, *args):
        """
        V.get_world_label_position([float, float, float])
        C++: void GetWorldLabelPosition(double pos[3])
        Get the position of the widget's label in display coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetWorldLabelPosition, *args)
        return ret

    def instantiate_handle_representation(self):
        """
        V.instantiate_handle_representation()
        C++: void InstantiateHandleRepresentation()
        This method is used to specify the type of handle representation
        to use for the four internal HandleRepresentations within
        BiDimensionalRepresentation2D.  To use this method, create a
        dummy HandleRepresentation (or subclass), and then invoke this
        method with this dummy. Then the BiDimensionalRepresentation2D
        uses this dummy to clone four HandleRepresentations of the
        same type. Make sure you set the handle representation before the
        widget is enabled. (The method instantiate_handle_representation()
        is invoked by the BiDimensionalWidget for the purposes of
        cloning.)
        """
        ret = self._vtk_obj.InstantiateHandleRepresentation()
        return ret
        

    def point2_widget_interaction(self, *args):
        """
        V.point2_widget_interaction([float, float])
        C++: virtual void Point2WidgetInteraction(double e[2])
        These are methods that satisfy WidgetRepresentation's API.
        """
        ret = self._wrap_call(self._vtk_obj.Point2WidgetInteraction, *args)
        return ret

    def point3_widget_interaction(self, *args):
        """
        V.point3_widget_interaction([float, float])
        C++: virtual void Point3WidgetInteraction(double e[2])
        These are methods that satisfy WidgetRepresentation's API.
        """
        ret = self._wrap_call(self._vtk_obj.Point3WidgetInteraction, *args)
        return ret

    def set_handle_representation(self, *args):
        """
        V.set_handle_representation(HandleRepresentation)
        C++: void SetHandleRepresentation(HandleRepresentation *handle)
        This method is used to specify the type of handle representation
        to use for the four internal HandleRepresentations within
        BiDimensionalRepresentation2D.  To use this method, create a
        dummy HandleRepresentation (or subclass), and then invoke this
        method with this dummy. Then the BiDimensionalRepresentation2D
        uses this dummy to clone four HandleRepresentations of the
        same type. Make sure you set the handle representation before the
        widget is enabled. (The method instantiate_handle_representation()
        is invoked by the BiDimensionalWidget for the purposes of
        cloning.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetHandleRepresentation, *my_args)
        return ret

    def start_widget_definition(self, *args):
        """
        V.start_widget_definition([float, float])
        C++: virtual void StartWidgetDefinition(double e[2])
        These are methods that satisfy WidgetRepresentation's API.
        """
        ret = self._wrap_call(self._vtk_obj.StartWidgetDefinition, *args)
        return ret

    def start_widget_manipulation(self, *args):
        """
        V.start_widget_manipulation([float, float])
        C++: virtual void StartWidgetManipulation(double e[2])
        These are methods that satisfy WidgetRepresentation's API.
        """
        ret = self._wrap_call(self._vtk_obj.StartWidgetManipulation, *args)
        return ret

    _updateable_traits_ = \
    (('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('line2_visibility', 'GetLine2Visibility'), ('label_format',
    'GetLabelFormat'), ('need_to_render', 'GetNeedToRender'), ('dragable',
    'GetDragable'), ('visibility', 'GetVisibility'), ('use_bounds',
    'GetUseBounds'), ('reference_count', 'GetReferenceCount'),
    ('line1_visibility', 'GetLine1Visibility'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('place_factor', 'GetPlaceFactor'),
    ('show_label_above_widget', 'GetShowLabelAboveWidget'), ('pickable',
    'GetPickable'), ('tolerance', 'GetTolerance'), ('id', 'GetID'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'line1_visibility',
    'line2_visibility', 'need_to_render', 'pickable',
    'show_label_above_widget', 'use_bounds', 'visibility',
    'allocated_render_time', 'estimated_render_time', 'handle_size', 'id',
    'label_format', 'place_factor', 'render_time_multiplier',
    'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BiDimensionalRepresentation2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BiDimensionalRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['line1_visibility', 'line2_visibility',
            'need_to_render', 'show_label_above_widget', 'use_bounds',
            'visibility'], [], ['allocated_render_time', 'estimated_render_time',
            'handle_size', 'id', 'label_format', 'place_factor',
            'render_time_multiplier', 'tolerance']),
            title='Edit BiDimensionalRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BiDimensionalRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

