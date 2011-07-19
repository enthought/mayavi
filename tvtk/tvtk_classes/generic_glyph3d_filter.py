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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class GenericGlyph3DFilter(PolyDataAlgorithm):
    """
    GenericGlyph3DFilter - copy oriented and scaled glyph geometry to
    every input point
    
    Superclass: PolyDataAlgorithm
    
    GenericGlyph3DFilter is a filter that copies a geometric
    representation (called a glyph) to every point in the input dataset.
    The glyph is defined with polygonal data from a source filter input.
    The glyph may be oriented along the input vectors or normals, and it
    may be scaled according to scalar data or vector magnitude. More than
    one glyph may be used by creating a table of source objects, each
    defining a different glyph. If a table of glyphs is defined, then the
    table can be indexed into by using either scalar value or vector
    magnitude.
    
    To use this object you'll have to provide an input dataset and a
    source to define the glyph. Then decide whether you want to scale the
    glyph and how to scale the glyph (using scalar value or vector
    magnitude). Next decide whether you want to orient the glyph, and
    whether to use the vector data or normal data to orient it. Finally,
    decide whether to use a table of glyphs, or just a single glyph. If
    you use a table of glyphs, you'll have to decide whether to index
    into it with scalar value or with vector magnitude.
    
    Caveats:
    
    Contrary to Glyph3D, the only way to specify which attributes will
    be used for scaling, coloring and orienting is through
    select_input_scalars(), select_input_vectors() and select_input_normals().
    
    The scaling of the glyphs is controlled by the scale_factor ivar
    multiplied by the scalar value at each point (if VTK_SCALE_BY_SCALAR
    is set), or multiplied by the vector magnitude (if
    VTK_SCALE_BY_VECTOR is set), Alternatively (if
    VTK_SCALE_BY_VECTORCOMPONENTS is set), the scaling may be specified
    for x,y,z using the vector components. The scale factor can be
    further controlled by enabling clamping using the Clamping ivar. If
    clamping is enabled, the scale is normalized by the Range ivar, and
    then multiplied by the scale factor. The normalization process
    includes clamping the scale value between (0,1).
    
    Typically this object operates on input data with scalar and/or
    vector data. However, scalar and/or vector aren't necessary, and it
    can be used to copy data from a single source to each point. In this
    case the scale factor can be used to uniformly scale the glyphs.
    
    The object uses "vector" data to scale glyphs, orient glyphs, and/or
    index into a table of glyphs. You can choose to use either the vector
    or normal data at each input point. Use the method
    set_vector_mode_to_use_vector() to use the vector input data, and
    set_vector_mode_to_use_normal() to use the normal input data.
    
    If you do use a table of glyphs, make sure to set the Range ivar to
    make sure the index into the glyph table is computed correctly.
    
    You can turn off scaling of the glyphs completely by using the
    Scaling ivar. You can also turn off scaling due to data (either
    vector or scalar) by using the set_scale_mode_to_data_scaling_off() method.
    
    See Also:
    
    TensorGlyph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericGlyph3DFilter, obj, update, **traits)
    
    scaling = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off scaling of source geometry.
        """
    )
    def _scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaling,
                        self.scaling_)

    generate_point_ids = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable the generation of point ids as part of the output.
        The point ids are the id of the input generating point. The point
        ids are stored in the output point field data and named
        "_input_point_ids". Point generation is useful for debugging and
        pick operations.
        """
    )
    def _generate_point_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePointIds,
                        self.generate_point_ids_)

    clamping = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off clamping of "scalar" values to range. (Scalar value
        may be
         vector magnitude if scale_by_vector() is enabled.)
        """
    )
    def _clamping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClamping,
                        self.clamping_)

    orient = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off orienting of input geometry along vector/normal.
        """
    )
    def _orient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrient,
                        self.orient_)

    color_mode = traits.Trait('color_by_scale',
    tvtk_base.TraitRevPrefixMap({'color_by_vector': 2, 'color_by_scale': 0, 'color_by_scalar': 1}), help=\
        """
        Either color by scale, scalar or by vector/normal magnitude.
        """
    )
    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    scale_mode = traits.Trait('scale_by_scalar',
    tvtk_base.TraitRevPrefixMap({'scale_by_vector': 1, 'data_scaling_off': 3, 'scale_by_vector_components': 2, 'scale_by_scalar': 0}), help=\
        """
        Either scale by scalar or by vector/normal magnitude.
        """
    )
    def _scale_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleMode,
                        self.scale_mode_)

    index_mode = traits.Trait('off',
    tvtk_base.TraitRevPrefixMap({'scalar': 1, 'vector': 2, 'off': 0}), help=\
        """
        Index into table of sources by scalar, by vector/normal
        magnitude, or no indexing. If indexing is turned off, then the
        first source glyph in the table of glyphs is used.
        """
    )
    def _index_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIndexMode,
                        self.index_mode_)

    vector_mode = traits.Trait('use_vector',
    tvtk_base.TraitRevPrefixMap({'use_vector': 0, 'vector_rotation_off': 2, 'use_normal': 1}), help=\
        """
        Specify whether to use vector or normal to perform vector
        operations.
        """
    )
    def _vector_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorMode,
                        self.vector_mode_)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource(0))
    def _set_source(self, obj):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource, deref_vtk(obj))
        self.trait_property_changed('source', old_val, obj)
    source = traits.Property(_get_source, _set_source,
                             help="The first source of this object, i.e. the result of `get_source(0)`.")
    
    def get_source(self, *args):
        """
        V.get_source(int) -> PolyData
        C++: PolyData *GetSource(int id=0)
        Get a pointer to a source object at a specified table location.
        """
        ret = self._wrap_call(self._vtk_obj.GetSource, *args)
        return wrap_vtk(ret)

    def set_source(self, *args):
        """
        V.set_source(PolyData)
        C++: void SetSource(PolyData *pd)
        V.set_source(int, PolyData)
        C++: void SetSource(int id, PolyData *pd)
        Set the source to use for the glyph.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSource, *my_args)
        return ret

    range = traits.Array(shape=(2,), value=(0.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify scale factor to scale object by.
        """
    )
    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    point_ids_name = traits.String(r"InputPointIds", enter_set=True, auto_set=False, help=\
        """
        Set/Get the name of the point_ids array if generated. By default
        the Ids are named "_input_point_ids", but this can be changed with
        this function.
        """
    )
    def _point_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointIdsName,
                        self.point_ids_name)

    def _get_input_normals_selection(self):
        return self._vtk_obj.GetInputNormalsSelection()
    input_normals_selection = traits.Property(_get_input_normals_selection, help=\
        """
        If you want to use an arbitrary normals array, then set its name
        here. By default this in NULL and the filter will use the active
        normal array.
        """
    )

    def _get_input_scalars_selection(self):
        return self._vtk_obj.GetInputScalarsSelection()
    input_scalars_selection = traits.Property(_get_input_scalars_selection, help=\
        """
        If you want to use an arbitrary scalars array, then set its name
        here. By default this in NULL and the filter will use the active
        scalar array.
        """
    )

    def _get_input_vectors_selection(self):
        return self._vtk_obj.GetInputVectorsSelection()
    input_vectors_selection = traits.Property(_get_input_vectors_selection, help=\
        """
        If you want to use an arbitrary vectors array, then set its name
        here. By default this in NULL and the filter will use the active
        vector array.
        """
    )

    def select_input_normals(self, *args):
        """
        V.select_input_normals(string)
        C++: void SelectInputNormals(const char *fieldName)
        If you want to use an arbitrary normals array, then set its name
        here. By default this in NULL and the filter will use the active
        normal array.
        """
        ret = self._wrap_call(self._vtk_obj.SelectInputNormals, *args)
        return ret

    def select_input_scalars(self, *args):
        """
        V.select_input_scalars(string)
        C++: void SelectInputScalars(const char *fieldName)
        If you want to use an arbitrary scalars array, then set its name
        here. By default this in NULL and the filter will use the active
        scalar array.
        """
        ret = self._wrap_call(self._vtk_obj.SelectInputScalars, *args)
        return ret

    def select_input_vectors(self, *args):
        """
        V.select_input_vectors(string)
        C++: void SelectInputVectors(const char *fieldName)
        If you want to use an arbitrary vectors array, then set its name
        here. By default this in NULL and the filter will use the active
        vector array.
        """
        ret = self._wrap_call(self._vtk_obj.SelectInputVectors, *args)
        return ret

    _updateable_traits_ = \
    (('color_mode', 'GetColorMode'), ('scale_factor', 'GetScaleFactor'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('generate_point_ids', 'GetGeneratePointIds'), ('scale_mode',
    'GetScaleMode'), ('progress_text', 'GetProgressText'),
    ('point_ids_name', 'GetPointIdsName'), ('scaling', 'GetScaling'),
    ('debug', 'GetDebug'), ('range', 'GetRange'), ('abort_execute',
    'GetAbortExecute'), ('index_mode', 'GetIndexMode'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('vector_mode',
    'GetVectorMode'), ('clamping', 'GetClamping'), ('orient',
    'GetOrient'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clamping', 'debug', 'generate_point_ids',
    'global_warning_display', 'orient', 'release_data_flag', 'scaling',
    'color_mode', 'index_mode', 'scale_mode', 'vector_mode',
    'point_ids_name', 'progress_text', 'range', 'scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericGlyph3DFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericGlyph3DFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clamping', 'generate_point_ids', 'orient',
            'scaling'], ['color_mode', 'index_mode', 'scale_mode', 'vector_mode'],
            ['point_ids_name', 'range', 'scale_factor']),
            title='Edit GenericGlyph3DFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericGlyph3DFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

