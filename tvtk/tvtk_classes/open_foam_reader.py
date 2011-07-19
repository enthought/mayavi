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


class OpenFOAMReader(MultiBlockDataSetAlgorithm):
    """
    OpenFOAMReader - reads a dataset in open_foam format
    
    Superclass: MultiBlockDataSetAlgorithm
    
    OpenFOAMReader creates a multiblock dataset. It reads mesh
    information and time dependent data.  The poly_mesh folders contain
    mesh information. The time folders contain transient data for the
    cells. Each folder can contain any number of data files.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenFOAMReader, obj, update, **traits)
    
    decompose_polyhedra = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether polyhedra are to be decomposed.
        """
    )
    def _decompose_polyhedra_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDecomposePolyhedra,
                        self.decompose_polyhedra_)

    cache_mesh = tvtk_base.true_bool_trait(help=\
        """
        Set/Get whether mesh is to be cached.
        """
    )
    def _cache_mesh_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCacheMesh,
                        self.cache_mesh_)

    list_time_steps_by_control_dict = tvtk_base.false_bool_trait(help=\
        """
        Determine if time directories are to be listed according to
        control_dict
        """
    )
    def _list_time_steps_by_control_dict_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetListTimeStepsByControlDict,
                        self.list_time_steps_by_control_dict_)

    positions_is_in13_format = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether the lagrangian/positions is in OF 1.3 format
        """
    )
    def _positions_is_in13_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPositionsIsIn13Format,
                        self.positions_is_in13_format_)

    add_dimensions_to_array_names = tvtk_base.false_bool_trait(help=\
        """
        Add dimensions to array names
        """
    )
    def _add_dimensions_to_array_names_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAddDimensionsToArrayNames,
                        self.add_dimensions_to_array_names_)

    read_zones = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether zones will be read.
        """
    )
    def _read_zones_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadZones,
                        self.read_zones_)

    create_cell_to_point = tvtk_base.true_bool_trait(help=\
        """
        Set/Get whether to create cell-to-point translated data for
        cell-type data
        """
    )
    def _create_cell_to_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCreateCellToPoint,
                        self.create_cell_to_point_)

    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *name)
        Get/Set whether the point array with the given name is to be
        read.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(string, int)
        C++: void SetPointArrayStatus(const char *name, int status)
        Get/Set whether the point array with the given name is to be
        read.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    def get_lagrangian_array_status(self, *args):
        """
        V.get_lagrangian_array_status(string) -> int
        C++: int GetLagrangianArrayStatus(const char *name)
        Get/Set whether the Lagrangian array with the given name is to be
        read.
        """
        ret = self._wrap_call(self._vtk_obj.GetLagrangianArrayStatus, *args)
        return ret

    def set_lagrangian_array_status(self, *args):
        """
        V.set_lagrangian_array_status(string, int)
        C++: void SetLagrangianArrayStatus(const char *name, int status)
        Get/Set whether the Lagrangian array with the given name is to be
        read.
        """
        ret = self._wrap_call(self._vtk_obj.SetLagrangianArrayStatus, *args)
        return ret

    def get_patch_array_status(self, *args):
        """
        V.get_patch_array_status(string) -> int
        C++: int GetPatchArrayStatus(const char *name)
        Get/Set whether the Patch with the given name is to be read.
        """
        ret = self._wrap_call(self._vtk_obj.GetPatchArrayStatus, *args)
        return ret

    def set_patch_array_status(self, *args):
        """
        V.set_patch_array_status(string, int)
        C++: void SetPatchArrayStatus(const char *name, int status)
        Get/Set whether the Patch with the given name is to be read.
        """
        ret = self._wrap_call(self._vtk_obj.SetPatchArrayStatus, *args)
        return ret

    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(string) -> int
        C++: int GetCellArrayStatus(const char *name)
        Get/Set whether the cell array with the given name is to be read.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(string, int)
        C++: void SetCellArrayStatus(const char *name, int status)
        Get/Set whether the cell array with the given name is to be read.
        """
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the filename.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int) -> string
        C++: const char *GetCellArrayName(int index)
        Get the name of the  cell array with the given index in the
        input.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def get_lagrangian_array_name(self, *args):
        """
        V.get_lagrangian_array_name(int) -> string
        C++: const char *GetLagrangianArrayName(int index)
        Get the name of the  Lagrangian array with the given index in the
        input.
        """
        ret = self._wrap_call(self._vtk_obj.GetLagrangianArrayName, *args)
        return ret

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        Get the number of cell arrays available in the input.
        """
    )

    def _get_number_of_lagrangian_arrays(self):
        return self._vtk_obj.GetNumberOfLagrangianArrays()
    number_of_lagrangian_arrays = traits.Property(_get_number_of_lagrangian_arrays, help=\
        """
        Get the number of Lagrangian arrays available in the input.
        """
    )

    def _get_number_of_patch_arrays(self):
        return self._vtk_obj.GetNumberOfPatchArrays()
    number_of_patch_arrays = traits.Property(_get_number_of_patch_arrays, help=\
        """
        Get the number of Patches (inlcuding Internal Mesh) available in
        the input.
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        Get the number of point arrays available in the input.
        """
    )

    def get_patch_array_name(self, *args):
        """
        V.get_patch_array_name(int) -> string
        C++: const char *GetPatchArrayName(int index)
        Get the name of the Patch with the given index in the input.
        """
        ret = self._wrap_call(self._vtk_obj.GetPatchArrayName, *args)
        return ret

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int index)
        Get the name of the  point array with the given index in the
        input.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
        return ret

    def _get_time_values(self):
        return wrap_vtk(self._vtk_obj.GetTimeValues())
    time_values = traits.Property(_get_time_values, help=\
        """
        
        """
    )

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: int CanReadFile(const char *)
        Determine if the file can be readed with this reader.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def disable_all_cell_arrays(self):
        """
        V.disable_all_cell_arrays()
        C++: void DisableAllCellArrays()
        Turn on/off all cell arrays.
        """
        ret = self._vtk_obj.DisableAllCellArrays()
        return ret
        

    def disable_all_lagrangian_arrays(self):
        """
        V.disable_all_lagrangian_arrays()
        C++: void DisableAllLagrangianArrays()
        Turn on/off all Lagrangian arrays.
        """
        ret = self._vtk_obj.DisableAllLagrangianArrays()
        return ret
        

    def disable_all_patch_arrays(self):
        """
        V.disable_all_patch_arrays()
        C++: void DisableAllPatchArrays()
        Turn on/off all Patches including the Internal Mesh.
        """
        ret = self._vtk_obj.DisableAllPatchArrays()
        return ret
        

    def disable_all_point_arrays(self):
        """
        V.disable_all_point_arrays()
        C++: void DisableAllPointArrays()
        Turn on/off all point arrays.
        """
        ret = self._vtk_obj.DisableAllPointArrays()
        return ret
        

    def enable_all_cell_arrays(self):
        """
        V.enable_all_cell_arrays()
        C++: void EnableAllCellArrays()
        Turn on/off all cell arrays.
        """
        ret = self._vtk_obj.EnableAllCellArrays()
        return ret
        

    def enable_all_lagrangian_arrays(self):
        """
        V.enable_all_lagrangian_arrays()
        C++: void EnableAllLagrangianArrays()
        Turn on/off all Lagrangian arrays.
        """
        ret = self._vtk_obj.EnableAllLagrangianArrays()
        return ret
        

    def enable_all_patch_arrays(self):
        """
        V.enable_all_patch_arrays()
        C++: void EnableAllPatchArrays()
        Turn on/off all Patches including the Internal Mesh.
        """
        ret = self._vtk_obj.EnableAllPatchArrays()
        return ret
        

    def enable_all_point_arrays(self):
        """
        V.enable_all_point_arrays()
        C++: void EnableAllPointArrays()
        Turn on/off all point arrays.
        """
        ret = self._vtk_obj.EnableAllPointArrays()
        return ret
        

    def make_information_vector(self, *args):
        """
        V.make_information_vector(InformationVector, string) -> int
        C++: int MakeInformationVector(InformationVector *,
            const StdString &)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MakeInformationVector, *my_args)
        return ret

    def make_meta_data_at_time_step(self, *args):
        """
        V.make_meta_data_at_time_step(bool) -> int
        C++: int MakeMetaDataAtTimeStep(const bool)"""
        ret = self._wrap_call(self._vtk_obj.MakeMetaDataAtTimeStep, *args)
        return ret

    def set_parent(self, *args):
        """
        V.set_parent(OpenFOAMReader)
        C++: void SetParent(OpenFOAMReader *parent)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetParent, *my_args)
        return ret

    def set_refresh(self):
        """
        V.set_refresh()
        C++: void SetRefresh()"""
        ret = self._vtk_obj.SetRefresh()
        return ret
        

    def set_time_value(self, *args):
        """
        V.set_time_value(float) -> bool
        C++: bool SetTimeValue(const double)"""
        ret = self._wrap_call(self._vtk_obj.SetTimeValue, *args)
        return ret

    _updateable_traits_ = \
    (('read_zones', 'GetReadZones'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('positions_is_in13_format', 'GetPositionsIsIn13Format'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('decompose_polyhedra', 'GetDecomposePolyhedra'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('list_time_steps_by_control_dict', 'GetListTimeStepsByControlDict'),
    ('add_dimensions_to_array_names', 'GetAddDimensionsToArrayNames'),
    ('cache_mesh', 'GetCacheMesh'), ('abort_execute', 'GetAbortExecute'),
    ('create_cell_to_point', 'GetCreateCellToPoint'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'add_dimensions_to_array_names', 'cache_mesh',
    'create_cell_to_point', 'debug', 'decompose_polyhedra',
    'global_warning_display', 'list_time_steps_by_control_dict',
    'positions_is_in13_format', 'read_zones', 'release_data_flag',
    'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenFOAMReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenFOAMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['add_dimensions_to_array_names', 'cache_mesh',
            'create_cell_to_point', 'decompose_polyhedra',
            'list_time_steps_by_control_dict', 'positions_is_in13_format',
            'read_zones'], [], ['file_name']),
            title='Edit OpenFOAMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenFOAMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

