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

from tvtk.tvtk_classes.xml_poly_data_reader import XMLPolyDataReader


class RTXMLPolyDataReader(XMLPolyDataReader):
    """
    RTXMLPolyDataReader - Read real_time VTK XML poly_data files.
    
    Superclass: XMLPolyDataReader
    
    RTXMLPolyDataReader reads the VTK XML poly_data file format in real
    time.
    
    See Also:
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRTXMLPolyDataReader, obj, update, **traits)
    
    def _get_data_location(self):
        return self._vtk_obj.GetDataLocation()
    data_location = traits.Property(_get_data_location, help=\
        """
        
        """
    )

    def _get_next_file_name(self):
        return self._vtk_obj.GetNextFileName()
    next_file_name = traits.Property(_get_next_file_name, help=\
        """
        Return the name of the next available data file assume
        new_data_available() return VTK_OK
        """
    )

    def new_data_available(self):
        """
        V.new_data_available() -> int
        C++: virtual int NewDataAvailable()
        check if there is new data file available in the given
        data_location
        """
        ret = self._vtk_obj.NewDataAvailable()
        return ret
        

    def reset_reader(self):
        """
        V.reset_reader()
        C++: virtual void ResetReader()
        reset_reader check the data directory specified in
        this->_data_location, and reset the Internal data structure
        specifically: this->_internal->_processed_file_list for monitoring
        the arriving new data files if set_data_location(char*) is set by
        the user, this reset_reader() should also be invoked.
        """
        ret = self._vtk_obj.ResetReader()
        return ret
        

    def set_location(self, *args):
        """
        V.set_location(string)
        C++: void SetLocation(const char *dataLocation)"""
        ret = self._wrap_call(self._vtk_obj.SetLocation, *args)
        return ret

    def update_to_next_file(self):
        """
        V.update_to_next_file()
        C++: virtual void UpdateToNextFile()
        Reader will read in the next available data file The filename is
        this->_next_file_name maintained internally
        """
        ret = self._vtk_obj.UpdateToNextFile()
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
            return super(RTXMLPolyDataReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RTXMLPolyDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name', 'time_step', 'time_step_range']),
            title='Edit RTXMLPolyDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RTXMLPolyDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

