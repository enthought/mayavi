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

from tvtk.tvtk_classes.rectilinear_grid_source import RectilinearGridSource


class SESAMEReader(RectilinearGridSource):
    """
    SESAMEReader - read SESAME files
    
    Superclass: RectilinearGridSource
    
    SESAMEReader is a source object that reads SESAME files. Currently
    supported tables include 301, 304, 502, 503, 504, 505, 602
    
    SESAMEReader creates rectilinear grid datasets. The dimension of the
    dataset depends upon the number of densities and temperatures in the
    table. Values at certain temperatures and densities are stored as
    scalars.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSESAMEReader, obj, update, **traits)
    
    table = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the table to read in
        """
    )
    def _table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTable,
                        self.table)

    def get_table_array_status(self, *args):
        """
        V.get_table_array_status(string) -> int
        C++: int GetTableArrayStatus(const char *name)
        Set whether to read a table array
        """
        ret = self._wrap_call(self._vtk_obj.GetTableArrayStatus, *args)
        return ret

    def set_table_array_status(self, *args):
        """
        V.set_table_array_status(string, int)
        C++: void SetTableArrayStatus(const char *name, int flag)
        Set whether to read a table array
        """
        ret = self._wrap_call(self._vtk_obj.SetTableArrayStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set the filename to read
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_number_of_table_array_names(self):
        return self._vtk_obj.GetNumberOfTableArrayNames()
    number_of_table_array_names = traits.Property(_get_number_of_table_array_names, help=\
        """
        Get the number of arrays for the table to read
        """
    )

    def _get_number_of_table_arrays(self):
        return self._vtk_obj.GetNumberOfTableArrays()
    number_of_table_arrays = traits.Property(_get_number_of_table_arrays, help=\
        """
        Get the number of arrays for the table to read
        """
    )

    def _get_number_of_table_ids(self):
        return self._vtk_obj.GetNumberOfTableIds()
    number_of_table_ids = traits.Property(_get_number_of_table_ids, help=\
        """
        Get the number of tables in this file
        """
    )

    def get_table_array_name(self, *args):
        """
        V.get_table_array_name(int) -> string
        C++: const char *GetTableArrayName(int index)
        Get the names of arrays for the table to read
        """
        ret = self._wrap_call(self._vtk_obj.GetTableArrayName, *args)
        return ret

    def _get_table_ids_as_array(self):
        return wrap_vtk(self._vtk_obj.GetTableIdsAsArray())
    table_ids_as_array = traits.Property(_get_table_ids_as_array, help=\
        """
        Returns the table ids in a data array.
        """
    )

    def is_valid_file(self):
        """
        V.is_valid_file() -> int
        C++: int IsValidFile()
        Return whether this is a valid file
        """
        ret = self._vtk_obj.IsValidFile()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('file_name',
    'GetFileName'), ('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('table', 'GetTable'), ('progress_text',
    'GetProgressText'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text',
    'release_data_flag', 'table'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SESAMEReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SESAMEReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name', 'release_data_flag', 'table']),
            title='Edit SESAMEReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SESAMEReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

