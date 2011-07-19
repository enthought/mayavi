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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class NetCDFReader(DataObjectAlgorithm):
    """
    NetCDFReader
    
    Superclass: DataObjectAlgorithm
    
    A superclass for reading net_cdf files.  Subclass add conventions to
    the reader.  This class just outputs data into a multi block data set
    with a ImageData at each block.  A block is created for each
    variable except that variables with matching dimensions will be
    placed in the same block.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNetCDFReader, obj, update, **traits)
    
    replace_fill_value_with_nan = tvtk_base.false_bool_trait(help=\
        """
        If on, any float or double variable read that has a _fill_value
        attribute will have that fill value replaced with a not-a-number
        (_na_n) value.  The advantage of setting these to na_n values is
        that, if implemented properly by the system and careful math
        operations are used, they can implicitly be ignored by
        calculations like finding the range of the values.  That said,
        this option should be used with caution as VTK does not fully
        support na_n values and therefore odd calculations may occur.  By
        default this is off.
        """
    )
    def _replace_fill_value_with_nan_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplaceFillValueWithNan,
                        self.replace_fill_value_with_nan_)

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

    def _get_all_dimensions(self):
        return wrap_vtk(self._vtk_obj.GetAllDimensions())
    all_dimensions = traits.Property(_get_all_dimensions, help=\
        """
        Returns an array with string encodings for the dimension
        combinations used in the variables.  The result is the same as
        get_variable_dimensions except that each entry in the array is
        unique (a set of dimensions is only given once even if it occurs
        for multiple variables) and the order is meaningless.
        """
    )

    def _get_all_variable_array_names(self):
        return wrap_vtk(self._vtk_obj.GetAllVariableArrayNames())
    all_variable_array_names = traits.Property(_get_all_variable_array_names, help=\
        """
        Convenience method to get a list of variable arrays.  The length
        of the returned list is the same as get_number_of_variable_arrays,
        and the string at each index i is the same as returned from
        get_variable_arrayname(i).
        """
    )

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

    def _get_variable_dimensions(self):
        return wrap_vtk(self._vtk_obj.GetVariableDimensions())
    variable_dimensions = traits.Property(_get_variable_dimensions, help=\
        """
        Returns an array with string encodings for the dimensions used in
        each of the variables.  The indices in the returned array
        correspond to those used in the get_variable_array_name method.  Two
        arrays with the same dimensions will have the same encoded string
        returned by this method.
        """
    )

    def set_dimensions(self, *args):
        """
        V.set_dimensions(string)
        C++: virtual void SetDimensions(const char *dimensions)
        Loads the grid with the given dimensions.  The dimensions are
        encoded in a string that conforms to the same format as returned
        by get_variable_dimensions and get_all_dimensions.  This method is
        really a convenience method for set_variable_array_status.  It turns
        on all variables that have the given dimensions and turns off all
        other variables.
        """
        ret = self._wrap_call(self._vtk_obj.SetDimensions, *args)
        return ret

    def update_meta_data(self):
        """
        V.update_meta_data() -> int
        C++: int UpdateMetaData()
        Update the meta data from the current file.  Automatically called
        during the request_information pipeline update stage.
        """
        ret = self._vtk_obj.UpdateMetaData()
        return ret
        

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress_text', 'GetProgressText'), ('debug',
    'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('replace_fill_value_with_nan', 'GetReplaceFillValueWithNan'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'replace_fill_value_with_nan', 'file_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(NetCDFReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit NetCDFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['replace_fill_value_with_nan'], [], ['file_name']),
            title='Edit NetCDFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NetCDFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

