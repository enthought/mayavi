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


class LSDynaReader(MultiBlockDataSetAlgorithm):
    """
    LSDynaReader - Read LS-Dyna databases (d3plot)
    
    Superclass: MultiBlockDataSetAlgorithm
    
    This filter reads LS-Dyna databases.
    
    The set/_get_file_name() routines are actually wrappers around the
    set/_get_database_directory() members; the actual filename you choose is
    irrelevant -- only the directory name is used.  This is done in order
    to accommodate para_view.
    
    Note that this reader produces 7 output meshes. These meshes are
    required as several attributes are defined on subsets of the mesh. 
    Below is a list of meshes in the order they are output and an
    explanation of which attributes are unique to each mesh:
    - solid (_3d) elements: number of integration points are different
      than 2d
    - thick shell elements: number of integration points are different
      than planar 2d
    - shell (_2d) elements: number of integration points are different
      than 3d
    - rigid surfaces: can't have deflection, only velocity, accel, etc.
    - road surfaces: have only a "segment ID" (serves as material ID) and
    a velocity.
    - beam elements: have Frenet (TNB) frame and cross-section attributes
      (shape and size)
    - spherical particle hydrodynamics (SPH) elements: have a radius of
      influence, internal energy, etc. Because each mesh has its own cell
    attributes, the LSDynaReader has a rather large API.  Instead of a
    single set of routines to query and set cell array names and status,
      one exists for each possible output mesh. Also, get_number_of_cells()
      will return the sum of all the cells in all 7 meshes.  If you want
      the number of cells in a specific mesh, there are separate routines
    for each mesh type.
    
    "Developer Notes":
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLSDynaReader, obj, update, **traits)
    
    deformed_mesh = tvtk_base.true_bool_trait(help=\
        """
        Should deflected coordinates be used, or should the mesh remain
        undeflected?  By default, this is true but its value is ignored
        if the nodal "Deflection" array is not set to be loaded.
        """
    )
    def _deformed_mesh_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeformedMesh,
                        self.deformed_mesh_)

    remove_deleted_cells = tvtk_base.true_bool_trait(help=\
        """
        Should dead cells be removed from the mesh?  Cells are marked
        dead by setting the corresponding entry in the cellarray "Death"
        to 0. Cells that are not dead have the corresponding entry in the
        cell array "Death" set to their material ID.  By default, this is
        true but its value is ignored if the cell "Death" array is not
        set to be loaded. It is also ignored if the database's element
        deletion option is set to denote points(not cells) as deleted; in
        that case, "Death" will appear to be a point array.
        """
    )
    def _remove_deleted_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRemoveDeletedCells,
                        self.remove_deleted_cells_)

    split_by_material_id = tvtk_base.false_bool_trait(help=\
        """
        Split each part into submeshes based on material ID. By default,
        this is false and all cells of a given type (solid, thick shell,
        shell, ...) are in a single mesh.
        """
    )
    def _split_by_material_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplitByMaterialId,
                        self.split_by_material_id_)

    database_directory = traits.String(r"", enter_set=True, auto_set=False, help=\
        """
        Get/Set the directory containing the LS-Dyna database and
        determine whether it is valid.
        """
    )
    def _database_directory_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDatabaseDirectory,
                        self.database_directory)

    time_step_range = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _time_step_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepRange,
                        self.time_step_range)

    def get_road_surface_array_status(self, *args):
        """
        V.get_road_surface_array_status(int) -> int
        C++: int GetRoadSurfaceArrayStatus(int arr)
        V.get_road_surface_array_status(string) -> int
        C++: int GetRoadSurfaceArrayStatus(const char *arrName)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetRoadSurfaceArrayStatus, *args)
        return ret

    def set_road_surface_array_status(self, *args):
        """
        V.set_road_surface_array_status(int, int)
        C++: virtual void SetRoadSurfaceArrayStatus(int arr, int status)
        V.set_road_surface_array_status(string, int)
        C++: virtual void SetRoadSurfaceArrayStatus(const char *arrName,
            int status)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.SetRoadSurfaceArrayStatus, *args)
        return ret

    def get_thick_shell_array_status(self, *args):
        """
        V.get_thick_shell_array_status(int) -> int
        C++: int GetThickShellArrayStatus(int arr)
        V.get_thick_shell_array_status(string) -> int
        C++: int GetThickShellArrayStatus(const char *arrName)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetThickShellArrayStatus, *args)
        return ret

    def set_thick_shell_array_status(self, *args):
        """
        V.set_thick_shell_array_status(int, int)
        C++: virtual void SetThickShellArrayStatus(int arr, int status)
        V.set_thick_shell_array_status(string, int)
        C++: virtual void SetThickShellArrayStatus(const char *arrName,
            int status)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.SetThickShellArrayStatus, *args)
        return ret

    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Retrieve information about the time extents of the LS-Dyna
        database. Do not call these functions before setting the database
        directory and calling update_information().
        """
    )
    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

    def get_solid_array_status(self, *args):
        """
        V.get_solid_array_status(int) -> int
        C++: int GetSolidArrayStatus(int arr)
        V.get_solid_array_status(string) -> int
        C++: int GetSolidArrayStatus(const char *arrName)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetSolidArrayStatus, *args)
        return ret

    def set_solid_array_status(self, *args):
        """
        V.set_solid_array_status(int, int)
        C++: virtual void SetSolidArrayStatus(int arr, int status)
        V.set_solid_array_status(string, int)
        C++: virtual void SetSolidArrayStatus(const char *arrName,
            int status)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.SetSolidArrayStatus, *args)
        return ret

    def get_shell_array_status(self, *args):
        """
        V.get_shell_array_status(int) -> int
        C++: int GetShellArrayStatus(int arr)
        V.get_shell_array_status(string) -> int
        C++: int GetShellArrayStatus(const char *arrName)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetShellArrayStatus, *args)
        return ret

    def set_shell_array_status(self, *args):
        """
        V.set_shell_array_status(int, int)
        C++: virtual void SetShellArrayStatus(int arr, int status)
        V.set_shell_array_status(string, int)
        C++: virtual void SetShellArrayStatus(const char *arrName,
            int status)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.SetShellArrayStatus, *args)
        return ret

    def get_beam_array_status(self, *args):
        """
        V.get_beam_array_status(int) -> int
        C++: int GetBeamArrayStatus(int arr)
        V.get_beam_array_status(string) -> int
        C++: int GetBeamArrayStatus(const char *arrName)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetBeamArrayStatus, *args)
        return ret

    def set_beam_array_status(self, *args):
        """
        V.set_beam_array_status(int, int)
        C++: virtual void SetBeamArrayStatus(int arr, int status)
        V.set_beam_array_status(string, int)
        C++: virtual void SetBeamArrayStatus(const char *arrName,
            int status)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.SetBeamArrayStatus, *args)
        return ret

    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(int, int) -> int
        C++: int GetCellArrayStatus(int cellType, int arr)
        V.get_cell_array_status(int, string) -> int
        C++: int GetCellArrayStatus(int cellType, const char *arrName)
        Routines that allow the status of a cell variable to be adjusted
        or queried independent of the output mesh.  The cell_type
        parameter should be one of: LS_POINT, LS_BEAM, LS_SHELL,
        LS_THICK_SHELL, LS_SOLID, LS_RIGID_BODY, or LS_ROAD_SURFACE
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(int, int, int)
        C++: virtual void SetCellArrayStatus(int cellType, int arr,
            int status)
        V.set_cell_array_status(int, string, int)
        C++: virtual void SetCellArrayStatus(int cellType,
            const char *arrName, int status)
        Routines that allow the status of a cell variable to be adjusted
        or queried independent of the output mesh.  The cell_type
        parameter should be one of: LS_POINT, LS_BEAM, LS_SHELL,
        LS_THICK_SHELL, LS_SOLID, LS_RIGID_BODY, or LS_ROAD_SURFACE
        """
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get/Set the filename. The set/_get_file_name() routines are actually
        wrappers around the set/_get_database_directory() members; the
        actual filename you choose is irrelevant -- only the directory
        name is used. This is done in order to accommodate para_view.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def get_rigid_body_array_status(self, *args):
        """
        V.get_rigid_body_array_status(int) -> int
        C++: int GetRigidBodyArrayStatus(int arr)
        V.get_rigid_body_array_status(string) -> int
        C++: int GetRigidBodyArrayStatus(const char *arrName)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetRigidBodyArrayStatus, *args)
        return ret

    def set_rigid_body_array_status(self, *args):
        """
        V.set_rigid_body_array_status(int, int)
        C++: virtual void SetRigidBodyArrayStatus(int arr, int status)
        V.set_rigid_body_array_status(string, int)
        C++: virtual void SetRigidBodyArrayStatus(const char *arrName,
            int status)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.SetRigidBodyArrayStatus, *args)
        return ret

    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(int) -> int
        C++: int GetPointArrayStatus(int arr)
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *arrName)
        These methods allow you to load only selected subsets of the
        nodal variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(int, int)
        C++: virtual void SetPointArrayStatus(int arr, int status)
        V.set_point_array_status(string, int)
        C++: virtual void SetPointArrayStatus(const char *arrName,
            int status)
        These methods allow you to load only selected subsets of the
        nodal variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    input_deck = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the input deck corresponding to the current database.
        This is used to determine the part names associated with each
        material ID. This file may be in two formats: a valid LSDyna
        input deck or a short XML summary. If the file begins with
        "<?xml" then the summary format is used. Otherwise, the keyword
        format is used and a summary file will be created if write
        permissions exist in the directory containing the keyword file.
        The newly created summary will have ".k" or ".key" stripped from
        the end of the keyword filename and ".lsdyna" appended.
        """
    )
    def _input_deck_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputDeck,
                        self.input_deck)

    def get_part_array_status(self, *args):
        """
        V.get_part_array_status(int) -> int
        C++: int GetPartArrayStatus(int arr)
        V.get_part_array_status(string) -> int
        C++: int GetPartArrayStatus(const char *partName)
        These methods allow you to load only selected parts of the input.
        If input_deck points to a valid keyword file (or summary), then
        part names will be taken from that file. Otherwise, when
        arbitrary material numbering is used, parts will be named "_part_xxx
        (_matl_yyy)" where XXX is an increasing sequential number and YYY
        is the respective material ID. If no input deck is specified and
        arbitrary arbitrary material numbering is not used, parts will be
        named "_part_xxx" where XXX is a sequential material ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetPartArrayStatus, *args)
        return ret

    def set_part_array_status(self, *args):
        """
        V.set_part_array_status(int, int)
        C++: virtual void SetPartArrayStatus(int arr, int status)
        V.set_part_array_status(string, int)
        C++: virtual void SetPartArrayStatus(const char *partName,
            int status)
        These methods allow you to load only selected parts of the input.
        If input_deck points to a valid keyword file (or summary), then
        part names will be taken from that file. Otherwise, when
        arbitrary material numbering is used, parts will be named "_part_xxx
        (_matl_yyy)" where XXX is an increasing sequential number and YYY
        is the respective material ID. If no input deck is specified and
        arbitrary arbitrary material numbering is not used, parts will be
        named "_part_xxx" where XXX is a sequential material ID.
        """
        ret = self._wrap_call(self._vtk_obj.SetPartArrayStatus, *args)
        return ret

    def get_particle_array_status(self, *args):
        """
        V.get_particle_array_status(int) -> int
        C++: int GetParticleArrayStatus(int arr)
        V.get_particle_array_status(string) -> int
        C++: int GetParticleArrayStatus(const char *arrName)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetParticleArrayStatus, *args)
        return ret

    def set_particle_array_status(self, *args):
        """
        V.set_particle_array_status(int, int)
        C++: virtual void SetParticleArrayStatus(int arr, int status)
        V.set_particle_array_status(string, int)
        C++: virtual void SetParticleArrayStatus(const char *arrName,
            int status)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.SetParticleArrayStatus, *args)
        return ret

    def get_beam_array_name(self, *args):
        """
        V.get_beam_array_name(int) -> string
        C++: const char *GetBeamArrayName(int)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetBeamArrayName, *args)
        return ret

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int, int) -> string
        C++: const char *GetCellArrayName(int cellType, int arr)
        Routines that allow the status of a cell variable to be adjusted
        or queried independent of the output mesh.  The cell_type
        parameter should be one of: LS_POINT, LS_BEAM, LS_SHELL,
        LS_THICK_SHELL, LS_SOLID, LS_RIGID_BODY, or LS_ROAD_SURFACE
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def _get_dimensionality(self):
        return self._vtk_obj.GetDimensionality()
    dimensionality = traits.Property(_get_dimensionality, help=\
        """
        Retrieve the dimension of points in the database. This should
        return 2 or 3.  Do not call this function before setting the
        database directory and calling update_information().
        """
    )

    def _get_number_of_beam_arrays(self):
        return self._vtk_obj.GetNumberOfBeamArrays()
    number_of_beam_arrays = traits.Property(_get_number_of_beam_arrays, help=\
        """
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
    )

    def _get_number_of_beam_cells(self):
        return self._vtk_obj.GetNumberOfBeamCells()
    number_of_beam_cells = traits.Property(_get_number_of_beam_cells, help=\
        """
        Retrieve the number of cells of a given type in the database. Do
        not call this function before setting the database directory and
        calling update_information().
        """
    )

    def get_number_of_cell_arrays(self, *args):
        """
        V.get_number_of_cell_arrays(int) -> int
        C++: int GetNumberOfCellArrays(int cellType)
        Routines that allow the status of a cell variable to be adjusted
        or queried independent of the output mesh.  The cell_type
        parameter should be one of: LS_POINT, LS_BEAM, LS_SHELL,
        LS_THICK_SHELL, LS_SOLID, LS_RIGID_BODY, or LS_ROAD_SURFACE
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfCellArrays, *args)
        return ret

    def _get_number_of_cells(self):
        return self._vtk_obj.GetNumberOfCells()
    number_of_cells = traits.Property(_get_number_of_cells, help=\
        """
        Retrieve the number of cells of a given type in the database.  Do
        not call this function before setting the database directory and
        calling update_information().
        
        Note that get_number_of_cells() returns the sum of
        get_number_of_continuum_cells() and get_number_of_particle_cells().
        """
    )

    def get_number_of_components_in_beam_array(self, *args):
        """
        V.get_number_of_components_in_beam_array(int) -> int
        C++: int GetNumberOfComponentsInBeamArray(int a)
        V.get_number_of_components_in_beam_array(string) -> int
        C++: int GetNumberOfComponentsInBeamArray(const char *arrName)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfComponentsInBeamArray, *args)
        return ret

    def get_number_of_components_in_cell_array(self, *args):
        """
        V.get_number_of_components_in_cell_array(int, int) -> int
        C++: int GetNumberOfComponentsInCellArray(int cellType, int arr)
        V.get_number_of_components_in_cell_array(int, string) -> int
        C++: int GetNumberOfComponentsInCellArray(int cellType,
            const char *arrName)
        Routines that allow the status of a cell variable to be adjusted
        or queried independent of the output mesh.  The cell_type
        parameter should be one of: LS_POINT, LS_BEAM, LS_SHELL,
        LS_THICK_SHELL, LS_SOLID, LS_RIGID_BODY, or LS_ROAD_SURFACE
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfComponentsInCellArray, *args)
        return ret

    def get_number_of_components_in_particle_array(self, *args):
        """
        V.get_number_of_components_in_particle_array(int) -> int
        C++: int GetNumberOfComponentsInParticleArray(int a)
        V.get_number_of_components_in_particle_array(string) -> int
        C++: int GetNumberOfComponentsInParticleArray(const char *arrName)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfComponentsInParticleArray, *args)
        return ret

    def get_number_of_components_in_point_array(self, *args):
        """
        V.get_number_of_components_in_point_array(int) -> int
        C++: int GetNumberOfComponentsInPointArray(int arr)
        V.get_number_of_components_in_point_array(string) -> int
        C++: int GetNumberOfComponentsInPointArray(const char *arrName)
        These methods allow you to load only selected subsets of the
        nodal variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfComponentsInPointArray, *args)
        return ret

    def get_number_of_components_in_rigid_body_array(self, *args):
        """
        V.get_number_of_components_in_rigid_body_array(int) -> int
        C++: int GetNumberOfComponentsInRigidBodyArray(int a)
        V.get_number_of_components_in_rigid_body_array(string) -> int
        C++: int GetNumberOfComponentsInRigidBodyArray(
            const char *arrName)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfComponentsInRigidBodyArray, *args)
        return ret

    def get_number_of_components_in_road_surface_array(self, *args):
        """
        V.get_number_of_components_in_road_surface_array(int) -> int
        C++: int GetNumberOfComponentsInRoadSurfaceArray(int a)
        V.get_number_of_components_in_road_surface_array(string) -> int
        C++: int GetNumberOfComponentsInRoadSurfaceArray(
            const char *arrName)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfComponentsInRoadSurfaceArray, *args)
        return ret

    def get_number_of_components_in_shell_array(self, *args):
        """
        V.get_number_of_components_in_shell_array(int) -> int
        C++: int GetNumberOfComponentsInShellArray(int a)
        V.get_number_of_components_in_shell_array(string) -> int
        C++: int GetNumberOfComponentsInShellArray(const char *arrName)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfComponentsInShellArray, *args)
        return ret

    def get_number_of_components_in_solid_array(self, *args):
        """
        V.get_number_of_components_in_solid_array(int) -> int
        C++: int GetNumberOfComponentsInSolidArray(int a)
        V.get_number_of_components_in_solid_array(string) -> int
        C++: int GetNumberOfComponentsInSolidArray(const char *arrName)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfComponentsInSolidArray, *args)
        return ret

    def get_number_of_components_in_thick_shell_array(self, *args):
        """
        V.get_number_of_components_in_thick_shell_array(int) -> int
        C++: int GetNumberOfComponentsInThickShellArray(int a)
        V.get_number_of_components_in_thick_shell_array(string) -> int
        C++: int GetNumberOfComponentsInThickShellArray(
            const char *arrName)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfComponentsInThickShellArray, *args)
        return ret

    def _get_number_of_continuum_cells(self):
        return self._vtk_obj.GetNumberOfContinuumCells()
    number_of_continuum_cells = traits.Property(_get_number_of_continuum_cells, help=\
        """
        Retrieve the number of cells of a given type in the database.  Do
        not call this function before setting the database directory and
        calling update_information().
        
        Note that get_number_of_continuum_cells() returns the sum of
        get_number_of_solid_cells(), get_number_of_thick_shell_cells(),
        get_number_of_shell_cells(), get_number_of_rigid_body_cells(),
        get_number_of_road_surface_cells(), and get_number_of_beam_cells().
        """
    )

    def _get_number_of_nodes(self):
        return self._vtk_obj.GetNumberOfNodes()
    number_of_nodes = traits.Property(_get_number_of_nodes, help=\
        """
        Retrieve the number of points in the database.  Do not call this
        function before setting the database directory and calling
        update_information().
        """
    )

    def _get_number_of_part_arrays(self):
        return self._vtk_obj.GetNumberOfPartArrays()
    number_of_part_arrays = traits.Property(_get_number_of_part_arrays, help=\
        """
        These methods allow you to load only selected parts of the input.
        If input_deck points to a valid keyword file (or summary), then
        part names will be taken from that file. Otherwise, when
        arbitrary material numbering is used, parts will be named "_part_xxx
        (_matl_yyy)" where XXX is an increasing sequential number and YYY
        is the respective material ID. If no input deck is specified and
        arbitrary arbitrary material numbering is not used, parts will be
        named "_part_xxx" where XXX is a sequential material ID.
        """
    )

    def _get_number_of_particle_arrays(self):
        return self._vtk_obj.GetNumberOfParticleArrays()
    number_of_particle_arrays = traits.Property(_get_number_of_particle_arrays, help=\
        """
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
    )

    def _get_number_of_particle_cells(self):
        return self._vtk_obj.GetNumberOfParticleCells()
    number_of_particle_cells = traits.Property(_get_number_of_particle_cells, help=\
        """
        Retrieve the number of cells of a given type in the database.  Do
        not call this function before setting the database directory and
        calling update_information().
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        These methods allow you to load only selected subsets of the
        nodal variables defined over the mesh.
        """
    )

    def _get_number_of_rigid_body_arrays(self):
        return self._vtk_obj.GetNumberOfRigidBodyArrays()
    number_of_rigid_body_arrays = traits.Property(_get_number_of_rigid_body_arrays, help=\
        """
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
    )

    def _get_number_of_rigid_body_cells(self):
        return self._vtk_obj.GetNumberOfRigidBodyCells()
    number_of_rigid_body_cells = traits.Property(_get_number_of_rigid_body_cells, help=\
        """
        Retrieve the number of cells of a given type in the database.  Do
        not call this function before setting the database directory and
        calling update_information().
        """
    )

    def _get_number_of_road_surface_arrays(self):
        return self._vtk_obj.GetNumberOfRoadSurfaceArrays()
    number_of_road_surface_arrays = traits.Property(_get_number_of_road_surface_arrays, help=\
        """
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
    )

    def _get_number_of_road_surface_cells(self):
        return self._vtk_obj.GetNumberOfRoadSurfaceCells()
    number_of_road_surface_cells = traits.Property(_get_number_of_road_surface_cells, help=\
        """
        Retrieve the number of cells of a given type in the database.  Do
        not call this function before setting the database directory and
        calling update_information().
        """
    )

    def _get_number_of_shell_arrays(self):
        return self._vtk_obj.GetNumberOfShellArrays()
    number_of_shell_arrays = traits.Property(_get_number_of_shell_arrays, help=\
        """
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
    )

    def _get_number_of_shell_cells(self):
        return self._vtk_obj.GetNumberOfShellCells()
    number_of_shell_cells = traits.Property(_get_number_of_shell_cells, help=\
        """
        Retrieve the number of cells of a given type in the database.  Do
        not call this function before setting the database directory and
        calling update_information().
        """
    )

    def _get_number_of_solid_arrays(self):
        return self._vtk_obj.GetNumberOfSolidArrays()
    number_of_solid_arrays = traits.Property(_get_number_of_solid_arrays, help=\
        """
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
    )

    def _get_number_of_solid_cells(self):
        return self._vtk_obj.GetNumberOfSolidCells()
    number_of_solid_cells = traits.Property(_get_number_of_solid_cells, help=\
        """
        Retrieve the number of cells of a given type in the database.  Do
        not call this function before setting the database directory and
        calling update_information().
        """
    )

    def _get_number_of_thick_shell_arrays(self):
        return self._vtk_obj.GetNumberOfThickShellArrays()
    number_of_thick_shell_arrays = traits.Property(_get_number_of_thick_shell_arrays, help=\
        """
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
    )

    def _get_number_of_thick_shell_cells(self):
        return self._vtk_obj.GetNumberOfThickShellCells()
    number_of_thick_shell_cells = traits.Property(_get_number_of_thick_shell_cells, help=\
        """
        Retrieve the number of cells of a given type in the database.  Do
        not call this function before setting the database directory and
        calling update_information().
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        Retrieve information about the time extents of the LS-Dyna
        database. Do not call these functions before setting the database
        directory and calling update_information().
        """
    )

    def get_part_array_name(self, *args):
        """
        V.get_part_array_name(int) -> string
        C++: const char *GetPartArrayName(int)
        These methods allow you to load only selected parts of the input.
        If input_deck points to a valid keyword file (or summary), then
        part names will be taken from that file. Otherwise, when
        arbitrary material numbering is used, parts will be named "_part_xxx
        (_matl_yyy)" where XXX is an increasing sequential number and YYY
        is the respective material ID. If no input deck is specified and
        arbitrary arbitrary material numbering is not used, parts will be
        named "_part_xxx" where XXX is a sequential material ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetPartArrayName, *args)
        return ret

    def get_particle_array_name(self, *args):
        """
        V.get_particle_array_name(int) -> string
        C++: const char *GetParticleArrayName(int)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetParticleArrayName, *args)
        return ret

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int)
        These methods allow you to load only selected subsets of the
        nodal variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
        return ret

    def get_rigid_body_array_name(self, *args):
        """
        V.get_rigid_body_array_name(int) -> string
        C++: const char *GetRigidBodyArrayName(int)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetRigidBodyArrayName, *args)
        return ret

    def get_road_surface_array_name(self, *args):
        """
        V.get_road_surface_array_name(int) -> string
        C++: const char *GetRoadSurfaceArrayName(int)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetRoadSurfaceArrayName, *args)
        return ret

    def get_shell_array_name(self, *args):
        """
        V.get_shell_array_name(int) -> string
        C++: const char *GetShellArrayName(int)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetShellArrayName, *args)
        return ret

    def get_solid_array_name(self, *args):
        """
        V.get_solid_array_name(int) -> string
        C++: const char *GetSolidArrayName(int)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetSolidArrayName, *args)
        return ret

    def get_thick_shell_array_name(self, *args):
        """
        V.get_thick_shell_array_name(int) -> string
        C++: const char *GetThickShellArrayName(int)
        These methods allow you to load only selected subsets of the cell
        variables defined over the mesh.
        """
        ret = self._wrap_call(self._vtk_obj.GetThickShellArrayName, *args)
        return ret

    def get_time_value(self, *args):
        """
        V.get_time_value(int) -> float
        C++: double GetTimeValue(IdType)
        Retrieve information about the time extents of the LS-Dyna
        database. Do not call these functions before setting the database
        directory and calling update_information().
        """
        ret = self._wrap_call(self._vtk_obj.GetTimeValue, *args)
        return ret

    def _get_title(self):
        return self._vtk_obj.GetTitle()
    title = traits.Property(_get_title, help=\
        """
        The title of the database is a 40 or 80 character text
        description stored at the front of a d3plot file.  Do not call
        this function before setting the database directory and calling
        update_information().
        """
    )

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: int CanReadFile(const char *fname)
        Determine if the file can be readed with this reader.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def debug_dump(self):
        """
        V.debug_dump()
        C++: void DebugDump()
        A routine to call Dump() from within a lame debugger that won't
        properly pass a C++ iostream object like cout.
        """
        ret = self._vtk_obj.DebugDump()
        return ret
        

    def is_database_valid(self):
        """
        V.is_database_valid() -> int
        C++: int IsDatabaseValid()
        Get/Set the directory containing the LS-Dyna database and
        determine whether it is valid.
        """
        ret = self._vtk_obj.IsDatabaseValid()
        return ret
        

    _updateable_traits_ = \
    (('deformed_mesh', 'GetDeformedMesh'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('release_data_flag',
    'GetReleaseDataFlag'), ('split_by_material_id',
    'GetSplitByMaterialId'), ('file_name', 'GetFileName'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('time_step_range', 'GetTimeStepRange'), ('abort_execute',
    'GetAbortExecute'), ('remove_deleted_cells', 'GetRemoveDeletedCells'),
    ('input_deck', 'GetInputDeck'), ('time_step', 'GetTimeStep'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('database_directory', 'GetDatabaseDirectory'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'deformed_mesh', 'global_warning_display',
    'release_data_flag', 'remove_deleted_cells', 'split_by_material_id',
    'database_directory', 'file_name', 'input_deck', 'progress_text',
    'time_step', 'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LSDynaReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LSDynaReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['deformed_mesh', 'remove_deleted_cells',
            'split_by_material_id'], [], ['database_directory', 'file_name',
            'input_deck', 'time_step', 'time_step_range']),
            title='Edit LSDynaReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LSDynaReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

