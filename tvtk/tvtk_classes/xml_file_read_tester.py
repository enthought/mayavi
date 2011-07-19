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


class XMLFileReadTester(XMLParser):
    """
    XMLFileReadTester - Utility class for XMLReader and subclasses.
    
    Superclass: XMLParser
    
    XMLFileReadTester reads the smallest part of a file necessary to
    determine whether it is a VTK XML file.  If so, it extracts the file
    type and version number.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLFileReadTester, obj, update, **traits)
    
    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get/Set the name of the file tested by test_read_file().
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_file_data_type(self):
        return self._vtk_obj.GetFileDataType()
    file_data_type = traits.Property(_get_file_data_type, help=\
        """
        Get the data type of the XML file tested.  If the file could not
        be read, returns NULL.
        """
    )

    def _get_file_version(self):
        return self._vtk_obj.GetFileVersion()
    file_version = traits.Property(_get_file_version, help=\
        """
        Get the file version of the XML file tested.  If the file could
        not be read, returns NULL.
        """
    )

    def test_read_file(self):
        """
        V.test_read_file() -> int
        C++: int TestReadFile()
        Try to read the file given by file_name.  Returns 1 if the file is
        a VTK XML file, and 0 otherwise.
        """
        ret = self._vtk_obj.TestReadFile()
        return ret
        

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
            return super(XMLFileReadTester, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLFileReadTester properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['encoding', 'file_name',
            'ignore_character_data']),
            title='Edit XMLFileReadTester properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLFileReadTester properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

