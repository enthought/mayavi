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


class MPASReader(UnstructuredGridAlgorithm):
    """
    MPASReader - Read an MPAS net_cfd file
    
    Superclass: UnstructuredGridAlgorithm
    
    This program reads an MPAS net_cdf data file to allow paraview to
    display a dual-grid sphere. The variables that have time dim are
    available to para_view.
    
    Assume all variables are of interest if they have dims (Time,
    n_cells|n_vertices, n_vert_levels, [n_tracers]) Converts variable data
    type from double to float. Assume no more than 100 vars each for cell
    and point data Displays tracer vars as tracer1, tracer2, etc. Does
    not deal with edge data.
    
    Christine Ahrens 8/9/2010 Version 1.2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMPASReader, obj, update, **traits)
    
    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *name)
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(string, int)
        C++: void SetPointArrayStatus(const char *name, int status)
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(string) -> int
        C++: int GetCellArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(string, int)
        C++: void SetCellArrayStatus(const char *name, int status)"""
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of MPAS data file to read.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int) -> string
        C++: const char *GetCellArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        
        """
    )

    def _get_number_of_dual_cells(self):
        return self._vtk_obj.GetNumberOfDualCells()
    number_of_dual_cells = traits.Property(_get_number_of_dual_cells, help=\
        """
        Get the number of data cells
        """
    )

    def _get_number_of_dual_points(self):
        return self._vtk_obj.GetNumberOfDualPoints()
    number_of_dual_points = traits.Property(_get_number_of_dual_points, help=\
        """
        Get the number of points
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
    )

    def _get_number_of_variables(self):
        return self._vtk_obj.GetNumberOfVariables()
    number_of_variables = traits.Property(_get_number_of_variables, help=\
        """
        Get the number of data variables at the cell centers and points
        """
    )

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int index)
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
        return ret

    def _get_vertical_level_range(self):
        return self._vtk_obj.GetVerticalLevelRange()
    vertical_level_range = traits.Property(_get_vertical_level_range, help=\
        """
        
        """
    )

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: static int CanReadFile(const char *filename)
        Returns true if the given file can be read.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def disable_all_cell_arrays(self):
        """
        V.disable_all_cell_arrays()
        C++: void DisableAllCellArrays()"""
        ret = self._vtk_obj.DisableAllCellArrays()
        return ret
        

    def disable_all_point_arrays(self):
        """
        V.disable_all_point_arrays()
        C++: void DisableAllPointArrays()
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._vtk_obj.DisableAllPointArrays()
        return ret
        

    def enable_all_cell_arrays(self):
        """
        V.enable_all_cell_arrays()
        C++: void EnableAllCellArrays()"""
        ret = self._vtk_obj.EnableAllCellArrays()
        return ret
        

    def enable_all_point_arrays(self):
        """
        V.enable_all_point_arrays()
        C++: void EnableAllPointArrays()
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._vtk_obj.EnableAllPointArrays()
        return ret
        

    def set_vertical_level(self, *args):
        """
        V.set_vertical_level(int)
        C++: void SetVerticalLevel(int level)"""
        ret = self._wrap_call(self._vtk_obj.SetVerticalLevel, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MPASReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MPASReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name']),
            title='Edit MPASReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MPASReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

