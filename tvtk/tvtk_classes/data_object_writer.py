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

from tvtk.tvtk_classes.writer import Writer


class DataObjectWriter(Writer):
    """
    DataObjectWriter - write vtk field data
    
    Superclass: Writer
    
    DataObjectWriter is a source object that writes ASCII or binary
    field data files in vtk format. Field data is a general form of data
    in matrix form.
    
    Caveats:
    
    Binary files written on one system may not be readable on other
    systems.
    
    See Also:
    
    FieldData FieldDataReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObjectWriter, obj, update, **traits)
    
    file_type = traits.Trait('ascii',
    tvtk_base.TraitRevPrefixMap({'binary': 2, 'ascii': 1}), help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )
    def _file_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileType,
                        self.file_type_)

    field_data_name = traits.String(r"FieldData", enter_set=True, auto_set=False, help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )
    def _field_data_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDataName,
                        self.field_data_name)

    header = traits.String(r"vtk output", enter_set=True, auto_set=False, help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )
    def _header_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeader,
                        self.header)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )
    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'), ('file_type',
    'GetFileType'), ('file_name', 'GetFileName'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('header', 'GetHeader'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('field_data_name', 'GetFieldDataName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_type', 'field_data_name', 'file_name',
    'header', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataObjectWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], ['file_type'], ['field_data_name', 'file_name',
            'header']),
            title='Edit DataObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

