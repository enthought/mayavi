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


class ExtractTensorComponents(DataSetAlgorithm):
    """
    ExtractTensorComponents - extract parts of tensor and create a
    scalar, vector, normal, or texture coordinates.
    
    Superclass: DataSetAlgorithm
    
    ExtractTensorComponents is a filter that extracts components of a
    tensor to create a scalar, vector, normal, or texture coords. For
    example, if the tensor contains components of stress, then you could
    extract the normal stress in the x-direction as a scalar (i.e.,
    tensor component (0,0).
    
    To use this filter, you must set some boolean flags to control which
    data is extracted from the tensors, and whether you want to pass the
    tensor data through to the output. Also, you must specify the tensor
    component(s) for each type of data you want to extract. The tensor
    component(s) is(are) specified using matrix notation into a 3x3
    matrix. That is, use the (row,column) address to specify a particular
    tensor component; and if the data you are extracting requires more
    than one component, use a list of addresses. (Note that the addresses
    are 0-offset -> (0,0) specifies upper left corner of the tensor.)
    
    There are two optional methods to extract scalar data. You can
    extract the determinant of the tensor, or you can extract the
    effective stress of the tensor. These require that the ivar
    extract_scalars is on, and the appropriate scalar extraction mode is
    set.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractTensorComponents, obj, update, **traits)
    
    extract_vectors = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether vector data is extracted from tensor.
        """
    )
    def _extract_vectors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractVectors,
                        self.extract_vectors_)

    normalize_normals = tvtk_base.true_bool_trait(help=\
        """
        Boolean controls whether normal vector is converted to unit
        normal after extraction.
        """
    )
    def _normalize_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizeNormals,
                        self.normalize_normals_)

    pass_tensors_to_output = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether tensor data is passed through to output.
        """
    )
    def _pass_tensors_to_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassTensorsToOutput,
                        self.pass_tensors_to_output_)

    extract_normals = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether normal data is extracted from tensor.
        """
    )
    def _extract_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractNormals,
                        self.extract_normals_)

    extract_t_coords = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether texture coordinates are extracted from
        tensor.
        """
    )
    def _extract_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractTCoords,
                        self.extract_t_coords_)

    extract_scalars = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether scalar data is extracted from tensor.
        """
    )
    def _extract_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractScalars,
                        self.extract_scalars_)

    scalar_mode = traits.Trait('component',
    tvtk_base.TraitRevPrefixMap({'determinant': 2, 'component': 0, 'effective_stress': 1}), help=\
        """
        Specify how to extract the scalar. You can extract it as one of
        the components of the tensor, as effective stress, or as the
        determinant of the tensor. If you extract a component make sure
        that you set the scalar_components ivar.
        """
    )
    def _scalar_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarMode,
                        self.scalar_mode_)

    scalar_components = traits.Array(shape=(2,), value=(0, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _scalar_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarComponents,
                        self.scalar_components)

    vector_components = traits.Array(shape=(6,), value=(0, 0, 1, 0, 2, 0), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _vector_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorComponents,
                        self.vector_components)

    t_coord_components = traits.Array(shape=(6,), value=(0, 2, 1, 2, 2, 2), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _t_coord_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTCoordComponents,
                        self.t_coord_components)

    normal_components = traits.Array(shape=(6,), value=(0, 1, 1, 1, 2, 1), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _normal_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalComponents,
                        self.normal_components)

    number_of_t_coords = traits.Trait(2, traits.Range(1, 3, enter_set=True, auto_set=False), help=\
        """
        Set the dimension of the texture coordinates to extract.
        """
    )
    def _number_of_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTCoords,
                        self.number_of_t_coords)

    def scalar_is_component(self):
        """
        V.scalar_is_component()
        C++: void ScalarIsComponent()
        Specify how to extract the scalar. You can extract it as one of
        the components of the tensor, as effective stress, or as the
        determinant of the tensor. If you extract a component make sure
        that you set the scalar_components ivar.
        """
        ret = self._vtk_obj.ScalarIsComponent()
        return ret
        

    def scalar_is_determinant(self):
        """
        V.scalar_is_determinant()
        C++: void ScalarIsDeterminant()
        Specify how to extract the scalar. You can extract it as one of
        the components of the tensor, as effective stress, or as the
        determinant of the tensor. If you extract a component make sure
        that you set the scalar_components ivar.
        """
        ret = self._vtk_obj.ScalarIsDeterminant()
        return ret
        

    def scalar_is_effective_stress(self):
        """
        V.scalar_is_effective_stress()
        C++: void ScalarIsEffectiveStress()
        Specify how to extract the scalar. You can extract it as one of
        the components of the tensor, as effective stress, or as the
        determinant of the tensor. If you extract a component make sure
        that you set the scalar_components ivar.
        """
        ret = self._vtk_obj.ScalarIsEffectiveStress()
        return ret
        

    _updateable_traits_ = \
    (('t_coord_components', 'GetTCoordComponents'), ('extract_scalars',
    'GetExtractScalars'), ('extract_normals', 'GetExtractNormals'),
    ('extract_t_coords', 'GetExtractTCoords'), ('extract_vectors',
    'GetExtractVectors'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('vector_components', 'GetVectorComponents'),
    ('number_of_t_coords', 'GetNumberOfTCoords'), ('normal_components',
    'GetNormalComponents'), ('abort_execute', 'GetAbortExecute'),
    ('scalar_mode', 'GetScalarMode'), ('scalar_components',
    'GetScalarComponents'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('normalize_normals', 'GetNormalizeNormals'),
    ('pass_tensors_to_output', 'GetPassTensorsToOutput'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'extract_normals', 'extract_scalars',
    'extract_t_coords', 'extract_vectors', 'global_warning_display',
    'normalize_normals', 'pass_tensors_to_output', 'release_data_flag',
    'scalar_mode', 'normal_components', 'number_of_t_coords',
    'progress_text', 'scalar_components', 't_coord_components',
    'vector_components'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractTensorComponents, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractTensorComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['extract_normals', 'extract_scalars',
            'extract_t_coords', 'extract_vectors', 'normalize_normals',
            'pass_tensors_to_output'], ['scalar_mode'], ['normal_components',
            'number_of_t_coords', 'scalar_components', 't_coord_components',
            'vector_components']),
            title='Edit ExtractTensorComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractTensorComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

