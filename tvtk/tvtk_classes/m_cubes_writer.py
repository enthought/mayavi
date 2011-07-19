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


class MCubesWriter(PolyDataWriter):
    """
    MCubesWriter - write binary marching cubes file
    
    Superclass: PolyDataWriter
    
    MCubesWriter is a polydata writer that writes binary marching
    cubes files. (Marching cubes is an isosurfacing technique that
    generates many triangles.) The binary format is supported by W.
    Lorensen's marching cubes program (and the SliceCubes object).
    Each triangle is represented by three records, with each record
    consisting of six single precision floating point numbers
    representing the a triangle vertex coordinate and vertex normal.
    
    Caveats:
    
    Binary files are written in sun/hp/sgi (i.e., Big Endian) form.
    
    See Also:
    
    MarchingCubes SliceCubes MCubesReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMCubesWriter, obj, update, **traits)
    
    limits_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/get file name of marching cubes limits file.
        """
    )
    def _limits_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLimitsFileName,
                        self.limits_file_name)

    _updateable_traits_ = \
    (('vectors_name', 'GetVectorsName'), ('global_ids_name',
    'GetGlobalIdsName'), ('tensors_name', 'GetTensorsName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('lookup_table_name', 'GetLookupTableName'),
    ('write_to_output_string', 'GetWriteToOutputString'), ('file_type',
    'GetFileType'), ('file_name', 'GetFileName'), ('scalars_name',
    'GetScalarsName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('limits_file_name', 'GetLimitsFileName'), ('header',
    'GetHeader'), ('abort_execute', 'GetAbortExecute'), ('t_coords_name',
    'GetTCoordsName'), ('normals_name', 'GetNormalsName'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('field_data_name',
    'GetFieldDataName'), ('pedigree_ids_name', 'GetPedigreeIdsName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'file_type',
    'field_data_name', 'file_name', 'global_ids_name', 'header',
    'limits_file_name', 'lookup_table_name', 'normals_name',
    'pedigree_ids_name', 'progress_text', 'scalars_name', 't_coords_name',
    'tensors_name', 'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MCubesWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MCubesWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['write_to_output_string'], ['file_type'],
            ['field_data_name', 'file_name', 'global_ids_name', 'header',
            'limits_file_name', 'lookup_table_name', 'normals_name',
            'pedigree_ids_name', 'scalars_name', 't_coords_name', 'tensors_name',
            'vectors_name']),
            title='Edit MCubesWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MCubesWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

