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

from tvtk.tvtk_classes.generic_en_sight_reader import GenericEnSightReader


class EnSightReader(GenericEnSightReader):
    """
    EnSightReader - superclass for en_sight file readers
    
    Superclass: GenericEnSightReader
    
    
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEnSightReader, obj, update, **traits)
    
    particle_coordinates_by_index = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The measured_geometry_file should list particle coordinates from
        0->N-1. If a file is loaded where point Ids are listed from 1-N
        the Id to points reference will be wrong and the data will be
        generated incorrectly. Setting particle_coordinates_by_index to true
        will force all Id's to increment from 0->N-1 (relative to their
        order in the file) and regardless of the actual Id of of the
        point. Warning, if the Points are listed in non sequential order
        then setting this flag will reorder them.
        """
    )
    def _particle_coordinates_by_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetParticleCoordinatesByIndex,
                        self.particle_coordinates_by_index)

    def _get_match_file_name(self):
        return self._vtk_obj.GetMatchFileName()
    match_file_name = traits.Property(_get_match_file_name, help=\
        """
        Get the Match file name. Made public to allow access from apps
        requiring detailed info about the Data contents
        """
    )

    def _get_measured_file_name(self):
        return self._vtk_obj.GetMeasuredFileName()
    measured_file_name = traits.Property(_get_measured_file_name, help=\
        """
        Get the Measured file name. Made public to allow access from apps
        requiring detailed info about the Data contents
        """
    )

    _updateable_traits_ = \
    (('byte_order', 'GetByteOrder'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('abort_execute', 'GetAbortExecute'),
    ('progress_text', 'GetProgressText'), ('case_file_name',
    'GetCaseFileName'), ('debug', 'GetDebug'), ('time_value',
    'GetTimeValue'), ('read_all_variables', 'GetReadAllVariables'),
    ('particle_coordinates_by_index', 'GetParticleCoordinatesByIndex'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('file_path',
    'GetFilePath'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'particle_coordinates_by_index', 'read_all_variables',
    'release_data_flag', 'byte_order', 'case_file_name', 'file_path',
    'particle_coordinates_by_index', 'progress_text', 'time_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EnSightReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit EnSightReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['particle_coordinates_by_index',
            'read_all_variables'], ['byte_order'], ['case_file_name', 'file_path',
            'particle_coordinates_by_index', 'time_value']),
            title='Edit EnSightReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EnSightReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

