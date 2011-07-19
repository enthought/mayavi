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


class IncrementalOctreeNode(Object):
    """
    IncrementalOctreeNode - Octree node constituting incremental
    
    Superclass: Object
    
    Octree nodes serve as spatial sub-division primitives to build the
    search
     structure of an incremental octree in a recursive top-down manner.
    The
     hierarchy takes the form of a tree-like representation by which a
    parent
     node contains eight mutually non-overlapping child nodes. Each child
    is
     assigned with an axis-aligned rectangular volume (Spatial Bounding
    Box)
     and the eight children together cover exactly the same region as
    governed
     by their parent. The eight child nodes / octants are ordered as
    
    
     { (x_b_box_min, x_b_box_mid] & (y_b_box_min, y_b_box_mid] & (z_b_box_min, z_b_box_mid]
    },
     { (x_b_box_mid, x_b_box_max] & (y_b_box_min, y_b_box_mid] & (z_b_box_min, z_b_box_mid]
    },
     { (x_b_box_min, x_b_box_mid] & (y_b_box_mid, y_b_box_max] & (z_b_box_min, z_b_box_mid]
    },
     { (x_b_box_mid, x_b_box_max] & (y_b_box_mid, y_b_box_max] & (z_b_box_min, z_b_box_mid]
    },
     { (x_b_box_min, x_b_box_mid] & (y_b_box_min, y_b_box_mid] & (z_b_box_mid, z_b_box_max]
    },
     { (x_b_box_mid, x_b_box_max] & (y_b_box_min, y_b_box_mid] & (z_b_box_mid, z_b_box_max]
    },
     { (x_b_box_min, x_b_box_mid] & (y_b_box_mid, y_b_box_max] & (z_b_box_mid, z_b_box_max]
    },
     { (x_b_box_mid, x_b_box_max] & (y_b_box_mid, y_b_box_max] & (z_b_box_mid, z_b_box_max]
    },
    
    
     where { xrange & y_range & z_range } defines the region of each 3d
    octant.
     In addition, the points falling within and registered, by means of
    point
     indices, in the parent node are distributed to the child nodes for
    delegated
     maintenance. In fact, only leaf nodes, i.e., those without any
    descendants,
     actually store point indices while each node, regardless of a leaf
    or non-
     leaf node, keeps a dynamically updated Data Bounding Box of the
    inhabitant
     points, if any. Given a maximum number of points per leaf node, an
    octree
     is initialized with an empty leaf node that is then recursively
    sub-divided,
     but only on demand as points are incrementally inserted, to
    construct a
     populated tree.
    
    
     Please note that this octree node class is able to handle a large
    number
     of EXACTLY duplicate points that is greater than the specified
    maximum
     number of points per leaf node. In other words, as an exception, a
    leaf
     node may maintain an arbitrary number of exactly duplicate points to
    deal
     with possible extreme cases.
    
    See Also:
    
    
     IncrementalOctreePointLocator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIncrementalOctreeNode, obj, update, **traits)
    
    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6])
        Get the spatial bounding box of the node. The values are returned
        via an array in order of: x_min, x_max, y_min, y_max, z_min,
        z_max.
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def set_bounds(self, *args):
        """
        V.set_bounds(float, float, float, float, float, float)
        C++: void SetBounds(double x1, double x2, double y1, double y2,
            double z1, double z2)
        Set the spatial bounding box of the node. This function sets a
        default data bounding box.
        """
        ret = self._wrap_call(self._vtk_obj.SetBounds, *args)
        return ret

    def get_child(self, *args):
        """
        V.get_child(int) -> IncrementalOctreeNode
        C++: IncrementalOctreeNode *GetChild(int i)
        Get quick access to a child of this node. Note that this node is
        assumed to be a non-leaf one and no checking is performed on the
        node type.
        """
        ret = self._wrap_call(self._vtk_obj.GetChild, *args)
        return wrap_vtk(ret)

    def get_child_index(self, *args):
        """
        V.get_child_index((float, float, float)) -> int
        C++: int GetChildIndex(const double point[3])
        Determine which specific child / octant contains a given point.
        Note that the point is assumed to be inside this node and no
        checking is performed on the inside issue.
        """
        ret = self._wrap_call(self._vtk_obj.GetChildIndex, *args)
        return ret

    def get_distance2_to_boundary(self, *args):
        """
        V.get_distance2_to_boundary((float, float, float),
            IncrementalOctreeNode, int) -> float
        C++: double GetDistance2ToBoundary(const double point[3],
            IncrementalOctreeNode *rootNode, int checkData)
        V.get_distance2_to_boundary((float, float, float), [float, float,
            float], IncrementalOctreeNode, int) -> float
        C++: double GetDistance2ToBoundary(const double point[3],
            double closest[3], IncrementalOctreeNode *rootNode,
            int checkData)
        Compute the minimum squared distance from a point to this node,
        with all six boundaries considered. The data bounding box is
        checked if check_data is non-zero.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDistance2ToBoundary, *my_args)
        return ret

    def get_distance2_to_inner_boundary(self, *args):
        """
        V.get_distance2_to_inner_boundary((float, float, float),
            IncrementalOctreeNode) -> float
        C++: double GetDistance2ToInnerBoundary(const double point[3],
            IncrementalOctreeNode *rootNode)
        Given a point inside this node, get the minimum squared distance
        to all inner boundaries. An inner boundary is a node's face that
        is shared by another non-root node.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDistance2ToInnerBoundary, *my_args)
        return ret

    def _get_max_bounds(self):
        return self._vtk_obj.GetMaxBounds()
    max_bounds = traits.Property(_get_max_bounds, help=\
        """
        
        """
    )

    def _get_min_bounds(self):
        return self._vtk_obj.GetMinBounds()
    min_bounds = traits.Property(_get_min_bounds, help=\
        """
        
        """
    )

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Get the number of points inside or under this node.
        """
    )

    def _get_point_id_set(self):
        return wrap_vtk(self._vtk_obj.GetPointIdSet())
    point_id_set = traits.Property(_get_point_id_set, help=\
        """
        Get the list of point indices, NULL for a non-leaf node.
        """
    )

    def contains_point(self, *args):
        """
        V.contains_point((float, float, float)) -> int
        C++: int ContainsPoint(const double pnt[3])
        A point is in a node if and only if min_bounds[i] < p[i] <=
        max_bounds[i], which allows a node to be divided into eight
        non-overlapping children.
        """
        ret = self._wrap_call(self._vtk_obj.ContainsPoint, *args)
        return ret

    def contains_point_by_data(self, *args):
        """
        V.contains_point_by_data((float, float, float)) -> int
        C++: int ContainsPointByData(const double pnt[3])
        A point is in a node, in terms of data, if and only if
        min_data_bounds[i] <= p[i] <= max_data_bounds[i].
        """
        ret = self._wrap_call(self._vtk_obj.ContainsPointByData, *args)
        return ret

    def delete_child_nodes(self):
        """
        V.delete_child_nodes()
        C++: void DeleteChildNodes()
        Delete the eight child nodes.
        """
        ret = self._vtk_obj.DeleteChildNodes()
        return ret
        

    def export_all_point_ids_by_insertion(self, *args):
        """
        V.export_all_point_ids_by_insertion(IdList)
        C++: void ExportAllPointIdsByInsertion(IdList *idList)
        Export all the indices of the points (contained in or under this
        node) by inserting them to an allocated IdList via
        IdList::InsertNextId().
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.ExportAllPointIdsByInsertion, *my_args)
        return ret

    def is_leaf(self):
        """
        V.is_leaf() -> int
        C++: int IsLeaf()
        Determine whether or not this node is a leaf.
        """
        ret = self._vtk_obj.IsLeaf()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IncrementalOctreeNode, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit IncrementalOctreeNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit IncrementalOctreeNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IncrementalOctreeNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

