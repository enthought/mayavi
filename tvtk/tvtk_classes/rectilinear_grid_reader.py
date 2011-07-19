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

from tvtk.tvtk_classes.data_reader import DataReader


class RectilinearGridReader(DataReader):
    """
    RectilinearGridReader - read vtk rectilinear grid data file
    
    Superclass: DataReader
    
    RectilinearGridReader is a source object that reads ASCII or
    binary rectilinear grid data files in vtk format (see text for format
    details). The output of this reader is a single RectilinearGrid
    data object. The superclass of this class, DataReader, provides
    many methods for controlling the reading of the data file, see
    DataReader for more information.
    
    Caveats:
    
    Binary files written on one system may not be readable on other
    systems.
    
    See Also:
    
    RectilinearGrid DataReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRectilinearGridReader, obj, update, **traits)
    
    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    def _set_output(self, obj):
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)
    output = traits.Property(_get_output, _set_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self, idx=None):
        """
        V.get_output() -> RectilinearGrid
        C++: RectilinearGrid *GetOutput()
        V.get_output(int) -> RectilinearGrid
        C++: RectilinearGrid *GetOutput(int idx)
        Get and set the output of this reader.
        """
        if idx is None:
            return wrap_vtk(self._vtk_obj.GetOutput())
        else:
            return wrap_vtk(self._vtk_obj.GetOutput(idx))

    def set_output(self, obj):
        """
        V.set_output(RectilinearGrid)
        C++: void SetOutput(RectilinearGrid *output)
        Get and set the output of this reader.
        """
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)

    _updateable_traits_ = \
    (('vectors_name', 'GetVectorsName'), ('tensors_name',
    'GetTensorsName'), ('file_name', 'GetFileName'), ('scalars_name',
    'GetScalarsName'), ('read_from_input_string',
    'GetReadFromInputString'), ('read_all_vectors', 'GetReadAllVectors'),
    ('input_string', 'GetInputString'), ('normals_name',
    'GetNormalsName'), ('t_coords_name', 'GetTCoordsName'),
    ('read_all_fields', 'GetReadAllFields'), ('field_data_name',
    'GetFieldDataName'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('lookup_table_name',
    'GetLookupTableName'), ('read_all_t_coords', 'GetReadAllTCoords'),
    ('debug', 'GetDebug'), ('read_all_tensors', 'GetReadAllTensors'),
    ('progress_text', 'GetProgressText'), ('read_all_scalars',
    'GetReadAllScalars'), ('read_all_normals', 'GetReadAllNormals'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('read_all_color_scalars',
    'GetReadAllColorScalars'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'read_all_color_scalars', 'read_all_fields', 'read_all_normals',
    'read_all_scalars', 'read_all_t_coords', 'read_all_tensors',
    'read_all_vectors', 'read_from_input_string', 'release_data_flag',
    'field_data_name', 'file_name', 'input_string', 'lookup_table_name',
    'normals_name', 'progress_text', 'scalars_name', 't_coords_name',
    'tensors_name', 'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RectilinearGridReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RectilinearGridReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['read_all_color_scalars', 'read_all_fields',
            'read_all_normals', 'read_all_scalars', 'read_all_t_coords',
            'read_all_tensors', 'read_all_vectors', 'read_from_input_string'], [],
            ['field_data_name', 'file_name', 'input_string', 'lookup_table_name',
            'normals_name', 'scalars_name', 't_coords_name', 'tensors_name',
            'vectors_name']),
            title='Edit RectilinearGridReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RectilinearGridReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

