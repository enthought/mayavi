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


class ExodusModel(Object):
    """
    ExodusModel - Exodus Model
    
    Superclass: Object
    
    A UnstructuredGrid output by ExodusReader or PExodusReader
      is missing a great deal of initialization and static model data
      that is in an Exodus II file.  (Global variables, properties,
      node sets, side sets, and so on.)  This data can be stored in a
      ModelMetadata object, which can be initialized using
      this ExodusModel class.
    
    
      This class can be initialized with a file handle for an open Exodus
      file, and the UnstructuredGrid derived from that file.  The
    methods
      used would be set_global_information, set_local_information,
      add_u_grid_element_variable and add_u_grid_node_variable.  The
    ExodusReader
      does this.
    
    
      It can also be initialized (using unpack_exodus_model) from a
      UnstructuredGrid that has had metadata packed into it's field
      arrays with pack_exodus_model.   The ExodusIIWriter does this.
    
    
      If you plan to write out the Exodus file (with ExodusIIWriter),
      you should direct the Exodus reader to create a ExodusModel
    object.
      This will be used by the Exodus writer to create a correct Exodus
    II
      file on output.  In addition, the DistributedDataFilter is
      cognizant of the exodus_model object and will unpack, extract,
    merge,
      and pack these objects associated with the grids it is
    partitioning.
    
    See also:
    
    
      ExodusReader  PExodusReader ExodusIIWriter
    ModelMetadata
      DistributedDataFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExodusModel, obj, update, **traits)
    
    def _get_model_metadata(self):
        return wrap_vtk(self._vtk_obj.GetModelMetadata())
    def _set_model_metadata(self, arg):
        old_val = self._get_model_metadata()
        self._wrap_call(self._vtk_obj.SetModelMetadata,
                        deref_vtk(arg))
        self.trait_property_changed('model_metadata', old_val, arg)
    model_metadata = traits.Property(_get_model_metadata, _set_model_metadata, help=\
        """
        Set or get the underlying ModelMetadata object.
        """
    )

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
          exodus_model refers, add each element and node variable
          name with this call, including the name of original variable
          that yielded it's first component, and the number of
        components.
          If a variable is removed from the UGrid, remove it from
          the exodus_model.  (If this information is missing or
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

    def extract_exodus_model(self, *args):
        """
        V.extract_exodus_model(IdTypeArray, UnstructuredGrid)
            -> ExodusModel
        C++: ExodusModel *ExtractExodusModel(
            IdTypeArray *globalCellIdList, UnstructuredGrid *grid)
        Create a new ExodusModel object representing a subset of the
           cells of this ExodusModel object.  We need a list of the
           global IDs of the cells to be extracted, the grid which
           generated the Exodus Model (so we can find the points
        associated
           with each cell), and the name of the grid's global cell ID
        array,
           and the name of the grid's global node ID array.
        """
        my_args = deref_array(args, [('vtkIdTypeArray', 'vtkUnstructuredGrid')])
        ret = self._wrap_call(self._vtk_obj.ExtractExodusModel, *my_args)
        return wrap_vtk(ret)

    def has_metadata(self, *args):
        """
        V.has_metadata(UnstructuredGrid) -> int
        C++: static int HasMetadata(UnstructuredGrid *grid)
        Static function that returns 1 if the UnstructuredGrid
          has metadata packed into it's field arrays, 0 otherwise.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasMetadata, *my_args)
        return ret

    def merge_exodus_model(self, *args):
        """
        V.merge_exodus_model(ExodusModel) -> int
        C++: int MergeExodusModel(ExodusModel *em)
        Merge the supplied ExodusModel object into this one.  It is
          assumed the two objects represent portions of the same
        distributed
          data set.  (So the list of block IDs is the same, and so on.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MergeExodusModel, *my_args)
        return ret

    def pack_exodus_model(self, *args):
        """
        V.pack_exodus_model(UnstructuredGrid)
        C++: void PackExodusModel(UnstructuredGrid *grid)
        The metadata encapsulated in a ExodusModel object can be
           written to field arrays which are then stored in the
           UnstructuredGrid itself.  pack_exodus_model creates these
           field arrays and attaches them to the supplied grid.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PackExodusModel, *my_args)
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
          exodus_model refers, add each element and node variable
          name with this call, including the name of original variable
          that yielded it's first component, and the number of
        components.
          If a variable is removed from the UGrid, remove it from
          the exodus_model.  (If this information is missing or
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
        Reset all fields to their initial value.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def set_global_information(self, *args):
        """
        V.set_global_information(int, int) -> int
        C++: int SetGlobalInformation(int fid, int compute_word_size)
        In order to write a correct Exodus file from a
          UnstructuredGrid, we need to know the global data
          which does not get represented in the UGrid.
          Initialize, with an open Exodus file, all the global
          fields of the exodus_model object.  fid is the file handle
          of the opened Exodus file.  compute_word_size is the
          size of floating point values exchanged with the
          the Exodus library.  (It's set in ex_open or ex_create.)
          The global fields are those which don't depend on
          which cells or field arrays are being read from the
          file.
        """
        ret = self._wrap_call(self._vtk_obj.SetGlobalInformation, *args)
        return ret

    def set_local_information(self, *args):
        """
        V.set_local_information(UnstructuredGrid, int, int, int, int)
            -> int
        C++: int SetLocalInformation(UnstructuredGrid *ugrid, int fid,
            int timeStep, int newGeometry, int compute_word_size)
        Set the local information in the exodus_model.  This is
         information which depends on which blocks were read in,
         and which time step was read in.
         (Example - count of cells in each block, values of global
         variables, node IDs for nodes in each node set.)
         Provide the ugrid, the time step (the first time step is 0),
         the handle of an open Exodus file, and the
         size of floating point values exchanged with the Exodus library.
         Also indicate with a 1 if the geometry has changed (new blocks
         or blocks removed) since the last call.  (When in doubt set to
        1.)
         Please call set_global_information once before calling
         set_local_information.  set_local_information may be called many
         times if different subsets of an Exodus file are read.  Each
         call replaces the previous local values.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLocalInformation, *my_args)
        return ret

    def unpack_exodus_model(self, *args):
        """
        V.unpack_exodus_model(UnstructuredGrid, int) -> int
        C++: int UnpackExodusModel(UnstructuredGrid *grid,
            int deleteIt)
        One way to initialize an exodus_model object is to use
           set_global_information, set_local_information, and the Add/Remove
           Variable calls to initialize it from an open Exodus file.
        
        
           Another way is to initialize it with the exodus_model which
           has been packed into field arrays of a UnstructuredGrid.
           Set the second argument to 1 if you would like the packed
           field arrays to be deleted after this exodus_model is
           initialized.
           Returns 1 if there is no exodus_model object associated with
           the grid, 0 otherwise.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UnpackExodusModel, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExodusModel, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExodusModel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ExodusModel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExodusModel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

