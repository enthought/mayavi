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


class ExodusIIReader(MultiBlockDataSetAlgorithm):
    """
    ExodusIIReader - Read exodus 2 files .ex2
    
    Superclass: MultiBlockDataSetAlgorithm
    
    ExodusIIReader is a unstructured grid source object that reads
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
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExodusIIReader, obj, update, **traits)
    
    generate_file_id_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _generate_file_id_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateFileIdArray,
                        self.generate_file_id_array_)

    generate_implicit_node_id_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _generate_implicit_node_id_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateImplicitNodeIdArray,
                        self.generate_implicit_node_id_array_)

    generate_global_node_id_array = tvtk_base.false_bool_trait(help=\
        """
        
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

    generate_object_id_cell_array = tvtk_base.true_bool_trait(help=\
        """
        Extra cell data array that can be generated.  By default, this
        array is ON.  The value of the array is the integer id found in
        the exodus file. The name of the array is returned by
        get_block_id_array_name(). For cells representing elements from an
        Exodus element block, this is set to the element block ID. For
        cells representing edges from an Exodus edge block, this is the
        edge block ID. Similarly, ths is the face block ID for cells
        representing faces from an Exodus face block. The same holds for
        cells representing entries of node, edge, face, side, and element
        sets.
        """
    )
    def _generate_object_id_cell_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateObjectIdCellArray,
                        self.generate_object_id_cell_array_)

    generate_implicit_element_id_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _generate_implicit_element_id_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateImplicitElementIdArray,
                        self.generate_implicit_element_id_array_)

    generate_global_element_id_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )
    def _generate_global_element_id_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateGlobalElementIdArray,
                        self.generate_global_element_id_array_)

    animate_mode_shapes = tvtk_base.true_bool_trait(help=\
        """
        If this flag is on (the default) and has_mode_shapes is also on,
        then this reader will report a continuous time range [0,1] and
        animate the displacements in a periodic sinusoid.  If this flag
        is off and has_mode_shapes is on, this reader ignores time.  This
        flag has no effect if has_mode_shapes is off.
        """
    )
    def _animate_mode_shapes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAnimateModeShapes,
                        self.animate_mode_shapes_)

    exodus_model_metadata = tvtk_base.false_bool_trait(help=\
        """
        There is a great deal of model information lost when an Exodus II
          file is read in to a MultiBlockDataSet.  Turn this option ON
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
        Set/Get whether the Exodus sequence number corresponds to time
        steps or mode shapes. By default, has_mode_shapes is false unless
        two time values in the Exodus file are identical, in which case
        it is true.
        """
    )
    def _has_mode_shapes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHasModeShapes,
                        self.has_mode_shapes_)

    def get_element_set_array_status(self, *args):
        """
        V.get_element_set_array_status(string) -> int
        C++: int GetElementSetArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetElementSetArrayStatus, *args)
        return ret

    def set_element_set_array_status(self, *args):
        """
        V.set_element_set_array_status(string, int)
        C++: void SetElementSetArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetElementSetArrayStatus, *args)
        return ret

    def get_node_map_array_status(self, *args):
        """
        V.get_node_map_array_status(string) -> int
        C++: int GetNodeMapArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetNodeMapArrayStatus, *args)
        return ret

    def set_node_map_array_status(self, *args):
        """
        V.set_node_map_array_status(string, int)
        C++: void SetNodeMapArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetNodeMapArrayStatus, *args)
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

    xml_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of the xml file.
        """
    )
    def _xml_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXMLFileName,
                        self.xml_file_name)

    mode_shape_time = traits.Float(-1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the time used to animate mode shapes. This is a number
        between 0 and 1 that is used to scale the displacement_magnitude
        in a sinusoidal pattern. Specifically, the displacement vector
        for each vertex is scaled by$ \mathrm{_displacement_magnitude} cos(
        2\pi \mathrm{_mode_shape_time} ) $ before it is added to the vertex
        coordinates.
        """
    )
    def _mode_shape_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModeShapeTime,
                        self.mode_shape_time)

    def get_face_set_result_array_status(self, *args):
        """
        V.get_face_set_result_array_status(string) -> int
        C++: int GetFaceSetResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceSetResultArrayStatus, *args)
        return ret

    def set_face_set_result_array_status(self, *args):
        """
        V.set_face_set_result_array_status(string, int)
        C++: void SetFaceSetResultArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetFaceSetResultArrayStatus, *args)
        return ret

    def get_face_block_array_status(self, *args):
        """
        V.get_face_block_array_status(string) -> int
        C++: int GetFaceBlockArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceBlockArrayStatus, *args)
        return ret

    def set_face_block_array_status(self, *args):
        """
        V.set_face_block_array_status(string, int)
        C++: void SetFaceBlockArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetFaceBlockArrayStatus, *args)
        return ret

    def get_object_attribute_status(self, *args):
        """
        V.get_object_attribute_status(int, int, int) -> int
        C++: int GetObjectAttributeStatus(int objectType, int objectIndex,
             int attribIndex)
        V.get_object_attribute_status(int, int, string) -> int
        C++: int GetObjectAttributeStatus(int objectType, int objectIndex,
             const char *attribName)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectAttributeStatus, *args)
        return ret

    def set_object_attribute_status(self, *args):
        """
        V.set_object_attribute_status(int, int, int, int)
        C++: void SetObjectAttributeStatus(int objectType,
            int objectIndex, int attribIndex, int status)
        V.set_object_attribute_status(int, int, string, int)
        C++: void SetObjectAttributeStatus(int objectType,
            int objectIndex, const char *attribName, int status)"""
        ret = self._wrap_call(self._vtk_obj.SetObjectAttributeStatus, *args)
        return ret

    def get_face_set_array_status(self, *args):
        """
        V.get_face_set_array_status(string) -> int
        C++: int GetFaceSetArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceSetArrayStatus, *args)
        return ret

    def set_face_set_array_status(self, *args):
        """
        V.set_face_set_array_status(string, int)
        C++: void SetFaceSetArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetFaceSetArrayStatus, *args)
        return ret

    def get_object_array_status(self, *args):
        """
        V.get_object_array_status(int, int) -> int
        C++: int GetObjectArrayStatus(int objectType, int arrayIndex)
        V.get_object_array_status(int, string) -> int
        C++: int GetObjectArrayStatus(int objectType,
            const char *arrayName)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectArrayStatus, *args)
        return ret

    def set_object_array_status(self, *args):
        """
        V.set_object_array_status(int, int, int)
        C++: void SetObjectArrayStatus(int objectType, int arrayIndex,
            int status)
        V.set_object_array_status(int, string, int)
        C++: void SetObjectArrayStatus(int objectType,
            const char *arrayName, int status)"""
        ret = self._wrap_call(self._vtk_obj.SetObjectArrayStatus, *args)
        return ret

    def get_face_map_array_status(self, *args):
        """
        V.get_face_map_array_status(string) -> int
        C++: int GetFaceMapArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceMapArrayStatus, *args)
        return ret

    def set_face_map_array_status(self, *args):
        """
        V.set_face_map_array_status(string, int)
        C++: void SetFaceMapArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetFaceMapArrayStatus, *args)
        return ret

    def get_side_set_result_array_status(self, *args):
        """
        V.get_side_set_result_array_status(string) -> int
        C++: int GetSideSetResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetSideSetResultArrayStatus, *args)
        return ret

    def set_side_set_result_array_status(self, *args):
        """
        V.set_side_set_result_array_status(string, int)
        C++: void SetSideSetResultArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetSideSetResultArrayStatus, *args)
        return ret

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

    def get_element_result_array_status(self, *args):
        """
        V.get_element_result_array_status(string) -> int
        C++: int GetElementResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetElementResultArrayStatus, *args)
        return ret

    def set_element_result_array_status(self, *args):
        """
        V.set_element_result_array_status(string, int)
        C++: void SetElementResultArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetElementResultArrayStatus, *args)
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

    def get_edge_result_array_status(self, *args):
        """
        V.get_edge_result_array_status(string) -> int
        C++: int GetEdgeResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeResultArrayStatus, *args)
        return ret

    def set_edge_result_array_status(self, *args):
        """
        V.set_edge_result_array_status(string, int)
        C++: void SetEdgeResultArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetEdgeResultArrayStatus, *args)
        return ret

    def get_edge_set_result_array_status(self, *args):
        """
        V.get_edge_set_result_array_status(string) -> int
        C++: int GetEdgeSetResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeSetResultArrayStatus, *args)
        return ret

    def set_edge_set_result_array_status(self, *args):
        """
        V.set_edge_set_result_array_status(string, int)
        C++: void SetEdgeSetResultArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetEdgeSetResultArrayStatus, *args)
        return ret

    def get_edge_set_array_status(self, *args):
        """
        V.get_edge_set_array_status(string) -> int
        C++: int GetEdgeSetArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeSetArrayStatus, *args)
        return ret

    def set_edge_set_array_status(self, *args):
        """
        V.set_edge_set_array_status(string, int)
        C++: void SetEdgeSetArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetEdgeSetArrayStatus, *args)
        return ret

    display_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _display_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayType,
                        self.display_type)

    def get_side_set_array_status(self, *args):
        """
        V.get_side_set_array_status(string) -> int
        C++: int GetSideSetArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetSideSetArrayStatus, *args)
        return ret

    def set_side_set_array_status(self, *args):
        """
        V.set_side_set_array_status(string, int)
        C++: void SetSideSetArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetSideSetArrayStatus, *args)
        return ret

    def get_node_set_array_status(self, *args):
        """
        V.get_node_set_array_status(string) -> int
        C++: int GetNodeSetArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetNodeSetArrayStatus, *args)
        return ret

    def set_node_set_array_status(self, *args):
        """
        V.set_node_set_array_status(string, int)
        C++: void SetNodeSetArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetNodeSetArrayStatus, *args)
        return ret

    def get_global_result_array_status(self, *args):
        """
        V.get_global_result_array_status(string) -> int
        C++: int GetGlobalResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetGlobalResultArrayStatus, *args)
        return ret

    def set_global_result_array_status(self, *args):
        """
        V.set_global_result_array_status(string, int)
        C++: void SetGlobalResultArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetGlobalResultArrayStatus, *args)
        return ret

    face_field_decorations = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        FIXME
        """
    )
    def _face_field_decorations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFaceFieldDecorations,
                        self.face_field_decorations)

    def get_element_block_array_status(self, *args):
        """
        V.get_element_block_array_status(string) -> int
        C++: int GetElementBlockArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetElementBlockArrayStatus, *args)
        return ret

    def set_element_block_array_status(self, *args):
        """
        V.set_element_block_array_status(string, int)
        C++: void SetElementBlockArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetElementBlockArrayStatus, *args)
        return ret

    def get_point_result_array_status(self, *args):
        """
        V.get_point_result_array_status(string) -> int
        C++: int GetPointResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetPointResultArrayStatus, *args)
        return ret

    def set_point_result_array_status(self, *args):
        """
        V.set_point_result_array_status(string, int)
        C++: void SetPointResultArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetPointResultArrayStatus, *args)
        return ret

    time_step_range = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _time_step_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepRange,
                        self.time_step_range)

    edge_field_decorations = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        FIXME
        """
    )
    def _edge_field_decorations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeFieldDecorations,
                        self.edge_field_decorations)

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

    def get_object_status(self, *args):
        """
        V.get_object_status(int, int) -> int
        C++: int GetObjectStatus(int objectType, int objectIndex)
        V.get_object_status(int, string) -> int
        C++: int GetObjectStatus(int objectType, const char *objectName)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectStatus, *args)
        return ret

    def set_object_status(self, *args):
        """
        V.set_object_status(int, int, int)
        C++: void SetObjectStatus(int objectType, int objectIndex,
            int status)
        V.set_object_status(int, string, int)
        C++: void SetObjectStatus(int objectType, const char *objectName,
            int status)"""
        ret = self._wrap_call(self._vtk_obj.SetObjectStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of the Exodus file.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def get_node_set_result_array_status(self, *args):
        """
        V.get_node_set_result_array_status(string) -> int
        C++: int GetNodeSetResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetNodeSetResultArrayStatus, *args)
        return ret

    def set_node_set_result_array_status(self, *args):
        """
        V.set_node_set_result_array_status(string, int)
        C++: void SetNodeSetResultArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetNodeSetResultArrayStatus, *args)
        return ret

    def get_edge_block_array_status(self, *args):
        """
        V.get_edge_block_array_status(string) -> int
        C++: int GetEdgeBlockArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeBlockArrayStatus, *args)
        return ret

    def set_edge_block_array_status(self, *args):
        """
        V.set_edge_block_array_status(string, int)
        C++: void SetEdgeBlockArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetEdgeBlockArrayStatus, *args)
        return ret

    def get_edge_map_array_status(self, *args):
        """
        V.get_edge_map_array_status(string) -> int
        C++: int GetEdgeMapArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeMapArrayStatus, *args)
        return ret

    def set_edge_map_array_status(self, *args):
        """
        V.set_edge_map_array_status(string, int)
        C++: void SetEdgeMapArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetEdgeMapArrayStatus, *args)
        return ret

    def get_element_set_result_array_status(self, *args):
        """
        V.get_element_set_result_array_status(string) -> int
        C++: int GetElementSetResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetElementSetResultArrayStatus, *args)
        return ret

    def set_element_set_result_array_status(self, *args):
        """
        V.set_element_set_result_array_status(string, int)
        C++: void SetElementSetResultArrayStatus(const char *name,
            int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetElementSetResultArrayStatus, *args)
        return ret

    def get_face_result_array_status(self, *args):
        """
        V.get_face_result_array_status(string) -> int
        C++: int GetFaceResultArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceResultArrayStatus, *args)
        return ret

    def set_face_result_array_status(self, *args):
        """
        V.set_face_result_array_status(string, int)
        C++: void SetFaceResultArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetFaceResultArrayStatus, *args)
        return ret

    def get_element_map_array_status(self, *args):
        """
        V.get_element_map_array_status(string) -> int
        C++: int GetElementMapArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetElementMapArrayStatus, *args)
        return ret

    def set_element_map_array_status(self, *args):
        """
        V.set_element_map_array_status(string, int)
        C++: void SetElementMapArrayStatus(const char *name, int flag)"""
        ret = self._wrap_call(self._vtk_obj.SetElementMapArrayStatus, *args)
        return ret

    file_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )
    def _file_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileId,
                        self.file_id)

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

    def _get_dimensionality(self):
        return self._vtk_obj.GetDimensionality()
    dimensionality = traits.Property(_get_dimensionality, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def get_edge_block_array_name(self, *args):
        """
        V.get_edge_block_array_name(int) -> string
        C++: const char *GetEdgeBlockArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeBlockArrayName, *args)
        return ret

    def get_edge_map_array_name(self, *args):
        """
        V.get_edge_map_array_name(int) -> string
        C++: const char *GetEdgeMapArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeMapArrayName, *args)
        return ret

    def get_edge_result_array_name(self, *args):
        """
        V.get_edge_result_array_name(int) -> string
        C++: const char *GetEdgeResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeResultArrayName, *args)
        return ret

    def get_edge_set_array_name(self, *args):
        """
        V.get_edge_set_array_name(int) -> string
        C++: const char *GetEdgeSetArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeSetArrayName, *args)
        return ret

    def get_edge_set_result_array_name(self, *args):
        """
        V.get_edge_set_result_array_name(int) -> string
        C++: const char *GetEdgeSetResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetEdgeSetResultArrayName, *args)
        return ret

    def get_element_block_array_name(self, *args):
        """
        V.get_element_block_array_name(int) -> string
        C++: const char *GetElementBlockArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetElementBlockArrayName, *args)
        return ret

    def get_element_map_array_name(self, *args):
        """
        V.get_element_map_array_name(int) -> string
        C++: const char *GetElementMapArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetElementMapArrayName, *args)
        return ret

    def get_element_result_array_name(self, *args):
        """
        V.get_element_result_array_name(int) -> string
        C++: const char *GetElementResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetElementResultArrayName, *args)
        return ret

    def get_element_set_array_name(self, *args):
        """
        V.get_element_set_array_name(int) -> string
        C++: const char *GetElementSetArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetElementSetArrayName, *args)
        return ret

    def get_element_set_result_array_name(self, *args):
        """
        V.get_element_set_result_array_name(int) -> string
        C++: const char *GetElementSetResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetElementSetResultArrayName, *args)
        return ret

    def _get_exodus_model(self):
        return wrap_vtk(self._vtk_obj.GetExodusModel())
    exodus_model = traits.Property(_get_exodus_model, help=\
        """
        Returns the object which encapsulates the model metadata.
        """
    )

    def get_face_block_array_name(self, *args):
        """
        V.get_face_block_array_name(int) -> string
        C++: const char *GetFaceBlockArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceBlockArrayName, *args)
        return ret

    def get_face_map_array_name(self, *args):
        """
        V.get_face_map_array_name(int) -> string
        C++: const char *GetFaceMapArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceMapArrayName, *args)
        return ret

    def get_face_result_array_name(self, *args):
        """
        V.get_face_result_array_name(int) -> string
        C++: const char *GetFaceResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceResultArrayName, *args)
        return ret

    def get_face_set_array_name(self, *args):
        """
        V.get_face_set_array_name(int) -> string
        C++: const char *GetFaceSetArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceSetArrayName, *args)
        return ret

    def get_face_set_result_array_name(self, *args):
        """
        V.get_face_set_result_array_name(int) -> string
        C++: const char *GetFaceSetResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetFaceSetResultArrayName, *args)
        return ret

    def get_global_edge_id(self, *args):
        """
        V.get_global_edge_id(DataSet, int) -> int
        C++: static int GetGlobalEdgeID(DataSet *data, int localID)
        V.get_global_edge_id(DataSet, int, int) -> int
        C++: static int GetGlobalEdgeID(DataSet *data, int localID,
            int searchType)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetGlobalEdgeID, *my_args)
        return ret

    def _get_global_edge_id_array_name(self):
        return self._vtk_obj.GetGlobalEdgeIdArrayName()
    global_edge_id_array_name = traits.Property(_get_global_edge_id_array_name, help=\
        """
        
        """
    )

    def get_global_element_id(self, *args):
        """
        V.get_global_element_id(DataSet, int) -> int
        C++: static int GetGlobalElementID(DataSet *data, int localID)
        V.get_global_element_id(DataSet, int, int) -> int
        C++: static int GetGlobalElementID(DataSet *data, int localID,
            int searchType)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetGlobalElementID, *my_args)
        return ret

    def _get_global_element_id_array_name(self):
        return self._vtk_obj.GetGlobalElementIdArrayName()
    global_element_id_array_name = traits.Property(_get_global_element_id_array_name, help=\
        """
        
        """
    )

    def get_global_face_id(self, *args):
        """
        V.get_global_face_id(DataSet, int) -> int
        C++: static int GetGlobalFaceID(DataSet *data, int localID)
        V.get_global_face_id(DataSet, int, int) -> int
        C++: static int GetGlobalFaceID(DataSet *data, int localID,
            int searchType)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetGlobalFaceID, *my_args)
        return ret

    def _get_global_face_id_array_name(self):
        return self._vtk_obj.GetGlobalFaceIdArrayName()
    global_face_id_array_name = traits.Property(_get_global_face_id_array_name, help=\
        """
        
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

    def get_global_result_array_name(self, *args):
        """
        V.get_global_result_array_name(int) -> string
        C++: const char *GetGlobalResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetGlobalResultArrayName, *args)
        return ret

    def get_hierarchy_array_name(self, *args):
        """
        V.get_hierarchy_array_name(int) -> string
        C++: const char *GetHierarchyArrayName(int arrayIdx)"""
        ret = self._wrap_call(self._vtk_obj.GetHierarchyArrayName, *args)
        return ret

    def _get_implicit_edge_id_array_name(self):
        return self._vtk_obj.GetImplicitEdgeIdArrayName()
    implicit_edge_id_array_name = traits.Property(_get_implicit_edge_id_array_name, help=\
        """
        
        """
    )

    def _get_implicit_element_id_array_name(self):
        return self._vtk_obj.GetImplicitElementIdArrayName()
    implicit_element_id_array_name = traits.Property(_get_implicit_element_id_array_name, help=\
        """
        
        """
    )

    def _get_implicit_face_id_array_name(self):
        return self._vtk_obj.GetImplicitFaceIdArrayName()
    implicit_face_id_array_name = traits.Property(_get_implicit_face_id_array_name, help=\
        """
        
        """
    )

    def _get_implicit_node_id_array_name(self):
        return self._vtk_obj.GetImplicitNodeIdArrayName()
    implicit_node_id_array_name = traits.Property(_get_implicit_node_id_array_name, help=\
        """
        Extra point data array that can be generated.  By default, this
        array is ON.  The value of the array is the integer id of the
        node. The id is relative to the entire data set. The name of the
        array is returned by global_node_id_array_name().
        """
    )

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

    def _get_metadata_m_time(self):
        return self._vtk_obj.GetMetadataMTime()
    metadata_m_time = traits.Property(_get_metadata_m_time, help=\
        """
        Return the MTime of the internal data structure. This is really
        only intended for use by PExodusIIReader in order to determine
        if the filename is newer than the metadata.
        """
    )

    def get_node_map_array_name(self, *args):
        """
        V.get_node_map_array_name(int) -> string
        C++: const char *GetNodeMapArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetNodeMapArrayName, *args)
        return ret

    def get_node_set_array_name(self, *args):
        """
        V.get_node_set_array_name(int) -> string
        C++: const char *GetNodeSetArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetNodeSetArrayName, *args)
        return ret

    def get_node_set_result_array_name(self, *args):
        """
        V.get_node_set_result_array_name(int) -> string
        C++: const char *GetNodeSetResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetNodeSetResultArrayName, *args)
        return ret

    def _get_number_of_assembly_arrays(self):
        return self._vtk_obj.GetNumberOfAssemblyArrays()
    number_of_assembly_arrays = traits.Property(_get_number_of_assembly_arrays, help=\
        """
        
        """
    )

    def _get_number_of_edge_block_arrays(self):
        return self._vtk_obj.GetNumberOfEdgeBlockArrays()
    number_of_edge_block_arrays = traits.Property(_get_number_of_edge_block_arrays, help=\
        """
        
        """
    )

    def _get_number_of_edge_map_arrays(self):
        return self._vtk_obj.GetNumberOfEdgeMapArrays()
    number_of_edge_map_arrays = traits.Property(_get_number_of_edge_map_arrays, help=\
        """
        
        """
    )

    def _get_number_of_edge_result_arrays(self):
        return self._vtk_obj.GetNumberOfEdgeResultArrays()
    number_of_edge_result_arrays = traits.Property(_get_number_of_edge_result_arrays, help=\
        """
        
        """
    )

    def _get_number_of_edge_set_arrays(self):
        return self._vtk_obj.GetNumberOfEdgeSetArrays()
    number_of_edge_set_arrays = traits.Property(_get_number_of_edge_set_arrays, help=\
        """
        
        """
    )

    def _get_number_of_edge_set_result_arrays(self):
        return self._vtk_obj.GetNumberOfEdgeSetResultArrays()
    number_of_edge_set_result_arrays = traits.Property(_get_number_of_edge_set_result_arrays, help=\
        """
        
        """
    )

    def _get_number_of_edges_in_file(self):
        return self._vtk_obj.GetNumberOfEdgesInFile()
    number_of_edges_in_file = traits.Property(_get_number_of_edges_in_file, help=\
        """
        
        """
    )

    def _get_number_of_element_block_arrays(self):
        return self._vtk_obj.GetNumberOfElementBlockArrays()
    number_of_element_block_arrays = traits.Property(_get_number_of_element_block_arrays, help=\
        """
        
        """
    )

    def _get_number_of_element_map_arrays(self):
        return self._vtk_obj.GetNumberOfElementMapArrays()
    number_of_element_map_arrays = traits.Property(_get_number_of_element_map_arrays, help=\
        """
        
        """
    )

    def _get_number_of_element_result_arrays(self):
        return self._vtk_obj.GetNumberOfElementResultArrays()
    number_of_element_result_arrays = traits.Property(_get_number_of_element_result_arrays, help=\
        """
        
        """
    )

    def _get_number_of_element_set_arrays(self):
        return self._vtk_obj.GetNumberOfElementSetArrays()
    number_of_element_set_arrays = traits.Property(_get_number_of_element_set_arrays, help=\
        """
        
        """
    )

    def _get_number_of_element_set_result_arrays(self):
        return self._vtk_obj.GetNumberOfElementSetResultArrays()
    number_of_element_set_result_arrays = traits.Property(_get_number_of_element_set_result_arrays, help=\
        """
        
        """
    )

    def _get_number_of_elements_in_file(self):
        return self._vtk_obj.GetNumberOfElementsInFile()
    number_of_elements_in_file = traits.Property(_get_number_of_elements_in_file, help=\
        """
        
        """
    )

    def get_number_of_entries_in_object(self, *args):
        """
        V.get_number_of_entries_in_object(int, int) -> int
        C++: int GetNumberOfEntriesInObject(int objectType,
            int objectIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfEntriesInObject, *args)
        return ret

    def _get_number_of_face_block_arrays(self):
        return self._vtk_obj.GetNumberOfFaceBlockArrays()
    number_of_face_block_arrays = traits.Property(_get_number_of_face_block_arrays, help=\
        """
        
        """
    )

    def _get_number_of_face_map_arrays(self):
        return self._vtk_obj.GetNumberOfFaceMapArrays()
    number_of_face_map_arrays = traits.Property(_get_number_of_face_map_arrays, help=\
        """
        
        """
    )

    def _get_number_of_face_result_arrays(self):
        return self._vtk_obj.GetNumberOfFaceResultArrays()
    number_of_face_result_arrays = traits.Property(_get_number_of_face_result_arrays, help=\
        """
        
        """
    )

    def _get_number_of_face_set_arrays(self):
        return self._vtk_obj.GetNumberOfFaceSetArrays()
    number_of_face_set_arrays = traits.Property(_get_number_of_face_set_arrays, help=\
        """
        
        """
    )

    def _get_number_of_face_set_result_arrays(self):
        return self._vtk_obj.GetNumberOfFaceSetResultArrays()
    number_of_face_set_result_arrays = traits.Property(_get_number_of_face_set_result_arrays, help=\
        """
        
        """
    )

    def _get_number_of_faces_in_file(self):
        return self._vtk_obj.GetNumberOfFacesInFile()
    number_of_faces_in_file = traits.Property(_get_number_of_faces_in_file, help=\
        """
        
        """
    )

    def _get_number_of_global_result_arrays(self):
        return self._vtk_obj.GetNumberOfGlobalResultArrays()
    number_of_global_result_arrays = traits.Property(_get_number_of_global_result_arrays, help=\
        """
        
        """
    )

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

    def _get_number_of_node_map_arrays(self):
        return self._vtk_obj.GetNumberOfNodeMapArrays()
    number_of_node_map_arrays = traits.Property(_get_number_of_node_map_arrays, help=\
        """
        
        """
    )

    def _get_number_of_node_set_arrays(self):
        return self._vtk_obj.GetNumberOfNodeSetArrays()
    number_of_node_set_arrays = traits.Property(_get_number_of_node_set_arrays, help=\
        """
        
        """
    )

    def _get_number_of_node_set_result_arrays(self):
        return self._vtk_obj.GetNumberOfNodeSetResultArrays()
    number_of_node_set_result_arrays = traits.Property(_get_number_of_node_set_result_arrays, help=\
        """
        
        """
    )

    def _get_number_of_nodes(self):
        return self._vtk_obj.GetNumberOfNodes()
    number_of_nodes = traits.Property(_get_number_of_nodes, help=\
        """
        
        """
    )

    def _get_number_of_nodes_in_file(self):
        return self._vtk_obj.GetNumberOfNodesInFile()
    number_of_nodes_in_file = traits.Property(_get_number_of_nodes_in_file, help=\
        """
        
        """
    )

    def get_number_of_object_array_components(self, *args):
        """
        V.get_number_of_object_array_components(int, int) -> int
        C++: int GetNumberOfObjectArrayComponents(int objectType,
            int arrayIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfObjectArrayComponents, *args)
        return ret

    def get_number_of_object_arrays(self, *args):
        """
        V.get_number_of_object_arrays(int) -> int
        C++: int GetNumberOfObjectArrays(int objectType)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfObjectArrays, *args)
        return ret

    def get_number_of_object_attributes(self, *args):
        """
        V.get_number_of_object_attributes(int, int) -> int
        C++: int GetNumberOfObjectAttributes(int objectType,
            int objectIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfObjectAttributes, *args)
        return ret

    def get_number_of_objects(self, *args):
        """
        V.get_number_of_objects(int) -> int
        C++: int GetNumberOfObjects(int objectType)"""
        ret = self._wrap_call(self._vtk_obj.GetNumberOfObjects, *args)
        return ret

    def _get_number_of_part_arrays(self):
        return self._vtk_obj.GetNumberOfPartArrays()
    number_of_part_arrays = traits.Property(_get_number_of_part_arrays, help=\
        """
        
        """
    )

    def _get_number_of_point_result_arrays(self):
        return self._vtk_obj.GetNumberOfPointResultArrays()
    number_of_point_result_arrays = traits.Property(_get_number_of_point_result_arrays, help=\
        """
        
        """
    )

    def _get_number_of_side_set_arrays(self):
        return self._vtk_obj.GetNumberOfSideSetArrays()
    number_of_side_set_arrays = traits.Property(_get_number_of_side_set_arrays, help=\
        """
        
        """
    )

    def _get_number_of_side_set_result_arrays(self):
        return self._vtk_obj.GetNumberOfSideSetResultArrays()
    number_of_side_set_result_arrays = traits.Property(_get_number_of_side_set_result_arrays, help=\
        """
        
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        Access to meta data generated by update_information.
        """
    )

    def get_object_array_index(self, *args):
        """
        V.get_object_array_index(int, string) -> int
        C++: int GetObjectArrayIndex(int objectType,
            const char *arrayName)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectArrayIndex, *args)
        return ret

    def get_object_array_name(self, *args):
        """
        V.get_object_array_name(int, int) -> string
        C++: const char *GetObjectArrayName(int objectType,
            int arrayIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectArrayName, *args)
        return ret

    def get_object_attribute_index(self, *args):
        """
        V.get_object_attribute_index(int, int, string) -> int
        C++: int GetObjectAttributeIndex(int objectType, int objectIndex,
            const char *attribName)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectAttributeIndex, *args)
        return ret

    def get_object_attribute_name(self, *args):
        """
        V.get_object_attribute_name(int, int, int) -> string
        C++: const char *GetObjectAttributeName(int objectType,
            int objectIndex, int attribIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectAttributeName, *args)
        return ret

    def get_object_id(self, *args):
        """
        V.get_object_id(int, int) -> int
        C++: int GetObjectId(int objectType, int objectIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectId, *args)
        return ret

    def _get_object_id_array_name(self):
        return self._vtk_obj.GetObjectIdArrayName()
    object_id_array_name = traits.Property(_get_object_id_array_name, help=\
        """
        Extra cell data array that can be generated.  By default, this
        array is ON.  The value of the array is the integer id found in
        the exodus file. The name of the array is returned by
        get_block_id_array_name(). For cells representing elements from an
        Exodus element block, this is set to the element block ID. For
        cells representing edges from an Exodus edge block, this is the
        edge block ID. Similarly, ths is the face block ID for cells
        representing faces from an Exodus face block. The same holds for
        cells representing entries of node, edge, face, side, and element
        sets.
        """
    )

    def get_object_index(self, *args):
        """
        V.get_object_index(int, string) -> int
        C++: int GetObjectIndex(int objectType, const char *objectName)
        V.get_object_index(int, int) -> int
        C++: int GetObjectIndex(int objectType, int id)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectIndex, *args)
        return ret

    def get_object_name(self, *args):
        """
        V.get_object_name(int, int) -> string
        C++: const char *GetObjectName(int objectType, int objectIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectName, *args)
        return ret

    def get_object_type_from_name(self, *args):
        """
        V.get_object_type_from_name(string) -> int
        C++: int GetObjectTypeFromName(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectTypeFromName, *args)
        return ret

    def get_object_type_name(self, *args):
        """
        V.get_object_type_name(int) -> string
        C++: const char *GetObjectTypeName(int)"""
        ret = self._wrap_call(self._vtk_obj.GetObjectTypeName, *args)
        return ret

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

    def _get_pedigree_edge_id_array_name(self):
        return self._vtk_obj.GetPedigreeEdgeIdArrayName()
    pedigree_edge_id_array_name = traits.Property(_get_pedigree_edge_id_array_name, help=\
        """
        
        """
    )

    def _get_pedigree_element_id_array_name(self):
        return self._vtk_obj.GetPedigreeElementIdArrayName()
    pedigree_element_id_array_name = traits.Property(_get_pedigree_element_id_array_name, help=\
        """
        
        """
    )

    def _get_pedigree_face_id_array_name(self):
        return self._vtk_obj.GetPedigreeFaceIdArrayName()
    pedigree_face_id_array_name = traits.Property(_get_pedigree_face_id_array_name, help=\
        """
        
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

    def get_point_result_array_name(self, *args):
        """
        V.get_point_result_array_name(int) -> string
        C++: const char *GetPointResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetPointResultArrayName, *args)
        return ret

    def _get_produced_fast_path_output(self):
        return self._vtk_obj.GetProducedFastPathOutput()
    produced_fast_path_output = traits.Property(_get_produced_fast_path_output, help=\
        """
        HACK: Used by PExodusIIReader to tell is the reader produced a
        valid fast path output.
        """
    )

    def _get_sil(self):
        return wrap_vtk(self._vtk_obj.GetSIL())
    sil = traits.Property(_get_sil, help=\
        """
        SIL describes organization of/relationships between
        classifications eg. blocks/materials/hierarchies.
        """
    )

    def _get_sil_update_stamp(self):
        return self._vtk_obj.GetSILUpdateStamp()
    sil_update_stamp = traits.Property(_get_sil_update_stamp, help=\
        """
        Every time the SIL is updated a this will return a different
        value.
        """
    )

    def get_side_set_array_name(self, *args):
        """
        V.get_side_set_array_name(int) -> string
        C++: const char *GetSideSetArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetSideSetArrayName, *args)
        return ret

    def get_side_set_result_array_name(self, *args):
        """
        V.get_side_set_result_array_name(int) -> string
        C++: const char *GetSideSetResultArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetSideSetResultArrayName, *args)
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

    def _get_total_number_of_edges(self):
        return self._vtk_obj.GetTotalNumberOfEdges()
    total_number_of_edges = traits.Property(_get_total_number_of_edges, help=\
        """
        
        """
    )

    def _get_total_number_of_elements(self):
        return self._vtk_obj.GetTotalNumberOfElements()
    total_number_of_elements = traits.Property(_get_total_number_of_elements, help=\
        """
        
        """
    )

    def _get_total_number_of_faces(self):
        return self._vtk_obj.GetTotalNumberOfFaces()
    total_number_of_faces = traits.Property(_get_total_number_of_faces, help=\
        """
        
        """
    )

    def _get_total_number_of_nodes(self):
        return self._vtk_obj.GetTotalNumberOfNodes()
    total_number_of_nodes = traits.Property(_get_total_number_of_nodes, help=\
        """
        
        """
    )

    def get_variable_id(self, *args):
        """
        V.get_variable_id(string, string) -> int
        C++: int GetVariableID(const char *type, const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetVariableID, *args)
        return ret

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: int CanReadFile(const char *fname)
        Determine if the file can be readed with this reader.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def dump(self):
        """
        V.dump()
        C++: virtual void Dump()"""
        ret = self._vtk_obj.Dump()
        return ret
        

    def edge_field_decorations_corner_averaged(self):
        """
        V.edge_field_decorations_corner_averaged()
        C++: void EdgeFieldDecorationsCornerAveraged()
        FIXME
        """
        ret = self._vtk_obj.EdgeFieldDecorationsCornerAveraged()
        return ret
        

    def edge_field_decorations_glyphs(self):
        """
        V.edge_field_decorations_glyphs()
        C++: void EdgeFieldDecorationsGlyphs()
        FIXME
        """
        ret = self._vtk_obj.EdgeFieldDecorationsGlyphs()
        return ret
        

    def edge_field_decorations_none(self):
        """
        V.edge_field_decorations_none()
        C++: void EdgeFieldDecorationsNone()
        FIXME
        """
        ret = self._vtk_obj.EdgeFieldDecorationsNone()
        return ret
        

    def face_field_decorations_corner_averaged(self):
        """
        V.face_field_decorations_corner_averaged()
        C++: void FaceFieldDecorationsCornerAveraged()
        FIXME
        """
        ret = self._vtk_obj.FaceFieldDecorationsCornerAveraged()
        return ret
        

    def face_field_decorations_glyphs(self):
        """
        V.face_field_decorations_glyphs()
        C++: void FaceFieldDecorationsGlyphs()
        FIXME
        """
        ret = self._vtk_obj.FaceFieldDecorationsGlyphs()
        return ret
        

    def face_field_decorations_none(self):
        """
        V.face_field_decorations_none()
        C++: void FaceFieldDecorationsNone()
        FIXME
        """
        ret = self._vtk_obj.FaceFieldDecorationsNone()
        return ret
        

    def is_valid_variable(self, *args):
        """
        V.is_valid_variable(string, string) -> int
        C++: int IsValidVariable(const char *type, const char *name)"""
        ret = self._wrap_call(self._vtk_obj.IsValidVariable, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reset the user-specified parameters and flush internal arrays so
        that the reader state is just as it was after the reader was
        instantiated.
        
        It doesn't make sense to let users reset only the internal state;
        both the settings and the state are changed by this call.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def reset_cache(self):
        """
        V.reset_cache()
        C++: void ResetCache()
        Clears out the cache entries.
        """
        ret = self._vtk_obj.ResetCache()
        return ret
        

    def reset_settings(self):
        """
        V.reset_settings()
        C++: void ResetSettings()
        Reset the user-specified parameters to their default values. The
        only settings not affected are the filename and/or pattern
        because these have no default.
        
        Resetting the settings but not the state allows users to keep the
        active cache but return to initial array selections, etc.
        """
        ret = self._vtk_obj.ResetSettings()
        return ret
        

    def set_all_array_status(self, *args):
        """
        V.set_all_array_status(int, int)
        C++: void SetAllArrayStatus(int otype, int status)"""
        ret = self._wrap_call(self._vtk_obj.SetAllArrayStatus, *args)
        return ret

    def set_fast_path_id_type(self, *args):
        """
        V.set_fast_path_id_type(string)
        C++: void SetFastPathIdType(const char *type)
        Possible argument values: "INDEX","GLOBAL" "GLOBAL" means the id
        refers to a global id "INDEX" means the id refers to an index
        into the VTK array
        """
        ret = self._wrap_call(self._vtk_obj.SetFastPathIdType, *args)
        return ret

    def set_fast_path_object_id(self, *args):
        """
        V.set_fast_path_object_id(int)
        C++: void SetFastPathObjectId(IdType id)
        Possible argument values: "INDEX","GLOBAL" "GLOBAL" means the id
        refers to a global id "INDEX" means the id refers to an index
        into the VTK array
        """
        ret = self._wrap_call(self._vtk_obj.SetFastPathObjectId, *args)
        return ret

    def set_fast_path_object_type(self, *args):
        """
        V.set_fast_path_object_type(string)
        C++: void SetFastPathObjectType(const char *type)
        Set the fast-path keys. All three must be set for the fast-path
        option to work. Possible argument values:
        "POINT","CELL","EDGE","FACE"
        """
        ret = self._wrap_call(self._vtk_obj.SetFastPathObjectType, *args)
        return ret

    def set_mode_shape(self, *args):
        """
        V.set_mode_shape(int)
        C++: void SetModeShape(int val)
        Convenience method to set the mode-shape which is same as
        this->_set_time_step(val-_1);
        """
        ret = self._wrap_call(self._vtk_obj.SetModeShape, *args)
        return ret

    def update_time_information(self):
        """
        V.update_time_information()
        C++: virtual void UpdateTimeInformation()
        Re-reads time information from the exodus file and updates
        time_step_range accordingly.
        """
        ret = self._vtk_obj.UpdateTimeInformation()
        return ret
        

    _updateable_traits_ = \
    (('displacement_magnitude', 'GetDisplacementMagnitude'),
    ('xml_file_name', 'GetXMLFileName'),
    ('generate_implicit_element_id_array',
    'GetGenerateImplicitElementIdArray'), ('file_name', 'GetFileName'),
    ('exodus_model_metadata', 'GetExodusModelMetadata'),
    ('reference_count', 'GetReferenceCount'),
    ('generate_global_element_id_array',
    'GetGenerateGlobalElementIdArray'), ('generate_global_node_id_array',
    'GetGenerateGlobalNodeIdArray'), ('display_type', 'GetDisplayType'),
    ('generate_file_id_array', 'GetGenerateFileIdArray'), ('time_step',
    'GetTimeStep'), ('debug', 'GetDebug'), ('animate_mode_shapes',
    'GetAnimateModeShapes'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('generate_implicit_node_id_array',
    'GetGenerateImplicitNodeIdArray'), ('apply_displacements',
    'GetApplyDisplacements'), ('progress_text', 'GetProgressText'),
    ('generate_object_id_cell_array', 'GetGenerateObjectIdCellArray'),
    ('mode_shape_time', 'GetModeShapeTime'), ('time_step_range',
    'GetTimeStepRange'), ('pack_exodus_model_onto_output',
    'GetPackExodusModelOntoOutput'), ('abort_execute', 'GetAbortExecute'),
    ('has_mode_shapes', 'GetHasModeShapes'), ('release_data_flag',
    'GetReleaseDataFlag'), ('face_field_decorations',
    'GetFaceFieldDecorations'), ('progress', 'GetProgress'),
    ('edge_field_decorations', 'GetEdgeFieldDecorations'), ('file_id',
    'GetFileId'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'animate_mode_shapes', 'apply_displacements',
    'debug', 'exodus_model_metadata', 'generate_file_id_array',
    'generate_global_element_id_array', 'generate_global_node_id_array',
    'generate_implicit_element_id_array',
    'generate_implicit_node_id_array', 'generate_object_id_cell_array',
    'global_warning_display', 'has_mode_shapes',
    'pack_exodus_model_onto_output', 'release_data_flag',
    'displacement_magnitude', 'display_type', 'edge_field_decorations',
    'face_field_decorations', 'file_id', 'file_name', 'mode_shape_time',
    'progress_text', 'time_step', 'time_step_range', 'xml_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExodusIIReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExodusIIReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['animate_mode_shapes', 'apply_displacements',
            'exodus_model_metadata', 'generate_file_id_array',
            'generate_global_element_id_array', 'generate_global_node_id_array',
            'generate_implicit_element_id_array',
            'generate_implicit_node_id_array', 'generate_object_id_cell_array',
            'has_mode_shapes', 'pack_exodus_model_onto_output'], [],
            ['displacement_magnitude', 'display_type', 'edge_field_decorations',
            'face_field_decorations', 'file_id', 'file_name', 'mode_shape_time',
            'time_step', 'time_step_range', 'xml_file_name']),
            title='Edit ExodusIIReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExodusIIReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

