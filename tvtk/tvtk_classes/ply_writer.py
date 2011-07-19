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

from tvtk.tvtk_classes.poly_data_writer import PolyDataWriter


class PLYWriter(PolyDataWriter):
    """
    PLYWriter - write Stanford PLY file format
    
    Superclass: PolyDataWriter
    
    PLYWriter writes polygonal data in Stanford University PLY format
    (see http://graphics.stanford.edu/data/_3dscanrep/). The data can be
    written in either binary (little or big endian) or ASCII
    representation. As for point_data and cell_data, PLYWriter cannot
    handle normals or vectors. It only handles RGB point_data and
    cell_data. You need to set the name of the array (using set_name for
    the array and set_array_name for the writer). If the array is not a
    UnsignedCharArray with 3 components, you need to specify a
    LookupTable to map the scalars to RGB.
    
    Caveats:
    
    PLY does not handle big endian versus little endian correctly.
    
    See Also:
    
    PLYReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPLYWriter, obj, update, **traits)
    
    color_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'uniform_cell_color': 1, 'off': 4, 'uniform_color': 3, 'uniform_point_color': 2}), help=\
        """
        These methods enable the user to control how to add color into
        the PLY output file. The default behavior is as follows. The user
        provides the name of an array and a component number. If the type
        of the array is three components, unsigned char, then the data is
        written as three separate "red", "green" and "blue" properties.
        If the type is not unsigned char, and a lookup table is provided,
        then the array/component are mapped through the table to generate
        three separate "red", "green" and "blue" properties in the PLY
        file. The user can also set the color_mode to specify a uniform
        color for the whole part (on a vertex colors, face colors, or
        both. (Note: vertex colors or cell colors may be written,
        depending on where the named array is found. If points and cells
        have the arrays with the same name, then both colors will be
        written.)
        """
    )
    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    data_byte_order = traits.Trait('little_endian',
    tvtk_base.TraitRevPrefixMap({'big_endian': 1, 'little_endian': 0}), help=\
        """
        If the file type is binary, then the user can specify which byte
        order to use (little versus big endian).
        """
    )
    def _data_byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataByteOrder,
                        self.data_byte_order_)

    color = tvtk_base.vtk_color_trait((255, 255, 255), help=\
        """
        
        """
    )
    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, False)

    array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the array name to use to color the data.
        """
    )
    def _array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayName,
                        self.array_name)

    component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the array component to use to color the data.
        """
    )
    def _component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponent,
                        self.component)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        A lookup table can be specified in order to convert data arrays
        to RGBA colors.
        """
    )

    _updateable_traits_ = \
    (('vectors_name', 'GetVectorsName'), ('tensors_name',
    'GetTensorsName'), ('color', 'GetColor'), ('file_name',
    'GetFileName'), ('scalars_name', 'GetScalarsName'), ('component',
    'GetComponent'), ('header', 'GetHeader'), ('color_mode',
    'GetColorMode'), ('normals_name', 'GetNormalsName'),
    ('data_byte_order', 'GetDataByteOrder'), ('t_coords_name',
    'GetTCoordsName'), ('field_data_name', 'GetFieldDataName'),
    ('array_name', 'GetArrayName'), ('global_ids_name',
    'GetGlobalIdsName'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('lookup_table_name',
    'GetLookupTableName'), ('write_to_output_string',
    'GetWriteToOutputString'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('pedigree_ids_name', 'GetPedigreeIdsName'),
    ('file_type', 'GetFileType'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'color_mode',
    'data_byte_order', 'file_type', 'array_name', 'color', 'component',
    'field_data_name', 'file_name', 'global_ids_name', 'header',
    'lookup_table_name', 'normals_name', 'pedigree_ids_name',
    'progress_text', 'scalars_name', 't_coords_name', 'tensors_name',
    'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PLYWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PLYWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['write_to_output_string'], ['color_mode',
            'data_byte_order', 'file_type'], ['array_name', 'color', 'component',
            'field_data_name', 'file_name', 'global_ids_name', 'header',
            'lookup_table_name', 'normals_name', 'pedigree_ids_name',
            'scalars_name', 't_coords_name', 'tensors_name', 'vectors_name']),
            title='Edit PLYWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PLYWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

