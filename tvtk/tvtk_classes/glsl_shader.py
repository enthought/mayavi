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

from tvtk.tvtk_classes.shader import Shader


class GLSLShader(Shader):
    """
    GLSLShader - GLSL Shader
    
    Superclass: Shader
    
    GLSLShader is a concrete class that creates and compiles hardware
    shaders written in the open_gl Shadering Language (GLSL, open_gl2._0).
    While step linking a vertex and a fragment shader is performed by
    GLSLShaderProgram, all shader parameters are initialized in this
    class.
    
    .Section OpenGLExtensionManager All open_gl calls are made through
    OpenGLExtensionManager.
    
    .Section Supported Basic Shader Types:
    
    Scalar Types uniform float uniform int uniform int -- boolean scalar
    not yet tested
    
    Vector Types: uniform vec{2|3|4} uniform ivec{2|3|4} uniform
    bvec{2|3|4} -- boolean vector not yet tested
    
    Matrix Types: uniform mat{2|3|4}
    
    Texture Samplers: sample_1d -- Not yet implemented in this cless.
    sample_2d -- Not yet implemented in this class. sample_3d -- Not yet
    implemented in this class. sampler_1d_shadow -- Not yet implemented in
    this class. sampler_1d_shadow -- Not yet implemented in this class.
    
    User-Defined structures: uniform struct
     NOTE: these must be defined and declared  outside of the 'main'
    shader
     function.
    
    Thanks:
    
    Shader support in VTK includes key contributions by Gary Templet at
    Sandia National Labs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGLSLShader, obj, update, **traits)
    
    program = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The Shader needs the id of the shader_program to obtain uniform
        variable locations. This is set by GLSLShaderProgram.
        """
    )
    def _program_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgram,
                        self.program)

    def _get_handle(self):
        return self._vtk_obj.GetHandle()
    handle = traits.Property(_get_handle, help=\
        """
        The GLSLShaderProgram needs the shader handle for attaching.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('program', 'GetProgram'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'program'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GLSLShader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GLSLShader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['program']),
            title='Edit GLSLShader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GLSLShader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

