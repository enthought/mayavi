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


class ClipVolume(UnstructuredGridAlgorithm):
    """
    ClipVolume - clip volume data with user-specified implicit
    function or input scalar data
    
    Superclass: UnstructuredGridAlgorithm
    
    ClipVolume is a filter that clips volume data (i.e., ImageData)
    using either: any subclass of ImplicitFunction or the input scalar
    data. The clipping operation cuts through the cells of the
    dataset--converting 3d image data into a 3d unstructured
    grid--returning everything inside of the specified implicit function
    (or greater than the scalar value). During the clipping the filter
    will produce pieces of a cell. (Compare this with ExtractGeometry
    or GeometryFilter, which produces entire, uncut cells.) The output
    of this filter is a 3d unstructured grid (e.g., tetrahedra or other
    3d cell types).
    
    To use this filter, you must decide if you will be clipping with an
    implicit function, or whether you will be using the input scalar
    data.  If you want to clip with an implicit function, you must first
    define and then set the implicit function with the set_clip_function()
    method. Otherwise, you must make sure input scalar data is available.
    You can also specify a scalar value, which is used to decide what is
    inside and outside of the implicit function. You can also reverse the
    sense of what inside/outside is by setting the inside_out instance
    variable. (The cutting algorithm proceeds by computing an implicit
    function value or using the input scalar data for each point in the
    dataset. This is compared to the scalar value to determine
    inside/outside.)
    
    This filter can be configured to compute a second output. The second
    output is the portion of the volume that is clipped away. Set the
    generate_clipped_data boolean on if you wish to access this output
    data.
    
    The filter will produce an unstructured grid of entirely tetrahedra
    or a mixed grid of tetrahedra and other 3d cell types (e.g., wedges).
    Control this behavior by setting the mixed3d_cell_generation. By
    default the mixed3d_cell_generation is on and a combination of cell
    types will be produced. Note that producing mixed cell types is a
    faster than producing only tetrahedra.
    
    Caveats:
    
    This filter is designed to function with 3d structured points.
    Clipping 2d images should be done by converting the image to
    polygonal data and using ClipPolyData,
    
    See Also:
    
    ImplicitFunction ClipPolyData GeometryFilter
    ExtractGeometry
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkClipVolume, obj, update, **traits)
    
    generate_clip_scalars = tvtk_base.false_bool_trait(help=\
        """
        If this flag is enabled, then the output scalar values will be
        interpolated from the implicit function values, and not the input
        scalar data. If you enable this flag but do not provide an
        implicit function an error will be reported.
        """
    )
    def _generate_clip_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateClipScalars,
                        self.generate_clip_scalars_)

    mixed3d_cell_generation = tvtk_base.true_bool_trait(help=\
        """
        Control whether the filter produces a mix of 3d cell types on
        output, or whether the output cells are all tetrahedra. By
        default, a mixed set of cells (e.g., tetrahedra and wedges) is
        produced. (Note: mixed type generation is faster and less overall
        data is generated.)
        """
    )
    def _mixed3d_cell_generation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMixed3DCellGeneration,
                        self.mixed3d_cell_generation_)

    generate_clipped_output = tvtk_base.false_bool_trait(help=\
        """
        Control whether a second output is generated. The second output
        contains the unstructured grid that's been clipped away.
        """
    )
    def _generate_clipped_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateClippedOutput,
                        self.generate_clipped_output_)

    inside_out = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the inside_out flag. When off, a vertex is considered
        inside the implicit function if its value is greater than the
        Value ivar. When inside_outside is turned on, a vertex is
        considered inside the implicit function if its implicit function
        value is less than or equal to the Value ivar.  inside_out is off
        by default.
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
        Set / Get a spatial locator for merging points. By default, an
        instance of MergePoints is used.
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
        Set the clipping value of the implicit function (if clipping with
        implicit function) or scalar value (if clipping with scalars).
        The default value is 0.0.
        """
    )
    def _value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValue,
                        self.value)

    merge_tolerance = traits.Trait(0.01, traits.Range(0.0001, 0.25, enter_set=True, auto_set=False), help=\
        """
        Set the tolerance for merging clip intersection points that are
        near the corners of voxels. This tolerance is used to prevent the
        generation of degenerate tetrahedra.
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
        Create default locator. Used to create one when none is
        specified. The locator is used to merge coincident points.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('merge_tolerance', 'GetMergeTolerance'), ('generate_clipped_output',
    'GetGenerateClippedOutput'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('value', 'GetValue'), ('generate_clip_scalars',
    'GetGenerateClipScalars'), ('inside_out', 'GetInsideOut'),
    ('release_data_flag', 'GetReleaseDataFlag'),
    ('mixed3d_cell_generation', 'GetMixed3DCellGeneration'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('abort_execute', 'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_clip_scalars',
    'generate_clipped_output', 'global_warning_display', 'inside_out',
    'mixed3d_cell_generation', 'release_data_flag', 'merge_tolerance',
    'progress_text', 'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ClipVolume, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ClipVolume properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_clip_scalars', 'generate_clipped_output',
            'inside_out', 'mixed3d_cell_generation'], [], ['merge_tolerance',
            'value']),
            title='Edit ClipVolume properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ClipVolume properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

