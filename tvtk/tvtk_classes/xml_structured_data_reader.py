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


class XMLStructuredDataReader(XMLDataReader):
    """
    XMLStructuredDataReader - Superclass for structured data XML
    readers.
    
    Superclass: XMLDataReader
    
    XMLStructuredDataReader provides functionality common to all
    structured data format readers.
    
    See Also:
    
    XMLImageDataReader XMLStructuredGridReader
    XMLRectilinearGridReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLStructuredDataReader, obj, update, **traits)
    
    whole_slices = tvtk_base.true_bool_trait(help=\
        """
        Get/Set whether the reader gets a whole slice from disk when only
        a rectangle inside it is needed.  This mode reads more data than
        necessary, but prevents many short reads from interacting poorly
        with the compression and encoding schemes.
        """
    )
    def _whole_slices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeSlices,
                        self.whole_slices_)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('whole_slices', 'GetWholeSlices'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('time_step_range',
    'GetTimeStepRange'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress',
    'GetProgress'), ('reference_count', 'GetReferenceCount'),
    ('time_step', 'GetTimeStep'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'whole_slices', 'file_name', 'progress_text',
    'time_step', 'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLStructuredDataReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLStructuredDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['whole_slices'], [], ['file_name', 'time_step',
            'time_step_range']),
            title='Edit XMLStructuredDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLStructuredDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

