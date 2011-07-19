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


class GenericDataObjectReader(DataReader):
    """
    GenericDataObjectReader - class to read any type of vtk data object
    
    Superclass: DataReader
    
    GenericDataObjectReader is a class that provides instance
    variables and methods to read any type of data object in
    Visualization Toolkit (vtk) format.  The output type of this class
    will vary depending upon the type of data file. Convenience methods
    are provided to return the data as a particular type. (See text for
    format description details). The superclass of this class,
    DataReader, provides many methods for controlling the reading of
    the data file, see DataReader for more information.
    
    Caveats:
    
    Binary files written on one system may not be readable on other
    systems.
    
    See Also:
    
    DataReader GraphReader PolyDataReader
    RectilinearGridReader StructuredPointsReader
    StructuredGridReader TableReader TreeReader
    UnstructuredGridReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericDataObjectReader, obj, update, **traits)
    
    def _get_graph_output(self):
        return wrap_vtk(self._vtk_obj.GetGraphOutput())
    graph_output = traits.Property(_get_graph_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self, idx=None):
        """
        V.get_output() -> DataObject
        C++: DataObject *GetOutput()
        V.get_output(int) -> DataObject
        C++: DataObject *GetOutput(int idx)
        Get the output of this filter
        """
        if idx is None:
            return wrap_vtk(self._vtk_obj.GetOutput())
        else:
            return wrap_vtk(self._vtk_obj.GetOutput(idx))

    def _get_poly_data_output(self):
        return wrap_vtk(self._vtk_obj.GetPolyDataOutput())
    poly_data_output = traits.Property(_get_poly_data_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_rectilinear_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetRectilinearGridOutput())
    rectilinear_grid_output = traits.Property(_get_rectilinear_grid_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_structured_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetStructuredGridOutput())
    structured_grid_output = traits.Property(_get_structured_grid_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_structured_points_output(self):
        return wrap_vtk(self._vtk_obj.GetStructuredPointsOutput())
    structured_points_output = traits.Property(_get_structured_points_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_table_output(self):
        return wrap_vtk(self._vtk_obj.GetTableOutput())
    table_output = traits.Property(_get_table_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_tree_output(self):
        return wrap_vtk(self._vtk_obj.GetTreeOutput())
    tree_output = traits.Property(_get_tree_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def _get_unstructured_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetUnstructuredGridOutput())
    unstructured_grid_output = traits.Property(_get_unstructured_grid_output, help=\
        """
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general get_output() method. If the
        wrong type is used NULL is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
    )

    def read_output_type(self):
        """
        V.read_output_type() -> int
        C++: virtual int ReadOutputType()
        This method can be used to find out the type of output expected
        without needing to read the whole file.
        """
        ret = self._vtk_obj.ReadOutputType()
        return ret
        

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
            return super(GenericDataObjectReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericDataObjectReader properties', scrollable=True, resizable=True,
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
            title='Edit GenericDataObjectReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericDataObjectReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

