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


class QuadricClustering(PolyDataAlgorithm):
    """
    QuadricClustering - reduce the number of triangles in a mesh
    
    Superclass: PolyDataAlgorithm
    
    QuadricClustering is a filter to reduce the number of triangles in
    a triangle mesh, forming a good approximation to the original
    geometry.  The input to QuadricClustering is a PolyData object,
    and all types of polygonal data are handled.
    
    The algorithm used is the one described by Peter Lindstrom in his
    Siggraph 2000 paper, "Out-of-Core Simplification of Large Polygonal
    Models."  The general approach of the algorithm is to cluster
    vertices in a uniform binning of space, accumulating the quadric of
    each triangle (pushed out to the triangles vertices) within each bin,
    and then determining an optimal position for a single vertex in a bin
    by using the accumulated quadric. In more detail, the algorithm first
    gets the bounds of the input poly data. It then breaks this bounding
    volume into a user-specified number of spatial bins.  It then reads
    each triangle from the input and hashes its vertices into these bins.
     (If this is the first time a bin has been visited, initialize its
    quadric to the 0 matrix.) The algorithm computes the error quadric
    for this triangle and adds it to the existing quadric of the bin in
    which each vertex is contained. Then, if 2 or more vertices of the
    triangle fall in the same bin, the triangle is dicarded.  If the
    triangle is not discarded, it adds the triangle to the list of output
    triangles as a list of vertex identifiers.  (There is one vertex id
    per bin.)  After all the triangles have been read, the representative
    vertex for each bin is computed (an optimal location is found) using
    the quadric for that bin.  This determines the spatial location of
    the vertices of each of the triangles in the output.
    
    To use this filter, specify the divisions defining the spatial
    subdivision in the x, y, and z directions. You must also specify an
    input PolyData. Then choose to either 1) use the original points
    that minimize the quadric error to produce the output triangles or 2)
    compute an optimal position in each bin to produce the output
    triangles (recommended and default behavior).
    
    This filter can take multiple inputs.  To do this, the user must
    explicity call start_append, Append (once for each input), and
    end_append.  start_append sets up the data structure to hold the
    quadric matrices.  Append processes each triangle in the input poly
    data it was called on, hashes its vertices to the appropriate bins,
    determines whether to keep this triangle, and updates the appropriate
    quadric matrices.  end_append determines the spatial location of each
    of the representative vertices for the visited bins. While this
    approach does not fit into the visualization architecture and
    requires manual control, it has the advantage that extremely large
    data can be processed in pieces and appended to the filter
    piece-by-piece.
    
    Caveats:
    
    This filter can drastically affect topology, i.e., topology is not
    preserved.
    
    The filter handles input triangle strips and arbitrary polygons.
    Arbitrary polygons are assumed convex: during insertion they are
    triangulated using a fan of triangles from the first point in the
    polygons. If the polygon is concave, this can produce bad results. In
    this case, use TriangleFilter to triangulate the polygons first.
    
    The filter also treats polylines and vertices.
    
    Note that for certain types of geometry (e.g., a mostly 2d plane with
    jitter in the normal direction), the decimator can perform badly. In
    this sitation, set the number of bins in the normal direction to one.
    
    See Also:
    
    QuadricDecimation DecimatePro Decimate QuadricLODActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkQuadricClustering, obj, update, **traits)
    
    use_input_points = tvtk_base.false_bool_trait(help=\
        """
        Normally the point that minimizes the quadric error function is
        used as the output of the bin.  When this flag is on, the bin
        point is forced to be one of the points from the input (the one
        with the smallest error). This option does not work (i.e., input
        points cannot be used) when the append methods (_start_append(),
        Append(), end_append()) are being called directly.
        """
    )
    def _use_input_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseInputPoints,
                        self.use_input_points_)

    use_feature_edges = tvtk_base.false_bool_trait(help=\
        """
        By default, this flag is off.  When "_use_feature_edges" is on, then
        quadrics are computed for boundary edges/feature edges.  They
        influence the quadrics (position of points), but not the mesh. 
        Which features to use can be controlled by the filter
        "_feature_edges".
        """
    )
    def _use_feature_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseFeatureEdges,
                        self.use_feature_edges_)

    copy_cell_data = tvtk_base.false_bool_trait(help=\
        """
        This flag makes the filter copy cell data from input to output
        (the best it can).  It uses input cells that trigger the addition
        of output cells (no averaging).  This is off by default, and does
        not work when append is being called explicitely (non-pipeline
        usage).
        """
    )
    def _copy_cell_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyCellData,
                        self.copy_cell_data_)

    prevent_duplicate_cells = tvtk_base.true_bool_trait(help=\
        """
        Specify a boolean indicating whether to remove duplicate cells
        (i.e. triangles).  This is a little slower, and takes more
        memory, but in some cases can reduce the number of cells produced
        by an order of magnitude. By default, this flag is true.
        """
    )
    def _prevent_duplicate_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreventDuplicateCells,
                        self.prevent_duplicate_cells_)

    use_feature_points = tvtk_base.false_bool_trait(help=\
        """
        By default, this flag is off.  It only has an effect when
        "_use_feature_edges" is also on.  When "_use_feature_points" is on,
        then quadrics are computed for boundary / feature points used in
        the boundary / feature edges.  They influence the quadrics
        (position of points), but not the mesh.
        """
    )
    def _use_feature_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseFeaturePoints,
                        self.use_feature_points_)

    use_internal_triangles = tvtk_base.true_bool_trait(help=\
        """
        When this flag is on (and it is on by default), then triangles
        that are completely contained in a bin are added to the bin
        quadrics.  When the the flag is off the filter operates faster,
        but the surface may not be as well behaved.
        """
    )
    def _use_internal_triangles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseInternalTriangles,
                        self.use_internal_triangles_)

    auto_adjust_number_of_divisions = tvtk_base.true_bool_trait(help=\
        """
        Enable automatic adjustment of number of divisions. If off, the
        number of divisions specified by the user is always used (as long
        as it is valid). The default is On
        """
    )
    def _auto_adjust_number_of_divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdjustNumberOfDivisions,
                        self.auto_adjust_number_of_divisions_)

    number_of_z_divisions = traits.Int(50, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of divisions along each axis for the spatial
        bins. The number of spatial bins is
        number_of_x_divisions*_number_of_y_divisions* number_of_z_divisions.  The
        filter may choose to ignore large numbers of divisions if the
        input has few points and auto_adjust_number_of_divisions is enabled.
        """
    )
    def _number_of_z_divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfZDivisions,
                        self.number_of_z_divisions)

    division_origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        This is an alternative way to set up the bins.  If you are trying
        to match boundaries between pieces, then you should use these
        methods rather than set_number_of_divisions. To use these methods,
        specify the origin and spacing of the spatial binning.
        """
    )
    def _division_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivisionOrigin,
                        self.division_origin)

    number_of_x_divisions = traits.Int(50, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of divisions along each axis for the spatial
        bins. The number of spatial bins is
        number_of_x_divisions*_number_of_y_divisions* number_of_z_divisions.  The
        filter may choose to ignore large numbers of divisions if the
        input has few points and auto_adjust_number_of_divisions is enabled.
        """
    )
    def _number_of_x_divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfXDivisions,
                        self.number_of_x_divisions)

    feature_points_angle = traits.Trait(30.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the angle to use in determining whether a point on a
        boundary / feature edge is a feature point.
        """
    )
    def _feature_points_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeaturePointsAngle,
                        self.feature_points_angle)

    number_of_y_divisions = traits.Int(50, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of divisions along each axis for the spatial
        bins. The number of spatial bins is
        number_of_x_divisions*_number_of_y_divisions* number_of_z_divisions.  The
        filter may choose to ignore large numbers of divisions if the
        input has few points and auto_adjust_number_of_divisions is enabled.
        """
    )
    def _number_of_y_divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfYDivisions,
                        self.number_of_y_divisions)

    number_of_divisions = traits.Array(shape=(3,), value=(50, 50, 50), dtype=int, enter_set=True, auto_set=False, cols=3, help=\
        """
        Set/Get the number of divisions along each axis for the spatial
        bins. The number of spatial bins is
        number_of_x_divisions*_number_of_y_divisions* number_of_z_divisions.  The
        filter may choose to ignore large numbers of divisions if the
        input has few points and auto_adjust_number_of_divisions is enabled.
        """
    )
    def _number_of_divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfDivisions,
                        self.number_of_divisions)

    division_spacing = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        This is an alternative way to set up the bins.  If you are trying
        to match boundaries between pieces, then you should use these
        methods rather than set_number_of_divisions. To use these methods,
        specify the origin and spacing of the spatial binning.
        """
    )
    def _division_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivisionSpacing,
                        self.division_spacing)

    def _get_feature_edges(self):
        return wrap_vtk(self._vtk_obj.GetFeatureEdges())
    feature_edges = traits.Property(_get_feature_edges, help=\
        """
        By default, this flag is off.  When "_use_feature_edges" is on, then
        quadrics are computed for boundary edges/feature edges.  They
        influence the quadrics (position of points), but not the mesh. 
        Which features to use can be controlled by the filter
        "_feature_edges".
        """
    )

    def append(self, *args):
        """
        V.append(PolyData)
        C++: void Append(PolyData *piece)
        These methods provide an alternative way of executing the filter.
        poly_data can be added to the result in pieces (append). In this
        mode, the user must specify the bounds of the entire model as an
        argument to the "_start_append" method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Append, *my_args)
        return ret

    def end_append(self):
        """
        V.end_append()
        C++: void EndAppend()
        These methods provide an alternative way of executing the filter.
        poly_data can be added to the result in pieces (append). In this
        mode, the user must specify the bounds of the entire model as an
        argument to the "_start_append" method.
        """
        ret = self._vtk_obj.EndAppend()
        return ret
        

    def start_append(self, *args):
        """
        V.start_append(float, float, float, float, float, float)
        C++: void StartAppend(double x0, double x1, double y0, double y1,
            double z0, double z1)
        These methods provide an alternative way of executing the filter.
        poly_data can be added to the result in pieces (append). In this
        mode, the user must specify the bounds of the entire model as an
        argument to the "_start_append" method.
        """
        ret = self._wrap_call(self._vtk_obj.StartAppend, *args)
        return ret

    _updateable_traits_ = \
    (('use_feature_edges', 'GetUseFeatureEdges'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('auto_adjust_number_of_divisions', 'GetAutoAdjustNumberOfDivisions'),
    ('number_of_divisions', 'GetNumberOfDivisions'),
    ('feature_points_angle', 'GetFeaturePointsAngle'), ('copy_cell_data',
    'GetCopyCellData'), ('progress_text', 'GetProgressText'),
    ('division_origin', 'GetDivisionOrigin'), ('number_of_z_divisions',
    'GetNumberOfZDivisions'), ('number_of_y_divisions',
    'GetNumberOfYDivisions'), ('prevent_duplicate_cells',
    'GetPreventDuplicateCells'), ('debug', 'GetDebug'),
    ('use_input_points', 'GetUseInputPoints'), ('use_internal_triangles',
    'GetUseInternalTriangles'), ('use_feature_points',
    'GetUseFeaturePoints'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('division_spacing', 'GetDivisionSpacing'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('number_of_x_divisions', 'GetNumberOfXDivisions'), ('abort_execute',
    'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_adjust_number_of_divisions',
    'copy_cell_data', 'debug', 'global_warning_display',
    'prevent_duplicate_cells', 'release_data_flag', 'use_feature_edges',
    'use_feature_points', 'use_input_points', 'use_internal_triangles',
    'division_origin', 'division_spacing', 'feature_points_angle',
    'number_of_divisions', 'number_of_x_divisions',
    'number_of_y_divisions', 'number_of_z_divisions', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(QuadricClustering, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit QuadricClustering properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['auto_adjust_number_of_divisions', 'copy_cell_data',
            'prevent_duplicate_cells', 'use_feature_edges', 'use_feature_points',
            'use_input_points', 'use_internal_triangles'], [], ['division_origin',
            'division_spacing', 'feature_points_angle', 'number_of_divisions',
            'number_of_x_divisions', 'number_of_y_divisions',
            'number_of_z_divisions']),
            title='Edit QuadricClustering properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit QuadricClustering properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

