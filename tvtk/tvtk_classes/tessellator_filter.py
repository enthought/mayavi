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


class TessellatorFilter(UnstructuredGridAlgorithm):
    """
    TessellatorFilter - approximate nonlinear FEM elements with
    simplices
    
    Superclass: UnstructuredGridAlgorithm
    
    This class approximates nonlinear FEM elements with linear simplices.
    
    Warning: This class is temporary and will go away at some point after
    para_view 1.4.0.
    
    This filter rifles through all the cells in an input DataSet. It
    tesselates each cell and uses the StreamingTessellator and
    DataSetEdgeSubdivisionCriterion classes to generate simplices that
    approximate the nonlinear mesh using some approximation metric
    (encoded in the particular
    DataSetEdgeSubdivisionCriterion::EvaluateEdge implementation). The
    simplices are placed into the filter's output DataSet object by
    the callback routines add_a_tetrahedron, add_a_triangle, and add_a_line,
    which are registered with the triangulator.
    
    The output mesh will have geometry and any fields specified as
    attributes in the input mesh's point data.  The attribute's copy
    flags are honored, except for normals.
    
    Internals:
    
    The filter's main member function is request_data(). This function
    first calls setup_output() which allocates arrays and some temporary
    variables for the primitive callbacks (_output_triangle and output_line
    which are called by add_a_triangle and add_a_line, respectively).  Each
    cell is given an initial tesselation, which results in one or more
    calls to output_tetrahedron, output_triangle or output_line to add
    elements to the output_mesh. Finally, Teardown() is called to free the
    filter's working space.
    
    See Also:
    
    DataSetToUnstructuredGridFilter DataSet StreamingTessellator
    DataSetEdgeSubdivisionCriterion
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTessellatorFilter, obj, update, **traits)
    
    merge_points = tvtk_base.true_bool_trait(help=\
        """
        The adaptive tessellation will output vertices that are not
        shared among cells, even where they should be. This can be
        corrected to some extents with a MergeFilter. By default, the
        filter is off and vertices will not be shared.
        """
    )
    def _merge_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMergePoints,
                        self.merge_points_)

    def _get_subdivider(self):
        return wrap_vtk(self._vtk_obj.GetSubdivider())
    def _set_subdivider(self, arg):
        old_val = self._get_subdivider()
        self._wrap_call(self._vtk_obj.SetSubdivider,
                        deref_vtk(arg))
        self.trait_property_changed('subdivider', old_val, arg)
    subdivider = traits.Property(_get_subdivider, _set_subdivider, help=\
        """
        
        """
    )

    def _get_tessellator(self):
        return wrap_vtk(self._vtk_obj.GetTessellator())
    def _set_tessellator(self, arg):
        old_val = self._get_tessellator()
        self._wrap_call(self._vtk_obj.SetTessellator,
                        deref_vtk(arg))
        self.trait_property_changed('tessellator', old_val, arg)
    tessellator = traits.Property(_get_tessellator, _set_tessellator, help=\
        """
        
        """
    )

    output_dimension = traits.Trait(3, traits.Range(1, 3, enter_set=True, auto_set=False), help=\
        """
        Set the dimension of the output tessellation. Cells in dimensions
        higher than the given value will have their boundaries of
        dimension output_dimension tessellated. For example, if
        output_dimension is 2, a hexahedron's quadrilateral faces would be
        tessellated rather than its interior.
        """
    )
    def _output_dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputDimension,
                        self.output_dimension)

    chord_error = traits.Float(0.001, enter_set=True, auto_set=False, help=\
        """
        These are convenience routines for setting properties maintained
        by the tessellator and subdivider. They are implemented here for
        para_view's sake.
        """
    )
    def _chord_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetChordError,
                        self.chord_error)

    maximum_number_of_subdivisions = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        These are convenience routines for setting properties maintained
        by the tessellator and subdivider. They are implemented here for
        para_view's sake.
        """
    )
    def _maximum_number_of_subdivisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfSubdivisions,
                        self.maximum_number_of_subdivisions)

    def reset_field_criteria(self):
        """
        V.reset_field_criteria()
        C++: virtual void ResetFieldCriteria()
        These methods are for the para_view client.
        """
        ret = self._vtk_obj.ResetFieldCriteria()
        return ret
        

    def set_field_criterion(self, *args):
        """
        V.set_field_criterion(int, float)
        C++: virtual void SetFieldCriterion(int field, double chord)
        These methods are for the para_view client.
        """
        ret = self._wrap_call(self._vtk_obj.SetFieldCriterion, *args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_number_of_subdivisions', 'GetMaximumNumberOfSubdivisions'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('output_dimension', 'GetOutputDimension'), ('abort_execute',
    'GetAbortExecute'), ('chord_error', 'GetChordError'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('merge_points',
    'GetMergePoints'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'merge_points',
    'release_data_flag', 'chord_error', 'maximum_number_of_subdivisions',
    'output_dimension', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TessellatorFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit TessellatorFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['merge_points'], [], ['chord_error',
            'maximum_number_of_subdivisions', 'output_dimension']),
            title='Edit TessellatorFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TessellatorFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

