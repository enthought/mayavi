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


class BYUWriter(PolyDataWriter):
    """
    BYUWriter - write MOVIE.BYU files
    
    Superclass: PolyDataWriter
    
    BYUWriter writes MOVIE.BYU polygonal files. These files consist of
    a geometry file (.g), a scalar file (.s), a displacement or vector
    file (.d), and a 2d texture coordinate file (.t). These files must be
    specified to the object, the appropriate boolean variables must be
    true, and data must be available from the input for the files to be
    written. WARNING: this writer does not currently write triangle
    strips. Use TriangleFilter to convert strips to triangles.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBYUWriter, obj, update, **traits)
    
    write_scalar = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off writing the scalar file.
        """
    )
    def _write_scalar_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteScalar,
                        self.write_scalar_)

    write_displacement = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off writing the displacement file.
        """
    )
    def _write_displacement_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteDisplacement,
                        self.write_displacement_)

    write_texture = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off writing the texture file.
        """
    )
    def _write_texture_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteTexture,
                        self.write_texture_)

    texture_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the texture file to write.
        """
    )
    def _texture_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureFileName,
                        self.texture_file_name)

    scalar_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the scalar file to write.
        """
    )
    def _scalar_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarFileName,
                        self.scalar_file_name)

    displacement_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the displacement file to write.
        """
    )
    def _displacement_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementFileName,
                        self.displacement_file_name)

    geometry_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the geometry file to write.
        """
    )
    def _geometry_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometryFileName,
                        self.geometry_file_name)

    _updateable_traits_ = \
    (('vectors_name', 'GetVectorsName'), ('tensors_name',
    'GetTensorsName'), ('file_type', 'GetFileType'), ('file_name',
    'GetFileName'), ('write_scalar', 'GetWriteScalar'), ('scalars_name',
    'GetScalarsName'), ('header', 'GetHeader'), ('write_displacement',
    'GetWriteDisplacement'), ('texture_file_name', 'GetTextureFileName'),
    ('normals_name', 'GetNormalsName'), ('t_coords_name',
    'GetTCoordsName'), ('field_data_name', 'GetFieldDataName'),
    ('pedigree_ids_name', 'GetPedigreeIdsName'), ('scalar_file_name',
    'GetScalarFileName'), ('global_ids_name', 'GetGlobalIdsName'),
    ('write_texture', 'GetWriteTexture'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('lookup_table_name',
    'GetLookupTableName'), ('write_to_output_string',
    'GetWriteToOutputString'), ('debug', 'GetDebug'),
    ('displacement_file_name', 'GetDisplacementFileName'),
    ('progress_text', 'GetProgressText'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('geometry_file_name', 'GetGeometryFileName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_displacement', 'write_scalar',
    'write_texture', 'write_to_output_string', 'file_type',
    'displacement_file_name', 'field_data_name', 'file_name',
    'geometry_file_name', 'global_ids_name', 'header',
    'lookup_table_name', 'normals_name', 'pedigree_ids_name',
    'progress_text', 'scalar_file_name', 'scalars_name', 't_coords_name',
    'tensors_name', 'texture_file_name', 'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BYUWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit BYUWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['write_displacement', 'write_scalar', 'write_texture',
            'write_to_output_string'], ['file_type'], ['displacement_file_name',
            'field_data_name', 'file_name', 'geometry_file_name',
            'global_ids_name', 'header', 'lookup_table_name', 'normals_name',
            'pedigree_ids_name', 'scalar_file_name', 'scalars_name',
            't_coords_name', 'tensors_name', 'texture_file_name',
            'vectors_name']),
            title='Edit BYUWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BYUWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

