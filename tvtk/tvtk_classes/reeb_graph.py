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

from tvtk.tvtk_classes.mutable_directed_graph import MutableDirectedGraph


class ReebGraph(MutableDirectedGraph):
    """
    ReebGraph - Reeb graph computation for PL scalar fields.
    
    Superclass: MutableDirectedGraph
    
    ReebGraph is a class that computes a Reeb graph given a PL scalar
    field (vtk_data_array) defined on a simplicial mesh. A Reeb graph is a
    concise representation of the connectivity evolution of the level
    sets of a scalar function.
    
    It is particularly useful in visualization (optimal seed set
    computation, fast flexible isosurface extraction, automated transfer
    function design, feature-driven visualization, etc.) and computer
    graphics (shape deformation, shape matching, shape compression,
    etc.).
    
    Reference: "Sur les points singuliers d'une forme de Pfaff
    completement integrable ou d'une fonction numerique", G. Reeb,
    Comptes-rendus de l'Academie des Sciences, 222:847-849, 1946.
    
    ReebGraph implements one of the latest and most robust Reeb graph
    computation algorithms.
    
    Reference: "Robust on-line computation of Reeb graphs: simplicity and
    speed", V. Pascucci, G. Scorzelli, P.-T. Bremer, and A. Mascarenhas,
    ACM Transactions on Graphics, Proc. of SIGGRAPH 2007.
    
    ReebGraph provides methods for computing multi-resolution
    topological hierarchies through topological simplification.
    Topoligical simplification can be either driven by persistence
    homology concepts (default behavior) or by application specific
    metrics (see ReebGraphSimplificationMetric). In the latter case,
    designing customized simplification metric evaluation algorithms
    enables the user to control the definition of what should be
    considered as noise or signal in the topological filtering process.
    
    References: "Topological persistence and simplification", H.
    Edelsbrunner, D. Letscher, and A. Zomorodian, Discrete Computational
    Geometry, 28:511-533, 2002.
    
    "Extreme elevation on a 2-manifold", P.K. Agarwal, H. Edelsbrunner,
    J. Harer, and Y. Wang, ACM Symposium on Computational Geometry, pp.
    357-365, 2004.
    
    "Simplifying flexible isosurfaces using local geometric measures", H.
    Carr, J. Snoeyink, M van de Panne, IEEE Visualization, 497-504, 2004
    
    "Loop surgery for volumetric meshes: Reeb graphs reduced to contour
    trees", J. Tierny, A. Gyulassy, E. Simon, V. Pascucci, IEEE Trans. on
    Vis. and Comp. Graph. (Proc of IEEE VIS), 15:1177-1184, 2009.
    
    Reeb graphs can be computed from 2d data (vtk_poly_data, with triangles
    only) or 3d data (vtk_unstructured_grid, with tetrahedra only),
    sequentially (see the "Build" calls) or in streaming (see the
    "_stream_triangle" and "_stream_tetrahedron" calls).
    
    ReebGraph inherits from MutableDirectedGraph.
    
    Each vertex of a ReebGraph object represents a critical point of
    the scalar field where the connectivity of the related level set
    changes (creation, deletion, split or merge of connected components).
    A IdTypeArray (called "Vertex Ids") is associated with the
    vertex_data of a ReebGraph object, in order to retrieve if
    necessary the exact Ids of the corresponding vertices in the input
    mesh.
    
    The edges of a ReebGraph object represent the regions of the input
    mesh separated by the critical contours of the field, and where the
    connectivity of the input field does not change. A VariantArray is
    associated with the edge_dta of a ReebGraph object and each entry
    of this array is a AbstractArray containing the Ids of the
    vertices of those regions, sorted by function value (useful for
    flexible isosurface extraction or level set signature computation,
    for instance).
    
    See graphics/_testing/_cxx/_test_reeb_graph.cxx for examples of traversals
    and typical usages (customized simplification, skeletonization,
    contour spectra,
     etc.) of a ReebGraph object.
    
    See Also:
    
    
         ReebGraphSimplificationMetric
         PolyDataToReebGraphFilter
         UnstructuredGridToReebGraphFilter
         ReebGraphSimplificationFilter
         ReebGraphSurfaceSkeletonFilter
         ReebGraphVolumeSkeletonFilter
         AreaContourSpectrumFilter
         VolumeContourSpectrumFilter
    
    Tests:
    
    
         graphics/_testing/_cxx/_test_reeb_graph.cxx
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkReebGraph, obj, update, **traits)
    
    def build(self, *args):
        """
        V.build(PolyData, DataArray) -> int
        C++: int Build(PolyData *mesh, DataArray *scalarField)
        V.build(UnstructuredGrid, DataArray) -> int
        C++: int Build(UnstructuredGrid *mesh,
            DataArray *scalarField)
        V.build(PolyData, int) -> int
        C++: int Build(PolyData *mesh, IdType scalarFieldId)
        V.build(UnstructuredGrid, int) -> int
        C++: int Build(UnstructuredGrid *mesh, IdType scalarFieldId)
        V.build(PolyData, string) -> int
        C++: int Build(PolyData *mesh, const char *scalarFieldName)
        V.build(UnstructuredGrid, string) -> int
        C++: int Build(UnstructuredGrid *mesh,
            const char *scalarFieldName)
        Build the Reeb graph of the field 'scalar_field' defined on the
        surface mesh 'mesh'.
        
        Returned values:
        
        ReebGraph::ERR_INCORRECT_FIELD: 'scalar_field' does not have as
        many tuples as 'mesh' has vertices.
        
        ReebGraph::ERR_NOT_A_SIMPLICIAL_MESH: the input mesh 'mesh' is
        not a simplicial mesh (for example, the surface mesh contains
        quads instead of triangles).
        """
        my_args = deref_array(args, [('vtkPolyData', 'vtkDataArray'), ('vtkUnstructuredGrid', 'vtkDataArray'), ('vtkPolyData', 'int'), ('vtkUnstructuredGrid', 'int'), ('vtkPolyData', 'string'), ('vtkUnstructuredGrid', 'string')])
        ret = self._wrap_call(self._vtk_obj.Build, *my_args)
        return ret

    def close_stream(self):
        """
        V.close_stream()
        C++: void CloseStream()
        Finalize internal data structures, in the case of streaming
        computations (with stream_triangle or stream_tetrahedron). After
        this call, no more triangle or tetrahedron can be inserted via
        stream_triangle or stream_tetrahedron. IMPORTANT: This method
        _must_ be called when the input stream is finished. If you need
        to get a snapshot of the Reeb graph during the streaming process
        (to parse or simplify it), do a deep_copy followed by a
        close_stream on the copy.
        """
        ret = self._vtk_obj.CloseStream()
        return ret
        

    def set(self, *args):
        """
        V.set(MutableDirectedGraph)
        C++: void Set(MutableDirectedGraph *g)
        Use a pre-defined Reeb graph (post-processing). Use with caution!
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Set, *my_args)
        return ret

    def simplify(self, *args):
        """
        V.simplify(float, ReebGraphSimplificationMetric) -> int
        C++: int Simplify(double simplificationThreshold,
            ReebGraphSimplificationMetric *simplificationMetric)
        Simplify the Reeb graph given a threshold
        'simplification_threshold' (between 0 and 1).
        
        This method is the core feature for Reeb graph multi-resolution
        hierarchy construction.
        
        Return the number of arcs that have been removed through the
        simplification process.
        
        'simplification_threshold' represents a "scale", under which each
        Reeb graph feature is considered as noise.
        'simplification_threshold' is expressed as a fraction of the
        scalar field overall span. It can vary from 0 (no simplification)
        to 1 (maximal simplification).
        
        'simplification_metric' is an object in charge of evaluating the
        importance of a Reeb graph arc at each step of the simplification
        process. if 'simplification_metric' is NULL, the default strategy
        (persitence of the scalar field) is used. Customized
        simplification metric evaluation algorithm can be designed (see
        ReebGraphSimplificationMetric), enabling the user to control
        the definition of what should be considered as noise or signal.
        
        References:
        
        "Topological persistence and simplification", H. Edelsbrunner, D.
        Letscher, and A. Zomorodian, Discrete Computational Geometry,
        28:511-533, 2002.
        
        "Extreme elevation on a 2-manifold", P.K. Agarwal, H.
        Edelsbrunner, J. Harer, and Y. Wang, ACM Symposium on
        Computational Geometry, pp. 357-365, 2004.
        
        "Simplifying flexible isosurfaces using local geometric
        measures", H. Carr, J. Snoeyink, M van de Panne, IEEE
        Visualization, 497-504, 2004
        
        "Loop surgery for volumetric meshes: Reeb graphs reduced to contour
        trees", J. Tierny, A. Gyulassy, E. Simon, V. Pascucci, IEEE
        Trans. on Vis. and Comp. Graph. (Proc of IEEE VIS),
        15:1177-1184,2009.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Simplify, *my_args)
        return ret

    def stream_tetrahedron(self, *args):
        """
        V.stream_tetrahedron(int, float, int, float, int, float, int,
            float) -> int
        C++: int StreamTetrahedron(IdType vertex0Id, double scalar0,
            IdType vertex1Id, double scalar1, IdType vertex2Id,
            double scalar2, IdType vertex3Id, double scalar3)
        Streaming Reeb graph computation. Add to the streaming
        computation the tetrahedra of the UnstructuredGrid volume mesh
        described by vertex_0_id, scalar0 vertex_1_id, scalar1 vertex_2_id,
        scalar2 vertex_3_id, scalar3
        
        	where vertex_id is the Id of the vertex in the
        UnstructuredGrid structure and scalaris the corresponding
        scalar field value.
        
        IMPORTANT: The stream _must_ be finalized with the "_close_stream"
        call.
        """
        ret = self._wrap_call(self._vtk_obj.StreamTetrahedron, *args)
        return ret

    def stream_triangle(self, *args):
        """
        V.stream_triangle(int, float, int, float, int, float) -> int
        C++: int StreamTriangle(IdType vertex0Id, double scalar0,
            IdType vertex1Id, double scalar1, IdType vertex2Id,
            double scalar2)
        Streaming Reeb graph computation. Add to the streaming
        computation the triangle of the PolyData surface mesh
        described by vertex_0_id, scalar0 vertex_1_id, scalar1 vertex_2_id,
        scalar2
        
        	where vertex_id is the Id of the vertex in the PolyData
        structure and scalaris the corresponding scalar field value.
        
        IMPORTANT: The stream _must_ be finalized with the "_close_stream"
        call.
        """
        ret = self._wrap_call(self._vtk_obj.StreamTriangle, *args)
        return ret

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('update_number_of_pieces',
    'GetUpdateNumberOfPieces'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('update_ghost_level',
    'GetUpdateGhostLevel'), ('update_extent', 'GetUpdateExtent'),
    ('debug', 'GetDebug'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('global_release_data_flag', 'GetGlobalReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('whole_extent',
    'GetWholeExtent'), ('request_exact_extent', 'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
    'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ReebGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ReebGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit ReebGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ReebGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

