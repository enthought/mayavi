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


class PainterDeviceAdapter(Object):
    """
    PainterDeviceAdapter - An adapter between a Painter and a
    rendering device.
    
    Superclass: Object
    
    This class is an adapter between a Painter and a rendering device
    (such as an open_gl machine).  Having an abstract adapter allows
    Painters to be re-used for any rendering system.
    
    Although VTK really only uses open_gl right now, there are reasons to
    swap out the rendering functions.  Sometimes MESA with mangled names
    is used.  Also, different shader extensions use different functions.
    Furthermore, Cg also has its own interface.
    
    The interface for this class should be familier to anyone experienced
    with open_gl.
    
    See Also:
    
    Painter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPainterDeviceAdapter, obj, update, **traits)
    
    def begin_primitive(self, *args):
        """
        V.begin_primitive(int)
        C++: virtual void BeginPrimitive(int mode)
        Signals the start of sending a primitive to the graphics card. 
        The mode is one of VTK_VERTEX, VTK_POLY_VERTEX, VTK_LINE,
        VTK_POLY_LINE, VTK_TRIANGLE, VTK_TRIANGLE_STRIP, VTK_POLYGON, or
        VTK_QUAD.  The primitive is defined by the attributes sent
        between the calls to begin_primitive and end_primitive.  You do not
        need to call end_primitive/_begin_primitive between primitives that
        have a constant number of points (i.e. VTK_VERTEX, VTK_LINE,
        VTK_TRIANGLE, and VTK_QUAD).
        """
        ret = self._wrap_call(self._vtk_obj.BeginPrimitive, *args)
        return ret

    def compatible(self, *args):
        """
        V.compatible(Renderer) -> int
        C++: virtual int Compatible(Renderer *renderer)
        Returns true if this device adapter is compatable with the given
        Renderer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Compatible, *my_args)
        return ret

    def disable_attribute_array(self, *args):
        """
        V.disable_attribute_array(int)
        C++: virtual void DisableAttributeArray(int index)
        Enable/disable the attribute array set with set_attribute_pointer.
        """
        ret = self._wrap_call(self._vtk_obj.DisableAttributeArray, *args)
        return ret

    def draw_arrays(self, *args):
        """
        V.draw_arrays(int, int, int)
        C++: virtual void DrawArrays(int mode, IdType first,
            IdType count)
        Send a section of the enabled attribute pointers to the graphics
        card to define a primitive.  The mode is one of VTK_VERTEX,
        VTK_POLY_VERTEX, VTK_LINE, VTK_POLY_LINE, VTK_TRIANGLE,
        VTK_TRIANGLE_STRIP, VTK_POLYGON, or VTK_QUAD.  It identifies
        which type of primitive the attribute data is defining.  The
        parameters first and count identify what part of the attribute
        arrays define the given primitive.  If mode is a primitive that
        has a constant number of points (i.e. VTK_VERTEX, VTK_LINE,
        VTK_TRIANGLE, and VTK_QUAD), you may draw multiple primitives
        with one call to draw_arrays.
        """
        ret = self._wrap_call(self._vtk_obj.DrawArrays, *args)
        return ret

    def draw_elements(self, *args):
        """
        V.draw_elements(int, int, int, )
        C++: virtual void DrawElements(int mode, IdType count,
            int type, void *indices)
        Send items in the attribute pointers to the graphics card to
        define a primitive.  The mode is one of VTK_VERTEX,
        VTK_POLY_VERTEX, VTK_LINE, VTK_POLY_LINE, VTK_TRIANGLE,
        VTK_TRIANGLE_STRIP, VTK_POLYGON, or VTK_QUAD.  It identifies
        which type of primitive the attribute data is defining.  The
        indices array holds the list of attribute elements that define
        the primitive.  The count and type parameters give the number and
        data type of the indices array.  The type parameter is a VTK type
        enumeration (VTK_UNSIGNED_INT, ...).  The type should be an
        integer type (for obvious reasons).  If mode is a primitive that
        has a constant number of points (i.e. VTK_VERTEX, VTK_LINE,
        VTK_TRIANGLE, and VTK_QUAD), you may draw multiple primitives
        with one call to draw_arrays.
        """
        ret = self._wrap_call(self._vtk_obj.DrawElements, *args)
        return ret

    def enable_attribute_array(self, *args):
        """
        V.enable_attribute_array(int)
        C++: virtual void EnableAttributeArray(int index)
        Enable/disable the attribute array set with set_attribute_pointer.
        """
        ret = self._wrap_call(self._vtk_obj.EnableAttributeArray, *args)
        return ret

    def end_primitive(self):
        """
        V.end_primitive()
        C++: virtual void EndPrimitive()
        Signals the end of sending a primitive to the graphics card.
        """
        ret = self._vtk_obj.EndPrimitive()
        return ret
        

    def is_attributes_supported(self, *args):
        """
        V.is_attributes_supported(int) -> int
        C++: virtual int IsAttributesSupported(int attribute)
        Returns if the given attribute type is supported by the device.
        Returns 1 is supported, 0 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.IsAttributesSupported, *args)
        return ret

    def make_blending(self, *args):
        """
        V.make_blending(int)
        C++: virtual void MakeBlending(int mode)
        Turns blending on and off.
        """
        ret = self._wrap_call(self._vtk_obj.MakeBlending, *args)
        return ret

    def make_lighting(self, *args):
        """
        V.make_lighting(int)
        C++: virtual void MakeLighting(int mode)
        Turns lighting on and off.
        """
        ret = self._wrap_call(self._vtk_obj.MakeLighting, *args)
        return ret

    def make_multisampling(self, *args):
        """
        V.make_multisampling(int)
        C++: virtual void MakeMultisampling(int mode)
        Turns antialiasing on and off.
        """
        ret = self._wrap_call(self._vtk_obj.MakeMultisampling, *args)
        return ret

    def make_vertex_emphasis(self, *args):
        """
        V.make_vertex_emphasis(bool)
        C++: virtual void MakeVertexEmphasis(bool mode)
        Turns emphasis of vertices on or off for vertex selection.
        """
        ret = self._wrap_call(self._vtk_obj.MakeVertexEmphasis, *args)
        return ret

    def make_vertex_emphasis_with_stencil_check(self, *args):
        """
        V.make_vertex_emphasis_with_stencil_check(int)
        C++: virtual void MakeVertexEmphasisWithStencilCheck(int mode)
        @deprecated
        """
        ret = self._wrap_call(self._vtk_obj.MakeVertexEmphasisWithStencilCheck, *args)
        return ret

    def query_blending(self):
        """
        V.query_blending() -> int
        C++: virtual int QueryBlending()
        Returns current blending setting.
        """
        ret = self._vtk_obj.QueryBlending()
        return ret
        

    def query_lighting(self):
        """
        V.query_lighting() -> int
        C++: virtual int QueryLighting()
        Returns current lighting setting.
        """
        ret = self._vtk_obj.QueryLighting()
        return ret
        

    def query_multisampling(self):
        """
        V.query_multisampling() -> int
        C++: virtual int QueryMultisampling()
        Returns current antialiasing setting.
        """
        ret = self._vtk_obj.QueryMultisampling()
        return ret
        

    def send_attribute(self, *args):
        """
        V.send_attribute(int, int, int, , int)
        C++: virtual void SendAttribute(int index, int components,
            int type, const void *attribute, IdType offset=0)
        Sends a single attribute to the graphics card.  The index
        parameter identifies the attribute.  Some indices have special
        meaning (see Painter for details).  The components parameter
        gives the number of components in the attribute.  In general,
        components must be between 1-4, but a rendering system may impose
        even more constraints.  The type parameter is a VTK type
        enumeration (VTK_FLOAT, VTK_INT, etc.). Again, a rendering system
        may not support all types for all attributes.  The attribute
        parameter is the actual data for the attribute. If offset is
        specified, it is added to attribute pointer after it has been
        casted to the proper type.
        """
        ret = self._wrap_call(self._vtk_obj.SendAttribute, *args)
        return ret

    def send_multi_texture_coords(self, *args):
        """
        V.send_multi_texture_coords(int, int, , int, int)
        C++: virtual void SendMultiTextureCoords(int numcomp, int type,
            const void *attribute, int idx, IdType offset)
        Calls gl_multi_tex
        """
        ret = self._wrap_call(self._vtk_obj.SendMultiTextureCoords, *args)
        return ret

    def set_attribute_pointer(self, *args):
        """
        V.set_attribute_pointer(int, DataArray)
        C++: void SetAttributePointer(int index,
            DataArray *attributeArray)
        V.set_attribute_pointer(int, int, int, int, )
        C++: virtual void SetAttributePointer(int index,
            int numcomponents, int type, int stride, const void *pointer)
        Sets an array of attributes.  This allows you to send all the
        data for a particular attribute with one call, thus greatly
        reducing function call overhead.  Once set, the array is enabled
        with enable_attribute_array, and the data is sent with a call to
        draw_arrays draw_elements.
        """
        my_args = deref_array(args, [('int', 'vtkDataArray'), ('int', 'int', 'int', 'int', 'string')])
        ret = self._wrap_call(self._vtk_obj.SetAttributePointer, *my_args)
        return ret

    def stencil(self, *args):
        """
        V.stencil(int)
        C++: virtual void Stencil(int on)
        Control use of the stencil buffer (for vertex selection).
        """
        ret = self._wrap_call(self._vtk_obj.Stencil, *args)
        return ret

    def test_stencil(self, *args):
        """
        V.test_stencil(int)
        C++: virtual void TestStencil(IdType value)
        Control use of the stencil buffer (for vertex selection).
        """
        ret = self._wrap_call(self._vtk_obj.TestStencil, *args)
        return ret

    def write_stencil(self, *args):
        """
        V.write_stencil(int)
        C++: virtual void WriteStencil(IdType value)
        Control use of the stencil buffer (for vertex selection).
        """
        ret = self._wrap_call(self._vtk_obj.WriteStencil, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PainterDeviceAdapter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PainterDeviceAdapter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit PainterDeviceAdapter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PainterDeviceAdapter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

