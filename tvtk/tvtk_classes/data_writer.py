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


class DataWriter(Writer):
    """
    DataWriter - helper class for objects that write vtk data files
    
    Superclass: Writer
    
    DataWriter is a helper class that opens and writes the vtk header
    and point data (e.g., scalars, vectors, normals, etc.) from a vtk
    data file. See text for various formats.
    
    See Also:
    
    DataSetWriter PolyDataWriter StructuredGridWriter
    StructuredPointsWriter UnstructuredGridWriter
    FieldDataWriter RectilinearGridWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataWriter, obj, update, **traits)
    
    write_to_output_string = tvtk_base.false_bool_trait(help=\
        """
        Enable writing to an output_string instead of the default, a file.
        """
    )
    def _write_to_output_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToOutputString,
                        self.write_to_output_string_)

    file_type = traits.Trait('ascii',
    tvtk_base.TraitRevPrefixMap({'binary': 2, 'ascii': 1}), help=\
        """
        Specify file type (ASCII or BINARY) for vtk data file.
        """
    )
    def _file_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileType,
                        self.file_type_)

    t_coords_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the texture coordinates data. If not specified,
        uses default name "texture_coords".
        """
    )
    def _t_coords_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTCoordsName,
                        self.t_coords_name)

    lookup_table_name = traits.String(r"lookup_table", enter_set=True, auto_set=False, help=\
        """
        Give a name to the lookup table. If not specified, uses default
        name "lookup_table".
        """
    )
    def _lookup_table_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLookupTableName,
                        self.lookup_table_name)

    scalars_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the scalar data. If not specified, uses default
        name "scalars".
        """
    )
    def _scalars_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarsName,
                        self.scalars_name)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of vtk polygon data file to write.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    header = traits.String(r"vtk output", enter_set=True, auto_set=False, help=\
        """
        Specify the header for the vtk data file.
        """
    )
    def _header_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeader,
                        self.header)

    field_data_name = traits.String(r"FieldData", enter_set=True, auto_set=False, help=\
        """
        Give a name to the field data. If not specified, uses default
        name "field".
        """
    )
    def _field_data_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDataName,
                        self.field_data_name)

    tensors_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the tensors data. If not specified, uses default
        name "tensors".
        """
    )
    def _tensors_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTensorsName,
                        self.tensors_name)

    normals_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the normals data. If not specified, uses default
        name "normals".
        """
    )
    def _normals_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalsName,
                        self.normals_name)

    global_ids_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the global ids data. If not specified, uses
        default name "global_ids".
        """
    )
    def _global_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalIdsName,
                        self.global_ids_name)

    vectors_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the vector data. If not specified, uses default
        name "vectors".
        """
    )
    def _vectors_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorsName,
                        self.vectors_name)

    pedigree_ids_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the pedigree ids data. If not specified, uses
        default name "pedigree_ids".
        """
    )
    def _pedigree_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPedigreeIdsName,
                        self.pedigree_ids_name)

    def _get_output_string(self):
        return self._vtk_obj.GetOutputString()
    output_string = traits.Property(_get_output_string, help=\
        """
        When write_to_output_string in on, then a string is allocated,
        written to, and can be retrieved with these methods.  The string
        is deleted during the next call to write ...
        """
    )

    def _get_output_string_length(self):
        return self._vtk_obj.GetOutputStringLength()
    output_string_length = traits.Property(_get_output_string_length, help=\
        """
        When write_to_output_string in on, then a string is allocated,
        written to, and can be retrieved with these methods.  The string
        is deleted during the next call to write ...
        """
    )

    def register_and_get_output_string(self):
        """
        V.register_and_get_output_string() -> string
        C++: char *RegisterAndGetOutputString()
        This convenience method returns the string, sets the IVAR to
        NULL, so that the user is responsible for deleting the string. I
        am not sure what the name should be, so it may change in the
        future.
        """
        ret = self._vtk_obj.RegisterAndGetOutputString()
        return ret
        

    _updateable_traits_ = \
    (('vectors_name', 'GetVectorsName'), ('global_ids_name',
    'GetGlobalIdsName'), ('tensors_name', 'GetTensorsName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('lookup_table_name', 'GetLookupTableName'),
    ('write_to_output_string', 'GetWriteToOutputString'), ('file_type',
    'GetFileType'), ('file_name', 'GetFileName'), ('scalars_name',
    'GetScalarsName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('header', 'GetHeader'), ('abort_execute',
    'GetAbortExecute'), ('t_coords_name', 'GetTCoordsName'),
    ('normals_name', 'GetNormalsName'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('field_data_name', 'GetFieldDataName'),
    ('pedigree_ids_name', 'GetPedigreeIdsName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'file_type',
    'field_data_name', 'file_name', 'global_ids_name', 'header',
    'lookup_table_name', 'normals_name', 'pedigree_ids_name',
    'progress_text', 'scalars_name', 't_coords_name', 'tensors_name',
    'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['write_to_output_string'], ['file_type'],
            ['field_data_name', 'file_name', 'global_ids_name', 'header',
            'lookup_table_name', 'normals_name', 'pedigree_ids_name',
            'scalars_name', 't_coords_name', 'tensors_name', 'vectors_name']),
            title='Edit DataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

