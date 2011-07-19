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


class ShaderCodeLibrary(Object):
    """
    ShaderCodeLibrary - Library for Hardware Shaders.
    
    Superclass: Object
    
    This class provides the hardware shader code.
    
    Thanks:
    
    Shader support in VTK includes key contributions by Gary Templet at
    Sandia National Labs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShaderCodeLibrary, obj, update, **traits)
    
    def get_shader_code(self, *args):
        """
        V.get_shader_code(string) -> string
        C++: static char *GetShaderCode(const char *name)
        Obtain the code for the shader with given name. Note that Cg
        shader names are prefixed with CG and GLSL shader names are
        prefixed with GLSL. This method allocates memory. It's the
        responsibility of the caller to free this memory.
        """
        ret = self._wrap_call(self._vtk_obj.GetShaderCode, *args)
        return ret

    def register_shader_code(self, *args):
        """
        V.register_shader_code(string, string)
        C++: static void RegisterShaderCode(const char *name,
            const char *code)
        Provides for registering shader code. This overrides the compiled
        in shader codes.
        """
        ret = self._wrap_call(self._vtk_obj.RegisterShaderCode, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShaderCodeLibrary, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ShaderCodeLibrary properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ShaderCodeLibrary properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShaderCodeLibrary properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

