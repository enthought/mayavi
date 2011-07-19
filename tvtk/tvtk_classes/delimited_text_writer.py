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

from tvtk.tvtk_classes.writer import Writer


class DelimitedTextWriter(Writer):
    """
    DelimitedTextWriter - Delimited text writer for Table
    
    Superclass: Writer
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDelimitedTextWriter, obj, update, **traits)
    
    write_to_output_string = tvtk_base.false_bool_trait(help=\
        """
        Enable writing to an output_string instead of the default, a file.
        """
    )
    def _write_to_output_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToOutputString,
                        self.write_to_output_string_)

    field_delimiter = traits.String(r",", enter_set=True, auto_set=False, help=\
        """
        Get/Set the delimiter use to separate fields ("," by default.)
        """
    )
    def _field_delimiter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDelimiter,
                        self.field_delimiter)

    use_string_delimiter = traits.Bool(True, help=\
        """
        Get/Set if string_delimiter must be used for string data. True by
        default.
        """
    )
    def _use_string_delimiter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseStringDelimiter,
                        self.use_string_delimiter)

    string_delimiter = traits.String('"', enter_set=True, auto_set=False, help=\
        """
        Get/Set the delimiter used for string data, if any eg. double
        quotes(").
        """
    )
    def _string_delimiter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStringDelimiter,
                        self.string_delimiter)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get/Set the filename for the file.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def get_string(self, *args):
        """
        V.get_string(string) -> string
        C++: StdString GetString(StdString string)
        Internal method: Returns the "string" with the "_string_delimiter"
        if use_string_delimiter is true.
        """
        ret = self._wrap_call(self._vtk_obj.GetString, *args)
        return ret

    def register_and_get_output_string(self):
        """
        V.register_and_get_output_string() -> string
        C++: char *RegisterAndGetOutputString()
        This convenience method returns the string, sets the IVAR to
        NULL, so that the user is responsible for deleting the string.
        """
        ret = self._vtk_obj.RegisterAndGetOutputString()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('write_to_output_string', 'GetWriteToOutputString'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'),
    ('field_delimiter', 'GetFieldDelimiter'), ('debug', 'GetDebug'),
    ('string_delimiter', 'GetStringDelimiter'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('use_string_delimiter', 'GetUseStringDelimiter'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'field_delimiter',
    'file_name', 'progress_text', 'string_delimiter',
    'use_string_delimiter'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DelimitedTextWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DelimitedTextWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['write_to_output_string'], [], ['field_delimiter',
            'file_name', 'string_delimiter', 'use_string_delimiter']),
            title='Edit DelimitedTextWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DelimitedTextWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

