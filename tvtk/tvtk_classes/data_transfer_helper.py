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


class DataTransferHelper(Object):
    """
    DataTransferHelper - is a helper class that aids in transferring
    
    Superclass: Object
    
    DataTransferHelper is a helper class that aids in transferring
    data
     between the CPU memory and the GPU memory. The data in GPU memory is
     stored as textures which that in CPU memory is stored as
    DataArray.
     DataTransferHelper provides API to transfer only a sub-extent of
    CPU
     structured data to/from the GPU.
    
    See Also:
    
    
     PixelBufferObject TextureObject OpenGLExtensionManager
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataTransferHelper, obj, update, **traits)
    
    cpu_extent = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _cpu_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCPUExtent,
                        self.cpu_extent)

    def _get_texture(self):
        return wrap_vtk(self._vtk_obj.GetTexture())
    def _set_texture(self, arg):
        old_val = self._get_texture()
        self._wrap_call(self._vtk_obj.SetTexture,
                        deref_vtk(arg))
        self.trait_property_changed('texture', old_val, arg)
    texture = traits.Property(_get_texture, _set_texture, help=\
        """
        Get/Set the GPU data buffer. Initial value is 0.
        """
    )

    gpu_extent = traits.Array(shape=(6,), value=(0, 0, 0, 0, 0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _gpu_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGPUExtent,
                        self.gpu_extent)

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

    shader_supports_texture_int = traits.Bool(False, help=\
        """
        
        """
    )
    def _shader_supports_texture_int_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShaderSupportsTextureInt,
                        self.shader_supports_texture_int)

    min_texture_dimension = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Define the minimal dimension of the texture regardless of the
        dimensions of the texture_extent. Initial value is 1. A texture
        extent can have a given dimension 0d (one value), 1d, 2d or 3d.
        By default 0d and 1d are translated into a 1d texture, 2d is
        translated into a 2d texture, 3d is translated into a 3d texture.
        To make life easier when writting GLSL code and use only one type
        of sampler (ex: sampler2d), the default behavior can be changed
        by forcing a type of texture with this ivar. 1: default behavior.
        Initial value. 2: force 0d and 1d to be in a 2d texture 3: force
        0d, 1d and 2d texture to be in a 3d texture.
        """
    )
    def _min_texture_dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinTextureDimension,
                        self.min_texture_dimension)

    def _get_array(self):
        return wrap_vtk(self._vtk_obj.GetArray())
    def _set_array(self, arg):
        old_val = self._get_array()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetArray,
                        my_arg[0])
        self.trait_property_changed('array', old_val, arg)
    array = traits.Property(_get_array, _set_array, help=\
        """
        Get/Set the CPU data buffer. Initial value is 0.
        """
    )

    texture_extent = traits.Array(shape=(6,), value=(0, -1, 0, -1, 0, -1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _texture_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureExtent,
                        self.texture_extent)

    def _get_cpu_extent_is_valid(self):
        return self._vtk_obj.GetCPUExtentIsValid()
    cpu_extent_is_valid = traits.Property(_get_cpu_extent_is_valid, help=\
        """
        Tells if CPUExtent is valid. True if min extent<=max extent.
        """
    )

    def _get_gpu_extent_is_valid(self):
        return self._vtk_obj.GetGPUExtentIsValid()
    gpu_extent_is_valid = traits.Property(_get_gpu_extent_is_valid, help=\
        """
        Tells if GPUExtent is valid. True if min extent<=max extent.
        """
    )

    def _get_texture_extent_is_valid(self):
        return self._vtk_obj.GetTextureExtentIsValid()
    texture_extent_is_valid = traits.Property(_get_texture_extent_is_valid, help=\
        """
        Tells if texture_extent is valid. True if min extent<=max extent.
        """
    )

    def download(self):
        """
        V.download() -> bool
        C++: bool Download()
        old comment: Downlad Extent from GPU data buffer to CPU. GPU data
        size must exactly match Extent. CPU data buffer will be resized
        to match whole_extent in which only the Extent will be filled with
        the GPU data. new comment: Download GPUExtent from GPU texture to
        CPU DataArray. If Array is not provided, it will be created
        with the size of CPUExtent. But only the tuples covered by
        GPUExtent will be download. In this case, if GPUExtent does not
        cover all GPUExtent, some of the DataArray will be
        uninitialized. Reminder: A=>B <=> !A||B
        \pre texture_exists: texture!=0
        \pre array_not_empty: array==0 || array->_get_number_of_tuples()>_0
        \pre valid_cpu_extent: this->_get_cpu_extent_is_valid()
        \pre valid_cpu_extent_size: array==0 ||
            (CPUExtent[1]-CPUExtent[0]+1)*(CPUExtent[3]-CPUExtent[2]+1)*(C
            pu_extent[_5]-_cpu_extent[_4]+_1)==array->_get_number_of_tuples()
        \pre valid_gpu_extent: this->_get_gpu_extent_is_valid()
        \pre gpu_extent_in_cpu_extent: CPUExtent[0]<=GPUExtent[0] &&
            GPUExtent[1]<=CPUExtent[1] && CPUExtent[2]<=GPUExtent[2] &&
            GPUExtent[3]<=CPUExtent[3] && CPUExtent[4]<=GPUExtent[4] &&
            GPUExtent[5]<=CPUExtent[5]
        \pre gpu_texture_size: !this->_get_texture_extent_is_valid() ||
            (GPUExtent[1]-GPUExtent[0]+1)*(GPUExtent[3]-GPUExtent[2]+1)*(G
            pu_extent[_5]-_gpu_extent[_4]+_1)==(_texture_extent[_1]-_texture_extent[_0
            ]+_1)*(_texture_extent[_3]-_texture_extent[_2]+_1)*(_texture_extent[_5]-_t
            exture_extent[_4]+_1)
        \pre valid_components: array==0 ||
            array->_get_number_of_components()<=_4
        \pre components_match: array==0 ||
            (texture->_get_components()==array->_get_number_of_components())
        """
        ret = self._vtk_obj.Download()
        return ret
        

    def download_async1(self):
        """
        V.download_async1() -> bool
        C++: bool DownloadAsync1()
        Splits the download in two operations
        * Asynchronously download from texture memory to PBO
          (_download_async1()).
        * Copy from pbo to user array (_download_async2()).
        """
        ret = self._vtk_obj.DownloadAsync1()
        return ret
        

    def download_async2(self):
        """
        V.download_async2() -> bool
        C++: bool DownloadAsync2()
        Splits the download in two operations
        * Asynchronously download from texture memory to PBO
          (_download_async1()).
        * Copy from pbo to user array (_download_async2()).
        """
        ret = self._vtk_obj.DownloadAsync2()
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

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('texture_extent', 'GetTextureExtent'),
    ('shader_supports_texture_int', 'GetShaderSupportsTextureInt'),
    ('min_texture_dimension', 'GetMinTextureDimension'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('gpu_extent',
    'GetGPUExtent'), ('reference_count', 'GetReferenceCount'),
    ('cpu_extent', 'GetCPUExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'cpu_extent', 'gpu_extent',
    'min_texture_dimension', 'shader_supports_texture_int',
    'texture_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataTransferHelper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataTransferHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['cpu_extent', 'gpu_extent',
            'min_texture_dimension', 'shader_supports_texture_int',
            'texture_extent']),
            title='Edit DataTransferHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataTransferHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

