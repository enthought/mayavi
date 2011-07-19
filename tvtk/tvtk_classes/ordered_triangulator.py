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

from tvtk.tvtk_classes.object import Object


class OrderedTriangulator(Object):
    """
    OrderedTriangulator - helper class to generate triangulations
    
    Superclass: Object
    
    This class is used to generate unique triangulations of points. The
    uniqueness of the triangulation is controlled by the id of the
    inserted points in combination with a Delaunay criterion. The class
    is designed to be as fast as possible (since the algorithm can be
    slow) and uses block memory allocations to support rapid
    triangulation generation. Also, the assumption behind the class is
    that a maximum of hundreds of points are to be triangulated. If you
    desire more robust triangulation methods use
    Polygon::Triangulate(), Delaunay2D, or Delaunay3D.
    
    Background:
    
    This work is documented in the technical paper: W.J. Schroeder, B.
    Geveci, M. Malaterre. Compatible Triangulations of Spatial
    Decompositions. In Proceedings of Visualization 2004, IEEE Press
    October 2004.
    
    Delaunay triangulations are unique assuming a random distribution of
    input points. The 3d Delaunay criterion is as follows: the
    circumsphere of each tetrahedron contains no other points of the
    triangulation except for the four points defining the tetrahedron. 
    In application this property is hard to satisfy because objects like
    cubes are defined by eight points all sharing the same circumsphere
    (center and radius); hence the Delaunay triangulation is not unique. 
    These so-called degenerate situations are typically resolved by
    arbitrary selecting a triangulation. This code does something
    different: it resolves degenerate triangulations by modifying the
    "_in_circumsphere" method to use a slightly smaller radius. Hence,
    degenerate points are always considered "out" of the circumsphere.
    This, in combination with an ordering (based on id) of the input
    points, guarantees a unique triangulation.
    
    There is another related characteristic of Delaunay triangulations.
    Given a N-dimensional Delaunay triangulation, points lying on a (N-1)
    dimensional plane also form a (N-1) Delaunay triangulation. This
    means for example, that if a 3d cell is defined by a set of (_2d)
    planar faces, then the face triangulations are Delaunay. Combining
    this with the method to generate unique triangulations described
    previously, the triangulations on the face are guaranteed unique.
    This fact can be used to triangulate 3d objects in such a way to
    guarantee compatible face triangulations. This is a very useful fact
    for parallel processing, or performing operations like clipping that
    require compatible triangulations across 3d cell faces. (See
    ClipVolume for an example.)
    
    A special feature of this class is that it can generate triangulation
    templates on the fly. If template triangulation is enabled, then the
    ordered triangulator will first triangulate the cell using the slower
    ordered Delaunay approach, and then store the result as a template.
    Later, if the same cell type and cell configuration is encountered,
    then the template is reused which greatly speeds the triangulation.
    
    Caveats:
    
    Duplicate vertices will be ignored, i.e., if two points have the same
    coordinates the second one is discarded. The implications are that
    the user of this class must prevent duplicate points. Because the
    precision of this algorithm is double, it's also a good idea to merge
    points that are within some epsilon of one another.
    
    The triangulation is performed using the parametric coordinates of
    the inserted points. Therefore the bounds (see init_triangulation())
    should represent the range of the parametric coordinates of the
    inserted points.
    
    See Also:
    
    Delaunay2D Delaunay3D Polygon
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOrderedTriangulator, obj, update, **traits)
    
    use_two_sort_ids = tvtk_base.false_bool_trait(help=\
        """
        Tells the triangulator that a second sort id is provided for each
        point and should also be considered when sorting.
        """
    )
    def _use_two_sort_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseTwoSortIds,
                        self.use_two_sort_ids_)

    pre_sorted = tvtk_base.false_bool_trait(help=\
        """
        Boolean indicates whether the points have been pre-sorted. If
        pre-sorted is enabled, the points are not sorted on point id. By
        default, presorted is off. (The point id is defined in
        insert_point().)
        """
    )
    def _pre_sorted_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreSorted,
                        self.pre_sorted_)

    use_templates = tvtk_base.false_bool_trait(help=\
        """
        If this flag is set, then the ordered triangulator will create
        and use templates for the triangulation. To use templates, the
        template_triangulate() method should be called when appropriate.
        (Note: the template_triangulate() method works for complete
        (interior) cells without extra points due to intersection, etc.)
        """
    )
    def _use_templates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseTemplates,
                        self.use_templates_)

    def get_next_tetra(self, *args):
        """
        V.get_next_tetra(int, Tetra, DataArray, DoubleArray) -> int
        C++: int GetNextTetra(int classification, Tetra *tet,
            DataArray *cellScalars, DoubleArray *tetScalars)
        Methods to get one tetra at a time. Start with
        init_tetra_traversal() and then invoke get_next_tetra() until the
        method returns 0. cell_scalars are point-centered scalars on the
        original cell. tet_scalars are point-centered scalars on the
        tetra: the values will be copied from cell_scalars.
        \pre tet_exists: tet!=0
        \pre cell_scalars_exists: cell_scalars!=_0
        \pre tet_scalars_exists: tet_scalars!=_0
        \pre tet_scalars_valid_size: tet_scalars->_get_number_of_tuples()==_4
        """
        my_args = deref_array(args, [('int', 'vtkTetra', 'vtkDataArray', 'vtkDoubleArray')])
        ret = self._wrap_call(self._vtk_obj.GetNextTetra, *my_args)
        return ret

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Return the number of inserted points.
        """
    )

    def get_point_id(self, *args):
        """
        V.get_point_id(int) -> int
        C++: IdType GetPointId(IdType internalId)
        Return the Id of point `internal_id'. This id is the one passed in
        argument of insert_point. It assumes that the point has already
        been inserted. The method should be invoked prior to the
        Triangulate method.
        \pre valid_range: internal_id>=_0 &&
            internal_id<this->_get_number_of_points()
        """
        ret = self._wrap_call(self._vtk_obj.GetPointId, *args)
        return ret

    def get_tetras(self, *args):
        """
        V.get_tetras(int, UnstructuredGrid) -> int
        C++: IdType GetTetras(int classification,
            UnstructuredGrid *ugrid)
        Initialize and add the tetras and points from the triangulation
        to the unstructured grid provided.  New points are created and
        the mesh is allocated. (This method differs from add_tetras() in
        that it inserts points and cells; add_tetras only adds the tetra
        cells.) The tetrahdera added are of the type specified
        (0=inside,1=outside,2=all). Inside tetrahedron are those whose
        points are classified "inside" or on the "boundary."  Outside
        tetrahedron have at least one point classified "outside."  The
        method returns the number of tetrahedrahedron of the type
        requested.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetTetras, *my_args)
        return ret

    def add_tetras(self, *args):
        """
        V.add_tetras(int, UnstructuredGrid) -> int
        C++: IdType AddTetras(int classification,
            UnstructuredGrid *ugrid)
        V.add_tetras(int, CellArray) -> int
        C++: IdType AddTetras(int classification,
            CellArray *connectivity)
        V.add_tetras(int, IncrementalPointLocator, CellArray,
            PointData, PointData, CellData, int, CellData)
            -> int
        C++: IdType AddTetras(int classification,
            IncrementalPointLocator *locator,
            CellArray *outConnectivity, PointData *inPD,
            PointData *outPD, CellData *inCD, IdType cellId,
            CellData *outCD)
        V.add_tetras(int, IdList, Points) -> int
        C++: IdType AddTetras(int classification, IdList *ptIds,
            Points *pts)
        Add the tetras to the unstructured grid provided. The
        unstructured grid is assumed to have been initialized (with
        Allocate()) and points set (with set_points()). The tetrahdera
        added are of the type specified (0=inside,1=outside,2=all).
        Inside tetrahedron are those whose points are classified "inside"
        or on the "boundary." Outside tetrahedron have at least one point
        classified "outside." The method returns the number of
        tetrahedrahedron of the type requested.
        """
        my_args = deref_array(args, [('int', 'vtkUnstructuredGrid'), ('int', 'vtkCellArray'), ('int', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData'), ('int', 'vtkIdList', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.AddTetras, *my_args)
        return ret

    def add_triangles(self, *args):
        """
        V.add_triangles(CellArray) -> int
        C++: IdType AddTriangles(CellArray *connectivity)
        V.add_triangles(int, CellArray) -> int
        C++: IdType AddTriangles(IdType id,
            CellArray *connectivity)
        Add the triangle faces classified (2=boundary) to the
        connectivity list provided. The method returns the number of
        triangles.
        """
        my_args = deref_array(args, [['vtkCellArray'], ('int', 'vtkCellArray')])
        ret = self._wrap_call(self._vtk_obj.AddTriangles, *my_args)
        return ret

    def init_tetra_traversal(self):
        """
        V.init_tetra_traversal()
        C++: void InitTetraTraversal()
        Methods to get one tetra at a time. Start with
        init_tetra_traversal() and then invoke get_next_tetra() until the
        method returns 0.
        """
        ret = self._vtk_obj.InitTetraTraversal()
        return ret
        

    def init_triangulation(self, *args):
        """
        V.init_triangulation(float, float, float, float, float, float, int)
        C++: void InitTriangulation(double xmin, double xmax, double ymin,
             double ymax, double zmin, double zmax, int numPts)
        V.init_triangulation([float, float, float, float, float, float],
            int)
        C++: void InitTriangulation(double bounds[6], int numPts)
        Initialize the triangulation process. Provide a bounding box and
        the maximum number of points to be inserted. Note that since the
        triangulation is performed using parametric coordinates (see
        insert_point()) the bounds should be represent the range of the
        parametric coordinates inserted.
        \post no_point_inserted: get_number_of_points()==_0
        """
        ret = self._wrap_call(self._vtk_obj.InitTriangulation, *args)
        return ret

    def insert_point(self, *args):
        """
        V.insert_point(int, [float, float, float], [float, float, float],
            int) -> int
        C++: IdType InsertPoint(IdType id, double x[3], double p[3],
             int type)
        V.insert_point(int, int, [float, float, float], [float, float,
            float], int) -> int
        C++: IdType InsertPoint(IdType id, IdType sortid,
            double x[3], double p[3], int type)
        V.insert_point(int, int, int, [float, float, float], [float, float,
             float], int) -> int
        C++: IdType InsertPoint(IdType id, IdType sortid,
            IdType sortid2, double x[3], double p[3], int type)
        For each point to be inserted, provide an id, a position x,
        parametric coordinate p, and whether the point is inside
        (type=0), outside (type=1), or on the boundary (type=2). You must
        call init_triangulation() prior to invoking this method. Make sure
        that the number of points inserted does not exceed the num_pts
        specified in init_triangulation(). Also note that the "id" can be
        any integer and can be greater than num_pts. It is used to create
        tetras (in add_tetras()) with the appropriate connectivity ids.
        The method returns an internal id that can be used prior to the
        Triangulate() method to update the type of the point with
        update_point_type(). (Note: the algorithm triangulated with the
        parametric coordinate p[3] and creates tetras with the global
        coordinate x[3]. The parametric coordinates and global
        coordinates may be the same.)
        """
        ret = self._wrap_call(self._vtk_obj.InsertPoint, *args)
        return ret

    def template_triangulate(self, *args):
        """
        V.template_triangulate(int, int, int)
        C++: void TemplateTriangulate(int cellType, int numPts,
            int numEdges)
        Perform the triangulation. (Complete all calls to insert_point()
        prior to invoking this method.) A special version is available
        when templates should be used.
        """
        ret = self._wrap_call(self._vtk_obj.TemplateTriangulate, *args)
        return ret

    def triangulate(self):
        """
        V.triangulate()
        C++: void Triangulate()
        Perform the triangulation. (Complete all calls to insert_point()
        prior to invoking this method.) A special version is available
        when templates should be used.
        """
        ret = self._vtk_obj.Triangulate()
        return ret
        

    def update_point_type(self, *args):
        """
        V.update_point_type(int, int)
        C++: void UpdatePointType(IdType internalId, int type)
        Update the point type. This is useful when the merging of nearly
        coincident points is performed. The id is the internal id
        returned from insert_point(). The method should be invoked prior
        to the Triangulate method. The type is specified as inside
        (type=0), outside (type=1), or on the boundary (type=2).
        \pre valid_range: internal_id>=_0 &&
            internal_id<this->_get_number_of_points()
        """
        ret = self._wrap_call(self._vtk_obj.UpdatePointType, *args)
        return ret

    _updateable_traits_ = \
    (('use_templates', 'GetUseTemplates'), ('debug', 'GetDebug'),
    ('use_two_sort_ids', 'GetUseTwoSortIds'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'),
    ('pre_sorted', 'GetPreSorted'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pre_sorted', 'use_templates',
    'use_two_sort_ids'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OrderedTriangulator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OrderedTriangulator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['pre_sorted', 'use_templates', 'use_two_sort_ids'],
            [], []),
            title='Edit OrderedTriangulator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OrderedTriangulator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

