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


class XMLDataParser(XMLParser):
    """
    XMLDataParser - Used by XMLReader to parse VTK XML files.
    
    Superclass: XMLParser
    
    XMLDataParser provides a subclass of XMLParser that constructs
    a representation of an XML data format's file using XMLDataElement
    to represent each XML element.  This representation is then used by
    XMLReader and its subclasses to traverse the structure of the file
    and extract data.
    
    See Also:
    
    XMLDataElement
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLDataParser, obj, update, **traits)
    
    def _get_compressor(self):
        return wrap_vtk(self._vtk_obj.GetCompressor())
    def _set_compressor(self, arg):
        old_val = self._get_compressor()
        self._wrap_call(self._vtk_obj.SetCompressor,
                        deref_vtk(arg))
        self.trait_property_changed('compressor', old_val, arg)
    compressor = traits.Property(_get_compressor, _set_compressor, help=\
        """
        Get/Set the compressor used to decompress binary and appended
        data after reading from the file.
        """
    )

    abort = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set flag to abort reading of data.  This may be set by a
        progress event observer.
        """
    )
    def _abort_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbort,
                        self.abort)

    attributes_encoding = traits.Trait(0, traits.Range(0, 20, enter_set=True, auto_set=False), help=\
        """
        Get/Set the character encoding that will be used to set the
        attributes's encoding type of each XMLDataElement created by
        this parser (i.e., the data element attributes will use that
        encoding internally). If set to VTK_ENCODING_NONE (default), the
        attribute encoding type will not be changed and will default to
        the XMLDataElement default encoding type (see
        XMLDataElement::AttributeEncoding).
        """
    )
    def _attributes_encoding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttributesEncoding,
                        self.attributes_encoding)

    progress = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set progress of reading data.  This may be checked by a
        progress event observer.
        """
    )
    def _progress_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgress,
                        self.progress)

    def _get_root_element(self):
        return wrap_vtk(self._vtk_obj.GetRootElement())
    root_element = traits.Property(_get_root_element, help=\
        """
        Get the root element from the XML document.
        """
    )

    def get_word_type_size(self, *args):
        """
        V.get_word_type_size(int) -> int
        C++: unsigned long GetWordTypeSize(int wordType)
        Get the size of a word of the given type.
        """
        ret = self._wrap_call(self._vtk_obj.GetWordTypeSize, *args)
        return ret

    def character_data_handler(self, *args):
        """
        V.character_data_handler(string, int)
        C++: virtual void CharacterDataHandler(const char *data,
            int length)
        If you need the text inside XMLElements, turn ignore_character_data
        off. This method will then be called when the file is parsed, and
        the text will be stored in each xml_data_element. VTK XML Readers
        store the information elsewhere, so the default is to ignore it.
        """
        ret = self._wrap_call(self._vtk_obj.CharacterDataHandler, *args)
        return ret

    def read_appended_data(self, *args):
        """
        V.read_appended_data(int, , int, int, int) -> int
        C++: OffsetType ReadAppendedData(OffsetType offset, void *buffer,
            OffsetType startWord, OffsetType numWords, int wordType)
        V.read_appended_data(int, string, int, int) -> int
        C++: OffsetType ReadAppendedData(OffsetType offset, char *buffer,
            OffsetType startWord, OffsetType numWords)
        Read from an appended data section starting at the given appended
        data offset.  Returns the number of words read.
        """
        ret = self._wrap_call(self._vtk_obj.ReadAppendedData, *args)
        return ret

    def read_ascii_data(self, *args):
        """
        V.read_ascii_data(, int, int, int) -> int
        C++: OffsetType ReadAsciiData(void *buffer, OffsetType startWord,
            OffsetType numWords, int wordType)
        Read from an ascii data section starting at the current position
        in the stream.  Returns the number of words read.
        """
        ret = self._wrap_call(self._vtk_obj.ReadAsciiData, *args)
        return ret

    def read_binary_data(self, *args):
        """
        V.read_binary_data(, int, int, int) -> int
        C++: OffsetType ReadBinaryData(void *buffer, OffsetType startWord,
             OffsetType maxWords, int wordType)
        Read from a data section starting at the current position in the
        stream.  Returns the number of words read.
        """
        ret = self._wrap_call(self._vtk_obj.ReadBinaryData, *args)
        return ret

    def read_inline_data(self, *args):
        """
        V.read_inline_data(XMLDataElement, int, , int, int, int) -> int
        C++: OffsetType ReadInlineData(XMLDataElement *element,
            int isAscii, void *buffer, OffsetType startWord,
            OffsetType numWords, int wordType)
        V.read_inline_data(XMLDataElement, int, string, int, int) -> int
        C++: OffsetType ReadInlineData(XMLDataElement *element,
            int isAscii, char *buffer, OffsetType startWord,
            OffsetType numWords)
        Read inline data from inside the given element.  Returns the
        number of words read.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadInlineData, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('attributes_encoding',
    'GetAttributesEncoding'), ('abort', 'GetAbort'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('reference_count', 'GetReferenceCount'),
    ('file_name', 'GetFileName'), ('encoding', 'GetEncoding'),
    ('ignore_character_data', 'GetIgnoreCharacterData'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'abort', 'attributes_encoding',
    'encoding', 'file_name', 'ignore_character_data'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLDataParser, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLDataParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['abort', 'attributes_encoding', 'encoding',
            'file_name', 'ignore_character_data']),
            title='Edit XMLDataParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLDataParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

