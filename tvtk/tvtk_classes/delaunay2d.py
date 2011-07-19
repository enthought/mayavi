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


class Delaunay2D(PolyDataAlgorithm):
    """
    Delaunay2D - create 2d Delaunay triangulation of input points
    
    Superclass: PolyDataAlgorithm
    
    Delaunay2D is a filter that constructs a 2d Delaunay triangulation
    from a list of input points. These points may be represented by any
    dataset of type PointSet and subclasses. The output of the filter
    is a polygonal dataset. Usually the output is a triangle mesh, but if
    a non-zero alpha distance value is specified (called the "alpha"
    value), then only triangles, edges, and vertices lying within the
    alpha radius are output. In other words, non-zero alpha values may
    result in arbitrary combinations of triangles, lines, and vertices.
    (The notion of alpha value is derived from Edelsbrunner's work on "alpha
    shapes".) Also, it is possible to generate "constrained
    triangulations" using this filter. A constrained triangulation is one
    where edges and loops (i.e., polygons) can be defined and the
    triangulation will preserve them (read on for more information).
    
    The 2d Delaunay triangulation is defined as the triangulation that
    satisfies the Delaunay criterion for n-dimensional simplexes (in this
    case n=2 and the simplexes are triangles). This criterion states that
    a circumsphere of each simplex in a triangulation contains only the
    n+1 defining points of the simplex. (See "The Visualization Toolkit"
    text for more information.) In two dimensions, this translates into
    an optimal triangulation. That is, the maximum interior angle of any
    triangle is less than or equal to that of any possible triangulation.
    
    Delaunay triangulations are used to build topological structures from
    unorganized (or unstructured) points. The input to this filter is a
    list of points specified in 3d, even though the triangulation is 2d.
    Thus the triangulation is constructed in the x-y plane, and the z
    coordinate is ignored (although carried through to the output). If
    you desire to triangulate in a different plane, you can use the
    TransformFilter to transform the points into and out of the x-y
    plane or you can specify a transform to the delaunay2d directly.  In
    the latter case, the input points are transformed, the transformed
    points are triangulated, and the output will use the triangulated
    topology for the original (non-transformed) points.  This avoids
    transforming the data back as would be required when using the
    TransformFilter method.  Specifying a transform directly also
    allows any transform to be used: rigid, non-rigid, non-invertible,
    etc.
    
    If an input transform is used, then alpha values are applied (for the
    most part) in the original data space.  The exception is when
    bounding_triangulation is on.  In this case, alpha values are applied
    in the original data space unless a cell uses a bounding vertex.
    
    The Delaunay triangulation can be numerically sensitive in some
    cases. To prevent problems, try to avoid injecting points that will
    result in triangles with bad aspect ratios (1000:1 or greater). In
    practice this means inserting points that are "widely dispersed", and
    enables smooth transition of triangle sizes throughout the mesh. (You
    may even want to add extra points to create a better point
    distribution.) If numerical problems are present, you will see a
    warning message to this effect at the end of the triangulation
    process.
    
    To create constrained meshes, you must define an additional input.
    This input is an instance of PolyData which contains lines,
    polylines, and/or polygons that define constrained edges and loops.
    Only the topology of (lines and polygons) from this second input are
    used.  The topology is assumed to reference points in the input point
    set (the one to be triangulated). In other words, the lines and
    polygons use point ids from the first input point set. Lines and
    polylines found in the input will be mesh edges in the output.
    Polygons define a loop with inside and outside regions. The inside of
    the polygon is determined by using the right-hand-rule, i.e., looking
    down the z-axis a polygon should be ordered counter-clockwise. Holes
    in a polygon should be ordered clockwise. If you choose to create a
    constrained triangulation, the final mesh may not satisfy the
    Delaunay criterion. (Noted: the lines/polygon edges must not
    intersect when projected onto the 2d plane.  It may not be possible
    to recover all edges due to not enough points in the triangulation,
    or poorly defined edges (coincident or excessively long).  The form
    of the lines or polygons is a list of point ids that correspond to
    the input point ids used to generate the triangulation.)
    
    If an input transform is used, constraints are defined in the
    "transformed" space.  So when the right hand rule is used for a
    polygon constraint, that operation is applied using the transformed
    points.  Since the input transform can be any transformation (rigid
    or non-rigid), care must be taken in constructing constraints when an
    input transform is used.
    
    Caveats:
    
    Points arranged on a regular lattice (termed degenerate cases) can be
    triangulated in more than one way (at least according to the Delaunay
    criterion). The choice of triangulation (as implemented by this
    algorithm) depends on the order of the input points. The first three
    points will form a triangle; other degenerate points will not break
    this triangle.
    
    Points that are coincident (or nearly so) may be discarded by the
    algorithm. This is because the Delaunay triangulation requires unique
    input points. You can control the definition of coincidence with the
    "Tolerance" instance variable.
    
    The output of the Delaunay triangulation is supposedly a convex hull.
    In certain cases this implementation may not generate the convex
    hull. This behavior can be controlled by the Offset instance
    variable. Offset is a multiplier used to control the size of the
    initial triangulation. The larger the offset value, the more likely
    you will generate a convex hull; but the more likely you are to see
    numerical problems.
    
    See Also:
    
    Delaunay3D TransformFilter GaussianSplatter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDelaunay2D, obj, update, **traits)
    
    bounding_triangulation = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether bounding triangulation points (and
        associated triangles) are included in the output. (These are
        introduced as an initial triangulation to begin the triangulation
        process. This feature is nice for debugging output.)
        """
    )
    def _bounding_triangulation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundingTriangulation,
                        self.bounding_triangulation_)

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Set / get the transform which is applied to points to generate a
        2d problem.  This maps a 3d dataset into a 2d dataset where
        triangulation can be done on the XY plane.  The points are
        transformed and triangulated.  The topology of triangulated
        points is used as the output topology.  The output points are the
        original (untransformed) points.  The transform can be any
        subclass of AbstractTransform (thus it does not need to be a
        linear or invertible transform).
        """
    )

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        deref_vtk(arg))
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        Get a pointer to the source object.
        """
    )

    offset = traits.Trait(1.0, traits.Range(0.75, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify a multiplier to control the size of the initial, bounding
        Delaunay triangulation.
        """
    )
    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    alpha = traits.Trait(0.0, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify alpha (or distance) value to control output of this
        filter. For a non-zero alpha value, only edges or triangles
        contained within a sphere centered at mesh vertices will be
        output. Otherwise, only triangles will be output.
        """
    )
    def _alpha_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlpha,
                        self.alpha)

    tolerance = traits.Trait(1e-05, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify a tolerance to control discarding of closely spaced
        points. This tolerance is specified as a fraction of the diagonal
        length of the bounding box of the points.
        """
    )
    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    projection_plane_mode = traits.Trait(0, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Define
        """
    )
    def _projection_plane_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionPlaneMode,
                        self.projection_plane_mode)

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the source object used to specify constrained edges and
        loops. (This is optional.) If set, and lines/polygons are
        defined, a constrained triangulation is created. The
        lines/polygons are assumed to reference points in the input point
        set (i.e. point ids are identical in the input and source). New
        style. This method is equivalent to set_input_connection(_1,
        alg_output).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_warning_display', 'GetGlobalWarningDisplay'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('projection_plane_mode',
    'GetProjectionPlaneMode'), ('progress', 'GetProgress'),
    ('bounding_triangulation', 'GetBoundingTriangulation'), ('offset',
    'GetOffset'), ('reference_count', 'GetReferenceCount'), ('alpha',
    'GetAlpha'), ('tolerance', 'GetTolerance'), ('abort_execute',
    'GetAbortExecute'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'bounding_triangulation', 'debug',
    'global_warning_display', 'release_data_flag', 'alpha', 'offset',
    'progress_text', 'projection_plane_mode', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Delaunay2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Delaunay2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['bounding_triangulation'], [], ['alpha', 'offset',
            'projection_plane_mode', 'tolerance']),
            title='Edit Delaunay2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Delaunay2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

