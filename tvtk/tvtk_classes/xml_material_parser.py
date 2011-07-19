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

from tvtk.tvtk_classes.xml_parser import XMLParser


class XMLMaterialParser(XMLParser):
    """
    XMLMaterialParser - Parses VTK Material file
    
    Superclass: XMLParser
    
    XMLMaterialParser parses a VTK Material file and provides that
    file's description of a number of vertex and fragment shaders along
    with data values specified for data members of Property. This
    material is to be applied to an actor through it's Property and augments
    VTK's concept of a Property to include explicitly include vertex
    and fragment shaders and parameter settings for those shaders. This
    effectively makes reflectance models and other shaders  a material
    property. If no shaders are specified VTK should default to standard
    rendering.
    
    Design:
    
    XMLMaterialParser provides access to 3 distinct types of
    first-level XMLDataElements that describe a VTK material. These
    elements are as follows:
    
    Property - describe values for Property data members
    
    VertexShader - a vertex shader and enough information to install
    it into the hardware rendering pipeline including values for specific
    shader parameters and structures.
    
    FragmentShader - a fragment shader and enough information to
    install it into the hardware rendering pipeline including values for
    specific shader parameters and structures.
    
    The design of the material file closely follows that of vtk's xml
    descriptions of it's data sets. This allows use of the very handy
    XMLDataElement which provides easy access to an xml element's
    attribute values. Inlined data is currently not handled.
    
    Ideally this class would be a Facade to a DOM parser, but VTK only
    provides access to expat, a SAX parser. Other vtk classes that parse
    xml files are tuned to read DataSets and don't provide the
    functionality to handle generic xml data. As such they are of little
    use here.
    
    This class may be extended for better data  handling or may become a
    Facade to a DOM parser should on become part of the VTK code base.
    
    Thanks:
    
    Shader support in VTK includes key contributions by Gary Templet at
    Sandia National Labs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLMaterialParser, obj, update, **traits)
    
    def _get_material(self):
        return wrap_vtk(self._vtk_obj.GetMaterial())
    def _set_material(self, arg):
        old_val = self._get_material()
        self._wrap_call(self._vtk_obj.SetMaterial,
                        deref_vtk(arg))
        self.trait_property_changed('material', old_val, arg)
    material = traits.Property(_get_material, _set_material, help=\
        """
        Set/Get the XMLMaterial representation of the parsed material.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('encoding', 'GetEncoding'),
    ('reference_count', 'GetReferenceCount'), ('file_name',
    'GetFileName'), ('ignore_character_data', 'GetIgnoreCharacterData'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'encoding', 'file_name',
    'ignore_character_data'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLMaterialParser, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLMaterialParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['encoding', 'file_name',
            'ignore_character_data']),
            title='Edit XMLMaterialParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLMaterialParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

