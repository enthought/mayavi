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

from tvtk.tvtk_classes.scalar_tree import ScalarTree


class SimpleScalarTree(ScalarTree):
    """
    SimpleScalarTree - organize data according to scalar values (used
    to accelerate contouring operations)
    
    Superclass: ScalarTree
    
    SimpleScalarTree creates a pointerless binary tree that helps
    search for cells that lie within a particular scalar range. This
    object is used to accelerate some contouring (and other scalar-based
    techniques).
    
    The tree consists of an array of (min,max) scalar range pairs per
    node in the tree. The (min,max) range is determined from looking at
    the range of the children of the tree node. If the node is a leaf,
    then the range is determined by scanning the range of scalar data in
    n cells in the dataset. The n cells are determined by arbitrary
    selecting cell ids from id(i) to id(i+n), and where n is specified
    using the branching_factor ivar. Note that leaf node i=0 contains the
    scalar range computed from cell ids (0,n-1); leaf node i=1 contains
    the range from cell ids (n,2n-1); and so on. The implication is that
    there are no direct lists of cell ids per leaf node, instead the cell
    ids are implicitly known.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSimpleScalarTree, obj, update, **traits)
    
    max_level = traits.Trait(20, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the maximum allowable level for the tree.
        """
    )
    def _max_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxLevel,
                        self.max_level)

    branching_factor = traits.Trait(3, traits.Range(2, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the branching factor for the tree. This is the number of
        children per tree node. Smaller values (minimum is 2) mean deeper
        trees and more memory overhead. Larger values mean shallower
        trees, less memory usage, but worse performance.
        """
    )
    def _branching_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBranchingFactor,
                        self.branching_factor)

    def _get_level(self):
        return self._vtk_obj.GetLevel()
    level = traits.Property(_get_level, help=\
        """
        Get the level of the scalar tree. This value may change each time
        the scalar tree is built and the branching factor changes.
        """
    )

    _updateable_traits_ = \
    (('max_level', 'GetMaxLevel'), ('reference_count',
    'GetReferenceCount'), ('branching_factor', 'GetBranchingFactor'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'branching_factor', 'max_level'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SimpleScalarTree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit SimpleScalarTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['branching_factor', 'max_level']),
            title='Edit SimpleScalarTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SimpleScalarTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

