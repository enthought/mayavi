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


class XMLParser(Object):
    """
    XMLParser - Parse XML to handle element tags and attributes.
    
    Superclass: Object
    
    XMLParser reads a stream and parses XML element tags and
    corresponding attributes.  Each element begin tag and its attributes
    are sent to the start_element method.  Each element end tag is sent to
    the end_element method.  Subclasses should replace these methods to
    actually use the tags.
    
    to_do: Add commands for parsing in Tcl.:
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLParser, obj, update, **traits)
    
    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set and get file name.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    ignore_character_data = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        If this is off (the default), character_data_handler will be called
        to process text within XML Elements. If this is on, the text will
        be ignored.
        """
    )
    def _ignore_character_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIgnoreCharacterData,
                        self.ignore_character_data)

    encoding = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set and get the encoding the parser should expect (NULL defaults
        to Expat's own default encoder, i.e UTF-8). This should be set
        before parsing (i.e. a call to Parse()) or even initializing the
        parser (i.e. a call to initialize_parser())
        """
    )
    def _encoding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEncoding,
                        self.encoding)

    def cleanup_parser(self):
        """
        V.cleanup_parser() -> int
        C++: virtual int CleanupParser()
        When parsing fragments of XML or streaming XML, use the following
        three methods.  initialize_parser method initialize parser but
        does not perform any actual parsing.  parse_chunk parses framgent
        of XML. This has to match to what was already parsed.
        cleanup_parser finishes parsing. If there were errors,
        cleanup_parser will report them.
        """
        ret = self._vtk_obj.CleanupParser()
        return ret
        

    def initialize_parser(self):
        """
        V.initialize_parser() -> int
        C++: virtual int InitializeParser()
        When parsing fragments of XML or streaming XML, use the following
        three methods.  initialize_parser method initialize parser but
        does not perform any actual parsing.  parse_chunk parses framgent
        of XML. This has to match to what was already parsed.
        cleanup_parser finishes parsing. If there were errors,
        cleanup_parser will report them.
        """
        ret = self._vtk_obj.InitializeParser()
        return ret
        

    def parse(self, *args):
        """
        V.parse() -> int
        C++: virtual int Parse()
        V.parse(string) -> int
        C++: virtual int Parse(const char *inputString)
        V.parse(string, int) -> int
        C++: virtual int Parse(const char *inputString,
            unsigned int length)
        Parse the XML input.
        """
        ret = self._wrap_call(self._vtk_obj.Parse, *args)
        return ret

    def parse_chunk(self, *args):
        """
        V.parse_chunk(string, int) -> int
        C++: virtual int ParseChunk(const char *inputString,
            unsigned int length)
        When parsing fragments of XML or streaming XML, use the following
        three methods.  initialize_parser method initialize parser but
        does not perform any actual parsing.  parse_chunk parses framgent
        of XML. This has to match to what was already parsed.
        cleanup_parser finishes parsing. If there were errors,
        cleanup_parser will report them.
        """
        ret = self._wrap_call(self._vtk_obj.ParseChunk, *args)
        return ret

    def seek_g(self, *args):
        """
        V.seek_g(int)
        C++: void SeekG(long position)
        Used by subclasses and their supporting classes.  These methods
        wrap around the tellg and seekg methods of the input stream to
        work-around stream bugs on various platforms.
        """
        ret = self._wrap_call(self._vtk_obj.SeekG, *args)
        return ret

    def tell_g(self):
        """
        V.tell_g() -> int
        C++: long TellG()
        Used by subclasses and their supporting classes.  These methods
        wrap around the tellg and seekg methods of the input stream to
        work-around stream bugs on various platforms.
        """
        ret = self._vtk_obj.TellG()
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
            return super(XMLParser, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['encoding', 'file_name',
            'ignore_character_data']),
            title='Edit XMLParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

