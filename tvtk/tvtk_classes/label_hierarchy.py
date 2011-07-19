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


class LabelHierarchy(PointSet):
    """
    LabelHierarchy - contains an octree of labels
    
    Superclass: PointSet
    
    This class represents labels in a hierarchy used to denote rendering
    priority. A binary tree of labels is maintained that subdivides the
    bounds of the of the label anchors spatially. Which level of the tree
    a label occupies determines its priority; those at higher levels of
    the tree will be more likely to render than those at lower levels of
    the tree.
    
    Pass LabelHierarchy objects to a LabelPlacementMapper filter
    for dynamic, non-overlapping, per-frame placement of labels.
    
    Note that if we have a d-dimensional binary tree and we want a fixed
    number $n $ of labels in each node (all nodes, not just leaves), we
    can compute the depth of tree required assuming a uniform
    distribution of points. Given a total of $N $ points we know
    that$\frac{N}{|T|} = n $, where $|T| $ is the cardinality of the tree
    (i.e., the number of nodes it contains). Because we have a uniform
    distribution, the tree will be uniformly subdivided and thus $|T| = 1
    + 2^d + \left(2^d\right)^2 + \cdots + \left(2^d\right)^k $, where $d $
    is the dimensionality of the input points (fixed at 3 for now). As $k $
    becomes large, $|T|\approx 2 \left(2^d\right)^k $. Using this
    approximation, we can solve for $k $:\[ k =
    \frac{\log{\frac{N}{2n}}}{\log{2^d}} \] Given a set of $N $ input
    label anchors, we'll compute $k $ and then bin the anchors into tree
    nodes at level $k $ of the tree. After this, all the nodes will be in
    the leaves of the tree and those leaves will be at the $k $-th level;
    no anchors will be in levels $1, 2, \ldots, k-1 $. To fix that, we'll
    choose to move some anchors upwards. The exact number to move upwards
    depends on target_label_count. We'll move as many up as required to
    have target_label_count at each node.
    
    You should avoid situations where maximum_depth does not allow
    for_target_label_count or fewer entries at each node. The maximum_depth
    is a hard limit while target_label_count is a suggested optimum. You
    will end up with many more than target_label_count entries per node and
    things will be sloooow.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabelHierarchy, obj, update, **traits)
    
    def _get_sizes(self):
        return wrap_vtk(self._vtk_obj.GetSizes())
    def _set_sizes(self, arg):
        old_val = self._get_sizes()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetSizes,
                        my_arg[0])
        self.trait_property_changed('sizes', old_val, arg)
    sizes = traits.Property(_get_sizes, _set_sizes, help=\
        """
        Set/get the array specifying the size of each label.
        """
    )

    maximum_depth = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        The maximum depth of the octree.
        """
    )
    def _maximum_depth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDepth,
                        self.maximum_depth)

    def _get_labels(self):
        return wrap_vtk(self._vtk_obj.GetLabels())
    def _set_labels(self, arg):
        old_val = self._get_labels()
        my_arg = deref_array([arg], [['vtkAbstractArray']])
        self._wrap_call(self._vtk_obj.SetLabels,
                        my_arg[0])
        self.trait_property_changed('labels', old_val, arg)
    labels = traits.Property(_get_labels, _set_labels, help=\
        """
        Set/get the array specifying the text of each label.
        """
    )

    def _get_priorities(self):
        return wrap_vtk(self._vtk_obj.GetPriorities())
    def _set_priorities(self, arg):
        old_val = self._get_priorities()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetPriorities,
                        my_arg[0])
        self.trait_property_changed('priorities', old_val, arg)
    priorities = traits.Property(_get_priorities, _set_priorities, help=\
        """
        Set/get the array specifying the importance (priority) of each
        label.
        """
    )

    def _get_icon_indices(self):
        return wrap_vtk(self._vtk_obj.GetIconIndices())
    def _set_icon_indices(self, arg):
        old_val = self._get_icon_indices()
        my_arg = deref_array([arg], [['vtkIntArray']])
        self._wrap_call(self._vtk_obj.SetIconIndices,
                        my_arg[0])
        self.trait_property_changed('icon_indices', old_val, arg)
    icon_indices = traits.Property(_get_icon_indices, _set_icon_indices, help=\
        """
        Set/get the array specifying the icon index of each label.
        """
    )

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    def _set_text_property(self, arg):
        old_val = self._get_text_property()
        self._wrap_call(self._vtk_obj.SetTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('text_property', old_val, arg)
    text_property = traits.Property(_get_text_property, _set_text_property, help=\
        """
        The default text property assigned to labels in this hierarchy.
        """
    )

    def _get_orientations(self):
        return wrap_vtk(self._vtk_obj.GetOrientations())
    def _set_orientations(self, arg):
        old_val = self._get_orientations()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetOrientations,
                        my_arg[0])
        self.trait_property_changed('orientations', old_val, arg)
    orientations = traits.Property(_get_orientations, _set_orientations, help=\
        """
        Set/get the array specifying the orientation of each label.
        """
    )

    def _get_bounded_sizes(self):
        return wrap_vtk(self._vtk_obj.GetBoundedSizes())
    def _set_bounded_sizes(self, arg):
        old_val = self._get_bounded_sizes()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetBoundedSizes,
                        my_arg[0])
        self.trait_property_changed('bounded_sizes', old_val, arg)
    bounded_sizes = traits.Property(_get_bounded_sizes, _set_bounded_sizes, help=\
        """
        Set/get the array specifying the maximum width and height in
        world coordinates of each label.
        """
    )

    target_label_count = traits.Int(16, enter_set=True, auto_set=False, help=\
        """
        The number of labels that is ideally present at any octree node.
        It is best if this is a multiple of $2^d $.
        """
    )
    def _target_label_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetLabelCount,
                        self.target_label_count)

    def _get_center_pts(self):
        return wrap_vtk(self._vtk_obj.GetCenterPts())
    center_pts = traits.Property(_get_center_pts, help=\
        """
        Provide access to original coordinates of sets of coincident
        points
        """
    )

    def _get_coincident_points(self):
        return wrap_vtk(self._vtk_obj.GetCoincidentPoints())
    coincident_points = traits.Property(_get_coincident_points, help=\
        """
        Provide access to the set of coincident points that have been
        perturbed by the hierarchy in order to render labels for each
        without overlap.
        """
    )

    def get_discrete_node_coordinates_from_world_point(self, *args):
        """
        V.get_discrete_node_coordinates_from_world_point([int, int, int],
            [float, float, float], int)
        C++: void GetDiscreteNodeCoordinatesFromWorldPoint(int ijk[3],
            double pt[3], int level)
        Given a depth in the hierarchy ( level) and a point pt in world
        space, compute ijk. This is used to find other octree nodes at
        the same level that are within the search radius for candidate
        labels to be placed. It is called with pt set to the camera eye
        point and pythagorean quadruples increasingly distant from the
        origin are added to ijk to identify octree nodes whose labels
        should be placed.
        @param[out] ijk - discrete coordinates of the octree node at
            level containing pt.
        @param[in]  pt - input world point coordinates
        @param[in]  level - input octree level to be considered
        """
        ret = self._wrap_call(self._vtk_obj.GetDiscreteNodeCoordinatesFromWorldPoint, *args)
        return ret

    def compute_hierarchy(self):
        """
        V.compute_hierarchy()
        C++: virtual void ComputeHierarchy()
        Fill the hierarchy with the input labels.
        """
        ret = self._vtk_obj.ComputeHierarchy()
        return ret
        

    def new_iterator(self, *args):
        """
        V.new_iterator(int, Renderer, Camera, [float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float], bool, [float, float])
            -> LabelHierarchyIterator
        C++: LabelHierarchyIterator *NewIterator(int type,
            Renderer *ren, Camera *cam, double frustumPlanes[24],
            bool positionsAsNormals, float bucketSize[2])
        Returns an iterator for this data object. positions_as_normals
        should only be true when labels are on a sphere centered at the
        origin (_3d world).
        @param type - the type should be one of FULL_SORT, QUEUE,
            DEPTH_FIRST, or FRUSTUM.
        @param ren - the current renderer (used for viewport information)
        @param cam - the current camera.
        @param frustum_planes - should be the output of the camera's
            frustum planes.
        @param positions_as_normals - throws out octree nodes on the
            opposite side of the origin.
        @param bucket_size - an array of 2 integers describing the width
            and height of label placer buckets.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.NewIterator, *my_args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('whole_bounding_box', 'GetWholeBoundingBox'), ('update_piece',
    'GetUpdatePiece'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('whole_extent', 'GetWholeExtent'),
    ('update_number_of_pieces', 'GetUpdateNumberOfPieces'),
    ('update_ghost_level', 'GetUpdateGhostLevel'), ('target_label_count',
    'GetTargetLabelCount'), ('update_extent', 'GetUpdateExtent'),
    ('debug', 'GetDebug'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('global_release_data_flag', 'GetGlobalReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('maximum_depth',
    'GetMaximumDepth'), ('maximum_number_of_pieces',
    'GetMaximumNumberOfPieces'), ('request_exact_extent',
    'GetRequestExactExtent'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'release_data_flag', 'request_exact_extent', 'maximum_depth',
    'maximum_number_of_pieces', 'target_label_count', 'update_extent',
    'update_ghost_level', 'update_number_of_pieces', 'update_piece',
    'whole_bounding_box', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabelHierarchy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit LabelHierarchy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['global_release_data_flag', 'request_exact_extent'],
            [], ['maximum_depth', 'maximum_number_of_pieces',
            'target_label_count', 'update_extent', 'update_ghost_level',
            'update_number_of_pieces', 'update_piece', 'whole_bounding_box',
            'whole_extent']),
            title='Edit LabelHierarchy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabelHierarchy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

