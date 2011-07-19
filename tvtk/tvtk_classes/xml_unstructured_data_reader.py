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

from tvtk.tvtk_classes.xml_data_reader import XMLDataReader


class XMLUnstructuredDataReader(XMLDataReader):
    """
    XMLUnstructuredDataReader - Superclass for unstructured data XML
    readers.
    
    Superclass: XMLDataReader
    
    XMLUnstructuredDataReader provides functionality common to all
    unstructured data format readers.
    
    See Also:
    
    XMLPolyDataReader XMLUnstructuredGridReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLUnstructuredDataReader, obj, update, **traits)
    
    def setup_update_extent(self, *args):
        """
        V.setup_update_extent(int, int, int)
        C++: void SetupUpdateExtent(int piece, int numberOfPieces,
            int ghostLevel)
        Setup the reader as if the given update extent were requested by
        its output.  This can be used after an update_information to
        validate get_number_of_points() and get_number_of_cells() without
        actually reading data.
        """
        ret = self._wrap_call(self._vtk_obj.SetupUpdateExtent, *args)
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
            return super(XMLUnstructuredDataReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLUnstructuredDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['file_name', 'time_step', 'time_step_range']),
            title='Edit XMLUnstructuredDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLUnstructuredDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

