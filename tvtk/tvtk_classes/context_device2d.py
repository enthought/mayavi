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


class ContextDevice2D(Object):
    """
    ContextDevice2D - Abstract class for drawing 2d primitives.
    
    Superclass: Object
    
    This defines the interface for a ContextDevice2D. In this sense a
    context_device is a class used to paint 2d primitives onto a device,
    such as an open_gl context or a q_graphics_view.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextDevice2D, obj, update, **traits)
    
    def get_matrix(self, *args):
        """
        V.get_matrix(Matrix3x3)
        C++: virtual void GetMatrix(Matrix3x3 *m)
        Set the model view matrix for the display
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetMatrix, *my_args)
        return ret

    def set_matrix(self, *args):
        """
        V.set_matrix(Matrix3x3)
        C++: virtual void SetMatrix(Matrix3x3 *m)
        Set the model view matrix for the display
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMatrix, *my_args)
        return ret

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
        Tell if the device context is in buffer_id creation mode. Initial
        value is false.
        """
    )

    def _get_height(self):
        return self._vtk_obj.GetHeight()
    height = traits.Property(_get_height, help=\
        """
        Get the width of the device in pixels.
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

    def _get_width(self):
        return self._vtk_obj.GetWidth()
    width = traits.Property(_get_width, help=\
        """
        Get the width of the device in pixels.
        """
    )

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
        V.begin(Viewport)
        C++: virtual void Begin(Viewport *)
        Begin drawing, pass in the viewport to set up the view.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Begin, *my_args)
        return ret

    def buffer_id_mode_begin(self, *args):
        """
        V.buffer_id_mode_begin(AbstractContextBufferId)
        C++: virtual void BufferIdModeBegin(
            AbstractContextBufferId *bufferId)
        Start buffer_id creation Mode. The default implementation is
        empty.
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
        C++: virtual void BufferIdModeEnd()
        Finalize buffer_id creation Mode. It makes sure that the content
        of the buffer_id passed in argument of buffer_id_mode_begin() is
        correctly set. The default implementation is empty.
        \pre started: get_buffer_id_mode()
        \post done: !_get_buffer_id_mode()
        """
        ret = self._vtk_obj.BufferIdModeEnd()
        return ret
        

    def compute_string_bounds(self, *args):
        """
        V.compute_string_bounds(string, [float, float, float, float])
        C++: virtual void ComputeStringBounds(const StdString &string,
            float bounds[4])
        V.compute_string_bounds(unicode, [float, float, float, float])
        C++: virtual void ComputeStringBounds(
            const UnicodeString &string, float bounds[4])
        Compute the bounds of the supplied string. The bounds will be
        copied to the supplied bounds variable, the first two elements
        are the bottom corner of the string, and the second two elements
        are the width and height of the bounding box. NOTE: This function
        does not take account of the text rotation.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeStringBounds, *args)
        return ret

    def disable_clipping(self):
        """
        V.disable_clipping()
        C++: virtual void DisableClipping()
        Disable clipping of the display.
        """
        ret = self._vtk_obj.DisableClipping()
        return ret
        

    def draw_ellipse_wedge(self, *args):
        """
        V.draw_ellipse_wedge(float, float, float, float, float, float,
            float, float)
        C++: virtual void DrawEllipseWedge(float x, float y, float outRx,
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
        C++: virtual void DrawEllipticArc(float x, float y, float rX,
            float rY, float startAngle, float stopAngle)
        Draw an elliptic arc with center at x,y with radii r_x and r_y
        between angles start_angle and stop_angle (expressed in degrees).
        \pre positive_r_x: r_x>=_0
        \pre positive_r_y: r_y>=_0
        """
        ret = self._wrap_call(self._vtk_obj.DrawEllipticArc, *args)
        return ret

    def draw_image(self, *args):
        """
        V.draw_image([float, float], float, ImageData)
        C++: virtual void DrawImage(float p[2], float scale,
            ImageData *image)
        Draw the supplied image at the given x, y (p[0], p[1]) (bottom
        corner), scaled by scale (1.0 would match the image).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawImage, *my_args)
        return ret

    def end(self):
        """
        V.end()
        C++: virtual void End()
        End drawing, clean up the view.
        """
        ret = self._vtk_obj.End()
        return ret
        

    def multiply_matrix(self, *args):
        """
        V.multiply_matrix(Matrix3x3)
        C++: virtual void MultiplyMatrix(Matrix3x3 *m)
        Multiply the current model view matrix by the supplied one
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MultiplyMatrix, *my_args)
        return ret

    def pop_matrix(self):
        """
        V.pop_matrix()
        C++: virtual void PopMatrix()
        Pop the current matrix off of the stack.
        """
        ret = self._vtk_obj.PopMatrix()
        return ret
        

    def push_matrix(self):
        """
        V.push_matrix()
        C++: virtual void PushMatrix()
        Push the current matrix onto the stack.
        """
        ret = self._vtk_obj.PushMatrix()
        return ret
        

    def set_color4(self, *args):
        """
        V.set_color4([, , , ])
        C++: virtual void SetColor4(unsigned char color[4])
        Set the color for the device using unsigned char of length 4,
        RGBA.
        """
        ret = self._wrap_call(self._vtk_obj.SetColor4, *args)
        return ret

    def set_line_type(self, *args):
        """
        V.set_line_type(int)
        C++: virtual void SetLineType(int type)
        Set the line type type (using anonymous enum in Pen).
        """
        ret = self._wrap_call(self._vtk_obj.SetLineType, *args)
        return ret

    def set_line_width(self, *args):
        """
        V.set_line_width(float)
        C++: virtual void SetLineWidth(float width)
        Set the line width.
        """
        ret = self._wrap_call(self._vtk_obj.SetLineWidth, *args)
        return ret

    def set_point_size(self, *args):
        """
        V.set_point_size(float)
        C++: virtual void SetPointSize(float size)
        Set the point size for glyphs/sprites.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointSize, *args)
        return ret

    def set_texture(self, *args):
        """
        V.set_texture(ImageData, int)
        C++: virtual void SetTexture(ImageData *image, int properties)
        Set the texture for the device, it is used to fill the polygons
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTexture, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('matrix', 'GetMatrix'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'matrix'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContextDevice2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextDevice2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['matrix']),
            title='Edit ContextDevice2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextDevice2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

