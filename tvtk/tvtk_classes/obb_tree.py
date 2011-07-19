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


class OBBTree(AbstractCellLocator):
    """
    OBBTree - generate oriented bounding box (OBB) tree
    
    Superclass: AbstractCellLocator
    
    OBBTree is an object to generate oriented bounding box (OBB)
    trees. An oriented bounding box is a bounding box that does not
    necessarily line up along coordinate axes. The OBB tree is a
    hierarchical tree structure of such boxes, where deeper levels of OBB
    confine smaller regions of space.
    
    To build the OBB, a recursive, top-down process is used. First, the
    root OBB is constructed by finding the mean and covariance matrix of
    the cells (and their points) that define the dataset. The
    eigenvectors of the covariance matrix are extracted, giving a set of
    three orthogonal vectors that define the tightest-fitting OBB. To
    create the two children OBB's, a split plane is found that
    (approximately) divides the number cells in half. These are then
    assigned to the children OBB's. This process then continues until the
    max_level ivar limits the recursion, or no split plane can be found.
    
    A good reference for OBB-trees is Gottschalk & Manocha in Proceedings
    of Siggraph `96.
    
    Caveats:
    
    Since this algorithms works from a list of cells, the OBB tree will
    only bound the "geometry" attached to the cells if the convex hull of
    the cells bounds the geometry.
    
    Long, skinny cells (i.e., cells with poor aspect ratio) may cause
    unsatisfactory results. This is due to the fact that this is a
    top-down implementation of the OBB tree, requiring that one or more
    complete cells are contained in each OBB. This requirement makes it
    hard to find good split planes during the recursion process. A
    bottom-up implementation would go a long way to correcting this
    problem.
    
    See Also:
    
    Locator CellLocator PointLocator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOBBTree, obj, update, **traits)
    
    def compute_obb(self, *args):
        """
        V.compute_obb(Points, [float, float, float], [float, float,
            float], [float, float, float], [float, float, float], [float,
            float, float])
        C++: static void ComputeOBB(Points *pts, double corner[3],
            double max[3], double mid[3], double min[3], double size[3])
        V.compute_obb(DataSet, [float, float, float], [float, float,
            float], [float, float, float], [float, float, float], [float,
            float, float])
        C++: void ComputeOBB(DataSet *input, double corner[3],
            double max[3], double mid[3], double min[3], double size[3])
        Compute an OBB from the list of points given. Return the corner
        point and the three axes defining the orientation of the OBB.
        Also return a sorted list of relative "sizes" of axes for
        comparison purposes.
        """
        my_args = deref_array(args, [('vtkPoints', ['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float']), ('vtkDataSet', ['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.ComputeOBB, *my_args)
        return ret

    def inside_or_outside(self, *args):
        """
        V.inside_or_outside((float, float, float)) -> int
        C++: int InsideOrOutside(const double point[3])
        Determine whether a point is inside or outside the data used to
        build this OBB tree.  The data must be a closed surface
        PolyData data set. The return value is +1 if outside, -1 if
        inside, and 0 if undecided.
        """
        ret = self._wrap_call(self._vtk_obj.InsideOrOutside, *args)
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
            return super(OBBTree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OBBTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['automatic', 'cache_cell_bounds', 'lazy_evaluation',
            'retain_cell_lists', 'use_existing_search_structure'], [],
            ['max_level', 'number_of_cells_per_node', 'tolerance']),
            title='Edit OBBTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OBBTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

