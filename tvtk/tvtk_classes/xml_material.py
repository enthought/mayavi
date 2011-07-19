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


class XMLMaterial(Object):
    """
    XMLMaterial - encapsulates a VTK Material description.
    
    Superclass: Object
    
    XMLMaterial encapsulates VTK Material description. It keeps a
    pointer to XMLDataElement that defines the material and provides
    access to Shaders/Properties defined in it.
    
    Thanks:
    
    Shader support in VTK includes key contributions by Gary Templet at
    Sandia National Labs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLMaterial, obj, update, **traits)
    
    def _get_root_element(self):
        return wrap_vtk(self._vtk_obj.GetRootElement())
    def _set_root_element(self, arg):
        old_val = self._get_root_element()
        self._wrap_call(self._vtk_obj.SetRootElement,
                        deref_vtk(arg))
        self.trait_property_changed('root_element', old_val, arg)
    root_element = traits.Property(_get_root_element, _set_root_element, help=\
        """
        Get/Set the XML root element that describes this material.
        """
    )

    def get_fragment_shader(self, *args):
        """
        V.get_fragment_shader(int) -> XMLShader
        C++: XMLShader *GetFragmentShader(int id=0)
        Get the ith XMLDataElement of type <_fragment_shader />.
        """
        ret = self._wrap_call(self._vtk_obj.GetFragmentShader, *args)
        return wrap_vtk(ret)

    def _get_number_of_fragment_shaders(self):
        return self._vtk_obj.GetNumberOfFragmentShaders()
    number_of_fragment_shaders = traits.Property(_get_number_of_fragment_shaders, help=\
        """
        Get number of fragment shaders.
        """
    )

    def _get_number_of_properties(self):
        return self._vtk_obj.GetNumberOfProperties()
    number_of_properties = traits.Property(_get_number_of_properties, help=\
        """
        Get number of elements of type Property.
        """
    )

    def _get_number_of_textures(self):
        return self._vtk_obj.GetNumberOfTextures()
    number_of_textures = traits.Property(_get_number_of_textures, help=\
        """
        Get number of elements of type Texture.
        """
    )

    def _get_number_of_vertex_shaders(self):
        return self._vtk_obj.GetNumberOfVertexShaders()
    number_of_vertex_shaders = traits.Property(_get_number_of_vertex_shaders, help=\
        """
        Get number of Vertex shaders.
        """
    )

    def get_property(self, *args):
        """
        V.get_property(int) -> XMLDataElement
        C++: XMLDataElement *GetProperty(int id=0)
        Get the ith XMLDataElement of type <Property />.
        """
        ret = self._wrap_call(self._vtk_obj.GetProperty, *args)
        return wrap_vtk(ret)

    def _get_shader_language(self):
        return self._vtk_obj.GetShaderLanguage()
    shader_language = traits.Property(_get_shader_language, help=\
        """
        Get the Language used by the shaders in this Material. The
        Language of a XMLMaterial is based on the Language of it's
        shaders.
        """
    )

    def _get_shader_style(self):
        return self._vtk_obj.GetShaderStyle()
    shader_style = traits.Property(_get_shader_style, help=\
        """
        Get the style the shaders.
        \post valid_result: result==1 || result==2
        """
    )

    def get_texture(self, *args):
        """
        V.get_texture(int) -> XMLDataElement
        C++: XMLDataElement *GetTexture(int id=0)
        Get the ith XMLDataElement of type <Texture />.
        """
        ret = self._wrap_call(self._vtk_obj.GetTexture, *args)
        return wrap_vtk(ret)

    def get_vertex_shader(self, *args):
        """
        V.get_vertex_shader(int) -> XMLShader
        C++: XMLShader *GetVertexShader(int id=0)
        Get the ith XMLDataElement of type <_vertex_shader />.
        """
        ret = self._wrap_call(self._vtk_obj.GetVertexShader, *args)
        return wrap_vtk(ret)

    def create_instance(self, *args):
        """
        V.create_instance(string) -> XMLMaterial
        C++: static XMLMaterial *CreateInstance(const char *name)
        Create a new instance. It searches for the material using the
        following order: first, check the material_library; second, treat
        the name as an absolute path and try to locate it; third, search
        the Material repository. Returns null is it fails to locate the
        material.
        """
        ret = self._wrap_call(self._vtk_obj.CreateInstance, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLMaterial, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLMaterial properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit XMLMaterial properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLMaterial properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

