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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class ExodusReader(UnstructuredGridAlgorithm):
    """
    ExodusReader - Read exodus 2 files .ex2
    
    Superclass: UnstructuredGridAlgorithm
    
    ExodusReader is a unstructured grid source object that reads
    exodus_ii files.  Most of the meta data associated with the file is
    loaded when update_information is called.  This includes information
    like Title, number of blocks, number and names of arrays. This data
    can be retrieved from methods in this reader. Separate arrays that
    are meant to be a single vector, are combined internally for
    convenience.  To be combined, the array names have to be identical
    except for a trailing X,Y and Z (or x,y,z).  By default cell and
    point arrays are not loaded.  However, the user can flag arrays to
    load with the methods "_set_point_array_status" and "_set_cell_array_status".
     The reader DOES NOT respond to piece requests
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExodusReader, obj, update, **traits)
    
    generate_block_id_cell_array = tvtk_base.true_bool_trait(help=\
        """
        Extra cell data array that can be generated.  By default, this
        array is ON.  The value of the array is the integer id found in
        the exodus file. The name of the array is returned by
        get_block_id_array_name()
        """
    )
    def _generate_block_id_cell_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateBlockIdCellArray,
                        self.generate_block_id_cell_array_)

    generate_global_node_id_array = tvtk_base.true_bool_trait(help=\
        """
        Extra point data array that can be generated.  By default, this
        array is ON.  The value of the array is the integer id of the
        node. The id is relative to the entire data set. The name of the
        array is returned by global_node_id_array_name().
        """
    )
    def _generate_global_node_id_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateGlobalNodeIdArray,
                        self.generate_global_node_id_array_)

    pack_exodus_model_onto_output = tvtk_base.true_bool_trait(help=\
        """
        By default, the exodus_model metadata (if requested with
         exodus_model_metadata_on()) is also encoded into field arrays
         and attached to the output unstructured grid.  Set this OFF
         if you don't want this to happen.  (The ExodusIIWriter and
         the EnSightWriter can unpack this metadata from the field
         arrays and use it when writing out Exodus or en_sight files.)
        """
    )
    def _pack_exodus_model_onto_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPackExodusModelOntoOutput,
                        self.pack_exodus_model_onto_output_)

    apply_displacements = tvtk_base.true_bool_trait(help=\
        """
        Geometric locations can include displacements.  By default, this
        is ON.  The nodal positions are 'displaced' by the standard
        exodus displacment vector. If displacements are turned 'off', the
        user can explicitly add them by applying a warp filter.
        """
    )
    def _apply_displacements_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetApplyDisplacements,
                        self.apply_displacements_)

    generate_global_element_id_array = tvtk_base.true_bool_trait(help=\
        """
        Extra cell data array that can be generated.  By default, this
        array is off.  The value of the array is the integer global id of
        the cell. The name of the array is returned by
        get_global_element_id_array_name()
        """
    )
    def _generate_global_element_id_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateGlobalElementIdArray,
                        self.generate_global_element_id_array_)

    exodus_model_metadata = tvtk_base.false_bool_trait(help=\
        """
        There is a great deal of model information lost when an Exodus II
          file is read in to a UnstructuredGrid.  Turn this option ON
          if you want this metadata to be read in to a ExodusModel
        object.
          The default is OFF.
        """
    )
    def _exodus_model_metadata_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExodusModelMetadata,
                        self.exodus_model_metadata_)

    has_mode_shapes = tvtk_base.false_bool_trait(help=\
        """
        Some simulations overload the Exodus time steps to represent mode
        shapes. In this case, it does not make sense to iterate over the "time
        steps", because they are not meant to be played in order. 
        Rather, each represents the vibration at a different "mode." 
        Setting this to 1 changes the semantics of the reader to not
        report the time steps to downstream filters. By default, this is
        off, which is the case for most Exodus files.
        """
    )
    def _has_mode_shapes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHasModeShapes,
                        self.has_mode_shapes_)

    displacement_magnitude = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Geometric locations can include displacements.  By default, this
        is ON.  The nodal positions are 'displaced' by the standard
        exodus displacment vector. If displacements are turned 'off', the
        user can explicitly add them by applying a warp filter.
        """
    )
    def _displacement_magnitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementMagnitude,
                        self.displacement_magnitude)

    xml_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of the xml file.
        """
    )
    def _xml_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXMLFileName,
                        self.xml_file_name)

    def get_side_set_array_status(self, *args):
        """
        V.get_side_set_array_status(int) -> int
        C++: int GetSideSetArrayStatus(int index)
        V.get_side_set_array_status(string) -> int
        C++: int GetSideSetArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetSideSetArrayStatus, *args)
        return ret

    def set_side_set_array_status(self, *args):
        """
        V.set_side_set_array_status(int, int)
        C++: void SetSideSetArrayStatus(int index, int flag)
        V.set_side_set_array_status(string, int)
        C++: void SetSideSetArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetSideSetArrayStatus, *args)
        return ret

    def get_material_array_status(self, *args):
        """
        V.get_material_array_status(int) -> int
        C++: int GetMaterialArrayStatus(int index)
        V.get_material_array_status(string) -> int
        C++: int GetMaterialArrayStatus(const char *)"""
        ret = self._wrap_call(self._vtk_obj.GetMaterialArrayStatus, *args)
        return ret

    def set_material_array_status(self, *args):
        """
        V.set_material_array_status(int, int)
        C++: void SetMaterialArrayStatus(int index, int flag)
        V.set_material_array_status(string, int)
        C++: void SetMaterialArrayStatus(const char *, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetMaterialArrayStatus, *args)
        return ret

    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Which time_step to read.
        """
    )
    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

    def get_assembly_array_status(self, *args):
        """
        V.get_assembly_array_status(int) -> int
        C++: int GetAssemblyArrayStatus(int index)
        V.get_assembly_array_status(string) -> int
        C++: int GetAssemblyArrayStatus(const char *)"""
        ret = self._wrap_call(self._vtk_obj.GetAssemblyArrayStatus, *args)
        return ret

    def set_assembly_array_status(self, *args):
        """
        V.set_assembly_array_status(int, int)
        C++: void SetAssemblyArrayStatus(int index, int flag)
        V.set_assembly_array_status(string, int)
        C++: void SetAssemblyArrayStatus(const char *, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetAssemblyArrayStatus, *args)
        return ret

    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(int) -> int
        C++: int GetCellArrayStatus(int index)
        V.get_cell_array_status(string) -> int
        C++: int GetCellArrayStatus(const char *)"""
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(int, int)
        C++: void SetCellArrayStatus(int index, int flag)
        V.set_cell_array_status(string, int)
        C++: void SetCellArrayStatus(const char *, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of the Exodus file.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    display_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _display_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayType,
                        self.display_type)

    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(int) -> int
        C++: int GetPointArrayStatus(int index)
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *)"""
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(int, int)
        C++: void SetPointArrayStatus(int index, int flag)
        V.set_point_array_status(string, int)
        C++: void SetPointArrayStatus(const char *, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    def get_array_status(self, *args):
        """
        V.get_array_status(string, string) -> int
        C++: int GetArrayStatus(const char *type, const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetArrayStatus, *args)
        return ret

    def set_array_status(self, *args):
        """
        V.set_array_status(string, string, int)
        C++: void SetArrayStatus(const char *type, const char *name,
            int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetArrayStatus, *args)
        return ret

    def get_part_array_status(self, *args):
        """
        V.get_part_array_status(int) -> int
        C++: int GetPartArrayStatus(int index)
        V.get_part_array_status(string) -> int
        C++: int GetPartArrayStatus(const char *)"""
        ret = self._wrap_call(self._vtk_obj.GetPartArrayStatus, *args)
        return ret

    def set_part_array_status(self, *args):
        """
        V.set_part_array_status(int, int)
        C++: void SetPartArrayStatus(int index, int flag)
        V.set_part_array_status(string, int)
        C++: void SetPartArrayStatus(const char *, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetPartArrayStatus, *args)
        return ret

    def get_node_set_array_status(self, *args):
        """
        V.get_node_set_array_status(int) -> int
        C++: int GetNodeSetArrayStatus(int index)
        V.get_node_set_array_status(string) -> int
        C++: int GetNodeSetArrayStatus(const char *name)
        By default Node/Side sets are not loaded, These methods allow the
        user to select which Node/Side sets they want to load.
        number_of_node_sets and number_of_side_sets (set by vtk macros) are
        stored in ExodusReader but other Node/Side set metadata are
        stored in ExodusMetaData Note: get_number_of_node_set_arrays and
        get_number_of_side_set_arrays are just syntatic sugar for paraview
        server xml
        """
        ret = self._wrap_call(self._vtk_obj.GetNodeSetArrayStatus, *args)
        return ret

    def set_node_set_array_status(self, *args):
        """
        V.set_node_set_array_status(int, int)
        C++: void SetNodeSetArrayStatus(int index, int flag)
        V.set_node_set_array_status(string, int)
        C++: void SetNodeSetArrayStatus(const char *name, int flag)
        By default Node/Side sets are not loaded, These methods allow the
        user to select which Node/Side sets they want to load.
        number_of_node_sets and number_of_side_sets (set by vtk macros) are
        stored in ExodusReader but other Node/Side set metadata are
        stored in ExodusMetaData Note: get_number_of_node_set_arrays and
        get_number_of_side_set_arrays are just syntatic sugar for paraview
        server xml
        """
        ret = self._wrap_call(self._vtk_obj.SetNodeSetArrayStatus, *args)
        return ret

    def get_block_array_status(self, *args):
        """
        V.get_block_array_status(int) -> int
        C++: int GetBlockArrayStatus(int index)
        V.get_block_array_status(string) -> int
        C++: int GetBlockArrayStatus(const char *)"""
        ret = self._wrap_call(self._vtk_obj.GetBlockArrayStatus, *args)
        return ret

    def set_block_array_status(self, *args):
        """
        V.set_block_array_status(int, int)
        C++: void SetBlockArrayStatus(int index, int flag)
        V.set_block_array_status(string, int)
        C++: void SetBlockArrayStatus(const char *, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetBlockArrayStatus, *args)
        return ret

    def get_hierarchy_array_status(self, *args):
        """
        V.get_hierarchy_array_status(int) -> int
        C++: int GetHierarchyArrayStatus(int index)
        V.get_hierarchy_array_status(string) -> int
        C++: int GetHierarchyArrayStatus(const char *)"""
        ret = self._wrap_call(self._vtk_obj.GetHierarchyArrayStatus, *args)
        return ret

    def set_hierarchy_array_status(self, *args):
        """
        V.set_hierarchy_array_status(int, int)
        C++: void SetHierarchyArrayStatus(int index, int flag)
        V.set_hierarchy_array_status(string, int)
        C++: void SetHierarchyArrayStatus(const char *, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetHierarchyArrayStatus, *args)
        return ret

    time_step_range = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _time_step_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepRange,
                        self.time_step_range)

    def get_assembly_array_id(self, *args):
        """
        V.get_assembly_array_id(string) -> int
        C++: int GetAssemblyArrayID(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetAssemblyArrayID, *args)
        return ret

    def get_assembly_array_name(self, *args):
        """
        V.get_assembly_array_name(int) -> string
        C++: const char *GetAssemblyArrayName(int arrayIdx)"""
        ret = self._wrap_call(self._vtk_obj.GetAssemblyArrayName, *args)
        return ret

    def get_block_array_id(self, *args):
        """
        V.get_block_array_id(string) -> int
        C++: int GetBlockArrayID(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetBlockArrayID, *args)
        return ret

    def get_block_array_name(self, *args):
        """
        V.get_block_array_name(int) -> string
        C++: const char *GetBlockArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetBlockArrayName, *args)
        return ret

    def get_block_id(self, *args):
        """
        V.get_block_id(int) -> int
        C++: int GetBlockId(int block_idx)
        Access to meta data generated by update_information.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockId, *args)
        return ret

    def _get_block_id_array_name(self):
        return self._vtk_obj.GetBlockIdArrayName()
    block_id_array_name = traits.Property(_get_block_id_array_name, help=\
        """
        Extra cell data array that can be generated.  By default, this
        array is ON.  The value of the array is the integer id found in
        the exodus file. The name of the array is returned by
        get_block_id_array_name()
        """
    )

    def get_cell_array_id(self, *args):
        """
        V.get_cell_array_id(string) -> int
        C++: int GetCellArrayID(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetCellArrayID, *args)
        return ret

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int) -> string
        C++: const char *GetCellArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def get_cell_array_number_of_components(self, *args):
        """
        V.get_cell_array_number_of_components(int) -> int
        C++: int GetCellArrayNumberOfComponents(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetCellArrayNumberOfComponents, *args)
        return ret

    def get_dsp_output_arrays(self, *args):
        """
        V.get_dsp_output_arrays(int, UnstructuredGrid)
        C++: void GetDSPOutputArrays(int exoid,
            UnstructuredGrid *output)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDSPOutputArrays, *my_args)
        return ret

    def _get_dimensionality(self):
        return self._vtk_obj.GetDimensionality()
    dimensionality = traits.Property(_get_dimensionality, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def _get_exodus_model(self):
        return wrap_vtk(self._vtk_obj.GetExodusModel())
    exodus_model = traits.Property(_get_exodus_model, help=\
        """
        Returns the object which encapsulates the model metadata.
        """
    )

    def get_global_element_id(self, *args):
        """
        V.get_global_element_id(DataSet, int) -> int
        C++: static int GetGlobalElementID(DataSet *data, int localID)
        V.get_global_element_id(DataSet, int, int) -> int
        C++: static int GetGlobalElementID(DataSet *data, int localID,
            int searchType)
        Extra cell data array that can be generated.  By default, this
        array is off.  The value of the array is the integer global id of
        the cell. The name of the array is returned by
        get_global_element_id_array_name()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetGlobalElementID, *my_args)
        return ret

    def _get_global_element_id_array_name(self):
        return self._vtk_obj.GetGlobalElementIdArrayName()
    global_element_id_array_name = traits.Property(_get_global_element_id_array_name, help=\
        """
        Extra cell data array that can be generated.  By default, this
        array is off.  The value of the array is the integer global id of
        the cell. The name of the array is returned by
        get_global_element_id_array_name()
        """
    )

    def get_global_node_id(self, *args):
        """
        V.get_global_node_id(DataSet, int) -> int
        C++: static int GetGlobalNodeID(DataSet *data, int localID)
        V.get_global_node_id(DataSet, int, int) -> int
        C++: static int GetGlobalNodeID(DataSet *data, int localID,
            int searchType)
        Extra point data array that can be generated.  By default, this
        array is ON.  The value of the array is the integer id of the
        node. The id is relative to the entire data set. The name of the
        array is returned by global_node_id_array_name().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetGlobalNodeID, *my_args)
        return ret

    def _get_global_node_id_array_name(self):
        return self._vtk_obj.GetGlobalNodeIdArrayName()
    global_node_id_array_name = traits.Property(_get_global_node_id_array_name, help=\
        """
        Extra point data array that can be generated.  By default, this
        array is ON.  The value of the array is the integer id of the
        node. The id is relative to the entire data set. The name of the
        array is returned by global_node_id_array_name().
        """
    )

    def get_hierarchy_array_name(self, *args):
        """
        V.get_hierarchy_array_name(int) -> string
        C++: const char *GetHierarchyArrayName(int arrayIdx)"""
        ret = self._wrap_call(self._vtk_obj.GetHierarchyArrayName, *args)
        return ret

    def get_material_array_id(self, *args):
        """
        V.get_material_array_id(string) -> int
        C++: int GetMaterialArrayID(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetMaterialArrayID, *args)
        return ret

    def get_material_array_name(self, *args):
        """
        V.get_material_array_name(int) -> string
        C++: const char *GetMaterialArrayName(int arrayIdx)"""
        ret = self._wrap_call(self._vtk_obj.GetMaterialArrayName, *args)
        return ret

    def get_node_set_array_name(self, *args):
        """
        V.get_node_set_array_name(int) -> string
        C++: const char *GetNodeSetArrayName(int index)
        By default Node/Side sets are not loaded, These methods allow the
        user to select which Node/Side sets they want to load.
        number_of_node_sets and number_of_side_sets (set by vtk macros) are
        stored in ExodusReader but other Node/Side set metadata are
        stored in ExodusMetaData Note: get_number_of_node_set_arrays and
        get_number_of_side_set_arrays are just syntatic sugar for paraview
        server xml
        """
        ret = self._wrap_call(self._vtk_obj.GetNodeSetArrayName, *args)
        return ret

    def _get_number_of_assembly_arrays(self):
        return self._vtk_obj.GetNumberOfAssemblyArrays()
    number_of_assembly_arrays = traits.Property(_get_number_of_assembly_arrays, help=\
        """
        
        """
    )

    def _get_number_of_block_arrays(self):
        return self._vtk_obj.GetNumberOfBlockArrays()
    number_of_block_arrays = traits.Property(_get_number_of_block_arrays, help=\
        """
        
        """
    )

    def _get_number_of_blocks(self):
        return self._vtk_obj.GetNumberOfBlocks()
    number_of_blocks = traits.Property(_get_number_of_blocks, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        
        """
    )

    def _get_number_of_elements(self):
        return self._vtk_obj.GetNumberOfElements()
    number_of_elements = traits.Property(_get_number_of_elements, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def get_number_of_elements_in_block(self, *args):
        """
        V.get_number_of_elements_in_block(int) -> int
        C++: int GetNumberOfElementsInBlock(int block_idx)
        Access to meta data generated by update_information.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfElementsInBlock, *args)
        return ret

    def _get_number_of_hierarchy_arrays(self):
        return self._vtk_obj.GetNumberOfHierarchyArrays()
    number_of_hierarchy_arrays = traits.Property(_get_number_of_hierarchy_arrays, help=\
        """
        
        """
    )

    def _get_number_of_material_arrays(self):
        return self._vtk_obj.GetNumberOfMaterialArrays()
    number_of_material_arrays = traits.Property(_get_number_of_material_arrays, help=\
        """
        
        """
    )

    def _get_number_of_node_set_arrays(self):
        return self._vtk_obj.GetNumberOfNodeSetArrays()
    number_of_node_set_arrays = traits.Property(_get_number_of_node_set_arrays, help=\
        """
        By default Node/Side sets are not loaded, These methods allow the
        user to select which Node/Side sets they want to load.
        number_of_node_sets and number_of_side_sets (set by vtk macros) are
        stored in ExodusReader but other Node/Side set metadata are
        stored in ExodusMetaData Note: get_number_of_node_set_arrays and
        get_number_of_side_set_arrays are just syntatic sugar for paraview
        server xml
        """
    )

    def _get_number_of_node_sets(self):
        return self._vtk_obj.GetNumberOfNodeSets()
    number_of_node_sets = traits.Property(_get_number_of_node_sets, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def _get_number_of_nodes(self):
        return self._vtk_obj.GetNumberOfNodes()
    number_of_nodes = traits.Property(_get_number_of_nodes, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def _get_number_of_part_arrays(self):
        return self._vtk_obj.GetNumberOfPartArrays()
    number_of_part_arrays = traits.Property(_get_number_of_part_arrays, help=\
        """
        
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        
        """
    )

    def _get_number_of_side_set_arrays(self):
        return self._vtk_obj.GetNumberOfSideSetArrays()
    number_of_side_set_arrays = traits.Property(_get_number_of_side_set_arrays, help=\
        """
        
        """
    )

    def _get_number_of_side_sets(self):
        return self._vtk_obj.GetNumberOfSideSets()
    number_of_side_sets = traits.Property(_get_number_of_side_sets, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def _get_number_of_variable_arrays(self):
        return self._vtk_obj.GetNumberOfVariableArrays()
    number_of_variable_arrays = traits.Property(_get_number_of_variable_arrays, help=\
        """
        
        """
    )

    def get_part_array_id(self, *args):
        """
        V.get_part_array_id(string) -> int
        C++: int GetPartArrayID(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetPartArrayID, *args)
        return ret

    def get_part_array_name(self, *args):
        """
        V.get_part_array_name(int) -> string
        C++: const char *GetPartArrayName(int arrayIdx)"""
        ret = self._wrap_call(self._vtk_obj.GetPartArrayName, *args)
        return ret

    def get_part_block_info(self, *args):
        """
        V.get_part_block_info(int) -> string
        C++: const char *GetPartBlockInfo(int arrayIdx)"""
        ret = self._wrap_call(self._vtk_obj.GetPartBlockInfo, *args)
        return ret

    def _get_pedigree_element_id_array_name(self):
        return self._vtk_obj.GetPedigreeElementIdArrayName()
    pedigree_element_id_array_name = traits.Property(_get_pedigree_element_id_array_name, help=\
        """
        Extra cell data array that can be generated.  By default, this
        array is off.  The value of the array is the integer global id of
        the cell. The name of the array is returned by
        get_global_element_id_array_name()
        """
    )

    def _get_pedigree_node_id_array_name(self):
        return self._vtk_obj.GetPedigreeNodeIdArrayName()
    pedigree_node_id_array_name = traits.Property(_get_pedigree_node_id_array_name, help=\
        """
        Extra point data array that can be generated.  By default, this
        array is ON.  The value of the array is the integer id of the
        node. The id is relative to the entire data set. The name of the
        array is returned by global_node_id_array_name().
        """
    )

    def get_point_array_id(self, *args):
        """
        V.get_point_array_id(string) -> int
        C++: int GetPointArrayID(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetPointArrayID, *args)
        return ret

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
        return ret

    def get_point_array_number_of_components(self, *args):
        """
        V.get_point_array_number_of_components(int) -> int
        C++: int GetPointArrayNumberOfComponents(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetPointArrayNumberOfComponents, *args)
        return ret

    def get_side_set_array_name(self, *args):
        """
        V.get_side_set_array_name(int) -> string
        C++: const char *GetSideSetArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetSideSetArrayName, *args)
        return ret

    def get_time_series_data(self, *args):
        """
        V.get_time_series_data(int, string, string, FloatArray) -> int
        C++: int GetTimeSeriesData(int ID, const char *vName,
            const char *vType, FloatArray *result)"""
        my_args = deref_array(args, [('int', 'string', 'string', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.GetTimeSeriesData, *my_args)
        return ret

    def _get_title(self):
        return self._vtk_obj.GetTitle()
    title = traits.Property(_get_title, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def _get_total_number_of_elements(self):
        return self._vtk_obj.GetTotalNumberOfElements()
    total_number_of_elements = traits.Property(_get_total_number_of_elements, help=\
        """
        
        """
    )

    def _get_total_number_of_nodes(self):
        return self._vtk_obj.GetTotalNumberOfNodes()
    total_number_of_nodes = traits.Property(_get_total_number_of_nodes, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def get_variable_array_name(self, *args):
        """
        V.get_variable_array_name(int) -> string
        C++: const char *GetVariableArrayName(int a_which)"""
        ret = self._wrap_call(self._vtk_obj.GetVariableArrayName, *args)
        return ret

    def get_variable_id(self, *args):
        """
        V.get_variable_id(string, string) -> int
        C++: int GetVariableID(const char *type, const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetVariableID, *args)
        return ret

    def add_filter(self, *args):
        """
        V.add_filter(DSPFilterDefinition)
        C++: void AddFilter(DSPFilterDefinition *a_filter)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddFilter, *my_args)
        return ret

    def add_filter_denominator_weight(self, *args):
        """
        V.add_filter_denominator_weight(float)
        C++: void AddFilterDenominatorWeight(double weight)"""
        ret = self._wrap_call(self._vtk_obj.AddFilterDenominatorWeight, *args)
        return ret

    def add_filter_forward_numerator_weight(self, *args):
        """
        V.add_filter_forward_numerator_weight(float)
        C++: void AddFilterForwardNumeratorWeight(double weight)"""
        ret = self._wrap_call(self._vtk_obj.AddFilterForwardNumeratorWeight, *args)
        return ret

    def add_filter_input_var(self, *args):
        """
        V.add_filter_input_var(string)
        C++: void AddFilterInputVar(char *name)"""
        ret = self._wrap_call(self._vtk_obj.AddFilterInputVar, *args)
        return ret

    def add_filter_numerator_weight(self, *args):
        """
        V.add_filter_numerator_weight(float)
        C++: void AddFilterNumeratorWeight(double weight)"""
        ret = self._wrap_call(self._vtk_obj.AddFilterNumeratorWeight, *args)
        return ret

    def add_filter_output_var(self, *args):
        """
        V.add_filter_output_var(string)
        C++: void AddFilterOutputVar(char *name)"""
        ret = self._wrap_call(self._vtk_obj.AddFilterOutputVar, *args)
        return ret

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: int CanReadFile(const char *fname)
        Determine if the file can be readed with this reader.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def enable_dsp_filtering(self):
        """
        V.enable_dsp_filtering()
        C++: void EnableDSPFiltering()"""
        ret = self._vtk_obj.EnableDSPFiltering()
        return ret
        

    def finish_adding_filter(self):
        """
        V.finish_adding_filter()
        C++: void FinishAddingFilter()"""
        ret = self._vtk_obj.FinishAddingFilter()
        return ret
        

    def is_valid_variable(self, *args):
        """
        V.is_valid_variable(string, string) -> int
        C++: int IsValidVariable(const char *type, const char *name)"""
        ret = self._wrap_call(self._vtk_obj.IsValidVariable, *args)
        return ret

    def remove_filter(self, *args):
        """
        V.remove_filter(string)
        C++: void RemoveFilter(char *a_outputVariableName)"""
        ret = self._wrap_call(self._vtk_obj.RemoveFilter, *args)
        return ret

    def set_all_assembly_array_status(self, *args):
        """
        V.set_all_assembly_array_status(int)
        C++: void SetAllAssemblyArrayStatus(int status)"""
        ret = self._wrap_call(self._vtk_obj.SetAllAssemblyArrayStatus, *args)
        return ret

    def set_all_block_array_status(self, *args):
        """
        V.set_all_block_array_status(int)
        C++: void SetAllBlockArrayStatus(int status)"""
        ret = self._wrap_call(self._vtk_obj.SetAllBlockArrayStatus, *args)
        return ret

    def set_all_cell_array_status(self, *args):
        """
        V.set_all_cell_array_status(int)
        C++: void SetAllCellArrayStatus(int status)"""
        ret = self._wrap_call(self._vtk_obj.SetAllCellArrayStatus, *args)
        return ret

    def set_all_hierarchy_array_status(self, *args):
        """
        V.set_all_hierarchy_array_status(int)
        C++: void SetAllHierarchyArrayStatus(int status)"""
        ret = self._wrap_call(self._vtk_obj.SetAllHierarchyArrayStatus, *args)
        return ret

    def set_all_material_array_status(self, *args):
        """
        V.set_all_material_array_status(int)
        C++: void SetAllMaterialArrayStatus(int status)"""
        ret = self._wrap_call(self._vtk_obj.SetAllMaterialArrayStatus, *args)
        return ret

    def set_all_part_array_status(self, *args):
        """
        V.set_all_part_array_status(int)
        C++: void SetAllPartArrayStatus(int status)"""
        ret = self._wrap_call(self._vtk_obj.SetAllPartArrayStatus, *args)
        return ret

    def set_all_point_array_status(self, *args):
        """
        V.set_all_point_array_status(int)
        C++: void SetAllPointArrayStatus(int status)"""
        ret = self._wrap_call(self._vtk_obj.SetAllPointArrayStatus, *args)
        return ret

    def start_adding_filter(self):
        """
        V.start_adding_filter()
        C++: void StartAddingFilter()"""
        ret = self._vtk_obj.StartAddingFilter()
        return ret
        

    def str_dup_with_new(self, *args):
        """
        V.str_dup_with_new(string) -> string
        C++: static char *StrDupWithNew(const char *s)"""
        ret = self._wrap_call(self._vtk_obj.StrDupWithNew, *args)
        return ret

    def string_uppercase(self, *args):
        """
        V.string_uppercase(string, string)
        C++: static void StringUppercase(const char *str, char *upperstr)"""
        ret = self._wrap_call(self._vtk_obj.StringUppercase, *args)
        return ret

    def strings_equal(self, *args):
        """
        V.strings_equal(string, string) -> int
        C++: static int StringsEqual(const char *s1, char *s2)"""
        ret = self._wrap_call(self._vtk_obj.StringsEqual, *args)
        return ret

    _updateable_traits_ = \
    (('displacement_magnitude', 'GetDisplacementMagnitude'),
    ('has_mode_shapes', 'GetHasModeShapes'),
    ('generate_block_id_cell_array', 'GetGenerateBlockIdCellArray'),
    ('xml_file_name', 'GetXMLFileName'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('apply_displacements', 'GetApplyDisplacements'), ('progress_text',
    'GetProgressText'), ('pack_exodus_model_onto_output',
    'GetPackExodusModelOntoOutput'), ('debug', 'GetDebug'),
    ('time_step_range', 'GetTimeStepRange'),
    ('generate_global_element_id_array',
    'GetGenerateGlobalElementIdArray'), ('generate_global_node_id_array',
    'GetGenerateGlobalNodeIdArray'), ('display_type', 'GetDisplayType'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('time_step',
    'GetTimeStep'), ('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('abort_execute', 'GetAbortExecute'),
    ('exodus_model_metadata', 'GetExodusModelMetadata'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'apply_displacements', 'debug',
    'exodus_model_metadata', 'generate_block_id_cell_array',
    'generate_global_element_id_array', 'generate_global_node_id_array',
    'global_warning_display', 'has_mode_shapes',
    'pack_exodus_model_onto_output', 'release_data_flag',
    'displacement_magnitude', 'display_type', 'file_name',
    'progress_text', 'time_step', 'time_step_range', 'xml_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExodusReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExodusReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['apply_displacements', 'exodus_model_metadata',
            'generate_block_id_cell_array', 'generate_global_element_id_array',
            'generate_global_node_id_array', 'has_mode_shapes',
            'pack_exodus_model_onto_output'], [], ['displacement_magnitude',
            'display_type', 'file_name', 'time_step', 'time_step_range',
            'xml_file_name']),
            title='Edit ExodusReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExodusReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

