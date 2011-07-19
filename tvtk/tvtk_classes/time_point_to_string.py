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


class TimePointToString(DataObjectAlgorithm):
    """
    TimePointToString - Converts a timestamp array to a string array
    
    Superclass: DataObjectAlgorithm
    
    TimePointToString is a filter for converting a timestamp array
    into string array using one of the formats defined in
    TimePointUtility.h.
    
    Use set_input_array_to_process to indicate the array to process. This
    array must be an unsigned 64-bit integer array for DATETIME formats,
    and may be either an unsigned 32-bit or unsigned 64-bit array for
    DATE and TIME formats.
    
    If the new array name is not specified, the array name will be the
    old name appended by " [to string]".
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTimePointToString, obj, update, **traits)
    
    output_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the output array. If this is not specified, the name
        will be the input array name with " [to string]" appended to it.
        """
    )
    def _output_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputArrayName,
                        self.output_array_name)

    iso8601_format = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The format to use when converting the timestamp to a string.
        """
    )
    def _iso8601_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetISO8601Format,
                        self.iso8601_format)

    _updateable_traits_ = \
    (('output_array_name', 'GetOutputArrayName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('iso8601_format',
    'GetISO8601Format'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'iso8601_format', 'output_array_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TimePointToString, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TimePointToString properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['iso8601_format', 'output_array_name']),
            title='Edit TimePointToString properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TimePointToString properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

