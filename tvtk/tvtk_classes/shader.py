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


class Shader(Object):
    """
    Shader
    
    Superclass: Object
    
    Shader is a base class for interfacing VTK to hardware shader
    libraries. Shader interprets a XMLDataElement that describes a
    particular shader. Descendants of this class inherit this
    functionality and additionally interface to specific shader libraries
    like NVidia's Cg and open_gl2._0 (GLSL) to perform operations, on
    individual shaders.
    
    During each render, the ShaderProgram calls Compile(),
    pass_shader_variables(), Bind() and after the actor has been rendered,
    calls Unbind(), in that order.
    
    See Also:
    
    CgShader GLSLShader
    
    Thanks:
    
    Shader support in VTK includes key contributions by Gary Templet at
    Sandia National Labs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShader, obj, update, **traits)
    
    def _get_xml_shader(self):
        return wrap_vtk(self._vtk_obj.GetXMLShader())
    def _set_xml_shader(self, arg):
        old_val = self._get_xml_shader()
        self._wrap_call(self._vtk_obj.SetXMLShader,
                        deref_vtk(arg))
        self.trait_property_changed('xml_shader', old_val, arg)
    xml_shader = traits.Property(_get_xml_shader, _set_xml_shader, help=\
        """
        Get/Set the XMLShader representation for this shader. A shader is
        not valid without a XMLShader.
        """
    )

    def _get_scope(self):
        return self._vtk_obj.GetScope()
    scope = traits.Property(_get_scope, help=\
        """
        Returns the scope of the shader i.e. if it's a vertex or fragment
        shader. (vtk_xml_shader::_scope__vertex or
        XMLShader::SCOPE_FRAGMENT).
        """
    )

    def get_shader_variable_size(self, *args):
        """
        V.get_shader_variable_size(string) -> int
        C++: int GetShaderVariableSize(const char *name)
        Get number of elements in a Shader variable. Return 0 if failed
        to find the shader variable.
        """
        ret = self._wrap_call(self._vtk_obj.GetShaderVariableSize, *args)
        return ret

    def get_shader_variable_type(self, *args):
        """
        V.get_shader_variable_type(string) -> int
        C++: int GetShaderVariableType(const char *name)
        Returns the type of a Shader variable with the given name. Return
        0 on error.
        """
        ret = self._wrap_call(self._vtk_obj.GetShaderVariableType, *args)
        return ret

    def bind(self):
        """
        V.bind()
        C++: virtual void Bind()
        In this method the shader can enable/bind itself. This is
        applicable only to Cg, since in GLSL, individual shaders in a
        program can't be enabled/bound.
        """
        ret = self._vtk_obj.Bind()
        return ret
        

    def compile(self):
        """
        V.compile() -> int
        C++: virtual int Compile()
        Called to compile the shader code. The subclasses must only
        compile the code in this method. Returns if the compile was
        successful. Subclasses should compile the code only if it was not
        already compiled.
        """
        ret = self._vtk_obj.Compile()
        return ret
        

    def has_shader_variable(self, *args):
        """
        V.has_shader_variable(string) -> int
        C++: int HasShaderVariable(const char *name)
        Indicates if a variable by the given name exists.
        """
        ret = self._wrap_call(self._vtk_obj.HasShaderVariable, *args)
        return ret

    def pass_shader_variables(self, *args):
        """
        V.pass_shader_variables(Actor, Renderer)
        C++: virtual void PassShaderVariables(Actor *actor,
            Renderer *ren)
        Called to pass VTK actor/property/light values and other Shader
        variables over to the shader. This is called by the shader_program
        during each render.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PassShaderVariables, *my_args)
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

    def unbind(self):
        """
        V.unbind()
        C++: virtual void Unbind()
        Called to unbind the shader. As with Bind(), this is only
        applicable to Cg.
        """
        ret = self._vtk_obj.Unbind()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Shader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Shader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit Shader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Shader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

