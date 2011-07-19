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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class TableBasedClipDataSet(UnstructuredGridAlgorithm):
    """
    TableBasedClipDataSet - Clip any dataset with a user-specified 
    
    Superclass: UnstructuredGridAlgorithm
    
    TableBasedClipDataSet is a filter that clips any type of dataset
    using
     either any subclass of ImplicitFunction or an input scalar point
    data
     array. Clipping means that it actually "cuts" through the cells of
    the
     dataset, returning everything outside the specified implicit
    function (or
     greater than the scalar value) including "pieces" of a cell (Note to
    compare
     this with ExtractGeometry, which pulls out entire, uncut cells).
    The
     output of this filter is a UnstructuredGrid data.
    
    
     To use this filter, you need to decide whether an implicit function
    or an
     input scalar point data array is used for clipping. For the former
    case,
    1) define an implicit function
    2) provide it to this filter via set_clip_function() If a clipping
       function is not specified, or generate_clip_scalars is off( the
       default), the input scalar point data array is then employed for
       clipping.
    
    
     You can also specify a scalar (iso-)value, which is used to decide
    what is
     inside and outside the implicit function. You can also reverse the
    sense of
     what inside/outside is by setting IVAR inside_out. The clipping
    algorithm
     proceeds by computing an implicit function value or using the input
    scalar
     point data value for each point in the dataset. This is compared
    against the
     scalar (iso-)value to determine the inside/outside status.
    
    
     Although this filter sometimes (but rarely) may resort to the
    sibling class
     ClipDataSet for handling some special grids (such as cylinders or
    cones
     with capping faces in the form of a PolyData), it itself is able
    to deal
     with most grids. It is worth mentioning that
    TableBasedClipDataSet is
     capable of addressing the artifacts that may occur with
    ClipDataSet due
     to the possibly inconsistent triangulation modes between neighboring
    cells.
     In addition, the former is much faster than the latter. Furthermore,
    the
     former produces less cells (with ratio usually being 5~6) than by
    the latter
     in the output. In other words, this filter retains the original
    cells (i.e.,
     without triangulation / tetrahedralization) wherever possible. All
    these
     advantages are gained by adopting the unique clipping and
    triangulation tables
     proposed by vis_it.
    
    Caveats:
    
    
     TableBasedClipDataSet makes use of a hash table (that is provided
    by class
     maintained by internal class TableBasedClipperDataSetFromVolume)
    to achieve
     rapid removal of duplicate points. The hash-based mechanism simply
    compares the
     point Ids, without considering the actual inter-point distance
    (vtk_clip_data_set
     adopts MergePoints that though considers the inter-point distance
    for robust
     points merging ). As a result, some duplicate points may be present
    in the output.
     This problem occurs when some boundary (cut-through cells) happen to
    have faces
     EXACTLY aligned with the clipping plane (such as Plane, Box, or
    other implicit
     functions with planar shapes). The occurrence (though very rare) of
    duplicate
     points produces degenerate cells, which can be fixed by
    post-processing the
     output with a filter like CleanGrid.
    
    Thanks:
    
    
     This filter was adapted from the vis_it clipper (vtk_vis_it_clipper).
    
    See Also:
    
    
     ClipDataSet ClipVolume ClipPolyData Cutter
    ImplicitFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableBasedClipDataSet, obj, update, **traits)
    
    generate_clip_scalars = tvtk_base.false_bool_trait(help=\
        """
        Set/Get flag generate_clip_scalars, with 0 as the default value.
        With this flag on, the scalar point data values obtained by
        evaluating the implicit function will be exported to the output.
        Note that this flag requries that an implicit function be
        provided.
        """
    )
    def _generate_clip_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateClipScalars,
                        self.generate_clip_scalars_)

    generate_clipped_output = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether a second output is generated. The second output
        contains the polygonal data that is clipped away by the
        iso-surface.
        """
    )
    def _generate_clipped_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateClippedOutput,
                        self.generate_clipped_output_)

    use_value_as_offset = tvtk_base.true_bool_trait(help=\
        """
        Set/Get flag use_value_as_offset, with true as the default value.
        With this flag on, IVAR Value is used as an offset parameter to
        the implicit function. Value is used only when clipping using a
        scalar array.
        """
    )
    def _use_value_as_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseValueAsOffset,
                        self.use_value_as_offset_)

    inside_out = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the inside_out flag. With this flag off, a vertex is
        considered inside (the implicit function or the isosurface) if
        the (function or scalar) value is greater than IVAR Value. With
        this flag on, a vertex is considered inside (the implicit
        function or the isosurface) if the (function or scalar) value is
        less than or equal to IVAR Value. This flag is off by default.
        """
    )
    def _inside_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInsideOut,
                        self.inside_out_)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set/Get a point locator locator for merging duplicate points. By
        default, an instance of MergePoints is used. Note that this
        IVAR is provided in this class only because this filter may
        resort to its sibling class ClipDataSet when processing some
        special grids (such as cylinders or cones with capping faces in
        the form of a PolyData) while the latter requires a point
        locator. This filter itself does not need a locator.
        """
    )

    def _get_clip_function(self):
        return wrap_vtk(self._vtk_obj.GetClipFunction())
    def _set_clip_function(self, arg):
        old_val = self._get_clip_function()
        self._wrap_call(self._vtk_obj.SetClipFunction,
                        deref_vtk(arg))
        self.trait_property_changed('clip_function', old_val, arg)
    clip_function = traits.Property(_get_clip_function, _set_clip_function, help=\
        """
        
        """
    )

    value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the clipping value of the implicit function (if an
        implicit function is applied) or scalar data array (if a scalar
        data array is used), with 0.0 as the default value. This value is
        ignored if flag use_value_as_offset is true AND a clip function is
        defined.
        """
    )
    def _value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValue,
                        self.value)

    merge_tolerance = traits.Trait(0.01, traits.Range(0.0001, 0.25, enter_set=True, auto_set=False), help=\
        """
        Set/Get the tolerance used for merging duplicate points near the
        clipping intersection cells. This tolerance may prevent the
        generation of degenerate primitives. Note that only 3d cells
        actually use this IVAR.
        """
    )
    def _merge_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMergeTolerance,
                        self.merge_tolerance)

    def _get_clipped_output(self):
        return wrap_vtk(self._vtk_obj.GetClippedOutput())
    clipped_output = traits.Property(_get_clipped_output, help=\
        """
        Return the clipped output.
        """
    )

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create a default point locator when none is specified. The point
        locator is used to merge coincident points.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('merge_tolerance', 'GetMergeTolerance'), ('generate_clipped_output',
    'GetGenerateClippedOutput'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('value', 'GetValue'), ('generate_clip_scalars',
    'GetGenerateClipScalars'), ('inside_out', 'GetInsideOut'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('use_value_as_offset',
    'GetUseValueAsOffset'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_clip_scalars',
    'generate_clipped_output', 'global_warning_display', 'inside_out',
    'release_data_flag', 'use_value_as_offset', 'merge_tolerance',
    'progress_text', 'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableBasedClipDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TableBasedClipDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_clip_scalars', 'generate_clipped_output',
            'inside_out', 'use_value_as_offset'], [], ['merge_tolerance',
            'value']),
            title='Edit TableBasedClipDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableBasedClipDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

