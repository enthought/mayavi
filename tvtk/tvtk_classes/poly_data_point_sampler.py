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


class PolyDataPointSampler(PolyDataAlgorithm):
    """
    PolyDataPointSampler - generate points from PolyData
    
    Superclass: PolyDataAlgorithm
    
    PolyDataPointSampler generates points from input PolyData. The
    points are placed approximately a specified distance apart.
    
    This filter functions as follows. First, it regurgitates all input
    points, then samples all lines, plus edges associated with the input
    polygons and triangle strips to produce edge points. Finally, the
    interiors of polygons and triangle strips are subsampled to produce
    points.  All of these functiona can be enabled or disabled
    separately. Note that this algorithm only approximately generates
    points the specified distance apart. Generally the point density is
    finer than requested.
    
    Caveats:
    
    Point generation can be useful in a variety of applications. For
    example, generating seed points for glyphing or streamline
    generation. Another useful application is generating points for
    implicit modeling. In many cases implicit models can be more
    efficiently generated from points than from polygons or other
    primitives.
    
    See Also:
    
    ImplicitModeller
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataPointSampler, obj, update, **traits)
    
    generate_vertices = tvtk_base.true_bool_trait(help=\
        """
        Specify/retrieve a boolean flag indicating whether cell vertices
        should be generated. Cell vertices are useful if you actually
        want to display the points (that is, for each point generated, a
        vertex is generated). Recall that VTK only renders vertices and
        not points. The default is true.
        """
    )
    def _generate_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateVertices,
                        self.generate_vertices_)

    generate_interior_points = tvtk_base.true_bool_trait(help=\
        """
        Specify/retrieve a boolean flag indicating whether cell interiors
        should be sampled to produce output points. The default is true.
        """
    )
    def _generate_interior_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateInteriorPoints,
                        self.generate_interior_points_)

    generate_vertex_points = tvtk_base.true_bool_trait(help=\
        """
        Specify/retrieve a boolean flag indicating whether cell vertex
        points should be output.
        """
    )
    def _generate_vertex_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateVertexPoints,
                        self.generate_vertex_points_)

    generate_edge_points = tvtk_base.true_bool_trait(help=\
        """
        Specify/retrieve a boolean flag indicating whether cell edges
        should be sampled to produce output points. The default is true.
        """
    )
    def _generate_edge_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateEdgePoints,
                        self.generate_edge_points_)

    distance = traits.Trait(0.01, traits.Range(0.0, 9.9999996802856925e+37, enter_set=True, auto_set=False), help=\
        """
        Set/Get the approximate distance between points. This is an
        absolute distance measure. The default is 0.01.
        """
    )
    def _distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistance,
                        self.distance)

    _updateable_traits_ = \
    (('distance', 'GetDistance'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('generate_vertex_points', 'GetGenerateVertexPoints'), ('debug',
    'GetDebug'), ('generate_interior_points',
    'GetGenerateInteriorPoints'), ('abort_execute', 'GetAbortExecute'),
    ('generate_vertices', 'GetGenerateVertices'), ('release_data_flag',
    'GetReleaseDataFlag'), ('generate_edge_points',
    'GetGenerateEdgePoints'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_edge_points',
    'generate_interior_points', 'generate_vertex_points',
    'generate_vertices', 'global_warning_display', 'release_data_flag',
    'distance', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataPointSampler, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataPointSampler properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['generate_edge_points', 'generate_interior_points',
            'generate_vertex_points', 'generate_vertices'], [], ['distance']),
            title='Edit PolyDataPointSampler properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataPointSampler properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

