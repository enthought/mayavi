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

from tvtk.tvtk_classes.table_algorithm import TableAlgorithm


class DelimitedTextReader(TableAlgorithm):
    """
    DelimitedTextReader - reads in delimited ascii or unicode text
    files
    
    Superclass: TableAlgorithm
    
    DelimitedTextReader is an interface for pulling in data from a
    flat, delimited ascii or unicode text file (delimiter can be any
    character).
    
    The behavior of the reader with respect to ascii or unicode input is
    controlled by the set_unicode_character_set() method.  By default
    (without calling set_unicode_character_set()), the reader will expect to
    read ascii text and will output StdString columns.  Use the Set
    and Get methods to set delimiters that do not contain UTF8 in the
    name when operating the reader in default ascii mode.  If the
    set_unicode_character_set() method is called, the reader will output
    UnicodeString columns in the output table.  In addition, it is
    necessary to use the Set and Get methods that contain UTF8 in the
    name to specify delimiters when operating in unicode mode.
    
    There is also a special character set US-ASCII-WITH-FALLBACK that
    will treat the input text as ASCII no matter what.  If and when it
    encounters a character with its 8th bit set it will replace that
    character with the code point replacement_character.  You may use this
    if you have text that belongs to a code page like LATIN9 or
    ISO-8859-1 or friends: mostly ASCII but not entirely.  Eventually
    this class will acquire the ability to read gracefully text from any
    code page, making this option obsolete.
    
    This class emits progress_event for every 100 lines it reads.
    
    Thanks:
    
    Thanks to Andy Wilson, Brian Wylie, Tim Shead, and Thomas Otahal from
    Sandia National Laboratories for implementing this class.
    
    Caveats:
    
    This reader assumes that the first line in the file (whether that's
    headers or the first document) contains at least as many fields as
    any other line in the file.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDelimitedTextReader, obj, update, **traits)
    
    generate_pedigree_ids = tvtk_base.true_bool_trait(help=\
        """
        If on (default), generates pedigree ids automatically. If off,
        assign one of the arrays to be the pedigree id.
        """
    )
    def _generate_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePedigreeIds,
                        self.generate_pedigree_ids_)

    merge_consecutive_delimiters = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether to merge successive delimiters.  Use this if (for
        example) your fields are separated by spaces but you don't know
        exactly how many.
        """
    )
    def _merge_consecutive_delimiters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMergeConsecutiveDelimiters,
                        self.merge_consecutive_delimiters_)

    use_string_delimiter = tvtk_base.true_bool_trait(help=\
        """
        Set/get whether to use the string delimiter.  Defaults to on.
        """
    )
    def _use_string_delimiter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseStringDelimiter,
                        self.use_string_delimiter_)

    output_pedigree_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, assigns pedigree ids to output. Defaults to off.
        """
    )
    def _output_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPedigreeIds,
                        self.output_pedigree_ids_)

    detect_numeric_columns = tvtk_base.false_bool_trait(help=\
        """
        When set to true, the reader will detect numeric columns and
        create DoubleArray or IntArray for those instead of
        StringArray. Default is off.
        """
    )
    def _detect_numeric_columns_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDetectNumericColumns,
                        self.detect_numeric_columns_)

    utf8_record_delimiters = traits.String(r"\r\n", enter_set=True, auto_set=False, help=\
        """
        Specify the character(s) that will be used to separate records.
        The order of characters in the string does not matter.  Defaults
        to "\r\n".
        """
    )
    def _utf8_record_delimiters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUTF8RecordDelimiters,
                        self.utf8_record_delimiters)

    pedigree_id_array_name = traits.String(r"id", enter_set=True, auto_set=False, help=\
        """
        The name of the array for generating or assigning pedigree ids
        (default "id").
        """
    )
    def _pedigree_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPedigreeIdArrayName,
                        self.pedigree_id_array_name)

    replacement_character = traits.Int(120, enter_set=True, auto_set=False, help=\
        """
        Fallback character for use in the US-ASCII-WITH-FALLBACK
        character set.  Any characters that have their 8th bit set will
        be replaced with this code point.  Defaults to 'x'.
        """
    )
    def _replacement_character_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplacementCharacter,
                        self.replacement_character)

    unicode_record_delimiters = traits.String(r"\r\n", enter_set=True, auto_set=False, help=\
        """
        Specify the character(s) that will be used to separate records.
        The order of characters in the string does not matter.  Defaults
        to "\r\n".
        """
    )
    def _unicode_record_delimiters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnicodeRecordDelimiters,
                        self.unicode_record_delimiters)

    field_delimiter_characters = traits.String(r",", enter_set=True, auto_set=False, help=\
        """
        Specify the character(s) that will be used to separate fields. 
        For example, set this to "," for a comma-separated value file. 
        Set it to ".:;" for a file where columns can be separated by a
        period, colon or semicolon.  The order of the characters in the
        string does not matter.  Defaults to a comma.
        """
    )
    def _field_delimiter_characters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDelimiterCharacters,
                        self.field_delimiter_characters)

    string_delimiter = traits.String('"', enter_set=True, auto_set=False, help=\
        """
        Get/set the character that will begin and end strings.  Microsoft
        Excel, for example, will export the following format:
        
        "First Field","Second Field","Field, With, Commas","Fourth Field"
        
        The third field has a comma in it.  By using a string delimiter,
        this will be correctly read.  The delimiter defaults to '"'.
        """
    )
    def _string_delimiter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStringDelimiter,
                        self.string_delimiter)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specifies the delimited text file to be loaded.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    max_records = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specifies the maximum number of records to read from the file. 
        Limiting the number of records to read is useful for previewing
        the contents of a file.
        """
    )
    def _max_records_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxRecords,
                        self.max_records)

    utf8_string_delimiters = traits.String('"', enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _utf8_string_delimiters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUTF8StringDelimiters,
                        self.utf8_string_delimiters)

    unicode_character_set = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specifies the character set used in the input file.  Valid
        character set names will be drawn from the list maintained by the
        Internet Assigned Name Authority at
        
        
          http://www.iana.org/assignments/character-sets
        
        Where multiple aliases are provided for a character set, the
        preferred MIME name will be used.  UnicodeDelimitedTextReader
        currently supports "US-ASCII", "UTF-8", "UTF-16", "_utf-_16be", and
        "_utf-_16le" character sets.
        """
    )
    def _unicode_character_set_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnicodeCharacterSet,
                        self.unicode_character_set)

    utf8_field_delimiters = traits.String(r",", enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _utf8_field_delimiters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUTF8FieldDelimiters,
                        self.utf8_field_delimiters)

    unicode_field_delimiters = traits.String(r",", enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _unicode_field_delimiters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnicodeFieldDelimiters,
                        self.unicode_field_delimiters)

    unicode_string_delimiters = traits.String('"', enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _unicode_string_delimiters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnicodeStringDelimiters,
                        self.unicode_string_delimiters)

    have_headers = traits.Bool(False, help=\
        """
        Set/get whether to treat the first line of the file as headers.
        """
    )
    def _have_headers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHaveHeaders,
                        self.have_headers)

    def _get_last_error(self):
        return self._vtk_obj.GetLastError()
    last_error = traits.Property(_get_last_error, help=\
        """
        Returns a human-readable description of the most recent error, if
        any. Otherwise, returns an empty string.  Note that the result is
        only valid after calling Update().
        """
    )

    _updateable_traits_ = \
    (('replacement_character', 'GetReplacementCharacter'),
    ('field_delimiter_characters', 'GetFieldDelimiterCharacters'),
    ('unicode_field_delimiters', 'GetUnicodeFieldDelimiters'),
    ('file_name', 'GetFileName'), ('unicode_string_delimiters',
    'GetUnicodeStringDelimiters'), ('debug', 'GetDebug'),
    ('generate_pedigree_ids', 'GetGeneratePedigreeIds'), ('have_headers',
    'GetHaveHeaders'), ('output_pedigree_ids', 'GetOutputPedigreeIds'),
    ('merge_consecutive_delimiters', 'GetMergeConsecutiveDelimiters'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('unicode_record_delimiters', 'GetUnicodeRecordDelimiters'),
    ('utf8_field_delimiters', 'GetUTF8FieldDelimiters'),
    ('unicode_character_set', 'GetUnicodeCharacterSet'),
    ('utf8_record_delimiters', 'GetUTF8RecordDelimiters'),
    ('detect_numeric_columns', 'GetDetectNumericColumns'),
    ('progress_text', 'GetProgressText'), ('pedigree_id_array_name',
    'GetPedigreeIdArrayName'), ('string_delimiter', 'GetStringDelimiter'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('use_string_delimiter',
    'GetUseStringDelimiter'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('max_records', 'GetMaxRecords'),
    ('utf8_string_delimiters', 'GetUTF8StringDelimiters'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'detect_numeric_columns',
    'generate_pedigree_ids', 'global_warning_display',
    'merge_consecutive_delimiters', 'output_pedigree_ids',
    'release_data_flag', 'use_string_delimiter',
    'field_delimiter_characters', 'file_name', 'have_headers',
    'max_records', 'pedigree_id_array_name', 'progress_text',
    'replacement_character', 'string_delimiter', 'unicode_character_set',
    'unicode_field_delimiters', 'unicode_record_delimiters',
    'unicode_string_delimiters', 'utf8_field_delimiters',
    'utf8_record_delimiters', 'utf8_string_delimiters'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DelimitedTextReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DelimitedTextReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['detect_numeric_columns', 'generate_pedigree_ids',
            'merge_consecutive_delimiters', 'output_pedigree_ids',
            'use_string_delimiter'], [], ['field_delimiter_characters',
            'file_name', 'have_headers', 'max_records', 'pedigree_id_array_name',
            'replacement_character', 'string_delimiter', 'unicode_character_set',
            'unicode_field_delimiters', 'unicode_record_delimiters',
            'unicode_string_delimiters', 'utf8_field_delimiters',
            'utf8_record_delimiters', 'utf8_string_delimiters']),
            title='Edit DelimitedTextReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DelimitedTextReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

