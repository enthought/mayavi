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


class WindowedSincPolyDataFilter(PolyDataAlgorithm):
    """
    WindowedSincPolyDataFilter - adjust point positions using a
    windowed sinc function interpolation kernel
    
    Superclass: PolyDataAlgorithm
    
    WindowedSincPolyDataFiler adjust point coordinate using a windowed
    sinc function interpolation kernel.  The effect is to "relax" the
    mesh, making the cells better shaped and the vertices more evenly
    distributed. Note that this filter operates the lines, polygons, and
    triangle strips composing an instance of PolyData.  Vertex or
    poly-vertex cells are never modified.
    
    The algorithm proceeds as follows. For each vertex v, a topological
    and geometric analysis is performed to determine which vertices are
    connected to v, and which cells are connected to v. Then, a
    connectivity array is constructed for each vertex. (The connectivity
    array is a list of lists of vertices that directly attach to each
    vertex.) Next, an iteration phase begins over all vertices. For each
    vertex v, the coordinates of v are modified using a windowed sinc
    function interpolation kernel. Taubin describes this methodology is
    the IBM tech report RC-20404 (#90237, dated 3/12/96) "Optimal Surface Smoothing as Filter
    Design" G. Taubin, T. Zhang and G. Golub. (Zhang and Golub are at
    Stanford University).
    
    This report discusses using standard signal processing low-pass
    filters (in particular windowed sinc functions) to smooth polyhedra.
    The transfer functions of the low-pass filters are approximated by
    Chebyshev polynomials. This facilitates applying the filters in an
    iterative diffusion process (as opposed to a kernel convolution). 
    The more smoothing iterations applied, the higher the degree of
    polynomial approximating the low-pass filter transfer function. Each
    smoothing iteration, therefore, applies the next higher term of the
    Chebyshev filter approximation to the polyhedron. This decoupling of
    the filter into an iteratively applied polynomial is possible since
    the Chebyshev polynomials are orthogonal, i.e. increasing the order
    of the approximation to the filter transfer function does not alter
    the previously calculated coefficients for the low order terms.
    
    Note: Care must be taken to avoid smoothing with too few iterations.
    A Chebyshev approximation with too few terms is an poor
    approximation. The first few smoothing iterations represent a severe
    scaling and translation of the data.  Subsequent iterations cause the
    smoothed polyhedron to converge to the true location and scale of the
    object. We have attempted to protect against this by automatically
    adjusting the filter, effectively widening the pass band. This
    adjustment is only possible if the number of iterations is greater
    than 1.  Note that this sacrifices some degree of smoothing for model
    integrity. For those interested, the filter is adjusted by searching
    for a value sigma such that the actual pass band is k_pb + sigma and
    such that the filter transfer function evaluates to unity at k_pb,
    i.e. f(k_pb) = 1
    
    To improve the numerical stability of the solution and minimize the
    scaling the translation effects, the algorithm can translate and
    scale the position coordinates to within the unit cube [-1, 1],
    perform the smoothing, and translate and scale the position
    coordinates back to the original coordinate frame.  This mode is
    controlled with the normalize_coordinates_on() /
    normalize_coordinates_off() methods.  For legacy reasons, the default
    is normalize_coordinates_off.
    
    This implementation is currently limited to using an interpolation
    kernel based on Hamming windows.  Other windows (such as Hann,
    Blackman, Kaiser, Lanczos, Gaussian, and exponential windows) could
    be used instead.
    
    There are some special instance variables used to control the
    execution of this filter. (These ivars basically control what
    vertices can be smoothed, and the creation of the connectivity
    array.) The boundary_smoothing ivar enables/disables the smoothing
    operation on vertices that are on the "boundary" of the mesh. A
    boundary vertex is one that is surrounded by a semi-cycle of polygons
    (or used by a single line).
    
    Another important ivar is feature_edge_smoothing. If this ivar is
    enabled, then interior vertices are classified as either "simple", "interior
    edge", or "fixed", and smoothed differently. (Interior vertices are
    manifold vertices surrounded by a cycle of polygons; or used by two
    line cells.) The classification is based on the number of feature
    edges attached to v. A feature edge occurs when the angle between the
    two surface normals of a polygon sharing an edge is greater than the
    feature_angle ivar. Then, vertices used by no feature edges are
    classified "simple", vertices used by exactly two feature edges are
    classified "interior edge", and all others are "fixed" vertices.
    
    Once the classification is known, the vertices are smoothed
    differently. Corner (i.e., fixed) vertices are not smoothed at all.
    Simple vertices are smoothed as before . Interior edge vertices are
    smoothed only along their two connected edges, and only if the angle
    between the edges is less than the edge_angle ivar.
    
    The total smoothing can be controlled by using two ivars. The
    number_of_iterations determines the maximum number of smoothing passes.
    The number_of_iterations corresponds to the degree of the polynomial
    that is used to approximate the windowed sinc function. Ten or twenty
    iterations is all the is usually necessary. Contrast this with
    SmoothPolyDataFilter which usually requires 100 to 200 smoothing
    iterations. SmoothPolyDataFilter is also not an approximation to
    an ideal low-pass filter, which can cause the geometry to shrink as
    the amount of smoothing increases.
    
    The second ivar is the specification of the pass_band for the windowed
    sinc filter.  By design, the pass_band is specified as a doubleing
    point number between 0 and 2.  Lower pass_band values produce more
    smoothing. A good default value for the pass_band is 0.1 (for those
    interested, the pass_band (and frequencies) for poly_data are based on
    the valence of the vertices, this limits all the frequency modes in a
    polyhedral mesh to between 0 and 2.)
    
    There are two instance variables that control the generation of error
    data. If the ivar generate_error_scalars is on, then a scalar value
    indicating the distance of each vertex from its original position is
    computed. If the ivar generate_error_vectors is on, then a vector
    representing change in position is computed.
    
    Caveats:
    
    The smoothing operation reduces high frequency information in the
    geometry of the mesh. With excessive smoothing important details may
    be lost. Enabling feature_edge_smoothing helps reduce this effect, but
    cannot entirely eliminate it.
    
    See Also:
    
    SmoothPolyDataFilter Decimate DecimatePro
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWindowedSincPolyDataFilter, obj, update, **traits)
    
    generate_error_scalars = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the generation of scalar distance values.
        """
    )
    def _generate_error_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateErrorScalars,
                        self.generate_error_scalars_)

    non_manifold_smoothing = tvtk_base.false_bool_trait(help=\
        """
        Smooth non-manifold vertices.
        """
    )
    def _non_manifold_smoothing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNonManifoldSmoothing,
                        self.non_manifold_smoothing_)

    boundary_smoothing = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the smoothing of vertices on the boundary of the
        mesh.
        """
    )
    def _boundary_smoothing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundarySmoothing,
                        self.boundary_smoothing_)

    normalize_coordinates = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off coordinate normalization.  The positions can be
        translated and scaled such that they fit within a [-1, 1] prior
        to the smoothing computation. The default is off.  The numerical
        stability of the solution can be improved by turning
        normalization on.  If normalization is on, the coordinates will
        be rescaled to the original coordinate system after smoothing has
        completed.
        """
    )
    def _normalize_coordinates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizeCoordinates,
                        self.normalize_coordinates_)

    generate_error_vectors = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the generation of error vectors.
        """
    )
    def _generate_error_vectors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateErrorVectors,
                        self.generate_error_vectors_)

    feature_edge_smoothing = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off smoothing along sharp interior edges.
        """
    )
    def _feature_edge_smoothing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureEdgeSmoothing,
                        self.feature_edge_smoothing_)

    edge_angle = traits.Trait(15.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Specify the edge angle to control smoothing along edges (either
        interior or boundary).
        """
    )
    def _edge_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeAngle,
                        self.edge_angle)

    number_of_iterations = traits.Trait(20, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of iterations (or degree of the polynomial
        approximating the windowed sinc function).
        """
    )
    def _number_of_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfIterations,
                        self.number_of_iterations)

    feature_angle = traits.Trait(45.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Specify the feature angle for sharp edge identification.
        """
    )
    def _feature_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureAngle,
                        self.feature_angle)

    pass_band = traits.Trait(0.1, traits.Range(0.0, 2.0, enter_set=True, auto_set=False), help=\
        """
        Set the passband value for the windowed sinc filter
        """
    )
    def _pass_band_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassBand,
                        self.pass_band)

    _updateable_traits_ = \
    (('normalize_coordinates', 'GetNormalizeCoordinates'),
    ('non_manifold_smoothing', 'GetNonManifoldSmoothing'),
    ('progress_text', 'GetProgressText'), ('debug', 'GetDebug'),
    ('feature_edge_smoothing', 'GetFeatureEdgeSmoothing'), ('edge_angle',
    'GetEdgeAngle'), ('generate_error_scalars',
    'GetGenerateErrorScalars'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_iterations',
    'GetNumberOfIterations'), ('boundary_smoothing',
    'GetBoundarySmoothing'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'), ('pass_band',
    'GetPassBand'), ('feature_angle', 'GetFeatureAngle'),
    ('generate_error_vectors', 'GetGenerateErrorVectors'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'boundary_smoothing', 'debug',
    'feature_edge_smoothing', 'generate_error_scalars',
    'generate_error_vectors', 'global_warning_display',
    'non_manifold_smoothing', 'normalize_coordinates',
    'release_data_flag', 'edge_angle', 'feature_angle',
    'number_of_iterations', 'pass_band', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WindowedSincPolyDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit WindowedSincPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['boundary_smoothing', 'feature_edge_smoothing',
            'generate_error_scalars', 'generate_error_vectors',
            'non_manifold_smoothing', 'normalize_coordinates'], [], ['edge_angle',
            'feature_angle', 'number_of_iterations', 'pass_band']),
            title='Edit WindowedSincPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WindowedSincPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

