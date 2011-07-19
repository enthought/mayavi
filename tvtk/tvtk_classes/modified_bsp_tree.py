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

from tvtk.tvtk_classes.abstract_cell_locator import AbstractCellLocator


class ModifiedBSPTree(AbstractCellLocator):
    """
    ModifiedBSPTree - Generate axis aligned BBox tree for raycasting
    and other Locator based searches
    
    Superclass: AbstractCellLocator
    
    ModifiedBSPTree creates an evenly balanced BSP tree using a top
    down implementation. Axis aligned split planes are found which evenly
    divide cells into two buckets. Generally a split plane will intersect
    some cells and these are usually stored in both child nodes of the
    current parent. (Or split into separate cells which we cannot
    consider in this case). Storing cells in multiple buckets creates
    problems associated with multiple tests against rays and increases
    the required storage as complex meshes will have many cells
    straddling a split plane (and further splits may cause multiple
    copies of these).
    
    During a discussion with Arno Formella in 1998 he suggested using a
    third child node to store objects which straddle split planes. I've
    not seen this published (Yes! - see below), but thought it worth
    trying. This implementation of the BSP tree creates a third child
    node for storing cells lying across split planes, the third cell may
    overlap the other two, but the two 'proper' nodes otherwise conform
    to usual BSP rules.
    
    The advantage of this implementation is cells only ever lie in one
    node and mailbox testing is avoided. All BBoxes are axis aligned and
    a ray cast uses an efficient search strategy based on near/far nodes
    and rejects all BBoxes using simple tests.
    
    For fast raytracing, 6 copies of cell lists are stored in each leaf
    node each list is in axis sorted order +/- x,y,z and cells are always
    tested in the direction of the ray dominant axis. Once an
    intersection is found any cell or BBox with a closest point further
    than the I-point can be instantly rejected and raytracing stops as
    soon as no nodes can be closer than the current best intersection
    point.
    
    The addition of the 'middle' node upsets the optimal balance of the
    tree, but is a minor overhead during the raytrace. Each child node is
    contracted such that it tightly fits all cells inside it, enabling
    further ray/box rejections.
    
    This class is intented for persons requiring many ray tests and is
    optimized for this purpose. As no cell ever lies in more than one
    leaf node, and parent nodes do not maintain cell lists, the memory
    overhead of the sorted cell lists is 6*num_cells*4 for 6 lists of
    ints, each num_cells in length. The memory requirement of the nodes
    themselves is usually of minor significance.
    
    Subdividision is controlled by max_cells_per_node - any node with more
    than this number will be subdivided providing a good split plane can
    be found and the max depth is not exceeded.
    
    The average cells per leaf will usually be around half the
    max_cells_per_node, though the middle node is usually sparsely populated
    and lowers the average slightly. The middle node will not be created
    when not needed. Subdividing down to very small cells per node is not
    generally suggested as then the 6 stored cell lists are effectively
    redundant.
    
    Values of maxcells_per_node of around 16->128 depending on dataset size
    will usually give good results.
    
    Cells are only sorted into 6 lists once - before tree creation, each
    node segments the lists and passes them down to the new child nodes
    whilst maintaining sorted order. This makes for an efficient
    subdivision strategy.
    
    NB. The following reference has been sent to me 
    @Article{formella-1995-ray,
        author =     "Arno Formella and Christian Gill",
        title =      "{Ray Tracing: A Quantitative Analysis and a New
                      Practical Algorithm}",
        journal =    "{The Visual Computer}",
        year =       "{1995}",
        month =       dec,
        pages =      "{465--476}",
        volume =     "{11}",
        number =     "{9}",
        publisher =  "{Springer}",
        keywords =   "{ray tracing, space subdivision, plane traversal,
                       octree, clustering, benchmark scenes}",
        annote =     "{We present a new method to accelerate the process
    of
                       finding nearest ray--object intersections in ray
                       tracing. The algorithm consumes an amount of
    memory
                       more or less linear in the number of objects. The
    basic
                       ideas can be characterized with a modified
    BSP--tree
                       and plane traversal. Plane traversal is a fast
    linear
                       time algorithm to find the closest intersection
    point
                       in a list of bounding volumes hit by a ray. We use
                       plane traversal at every node of the high
    outdegree
                       BSP--tree. Our implementation is competitive to
    fast
                       ray tracing programs. We present a benchmark suite
                       which allows for an extensive comparison of ray
    tracing
                       algorithms.}",
      }
    
    Thanks:
    
    
     John Biddiscombe for developing and contributing this class
    
    to_do:
    
    ------------- Implement intersection heap for testing rays against
        transparent objects
    
    Style:
    
    -------------- This class is currently maintained by J. Biddiscombe
        who has specially requested that the code style not be modified
        to the kitware standard. Please respect the contribution of this
        class by keeping the style as close as possible to the author's
        original.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkModifiedBSPTree, obj, update, **traits)
    
    def _get_leaf_node_cell_information(self):
        return wrap_vtk(self._vtk_obj.GetLeafNodeCellInformation())
    leaf_node_cell_information = traits.Property(_get_leaf_node_cell_information, help=\
        """
        After subdivision has completed, one may wish to query the tree
        to find which cells are in which leaf nodes. This function
        returns a list which holds a cell Id list for each leaf node.
        """
    )

    def generate_representation_leafs(self, *args):
        """
        V.generate_representation_leafs(PolyData)
        C++: virtual void GenerateRepresentationLeafs(PolyData *pd)
        Generate BBox representation of all leaf nodes
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GenerateRepresentationLeafs, *my_args)
        return ret

    _updateable_traits_ = \
    (('use_existing_search_structure', 'GetUseExistingSearchStructure'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('max_level',
    'GetMaxLevel'), ('retain_cell_lists', 'GetRetainCellLists'), ('debug',
    'GetDebug'), ('automatic', 'GetAutomatic'), ('lazy_evaluation',
    'GetLazyEvaluation'), ('cache_cell_bounds', 'GetCacheCellBounds'),
    ('reference_count', 'GetReferenceCount'), ('number_of_cells_per_node',
    'GetNumberOfCellsPerNode'), ('tolerance', 'GetTolerance'))
    
    _full_traitnames_list_ = \
    (['automatic', 'cache_cell_bounds', 'debug', 'global_warning_display',
    'lazy_evaluation', 'retain_cell_lists',
    'use_existing_search_structure', 'max_level',
    'number_of_cells_per_node', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ModifiedBSPTree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ModifiedBSPTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic', 'cache_cell_bounds', 'lazy_evaluation',
            'retain_cell_lists', 'use_existing_search_structure'], [],
            ['max_level', 'number_of_cells_per_node', 'tolerance']),
            title='Edit ModifiedBSPTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ModifiedBSPTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

