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


class ShaderProgram(Object):
    """
    ShaderProgram
    
    Superclass: Object
    
    ShaderProgram is a superclass for managing Hardware Shaders
    defined in the XML Material file and interfacing VTK to those
    shaders. It's concrete descendants are responsible for installing
    vertex and fragment programs to the graphics hardware.
    
    Shader Operations are shader library operations that are performed:
    
    on individual shaders, that is, without consideration of the partner
    shader.
    
    Program Operations are shader library operations that treat the:
    
    vertex and fragment shader as a single unit.
    
    Design:
    
    This class is a Strategy pattern for 'Program' operations, which
    treat vertex/fragment shader pairs as a single 'Program', as required
    by some shader libraries (GLSL). Typically, 'Shader' operations are
    delegated to instances of Shader (managed by descendants of this
    class) while 'Program' operations are handled by descendants of this
    class, CgShaderProgram, GLSLShaderProgram.
    
    See Also:
    
    CgShaderProgram, GLSLShaderProgram
    
    Thanks:
    
    Shader support in VTK includes key contributions by Gary Templet at
    Sandia National Labs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShaderProgram, obj, update, **traits)
    
    def _get_material(self):
        return wrap_vtk(self._vtk_obj.GetMaterial())
    def _set_material(self, arg):
        old_val = self._get_material()
        self._wrap_call(self._vtk_obj.SetMaterial,
                        deref_vtk(arg))
        self.trait_property_changed('material', old_val, arg)
    material = traits.Property(_get_material, _set_material, help=\
        """
        
        """
    )

    def _get_number_of_shaders(self):
        return self._vtk_obj.GetNumberOfShaders()
    number_of_shaders = traits.Property(_get_number_of_shaders, help=\
        """
        Returns the number of shaders available in this shader program.
        """
    )

    def _get_shader_device_adapter(self):
        return wrap_vtk(self._vtk_obj.GetShaderDeviceAdapter())
    shader_device_adapter = traits.Property(_get_shader_device_adapter, help=\
        """
        Get the ShaderDeviceAdapter which can be used to execute this
        shader program.
        """
    )

    def add_shader(self, *args):
        """
        V.add_shader(Shader) -> int
        C++: int AddShader(Shader *shader)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddShader, *my_args)
        return ret

    def create_shader_program(self, *args):
        """
        V.create_shader_program(int) -> ShaderProgram
        C++: static ShaderProgram *CreateShaderProgram(int type)"""
        ret = self._wrap_call(self._vtk_obj.CreateShaderProgram, *args)
        return wrap_vtk(ret)

    def new_shader_iterator(self):
        """
        V.new_shader_iterator() -> CollectionIterator
        C++: CollectionIterator *NewShaderIterator()
        Returns a new iterator to iterate over the shaders.
        """
        ret = wrap_vtk(self._vtk_obj.NewShaderIterator())
        return ret
        

    def post_render(self, *args):
        """
        V.post_render(Actor, Renderer)
        C++: virtual void PostRender(Actor *, Renderer *)
        Called to unload the shaders after the actor has been rendered.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PostRender, *my_args)
        return ret

    def read_material(self):
        """
        V.read_material()
        C++: virtual void ReadMaterial()"""
        ret = self._vtk_obj.ReadMaterial()
        return ret
        

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *)
        Release any graphics resources that are being consumed by this
        actor. The parameter window could be used to determine which
        graphic resources to release.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def remove_shader(self, *args):
        """
        V.remove_shader(int)
        C++: void RemoveShader(int index)
        V.remove_shader(Shader)
        C++: void RemoveShader(Shader *shader)
        Remove a shader at the given index.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveShader, *my_args)
        return ret

    def render(self, *args):
        """
        V.render(Actor, Renderer)
        C++: virtual void Render(Actor *, Renderer *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShaderProgram, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ShaderProgram properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ShaderProgram properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShaderProgram properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

