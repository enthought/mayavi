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


class XMLReader(Algorithm):
    """
    XMLReader - Superclass for VTK's XML format readers.
    
    Superclass: Algorithm
    
    XMLReader uses XMLDataParser to parse a VTK XML input file.
    Concrete subclasses then traverse the parsed file structure and
    extract data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLReader, obj, update, **traits)
    
    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Which time_step to read.
        """
    )
    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

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

    time_step_range = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _time_step_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepRange,
                        self.time_step_range)

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

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get/Set the name of the input file.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

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

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        Get the number of point or cell arrays available in the input.
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        Get the number of point or cell arrays available in the input.
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        
        """
    )

    def _get_output_as_data_set(self):
        return wrap_vtk(self._vtk_obj.GetOutputAsDataSet())
    output_as_data_set = traits.Property(_get_output_as_data_set, help=\
        """
        Get the output as a DataSet pointer.
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

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: virtual int CanReadFile(const char *name)
        Test whether the file with the given name can be read by this
        reader.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def copy_output_information(self, *args):
        """
        V.copy_output_information(Information, int)
        C++: virtual void CopyOutputInformation(Information *outInfo,
            int port)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyOutputInformation, *my_args)
        return ret

    _updateable_traits_ = \
    (('file_name', 'GetFileName'), ('time_step_range',
    'GetTimeStepRange'), ('abort_execute', 'GetAbortExecute'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('time_step',
    'GetTimeStep'), ('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text', 'time_step',
    'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name', 'time_step', 'time_step_range']),
            title='Edit XMLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

