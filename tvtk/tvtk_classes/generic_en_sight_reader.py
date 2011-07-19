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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class GenericEnSightReader(MultiBlockDataSetAlgorithm):
    """
    GenericEnSightReader - class to read any type of en_sight files
    
    Superclass: MultiBlockDataSetAlgorithm
    
    The class GenericEnSightReader allows the user to read an en_sight
    data set without a priori knowledge of what type of en_sight data set
    it is.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericEnSightReader, obj, update, **traits)
    
    read_all_variables = tvtk_base.true_bool_trait(help=\
        """
        Set/get the flag for whether to read all the variables
        """
    )
    def _read_all_variables_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadAllVariables,
                        self.read_all_variables_)

    particle_coordinates_by_index = tvtk_base.false_bool_trait(help=\
        """
        The measured_geometry_file should list particle coordinates from
        0->N-1. If a file is loaded where point Ids are listed from 1-N
        the Id to points reference will be wrong and the data will be
        generated incorrectly. Setting particle_coordinates_by_index to true
        will force all Id's to increment from 0->N-1 (relative to their
        order in the file) and regardless of the actual Id of of the
        point. Warning, if the Points are listed in non sequential order
        then setting this flag will reorder them.
        """
    )
    def _particle_coordinates_by_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetParticleCoordinatesByIndex,
                        self.particle_coordinates_by_index_)

    byte_order = traits.Trait('big_endian', 2,
    tvtk_base.TraitRevPrefixMap({'big_endian': 0, 'little_endian': 1}), help=\
        """
        Set the byte order of the file (remember, more Unix workstations
        write big endian whereas PCs write little endian). Default is big
        endian (since most older plot3d files were written by
        workstations).
        """
    )
    def _byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetByteOrder,
                        self.byte_order_)

    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *name)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(string, int)
        C++: void SetPointArrayStatus(const char *name, int status)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    file_path = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the file path.
        """
    )
    def _file_path_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePath,
                        self.file_path)

    time_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the time value at which to get the value.
        """
    )
    def _time_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeValue,
                        self.time_value)

    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(string) -> int
        C++: int GetCellArrayStatus(const char *name)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(string, int)
        C++: void SetCellArrayStatus(const char *name, int status)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    case_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the Case file name.
        """
    )
    def _case_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCaseFileName,
                        self.case_file_name)

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int) -> string
        C++: const char *GetCellArrayName(int index)
        Get the name of the point or cell array with the given index in
        the input.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def _get_cell_data_array_selection(self):
        return wrap_vtk(self._vtk_obj.GetCellDataArraySelection())
    cell_data_array_selection = traits.Property(_get_cell_data_array_selection, help=\
        """
        Get the data array selection tables used to configure which data
        arrays are loaded by the reader.
        """
    )

    def get_complex_description(self, *args):
        """
        V.get_complex_description(int) -> string
        C++: const char *GetComplexDescription(int n)
        Get the nth description for a complex variable.
        """
        ret = self._wrap_call(self._vtk_obj.GetComplexDescription, *args)
        return ret

    def get_complex_variable_type(self, *args):
        """
        V.get_complex_variable_type(int) -> int
        C++: int GetComplexVariableType(int n)
        Get the variable type of variable n.
        """
        ret = self._wrap_call(self._vtk_obj.GetComplexVariableType, *args)
        return ret

    def get_description(self, *args):
        """
        V.get_description(int) -> string
        C++: const char *GetDescription(int n)
        V.get_description(int, int) -> string
        C++: const char *GetDescription(int n, int type)
        Get the nth description for a non-complex variable.
        """
        ret = self._wrap_call(self._vtk_obj.GetDescription, *args)
        return ret

    def _get_en_sight_version(self):
        return self._vtk_obj.GetEnSightVersion()
    en_sight_version = traits.Property(_get_en_sight_version, help=\
        """
        Get the en_sight file version being read.
        """
    )

    def _get_geometry_file_name(self):
        return self._vtk_obj.GetGeometryFileName()
    geometry_file_name = traits.Property(_get_geometry_file_name, help=\
        """
        Get the Geometry file name. Made public to allow access from apps
        requiring detailed info about the Data contents
        """
    )

    def _get_maximum_time_value(self):
        return self._vtk_obj.GetMaximumTimeValue()
    maximum_time_value = traits.Property(_get_maximum_time_value, help=\
        """
        Get the minimum or maximum time value for this data set.
        """
    )

    def _get_minimum_time_value(self):
        return self._vtk_obj.GetMinimumTimeValue()
    minimum_time_value = traits.Property(_get_minimum_time_value, help=\
        """
        Get the minimum or maximum time value for this data set.
        """
    )

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        Get the number of point or cell arrays available in the input.
        """
    )

    def _get_number_of_complex_scalars_per_element(self):
        return self._vtk_obj.GetNumberOfComplexScalarsPerElement()
    number_of_complex_scalars_per_element = traits.Property(_get_number_of_complex_scalars_per_element, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_complex_scalars_per_node(self):
        return self._vtk_obj.GetNumberOfComplexScalarsPerNode()
    number_of_complex_scalars_per_node = traits.Property(_get_number_of_complex_scalars_per_node, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_complex_variables(self):
        return self._vtk_obj.GetNumberOfComplexVariables()
    number_of_complex_variables = traits.Property(_get_number_of_complex_variables, help=\
        """
        Get the number of variables listed in the case file.
        """
    )

    def _get_number_of_complex_vectors_per_element(self):
        return self._vtk_obj.GetNumberOfComplexVectorsPerElement()
    number_of_complex_vectors_per_element = traits.Property(_get_number_of_complex_vectors_per_element, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_complex_vectors_per_node(self):
        return self._vtk_obj.GetNumberOfComplexVectorsPerNode()
    number_of_complex_vectors_per_node = traits.Property(_get_number_of_complex_vectors_per_node, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        Get the number of point or cell arrays available in the input.
        """
    )

    def _get_number_of_scalars_per_element(self):
        return self._vtk_obj.GetNumberOfScalarsPerElement()
    number_of_scalars_per_element = traits.Property(_get_number_of_scalars_per_element, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_scalars_per_measured_node(self):
        return self._vtk_obj.GetNumberOfScalarsPerMeasuredNode()
    number_of_scalars_per_measured_node = traits.Property(_get_number_of_scalars_per_measured_node, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_scalars_per_node(self):
        return self._vtk_obj.GetNumberOfScalarsPerNode()
    number_of_scalars_per_node = traits.Property(_get_number_of_scalars_per_node, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_tensors_symm_per_element(self):
        return self._vtk_obj.GetNumberOfTensorsSymmPerElement()
    number_of_tensors_symm_per_element = traits.Property(_get_number_of_tensors_symm_per_element, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_tensors_symm_per_node(self):
        return self._vtk_obj.GetNumberOfTensorsSymmPerNode()
    number_of_tensors_symm_per_node = traits.Property(_get_number_of_tensors_symm_per_node, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_variables(self):
        return self._vtk_obj.GetNumberOfVariables()
    number_of_variables = traits.Property(_get_number_of_variables, help=\
        """
        Get the number of variables listed in the case file.
        """
    )

    def _get_number_of_vectors_per_element(self):
        return self._vtk_obj.GetNumberOfVectorsPerElement()
    number_of_vectors_per_element = traits.Property(_get_number_of_vectors_per_element, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_vectors_per_measured_node(self):
        return self._vtk_obj.GetNumberOfVectorsPerMeasuredNode()
    number_of_vectors_per_measured_node = traits.Property(_get_number_of_vectors_per_measured_node, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def _get_number_of_vectors_per_node(self):
        return self._vtk_obj.GetNumberOfVectorsPerNode()
    number_of_vectors_per_node = traits.Property(_get_number_of_vectors_per_node, help=\
        """
        Get the number of variables of a particular type.
        """
    )

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int index)
        Get the name of the point or cell array with the given index in
        the input.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
        return ret

    def _get_point_data_array_selection(self):
        return wrap_vtk(self._vtk_obj.GetPointDataArraySelection())
    point_data_array_selection = traits.Property(_get_point_data_array_selection, help=\
        """
        Get the data array selection tables used to configure which data
        arrays are loaded by the reader.
        """
    )

    def _get_reader(self):
        return wrap_vtk(self._vtk_obj.GetReader())
    reader = traits.Property(_get_reader, help=\
        """
        
        """
    )

    def _get_time_sets(self):
        return wrap_vtk(self._vtk_obj.GetTimeSets())
    time_sets = traits.Property(_get_time_sets, help=\
        """
        Get the time values per time set
        """
    )

    def get_variable_type(self, *args):
        """
        V.get_variable_type(int) -> int
        C++: int GetVariableType(int n)
        Get the variable type of variable n.
        """
        ret = self._wrap_call(self._vtk_obj.GetVariableType, *args)
        return ret

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: static int CanReadFile(const char *casefilename)
        Returns true if the file pointed to by casefilename appears to be
        a valid en_sight case file.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def determine_en_sight_version(self, *args):
        """
        V.determine_en_sight_version(int) -> int
        C++: int DetermineEnSightVersion(int quiet=0)
        Reads the FORMAT part of the case file to determine whether this
        is an en_sight6 or en_sight_gold data set.  Returns an identifier
        listed in the file_types enum or -1 if an error occurred or the
        file could not be indentified as any en_sight type.
        """
        ret = self._wrap_call(self._vtk_obj.DetermineEnSightVersion, *args)
        return ret

    _updateable_traits_ = \
    (('byte_order', 'GetByteOrder'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('abort_execute', 'GetAbortExecute'),
    ('progress_text', 'GetProgressText'), ('case_file_name',
    'GetCaseFileName'), ('debug', 'GetDebug'), ('time_value',
    'GetTimeValue'), ('read_all_variables', 'GetReadAllVariables'),
    ('particle_coordinates_by_index', 'GetParticleCoordinatesByIndex'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('file_path',
    'GetFilePath'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'particle_coordinates_by_index', 'read_all_variables',
    'release_data_flag', 'byte_order', 'case_file_name', 'file_path',
    'progress_text', 'time_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericEnSightReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericEnSightReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['particle_coordinates_by_index',
            'read_all_variables'], ['byte_order'], ['case_file_name', 'file_path',
            'time_value']),
            title='Edit GenericEnSightReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericEnSightReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

