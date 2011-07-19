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

from tvtk.tvtk_classes.rectilinear_grid_algorithm import RectilinearGridAlgorithm


class NetCDFPOPReader(RectilinearGridAlgorithm):
    """
    NetCDFPOPReader - read net_cdf files
    
    Superclass: RectilinearGridAlgorithm
    
    NetCDFPOPReader is a source object that reads net_cdf files. It
    should be able to read most any net_cdf file that wants to output a
    rectilinear grid.  The ordering of the variables is changed such that
    the net_cdf x, y, z directions correspond to the RectilinearGrid z,
    y, x directions, respectively.  The striding is done with respect to
    the RectilinearGrid ordering.  Additionally, the z coordinates of
    the RectilinearGrid are negated so that the first slice/plane has
    the highest z-value and the last slice/plane has the lowest z-value.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNetCDFPOPReader, obj, update, **traits)
    
    stride = traits.Array(shape=(3,), value=(1, 1, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _stride_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStride,
                        self.stride)

    def get_variable_array_status(self, *args):
        """
        V.get_variable_array_status(string) -> int
        C++: virtual int GetVariableArrayStatus(const char *name)
        Variable array selection.
        """
        ret = self._wrap_call(self._vtk_obj.GetVariableArrayStatus, *args)
        return ret

    def set_variable_array_status(self, *args):
        """
        V.set_variable_array_status(string, int)
        C++: virtual void SetVariableArrayStatus(const char *name,
            int status)
        Variable array selection.
        """
        ret = self._wrap_call(self._vtk_obj.SetVariableArrayStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_number_of_variable_arrays(self):
        return self._vtk_obj.GetNumberOfVariableArrays()
    number_of_variable_arrays = traits.Property(_get_number_of_variable_arrays, help=\
        """
        Variable array selection.
        """
    )

    def get_variable_array_name(self, *args):
        """
        V.get_variable_array_name(int) -> string
        C++: virtual const char *GetVariableArrayName(int idx)
        Variable array selection.
        """
        ret = self._wrap_call(self._vtk_obj.GetVariableArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('stride', 'GetStride'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text', 'stride'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(NetCDFPOPReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit NetCDFPOPReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name', 'stride']),
            title='Edit NetCDFPOPReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NetCDFPOPReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

