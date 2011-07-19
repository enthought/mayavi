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

from tvtk.tvtk_classes.poly_data_writer import PolyDataWriter


class MNIObjectWriter(PolyDataWriter):
    """
    MNIObjectWriter - A writer for MNI surface mesh files.
    
    Superclass: PolyDataWriter
    
    The MNI .obj file format is used to store geometrical data.  This
    file format was developed at the mc_connell Brain Imaging Centre at
    the Montreal Neurological Institute and is used by their software.
    Only polygon and line files are supported by this writer.  For these
    formats, all data elements are written including normals, colors, and
    surface properties.  ASCII and binary file types are supported.
    
    See Also:
    
    MINCImageReader MNIObjectReader MNITransformReader
    
    Thanks:
    
    Thanks to David Gobbi for writing this class and Atamai Inc. for
    contributing it to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMNIObjectWriter, obj, update, **traits)
    
    def _get_mapper(self):
        return wrap_vtk(self._vtk_obj.GetMapper())
    def _set_mapper(self, arg):
        old_val = self._get_mapper()
        self._wrap_call(self._vtk_obj.SetMapper,
                        deref_vtk(arg))
        self.trait_property_changed('mapper', old_val, arg)
    mapper = traits.Property(_get_mapper, _set_mapper, help=\
        """
        Set the mapper associated with the object.  Optional. This is
        useful for exporting an actor with the same colors that are used
        to display the actor within VTK.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Set the property associated with the object.  Optional. This is
        useful for exporting an actor.
        """
    )

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set the lookup table associated with the object.  This will be
        used to convert scalar values to colors, if a mapper is not set.
        """
    )

    def _get_descriptive_name(self):
        return self._vtk_obj.GetDescriptiveName()
    descriptive_name = traits.Property(_get_descriptive_name, help=\
        """
        Get the name of this file format.
        """
    )

    def _get_file_extensions(self):
        return self._vtk_obj.GetFileExtensions()
    file_extensions = traits.Property(_get_file_extensions, help=\
        """
        Get the entension for this file format.
        """
    )

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
            return super(MNIObjectWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MNIObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['write_to_output_string'], ['file_type'],
            ['field_data_name', 'file_name', 'global_ids_name', 'header',
            'lookup_table_name', 'normals_name', 'pedigree_ids_name',
            'scalars_name', 't_coords_name', 'tensors_name', 'vectors_name']),
            title='Edit MNIObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MNIObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

