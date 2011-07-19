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


class XMLMaterialReader(Object):
    """
    XMLMaterialReader - Provide access to elements in Material files
    
    Superclass: Object
    
    XMLMaterialReader provides access to three types of
    XMLDataElement found in XML Material Files. This class sorts them
    by type and integer id from 0-N for N elements of a specific type
    starting with the first instance found.
    
    Design:
    
    This class is basically a Facade for XMLMaterialParser. Currently
    functionality is to only provide access to XMLDataElements but
    further extensions may return higher level data structures.
    
    Having both an XMLMaterialParser and a XMLMaterialReader is
    consistent with VTK's design for handling xml file and provides for
    future flexibility, that is better data handlers and interfacing with
    a DOM xml parser.
    
    Property - defines values for some or all data members of
    Property
    
    VertexShader - defines vertex shaders
    
    FragmentShader - defines fragment shaders
    
    Thanks:
    
    Shader support in VTK includes key contributions by Gary Templet at
    Sandia National Labs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLMaterialReader, obj, update, **traits)
    
    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set and get file name.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_material(self):
        return wrap_vtk(self._vtk_obj.GetMaterial())
    material = traits.Property(_get_material, help=\
        """
        Get the Material representation read by the reader.
        """
    )

    def read_material(self):
        """
        V.read_material()
        C++: void ReadMaterial()
        Read the material file refered to in file_name. If the Reader
        hasn't changed since the last read_material(), it does not read
        the file again.
        """
        ret = self._vtk_obj.ReadMaterial()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('file_name',
    'GetFileName'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLMaterialReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLMaterialReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name']),
            title='Edit XMLMaterialReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLMaterialReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

