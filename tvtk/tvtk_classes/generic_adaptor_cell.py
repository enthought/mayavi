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


class GenericAdaptorCell(Object):
    """
    GenericAdaptorCell - defines cell interface
    
    Superclass: Object
    
    In VTK, spatial-temporal data is defined in terms of a dataset which
    is composed of cells. The cells are topological entities over which
    an interpolation field is applied. Cells are defined in terms of a
    topology (e.g., vertices, lines, triangles, polygons, tetrahedra,
    etc.), points that instantiate the geometry of the cells, and
    interpolation fields (in the general case one interpolation field is
    for geometry, the other is for attribute data associated with the
    cell).
    
    Currently most algorithms in VTK use Cell and DataSet, which
    make assumptions about the nature of datasets, cells, and attributes.
    In particular, this abstraction assumes that cell interpolation
    functions are linear, or products of linear functions. Further, VTK
    implements most of the interpolation functions. This implementation
    starts breaking down as the complexity of the interpolation (or
    basis) functions increases.
    
    GenericAdaptorCell addresses these issues by providing more
    general abstraction for cells. It also adopts modern C++ practices
    including using iterators. The GenericAdaptorCell is designed to
    fit within the adaptor framework; meaning that it is meant to adapt
    VTK to external simulation systems (see the
    generic_filtering/_readme.html).
    
    Please note that most cells are defined in terms of other cells (the
    boundary cells). They are also defined in terms of points, which are
    not the same as vertices (vertices are a 0-D cell; points represent a
    position in space).
    
    Another important concept is the notion of DOFNodes. These concept
    supports cell types with complex interpolation functions. For
    example, higher-order p-method finite elements may have different
    functions on each of their topological features (edges, faces,
    region). The coefficients of these polynomial functions are
    associated with DOFNodes. (There is a single DOFNode for each
    topological feature.) Note that from this perspective, points are
    used to establish the topological form of the cell; mid-side nodes
    and such are considered DOFNodes.
    
    See Also:
    
    GenericDataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericAdaptorCell, obj, update, **traits)
    
    def get_attribute_order(self, *args):
        """
        V.get_attribute_order(GenericAttribute) -> int
        C++: virtual int GetAttributeOrder(GenericAttribute *a)
        Return the interpolation order of attribute `a' on the cell (may
        differ by cell).
        \pre a_exists: a!=0
        \post positive_result: result>=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetAttributeOrder, *my_args)
        return ret

    def get_boundary_iterator(self, *args):
        """
        V.get_boundary_iterator(GenericCellIterator, int)
        C++: virtual void GetBoundaryIterator(
            GenericCellIterator *boundaries, int dim=-1)
        Return the `boundaries' cells of dimension `dim' (or all
        dimensions less than get_dimension() if -1) that are part of the
        boundary of the cell.
        \pre valid_dim_range: (dim==-1) ||
            ((dim>=_0)&&(dim<_get_dimension()))
        \pre boundaries_exist: boundaries!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBoundaryIterator, *my_args)
        return ret

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float, float, float])
        C++: virtual void GetBounds(double bounds[6])
        Compute the bounding box of the current cell in `bounds' in
        global coordinates. THREAD SAFE
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def _get_dimension(self):
        return self._vtk_obj.GetDimension()
    dimension = traits.Property(_get_dimension, help=\
        """
        Return the topological dimension of the current cell.
        \post valid_result: result>=0 && result<=3
        """
    )

    def _get_geometry_order(self):
        return self._vtk_obj.GetGeometryOrder()
    geometry_order = traits.Property(_get_geometry_order, help=\
        """
        Return the interpolation order of the geometry.
        \post positive_result: result>=0
        """
    )

    def get_highest_order_attribute(self, *args):
        """
        V.get_highest_order_attribute(GenericAttributeCollection) -> int
        C++: virtual int GetHighestOrderAttribute(
            GenericAttributeCollection *ac)
        Return the index of the first point centered attribute with the
        highest order in `ac'.
        \pre ac_exists: ac!=0
        \post valid_result: result>=-1 &&
            result<ac->_get_number_of_attributes()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetHighestOrderAttribute, *my_args)
        return ret

    def _get_id(self):
        return self._vtk_obj.GetId()
    id = traits.Property(_get_id, help=\
        """
        Unique identification number of the cell over the whole data set.
        This unique key may not be contiguous.
        """
    )

    def _get_length2(self):
        return self._vtk_obj.GetLength2()
    length2 = traits.Property(_get_length2, help=\
        """
        Return the bounding box diagonal squared of the current cell.
        \post positive_result: result>=0
        """
    )

    def get_neighbors(self, *args):
        """
        V.get_neighbors(GenericAdaptorCell, GenericCellIterator)
        C++: virtual void GetNeighbors(GenericAdaptorCell *boundary,
            GenericCellIterator *neighbors)
        Put into `neighbors' the cells
        (dimension>boundary->_get_dimension()) of the dataset that share
        the boundary `boundary' with this cell. `this' IS NOT INCLUDED.
        \pre boundary_exists: boundary!=0
        \pre real_boundary: !boundary->_is_in_data_set()
        \pre cell_of_the_dataset: is_in_data_set()
        \pre boundary: has_boundary(boundary)
        \pre neighbors_exist: neighbors!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetNeighbors, *my_args)
        return ret

    def get_number_of_boundaries(self, *args):
        """
        V.get_number_of_boundaries(int) -> int
        C++: virtual int GetNumberOfBoundaries(int dim=-1)
        Return the number of boundaries of dimension `dim' (or all
        dimensions greater than 0 and less than get_dimension() if -1) of
        the cell. When dim is -1, the number of vertices is not included
        in the count because vertices are a special case: a vertex will
        have at most a single field value associated with it; DOF nodes
        may have an arbitrary number of field values associated with
        them.
        \pre valid_dim_range: (dim==-1) ||
            ((dim>=_0)&&(dim<_get_dimension()))
        \post positive_result: result>=0
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfBoundaries, *args)
        return ret

    def _get_number_of_dof_nodes(self):
        return self._vtk_obj.GetNumberOfDOFNodes()
    number_of_dof_nodes = traits.Property(_get_number_of_dof_nodes, help=\
        """
        Accumulated number of DOF nodes of the current cell. A DOF node
        is a component of cell with a given topological dimension. e.g.:
        a triangle has 4 DOF: 1 face and 3 edges. An hexahedron has 19
        DOF: 1 region, 6 faces, and 12 edges.
        
        The number of vertices is not included in the count because
        vertices are a special case: a vertex will have at most a single
        field value associated with it; DOF nodes may have an arbitrary
        number of field values associated with them.
        \post valid_result: result==_get_number_of_boundaries(-_1)+_1
        """
    )

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Return the number of corner points that compose the cell.
        \post positive_result: result>=0
        """
    )

    def get_number_of_vertices_on_face(self, *args):
        """
        V.get_number_of_vertices_on_face(int) -> int
        C++: virtual int GetNumberOfVerticesOnFace(int faceId)
        Return the number of vertices defining face `face_id'.
        \pre is_3d: this->_get_dimension()==_3
        \pre valid_face_id_range: face_id>=_0 &&
            face_id<this->_get_number_of_boundaries(_2)
        \post positive_result: && result>0
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfVerticesOnFace, *args)
        return ret

    def get_parametric_center(self, *args):
        """
        V.get_parametric_center([float, float, float]) -> int
        C++: virtual int GetParametricCenter(double pcoords[3])
        Get the center of the current cell (in parametric coordinates)
        and place it in `pcoords'.  If the current cell is a composite,
        the return value is the sub-cell id that the center is in.  \post
        valid_result: (result>=0) && (_is_primary() implies result==0)
        """
        ret = self._wrap_call(self._vtk_obj.GetParametricCenter, *args)
        return ret

    def get_parametric_distance(self, *args):
        """
        V.get_parametric_distance([float, float, float]) -> float
        C++: virtual double GetParametricDistance(double pcoords[3])
        Return the distance of the parametric coordinate `pcoords' to the
        current cell.  If inside the cell, a distance of zero is
        returned. This is used during picking to get the correct cell
        picked. (The tolerance will occasionally allow cells to be picked
        who are not really intersected "inside" the cell.)  \post
        positive_result: result>=0
        """
        ret = self._wrap_call(self._vtk_obj.GetParametricDistance, *args)
        return ret

    def get_point_iterator(self, *args):
        """
        V.get_point_iterator(GenericPointIterator)
        C++: virtual void GetPointIterator(GenericPointIterator *it)
        Return the points of cell into `it'.
        \pre it_exists: it!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPointIterator, *my_args)
        return ret

    def _get_type(self):
        return self._vtk_obj.GetType()
    type = traits.Property(_get_type, help=\
        """
        Return the type of the current cell.
        \post (result==VTK_HIGHER_ORDER_EDGE)||
              (result==VTK_HIGHER_ORDER_TRIANGLE)||
              (result==VTK_HIGHER_ORDER_TETRAHEDRON)
        """
    )

    def clip(self, *args):
        """
        V.clip(float, ImplicitFunction, GenericAttributeCollection,
            GenericCellTessellator, int, IncrementalPointLocator,
            CellArray, PointData, CellData, PointData,
            PointData, CellData)
        C++: virtual void Clip(double value, ImplicitFunction *f,
            GenericAttributeCollection *attributes,
            GenericCellTessellator *tess, int insideOut,
            IncrementalPointLocator *locator,
            CellArray *connectivity, PointData *outPd,
            CellData *outCd, PointData *internalPd,
            PointData *secondaryPd, CellData *secondaryCd)
        Cut (or clip) the current cell with respect to the contour
        defined by the `value' or the implicit function `f' of the scalar
        attribute
        (`attributes->_get_active_attribute()',`attributes->_get_active_component()'
        ). If `f' exists, `value' is not used. The output is the part of
        the current cell which is inside the contour.  The output is a
        set of zero, one or more cells of the same topological dimension
        as the current cell. Normally, cell points whose scalar value is
        greater than "value" are considered inside. If `inside_out' is on,
        this is reversed.  Clipping interpolates the
        `attributes->_get_number_ofattributes_to_interpolate()' attributes
        `attributes->_get_attributes_to_interpolate()'.  `locator',
        `connectivity', `out_pd' and `out_cd' are cumulative data arrays
        over cell iterations: they store the result of each call to
        Clip():
        - `locator' is a points list that merges points as they are
          inserted (i.e., prevents duplicates).
        - `connectivity' is an array of generated cells
        - `out_pd' is an array of interpolated point data along the edge
          (if not-NULL)
        - `out_cd' is an array of copied cell data of the current cell (if
          not-NULL) `internal_pd', `secondary_pd' and `secondary_cd' are
          initialized by the filter that call it from `attributes'.
        - `internal_pd' stores the result of the tessellation pass: the
          higher-order cell is tessellated into linear sub-cells.
        - `secondary_pd' and `secondary_cd' are use ...
         [Truncated]
        """
        my_args = deref_array(args, [('float', 'vtkImplicitFunction', 'vtkGenericAttributeCollection', 'vtkGenericCellTessellator', 'int', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkCellData', 'vtkPointData', 'vtkPointData', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.Clip, *my_args)
        return ret

    def contour(self, *args):
        """
        V.contour(ContourValues, ImplicitFunction,
            GenericAttributeCollection, GenericCellTessellator,
            IncrementalPointLocator, CellArray, CellArray,
            CellArray, PointData, CellData, PointData,
            PointData, CellData)
        C++: virtual void Contour(ContourValues *values,
            ImplicitFunction *f,
            GenericAttributeCollection *attributes,
            GenericCellTessellator *tess,
            IncrementalPointLocator *locator, CellArray *verts,
            CellArray *lines, CellArray *polys, PointData *outPd,
             CellData *outCd, PointData *internalPd,
            PointData *secondaryPd, CellData *secondaryCd)
        Generate a contour (contouring primitives) for each `values' or
        with respect to an implicit function `f'. Contouring is performed
        on the scalar attribute (`attributes->_get_active_attribute()'
        `attributes->_get_active_component()').  Contouring interpolates the
        `attributes->_get_number_ofattributes_to_interpolate()' attributes
        `attributes->_get_attributes_to_interpolate()'.  The `locator',
        `verts', `lines', `polys', `out_pd' and `out_cd' are cumulative
        data arrays over cell iterations: they store the result of each
        call to Contour():
        - `locator' is a points list that merges points as they are
          inserted (i.e., prevents duplicates).
        - `verts' is an array of generated vertices
        - `lines' is an array of generated lines
        - `polys' is an array of generated polygons
        - `out_pd' is an array of interpolated point data along the edge
          (if not-NULL)
        - `out_cd' is an array of copied cell data of the current cell (if
          not-NULL) `internal_pd', `secondary_pd' and `secondary_cd' are
          initialized by the filter that call it from `attributes'.
        - `internal_pd' stores the result of the tessellation pass: the
          higher-order cell is tessellated into linear sub-cells.
        - `secondary_pd' and `secondary_cd' are used internally as inputs
          to the Contour() method on linear sub-cells. Note: the
          copy_allocate() method must be invoked on both `out_pd' and
         ...
         [Truncated]
        """
        my_args = deref_array(args, [('vtkContourValues', 'vtkImplicitFunction', 'vtkGenericAttributeCollection', 'vtkGenericCellTessellator', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkCellArray', 'vtkCellArray', 'vtkPointData', 'vtkCellData', 'vtkPointData', 'vtkPointData', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.Contour, *my_args)
        return ret

    def count_neighbors(self, *args):
        """
        V.count_neighbors(GenericAdaptorCell) -> int
        C++: virtual int CountNeighbors(GenericAdaptorCell *boundary)
        Number of cells (dimension>boundary->_get_dimension()) of the
        dataset that share the boundary `boundary' of `this'. `this' IS
        NOT INCLUDED.
        \pre boundary_exists: boundary!=0
        \pre real_boundary: !boundary->_is_in_data_set()
        \pre cell_of_the_dataset: is_in_data_set()
        \pre boundary: has_boundary(boundary)
        \post positive_result: result>=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CountNeighbors, *my_args)
        return ret

    def evaluate_location(self, *args):
        """
        V.evaluate_location(int, [float, float, float], [float, float,
            float])
        C++: virtual void EvaluateLocation(int subId, double pcoords[3],
            double x[3])
        Determine the global coordinates `x' from sub-cell `sub_id' and
        parametric coordinates `pcoords' in the cell.
        \pre positive_sub_id: sub_id>=_0
        \pre clamped_pcoords:
            (0<=pcoords[0])&&(pcoords[0]<=1)&&(0<=pcoords[1])
        &&(pcoords[1]<=1)&&(0<=pcoords[2])&&(pcoords[2]<=1)
        """
        ret = self._wrap_call(self._vtk_obj.EvaluateLocation, *args)
        return ret

    def intersect_with_line(self, *args):
        """
        V.intersect_with_line([float, float, float], [float, float, float],
            float, float, [float, float, float], [float, float, float],
            int) -> int
        C++: virtual int IntersectWithLine(double p1[3], double p2[3],
            double tol, double &t, double x[3], double pcoords[3],
            int &subId)
        Is there an intersection between the current cell and the ray
        (`p1',`p2') according to a tolerance `tol'? If true, `x' is the
        global intersection, `t' is the parametric coordinate for the line,
        `pcoords' are the parametric coordinates for cell. `sub_id' is the
        sub-cell where the intersection occurs.
        \pre positive_tolerance: tol>0
        """
        ret = self._wrap_call(self._vtk_obj.IntersectWithLine, *args)
        return ret

    def is_attribute_linear(self, *args):
        """
        V.is_attribute_linear(GenericAttribute) -> int
        C++: int IsAttributeLinear(GenericAttribute *a)
        Does the attribute `a' have a non-linear interpolation?
        \pre a_exists: a!=0
        \post definition: result==(_get_attribute_order()==_1)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsAttributeLinear, *my_args)
        return ret

    def is_face_on_boundary(self, *args):
        """
        V.is_face_on_boundary(int) -> int
        C++: virtual int IsFaceOnBoundary(IdType faceId)
        Is the face `face_id' of the current cell on the exterior boundary
        of the dataset?
        \pre 3d: get_dimension()==_3
        """
        ret = self._wrap_call(self._vtk_obj.IsFaceOnBoundary, *args)
        return ret

    def is_geometry_linear(self):
        """
        V.is_geometry_linear() -> int
        C++: int IsGeometryLinear()
        Does the cell have a non-linear interpolation for the geometry?
        \post definition: result==(_get_geometry_order()==_1)
        """
        ret = self._vtk_obj.IsGeometryLinear()
        return ret
        

    def is_in_data_set(self):
        """
        V.is_in_data_set() -> int
        C++: virtual int IsInDataSet()
        Does `this' a cell of a dataset? (otherwise, it is a boundary
        cell)
        """
        ret = self._vtk_obj.IsInDataSet()
        return ret
        

    def is_on_boundary(self):
        """
        V.is_on_boundary() -> int
        C++: virtual int IsOnBoundary()
        Is the cell on the exterior boundary of the dataset?
        \pre 2d: get_dimension()==_2
        """
        ret = self._vtk_obj.IsOnBoundary()
        return ret
        

    def is_primary(self):
        """
        V.is_primary() -> int
        C++: virtual int IsPrimary()
        Is the cell primary (i.e. not composite) ?
        """
        ret = self._vtk_obj.IsPrimary()
        return ret
        

    def new_cell_iterator(self):
        """
        V.new_cell_iterator() -> GenericCellIterator
        C++: virtual GenericCellIterator *NewCellIterator()
        Create an empty cell iterator. The user is responsible for
        deleting it.
        \post result_exists: result!=0
        """
        ret = wrap_vtk(self._vtk_obj.NewCellIterator())
        return ret
        

    def tessellate(self, *args):
        """
        V.tessellate(GenericAttributeCollection,
            GenericCellTessellator, Points,
            IncrementalPointLocator, CellArray, PointData,
            PointData, CellData, UnsignedCharArray)
        C++: virtual void Tessellate(
            GenericAttributeCollection *attributes,
            GenericCellTessellator *tess, Points *points,
            IncrementalPointLocator *locator, CellArray *cellArray,
            PointData *internalPd, PointData *pd, CellData *cd,
            UnsignedCharArray *types)
        Tessellate the cell if it is not linear or if at least one
        attribute of `attributes' is not linear. The output are linear
        cells of the same dimension than the cell. If the cell is linear
        and all attributes are linear, the output is just a copy of the
        current cell. `points', `cell_array', `pd' and `cd' are cumulative
        output data arrays over cell iterations: they store the result of
        each call to Tessellate(). `internal_pd' is initialized by the
        calling filter and stores the result of the tessellation. If it
        is not null, `types' is filled with the types of the linear
        cells. `types' is null when it is called from
        GenericGeometryFilter and not null when it is called from
        GenericDatasetTessellator.
        \pre attributes_exist: attributes!=0
        \pre tessellator_exists: tess!=0
        \pre points_exist: points!=0
        \pre cell_array_exists: cell_array!=_0
        \pre internal_pd_exists: internal_pd!=_0
        \pre pd_exist: pd!=0
        \pre cd_exists: cd!=0
        """
        my_args = deref_array(args, [('vtkGenericAttributeCollection', 'vtkGenericCellTessellator', 'vtkPoints', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'vtkUnsignedCharArray')])
        ret = self._wrap_call(self._vtk_obj.Tessellate, *my_args)
        return ret

    def triangulate_face(self, *args):
        """
        V.triangulate_face(GenericAttributeCollection,
            GenericCellTessellator, int, Points,
            IncrementalPointLocator, CellArray, PointData,
            PointData, CellData)
        C++: virtual void TriangulateFace(
            GenericAttributeCollection *attributes,
            GenericCellTessellator *tess, int index, Points *points,
             IncrementalPointLocator *locator, CellArray *cellArray,
             PointData *internalPd, PointData *pd, CellData *cd)
        Tessellate face `index' of the cell. See Tessellate() for further
        explanations.
        \pre cell_is_3d: get_dimension()==_3
        \pre attributes_exist: attributes!=0
        \pre tessellator_exists: tess!=0
        \pre valid_face: index>=0
        \pre points_exist: points!=0
        \pre cell_array_exists: cell_array!=_0
        \pre internal_pd_exists: internal_pd!=_0
        \pre pd_exist: pd!=0
        \pre cd_exists: cd!=0
        """
        my_args = deref_array(args, [('vtkGenericAttributeCollection', 'vtkGenericCellTessellator', 'int', 'vtkPoints', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.TriangulateFace, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericAdaptorCell, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericAdaptorCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit GenericAdaptorCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericAdaptorCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

