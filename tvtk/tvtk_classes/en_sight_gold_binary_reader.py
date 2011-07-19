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

from tvtk.tvtk_classes.en_sight_reader import EnSightReader


class EnSightGoldBinaryReader(EnSightReader):
    """
    EnSightGoldBinaryReader - class to read binary en_sight Gold files
    
    Superclass: EnSightReader
    
    EnSightGoldBinaryReader is a class to read en_sight Gold files into
    vtk. Because the different parts of the en_sight data can be of
    various data types, this reader produces multiple outputs, one per
    part in the input file. All variable information is being stored in
    field data.  The descriptions listed in the case file are used as the
    array names in the field data. For complex vector variables, the
    description is appended with _r (for the array of real values) and _i
    (for the array if imaginary values).  Complex scalar variables are
    stored as a single array with 2 components, real and imaginary,
    listed in that order.
    
    Caveats:
    
    You must manually call Update on this reader and then connect the
    rest of the pipeline because (due to the nature of the file format)
    it is not possible to know ahead of time how many outputs you will
    have or what types they will be. This reader can only handle static
    en_sight datasets (both static geometry and variables).
    
    Thanks:
    
    Thanks to Yvan Fournier for providing the code to support nfaced
    elements.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEnSightGoldBinaryReader, obj, update, **traits)
    
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
            return super(EnSightGoldBinaryReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit EnSightGoldBinaryReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['particle_coordinates_by_index',
            'read_all_variables'], ['byte_order'], ['case_file_name', 'file_path',
            'particle_coordinates_by_index', 'time_value']),
            title='Edit EnSightGoldBinaryReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EnSightGoldBinaryReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

