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


class PixelBufferObject(Object):
    """
    PixelBufferObject - abstracts an open_gl pixel buffer object.
    
    Superclass: Object
    
    Provides low-level access to GPU memory. Used to pass raw data to
    GPU. The data is uploaded into a pixel buffer.
    
    Caveats:
    
    Since most GPUs don't support double format all double data is
    converted to float and then uploaded. DON'T PLAY WITH IT YET.
    
    See Also:
    
    open_gl Pixel Buffer Object Extension Spec (ARB_pixel_buffer_object):
    http://www.opengl.org/registry/specs/ARB/pixel_buffer_object.txt
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPixelBufferObject, obj, update, **traits)
    
    usage = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Usage is a performance hint. Valid values are:
        - stream_draw specified once by A, used few times S
        - stream_read specified once by R, queried a few times by A
        - stream_copy specified once by R, used a few times S
        - static_draw specified once by A, used many times S
        - static_read specificed once by R, queried many times by A
        - static_copy specified once by R, used many times S
        - dynamic_draw respecified repeatedly by A, used many times S
        - dynamic_read respecified repeatedly by R, queried many times by
          A
        - dynamic_copy respecified repeatedly by R, used many times S A:
          the application S: as the source for GL drawing and image
          specification commands. R: reading data from the GL Initial
          value is static_draw, as in open_gl spec.
        """
    )
    def _usage_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUsage,
                        self.usage)

    def _get_context(self):
        return wrap_vtk(self._vtk_obj.GetContext())
    def _set_context(self, arg):
        old_val = self._get_context()
        self._wrap_call(self._vtk_obj.SetContext,
                        deref_vtk(arg))
        self.trait_property_changed('context', old_val, arg)
    context = traits.Property(_get_context, _set_context, help=\
        """
        Get/Set the context. Context must be a OpenGLRenderWindow.
        This does not increase the reference count of the context to
        avoid reference loops. set_context() may raise an error is the
        open_gl context does not support the required open_gl extensions.
        """
    )

    def _get_handle(self):
        return self._vtk_obj.GetHandle()
    handle = traits.Property(_get_handle, help=\
        """
        Get the open_gl buffer handle.
        """
    )

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        Get the size of the data loaded into the GPU. Size is in the
        number of elements of the uploaded Type.
        """
    )

    def _get_type(self):
        return self._vtk_obj.GetType()
    type = traits.Property(_get_type, help=\
        """
        Get the type with which the data is loaded into the GPU. eg.
        VTK_FLOAT for float32, VTK_CHAR for byte, VTK_UNSIGNED_CHAR for
        unsigned byte etc.
        """
    )

    def allocate(self, *args):
        """
        V.allocate(int, int)
        C++: void Allocate(unsigned int size, int type)
        Allocate the memory. size is in number of bytes. type is a VTK
        type.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def bind_to_packed_buffer(self):
        """
        V.bind_to_packed_buffer()
        C++: void BindToPackedBuffer()
        For wrapping.
        """
        ret = self._vtk_obj.BindToPackedBuffer()
        return ret
        

    def bind_to_un_packed_buffer(self):
        """
        V.bind_to_un_packed_buffer()
        C++: void BindToUnPackedBuffer()"""
        ret = self._vtk_obj.BindToUnPackedBuffer()
        return ret
        

    def download1d(self, *args):
        """
        V.download1d(int, , int, int, int) -> bool
        C++: bool Download1D(int type, void *data, unsigned int dim,
            int numcomps, IdType increment)
        Download data from pixel buffer to the 1d array. The length of
        the array must be equal to the size of the data in the memory.
        """
        ret = self._wrap_call(self._vtk_obj.Download1D, *args)
        return ret

    def download2d(self, *args):
        """
        V.download2d(int, , [int, int], int, [int, int]) -> bool
        C++: bool Download2D(int type, void *data, unsigned int dims[2],
            int numcomps, IdType increments[2])
        Download data from pixel buffer to the 2d array. (lengthx *
        lengthy) must be equal to the size of the data in the memory.
        """
        ret = self._wrap_call(self._vtk_obj.Download2D, *args)
        return ret

    def download3d(self, *args):
        """
        V.download3d(int, , [int, int, int], int, [int, int, int]) -> bool
        C++: bool Download3D(int type, void *data, unsigned int dims[3],
            int numcomps, IdType increments[3])
        Download data from pixel buffer to the 3d array. (lengthx *
        lengthy * lengthz) must be equal to the size of the data in the
        memory.
        """
        ret = self._wrap_call(self._vtk_obj.Download3D, *args)
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

    def release_memory(self):
        """
        V.release_memory()
        C++: void ReleaseMemory()
        Release the memory allocated without destroying the PBO handle.
        """
        ret = self._vtk_obj.ReleaseMemory()
        return ret
        

    def un_bind(self):
        """
        V.un_bind()
        C++: void UnBind()
        Inactivate the buffer.
        """
        ret = self._vtk_obj.UnBind()
        return ret
        

    def upload1d(self, *args):
        """
        V.upload1d(int, , int, int, int) -> bool
        C++: bool Upload1D(int type, void *data, unsigned int numtuples,
            int comps, IdType increment)
        Upload data to GPU. The input data can be freed after this call.
        The data ptr is treated as an 1d array with the given number of
        tuples and given number of components in each tuple to be copied
        to the GPU. increment is the offset added after the last
        component in each tuple is transferred. Look at the documentation
        for continuous_increments in ImageData for details about how
        increments are specified.
        """
        ret = self._wrap_call(self._vtk_obj.Upload1D, *args)
        return ret

    def upload2d(self, *args):
        """
        V.upload2d(int, , [int, int], int, [int, int]) -> bool
        C++: bool Upload2D(int type, void *data, unsigned int dims[2],
            int comps, IdType increments[2])
        Update data to GPU sourcing it from a 2d array. The input data
        can be freed after this call. The data ptr is treated as a 2d
        array with increments indicating how to iterate over the data.
        Look at the documentation for continuous_increments in
        ImageData for details about how increments are specified.
        """
        ret = self._wrap_call(self._vtk_obj.Upload2D, *args)
        return ret

    _updateable_traits_ = \
    (('usage', 'GetUsage'), ('reference_count', 'GetReferenceCount'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'usage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PixelBufferObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PixelBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['usage']),
            title='Edit PixelBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PixelBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

