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


class TextureObject(Object):
    """
    TextureObject - abstracts an open_gl texture object.
    
    Superclass: Object
    
    TextureObject represents an open_gl texture object. It provides API
    to create textures using data already loaded into pixel buffer
    objects. It can also be used to create textures without uploading any
    data.
    
    Caveats:
    
    DON'T PLAY WITH IT YET.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextureObject, obj, update, **traits)
    
    border_color = traits.Array(shape=(4,), value=(0.0, 0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _border_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorderColor,
                        self.border_color)

    priority = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Priority of the texture object to be resident on the card for
        higher performance in the range [0.0f,1.0f]. Initial value is
        1.0f, as in open_gl spec.
        """
    )
    def _priority_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPriority,
                        self.priority)

    wrap_s = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Wrap mode for the first texture coordinate "s" Valid values are:
        - Clamp
        - clamp_to_edge
        - Repeat
        - clamp_to_border
        - mirrored_repeat Initial value is Repeat (as in open_gl spec)
        """
    )
    def _wrap_s_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrapS,
                        self.wrap_s)

    generate_mipmap = traits.Bool(False, help=\
        """
        Tells the hardware to generate mipmap textures from the first
        texture image at base_level. Initial value is false, as in open_gl
        spec.
        """
    )
    def _generate_mipmap_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateMipmap,
                        self.generate_mipmap)

    wrap_t = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Wrap mode for the first texture coordinate "t" Valid values are:
        - Clamp
        - clamp_to_edge
        - Repeat
        - clamp_to_border
        - mirrored_repeat Initial value is Repeat (as in open_gl spec)
        """
    )
    def _wrap_t_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrapT,
                        self.wrap_t)

    base_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Level of detail of the first texture image. A texture object is a
        list of texture images. It is a non-negative integer value.
        Initial value is 0, as in open_gl spec.
        """
    )
    def _base_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBaseLevel,
                        self.base_level)

    max_lod = traits.Float(1000.0, enter_set=True, auto_set=False, help=\
        """
        Upper-clamp the computed LOD against this value. Any float value
        is valid. Initial value is 1000.0f, as in open_gl spec.
        """
    )
    def _max_lod_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxLOD,
                        self.max_lod)

    depth_texture_compare_function = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        In case depth_texture_compare is true, specify the comparison
        function in use. The result of the comparison is noted `r'. Valid
        values are:
        - Value
        - Lequal: r=R<=Dt ? 1.0 : 0.0
        - Gequal: r=R>=Dt ? 1.0 : 0.0
        - Less: r=R<D_t ? 1.0 : 0.0
        - Greater: r=R>Dt ? 1.0 : 0.0
        - Equal: r=R==Dt ? 1.0 : 0.0
        - not_equal: r=R!=Dt ? 1.0 : 0.0
        - always_true: r=1.0
        - Never: r=0.0 If the magnification of minification factor are
          not nearest, percentage closer filtering (PCF) is used: R is
          compared to several D_t and r is the average of the comparisons
        (it is NOT the average of D_t compared once to R). Initial value
          is Lequal, as in open_gl spec. Ignored if the texture object is
          not a depth texture.
        """
    )
    def _depth_texture_compare_function_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthTextureCompareFunction,
                        self.depth_texture_compare_function)

    min_lod = traits.Float(-1000.0, enter_set=True, auto_set=False, help=\
        """
        Lower-clamp the computed LOD against this value. Any float value
        is valid. Initial value is -1000.0f, as in open_gl spec.
        """
    )
    def _min_lod_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinLOD,
                        self.min_lod)

    minification_filter = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Minification filter mode. Valid values are:
        - Nearest
        - Linear
        - nearest_mipmap_nearest
        - nearest_mipmap_linear
        - linear_mipmap_nearest
        - linear_mipmap_linear Initial value is Nearest (note initial value
        in open_gl spec is nearest_mip_map_linear but this is error-prone
          because it makes the texture object incomplete. ).
        """
    )
    def _minification_filter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinificationFilter,
                        self.minification_filter)

    linear_magnification = traits.Bool(False, help=\
        """
        Tells if the magnification mode is linear (true) or nearest
        (false). Initial value is false (initial value in open_gl spec is
        true).
        """
    )
    def _linear_magnification_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLinearMagnification,
                        self.linear_magnification)

    depth_texture_compare = traits.Bool(False, help=\
        """
        Tells if the output of a texture unit with a depth texture uses
        comparison or not. Comparison happens between D_t the depth
        texture value in the range [0,1] and with R the interpolated
        third texture coordinate clamped to range [0,1]. The result of
        the comparison is noted `r'. If this flag is false, r=D_t.
        Initial value is false, as in open_gl spec. Ignored if the texture
        object is not a depth texture.
        """
    )
    def _depth_texture_compare_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthTextureCompare,
                        self.depth_texture_compare)

    wrap_r = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Wrap mode for the first texture coordinate "r" Valid values are:
        - Clamp
        - clamp_to_edge
        - Repeat
        - clamp_to_border
        - mirrored_repeat Initial value is Repeat (as in open_gl spec)
        """
    )
    def _wrap_r_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrapR,
                        self.wrap_r)

    def _get_context(self):
        return wrap_vtk(self._vtk_obj.GetContext())
    def _set_context(self, arg):
        old_val = self._get_context()
        self._wrap_call(self._vtk_obj.SetContext,
                        deref_vtk(arg))
        self.trait_property_changed('context', old_val, arg)
    context = traits.Property(_get_context, _set_context, help=\
        """
        Get/Set the context. This does not increase the reference count
        of the context to avoid reference loops. set_context() may raise
        an error is the open_gl context does not support the required
        open_gl extensions.
        """
    )

    max_level = traits.Int(1000, enter_set=True, auto_set=False, help=\
        """
        Level of detail of the first texture image. A texture object is a
        list of texture images. It is a non-negative integer value.
        Initial value is 1000, as in open_gl spec.
        """
    )
    def _max_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxLevel,
                        self.max_level)

    depth_texture_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Defines the mapping from depth component `r' to RGBA components.
        Ignored if the texture object is not a depth texture. Valid modes
        are:
        - Luminance: (R,G,B,A)=(r,r,r,1)
        - Intensity: (R,G,B,A)=(r,r,r,r)
        - Alpha: (R.G.B.A)=(0,0,0,r) Initial value is Luminance, as in
          open_gl spec.
        """
    )
    def _depth_texture_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthTextureMode,
                        self.depth_texture_mode)

    def _get_components(self):
        return self._vtk_obj.GetComponents()
    components = traits.Property(_get_components, help=\
        """
        Get the texture dimensions. These are the properties of the
        open_gl texture this instance represents.
        """
    )

    def _get_data_type(self):
        return self._vtk_obj.GetDataType()
    data_type = traits.Property(_get_data_type, help=\
        """
        Get the data type for the texture as a vtk type int i.e. VTK_INT
        etc.
        """
    )

    def _get_depth(self):
        return self._vtk_obj.GetDepth()
    depth = traits.Property(_get_depth, help=\
        """
        Get the texture dimensions. These are the properties of the
        open_gl texture this instance represents.
        """
    )

    def get_format(self, *args):
        """
        V.get_format(int, int, bool) -> int
        C++: unsigned int GetFormat(int vtktype, int numComps,
            bool shaderSupportsTextureInt)"""
        ret = self._wrap_call(self._vtk_obj.GetFormat, *args)
        return ret

    def _get_handle(self):
        return self._vtk_obj.GetHandle()
    handle = traits.Property(_get_handle, help=\
        """
        Returns the open_gl handle.
        """
    )

    def _get_height(self):
        return self._vtk_obj.GetHeight()
    height = traits.Property(_get_height, help=\
        """
        Get the texture dimensions. These are the properties of the
        open_gl texture this instance represents.
        """
    )

    def get_internal_format(self, *args):
        """
        V.get_internal_format(int, int, bool) -> int
        C++: unsigned int GetInternalFormat(int vtktype, int numComps,
            bool shaderSupportsTextureInt)"""
        ret = self._wrap_call(self._vtk_obj.GetInternalFormat, *args)
        return ret

    def _get_number_of_dimensions(self):
        return self._vtk_obj.GetNumberOfDimensions()
    number_of_dimensions = traits.Property(_get_number_of_dimensions, help=\
        """
        
        """
    )

    def _get_target(self):
        return self._vtk_obj.GetTarget()
    target = traits.Property(_get_target, help=\
        """
        Returns open_gl texture target to which the texture is/can be
        bound.
        """
    )

    def _get_width(self):
        return self._vtk_obj.GetWidth()
    width = traits.Property(_get_width, help=\
        """
        Get the texture dimensions. These are the properties of the
        open_gl texture this instance represents.
        """
    )

    def allocate1d(self, *args):
        """
        V.allocate1d(int, int, int) -> bool
        C++: bool Allocate1D(unsigned int width, int numComps,
            int Type)
        Create a 1d color texture but does not initialize its values.
        Internal format is deduced from num_comps and Type.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate1D, *args)
        return ret

    def allocate2d(self, *args):
        """
        V.allocate2d(int, int, int, int) -> bool
        C++: bool Allocate2D(unsigned int width, unsigned int height,
            int numComps, int Type)
        Create a 2d color texture but does not initialize its values.
        Internal format is deduced from num_comps and Type.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate2D, *args)
        return ret

    def allocate3d(self, *args):
        """
        V.allocate3d(int, int, int, int, int) -> bool
        C++: bool Allocate3D(unsigned int width, unsigned int height,
            unsigned int depth, int numComps, int Type)
        Create a 3d color texture but does not initialize its values.
        Internal format is deduced from num_comps and Type.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate3D, *args)
        return ret

    def allocate_depth(self, *args):
        """
        V.allocate_depth(int, int, int) -> bool
        C++: bool AllocateDepth(unsigned int width, unsigned int height,
            int internalFormat)
        Create a 2d depth texture but does not initialize its values.
        """
        ret = self._wrap_call(self._vtk_obj.AllocateDepth, *args)
        return ret

    def bind(self):
        """
        V.bind()
        C++: void Bind()
        Activate the texture. The texture must have been created using
        Create(). render_window must be set before calling this.
        """
        ret = self._vtk_obj.Bind()
        return ret
        

    def copy_from_frame_buffer(self, *args):
        """
        V.copy_from_frame_buffer(int, int, int, int, int, int)
        C++: void CopyFromFrameBuffer(int srcXmin, int srcYmin,
            int dstXmin, int dstYmin, int width, int height)
        Copy a sub-part of a logical buffer of the framebuffer (color or
        depth) to the texture object. src is the framebuffer, dst is the
        texture. (src_xmin,src_ymin) is the location of the lower left
        corner of the rectangle in the framebuffer. (dst_xmin,dst_ymin) is
        the location of the lower left corner of the rectangle in the
        texture. width and height specifies the size of the rectangle in
        pixels. If the logical buffer is a color buffer, it has to be
        selected first with gl_read_buffer().
        \pre is_2d: get_number_of_dimensions()==_2
        """
        ret = self._wrap_call(self._vtk_obj.CopyFromFrameBuffer, *args)
        return ret

    def copy_to_frame_buffer(self, *args):
        """
        V.copy_to_frame_buffer(int, int, int, int, int, int, int, int)
        C++: void CopyToFrameBuffer(int srcXmin, int srcYmin, int srcXmax,
             int srcYmax, int dstXmin, int dstYmin, int width, int height)
        Copy a sub-part of the texture (src) in the current framebuffer
        at location (dst_xmin,dst_ymin). (dst_xmin,dst_ymin) is the location
        of the lower left corner of the rectangle. width and height are
        the dimensions of the framebuffer.
        - texture coordinates are sent on texture coordinate processing
          unit 0.
        - if the fixed-pipeline fragment shader is used, texturing has to
        be set on texture image unit 0 and the texture object has to be
          bound on texture image unit 0.
        - if a customized fragment shader is used, you are free to pick
          the texture image unit you want. You can even have multiple
          texture objects attached on multiple texture image units. In
          this case, you call this method only on one of them.
        \pre positive_src_xmin: src_xmin>=_0
        \pre max_src_xmax: src_xmax<this->_get_width()
        \pre increasing_x: src_xmin<=src_xmax
        \pre positive_src_ymin: src_ymin>=_0
        \pre max_src_ymax: src_ymax<this->_get_height()
        \pre increasing_y: src_ymin<=src_ymax
        \pre positive_dst_xmin: dst_xmin>=_0
        \pre positive_dst_ymin: dst_ymin>=_0
        \pre positive_width: width>0
        \pre positive_height: height>0
        \pre x_fit: dest_xmin+(src_xmax-src_xmin)<width
        \pre y_fit: dest_ymin+(src_ymax-src_ymin)<height
        """
        ret = self._wrap_call(self._vtk_obj.CopyToFrameBuffer, *args)
        return ret

    def create1d(self, *args):
        """
        V.create1d(int, PixelBufferObject, bool) -> bool
        C++: bool Create1D(int numComps, PixelBufferObject *pbo,
            bool shaderSupportsTextureInt)
        Create a 1d texture using the PBO. Eventually we may start
        supporting creating a texture from subset of data in the PBO, but
        for simplicity we'll begin with entire PBO data. num_comps must be
        in [1-4]. shader_supports_texture_int is true if the shader has an
        alternate implementation supporting sampler with integer values.
        Even if the card supports texture int, it does not mean that the
        implementor of the shader made a version that supports texture
        int.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Create1D, *my_args)
        return ret

    def create2d(self, *args):
        """
        V.create2d(int, int, int, PixelBufferObject, bool) -> bool
        C++: bool Create2D(unsigned int width, unsigned int height,
            int numComps, PixelBufferObject *pbo,
            bool shaderSupportsTextureInt)
        V.create2d(int, int, int, int, bool) -> bool
        C++: bool Create2D(unsigned int width, unsigned int height,
            int numComps, int vtktype, bool shaderSupportsTextureInt)
        Create a 2d texture using the PBO. Eventually we may start
        supporting creating a texture from subset of data in the PBO, but
        for simplicity we'll begin with entire PBO data. num_comps must be
        in [1-4].
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Create2D, *my_args)
        return ret

    def create3d(self, *args):
        """
        V.create3d(int, int, int, int, PixelBufferObject, bool) -> bool
        C++: bool Create3D(unsigned int width, unsigned int height,
            unsigned int depth, int numComps, PixelBufferObject *pbo,
            bool shaderSupportsTextureInt)
        V.create3d(int, int, int, int, int, bool) -> bool
        C++: bool Create3D(unsigned int width, unsigned int height,
            unsigned int depth, int numComps, int vtktype,
            bool shaderSupportsTextureInt)
        Create a 3d texture using the PBO. Eventually we may start
        supporting creating a texture from subset of data in the PBO, but
        for simplicity we'll begin with entire PBO data. num_comps must be
        in [1-4].
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Create3D, *my_args)
        return ret

    def create_depth(self, *args):
        """
        V.create_depth(int, int, int, PixelBufferObject) -> bool
        C++: bool CreateDepth(unsigned int width, unsigned int height,
            int internalFormat, PixelBufferObject *pbo)
        Create a 2d depth texture using a PBO.
        \pre: valid_internal_format: internal_format>=_0 &&
            internal_format<_number_of_depth_formats
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateDepth, *my_args)
        return ret

    def create_depth_from_raw(self, *args):
        """
        V.create_depth_from_raw(int, int, int, int, ) -> bool
        C++: bool CreateDepthFromRaw(unsigned int width,
            unsigned int height, int internalFormat, int rawType,
            void *raw)
        Create a 2d depth texture using a raw pointer. This is a blocking
        call. If you can, use PBO instead.
        """
        ret = self._wrap_call(self._vtk_obj.CreateDepthFromRaw, *args)
        return ret

    def download(self):
        """
        V.download() -> PixelBufferObject
        C++: PixelBufferObject *Download()
        This is used to download raw data from the texture into a pixel
        bufer. The pixel buffer API can then be used to download the
        pixel buffer data to CPU arrays. The caller takes on the
        responsibility of deleting the returns PixelBufferObject once
        it done with it.
        """
        ret = wrap_vtk(self._vtk_obj.Download())
        return ret
        

    def is_bound(self):
        """
        V.is_bound() -> bool
        C++: bool IsBound()
        Tells if the texture object is bound to the active texture image
        unit. (a texture object can be bound to multiple texture image
        unit).
        """
        ret = self._vtk_obj.IsBound()
        return ret
        

    def is_supported(self, *args):
        """
        V.is_supported(RenderWindow) -> bool
        C++: static bool IsSupported(RenderWindow *renWin)
        Returns if the context supports the required extensions.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsSupported, *my_args)
        return ret

    def send_parameters(self):
        """
        V.send_parameters()
        C++: void SendParameters()
        Send all the texture object parameters to the hardware if not
        done yet.
        \pre is_bound: is_bound()
        """
        ret = self._vtk_obj.SendParameters()
        return ret
        

    def un_bind(self):
        """
        V.un_bind()
        C++: void UnBind()
        Activate the texture. The texture must have been created using
        Create(). render_window must be set before calling this.
        """
        ret = self._vtk_obj.UnBind()
        return ret
        

    _updateable_traits_ = \
    (('depth_texture_compare_function', 'GetDepthTextureCompareFunction'),
    ('max_lod', 'GetMaxLOD'), ('max_level', 'GetMaxLevel'),
    ('depth_texture_mode', 'GetDepthTextureMode'), ('border_color',
    'GetBorderColor'), ('linear_magnification', 'GetLinearMagnification'),
    ('debug', 'GetDebug'), ('wrap_t', 'GetWrapT'), ('wrap_s', 'GetWrapS'),
    ('depth_texture_compare', 'GetDepthTextureCompare'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('generate_mipmap', 'GetGenerateMipmap'), ('base_level',
    'GetBaseLevel'), ('priority', 'GetPriority'), ('minification_filter',
    'GetMinificationFilter'), ('min_lod', 'GetMinLOD'),
    ('reference_count', 'GetReferenceCount'), ('wrap_r', 'GetWrapR'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'base_level', 'border_color',
    'depth_texture_compare', 'depth_texture_compare_function',
    'depth_texture_mode', 'generate_mipmap', 'linear_magnification',
    'max_level', 'max_lod', 'min_lod', 'minification_filter', 'priority',
    'wrap_r', 'wrap_s', 'wrap_t'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextureObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TextureObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['base_level', 'border_color',
            'depth_texture_compare', 'depth_texture_compare_function',
            'depth_texture_mode', 'generate_mipmap', 'linear_magnification',
            'max_level', 'max_lod', 'min_lod', 'minification_filter', 'priority',
            'wrap_r', 'wrap_s', 'wrap_t']),
            title='Edit TextureObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextureObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

