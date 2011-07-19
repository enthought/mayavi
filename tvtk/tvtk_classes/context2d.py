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

from tvtk.tvtk_classes.object import Object


class Context2D(Object):
    """
    Context2D - Class for drawing 2d primitives to a graphical context.
    
    Superclass: Object
    
    This defines the interface for drawing onto a 2d context. The context
    must be set up with a ContextDevice2D derived class that provides
    the functions to facilitate the low level calls to the context.
    Currently only an open_gl based device is provided, but this could be
    extended in the future.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContext2D, obj, update, **traits)
    
    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Compute the current transform applied to the context.
        """
    )

    def _get_brush(self):
        return wrap_vtk(self._vtk_obj.GetBrush())
    brush = traits.Property(_get_brush, help=\
        """
        Get the pen which controls the outlines of shapes as well as
        lines, points and related primitives.
        """
    )

    def _get_buffer_id_mode(self):
        return self._vtk_obj.GetBufferIdMode()
    buffer_id_mode = traits.Property(_get_buffer_id_mode, help=\
        """
        Tell if the context is in buffer_id creation mode. Initial value
        is false.
        """
    )

    def _get_device(self):
        return wrap_vtk(self._vtk_obj.GetDevice())
    device = traits.Property(_get_device, help=\
        """
        
        """
    )

    def _get_pen(self):
        return wrap_vtk(self._vtk_obj.GetPen())
    pen = traits.Property(_get_pen, help=\
        """
        Get the pen which controls the outlines of shapes, as well as
        lines, points and related primitives. This object can be modified
        and the changes will be reflected in subsequent drawing
        operations.
        """
    )

    def _get_text_prop(self):
        return wrap_vtk(self._vtk_obj.GetTextProp())
    text_prop = traits.Property(_get_text_prop, help=\
        """
        Get the text properties object for the Context2D.
        """
    )

    def append_transform(self, *args):
        """
        V.append_transform(Transform2D)
        C++: void AppendTransform(Transform2D *transform)
        Append the transform for the context, the underlying device will
        use the matrix of the transform. Note, this is set immediately,
        later changes to the matrix will have no effect until it is set
        again. The matrix of the transform will multiply the current
        context transform.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AppendTransform, *my_args)
        return ret

    def apply_brush(self, *args):
        """
        V.apply_brush(Brush)
        C++: void ApplyBrush(Brush *brush)
        Apply the supplied brush which controls the outlines of shapes,
        as well as lines, points and related primitives. This makes a
        deep copy of the Brush object in the Context2D, it does not
        hold a pointer to the supplied object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyBrush, *my_args)
        return ret

    def apply_id(self, *args):
        """
        V.apply_id(int)
        C++: void ApplyId(IdType id)
        Apply id as a color.
        """
        ret = self._wrap_call(self._vtk_obj.ApplyId, *args)
        return ret

    def apply_pen(self, *args):
        """
        V.apply_pen(Pen)
        C++: void ApplyPen(Pen *pen)
        Apply the supplied pen which controls the outlines of shapes, as
        well as lines, points and related primitives. This makes a deep
        copy of the Pen object in the Context2D, it does not hold a
        pointer to the supplied object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyPen, *my_args)
        return ret

    def apply_text_prop(self, *args):
        """
        V.apply_text_prop(TextProperty)
        C++: void ApplyTextProp(TextProperty *prop)
        Apply the supplied text property which controls how text is
        rendered. This makes a deep copy of the TextProperty object in
        the Context2D, it does not hold a pointer to the supplied
        object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyTextProp, *my_args)
        return ret

    def begin(self, *args):
        """
        V.begin(ContextDevice2D) -> bool
        C++: bool Begin(ContextDevice2D *device)
        Begin painting on a ContextDevice2D, no painting can occur
        before this call has been made. Only one painter is allowed at a
        time on any given paint device. Returns true if successful,
        otherwise false.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Begin, *my_args)
        return ret

    def buffer_id_mode_begin(self, *args):
        """
        V.buffer_id_mode_begin(AbstractContextBufferId)
        C++: void BufferIdModeBegin(AbstractContextBufferId *bufferId)
        Start buffer_id creation Mode.
        \pre not_yet: !_get_buffer_id_mode()
        \pre buffer_id_exists: buffer_id!=_0
        \post started: get_buffer_id_mode()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BufferIdModeBegin, *my_args)
        return ret

    def buffer_id_mode_end(self):
        """
        V.buffer_id_mode_end()
        C++: void BufferIdModeEnd()
        Finalize buffer_id creation Mode. It makes sure that the content
        of the buffer_id passed in argument of buffer_id_mode_begin() is
        correctly set.
        \pre started: get_buffer_id_mode()
        \post done: !_get_buffer_id_mode()
        """
        ret = self._vtk_obj.BufferIdModeEnd()
        return ret
        

    def compute_string_bounds(self, *args):
        """
        V.compute_string_bounds(string, Points2D)
        C++: void ComputeStringBounds(const StdString &string,
            Points2D *bounds)
        V.compute_string_bounds(string, [float, float, float, float])
        C++: void ComputeStringBounds(const StdString &string,
            float bounds[4])
        V.compute_string_bounds(unicode, Points2D)
        C++: void ComputeStringBounds(const UnicodeString &string,
            Points2D *bounds)
        V.compute_string_bounds(unicode, [float, float, float, float])
        C++: void ComputeStringBounds(const UnicodeString &string,
            float bounds[4])
        Compute the bounds of the supplied string. The bounds will be
        copied to the supplied bounds variable, the first two elements
        are the bottom corner of the string, and the second two elements
        are the width and height of the bounding box. NOTE: This function
        does not take account of the text rotation.
        """
        my_args = deref_array(args, [('string', 'vtkPoints2D'), ('string', ['float', 'float', 'float', 'float']), ('unicode', 'vtkPoints2D'), ('unicode', ['float', 'float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.ComputeStringBounds, *my_args)
        return ret

    def draw_arc(self, *args):
        """
        V.draw_arc(float, float, float, float, float)
        C++: void DrawArc(float x, float y, float r, float startAngle,
            float stopAngle)
        Draw a circular arc with center at x,y with radius r between
        angles start_angle and stop_angle (expressed in degrees).
        \pre positive_radius: r>=0
        """
        ret = self._wrap_call(self._vtk_obj.DrawArc, *args)
        return ret

    def draw_ellipse(self, *args):
        """
        V.draw_ellipse(float, float, float, float)
        C++: void DrawEllipse(float x, float y, float rx, float ry)
        Draw an ellipse with center at x, y and radii rx, ry.
        \pre positive_rx: rx>=0
        \pre positive_ry: ry>=0
        """
        ret = self._wrap_call(self._vtk_obj.DrawEllipse, *args)
        return ret

    def draw_ellipse_wedge(self, *args):
        """
        V.draw_ellipse_wedge(float, float, float, float, float, float,
            float, float)
        C++: void DrawEllipseWedge(float x, float y, float outRx,
            float outRy, float inRx, float inRy, float startAngle,
            float stopAngle)
        Draw an elliptic wedge with center at x, y, outer radii out_rx,
        out_ry, inner radii in_rx, in_ry between angles start_angle and
        stop_angle (expressed in degrees).
        \pre positive_out_rx: out_rx>=_0
        \pre positive_out_ry: out_ry>=_0
        \pre positive_in_rx: in_rx>=_0
        \pre positive_in_ry: in_ry>=_0
        \pre ordered_rx: in_rx<=out_rx
        \pre ordered_ry: in_ry<=out_ry
        """
        ret = self._wrap_call(self._vtk_obj.DrawEllipseWedge, *args)
        return ret

    def draw_elliptic_arc(self, *args):
        """
        V.draw_elliptic_arc(float, float, float, float, float, float)
        C++: void DrawEllipticArc(float x, float y, float rX, float rY,
            float startAngle, float stopAngle)
        Draw an elliptic arc with center at x,y with radii r_x and r_y
        between angles start_angle and stop_angle (expressed in degrees).
        \pre positive_r_x: r_x>=_0
        \pre positive_r_y: r_y>=_0
        """
        ret = self._wrap_call(self._vtk_obj.DrawEllipticArc, *args)
        return ret

    def draw_image(self, *args):
        """
        V.draw_image(float, float, ImageData)
        C++: void DrawImage(float x, float y, ImageData *image)
        V.draw_image(float, float, float, ImageData)
        C++: void DrawImage(float x, float y, float scale,
            ImageData *image)
        Draw the supplied image at the given x, y location (bottom
        corner).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawImage, *my_args)
        return ret

    def draw_line(self, *args):
        """
        V.draw_line(float, float, float, float)
        C++: void DrawLine(float x1, float y1, float x2, float y2)
        V.draw_line([float, float, float, float])
        C++: void DrawLine(float p[4])
        V.draw_line(Points2D)
        C++: void DrawLine(Points2D *points)
        Draw a line between the specified points.
        """
        my_args = deref_array(args, [('float', 'float', 'float', 'float'), (['float', 'float', 'float', 'float'],), ['vtkPoints2D']])
        ret = self._wrap_call(self._vtk_obj.DrawLine, *my_args)
        return ret

    def draw_point(self, *args):
        """
        V.draw_point(float, float)
        C++: void DrawPoint(float x, float y)
        Draw a point at the supplied x and y coordinate
        """
        ret = self._wrap_call(self._vtk_obj.DrawPoint, *args)
        return ret

    def draw_point_sprites(self, *args):
        """
        V.draw_point_sprites(ImageData, Points2D)
        C++: void DrawPointSprites(ImageData *sprite,
            Points2D *points)
        V.draw_point_sprites(ImageData, Points2D,
            UnsignedCharArray)
        C++: void DrawPointSprites(ImageData *sprite,
            Points2D *points, UnsignedCharArray *colors)
        Draw a series of point sprites, images centred at the points
        supplied. The supplied ImageData is the sprite to be drawn,
        only squares will be drawn and the size is set using
        set_point_size.
        """
        my_args = deref_array(args, [('vtkImageData', 'vtkPoints2D'), ('vtkImageData', 'vtkPoints2D', 'vtkUnsignedCharArray')])
        ret = self._wrap_call(self._vtk_obj.DrawPointSprites, *my_args)
        return ret

    def draw_points(self, *args):
        """
        V.draw_points(Points2D)
        C++: void DrawPoints(Points2D *points)
        Draw a poly line between the specified points - fastest code path
        due to memory layout of the coordinates.
        """
        my_args = deref_array(args, [['vtkPoints2D']])
        ret = self._wrap_call(self._vtk_obj.DrawPoints, *my_args)
        return ret

    def draw_poly(self, *args):
        """
        V.draw_poly(Points2D)
        C++: void DrawPoly(Points2D *points)
        Draw a poly line between the specified points - fastest code path
        due to memory layout of the coordinates.
        """
        my_args = deref_array(args, [['vtkPoints2D']])
        ret = self._wrap_call(self._vtk_obj.DrawPoly, *my_args)
        return ret

    def draw_polygon(self, *args):
        """
        V.draw_polygon(Points2D)
        C++: void DrawPolygon(Points2D *points)
        Draw a polygon defined by the specified points - fastest code
        path due to memory layout of the coordinates.
        """
        my_args = deref_array(args, [['vtkPoints2D']])
        ret = self._wrap_call(self._vtk_obj.DrawPolygon, *my_args)
        return ret

    def draw_quad(self, *args):
        """
        V.draw_quad(float, float, float, float, float, float, float, float)
        C++: void DrawQuad(float x1, float y1, float x2, float y2,
            float x3, float y3, float x4, float y4)
        Draw a quadrilateral at the specified points (4 points, 8 floats
        in x, y).
        """
        ret = self._wrap_call(self._vtk_obj.DrawQuad, *args)
        return ret

    def draw_quad_strip(self, *args):
        """
        V.draw_quad_strip(Points2D)
        C++: void DrawQuadStrip(Points2D *points)
        Draw a strip of quads
        """
        my_args = deref_array(args, [['vtkPoints2D']])
        ret = self._wrap_call(self._vtk_obj.DrawQuadStrip, *my_args)
        return ret

    def draw_rect(self, *args):
        """
        V.draw_rect(float, float, float, float)
        C++: void DrawRect(float x, float y, float w, float h)
        Draw a rectangle with origin at x, y and width w, height h
        """
        ret = self._wrap_call(self._vtk_obj.DrawRect, *args)
        return ret

    def draw_string(self, *args):
        """
        V.draw_string(Points2D, string)
        C++: void DrawString(Points2D *point,
            const StdString &string)
        V.draw_string(float, float, string)
        C++: void DrawString(float x, float y, const StdString &string)
        V.draw_string(Points2D, unicode)
        C++: void DrawString(Points2D *point,
            const UnicodeString &string)
        V.draw_string(float, float, unicode)
        C++: void DrawString(float x, float y,
            const UnicodeString &string)
        Draw some text to the screen.
        """
        my_args = deref_array(args, [('vtkPoints2D', 'string'), ('float', 'float', 'string'), ('vtkPoints2D', 'unicode'), ('float', 'float', 'unicode')])
        ret = self._wrap_call(self._vtk_obj.DrawString, *my_args)
        return ret

    def draw_string_rect(self, *args):
        """
        V.draw_string_rect(Points2D, string)
        C++: void DrawStringRect(Points2D *rect,
            const StdString &string)
        V.draw_string_rect(Points2D, unicode)
        C++: void DrawStringRect(Points2D *rect,
            const UnicodeString &string)
        Draw some text to the screen in a bounding rectangle with the
        alignment of the text properties respecting the rectangle. The
        points should be supplied as bottom corner (x, y), width, height.
        """
        my_args = deref_array(args, [('vtkPoints2D', 'string'), ('vtkPoints2D', 'unicode')])
        ret = self._wrap_call(self._vtk_obj.DrawStringRect, *my_args)
        return ret

    def draw_wedge(self, *args):
        """
        V.draw_wedge(float, float, float, float, float, float)
        C++: void DrawWedge(float x, float y, float outRadius,
            float inRadius, float startAngle, float stopAngle)
        Draw a circular wedge with center at x, y, outer radius
        out_radius, inner radius in_radius between angles start_angle and
        stop_angle (expressed in degrees).
        \pre positive_out_radius: out_radius>=_0
        \pre positive_in_radius: in_radius>=_0
        \pre ordered_radii: in_radius<=out_radius
        """
        ret = self._wrap_call(self._vtk_obj.DrawWedge, *args)
        return ret

    def end(self):
        """
        V.end() -> bool
        C++: bool End()
        Ends painting on the device, you would not usually need to call
        this as it should be called by the destructor. Returns true if
        the painter is no longer active, otherwise false.
        """
        ret = self._vtk_obj.End()
        return ret
        

    def float_to_int(self, *args):
        """
        V.float_to_int(float) -> int
        C++: static int FloatToInt(float x)
        Float to int conversion, performs truncation but with a rounding
        tolerance for float values that are within 1/256 of their closest
        integer.
        """
        ret = self._wrap_call(self._vtk_obj.FloatToInt, *args)
        return ret

    def pop_matrix(self):
        """
        V.pop_matrix()
        C++: void PopMatrix()
        Push/pop the transformation matrix for the painter (sets the
        underlying matrix for the device when available).
        """
        ret = self._vtk_obj.PopMatrix()
        return ret
        

    def push_matrix(self):
        """
        V.push_matrix()
        C++: void PushMatrix()
        Push/pop the transformation matrix for the painter (sets the
        underlying matrix for the device when available).
        """
        ret = self._vtk_obj.PushMatrix()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Context2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Context2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Context2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Context2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

