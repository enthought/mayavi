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

from tvtk.tvtk_classes.algorithm import Algorithm


class DataReader(Algorithm):
    """
    DataReader - helper superclass for objects that read vtk data files
    
    Superclass: Algorithm
    
    DataReader is a helper superclass that reads the vtk data file
    header, dataset type, and attribute data (point and cell attributes
    such as scalars, vectors, normals, etc.) from a vtk data file.  See
    text for the format of the various vtk file types.
    
    See Also:
    
    PolyDataReader StructuredPointsReader StructuredGridReader
    UnstructuredGridReader RectilinearGridReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataReader, obj, update, **traits)
    
    read_all_vectors = tvtk_base.false_bool_trait(help=\
        """
        Enable reading all vectors.
        """
    )
    def _read_all_vectors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadAllVectors,
                        self.read_all_vectors_)

    read_all_normals = tvtk_base.false_bool_trait(help=\
        """
        Enable reading all normals.
        """
    )
    def _read_all_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadAllNormals,
                        self.read_all_normals_)

    read_all_t_coords = tvtk_base.false_bool_trait(help=\
        """
        Enable reading all tcoords.
        """
    )
    def _read_all_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadAllTCoords,
                        self.read_all_t_coords_)

    read_all_tensors = tvtk_base.false_bool_trait(help=\
        """
        Enable reading all tensors.
        """
    )
    def _read_all_tensors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadAllTensors,
                        self.read_all_tensors_)

    read_all_scalars = tvtk_base.false_bool_trait(help=\
        """
        Enable reading all scalars.
        """
    )
    def _read_all_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadAllScalars,
                        self.read_all_scalars_)

    read_all_fields = tvtk_base.false_bool_trait(help=\
        """
        Enable reading all fields.
        """
    )
    def _read_all_fields_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadAllFields,
                        self.read_all_fields_)

    read_from_input_string = tvtk_base.false_bool_trait(help=\
        """
        Enable reading from an input_string or input_array instead of the
        default, a file.
        """
    )
    def _read_from_input_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadFromInputString,
                        self.read_from_input_string_)

    read_all_color_scalars = tvtk_base.false_bool_trait(help=\
        """
        Enable reading all color scalars.
        """
    )
    def _read_all_color_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadAllColorScalars,
                        self.read_all_color_scalars_)

    t_coords_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the texture coordinate data to extract. If not
        specified, first texture coordinate data encountered is
        extracted.
        """
    )
    def _t_coords_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTCoordsName,
                        self.t_coords_name)

    lookup_table_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the lookup table data to extract. If not
        specified, uses lookup table named by scalar. Otherwise, this
        specification supersedes.
        """
    )
    def _lookup_table_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLookupTableName,
                        self.lookup_table_name)

    def _get_input_array(self):
        return wrap_vtk(self._vtk_obj.GetInputArray())
    def _set_input_array(self, arg):
        old_val = self._get_input_array()
        my_arg = deref_array([arg], [['vtkCharArray']])
        self._wrap_call(self._vtk_obj.SetInputArray,
                        my_arg[0])
        self.trait_property_changed('input_array', old_val, arg)
    input_array = traits.Property(_get_input_array, _set_input_array, help=\
        """
        Specify the CharArray to be used  when reading from a string.
        If set, this array has precendence over input_string. Use this
        instead of input_string to avoid the extra memory copy. It should
        be noted that if the underlying char* is owned by the user (
        CharArray::SetArray(array, 1); ) and is deleted before the
        reader, bad things will happen during a pipeline update.
        """
    )

    input_string = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the input_string for use when reading from a character
        array. Optionally include the length for binary strings. Note
        that a copy of the string is made and stored. If this causes
        exceedingly large memory consumption, consider using input_array
        instead.
        """
    )
    def _input_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputString,
                        self.input_string)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of vtk data file to read.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    scalars_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the scalar data to extract. If not specified,
        first scalar data encountered is extracted.
        """
    )
    def _scalars_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarsName,
                        self.scalars_name)

    field_data_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the field data to extract. If not specified, uses
        first field data encountered in file.
        """
    )
    def _field_data_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDataName,
                        self.field_data_name)

    tensors_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the tensor data to extract. If not specified,
        first tensor data encountered is extracted.
        """
    )
    def _tensors_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTensorsName,
                        self.tensors_name)

    normals_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the normal data to extract. If not specified,
        first normal data encountered is extracted.
        """
    )
    def _normals_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalsName,
                        self.normals_name)

    vectors_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the vector data to extract. If not specified,
        first vector data encountered is extracted.
        """
    )
    def _vectors_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorsName,
                        self.vectors_name)

    def get_field_data_name_in_file(self, *args):
        """
        V.get_field_data_name_in_file(int) -> string
        C++: const char *GetFieldDataNameInFile(int i)
        What is the name of the ith attribute of a certain type in this
        file? This requires reading the file, so the filename must be set
        prior to invoking this operation.
        """
        ret = self._wrap_call(self._vtk_obj.GetFieldDataNameInFile, *args)
        return ret

    def _get_file_type(self):
        return self._vtk_obj.GetFileType()
    file_type = traits.Property(_get_file_type, help=\
        """
        Get the type of file (ASCII or BINARY). Returned value only valid
        after file has been read.
        """
    )

    def _get_header(self):
        return self._vtk_obj.GetHeader()
    header = traits.Property(_get_header, help=\
        """
        Get the header from the vtk data file.
        """
    )

    def _get_input_string_length(self):
        return self._vtk_obj.GetInputStringLength()
    input_string_length = traits.Property(_get_input_string_length, help=\
        """
        Specify the input_string for use when reading from a character
        array. Optionally include the length for binary strings. Note
        that a copy of the string is made and stored. If this causes
        exceedingly large memory consumption, consider using input_array
        instead.
        """
    )

    def get_normals_name_in_file(self, *args):
        """
        V.get_normals_name_in_file(int) -> string
        C++: const char *GetNormalsNameInFile(int i)
        What is the name of the ith attribute of a certain type in this
        file? This requires reading the file, so the filename must be set
        prior to invoking this operation.
        """
        ret = self._wrap_call(self._vtk_obj.GetNormalsNameInFile, *args)
        return ret

    def _get_number_of_field_data_in_file(self):
        return self._vtk_obj.GetNumberOfFieldDataInFile()
    number_of_field_data_in_file = traits.Property(_get_number_of_field_data_in_file, help=\
        """
        How many attributes of various types are in this file? This
        requires reading the file, so the filename must be set prior to
        invoking this operation. (Note: file characteristics are cached,
        so only a single read is necessary to return file
        characteristics.)
        """
    )

    def _get_number_of_normals_in_file(self):
        return self._vtk_obj.GetNumberOfNormalsInFile()
    number_of_normals_in_file = traits.Property(_get_number_of_normals_in_file, help=\
        """
        How many attributes of various types are in this file? This
        requires reading the file, so the filename must be set prior to
        invoking this operation. (Note: file characteristics are cached,
        so only a single read is necessary to return file
        characteristics.)
        """
    )

    def _get_number_of_scalars_in_file(self):
        return self._vtk_obj.GetNumberOfScalarsInFile()
    number_of_scalars_in_file = traits.Property(_get_number_of_scalars_in_file, help=\
        """
        How many attributes of various types are in this file? This
        requires reading the file, so the filename must be set prior to
        invoking this operation. (Note: file characteristics are cached,
        so only a single read is necessary to return file
        characteristics.)
        """
    )

    def _get_number_of_t_coords_in_file(self):
        return self._vtk_obj.GetNumberOfTCoordsInFile()
    number_of_t_coords_in_file = traits.Property(_get_number_of_t_coords_in_file, help=\
        """
        How many attributes of various types are in this file? This
        requires reading the file, so the filename must be set prior to
        invoking this operation. (Note: file characteristics are cached,
        so only a single read is necessary to return file
        characteristics.)
        """
    )

    def _get_number_of_tensors_in_file(self):
        return self._vtk_obj.GetNumberOfTensorsInFile()
    number_of_tensors_in_file = traits.Property(_get_number_of_tensors_in_file, help=\
        """
        How many attributes of various types are in this file? This
        requires reading the file, so the filename must be set prior to
        invoking this operation. (Note: file characteristics are cached,
        so only a single read is necessary to return file
        characteristics.)
        """
    )

    def _get_number_of_vectors_in_file(self):
        return self._vtk_obj.GetNumberOfVectorsInFile()
    number_of_vectors_in_file = traits.Property(_get_number_of_vectors_in_file, help=\
        """
        How many attributes of various types are in this file? This
        requires reading the file, so the filename must be set prior to
        invoking this operation. (Note: file characteristics are cached,
        so only a single read is necessary to return file
        characteristics.)
        """
    )

    def get_scalars_name_in_file(self, *args):
        """
        V.get_scalars_name_in_file(int) -> string
        C++: const char *GetScalarsNameInFile(int i)
        What is the name of the ith attribute of a certain type in this
        file? This requires reading the file, so the filename must be set
        prior to invoking this operation.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarsNameInFile, *args)
        return ret

    def get_t_coords_name_in_file(self, *args):
        """
        V.get_t_coords_name_in_file(int) -> string
        C++: const char *GetTCoordsNameInFile(int i)
        What is the name of the ith attribute of a certain type in this
        file? This requires reading the file, so the filename must be set
        prior to invoking this operation.
        """
        ret = self._wrap_call(self._vtk_obj.GetTCoordsNameInFile, *args)
        return ret

    def get_tensors_name_in_file(self, *args):
        """
        V.get_tensors_name_in_file(int) -> string
        C++: const char *GetTensorsNameInFile(int i)
        What is the name of the ith attribute of a certain type in this
        file? This requires reading the file, so the filename must be set
        prior to invoking this operation.
        """
        ret = self._wrap_call(self._vtk_obj.GetTensorsNameInFile, *args)
        return ret

    def get_vectors_name_in_file(self, *args):
        """
        V.get_vectors_name_in_file(int) -> string
        C++: const char *GetVectorsNameInFile(int i)
        What is the name of the ith attribute of a certain type in this
        file? This requires reading the file, so the filename must be set
        prior to invoking this operation.
        """
        ret = self._wrap_call(self._vtk_obj.GetVectorsNameInFile, *args)
        return ret

    def close_vtk_file(self):
        """
        V.close_vtk_file()
        C++: void CloseVTKFile()
        Close the vtk file.
        """
        ret = self._vtk_obj.CloseVTKFile()
        return ret
        

    def is_file_poly_data(self):
        """
        V.is_file_poly_data() -> int
        C++: int IsFilePolyData()
        Is the file a valid vtk file of the passed dataset type ? The
        dataset type is passed as a lower case string.
        """
        ret = self._vtk_obj.IsFilePolyData()
        return ret
        

    def is_file_rectilinear_grid(self):
        """
        V.is_file_rectilinear_grid() -> int
        C++: int IsFileRectilinearGrid()
        Is the file a valid vtk file of the passed dataset type ? The
        dataset type is passed as a lower case string.
        """
        ret = self._vtk_obj.IsFileRectilinearGrid()
        return ret
        

    def is_file_structured_grid(self):
        """
        V.is_file_structured_grid() -> int
        C++: int IsFileStructuredGrid()
        Is the file a valid vtk file of the passed dataset type ? The
        dataset type is passed as a lower case string.
        """
        ret = self._vtk_obj.IsFileStructuredGrid()
        return ret
        

    def is_file_structured_points(self):
        """
        V.is_file_structured_points() -> int
        C++: int IsFileStructuredPoints()
        Is the file a valid vtk file of the passed dataset type ? The
        dataset type is passed as a lower case string.
        """
        ret = self._vtk_obj.IsFileStructuredPoints()
        return ret
        

    def is_file_unstructured_grid(self):
        """
        V.is_file_unstructured_grid() -> int
        C++: int IsFileUnstructuredGrid()
        Is the file a valid vtk file of the passed dataset type ? The
        dataset type is passed as a lower case string.
        """
        ret = self._vtk_obj.IsFileUnstructuredGrid()
        return ret
        

    def is_file_valid(self, *args):
        """
        V.is_file_valid(string) -> int
        C++: int IsFileValid(const char *dstype)
        Is the file a valid vtk file of the passed dataset type ? The
        dataset type is passed as a lower case string.
        """
        ret = self._wrap_call(self._vtk_obj.IsFileValid, *args)
        return ret

    def lower_case(self, *args):
        """
        V.lower_case(string, int) -> string
        C++: char *LowerCase(char *str, const size_t len=256)
        Helper method for reading in data.
        """
        ret = self._wrap_call(self._vtk_obj.LowerCase, *args)
        return ret

    def open_vtk_file(self):
        """
        V.open_vtk_file() -> int
        C++: int OpenVTKFile()
        Open a vtk data file. Returns zero if error.
        """
        ret = self._vtk_obj.OpenVTKFile()
        return ret
        

    def read(self, *args):
        """
        V.read(string) -> int
        C++: int Read(char *)
        Internal function to read in a value.  Returns zero if there was
        an error.
        """
        ret = self._wrap_call(self._vtk_obj.Read, *args)
        return ret

    def read_array(self, *args):
        """
        V.read_array(string, int, int) -> AbstractArray
        C++: AbstractArray *ReadArray(const char *dataType,
            int numTuples, int numComp)
        Helper functions for reading data.
        """
        ret = self._wrap_call(self._vtk_obj.ReadArray, *args)
        return wrap_vtk(ret)

    def read_cell_data(self, *args):
        """
        V.read_cell_data(DataSet, int) -> int
        C++: int ReadCellData(DataSet *ds, int numCells)
        Read the cell data of a vtk data file. The number of cells (from
        the dataset) must match the number of cells defined in cell
        attributes (unless no geometry was defined).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadCellData, *my_args)
        return ret

    def read_coordinates(self, *args):
        """
        V.read_coordinates(RectilinearGrid, int, int) -> int
        C++: int ReadCoordinates(RectilinearGrid *rg, int axes,
            int numCoords)
        Read the coordinates for a rectilinear grid. The axes parameter
        specifies which coordinate axes (0,1,2) is being read.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadCoordinates, *my_args)
        return ret

    def read_edge_data(self, *args):
        """
        V.read_edge_data(Graph, int) -> int
        C++: int ReadEdgeData(Graph *g, int numEdges)
        Read the edge data of a vtk data file. The number of edges (from
        the graph) must match the number of edges defined in edge
        attributes (unless no geometry was defined).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadEdgeData, *my_args)
        return ret

    def read_field_data(self):
        """
        V.read_field_data() -> FieldData
        C++: FieldData *ReadFieldData()
        Helper functions for reading data.
        """
        ret = wrap_vtk(self._vtk_obj.ReadFieldData())
        return ret
        

    def read_header(self):
        """
        V.read_header() -> int
        C++: int ReadHeader()
        Read the header of a vtk data file. Returns 0 if error.
        """
        ret = self._vtk_obj.ReadHeader()
        return ret
        

    def read_line(self, *args):
        """
        V.read_line([char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char]) -> int
        C++: int ReadLine(char result[256])
        Internal function to read in a line up to 256 characters. Returns
        zero if there was an error.
        """
        ret = self._wrap_call(self._vtk_obj.ReadLine, *args)
        return ret

    def read_meta_data(self, *args):
        """
        V.read_meta_data(Information) -> int
        C++: virtual int ReadMetaData(Information *)
        Read the meta information from the file.  This needs to be public
        to it can be accessed by DataSetReader.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadMetaData, *my_args)
        return ret

    def read_point_data(self, *args):
        """
        V.read_point_data(DataSet, int) -> int
        C++: int ReadPointData(DataSet *ds, int numPts)
        Read the point data of a vtk data file. The number of points
        (from the dataset) must match the number of points defined in
        point attributes (unless no geometry was defined).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadPointData, *my_args)
        return ret

    def read_points(self, *args):
        """
        V.read_points(PointSet, int) -> int
        C++: int ReadPoints(PointSet *ps, int numPts)
        V.read_points(Graph, int) -> int
        C++: int ReadPoints(Graph *g, int numPts)
        Read point coordinates. Return 0 if error.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadPoints, *my_args)
        return ret

    def read_row_data(self, *args):
        """
        V.read_row_data(Table, int) -> int
        C++: int ReadRowData(Table *t, int numEdges)
        Read the row data of a vtk data file.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadRowData, *my_args)
        return ret

    def read_string(self, *args):
        """
        V.read_string([char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char, char, char,
            char, char, char, char, char, char, char, char]) -> int
        C++: int ReadString(char result[256])
        Internal function to read in a string up to 256 characters.
        Returns zero if there was an error.
        """
        ret = self._wrap_call(self._vtk_obj.ReadString, *args)
        return ret

    def read_vertex_data(self, *args):
        """
        V.read_vertex_data(Graph, int) -> int
        C++: int ReadVertexData(Graph *g, int numVertices)
        Read the vertex data of a vtk data file. The number of vertices
        (from the graph) must match the number of vertices defined in
        vertex attributes (unless no geometry was defined).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadVertexData, *my_args)
        return ret

    def set_binary_input_string(self, *args):
        """
        V.set_binary_input_string(string, int)
        C++: void SetBinaryInputString(const char *, int len)
        Specify the input_string for use when reading from a character
        array. Optionally include the length for binary strings. Note
        that a copy of the string is made and stored. If this causes
        exceedingly large memory consumption, consider using input_array
        instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetBinaryInputString, *args)
        return ret

    _updateable_traits_ = \
    (('vectors_name', 'GetVectorsName'), ('tensors_name',
    'GetTensorsName'), ('file_name', 'GetFileName'), ('scalars_name',
    'GetScalarsName'), ('read_from_input_string',
    'GetReadFromInputString'), ('read_all_vectors', 'GetReadAllVectors'),
    ('t_coords_name', 'GetTCoordsName'), ('normals_name',
    'GetNormalsName'), ('input_string', 'GetInputString'),
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
            return super(DataReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataReader properties', scrollable=True, resizable=True,
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
            title='Edit DataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

