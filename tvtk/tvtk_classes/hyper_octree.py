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

from tvtk.tvtk_classes.data_set import DataSet


class HyperOctree(DataSet):
    """
    HyperOctree - A dataset structured as a tree where each node has
    
    Superclass: DataSet
    
    An hyperoctree is a dataset where each node has either exactly 2^n
    children or no child at all if the node is a leaf. `n' is the
    dimension of the dataset (1 (binary tree), 2 (quadtree) or 3 (octree)
    ). The class name comes from the following paper:
    
    
     @ARTICLE{yau-srihari-1983,
      author={Mann-May Yau and Sargur N. Srihari},
      title={A Hierarchical Data Structure for Multidimensional Digital Images},
      journal={Communications of the ACM},
      month={July},
      year={1983},
      volume={26},
      number={7},
      pages={504--515}
      }
     
    
    Each node is a cell. Attributes are associated with cells, not with
    points. The geometry is implicitly given by the size of the root node
    on each axis and position of the center and the orientation. (TODO:
    review center position and orientation). The geometry is then not
    limited to an hybercube but can have a rectangular shape. Attributes
    are associated with leaves. For LOD (Level-Of-Detail) purpose,
    attributes can be computed on none-leaf nodes by computing the
    average values from its children (which can be leaves or not).
    
    By construction, an hyperoctree is efficient in memory usage when the
    geometry is sparse. The LOD feature allows to cull quickly part of
    the dataset.
    
    A couple of filters can be applied on this dataset: contour, outline,
    geometry.
    
    * 3d case (octree) for each node, each child index (from 0 to 7) is
      encoded in the following orientation. It is easy to access each
      child as a cell of a grid. Note also that the binary representation
    is relevant, each bit code a side: bit 0 encodes -x side (0) or +x
      side (1) bit 1 encodes -y side (0) or +y side (1) bit 2 encodes -z
      side (0) or +z side (2)
    - the -z side first
    - 0: -y -x sides
    - 1: -y +x sides
    - 2: +y -x sides
    - 3: +y +x sides
                  +y
     +-+-+        ^
     |2|3|        |
     +-+-+  O +z  +-> +x
     |0|1|
     +-+-+
     
    
    - then the +z side, in counter-clockwise
    - 4: -y -x sides
    - 5: -y +x sides
    - 6: +y -x sides
    - 7: +y +x sides
                  +y
     +-+-+        ^
     |6|7|        |
     +-+-+  O +z  +-> +x
     |4|5|
     +-+-+
     
    
    The cases with fewer dimensions are consistent with the octree case:
    
    * Quadtree: in counter-clockwise
    - 0: -y -x edges
    - 1: -y +x edges
    - 2: +y -x edges
    - 3: +y +x edges
             +y
     +-+-+   ^
     |2|3|   |
     +-+-+  O+-> +x
     |0|1|
     +-+-+
     
    
    * Binary tree:
     +0+1+  O+-> +x
     
    
    Caveats:
    
    It is not a spatial search object! If you looking for this kind of
    octree see CellLocator instead.
    
    See Also:
    
    HyperOctreeAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperOctree, obj, update, **traits)
    
    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    dual_grid_flag = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Switch between returning leaves as cells, or the dual grid.
        """
    )
    def _dual_grid_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDualGridFlag,
                        self.dual_grid_flag)

    dimension = traits.Trait(3, traits.Range(1, 3, enter_set=True, auto_set=False), help=\
        """
        Set the dimension of the tree with `dim'. See get_dimension() for
        details.
        \pre valid_dim: dim>=1 && dim<=3
        \post dimension_is_set: get_dimension()==dim
        """
    )
    def _dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimension,
                        self.dimension)

    size = traits.Array(shape=(3,), value=(1.0, 1.0, 1.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        
        """
    )
    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    def _get_leaf_data(self):
        return wrap_vtk(self._vtk_obj.GetLeafData())
    leaf_data = traits.Property(_get_leaf_data, help=\
        """
        A generic way to set the leaf data attributes. This can be either
        point data for dual or cell data for normal grid.
        """
    )

    def get_max_number_of_cells_on_boundary(self, *args):
        """
        V.get_max_number_of_cells_on_boundary(int) -> int
        C++: IdType GetMaxNumberOfCellsOnBoundary(int level)
        Return the number of cells corresponding to the boundary of a
        cell of level `level' where all the leaves at at the last level.
        \pre positive_level: level>=0 && level<this->_get_number_of_levels()
        \post positive_result: result>=0
        """
        ret = self._wrap_call(self._vtk_obj.GetMaxNumberOfCellsOnBoundary, *args)
        return ret

    def get_max_number_of_points(self, *args):
        """
        V.get_max_number_of_points(int) -> int
        C++: IdType GetMaxNumberOfPoints(int level)
        Return the number of points corresponding to an hyperoctree
        starting at level `level' where all the leaves at at the last
        level. In this case, the hyperoctree is like a uniform grid. So
        this number is the number of points of the uniform grid.
        \pre positive_level: level>=0 && level<this->_get_number_of_levels()
        \post definition:
            result==(_2^(_get_number_of_levels()-level-_1)+_1)^_get_dimension()
        """
        ret = self._wrap_call(self._vtk_obj.GetMaxNumberOfPoints, *args)
        return ret

    def get_max_number_of_points_on_boundary(self, *args):
        """
        V.get_max_number_of_points_on_boundary(int) -> int
        C++: IdType GetMaxNumberOfPointsOnBoundary(int level)
        Return the number of points corresponding to the boundary of an
        hyperoctree starting at level `level' where all the leaves at at
        the last level. In this case, the hyperoctree is like a uniform
        grid. So this number is the number of points of on the boundary
        of the uniform grid. For an octree, the boundary are the faces.
        For a quadtree, the boundary are the edges.
        \pre 2d_or_3d: this->_get_dimension()==_2 || this->_get_dimension()==_3
        \pre positive_level: level>=0 && level<this->_get_number_of_levels()
        \post min_result:
            result>=_get_max_number_of_points(this->_get_number_of_levels()-_1)
        \post max_result: result<=_get_max_number_of_points(level)
        """
        ret = self._wrap_call(self._vtk_obj.GetMaxNumberOfPointsOnBoundary, *args)
        return ret

    def _get_number_of_leaves(self):
        return self._vtk_obj.GetNumberOfLeaves()
    number_of_leaves = traits.Property(_get_number_of_leaves, help=\
        """
        Get the number of leaves in the tree.
        """
    )

    def _get_number_of_levels(self):
        return self._vtk_obj.GetNumberOfLevels()
    number_of_levels = traits.Property(_get_number_of_levels, help=\
        """
        Return the number of levels.
        \post result_greater_or_equal_to_one: result>=1
        """
    )

    def get_points_on_edge(self, *args):
        """
        V.get_points_on_edge(HyperOctreeCursor, int, int, int, int,
            HyperOctreePointsGrabber)
        C++: void GetPointsOnEdge(HyperOctreeCursor *sibling,
            int level, int axis, int k, int j,
            HyperOctreePointsGrabber *grabber)
        Get the points of node `sibling' on its edge `axis','k','j'. If
        axis==0, the edge is X-aligned and k gives the z coordinate and j
        the y-coordinate. If axis==1, the edge is Y-aligned and k gives
        the x coordinate and j the z coordinate. If axis==2, the edge is
        Z-aligned and k gives the y coordinate and j the x coordinate.
        \pre sibling_exists: sibling!=0
        \pre sibling_3d: sibling->_get_dimension()==_3
        \pre sibling_not_leaf: !sibling->_current_is_leaf()
        \pre valid_axis: axis>=0 && axis<3
        \pre valid_k: k>=0 && k<=1
        \pre valid_j: j>=0 && j<=1
        \pre valid_level_not_leaf: level>=0
            level<(this->_input->_get_number_of_levels()-_1)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPointsOnEdge, *my_args)
        return ret

    def get_points_on_edge2d(self, *args):
        """
        V.get_points_on_edge2d(HyperOctreeCursor, int, int,
            HyperOctreePointsGrabber)
        C++: void GetPointsOnEdge2D(HyperOctreeCursor *sibling,
            int edge, int level, HyperOctreePointsGrabber *grabber)
        Get the points of node `sibling' on its edge `edge'.
        \pre sibling_exists: sibling!=0
        \pre sibling_not_leaf: !sibling->_current_is_leaf()
        \pre sibling_2d: sibling->_get_dimension()==_2
        \pre valid_edge: edge>=0 && edge<4
        \pre valid_level_not_leaf: level>=0
            level<(this->_input->_get_number_of_levels()-_1)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPointsOnEdge2D, *my_args)
        return ret

    def get_points_on_face(self, *args):
        """
        V.get_points_on_face(HyperOctreeCursor, int, int,
            HyperOctreePointsGrabber)
        C++: void GetPointsOnFace(HyperOctreeCursor *sibling, int face,
             int level, HyperOctreePointsGrabber *grabber)
        Get the points of node `sibling' on its face `face'.
        \pre sibling_exists: sibling!=0
        \pre sibling_not_leaf: !sibling->_current_is_leaf()
        \pre sibling_3d: sibling->_get_dimension()==_3
        \pre valid_face: face>=0 && face<6
        \pre valid_level_not_leaf: level>=0
            level<(this->_get_number_of_levels()-_1)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPointsOnFace, *my_args)
        return ret

    def get_points_on_parent_edge(self, *args):
        """
        V.get_points_on_parent_edge(HyperOctreeCursor, int, int, int, int,
            HyperOctreePointsGrabber)
        C++: void GetPointsOnParentEdge(HyperOctreeCursor *cursor,
            int level, int axis, int k, int j,
            HyperOctreePointsGrabber *grabber)
        Get the points of the parent node of `cursor' on its edge
        `axis','k','j' at level `level' or deeper. If axis==0, the edge
        is X-aligned and k gives the z coordinate and j the y-coordinate.
        If axis==1, the edge is Y-aligned and k gives the x coordinate
        and j the z coordinate. If axis==2, the edge is Z-aligned and k
        gives the y coordinate and j the x coordinate.
        \pre cursor_exists: cursor!=0
        \pre cursor_3d: cursor->_get_dimension()==_3
        \pre valid_level: level>=0
        \pre valid_range_axis: axis>=0 && axis<3
        \pre valid_range_k: k>=0 && k<=1
        \pre valid_range_j: j>=0 && j<=1
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPointsOnParentEdge, *my_args)
        return ret

    def get_points_on_parent_edge2d(self, *args):
        """
        V.get_points_on_parent_edge2d(HyperOctreeCursor, int, int,
            HyperOctreePointsGrabber)
        C++: void GetPointsOnParentEdge2D(HyperOctreeCursor *cursor,
            int edge, int level, HyperOctreePointsGrabber *grabber)
        Get the points of the parent node of `cursor' on its edge `edge'
        at level `level' or deeper. (edge=0 for -X, 1 for +X, 2 for -Y, 3
        for +Y)
        \pre cursor_exists: cursor!=0
        \pre cursor_2d: cursor->_get_dimension()==_2
        \pre valid_level: level>=0
        \pre valid_edge: edge>=0 && edge<4
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPointsOnParentEdge2D, *my_args)
        return ret

    def get_points_on_parent_faces(self, *args):
        """
        V.get_points_on_parent_faces([int, int, int], int,
            HyperOctreeCursor, HyperOctreePointsGrabber)
        C++: void GetPointsOnParentFaces(int faces[3], int level,
            HyperOctreeCursor *cursor,
            HyperOctreePointsGrabber *grabber)
        Get the points of the parent node of `cursor' on its faces
        `faces' at level `level' or deeper.
        \pre cursor_exists: cursor!=0
        \pre cursor_3d: cursor->_get_dimension()==_3
        \pre valid_level: level>=0
        \pre boolean_faces: (faces[0]==0 || faces[0]==1) && (faces[1]==0
            || faces[1]==1) && (faces[2]==0 || faces[2]==1)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPointsOnParentFaces, *my_args)
        return ret

    def collapse_terminal_node(self, *args):
        """
        V.collapse_terminal_node(HyperOctreeCursor)
        C++: void CollapseTerminalNode(HyperOctreeCursor *node)
        Collapse a node for which all children are leaves. At the end,
        cursor points on the leaf that used to be a node.
        \pre node_exists: node!=0
        \pre node_is_node: !node->_current_is_leaf()
        \pre children_are_leaves: node->_current_is_terminal_node()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CollapseTerminalNode, *my_args)
        return ret

    def DIMENSION(self):
        """
        V.dimension() -> InformationIntegerKey
        C++: static InformationIntegerKey *DIMENSION()"""
        ret = wrap_vtk(self._vtk_obj.DIMENSION())
        return ret
        

    def LEVELS(self):
        """
        V.levels() -> InformationIntegerKey
        C++: static InformationIntegerKey *LEVELS()"""
        ret = wrap_vtk(self._vtk_obj.LEVELS())
        return ret
        

    def new_cell_cursor(self):
        """
        V.new_cell_cursor() -> HyperOctreeCursor
        C++: HyperOctreeCursor *NewCellCursor()
        Create a new cursor: an object that can traverse the cell of an
        hyperoctree.
        \post result_exists: result!=0
        """
        ret = wrap_vtk(self._vtk_obj.NewCellCursor())
        return ret
        

    def SIZES(self):
        """
        V.sizes() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *SIZES()"""
        ret = wrap_vtk(self._vtk_obj.SIZES())
        return ret
        

    def subdivide_leaf(self, *args):
        """
        V.subdivide_leaf(HyperOctreeCursor)
        C++: void SubdivideLeaf(HyperOctreeCursor *leaf)
        Subdivide node pointed by cursor, only if its a leaf. At the end,
        cursor points on the node that used to be leaf.
        \pre leaf_exists: leaf!=0
        \pre is_a_leaf: leaf->_current_is_leaf()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SubdivideLeaf, *my_args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('whole_bounding_box',
    'GetWholeBoundingBox'), ('request_exact_extent',
    'GetRequestExactExtent'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('update_number_of_pieces',
    'GetUpdateNumberOfPieces'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('update_ghost_level',
    'GetUpdateGhostLevel'), ('debug', 'GetDebug'), ('update_extent',
    'GetUpdateExtent'), ('dual_grid_flag', 'GetDualGridFlag'),
    ('update_piece', 'GetUpdatePiece'), ('release_data_flag',
    'GetReleaseDataFlag'), ('global_release_data_flag',
    'GetGlobalReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('whole_extent', 'GetWholeExtent'), ('dimension', 'GetDimension'),
    ('size', 'GetSize'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent', 'dimension',
    'dual_grid_flag', 'maximum_number_of_pieces', 'origin', 'size',
    'update_extent', 'update_ghost_level', 'update_number_of_pieces',
    'update_piece', 'whole_bounding_box', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperOctree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperOctree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['dimension', 'dual_grid_flag', 'maximum_number_of_pieces',
            'origin', 'size', 'update_extent', 'update_ghost_level',
            'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
            'whole_extent']),
            title='Edit HyperOctree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperOctree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

