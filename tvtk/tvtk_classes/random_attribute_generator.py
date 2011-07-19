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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class RandomAttributeGenerator(DataSetAlgorithm):
    """
    RandomAttributeGenerator - generate and create random data
    attributes
    
    Superclass: DataSetAlgorithm
    
    RandomAttributeGenerator is a filter that creates random
    attributes including scalars, vectors, normals, tensors, texture
    coordinates and/or general data arrays. These attributes can be
    generated as point data, cell data or general field data. The
    generation of each component is normalized between a user-specified
    minimum and maximum value.
    
    This filter provides that capability to specify the data type of the
    attributes, the range for each of the components, and the number of
    components. Note, however, that this flexibility only goes so far
    because some attributes (e.g., normals, vectors and tensors) are
    fixed in the number of components, and in the case of normals and
    tensors, are constrained in the values that some of the components
    can take (i.e., normals have magnitude one, and tensors are
    symmetric).
    
    Caveats:
    
    In general this class is used for debugging or testing purposes.
    
    It is possible to generate multiple attributes simultaneously.
    
    By default, no data is generated. Make sure to enable the generation
    of some attributes if you want this filter to affect the output. Also
    note that this filter passes through input geometry, topology and
    attributes. Newly created attributes may replace attribute data that
    would have otherwise been passed through.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRandomAttributeGenerator, obj, update, **traits)
    
    generate_cell_vectors = tvtk_base.false_bool_trait(help=\
        """
        Indicate that cell vectors are to be generated. Note that the
        number of components is always equal to three.
        """
    )
    def _generate_cell_vectors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateCellVectors,
                        self.generate_cell_vectors_)

    generate_point_t_coords = tvtk_base.false_bool_trait(help=\
        """
        Indicate that point texture coordinates are to be generated. Note
        that the specified number of components is used to create the
        texture coordinates (but must range between one and three).
        """
    )
    def _generate_point_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePointTCoords,
                        self.generate_point_t_coords_)

    generate_point_normals = tvtk_base.false_bool_trait(help=\
        """
        Indicate that point normals are to be generated. Note that the
        number of components is always equal to three.
        """
    )
    def _generate_point_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePointNormals,
                        self.generate_point_normals_)

    generate_point_scalars = tvtk_base.false_bool_trait(help=\
        """
        Indicate that point scalars are to be generated. Note that the
        specified number of components is used to create the scalar.
        """
    )
    def _generate_point_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePointScalars,
                        self.generate_point_scalars_)

    generate_cell_tensors = tvtk_base.false_bool_trait(help=\
        """
        Indicate that cell tensors are to be generated. Note that the
        number of components is always equal to nine.
        """
    )
    def _generate_cell_tensors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateCellTensors,
                        self.generate_cell_tensors_)

    generate_field_array = tvtk_base.false_bool_trait(help=\
        """
        Indicate that an arbitrary field data array is to be generated.
        Note that the specified number of components is used to create
        the scalar.
        """
    )
    def _generate_field_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateFieldArray,
                        self.generate_field_array_)

    generate_cell_t_coords = tvtk_base.false_bool_trait(help=\
        """
        Indicate that cell texture coordinates are to be generated. Note
        that the specified number of components is used to create the
        texture coordinates (but must range between one and three).
        """
    )
    def _generate_cell_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateCellTCoords,
                        self.generate_cell_t_coords_)

    generate_cell_scalars = tvtk_base.false_bool_trait(help=\
        """
        Indicate that cell scalars are to be generated. Note that the
        specified number of components is used to create the scalar.
        """
    )
    def _generate_cell_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateCellScalars,
                        self.generate_cell_scalars_)

    generate_point_vectors = tvtk_base.false_bool_trait(help=\
        """
        Indicate that point vectors are to be generated. Note that the
        number of components is always equal to three.
        """
    )
    def _generate_point_vectors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePointVectors,
                        self.generate_point_vectors_)

    generate_point_tensors = tvtk_base.false_bool_trait(help=\
        """
        Indicate that point tensors are to be generated. Note that the
        number of components is always equal to nine.
        """
    )
    def _generate_point_tensors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePointTensors,
                        self.generate_point_tensors_)

    generate_cell_array = tvtk_base.false_bool_trait(help=\
        """
        Indicate that an arbitrary cell array is to be generated. Note
        that the specified number of components is used to create the
        array.
        """
    )
    def _generate_cell_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateCellArray,
                        self.generate_cell_array_)

    generate_cell_normals = tvtk_base.false_bool_trait(help=\
        """
        Indicate that cell normals are to be generated. Note that the
        number of components is always equal to three.
        """
    )
    def _generate_cell_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateCellNormals,
                        self.generate_cell_normals_)

    generate_point_array = tvtk_base.false_bool_trait(help=\
        """
        Indicate that an arbitrary point array is to be generated. Note
        that the specified number of components is used to create the
        array.
        """
    )
    def _generate_point_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePointArray,
                        self.generate_point_array_)

    data_type = traits.Trait('float',
    tvtk_base.TraitRevPrefixMap({'short': 4, 'int': 6, 'double': 11, 'float': 10, 'unsigned_long': 9, 'long': 8, 'char': 2, 'unsigned_int': 7, 'unsigned_char': 3, 'unsigned_short': 5, 'bit': 1}), help=\
        """
        Specify the type of array to create (all components of this array
        are of this type). This holds true for all arrays that are
        created.
        """
    )
    def _data_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataType,
                        self.data_type_)

    number_of_components = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of components to generate. This value only
        applies to those attribute types that take a variable number of
        components. For example, a vector is only three components so the
        number of components is not applicable; whereas a scalar may
        support multiple, varying number of components.
        """
    )
    def _number_of_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfComponents,
                        self.number_of_components)

    maximum_component_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the maximum component value. This applies to all data that is
        generated, although normals and tensors have internal constraints
        that must be observed.
        """
    )
    def _maximum_component_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumComponentValue,
                        self.maximum_component_value)

    minimum_component_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the minimum component value. This applies to all data that is
        generated, although normals and tensors have internal constraints
        that must be observed.
        """
    )
    def _minimum_component_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumComponentValue,
                        self.minimum_component_value)

    number_of_tuples = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of tuples to generate. This value only applies
        when creating general field data. In all other cases (i.e., point
        data or cell data), the number of tuples is controlled by the
        number of points and cells, respectively.
        """
    )
    def _number_of_tuples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTuples,
                        self.number_of_tuples)

    def generate_all_cell_data_off(self):
        """
        V.generate_all_cell_data_off()
        C++: void GenerateAllCellDataOff()
        Convenience methods for generating data: all data, all point
        data, or all cell data. For example, if all data is enabled, then
        all point, cell and field data is generated. If all point data is
        enabled, then point scalars, vectors, normals, tensors, tcoords,
        and a data array are produced.
        """
        ret = self._vtk_obj.GenerateAllCellDataOff()
        return ret
        

    def generate_all_cell_data_on(self):
        """
        V.generate_all_cell_data_on()
        C++: void GenerateAllCellDataOn()
        Convenience methods for generating data: all data, all point
        data, or all cell data. For example, if all data is enabled, then
        all point, cell and field data is generated. If all point data is
        enabled, then point scalars, vectors, normals, tensors, tcoords,
        and a data array are produced.
        """
        ret = self._vtk_obj.GenerateAllCellDataOn()
        return ret
        

    def generate_all_data_off(self):
        """
        V.generate_all_data_off()
        C++: void GenerateAllDataOff()
        Convenience methods for generating data: all data, all point
        data, or all cell data. For example, if all data is enabled, then
        all point, cell and field data is generated. If all point data is
        enabled, then point scalars, vectors, normals, tensors, tcoords,
        and a data array are produced.
        """
        ret = self._vtk_obj.GenerateAllDataOff()
        return ret
        

    def generate_all_data_on(self):
        """
        V.generate_all_data_on()
        C++: void GenerateAllDataOn()
        Convenience methods for generating data: all data, all point
        data, or all cell data. For example, if all data is enabled, then
        all point, cell and field data is generated. If all point data is
        enabled, then point scalars, vectors, normals, tensors, tcoords,
        and a data array are produced.
        """
        ret = self._vtk_obj.GenerateAllDataOn()
        return ret
        

    def generate_all_point_data_off(self):
        """
        V.generate_all_point_data_off()
        C++: void GenerateAllPointDataOff()
        Convenience methods for generating data: all data, all point
        data, or all cell data. For example, if all data is enabled, then
        all point, cell and field data is generated. If all point data is
        enabled, then point scalars, vectors, normals, tensors, tcoords,
        and a data array are produced.
        """
        ret = self._vtk_obj.GenerateAllPointDataOff()
        return ret
        

    def generate_all_point_data_on(self):
        """
        V.generate_all_point_data_on()
        C++: void GenerateAllPointDataOn()
        Convenience methods for generating data: all data, all point
        data, or all cell data. For example, if all data is enabled, then
        all point, cell and field data is generated. If all point data is
        enabled, then point scalars, vectors, normals, tensors, tcoords,
        and a data array are produced.
        """
        ret = self._vtk_obj.GenerateAllPointDataOn()
        return ret
        

    _updateable_traits_ = \
    (('data_type', 'GetDataType'), ('maximum_component_value',
    'GetMaximumComponentValue'), ('generate_cell_t_coords',
    'GetGenerateCellTCoords'), ('minimum_component_value',
    'GetMinimumComponentValue'), ('generate_point_vectors',
    'GetGeneratePointVectors'), ('generate_point_normals',
    'GetGeneratePointNormals'), ('generate_point_scalars',
    'GetGeneratePointScalars'), ('number_of_tuples', 'GetNumberOfTuples'),
    ('generate_cell_scalars', 'GetGenerateCellScalars'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('generate_cell_vectors', 'GetGenerateCellVectors'),
    ('generate_field_array', 'GetGenerateFieldArray'),
    ('generate_point_array', 'GetGeneratePointArray'),
    ('generate_cell_array', 'GetGenerateCellArray'),
    ('generate_point_tensors', 'GetGeneratePointTensors'), ('debug',
    'GetDebug'), ('progress_text', 'GetProgressText'),
    ('generate_point_t_coords', 'GetGeneratePointTCoords'),
    ('generate_cell_normals', 'GetGenerateCellNormals'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('number_of_components', 'GetNumberOfComponents'),
    ('generate_cell_tensors', 'GetGenerateCellTensors'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_cell_array',
    'generate_cell_normals', 'generate_cell_scalars',
    'generate_cell_t_coords', 'generate_cell_tensors',
    'generate_cell_vectors', 'generate_field_array',
    'generate_point_array', 'generate_point_normals',
    'generate_point_scalars', 'generate_point_t_coords',
    'generate_point_tensors', 'generate_point_vectors',
    'global_warning_display', 'release_data_flag', 'data_type',
    'maximum_component_value', 'minimum_component_value',
    'number_of_components', 'number_of_tuples', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RandomAttributeGenerator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit RandomAttributeGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_cell_array', 'generate_cell_normals',
            'generate_cell_scalars', 'generate_cell_t_coords',
            'generate_cell_tensors', 'generate_cell_vectors',
            'generate_field_array', 'generate_point_array',
            'generate_point_normals', 'generate_point_scalars',
            'generate_point_t_coords', 'generate_point_tensors',
            'generate_point_vectors'], ['data_type'], ['maximum_component_value',
            'minimum_component_value', 'number_of_components',
            'number_of_tuples']),
            title='Edit RandomAttributeGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RandomAttributeGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

