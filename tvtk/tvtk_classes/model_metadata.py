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

from tvtk.tvtk_classes.object import Object


class ModelMetadata(Object):
    """
    ModelMetadata - This class encapsulates the metadata
    
    Superclass: Object
    
    This class is inspired by the Exodus II file format, but
      because this class does not depend on the Exodus library, it
      should be possible to use it to represent metadata for other
      dataset file formats.  Sandia Labs uses it in their Exodus II
      reader, their Exodus II writer and their en_sight writer.
      DistributedDataFilter looks for metadata attached to
      it's input and redistributes the metadata with the grid.
    
    
      The fields in this class are those described in the document
      "EXODUS II: A Finite Element Data Model", SAND92-2137, November
    1995.
    
    
      Element and node IDs stored in this object must be global IDs,
      in the event that the original dataset was partitioned across
      many files.
    
    
      One way to initialize this object is by using ExodusModel
      (a Sandia class used by the Sandia Exodus reader).
      That class will take an open Exodus II file and a
      UnstructuredGrid drawn from it and will set the required fields.
    
    
      Alternatively, you can use all the Set*
      methods to set the individual fields. This class does not
      copy the data, it simply uses your pointer. This
      class will free the storage associated with your pointer
      when the class is deleted.  Most fields have sensible defaults.
      The only requirement is that if you are using this model_metadata
      to write out an Exodus or en_sight file in parallel, you must
      set_block_ids and set_block_id_array_name.  Your UnstructuredGrid must
      have a cell array giving the block ID for each cell.
    
    Caveats:
    
    
      The Exodus II library supports an optimized element order map
      (section 3.7 in the SAND document).  It contains all the element
      IDs, listed in the order in which a solver should process them.
      We don't include this, and won't unless there is a request.
    
    
      There is an assumption in some classes that the name of the cell
      array containing global element ids is "_global_element_id" and the
      name of the point array containing global node ids is
    "_global_node_id".
      (element == cell) and (node == point).
    
    See also:
    
    
      DistributedDataFilter ExtractCells
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkModelMetadata, obj, update, **traits)
    
    all_variables_defined_in_all_blocks = tvtk_base.false_bool_trait(help=\
        """
        Instead of a truth table of all "1"s, you can set this
          instance variable to indicate that all variables are
          defined in all blocks.
        """
    )
    def _all_variables_defined_in_all_blocks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllVariablesDefinedInAllBlocks,
                        self.all_variables_defined_in_all_blocks_)

    number_of_blocks = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The number of blocks in the file.  Set this before setting
          any of the block arrays.
        """
    )
    def _number_of_blocks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfBlocks,
                        self.number_of_blocks)

    number_of_node_sets = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The number of node sets in the file.  Set this value before
          setting the various node set arrays.
        """
    )
    def _number_of_node_sets_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfNodeSets,
                        self.number_of_node_sets)

    time_step_index = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the index of the time step represented by the results
           data in the file attached to this model_metadata object.  Time
           step indices start at 0 in this file, they start at 1 in
           an Exodus file.
        """
    )
    def _time_step_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepIndex,
                        self.time_step_index)

    number_of_side_sets = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set or get the number of side sets.  Set this value before
          setting any of the other side set arrays.
        """
    )
    def _number_of_side_sets_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSideSets,
                        self.number_of_side_sets)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The title of the dataset.
        """
    )
    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    def get_block_local_index(self, *args):
        """
        V.get_block_local_index(int) -> int
        C++: int GetBlockLocalIndex(int id)
        Block information is stored in arrays.  This method returns
          the array index for a given block ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockLocalIndex, *args)
        return ret

    def _get_dimension(self):
        return self._vtk_obj.GetDimension()
    dimension = traits.Property(_get_dimension, help=\
        """
        Get the dimension of the model.  This is also the number
          of coordinate names.
        """
    )

    def _get_number_of_block_properties(self):
        return self._vtk_obj.GetNumberOfBlockProperties()
    number_of_block_properties = traits.Property(_get_number_of_block_properties, help=\
        """
        The number of block properties (global variables)
        """
    )

    def _get_number_of_element_variables(self):
        return self._vtk_obj.GetNumberOfElementVariables()
    number_of_element_variables = traits.Property(_get_number_of_element_variables, help=\
        """
        The model_metadata object may contain these lists:
           o  the variables in the original data file
           o  the variables created in the u grid from those original
        variables
           o  a mapping from the grid variable names to the original
        names
           o  a list of the number of components each grid variable has
        
        
          (Example: Variables in Exodus II files are all scalars.  Some
        are
          combined by the exodus_reader into vector variables in the
        grid.)
        
        
          These methods return names of the original variables, the names
          of the grid variables, a list of the number of components in
          each grid variable, and a list of the index into the list of
          original variable names where the original name of the first
          component of a grid variable may be found.  The names of
        subsequent
          components would immediately follow the name of the the first
          component.
        """
    )

    def _get_number_of_global_variables(self):
        return self._vtk_obj.GetNumberOfGlobalVariables()
    number_of_global_variables = traits.Property(_get_number_of_global_variables, help=\
        """
        Get the number of global variables per time step
        """
    )

    def _get_number_of_information_lines(self):
        return self._vtk_obj.GetNumberOfInformationLines()
    number_of_information_lines = traits.Property(_get_number_of_information_lines, help=\
        """
        Get the number of information lines.
        """
    )

    def _get_number_of_node_set_properties(self):
        return self._vtk_obj.GetNumberOfNodeSetProperties()
    number_of_node_set_properties = traits.Property(_get_number_of_node_set_properties, help=\
        """
        The number of node set properties (global variables)
        """
    )

    def _get_number_of_node_variables(self):
        return self._vtk_obj.GetNumberOfNodeVariables()
    number_of_node_variables = traits.Property(_get_number_of_node_variables, help=\
        """
        
        """
    )

    def _get_number_of_qa_records(self):
        return self._vtk_obj.GetNumberOfQARecords()
    number_of_qa_records = traits.Property(_get_number_of_qa_records, help=\
        """
        Get the number of QA records
        """
    )

    def _get_number_of_side_set_properties(self):
        return self._vtk_obj.GetNumberOfSideSetProperties()
    number_of_side_set_properties = traits.Property(_get_number_of_side_set_properties, help=\
        """
        The number of side set properties (global variables)
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        Set the total number of time steps in the file,
           and the value at each time step.  We use your time
           step value array and delete it when we're done.
        """
    )

    def _get_original_number_of_element_variables(self):
        return self._vtk_obj.GetOriginalNumberOfElementVariables()
    original_number_of_element_variables = traits.Property(_get_original_number_of_element_variables, help=\
        """
        The model_metadata object may contain these lists:
           o  the variables in the original data file
           o  the variables created in the u grid from those original
        variables
           o  a mapping from the grid variable names to the original
        names
           o  a list of the number of components each grid variable has
        
        
          (Example: Variables in Exodus II files are all scalars.  Some
        are
          combined by the exodus_reader into vector variables in the
        grid.)
        
        
          These methods return names of the original variables, the names
          of the grid variables, a list of the number of components in
          each grid variable, and a list of the index into the list of
          original variable names where the original name of the first
          component of a grid variable may be found.  The names of
        subsequent
          components would immediately follow the name of the the first
          component.
        """
    )

    def _get_original_number_of_node_variables(self):
        return self._vtk_obj.GetOriginalNumberOfNodeVariables()
    original_number_of_node_variables = traits.Property(_get_original_number_of_node_variables, help=\
        """
        
        """
    )

    def _get_size_block_attribute_array(self):
        return self._vtk_obj.GetSizeBlockAttributeArray()
    size_block_attribute_array = traits.Property(_get_size_block_attribute_array, help=\
        """
        Get the length of the list of floating point block attributes.
        """
    )

    def _get_sum_dist_fact_per_node_set(self):
        return self._vtk_obj.GetSumDistFactPerNodeSet()
    sum_dist_fact_per_node_set = traits.Property(_get_sum_dist_fact_per_node_set, help=\
        """
        Get the total number of distribution factors stored for all node
        sets
        """
    )

    def _get_sum_dist_fact_per_side_set(self):
        return self._vtk_obj.GetSumDistFactPerSideSet()
    sum_dist_fact_per_side_set = traits.Property(_get_sum_dist_fact_per_side_set, help=\
        """
        Get the total number of distribution factors stored for all side
        sets
        """
    )

    def _get_sum_elements_per_block(self):
        return self._vtk_obj.GetSumElementsPerBlock()
    sum_elements_per_block = traits.Property(_get_sum_elements_per_block, help=\
        """
        Get the length of the list of elements in every block.
        """
    )

    def _get_sum_nodes_per_node_set(self):
        return self._vtk_obj.GetSumNodesPerNodeSet()
    sum_nodes_per_node_set = traits.Property(_get_sum_nodes_per_node_set, help=\
        """
        Get the total number of nodes in all node sets
        """
    )

    def _get_sum_sides_per_side_set(self):
        return self._vtk_obj.GetSumSidesPerSideSet()
    sum_sides_per_side_set = traits.Property(_get_sum_sides_per_side_set, help=\
        """
        Get the total number of sides in all side sets
        """
    )

    def add_information_line(self, *args):
        """
        V.add_information_line(string)
        C++: void AddInformationLine(char *info)
        Add an information line.
        """
        ret = self._wrap_call(self._vtk_obj.AddInformationLine, *args)
        return ret

    def add_qa_record(self, *args):
        """
        V.add_qa_record(string, string, string, string)
        C++: void AddQARecord(char *name, char *version, char *date,
            char *time)
        Add a QA record.  They fields are:
           The code name
           The code version number
           The date (MM/DD/YY or NULL for today)
           The time (HH:MM:SS or NULL for right now)
        """
        ret = self._wrap_call(self._vtk_obj.AddQARecord, *args)
        return ret

    def add_u_grid_element_variable(self, *args):
        """
        V.add_u_grid_element_variable(string, string, int) -> int
        C++: int AddUGridElementVariable(char *ugridVarName,
            char *origName, int numComponents)
        In order to write Exodus files from UnstructuredGrid
          objects that were read from Exodus files, we need to know
          the mapping from variable names in the UGrid to variable
          names in the Exodus file.  (The Exodus reader combines
          scalar variables with similar names into vectors in the
          UGrid.)  When building the UGrid to which this
          model_metadata refers, add each element and node variable
          name with this call, including the name of original variable
          that yielded it's first component, and the number of
        components.
          If a variable is removed from the UGrid, remove it from
          the model_metadata.  (If this information is missing or
          incomplete, the exodus_ii_writer can still do something
          sensible in creating names for variables.)
        """
        ret = self._wrap_call(self._vtk_obj.AddUGridElementVariable, *args)
        return ret

    def add_u_grid_node_variable(self, *args):
        """
        V.add_u_grid_node_variable(string, string, int) -> int
        C++: int AddUGridNodeVariable(char *ugridVarName, char *origName,
            int numComponents)"""
        ret = self._wrap_call(self._vtk_obj.AddUGridNodeVariable, *args)
        return ret

    def element_variable_is_defined_in_block(self, *args):
        """
        V.element_variable_is_defined_in_block(string, int) -> int
        C++: int ElementVariableIsDefinedInBlock(char *varname,
            int blockId)
        If the element variable named is defined for the block Id
          provided (in the element variable truth table) return a
          1, otherwise return a 0.  If the variable name or block Id
          are unrecognized, the default value of 1 is returned.
          (This is an "original" variable name, from the file,
          not a name created for the UnstructuredGrid.  Use
          find_original*_variable_name to map between the two.)
        """
        ret = self._wrap_call(self._vtk_obj.ElementVariableIsDefinedInBlock, *args)
        return ret

    def extract_global_metadata(self):
        """
        V.extract_global_metadata() -> ModelMetadata
        C++: ModelMetadata *ExtractGlobalMetadata()
        Create and return a new metadata object containing only the
          global metadata of this metadata object.
        """
        ret = wrap_vtk(self._vtk_obj.ExtractGlobalMetadata())
        return ret
        

    def extract_model_metadata(self, *args):
        """
        V.extract_model_metadata(IdTypeArray, DataSet)
            -> ModelMetadata
        C++: ModelMetadata *ExtractModelMetadata(
            IdTypeArray *globalCellIdList, DataSet *grid)
        Create and return a new metadata object which contains
          the information for the subset of global cell IDs provided.
          We need the grid containing the cells so we can find point
          Ids as well, and also the name of the global cell ID array
          and the name of the global point ID array.
        """
        my_args = deref_array(args, [('vtkIdTypeArray', 'vtkDataSet')])
        ret = self._wrap_call(self._vtk_obj.ExtractModelMetadata, *my_args)
        return wrap_vtk(ret)

    def find_original_element_variable_name(self, *args):
        """
        V.find_original_element_variable_name(string, int) -> string
        C++: char *FindOriginalElementVariableName(const char *name,
            int component)
        Given the name of an element variable the UnstructuredGrid
          described by this model_metadata, and a component number, give
          the name of the scalar array in the original
          file that turned into that component when the file was
          read into VTK.
        """
        ret = self._wrap_call(self._vtk_obj.FindOriginalElementVariableName, *args)
        return ret

    def find_original_node_variable_name(self, *args):
        """
        V.find_original_node_variable_name(string, int) -> string
        C++: char *FindOriginalNodeVariableName(const char *name,
            int component)
        Given the name of an node variable the UnstructuredGrid
          described by this model_metadata, and a component number, give
          the name of the scalar array in the original
          file that turned into that component when the file was
          read into VTK.
        """
        ret = self._wrap_call(self._vtk_obj.FindOriginalNodeVariableName, *args)
        return ret

    def free_all_global_data(self):
        """
        V.free_all_global_data()
        C++: void FreeAllGlobalData()
        Free selected portions of the metadata when updating values
          in the ModelMetadata object.  Resetting a particular field,
          (i.e. set_node_set_ids) frees the previous setting, but if you
          are not setting every field, you may want to do a wholesale
          "Free" first.
        
        
          free_all_global_data frees all the fields which don't depend on
            which time step, which blocks, or which variables are in the
        input.
          free_all_local_data frees all the fields which do depend on which
            time step, blocks or variables are in the input.
          free_block_dependent_data frees all metadata fields which depend
        on
            which blocks were read in.
        """
        ret = self._vtk_obj.FreeAllGlobalData()
        return ret
        

    def free_all_local_data(self):
        """
        V.free_all_local_data()
        C++: void FreeAllLocalData()
        Free selected portions of the metadata when updating values
          in the ModelMetadata object.  Resetting a particular field,
          (i.e. set_node_set_ids) frees the previous setting, but if you
          are not setting every field, you may want to do a wholesale
          "Free" first.
        
        
          free_all_global_data frees all the fields which don't depend on
            which time step, which blocks, or which variables are in the
        input.
          free_all_local_data frees all the fields which do depend on which
            time step, blocks or variables are in the input.
          free_block_dependent_data frees all metadata fields which depend
        on
            which blocks were read in.
        """
        ret = self._vtk_obj.FreeAllLocalData()
        return ret
        

    def free_block_dependent_data(self):
        """
        V.free_block_dependent_data()
        C++: void FreeBlockDependentData()
        Free selected portions of the metadata when updating values
          in the ModelMetadata object.  Resetting a particular field,
          (i.e. set_node_set_ids) frees the previous setting, but if you
          are not setting every field, you may want to do a wholesale
          "Free" first.
        
        
          free_all_global_data frees all the fields which don't depend on
            which time step, which blocks, or which variables are in the
        input.
          free_all_local_data frees all the fields which do depend on which
            time step, blocks or variables are in the input.
          free_block_dependent_data frees all metadata fields which depend
        on
            which blocks were read in.
        """
        ret = self._vtk_obj.FreeBlockDependentData()
        return ret
        

    def free_original_element_variable_names(self):
        """
        V.free_original_element_variable_names()
        C++: void FreeOriginalElementVariableNames()
        Free selected portions of the metadata when updating values
          in the ModelMetadata object.  Resetting a particular field,
          (i.e. set_node_set_ids) frees the previous setting, but if you
          are not setting every field, you may want to do a wholesale
          "Free" first.
        
        
          free_all_global_data frees all the fields which don't depend on
            which time step, which blocks, or which variables are in the
        input.
          free_all_local_data frees all the fields which do depend on which
            time step, blocks or variables are in the input.
          free_block_dependent_data frees all metadata fields which depend
        on
            which blocks were read in.
        """
        ret = self._vtk_obj.FreeOriginalElementVariableNames()
        return ret
        

    def free_original_node_variable_names(self):
        """
        V.free_original_node_variable_names()
        C++: void FreeOriginalNodeVariableNames()
        Free selected portions of the metadata when updating values
          in the ModelMetadata object.  Resetting a particular field,
          (i.e. set_node_set_ids) frees the previous setting, but if you
          are not setting every field, you may want to do a wholesale
          "Free" first.
        
        
          free_all_global_data frees all the fields which don't depend on
            which time step, which blocks, or which variables are in the
        input.
          free_all_local_data frees all the fields which do depend on which
            time step, blocks or variables are in the input.
          free_block_dependent_data frees all metadata fields which depend
        on
            which blocks were read in.
        """
        ret = self._vtk_obj.FreeOriginalNodeVariableNames()
        return ret
        

    def free_used_element_variable_names(self):
        """
        V.free_used_element_variable_names()
        C++: void FreeUsedElementVariableNames()
        Free selected portions of the metadata when updating values
          in the ModelMetadata object.  Resetting a particular field,
          (i.e. set_node_set_ids) frees the previous setting, but if you
          are not setting every field, you may want to do a wholesale
          "Free" first.
        
        
          free_all_global_data frees all the fields which don't depend on
            which time step, which blocks, or which variables are in the
        input.
          free_all_local_data frees all the fields which do depend on which
            time step, blocks or variables are in the input.
          free_block_dependent_data frees all metadata fields which depend
        on
            which blocks were read in.
        """
        ret = self._vtk_obj.FreeUsedElementVariableNames()
        return ret
        

    def free_used_element_variables(self):
        """
        V.free_used_element_variables()
        C++: void FreeUsedElementVariables()
        Free selected portions of the metadata when updating values
          in the ModelMetadata object.  Resetting a particular field,
          (i.e. set_node_set_ids) frees the previous setting, but if you
          are not setting every field, you may want to do a wholesale
          "Free" first.
        
        
          free_all_global_data frees all the fields which don't depend on
            which time step, which blocks, or which variables are in the
        input.
          free_all_local_data frees all the fields which do depend on which
            time step, blocks or variables are in the input.
          free_block_dependent_data frees all metadata fields which depend
        on
            which blocks were read in.
        """
        ret = self._vtk_obj.FreeUsedElementVariables()
        return ret
        

    def free_used_node_variable_names(self):
        """
        V.free_used_node_variable_names()
        C++: void FreeUsedNodeVariableNames()
        Free selected portions of the metadata when updating values
          in the ModelMetadata object.  Resetting a particular field,
          (i.e. set_node_set_ids) frees the previous setting, but if you
          are not setting every field, you may want to do a wholesale
          "Free" first.
        
        
          free_all_global_data frees all the fields which don't depend on
            which time step, which blocks, or which variables are in the
        input.
          free_all_local_data frees all the fields which do depend on which
            time step, blocks or variables are in the input.
          free_block_dependent_data frees all metadata fields which depend
        on
            which blocks were read in.
        """
        ret = self._vtk_obj.FreeUsedNodeVariableNames()
        return ret
        

    def free_used_node_variables(self):
        """
        V.free_used_node_variables()
        C++: void FreeUsedNodeVariables()
        Free selected portions of the metadata when updating values
          in the ModelMetadata object.  Resetting a particular field,
          (i.e. set_node_set_ids) frees the previous setting, but if you
          are not setting every field, you may want to do a wholesale
          "Free" first.
        
        
          free_all_global_data frees all the fields which don't depend on
            which time step, which blocks, or which variables are in the
        input.
          free_all_local_data frees all the fields which do depend on which
            time step, blocks or variables are in the input.
          free_block_dependent_data frees all metadata fields which depend
        on
            which blocks were read in.
        """
        ret = self._vtk_obj.FreeUsedNodeVariables()
        return ret
        

    def has_metadata(self, *args):
        """
        V.has_metadata(DataSet) -> int
        C++: static int HasMetadata(DataSet *grid)
        Static function that returns 1 if the UnstructuredGrid
          has metadata packed into it's field arrays, and 0 otherwise.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasMetadata, *my_args)
        return ret

    def merge_global_information(self, *args):
        """
        V.merge_global_information(ModelMetadata) -> int
        C++: int MergeGlobalInformation(const ModelMetadata *em)
        The metadata is divided into global metadata and local
          metadata.  merge_global_information merges just the
          global metadata of the supplied object into the
          global metadata of this object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MergeGlobalInformation, *my_args)
        return ret

    def merge_model_metadata(self, *args):
        """
        V.merge_model_metadata(ModelMetadata) -> int
        C++: int MergeModelMetadata(const ModelMetadata *em)
        In VTK we take UnstructuredGrids and perform
          operations on them, including subsetting and merging
          grids.  We need to modify the metadata object
          when this happens.  merge_model_metadata merges the supplied
          model (both global and local metadata) into this model.
          The models must be from the same file set.
        
        
          merge_model_metadata assumes that no element in one metadata
          object appears in the other.  (It doesn't test for duplicate
          elements when merging the two metadata objects.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MergeModelMetadata, *my_args)
        return ret

    def pack(self, *args):
        """
        V.pack(DataSet)
        C++: void Pack(DataSet *ugrid)
        Pack this object's metadata into a field array of a dataset.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Pack, *my_args)
        return ret

    def print_global_information(self):
        """
        V.print_global_information()
        C++: virtual void PrintGlobalInformation()
        The global fields are those which pertain to the whole
           file.  Examples are the title, information lines,
           and list of block IDs.  This method prints out all the
           global information.
        """
        ret = self._vtk_obj.PrintGlobalInformation()
        return ret
        

    def print_local_information(self):
        """
        V.print_local_information()
        C++: virtual void PrintLocalInformation()
        The local fields are those which depend on exactly which
           blocks, which time step, and which variables you read in
           from the file.  Examples are the number of cells in
           each block, and the list of nodes in a node set, or the
           value of the global variables at a time step.  If
           VERBOSE_TESTING is defined in your execution environment,
           this method will print more than mere counts, and actually
           print a few of the IDs, distribution factors and so on.  If
           VERY_VERBOSE_TESTING is defined, it will print out
           all ID lists, distribution factor lists, and so on.
        """
        ret = self._vtk_obj.PrintLocalInformation()
        return ret
        

    def remove_metadata(self, *args):
        """
        V.remove_metadata(DataSet)
        C++: static void RemoveMetadata(DataSet *grid)
        Static function that removes the packed metadata arrays
          from a dataset.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveMetadata, *my_args)
        return ret

    def remove_u_grid_element_variable(self, *args):
        """
        V.remove_u_grid_element_variable(string) -> int
        C++: int RemoveUGridElementVariable(char *ugridVarName)
        In order to write Exodus files from UnstructuredGrid
          objects that were read from Exodus files, we need to know
          the mapping from variable names in the UGrid to variable
          names in the Exodus file.  (The Exodus reader combines
          scalar variables with similar names into vectors in the
          UGrid.)  When building the UGrid to which this
          model_metadata refers, add each element and node variable
          name with this call, including the name of original variable
          that yielded it's first component, and the number of
        components.
          If a variable is removed from the UGrid, remove it from
          the model_metadata.  (If this information is missing or
          incomplete, the exodus_ii_writer can still do something
          sensible in creating names for variables.)
        """
        ret = self._wrap_call(self._vtk_obj.RemoveUGridElementVariable, *args)
        return ret

    def remove_u_grid_node_variable(self, *args):
        """
        V.remove_u_grid_node_variable(string) -> int
        C++: int RemoveUGridNodeVariable(char *ugridVarName)"""
        ret = self._wrap_call(self._vtk_obj.RemoveUGridNodeVariable, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Set the object back to it's initial state
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def unpack(self, *args):
        """
        V.unpack(DataSet, int) -> int
        C++: int Unpack(DataSet *ugrid, int deleteIt)
        Unpack the metadata stored in a dataset,
          and initialize this object with it.  Return 1 if there's
          no metadata packed into the grid, 0 if OK.
          If delete_it is ON, then delete the grid's packed data after
          unpacking it into the object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Unpack, *my_args)
        return ret

    _updateable_traits_ = \
    (('number_of_side_sets', 'GetNumberOfSideSets'),
    ('number_of_node_sets', 'GetNumberOfNodeSets'),
    ('all_variables_defined_in_all_blocks',
    'GetAllVariablesDefinedInAllBlocks'), ('number_of_blocks',
    'GetNumberOfBlocks'), ('title', 'GetTitle'), ('reference_count',
    'GetReferenceCount'), ('debug', 'GetDebug'), ('time_step_index',
    'GetTimeStepIndex'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['all_variables_defined_in_all_blocks', 'debug',
    'global_warning_display', 'number_of_blocks', 'number_of_node_sets',
    'number_of_side_sets', 'time_step_index', 'title'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ModelMetadata, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ModelMetadata properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['all_variables_defined_in_all_blocks'], [],
            ['number_of_blocks', 'number_of_node_sets', 'number_of_side_sets',
            'time_step_index', 'title']),
            title='Edit ModelMetadata properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ModelMetadata properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

