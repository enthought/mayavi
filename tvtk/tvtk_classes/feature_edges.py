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


class FeatureEdges(PolyDataAlgorithm):
    """
    FeatureEdges - extract boundary, non-manifold, and/or sharp edges
    from polygonal data
    
    Superclass: PolyDataAlgorithm
    
    FeatureEdges is a filter to extract special types of edges from
    input polygonal data. These edges are either 1) boundary (used by one
    polygon) or a line cell; 2) non-manifold (used by three or more
    polygons); 3) feature edges (edges used by two triangles and whose
    dihedral angle > feature_angle); or 4) manifold edges (edges used by
    exactly two polygons). These edges may be extracted in any
    combination. Edges may also be "colored" (i.e., scalar values
    assigned) based on edge type. The cell coloring is assigned to the
    cell data of the extracted edges.
    
    Caveats:
    
    To see the coloring of the liens you may have to set the scalar_mode
    instance variable of the mapper to set_scalar_mode_to_use_cell_data().
    (This is only a problem if there are point data scalars.)
    
    See Also:
    
    ExtractEdges
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFeatureEdges, obj, update, **traits)
    
    feature_edges = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the extraction of feature edges.
        """
    )
    def _feature_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureEdges,
                        self.feature_edges_)

    boundary_edges = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the extraction of boundary edges.
        """
    )
    def _boundary_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundaryEdges,
                        self.boundary_edges_)

    coloring = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the coloring of edges by type.
        """
    )
    def _coloring_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColoring,
                        self.coloring_)

    non_manifold_edges = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the extraction of non-manifold edges.
        """
    )
    def _non_manifold_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNonManifoldEdges,
                        self.non_manifold_edges_)

    manifold_edges = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the extraction of manifold edges.
        """
    )
    def _manifold_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetManifoldEdges,
                        self.manifold_edges_)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set / get a spatial locator for merging points. By default an
        instance of MergePoints is used.
        """
    )

    feature_angle = traits.Trait(30.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Specify the feature angle for extracting feature edges.
        """
    )
    def _feature_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureAngle,
                        self.feature_angle)

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('feature_edges', 'GetFeatureEdges'), ('coloring', 'GetColoring'),
    ('manifold_edges', 'GetManifoldEdges'), ('boundary_edges',
    'GetBoundaryEdges'), ('progress_text', 'GetProgressText'),
    ('non_manifold_edges', 'GetNonManifoldEdges'), ('debug', 'GetDebug'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'), ('feature_angle', 'GetFeatureAngle'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'boundary_edges', 'coloring', 'debug',
    'feature_edges', 'global_warning_display', 'manifold_edges',
    'non_manifold_edges', 'release_data_flag', 'feature_angle',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FeatureEdges, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit FeatureEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['boundary_edges', 'coloring', 'feature_edges',
            'manifold_edges', 'non_manifold_edges'], [], ['feature_angle']),
            title='Edit FeatureEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FeatureEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

