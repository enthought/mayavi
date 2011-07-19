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

from tvtk.tvtk_classes.point_set import PointSet


class PolyData(PointSet):
    """
    PolyData - concrete dataset represents vertices, lines, polygons,
    and triangle strips
    
    Superclass: PointSet
    
    PolyData is a data object that is a concrete implementation of
    DataSet. PolyData represents a geometric structure consisting
    of vertices, lines, polygons, and/or triangle strips. Point and cell
    attribute values (e.g., scalars, vectors, etc.) also are represented.
    
    The actual cell types (vtk_cell_type.h) supported by PolyData are:
    Vertex, PolyVertex, Line, PolyLine, Triangle, Quad,
    Polygon, and TriangleStrip.
    
    One important feature of PolyData objects is that special
    traversal and data manipulation methods are available to process
    data. These methods are generally more efficient than DataSet
    methods and should be used whenever possible. For example, traversing
    the cells in a dataset we would use get_cell(). To traverse cells with
    PolyData we would retrieve the cell array object representing
    polygons (for example using get_polys()) and then use CellArray's
    init_traversal() and get_next_cell() methods.
    
    Caveats:
    
    Because PolyData is implemented with four separate instances of
    CellArray to represent 0d vertices, 1d lines, 2d polygons, and 2d
    triangle strips, it is possible to create PolyData instances that
    consist of a mixture of cell types. Because of the design of the
    class, there are certain limitations on how mixed cell types are
    inserted into the PolyData, and in turn the order in which they
    are processed and rendered. To preserve the consistency of cell ids,
    and to insure that cells with cell data are rendered properly, users
    must insert mixed cells in the order of vertices (vtk_vertex and
    PolyVertex), lines (vtk_line and PolyLine), polygons
    (vtk_triangle, Quad, Polygon), and triangle strips
    (vtk_triangle_strip).
    
    Some filters when processing PolyData with mixed cell types may
    process the cells in differing ways. Some will convert one type into
    another (e.g., TriangleStrip into Triangles) or expect a
    certain type (vtk_decimate_pro expects triangles or triangle strips;
    TubeFilter expects lines). Read the documentation for each filter
    carefully to understand how each part of PolyData is processed.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyData, obj, update, **traits)
    
    def _get_polys(self):
        return wrap_vtk(self._vtk_obj.GetPolys())
    def _set_polys(self, arg):
        old_val = self._get_polys()
        my_arg = deref_array([arg], [['vtkCellArray']])
        self._wrap_call(self._vtk_obj.SetPolys,
                        my_arg[0])
        self.trait_property_changed('polys', old_val, arg)
    polys = traits.Property(_get_polys, _set_polys, help=\
        """
        Get the cell array defining polygons. If there are no polygons,
        an empty array will be returned (convenience to simplify
        traversal).
        """
    )

    def _get_strips(self):
        return wrap_vtk(self._vtk_obj.GetStrips())
    def _set_strips(self, arg):
        old_val = self._get_strips()
        my_arg = deref_array([arg], [['vtkCellArray']])
        self._wrap_call(self._vtk_obj.SetStrips,
                        my_arg[0])
        self.trait_property_changed('strips', old_val, arg)
    strips = traits.Property(_get_strips, _set_strips, help=\
        """
        Get the cell array defining triangle strips. If there are no
        triangle strips, an empty array will be returned (convenience to
        simplify traversal).
        """
    )

    def _get_lines(self):
        return wrap_vtk(self._vtk_obj.GetLines())
    def _set_lines(self, arg):
        old_val = self._get_lines()
        my_arg = deref_array([arg], [['vtkCellArray']])
        self._wrap_call(self._vtk_obj.SetLines,
                        my_arg[0])
        self.trait_property_changed('lines', old_val, arg)
    lines = traits.Property(_get_lines, _set_lines, help=\
        """
        Get the cell array defining lines. If there are no lines, an
        empty array will be returned (convenience to simplify traversal).
        """
    )

    def _get_verts(self):
        return wrap_vtk(self._vtk_obj.GetVerts())
    def _set_verts(self, arg):
        old_val = self._get_verts()
        my_arg = deref_array([arg], [['vtkCellArray']])
        self._wrap_call(self._vtk_obj.SetVerts,
                        my_arg[0])
        self.trait_property_changed('verts', old_val, arg)
    verts = traits.Property(_get_verts, _set_verts, help=\
        """
        Get the cell array defining vertices. If there are no vertices,
        an empty array will be returned (convenience to simplify
        traversal).
        """
    )

    def get_cell_edge_neighbors(self, *args):
        """
        V.get_cell_edge_neighbors(int, int, int, IdList)
        C++: void GetCellEdgeNeighbors(IdType cellId, IdType p1,
            IdType p2, IdList *cellIds)
        Get the neighbors at an edge. More efficient than the general
        get_cell_neighbors(). Assumes links have been built (with
        build_links()), and looks specifically for edge neighbors.
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetCellEdgeNeighbors, *my_args)
        return ret

    def _get_ghost_level(self):
        return self._vtk_obj.GetGhostLevel()
    ghost_level = traits.Property(_get_ghost_level, help=\
        """
        Get the ghost level.
        """
    )

    def _get_number_of_lines(self):
        return self._vtk_obj.GetNumberOfLines()
    number_of_lines = traits.Property(_get_number_of_lines, help=\
        """
        Return the number of primitives of a particular type held..
        """
    )

    def _get_number_of_pieces(self):
        return self._vtk_obj.GetNumberOfPieces()
    number_of_pieces = traits.Property(_get_number_of_pieces, help=\
        """
        Get the piece and the number of pieces. Similar to extent in 3d.
        """
    )

    def _get_number_of_polys(self):
        return self._vtk_obj.GetNumberOfPolys()
    number_of_polys = traits.Property(_get_number_of_polys, help=\
        """
        Return the number of primitives of a particular type held..
        """
    )

    def _get_number_of_strips(self):
        return self._vtk_obj.GetNumberOfStrips()
    number_of_strips = traits.Property(_get_number_of_strips, help=\
        """
        Return the number of primitives of a particular type held..
        """
    )

    def _get_number_of_verts(self):
        return self._vtk_obj.GetNumberOfVerts()
    number_of_verts = traits.Property(_get_number_of_verts, help=\
        """
        Return the number of primitives of a particular type held..
        """
    )

    def _get_piece(self):
        return self._vtk_obj.GetPiece()
    piece = traits.Property(_get_piece, help=\
        """
        Get the piece and the number of pieces. Similar to extent in 3d.
        """
    )

    def get_scalar_field_critical_index(self, *args):
        """
        V.get_scalar_field_critical_index(int, DataArray) -> int
        C++: int GetScalarFieldCriticalIndex(IdType pointId,
            DataArray *scalarField)
        V.get_scalar_field_critical_index(int, int) -> int
        C++: int GetScalarFieldCriticalIndex(IdType pointId,
            int fieldId)
        V.get_scalar_field_critical_index(int, string) -> int
        C++: int GetScalarFieldCriticalIndex(IdType pointId,
            const char *fieldName)
        Scalar field critical point classification (for manifold 2d
        meshes). Reference: J. Milnor "Morse Theory", Princeton
        University Press, 1963.
        
        Given a point_id and an attribute representing a scalar field,
        this member returns the index of the critical point:
        PolyData::MINIMUM (index 0): local minimum;
        PolyData::SADDLE  (index 1): local saddle;
        PolyData::MAXIMUM (index 2): local maximum.
        
        Other returned values are: PolyData::REGULAR_POINT: regular
        point (the gradient does not vanish);
        PolyData::ERR_NON_MANIFOLD_STAR: the star of the considered
        vertex is not manifold (could not evaluate the index)
        PolyData::ERR_INCORRECT_FIELD: the number of entries in the
        scalar field array is different form the number of vertices in
        the mesh. PolyData::ERR_NO_SUCH_FIELD: the specified scalar
        field does not exist.
        """
        my_args = deref_array(args, [('int', 'vtkDataArray'), ('int', 'int'), ('int', 'string')])
        ret = self._wrap_call(self._vtk_obj.GetScalarFieldCriticalIndex, *my_args)
        return ret

    def add_cell_reference(self, *args):
        """
        V.add_cell_reference(int)
        C++: void AddCellReference(IdType cellId)
        Add references to cell in cell structure. This means the links
        from the cell's points to the cell are modified. Memory is not
        extended. Use the method resize_cell_list() to resize the link list
        from a point to its using cells. (This operator assumes
        build_links() has been called.)
        """
        ret = self._wrap_call(self._vtk_obj.AddCellReference, *args)
        return ret

    def add_reference_to_cell(self, *args):
        """
        V.add_reference_to_cell(int, int)
        C++: void AddReferenceToCell(IdType ptId, IdType cellId)
        Add a reference to a cell in a particular point's link list. (You
        may also consider using add_cell_reference() to add the references
        from all the cell's points to the cell.) This operator does not
        realloc memory; use the operator resize_cell_list() to do this if
        necessary.
        """
        ret = self._wrap_call(self._vtk_obj.AddReferenceToCell, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int)
        C++: void Allocate(IdType numCells=1000, int extSize=1000)
        V.allocate(PolyData, int, int)
        C++: void Allocate(PolyData *inPolyData,
            IdType numCells=1000, int extSize=1000)
        Method allocates initial storage for vertex, line, polygon, and
        triangle strip arrays. Use this method before the method
        poly_data::_insert_next_cell(). (Or, provide vertex, line, polygon,
        and triangle strip cell arrays.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Allocate, *my_args)
        return ret

    def build_cells(self):
        """
        V.build_cells()
        C++: void BuildCells()
        Create data structure that allows random access of cells.
        """
        ret = self._vtk_obj.BuildCells()
        return ret
        

    def build_links(self, *args):
        """
        V.build_links(int)
        C++: void BuildLinks(int initialSize=0)
        Create upward links from points to cells that use each point.
        Enables topologically complex queries. Normally the links array
        is allocated based on the number of points in the PolyData.
        The optional initial_size parameter can be used to allocate a
        larger size initially.
        """
        ret = self._wrap_call(self._vtk_obj.BuildLinks, *args)
        return ret

    def copy_cells(self, *args):
        """
        V.copy_cells(PolyData, IdList, PointLocator)
        C++: void CopyCells(PolyData *pd, IdList *idList,
            PointLocator *locator=NULL)
        Copy cells listed in id_list from pd, including points, point
        data, and cell data.  This method assumes that point and cell
        data have been allocated.  If you pass in a point locator, then
        the points won't be duplicated in the output.
        """
        my_args = deref_array(args, [('vtkPolyData', 'vtkIdList', 'vtkPointLocator')])
        ret = self._wrap_call(self._vtk_obj.CopyCells, *my_args)
        return ret

    def delete_cell(self, *args):
        """
        V.delete_cell(int)
        C++: void DeleteCell(IdType cellId)
        Mark a point/cell as deleted from this PolyData.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteCell, *args)
        return ret

    def delete_cells(self):
        """
        V.delete_cells()
        C++: void DeleteCells()
        Release data structure that allows random access of the cells.
        This must be done before a 2nd call to build_links(). delete_cells
        implicitly deletes the links as well since they are no longer
        valid.
        """
        ret = self._vtk_obj.DeleteCells()
        return ret
        

    def delete_links(self):
        """
        V.delete_links()
        C++: void DeleteLinks()
        Release the upward links from point to cells that use each point.
        """
        ret = self._vtk_obj.DeleteLinks()
        return ret
        

    def delete_point(self, *args):
        """
        V.delete_point(int)
        C++: void DeletePoint(IdType ptId)
        Mark a point/cell as deleted from this PolyData.
        """
        ret = self._wrap_call(self._vtk_obj.DeletePoint, *args)
        return ret

    def insert_next_cell(self, *args):
        """
        V.insert_next_cell(int, IdList) -> int
        C++: int InsertNextCell(int type, IdList *pts)
        Insert a cell of type VTK_VERTEX, VTK_POLY_VERTEX, VTK_LINE,
        VTK_POLY_LINE, VTK_TRIANGLE, VTK_QUAD, VTK_POLYGON, or
        VTK_TRIANGLE_STRIP.  Make sure that the poly_data::_allocate()
        function has been called first or that vertex, line, polygon, and
        triangle strip arrays have been supplied. Note: will also insert
        VTK_PIXEL, but converts it to VTK_QUAD.
        """
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.InsertNextCell, *my_args)
        return ret

    def insert_next_linked_point(self, *args):
        """
        V.insert_next_linked_point(int) -> int
        C++: int InsertNextLinkedPoint(int numLinks)
        V.insert_next_linked_point([float, float, float], int) -> int
        C++: int InsertNextLinkedPoint(double x[3], int numLinks)
        Add a point to the cell data structure (after cell pointers have
        been built). This method adds the point and then allocates memory
        for the links to the cells.  (To use this method, make sure
        points are available and build_links() has been invoked.) Of the
        two methods below, one inserts a point coordinate and the other
        just makes room for cell links.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextLinkedPoint, *args)
        return ret

    def is_edge(self, *args):
        """
        V.is_edge(int, int) -> int
        C++: int IsEdge(IdType p1, IdType p2)
        Determine whether two points form an edge. If they do, return
        non-zero. By definition poly_vertex and poly_line have no edges
        since 1-dimensional edges are only found on cells 2d and higher.
        Edges are defined as 1-D boundary entities to cells. Make sure
        build_links() has been called first.
        """
        ret = self._wrap_call(self._vtk_obj.IsEdge, *args)
        return ret

    def is_point_used_by_cell(self, *args):
        """
        V.is_point_used_by_cell(int, int) -> int
        C++: int IsPointUsedByCell(IdType ptId, IdType cellId)
        Determine whether a point is used by a particular cell. If it is,
        return non-zero. Make sure build_cells() has been called first.
        """
        ret = self._wrap_call(self._vtk_obj.IsPointUsedByCell, *args)
        return ret

    def is_triangle(self, *args):
        """
        V.is_triangle(int, int, int) -> int
        C++: int IsTriangle(int v1, int v2, int v3)
        Given three vertices, determine whether it's a triangle. Make
        sure build_links() has been called first.
        """
        ret = self._wrap_call(self._vtk_obj.IsTriangle, *args)
        return ret

    def remove_cell_reference(self, *args):
        """
        V.remove_cell_reference(int)
        C++: void RemoveCellReference(IdType cellId)
        Remove all references to cell in cell structure. This means the
        links from the cell's points to the cell are deleted. Memory is
        not reclaimed. Use the method resize_cell_list() to resize the link
        list from a point to its using cells. (This operator assumes
        build_links() has been called.)
        """
        ret = self._wrap_call(self._vtk_obj.RemoveCellReference, *args)
        return ret

    def remove_deleted_cells(self):
        """
        V.remove_deleted_cells()
        C++: void RemoveDeletedCells()
        The cells marked by calls to delete_cell are stored in the Cell
        Array VTK_EMPTY_CELL, but they still exist in the polys array.
        Calling remove_deleted_cells will travers the poly array and
        remove/compact the cell array as well as any cell data thus truly
        removing the cells from the polydata object. WARNING. This only
        handles the polys at the moment
        """
        ret = self._vtk_obj.RemoveDeletedCells()
        return ret
        

    def remove_ghost_cells(self, *args):
        """
        V.remove_ghost_cells(int)
        C++: void RemoveGhostCells(int level)
        This method will remove any cell that has a ghost level array
        value greater or equal to level.  It does not remove unused
        points (yet).
        """
        ret = self._wrap_call(self._vtk_obj.RemoveGhostCells, *args)
        return ret

    def remove_reference_to_cell(self, *args):
        """
        V.remove_reference_to_cell(int, int)
        C++: void RemoveReferenceToCell(IdType ptId, IdType cellId)
        Remove a reference to a cell in a particular point's link list.
        You may also consider using remove_cell_reference() to remove the
        references from all the cell's points to the cell. This operator
        does not reallocate memory; use the operator resize_cell_list() to
        do this if necessary.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveReferenceToCell, *args)
        return ret

    def replace_cell_point(self, *args):
        """
        V.replace_cell_point(int, int, int)
        C++: void ReplaceCellPoint(IdType cellId, IdType oldPtId,
            IdType newPtId)
        Replace a point in the cell connectivity list with a different
        point.
        """
        ret = self._wrap_call(self._vtk_obj.ReplaceCellPoint, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Begin inserting data all over again. Memory is not freed but
        otherwise objects are returned to their initial state.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def resize_cell_list(self, *args):
        """
        V.resize_cell_list(int, int)
        C++: void ResizeCellList(IdType ptId, int size)
        Resize the list of cells using a particular point. (This operator
        assumes that build_links() has been called.)
        """
        ret = self._wrap_call(self._vtk_obj.ResizeCellList, *args)
        return ret

    def reverse_cell(self, *args):
        """
        V.reverse_cell(int)
        C++: void ReverseCell(IdType cellId)
        Reverse the order of point ids defining the cell.
        """
        ret = self._wrap_call(self._vtk_obj.ReverseCell, *args)
        return ret

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('whole_extent', 'GetWholeExtent'),
    ('update_number_of_pieces', 'GetUpdateNumberOfPieces'),
    ('update_ghost_level', 'GetUpdateGhostLevel'), ('update_extent',
    'GetUpdateExtent'), ('debug', 'GetDebug'), ('release_data_flag',
    'GetReleaseDataFlag'), ('global_release_data_flag',
    'GetGlobalReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('maximum_number_of_pieces', 'GetMaximumNumberOfPieces'),
    ('request_exact_extent', 'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent',
    'maximum_number_of_pieces', 'update_extent', 'update_ghost_level',
    'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_number_of_pieces', 'update_extent',
            'update_ghost_level', 'update_number_of_pieces', 'update_piece',
            'whole_bounding_box', 'whole_extent']),
            title='Edit PolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

