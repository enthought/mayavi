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

from tvtk.tvtk_classes.data_writer import DataWriter


class TableWriter(DataWriter):
    """
    TableWriter - write Table to a file
    
    Superclass: DataWriter
    
    TableWriter is a sink object that writes ASCII or binary Table
    data files in vtk format. See text for format details.
    
    Caveats:
    
    Binary files written on one system may not be readable on other
    systems.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableWriter, obj, update, **traits)
    
    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> Table
        C++: Table *GetInput()
        V.get_input(int) -> Table
        C++: Table *GetInput(int port)
        Get the input to this writer.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input(DataObject)
        C++: void SetInput(DataObject *input)
        V.set_input(int, DataObject)
        C++: void SetInput(int index, DataObject *input)
        Set/get the input to this writer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    _updateable_traits_ = \
    (('vectors_name', 'GetVectorsName'), ('global_ids_name',
    'GetGlobalIdsName'), ('tensors_name', 'GetTensorsName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('lookup_table_name', 'GetLookupTableName'), ('reference_count',
    'GetReferenceCount'), ('write_to_output_string',
    'GetWriteToOutputString'), ('file_name', 'GetFileName'),
    ('scalars_name', 'GetScalarsName'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('file_type',
    'GetFileType'), ('header', 'GetHeader'), ('abort_execute',
    'GetAbortExecute'), ('normals_name', 'GetNormalsName'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('t_coords_name',
    'GetTCoordsName'), ('progress', 'GetProgress'), ('field_data_name',
    'GetFieldDataName'), ('pedigree_ids_name', 'GetPedigreeIdsName'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'file_type',
    'field_data_name', 'file_name', 'global_ids_name', 'header',
    'lookup_table_name', 'normals_name', 'pedigree_ids_name',
    'progress_text', 'scalars_name', 't_coords_name', 'tensors_name',
    'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TableWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['write_to_output_string'], ['file_type'],
            ['field_data_name', 'file_name', 'global_ids_name', 'header',
            'lookup_table_name', 'normals_name', 'pedigree_ids_name',
            'scalars_name', 't_coords_name', 'tensors_name', 'vectors_name']),
            title='Edit TableWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

