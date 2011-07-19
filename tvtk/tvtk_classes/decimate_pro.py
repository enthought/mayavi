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


class DecimatePro(PolyDataAlgorithm):
    """
    DecimatePro - reduce the number of triangles in a mesh
    
    Superclass: PolyDataAlgorithm
    
    DecimatePro is a filter to reduce the number of triangles in a
    triangle mesh, forming a good approximation to the original geometry.
    The input to DecimatePro is a PolyData object, and only
    triangles are treated. If you desire to decimate polygonal meshes,
    first triangulate the polygons with TriangleFilter object.
    
    The implementation of DecimatePro is similar to the algorithm
    originally described in "Decimation of Triangle Meshes", Proc
    Siggraph `92, with three major differences. First, this algorithm
    does not necessarily preserve the topology of the mesh. Second, it is
    guaranteed to give the a mesh reduction factor specified by the user
    (as long as certain constraints are not set - see Caveats). Third, it
    is set up generate progressive meshes, that is a stream of operations
    that can be easily transmitted and incrementally updated (see Hugues
    Hoppe's Siggraph '96 paper on progressive meshes).
    
    The algorithm proceeds as follows. Each vertex in the mesh is
    classified and inserted into a priority queue. The priority is based
    on the error to delete the vertex and retriangulate the hole.
    Vertices that cannot be deleted or triangulated (at this point in the
    algorithm) are skipped. Then, each vertex in the priority queue is
    processed (i.e., deleted followed by hole triangulation using edge
    collapse). This continues until the priority queue is empty. Next,
    all remaining vertices are processed, and the mesh is split into
    separate pieces along sharp edges or at non-manifold attachment
    points and reinserted into the priority queue. Again, the priority
    queue is processed until empty. If the desired reduction is still not
    achieved, the remaining vertices are split as necessary (in a
    recursive fashion) so that it is possible to eliminate every triangle
    as necessary.
    
    To use this object, at a minimum you need to specify the ivar
    target_reduction. The algorithm is guaranteed to generate a reduced
    mesh at this level as long as the following four conditions are met:
    1) topology modification is allowed (i.e., the ivar preserve_topology
    is off);
    2) mesh splitting is enabled (i.e., the ivar Splitting is on); 3) the
       algorithm is allowed to modify the boundary of the mesh (i.e., the
    ivar boundary_vertex_deletion is on); and 4) the maximum allowable
       error (i.e., the ivar maximum_error) is set to VTK_DOUBLE_MAX. 
       Other important parameters to adjust include the feature_angle and
       split_angle ivars, since these can impact the quality of the final
       mesh. Also, you can set the ivar accumulate_error to force
       incremental error update and distribution to surrounding vertices
       as each vertex is deleted. The accumulated error is a conservative
    global error bounds and decimation error, but requires additional
       memory and time to compute.
    
    Caveats:
    
    To guarantee a given level of reduction, the ivar preserve_topology
    must be off; the ivar Splitting is on; the ivar
    boundary_vertex_deletion is on; and the ivar maximum_error is set to
    VTK_DOUBLE_MAX.
    
    If preserve_topology is off, and split_edges is off; the mesh topology
    may be modified by closing holes.
    
    Once mesh splitting begins, the feature angle is set to the split
    angle.
    
    See Also:
    
    Decimate QuadricClustering QuadricDecimation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDecimatePro, obj, update, **traits)
    
    pre_split_mesh = tvtk_base.false_bool_trait(help=\
        """
        In some cases you may wish to split the mesh prior to algorithm
        execution. This separates the mesh into semi-planar patches,
        which are disconnected from each other. This can give superior
        results in some cases. If the ivar pre_split_mesh ivar is enabled,
        the mesh is split with the specified split_angle. Otherwise mesh
        splitting is deferred as long as possible.
        """
    )
    def _pre_split_mesh_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreSplitMesh,
                        self.pre_split_mesh_)

    preserve_topology = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off whether to preserve the topology of the original
        mesh. If on, mesh splitting and hole elimination will not occur.
        This may limit the maximum reduction that may be achieved.
        """
    )
    def _preserve_topology_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreserveTopology,
                        self.preserve_topology_)

    boundary_vertex_deletion = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the deletion of vertices on the boundary of a mesh.
        This may limit the maximum reduction that may be achieved.
        """
    )
    def _boundary_vertex_deletion_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundaryVertexDeletion,
                        self.boundary_vertex_deletion_)

    splitting = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the splitting of the mesh at corners, along edges, at
        non-manifold points, or anywhere else a split is required.
        Turning splitting off will better preserve the original topology
        of the mesh, but you may not obtain the requested reduction.
        """
    )
    def _splitting_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplitting,
                        self.splitting_)

    accumulate_error = tvtk_base.false_bool_trait(help=\
        """
        The computed error can either be computed directly from the mesh
        or the error may be accumulated as the mesh is modified. If the
        error is accumulated, then it represents a global error bounds,
        and the ivar maximum_error becomes a global bounds on mesh error.
        Accumulating the error requires extra memory proportional to the
        number of vertices in the mesh. If accumulate_error is off, then
        the error is not accumulated.
        """
    )
    def _accumulate_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAccumulateError,
                        self.accumulate_error_)

    maximum_error = traits.Trait(1e+299, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Set the largest decimation error that is allowed during the
        decimation process. This may limit the maximum reduction that may
        be achieved. The maximum error is specified as a fraction of the
        maximum length of the input data bounding box.
        """
    )
    def _maximum_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumError,
                        self.maximum_error)

    degree = traits.Trait(25, traits.Range(25, 512, enter_set=True, auto_set=False), help=\
        """
        If the number of triangles connected to a vertex exceeds
        "Degree", then the vertex will be split. (NOTE: the complexity of
        the triangulation algorithm is proportional to Degree^2. Setting
        degree small can improve the performance of the algorithm.)
        """
    )
    def _degree_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDegree,
                        self.degree)

    feature_angle = traits.Trait(15.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Specify the mesh feature angle. This angle is used to define what
        an edge is (i.e., if the surface normal between two adjacent
        triangles is >= feature_angle, an edge exists).
        """
    )
    def _feature_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureAngle,
                        self.feature_angle)

    error_is_absolute = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The maximum_error is normally defined as a fraction of the dataset
        bounding diagonal. By setting error_is_absolute to 1, the error is
        instead defined as that specified by absolute_error. By default
        error_is_absolute=_0.
        """
    )
    def _error_is_absolute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetErrorIsAbsolute,
                        self.error_is_absolute)

    absolute_error = traits.Trait(1e+299, traits.Range(0.0, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Same as maximum_error, but to be used when error_is_absolute is 1
        """
    )
    def _absolute_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbsoluteError,
                        self.absolute_error)

    split_angle = traits.Trait(75.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Specify the mesh split angle. This angle is used to control the
        splitting of the mesh. A split line exists when the surface
        normals between two edge connected triangles are >= split_angle.
        """
    )
    def _split_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplitAngle,
                        self.split_angle)

    inflection_point_ratio = traits.Trait(10.0, traits.Range(1.0009999999999999, 1.0000000000000001e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the inflection point ratio. An inflection point occurs
        when the ratio of reduction error between two iterations is
        greater than or equal to the inflection_point_ratio.
        """
    )
    def _inflection_point_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInflectionPointRatio,
                        self.inflection_point_ratio)

    target_reduction = traits.Trait(0.9, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify the desired reduction in the total number of polygons
        (e.g., if target_reduction is set to 0.9, this filter will try to
        reduce the data set to 10% of its original size). Because of
        various constraints, this level of reduction may not be realized.
        If you want to guarantee a particular reduction, you must turn
        off preserve_topology, turn on split_edges and
        boundary_vertex_deletion, and set the maximum_error to
        VTK_DOUBLE_MAX (these ivars are initialized this way when the
        object is instantiated).
        """
    )
    def _target_reduction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetReduction,
                        self.target_reduction)

    def _get_number_of_inflection_points(self):
        return self._vtk_obj.GetNumberOfInflectionPoints()
    number_of_inflection_points = traits.Property(_get_number_of_inflection_points, help=\
        """
        Get the number of inflection points. Only returns a valid value
        after the filter has executed.  The values in the list are mesh
        reduction values at each inflection point. Note: the first
        inflection point always occurs right before non-planar triangles
        are decimated (i.e., as the error becomes non-zero).
        """
    )

    _updateable_traits_ = \
    (('pre_split_mesh', 'GetPreSplitMesh'), ('split_angle',
    'GetSplitAngle'), ('error_is_absolute', 'GetErrorIsAbsolute'),
    ('degree', 'GetDegree'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug', 'GetDebug'), ('progress_text',
    'GetProgressText'), ('preserve_topology', 'GetPreserveTopology'),
    ('splitting', 'GetSplitting'), ('inflection_point_ratio',
    'GetInflectionPointRatio'), ('accumulate_error',
    'GetAccumulateError'), ('abort_execute', 'GetAbortExecute'),
    ('maximum_error', 'GetMaximumError'), ('absolute_error',
    'GetAbsoluteError'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('feature_angle', 'GetFeatureAngle'), ('boundary_vertex_deletion',
    'GetBoundaryVertexDeletion'), ('target_reduction',
    'GetTargetReduction'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'accumulate_error', 'boundary_vertex_deletion',
    'debug', 'global_warning_display', 'pre_split_mesh',
    'preserve_topology', 'release_data_flag', 'splitting',
    'absolute_error', 'degree', 'error_is_absolute', 'feature_angle',
    'inflection_point_ratio', 'maximum_error', 'progress_text',
    'split_angle', 'target_reduction'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DecimatePro, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit DecimatePro properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['accumulate_error', 'boundary_vertex_deletion',
            'pre_split_mesh', 'preserve_topology', 'splitting'], [],
            ['absolute_error', 'degree', 'error_is_absolute', 'feature_angle',
            'inflection_point_ratio', 'maximum_error', 'split_angle',
            'target_reduction']),
            title='Edit DecimatePro properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DecimatePro properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

