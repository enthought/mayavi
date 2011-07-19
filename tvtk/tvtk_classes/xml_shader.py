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


class XMLShader(Object):
    """
    XMLShader - encapsulates a Shader XML description.
    
    Superclass: Object
    
    XMLShader encapsulates the XML description for a Shader. It
    provides convenient access to various attributes/properties of a
    shader.
    
    Thanks:
    
    Shader support in VTK includes key contributions by Gary Templet at
    Sandia National Labs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLShader, obj, update, **traits)
    
    def _get_root_element(self):
        return wrap_vtk(self._vtk_obj.GetRootElement())
    def _set_root_element(self, arg):
        old_val = self._get_root_element()
        self._wrap_call(self._vtk_obj.SetRootElement,
                        deref_vtk(arg))
        self.trait_property_changed('root_element', old_val, arg)
    root_element = traits.Property(_get_root_element, _set_root_element, help=\
        """
        Get/Set the XML root element that describes this shader.
        """
    )

    def _get_code(self):
        return self._vtk_obj.GetCode()
    code = traits.Property(_get_code, help=\
        """
        Get the shader code.
        """
    )

    def _get_entry(self):
        return self._vtk_obj.GetEntry()
    entry = traits.Property(_get_entry, help=\
        """
        Get the entry point to the shader code as defined in the XML.
        """
    )

    def _get_language(self):
        return self._vtk_obj.GetLanguage()
    language = traits.Property(_get_language, help=\
        """
        Returns the shader's language as defined in the XML description.
        """
    )

    def _get_location(self):
        return self._vtk_obj.GetLocation()
    location = traits.Property(_get_location, help=\
        """
        Returns the location of the shader as defined in the XML
        description.
        """
    )

    def _get_name(self):
        return self._vtk_obj.GetName()
    name = traits.Property(_get_name, help=\
        """
        Get the name of the Shader.
        """
    )

    def _get_scope(self):
        return self._vtk_obj.GetScope()
    scope = traits.Property(_get_scope, help=\
        """
        Returns the type of the shader as defined in the XML description.
        """
    )

    def _get_style(self):
        return self._vtk_obj.GetStyle()
    style = traits.Property(_get_style, help=\
        """
        Returns the style of the shader as optionaly defined in the XML
        description. If not present, default style is 1. "style=2" means
        it is a shader without a main(). In style 2, the "main" function
        for the vertex shader part is void prop_func_vs(void), the main
        function for the fragment shader part is void prop_func_fs(). This
        is useful when combining a shader at the actor level and a shader
        defines at the renderer level, like the depth peeling pass.
        \post valid_result: result==1 || result==2
        """
    )

    def locate_file(self, *args):
        """
        V.locate_file(string) -> string
        C++: static char *LocateFile(const char *filename)
        Searches the file in the VTK_MATERIALS_DIRS. Note that this
        allocates new memory for the string. The caller must delete it.
        """
        ret = self._wrap_call(self._vtk_obj.LocateFile, *args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLShader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLShader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit XMLShader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLShader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

