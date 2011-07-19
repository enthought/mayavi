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

from tvtk.tvtk_classes.generic_cell_tessellator import GenericCellTessellator


class SimpleCellTessellator(GenericCellTessellator):
    """
    SimpleCellTessellator - helper class to perform cell tessellation
    
    Superclass: GenericCellTessellator
    
    SimpleCellTessellator is a helper class to perform adaptive
    tessellation of particular cell topologies. The major purpose for
    this class is to transform higher-order cell types (e.g.,
    higher-order finite elements) into linear cells that can then be
    easily visualized by VTK. This class works in conjunction with the
    GenericDataSet and GenericAdaptorCell classes.
    
    This algorithm is based on edge subdivision. An error metric along
    each edge is evaluated, and if the error is greater than some
    tolerance, the edge is subdivided (as well as all connected 2d and 3d
    cells). The process repeats until the error metric is satisfied.
    Since the algorithm is based on edge subdivision it inherently avoid
    T-junctions.
    
    A significant issue addressed by this algorithm is to insure face
    compatibility across neigboring cells. That is, diagonals due to face
    triangulation must match to insure that the mesh is compatible. The
    algorithm employs a precomputed table to accelerate the tessellation
    process. The table was generated with the help of
    OrderedTriangulator the basic idea is that the choice of diagonal
    is made only by considering the relative value of the point ids.
    
    See Also:
    
    GenericCellTessellator GenericSubdivisionErrorMetric
    AttributesErrorMetric GeometricErrorMetric
    ViewDependentErrorMetric
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSimpleCellTessellator, obj, update, **traits)
    
    fixed_subdivisions = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of fixed subdivisions. See get_fixed_subdivisions()
        for more explanations.
        \pre positive_level: level>=0 && level<=_get_max_subdivision_level()
        \post is_set: get_fixed_subdivisions()==level
        """
    )
    def _fixed_subdivisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFixedSubdivisions,
                        self.fixed_subdivisions)

    max_subdivision_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the maximum level of subdivision. See
        get_max_subdivision_level() for more explanations.
        \pre positive_level: level>=_get_fixed_subdivisions()
        \post is_set: level==_get_max_subdivision_level()
        """
    )
    def _max_subdivision_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxSubdivisionLevel,
                        self.max_subdivision_level)

    def _get_generic_cell(self):
        return wrap_vtk(self._vtk_obj.GetGenericCell())
    generic_cell = traits.Property(_get_generic_cell, help=\
        """
        Get the higher order cell in order to access the evaluation
        function.
        """
    )

    def _get_max_adaptive_subdivisions(self):
        return self._vtk_obj.GetMaxAdaptiveSubdivisions()
    max_adaptive_subdivisions = traits.Property(_get_max_adaptive_subdivisions, help=\
        """
        Return the maximum number of adaptive subdivisions.
        \post valid_result:
            result==_get_max_subdivision_level()-_get_fixed_subdivisions()
        """
    )

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Reset the output for repeated use of this class.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def set_subdivision_levels(self, *args):
        """
        V.set_subdivision_levels(int, int)
        C++: void SetSubdivisionLevels(int fixed, int maxLevel)
        Set both the number of fixed subdivisions and the maximum level
        of subdivisions. See get_fixed_subdivisions(),
        get_max_subdivision_level() and get_max_adaptive_subdivisions() for
        more explanations.
        \pre positive_fixed: fixed>=0
        \pre valid_range: fixed<=max_level
        \post fixed_is_set: fixed==_get_fixed_subdivisions()
        \post max_level_is_set: max_level==_get_max_subdivision_level()
        """
        ret = self._wrap_call(self._vtk_obj.SetSubdivisionLevels, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('fixed_subdivisions',
    'GetFixedSubdivisions'), ('measurement', 'GetMeasurement'),
    ('reference_count', 'GetReferenceCount'), ('max_subdivision_level',
    'GetMaxSubdivisionLevel'), ('global_warning_display',
    'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'fixed_subdivisions',
    'max_subdivision_level', 'measurement'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SimpleCellTessellator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SimpleCellTessellator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['fixed_subdivisions', 'max_subdivision_level',
            'measurement']),
            title='Edit SimpleCellTessellator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SimpleCellTessellator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

